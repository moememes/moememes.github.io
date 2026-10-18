#!/usr/bin/env python3
"""Prepare a separate GitHub Pages blog repository from this site's source."""
import shutil
import subprocess
import sys
from pathlib import Path

source = Path(__file__).resolve().parent.parent
if len(sys.argv) != 2:
    raise SystemExit("Usage: python3 scripts/export-blog.py /path/to/empty/blog-checkout")
destination = Path(sys.argv[1]).resolve()
if destination == source or source in destination.parents:
    raise SystemExit("Choose a destination outside the source repository.")
destination.mkdir(parents=True, exist_ok=True)
if any(p.name != ".git" for p in destination.iterdir()):
    raise SystemExit("Destination must be empty apart from its .git directory.")
files = subprocess.check_output(
    ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
    cwd=source,
).decode().split("\0")
for name in filter(None, files):
    if name.startswith(("scripts/", ".github/")) or name == "DOMAIN_SETUP.md":
        continue
    original = source / name
    if not original.is_file():
        continue
    target = destination / name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(original, target)
config = (source / "_config.yml").read_text().replace(
    'url:         "https://memes.moe"', 'url:         "https://blog.memes.moe"'
)
(destination / "_config.yml").write_text(config + "\npaginate: 4\npaginate_path: /page:num/\n")
(destination / "index.html").write_text(
    "---\nlayout: default\n---\n{% include blog.html %}\n"
)
(destination / "CNAME").write_text("blog.memes.moe\n")
print(f"Blog source prepared at {destination}")
