#!/usr/bin/env python3
"""Validate manifest structure and local evidence paths, not factual eligibility."""
import argparse
import json
from pathlib import Path

STATES = {"ready", "conditional", "hold", "excluded", "closed", "duplicate"}
def validate(data, root):
    errors = []
    jobs = data.get("jobs", [])
    if not isinstance(jobs, list):
        return ["jobs must be a list"]
    seen = set()
    counts = {s: 0 for s in STATES}
    def exists(name):
        if not isinstance(name, str) or not name:
            return False
        rel = Path(name)
        if rel.is_absolute() or ".." in rel.parts:
            return False
        p = root / rel
        return p.is_file() and root.resolve() in p.resolve().parents
    for index, job in enumerate(jobs):
        key = job.get("job_id")
        prefix = str(key or index)
        if not key or key in seen:
            errors.append(prefix + ": missing or duplicate job_id")
        seen.add(key)
        state = job.get("status")
        if state not in STATES:
            errors.append(prefix + ": unknown status")
            continue
        counts[state] += 1
        if not job.get("official_url") or not job.get("retrieved_at"):
            errors.append(prefix + ": missing source URL or retrieval time")
        if not exists(job.get("review_path")):
            errors.append(prefix + ": missing review file")
        if state == "ready":
            if job.get("unresolved"):
                errors.append(prefix + ": ready role has unresolved conditions")
            for field in ("jd_path", "task_path", "resume_pdf"):
                if not exists(job.get(field)):
                    errors.append(prefix + ": missing " + field)
            if job.get("eligibility_resolved") is not True or job.get("pdf_inspected") is not True:
                errors.append(prefix + ": ready role lacks completed checks")
        if state == "excluded" and not job.get("reason"):
            errors.append(prefix + ": exclusion needs a reason")
    if data.get("counts") != {"reviewed": len(jobs), **dict(sorted(counts.items()))}:
        errors.append("Counts differ from manifest records")
    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(json.loads(args.manifest.read_text()), args.root)
    print(json.dumps({"valid_structure": not errors, "errors": errors,
                      "note": "This does not verify facts, approval, or browser submission."}, indent=2))
    raise SystemExit(bool(errors))

if __name__ == "__main__":
    main()
