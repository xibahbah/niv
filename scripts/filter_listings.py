#!/usr/bin/env python3
"""Filter downloaded public listing indexes. Output leads, never eligibility decisions."""
import argparse
import csv
import json
import re
import time
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

def canonical(url):
    p = urlsplit(url)
    query = [(k,v) for k,v in parse_qsl(p.query, keep_blank_values=True)
             if not k.lower().startswith("utm_") and k.lower() not in {"ref", "source"}]
    return urlunsplit((p.scheme.lower(), p.netloc.lower(), p.path.rstrip("/"), urlencode(sorted(query)), ""))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("listings", type=Path, nargs="+")
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--log", type=Path)
    parser.add_argument("--max-days", type=float)
    parser.add_argument("--output", type=Path, required=True)
    a = parser.parse_args()
    cfg = json.loads(a.config.read_text())
    seen = set()
    if a.log and a.log.exists():
        with a.log.open(newline="") as f:
            for row in csv.DictReader(f):
                u = row.get("apply_url") or row.get("source_url") or row.get("url")
                if u:
                    seen.add(canonical(u))
    output = []
    counts = {"input": 0, "inactive": 0, "old": 0, "title_filtered": 0, "duplicate": 0, "missing_url": 0}
    for filename in a.listings:
        rows = json.loads(filename.read_text())
        if not isinstance(rows, list):
            parser.error(str(filename) + ": expected a listing array")
        for job in rows:
            counts["input"] += 1
            if job.get("active") is False or job.get("is_visible") is False:
                counts["inactive"] += 1
                continue
            posted = job.get("date_posted")
            if a.max_days is not None and isinstance(posted, (float, int)) and time.time()-posted > a.max_days*86400:
                counts["old"] += 1
                continue
            title = str(job.get("title", "")).lower()
            targets = cfg.get("target_roles", [])
            excludes = cfg.get("excluded_title_keywords", [])
            if (targets and not any(t.lower() in title for t in targets)) or any(
                re.search(r"\b"+re.escape(t.lower())+r"\b", title) for t in excludes):
                counts["title_filtered"] += 1
                continue
            u = job.get("url") or job.get("apply_url")
            if not u:
                counts["missing_url"] += 1
                continue
            key = canonical(u)
            if key in seen:
                counts["duplicate"] += 1
                continue
            seen.add(key)
            output.append({"listing": job, "canonical_url": key, "source_file": filename.name,
                           "status": "lead", "requires_official_jd_review": True})
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps({"counts": counts, "leads": output}, indent=2)+"\n")
    print(json.dumps({"leads": len(output), "counts": counts}))

if __name__ == "__main__":
    main()
