import os
"""Safety test: change the H1 only, verify round-trip."""
import json
import urllib.request
import base64

PAGE_ID = 524
ENDPOINT_BASE = "https://www.customfabriccreations.net/wp-json/cfc/v1/bricks"
USER = "daniel"
APP_PASS = os.environ.get("CFC_WP_APP_PASS", "")

auth = base64.b64encode(f"{USER}:{APP_PASS}".encode()).decode()
headers = {"Authorization": f"Basic {auth}", "Content-Type": "application/json"}

# Fetch current
req = urllib.request.Request(f"{ENDPOINT_BASE}/{PAGE_ID}", headers=headers)
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())
content = data["content"]

# Modify ONLY the H1 (element d66522)
H1_ID = "d66522"
NEW_H1 = "Custom Plantation Shutters in St. Petersburg, FL"

changed = False
for e in content:
    if e.get("id") == H1_ID:
        old = e["settings"].get("text", "")
        e["settings"]["text"] = NEW_H1
        print(f"H1 {H1_ID}: {old!r} -> {NEW_H1!r}")
        changed = True
        break

if not changed:
    print(f"ERROR: H1 {H1_ID} not found")
    exit(1)

# POST the updated content
payload = json.dumps({"content": content}).encode()
req = urllib.request.Request(
    f"{ENDPOINT_BASE}/{PAGE_ID}",
    data=payload,
    headers=headers,
    method="POST",
)
with urllib.request.urlopen(req) as r:
    print(f"POST response: {r.status} {r.read().decode()}")

# Verify round-trip
req = urllib.request.Request(f"{ENDPOINT_BASE}/{PAGE_ID}", headers=headers)
with urllib.request.urlopen(req) as r:
    verify = json.loads(r.read())
for e in verify["content"]:
    if e.get("id") == H1_ID:
        print(f"Verify H1 after save: {e['settings'].get('text')!r}")
        break
