"""Inspect Bricks page 524 structure."""
import json
import shutil
import datetime
from collections import Counter

RAW = r"C:\Users\Willb\Claude\CFC\bricks_raw.json"

# Timestamped backup
ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_path = rf"C:\Users\Willb\Claude\CFC\bricks_backup_524_{ts}.json"
shutil.copy(RAW, backup_path)
print(f"Backup saved: {backup_path}")
print()

d = json.load(open(RAW))
content = d["content"]
by_id = {e["id"]: e for e in content}

# Root elements (parent=0)
roots = [e for e in content if e.get("parent") == 0]
print(f"Root elements: {len(roots)}")
for r in roots:
    print(f"  {r['id']} {r['name']} label={r.get('label','')!r}")
print()

# All headings in DOM order
print("=== Headings in order ===")
for e in content:
    if e["name"] == "heading":
        s = e.get("settings", {})
        text = s.get("text", "")
        tag = s.get("tag", "")
        parent = e.get("parent", "?")
        print(f"  [{tag:4s}] id={e['id']:8s} parent={parent:8s} {text[:120]!r}")
print()

# Show the last 10 elements in content (where we'd append new sections)
print("=== Last 10 elements in content list ===")
for e in content[-10:]:
    s = e.get("settings", {})
    preview = ""
    if e["name"] == "heading":
        preview = s.get("text", "")[:60]
    elif e["name"] in ("text", "text-basic"):
        preview = str(s.get("text", ""))[:60]
    print(f"  {e['name']:12s} id={e['id']:8s} parent={e.get('parent','?'):8s} {preview!r}")
