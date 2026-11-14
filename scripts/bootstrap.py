#!/usr/bin/env python3
"""Create missing private working files. Never overwrite existing answers."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    pairs = {
        "workflow/OWNER.example.md": "OWNER.md",
        "workflow/profile.example.json": "workflow/profile.json",
        "workflow/daily-policy.example.json": "workflow/daily-policy.json",
        "workflow/LATEST.example.md": "workflow/LATEST.md",
    }
    created = []
    for source, target in pairs.items():
        p = ROOT / target
        if not p.exists():
            p.parent.mkdir(parents=True, exist_ok=True)
            with p.open("x") as f:
                f.write((ROOT / source).read_text())
            created.append(target)
    for folder in ("assets", "applications", "scans", "logs/grok", "outreach/records", "workflow/runs"):
        (ROOT / folder).mkdir(parents=True, exist_ok=True)
    log = ROOT / "applications/log.csv"
    if not log.exists():
        with log.open("x", newline="") as f:
            csv.writer(f).writerow(["job_id", "company", "role", "apply_url", "status", "submitted_at", "confirmation_path", "worker"])
        created.append("applications/log.csv")
    print(json.dumps({"created": created, "next": "Complete ONBOARDING.md. No submissions are authorized by this template."}, indent=2))

if __name__ == "__main__":
    main()
