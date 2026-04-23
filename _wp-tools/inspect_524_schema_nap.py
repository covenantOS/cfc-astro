import os
"""Extract LocalBusiness NAP from the schema on 524 so the visible H7
NAP block matches exactly."""
import json, urllib.request, base64, re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
req = urllib.request.Request('https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/524',
    headers={'Authorization': f'Basic {auth}'})
d = json.loads(urllib.request.urlopen(req, timeout=20).read())

for e in d['content']:
    if e['id'] != 'abe9b6': continue
    t = e['settings'].get('text', '')
    m = re.search(r'<script[^>]*>(.*?)</script>', t, flags=re.DOTALL)
    if not m:
        print('No script tag')
        break
    raw = m.group(1)
    try:
        obj = json.loads(raw)
    except Exception as ex:
        print(f'JSON parse failed: {ex}')
        break
    # obj is an array
    for node in obj:
        if node.get('@type') == 'LocalBusiness':
            print(json.dumps(node, indent=2, ensure_ascii=False))
            break

# Also check /areas/west-st-pete/ schema for NAP reference
print('\n\n=== West St. Pete area page schema (1346) ===')
req = urllib.request.Request('https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/1346',
    headers={'Authorization': f'Basic {auth}'})
d2 = json.loads(urllib.request.urlopen(req, timeout=20).read())
for e in d2['content']:
    s = e.get('settings') or {}
    for k, v in s.items():
        if isinstance(v, str) and '<script' in v.lower() and 'LocalBusiness' in v:
            m = re.search(r'<script[^>]*>(.*?)</script>', v, flags=re.DOTALL)
            if m:
                try:
                    obj = json.loads(m.group(1))
                    if isinstance(obj, list):
                        for n in obj:
                            if n.get('@type') == 'LocalBusiness':
                                print(json.dumps(n, indent=2, ensure_ascii=False))
                                break
                    elif isinstance(obj, dict) and obj.get('@type') == 'LocalBusiness':
                        print(json.dumps(obj, indent=2, ensure_ascii=False))
                except Exception as ex:
                    print(f'1346 parse failed: {ex}')
                break
