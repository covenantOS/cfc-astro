import os
"""Inspect the Contact Section (3e5525) on 524 to see what's already
inside it — so we can add the NAP block in the right place."""
import json, urllib.request, base64, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
req = urllib.request.Request('https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/524',
    headers={'Authorization': f'Basic {auth}'})
d = json.loads(urllib.request.urlopen(req, timeout=20).read())
content = d['content']
by_id = {e['id']: e for e in content}

def walk(eid, depth=0):
    e = by_id.get(eid)
    if not e: return
    s = e.get('settings') or {}
    preview = ''
    for k in ('text','title','subtitle','heading','content','label'):
        v = s.get(k)
        if isinstance(v, str) and v:
            preview = v[:200].replace('\n', ' ')
            break
    indent = '  ' * depth
    print(f"{indent}{eid} [{e.get('name')}] label={e.get('label')!r} | {preview!r}")
    for cid in (e.get('children') or []):
        walk(cid, depth + 1)

print('=== 3e5525 (Contact Section) full tree ===')
walk('3e5525')

# Also show existing IDs so we can pick a non-colliding one
print(f'\n\nTotal unique element IDs: {len(by_id)}')
import re
# Show which tag/customTag combos are common for text blocks
tag_combos = {}
for e in content:
    if e.get('name') in ('text-basic', 'text'):
        s = e.get('settings') or {}
        combo = (s.get('tag'), s.get('customTag'))
        tag_combos[combo] = tag_combos.get(combo, 0) + 1
print(f'\nTag combos for text / text-basic elements:')
for combo, n in sorted(tag_combos.items(), key=lambda x: -x[1]):
    print(f'  {combo}: {n}')

# Dump full JSON of 3e5525 and its direct children
print('\n\n=== Full JSON: 3e5525 ===')
print(json.dumps(by_id['3e5525'], indent=2, ensure_ascii=False)[:2000])
print('\n=== Full JSON: 13b590 (Contact Wrapper) ===')
if '13b590' in by_id:
    print(json.dumps(by_id['13b590'], indent=2, ensure_ascii=False)[:2000])
