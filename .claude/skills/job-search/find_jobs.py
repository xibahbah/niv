#!/usr/bin/env python3
"""ATS adapters adapted from Yodablues/claude-code-job-search (MIT).
See LICENSE and workflow/upstreams.json. Configuration is repository-relative.
"""
import argparse
import html
import json
import re
import time
import urllib.request
import urllib.parse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

PROFILE = {}
ERRORS = []
UA = {"User-Agent": "JobSearchWorkflow/1.0", "Accept": "application/json"}
TIMEOUT = 20
RETRIES = 2


def coarse_match(title, blob):
    title = title.lower()
    excluded = PROFILE.get("excluded_title_keywords", [])
    if any(re.search(r"\b" + re.escape(word.lower()) + r"\b", title) for word in excluded):
        return False
    roles = PROFILE.get("target_roles", [])
    return not roles or any(role.lower() in title for role in roles)


def rec(title, company, desc, url, source, location, salary_text=""):
    return {"title": title, "company": company, "location": location,
            "url": url, "source": source, "salary_text": salary_text,
            "description": strip_html(desc)}

def get(url):
    last = None
    for attempt in range(RETRIES):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=TIMEOUT) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001 - transient (rate limit / network); back off
            last = e
            time.sleep(1.5 * (attempt + 1))
    ERRORS.append({"url": url, "error": str(last)})
    raise last

def strip_html(s):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s or ""))).strip()

def from_remoteok():
    out = []
    try:
        data = json.loads(get("https://remoteok.com/api"))[1:]
    except Exception:
        return out
    for j in data:
        title = j.get("position", "")
        blob = strip_html(j.get("description", "")) + " " + " ".join(j.get("tags", []))
        if coarse_match(title, blob):
            out.append(rec(title, j.get("company", ""), blob,
                           j.get("url") or j.get("apply_url", ""), "RemoteOK",
                           j.get("location") or "Remote"))
    return out

def from_remotive():
    out = []
    try:
        data = json.loads(get("https://remotive.com/api/remote-jobs?limit=100"))
    except Exception:
        return out
    for j in data.get("jobs", []):
        title = j.get("title", "")
        blob = strip_html(j.get("description", "")) + " " + " ".join(j.get("tags", []))
        if coarse_match(title, blob):
            out.append(rec(title, j.get("company_name", ""), blob, j.get("url", ""),
                           "Remotive", j.get("candidate_required_location", ""),
                           j.get("salary", "")))
    return out

def from_greenhouse(token):
    out = []
    try:
        data = json.loads(get(f"https://boards-api.greenhouse.io/v1/boards/{token}/jobs?content=true"))
    except Exception:
        return out
    for j in data.get("jobs", []):
        title = j.get("title", "")
        loc = (j.get("location") or {}).get("name", "")
        content = strip_html(urllib.parse.unquote(j.get("content", "")))
        if (not PROFILE["remote_only"] or "remote" in loc.lower()) and coarse_match(title, content):
            out.append(rec(title, token.title(), content, j.get("absolute_url", ""),
                           "Greenhouse", loc))
    return out

def from_ashby(name):
    out = []
    try:
        data = json.loads(get("https://api.ashbyhq.com/posting-api/job-board/"
                              + urllib.parse.quote(name) + "?includeCompensation=true"))
    except Exception:
        return out
    for j in data.get("jobs", []):
        title = j.get("title", "")
        loc = j.get("location") or ""
        if PROFILE["remote_only"] and not (j.get("isRemote") or "remote" in loc.lower()):
            continue
        desc = j.get("descriptionPlain") or strip_html(j.get("descriptionHtml", ""))
        if coarse_match(title, desc):
            out.append(rec(title, name, desc, j.get("applyUrl") or j.get("jobUrl", ""),
                           "Ashby", loc, json.dumps(j.get("compensation") or {})))
    return out

def from_lever(token):
    out = []
    try:
        data = json.loads(get(f"https://api.lever.co/v0/postings/{token}?mode=json"))
    except Exception:
        return out
    for j in data:
        title = j.get("text", "")
        cats = j.get("categories") or {}
        loc = cats.get("location", "")
        sections = [j.get("descriptionPlain") or strip_html(j.get("description", ""))]
        for section in j.get("lists", []):
            sections.extend([section.get("text", ""), strip_html(section.get("content", ""))])
        sections.append(j.get("additionalPlain") or strip_html(j.get("additional", "")))
        desc = "\n".join(part for part in sections if part)
        if (not PROFILE["remote_only"] or "remote" in loc.lower()) and coarse_match(title, desc):
            out.append(rec(title, token.title(), desc, j.get("hostedUrl", ""),
                           "Lever", loc, json.dumps(j.get("salaryRange") or {})))
    return out

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    PROFILE.update(json.loads(Path(args.config).read_text()))
    PROFILE.setdefault("remote_only", False)
    sources = PROFILE["sources"]
    jobs = []
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = []
        for name, adapter in [("greenhouse", from_greenhouse), ("ashby", from_ashby), ("lever", from_lever)]:
            futures.extend(pool.submit(adapter, token) for token in dict.fromkeys(sources.get(name, [])))
        for name, adapter in [("remoteok", from_remoteok), ("remotive", from_remotive)]:
            if sources.get(name, False):
                futures.append(pool.submit(adapter))
        for future in as_completed(futures):
            try:
                jobs.extend(future.result())
            except Exception as exc:
                ERRORS.append({"error": str(exc), "stage": "parse-source"})
    unique = {}
    for job in jobs:
        if job["url"]:
            unique.setdefault(job["url"], job)
    result = {"candidates": sorted(unique.values(), key=lambda j: (j["company"], j["title"])),
              "source_errors": ERRORS}
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    temp = output.with_suffix(output.suffix + ".tmp")
    temp.write_text(json.dumps(result, indent=2))
    temp.replace(output)
    print(f"Collected {len(unique)} candidates; {len(ERRORS)} source errors; {output}")


if __name__ == "__main__":
    main()

