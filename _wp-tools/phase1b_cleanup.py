import os
"""Phase 1b: clean 6 remaining Tampa Bay / Central Florida mentions in body copy.

Elements:
- dfc524: '...Central Florida homeowners keep choosing them' + '...across Tampa Bay measured...'
- 863443: '...Tampa Bay homeowners keep choosing them:' + '...Tampa Bay is hurricane country...'
- 5c9c3e: '...default for Tampa Bay windows...'
- hxhdwa: '...most of the Tampa Bay region.'
"""
import json
import urllib.request
import base64
import datetime

PAGE_ID = 524
ENDPOINT_BASE = "https://www.customfabriccreations.net/wp-json/cfc/v1/bricks"
USER = "daniel"
APP_PASS = os.environ.get("CFC_WP_APP_PASS", "")

auth = base64.b64encode(f"{USER}:{APP_PASS}".encode()).decode()
headers = {"Authorization": f"Basic {auth}", "Content-Type": "application/json"}

req = urllib.request.Request(f"{ENDPOINT_BASE}/{PAGE_ID}", headers=headers)
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())
content = data["content"]

ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup = rf"C:\Users\Willb\Claude\CFC\bricks_backup_524_{ts}_pre_phase1b.json"
with open(backup, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
print(f"Backup: {backup}")

# Partial substring replacements (old, new) per element id
replacements = {
    "dfc524": [
        ("Central Florida homeowners keep choosing", "St. Pete homeowners keep choosing"),
        ("across Tampa Bay measured", "across St. Pete and the Gulf Coast measured"),
    ],
    "863443": [
        ("Here's why Tampa Bay homeowners keep choosing them", "Here's why St. Pete homeowners keep choosing them"),
        ("Tampa Bay is hurricane country", "The Gulf Coast is hurricane country"),
    ],
    "5c9c3e": [
        ("default for Tampa Bay windows", "default for St. Pete windows"),
    ],
    "hxhdwa": [
        ("most of the Tampa Bay region", "most of the Tampa Bay and Gulf Coast region"),
    ],
}

by_id = {e["id"]: e for e in content}

print("\n=== Applying cleanups ===")
for eid, subs in replacements.items():
    e = by_id.get(eid)
    if not e:
        print(f"  MISS: {eid} not found")
        continue
    s = e["settings"]
    txt = s.get("text", "")
    for old, new in subs:
        if old in txt:
            txt = txt.replace(old, new)
            print(f"  OK  : {eid} {old[:50]!r} -> {new[:50]!r}")
        else:
            print(f"  MISS: {eid} substring not found: {old[:50]!r}")
    s["text"] = txt

# POST
print("\n=== POSTing ===")
payload = json.dumps({"content": content}).encode()
req = urllib.request.Request(f"{ENDPOINT_BASE}/{PAGE_ID}", data=payload, headers=headers, method="POST")
with urllib.request.urlopen(req) as r:
    print(f"POST: {r.status} {r.read().decode()}")

# Verify
req = urllib.request.Request(f"{ENDPOINT_BASE}/{PAGE_ID}", headers=headers)
with urllib.request.urlopen(req) as r:
    verify = json.loads(r.read())
v_by_id = {e["id"]: e for e in verify["content"]}

print("\n=== Verification ===")
for eid in replacements:
    txt = v_by_id[eid]["settings"].get("text", "")
    hits = []
    for term in ("Tampa Bay", "Central Florida"):
        if term in txt:
            hits.append(term)
    print(f"  {eid}: remaining geo terms = {hits or 'NONE'}")
