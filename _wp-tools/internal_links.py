import os
"""Internal linking pass: add geo-anchor link to plantation-shutters from homepage (14) and services hub (145)."""
import json, urllib.request, base64, datetime, re

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
BASE = 'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks'
TARGET_URL = '/services/plantation-shutters/'
ANCHOR_PHRASES = [
    ('plantation shutters', 'plantation shutters in St. Petersburg'),
    ('shutters', 'custom plantation shutters'),
]

def fetch(pid):
    req = urllib.request.Request(f'{BASE}/{pid}', headers={'Authorization': f'Basic {auth}'})
    return json.loads(urllib.request.urlopen(req).read())

def push(pid, content):
    req = urllib.request.Request(f'{BASE}/{pid}', data=json.dumps({'content': content}).encode(),
        headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'}, method='POST')
    return json.loads(urllib.request.urlopen(req).read())

def has_link_already(content, target):
    return any(target in str(e.get('settings', {})) for e in content)

ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

for pid in (14, 145):
    d = fetch(pid)
    content = d['content']
    with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_{pid}_{ts}_pre_links.json','w',encoding='utf-8') as f:
        json.dump(d, f, indent=2)

    if has_link_already(content, TARGET_URL):
        print(f"[{pid}] Link to {TARGET_URL} already present. Skipping.")
        continue

    modified = 0
    link_html = f'<a href="{TARGET_URL}">plantation shutters in St. Petersburg</a>'

    # Strategy: find first text-basic or text element whose text contains a shutter-adjacent phrase,
    # and replace the first occurrence of "plantation shutters" (case-insensitive) with a link.
    for e in content:
        if modified >= 2:  # cap at 2 links per page
            break
        if e.get('name') not in ('text-basic','text'):
            continue
        s = e.get('settings', {}) or {}
        text = s.get('text','')
        if not isinstance(text, str):
            continue
        # Skip if already linked to the target
        if TARGET_URL in text:
            continue
        # Look for the phrase "plantation shutters" not already inside an <a>
        m = re.search(r'(?i)(?<!>)\bplantation shutters\b', text)
        if m:
            # Wrap that occurrence in an anchor. Use a function to preserve original casing.
            def replace_once(match):
                return f'<a href="{TARGET_URL}">{match.group(0)}</a>'
            new_text, n = re.subn(r'(?i)\bplantation shutters\b', replace_once, text, count=1)
            if n > 0:
                e['settings']['text'] = new_text
                print(f"[{pid}] Linked in element {e['id']} ({e.get('name')}) — preview: {new_text[:140]!r}")
                modified += 1

    if modified == 0:
        # Fallback: append a text-basic link block at the end of the last text element's parent
        print(f"[{pid}] No existing mention to link. Skipping (fallback append not safe without content context).")
        continue

    resp = push(pid, content)
    print(f"[{pid}] Push: {resp}  links added: {modified}")
