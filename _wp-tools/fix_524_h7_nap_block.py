import os
"""H7: Add visible NAP street address to page 524 Contact Section.

Current state:
- 18a293 'address' div has icon + text wrappers
- a93590 is empty (first address line slot)
- 15fd46 says 'All Pinellas & Gulf Coast' (service area)
- 78f69d 'Number' div shows '(727) 240-4512' (CTA number — leave alone)

Per memory: West St. Pete NAP confirmed at 3026 Central Ave Ste 551,
(352) 266-1262. Schema on 524 uses this address + phone.

Fix: populate a93590 with street address line; keep 15fd46 as service
area tagline so the display reads:
  [icon] 3026 Central Ave, Ste 551, St. Petersburg, FL 33712
         All Pinellas & Gulf Coast
         (727) 240-4512

The 727/352 phone canonical mismatch is a separate Daniel wp-admin
decision (C4). Not touching the 727 CTA number here.
"""
import json, urllib.request, base64, datetime, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()

def fetch(pid):
    req = urllib.request.Request(
        f'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/{pid}',
        headers={'Authorization': f'Basic {auth}'})
    return json.loads(urllib.request.urlopen(req, timeout=20).read())

def push(pid, content):
    req = urllib.request.Request(
        f'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/{pid}',
        data=json.dumps({'content': content}).encode(),
        headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'},
        method='POST')
    return json.loads(urllib.request.urlopen(req, timeout=20).read())

ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
d = fetch(524)
content = d['content']

with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_524_{ts}_pre_h7.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)

by_id = {e['id']: e for e in content}

# ------------------------------------------------------------------
# Print before-state
# ------------------------------------------------------------------
print('=== BEFORE ===')
for eid in ('a93590', '15fd46', '5ef9eb'):
    e = by_id.get(eid)
    if e:
        s = e.get('settings') or {}
        print(f"  {eid} [{e.get('name')}] label={e.get('label')}")
        for k in ('text','title','heading'):
            v = s.get(k)
            if v is not None:
                print(f"    {k}: {v!r}")
        if not any(s.get(k) for k in ('text','title','heading')):
            print(f"    settings: {s}")

# ------------------------------------------------------------------
# Apply edit
# ------------------------------------------------------------------
# Populate a93590 with street address
a93590 = by_id.get('a93590')
if a93590:
    s = a93590.setdefault('settings', {})
    current = s.get('text', '')
    new_text = '<p>3026 Central Ave, Suite 551, St. Petersburg, FL 33712</p>'
    if current.strip() in ('', '<p></p>', None):
        s['text'] = new_text
        print(f"\n  a93590: populated empty address slot with street address")
    elif '3026 Central' in current:
        print(f"\n  a93590: already has street address \u2014 skipping")
    else:
        print(f"\n  a93590: already has non-empty text, not overwriting:")
        print(f"    current: {current[:200]!r}")
        # Prepend rather than overwrite to be safe
        s['text'] = new_text + current
        print(f"    PREPENDED street address")
else:
    print('\n  a93590 NOT FOUND \u2014 cannot add NAP')

# Also check 15fd46 reads "All Pinellas & Gulf Coast" and leave it
fd = by_id.get('15fd46')
if fd:
    cur = fd['settings'].get('text', '')
    print(f"\n  15fd46 text (leaving unchanged): {cur!r}")

# ------------------------------------------------------------------
# Push
# ------------------------------------------------------------------
resp = push(524, content)
print(f'\n  PUSH: {resp}')

# ------------------------------------------------------------------
# Post-verify by fetching live HTML
# ------------------------------------------------------------------
print('\n=== POST-VERIFY ===')
import urllib.request as ur
html_req = ur.Request('https://www.customfabriccreations.net/services/plantation-shutters/?nocache=' + ts)
html = ur.urlopen(html_req, timeout=30).read().decode('utf-8', errors='replace')
has_street = '3026 Central' in html
has_zip = '33712' in html
has_phone_352 = '352-266-1262' in html or '352) 266-1262' in html
has_phone_727 = '727) 240-4512' in html or '727-240-4512' in html
print(f"  live HTML contains '3026 Central':  {has_street}")
print(f"  live HTML contains '33712':         {has_zip}")
print(f"  live HTML contains 352 phone:       {has_phone_352}  (expected True from schema)")
print(f"  live HTML contains 727 phone:       {has_phone_727}  (expected True from CTA)")

# Re-fetch JSON and confirm
d2 = fetch(524)
by_id2 = {e['id']: e for e in d2['content']}
print(f"\n  a93590.text post-push: {by_id2.get('a93590', {}).get('settings', {}).get('text', '')!r}")
