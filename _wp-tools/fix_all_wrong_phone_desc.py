import os
"""Bulk-replace wrong phone 624-0162 -> 266-1262 in Rank Math meta descriptions
across all affected area pages. Preserves other formatting."""
import json, urllib.request, base64, re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()

AREAS = [1346, 1023, 567, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583]

def get_seo(pid):
    req = urllib.request.Request(f'https://www.customfabriccreations.net/wp-json/cfc/v1/seo/{pid}',
        headers={'Authorization': f'Basic {auth}'})
    return json.loads(urllib.request.urlopen(req, timeout=20).read())

def set_seo(pid, payload):
    req = urllib.request.Request(f'https://www.customfabriccreations.net/wp-json/cfc/v1/seo/{pid}',
        data=json.dumps(payload).encode(),
        headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'},
        method='POST')
    return json.loads(urllib.request.urlopen(req, timeout=20).read())

# Multiple phone patterns — normalize to the same formatting as the source
PATTERNS = [
    (re.compile(r'\(352\)\s*624[\s\-\.]?0162'), '(352) 266-1262'),
    (re.compile(r'\+1[\s\-\.]?352[\s\-\.]?624[\s\-\.]?0162'), '+1-352-266-1262'),
    (re.compile(r'(?<!\d)352[\s\-\.]?624[\s\-\.]?0162'), '352-266-1262'),
]

fixed = 0
unchanged = 0
for pid in AREAS:
    try:
        s = get_seo(pid)
        desc = s.get('description', '') or ''
        title = s.get('title', '') or ''
        new_desc = desc
        new_title = title
        for patt, repl in PATTERNS:
            new_desc = patt.sub(repl, new_desc)
            new_title = patt.sub(repl, new_title)
        payload = {}
        if new_desc != desc:
            payload['description'] = new_desc
        if new_title != title:
            payload['title'] = new_title
        if payload:
            resp = set_seo(pid, payload)
            print(f'{pid}: FIXED {list(payload.keys())} -> {resp.get("ok")}')
            fixed += 1
        else:
            unchanged += 1
    except Exception as e:
        print(f'{pid}: ERROR {e}')

print(f'\nFixed {fixed} pages, {unchanged} unchanged')
