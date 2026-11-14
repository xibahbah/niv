#!/usr/bin/env python3
"""Read-only capability inventory. No network, setup, or credential output."""
import json
import shutil
from pathlib import Path

root = Path(__file__).resolve().parents[1]
commands = ("python3", "git", "gh", "agent-reach", "pdflatex", "xelatex", "pdftoppm")
result = {
    "commands_present": {name: bool(shutil.which(name)) for name in commands},
    "working_files_present": {name: (root / name).is_file() for name in (
        "OWNER.md", "workflow/profile.json", "workflow/daily-policy.json", "workflow/LATEST.md")},
    "not_verified": ["network access", "GitHub authentication", "cloud execution", "selected model",
                     "browser access", "live ATS access", "LinkedIn channel", "submission authorization"],
}
print(json.dumps(result, indent=2))
