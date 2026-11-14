#!/usr/bin/env python3
"""Export only release-manifest files after checking exact reviewed hashes."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = {"OWNER.md", "workflow/profile.json", "workflow/daily-policy.json", "workflow/LATEST.md"}
PRIVATE_DIRS = {"assets", "applications", "scans", "logs", "outreach", "build", ".git"}

def checked_files(root):
    entries = json.loads((root / "release-manifest.json").read_text())["files"]
    result = []
    seen = set()
    for entry in entries:
        name = entry["path"]
        rel = Path(name)
        if rel.is_absolute() or ".." in rel.parts or name in seen:
            raise ValueError("Unsafe or duplicate manifest path")
        if name in PRIVATE or rel.parts[0] in PRIVATE_DIRS:
            raise ValueError("Private path in release manifest: " + name)
        seen.add(name)
        path = root / rel
        if any(p.is_symlink() for p in [path, *path.parents] if p != root.parent):
            raise ValueError("Symlink rejected: " + name)
        if not path.is_file():
            raise ValueError("Missing file: " + name)
        if hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
            raise ValueError("Changed file needs a fresh privacy review: " + name)
        result.append((name, path))
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    destination = args.destination.resolve()
    if destination.exists():
        parser.error("Choose a new destination directory.")
    files = checked_files(ROOT)
    destination.mkdir(parents=True)
    for name, source in files:
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    shutil.copyfile(ROOT / "release-manifest.json", destination / "release-manifest.json")
    print(json.dumps({"exported_files": len(files) + 1, "destination": str(destination),
                      "history_copied": False}))

if __name__ == "__main__":
    main()
