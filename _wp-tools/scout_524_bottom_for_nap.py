import os
"""Find a good insertion point for a visible NAP block on page 524.

Strategy: look at the LAST 20 elements to find either (a) a CTA section
we can slot into, or (b) an existing text-basic we can safely append
NAP HTML to.

Also: dump one text-basic element's full JSON structure so we know what
fields a new one needs."""
import json, urllib.request, base64, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
req = urllib.request.Request('https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/524',
    headers={'Authorization': f'Basic {auth}'})
d = json.loads(urllib.request.urlopen(req, timeout=20).read())
content = d['content']

by_id = {e['id']: e for e in content}

print(f'Total elements: {len(content)}')
print('\n=== Last 25 elements (in order) ===')
for i, e in enumerate(content[-25:], start=len(content)-25):
    s = e.get('settings') or {}
    preview = ''
    for k in ('text', 'title', 'heading', 'subtitle', 'content'):
        v = s.get(k)
        if isinstance(v, str) and v:
            preview = v[:100].replace('\n', ' ')
            break
    print(f"  [{i}] {e['id']} name={e.get('name')} label={e.get('label')} parent={e.get('parent')} | {preview!r}")

# Also find all section-level elements (name=section) to identify structure
print('\n=== All top-level sections ===')
for e in content:
    if e.get('name') == 'section' or e.get('parent') is None or e.get('parent') == '':
        s = e.get('settings') or {}
        print(f"  {e['id']} name={e.get('name')} label={e.get('label')} parent={e.get('parent')} children={len(e.get('children') or [])}")

# Find CTAs or footer sections
print('\n=== Elements with CTA-like labels ===')
for e in content:
    lbl = (e.get('label') or '').lower()
    nm = (e.get('name') or '').lower()
    if any(k in lbl + ' ' + nm for k in ['cta', 'contact', 'footer', 'bottom', 'conclusion', 'final']):
        s = e.get('settings') or {}
        preview = ''
        for k in ('text','title','heading'):
            v = s.get(k)
            if isinstance(v, str): preview = v[:120]; break
        print(f"  {e['id']} name={e.get('name')} label={e.get('label')} parent={e.get('parent')} | {preview!r}")

# Find text with phone number patterns (existing CTA)
print('\n=== Elements with phone numbers (existing contact info) ===')
for e in content:
    s = e.get('settings') or {}
    blob = json.dumps(s, ensure_ascii=False)
    if '352-266-1262' in blob or '352) 266-1262' in blob or '3522661262' in blob:
        print(f"  {e['id']} name={e.get('name')} parent={e.get('parent')}")
        for k, v in s.items():
            if isinstance(v, str) and ('352' in v or '266' in v):
                print(f"    {k}: {v[:200]!r}")

# Dump full JSON of one text-basic element so we know the shape to clone
print('\n=== Full JSON of one text-basic element (caeb7e) for cloning reference ===')
tb = by_id.get('caeb7e')
if tb:
    print(json.dumps(tb, indent=2, ensure_ascii=False))
