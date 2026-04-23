import os
"""Inspect current Bricks structure for Phase 2 section insertion."""
import json, urllib.request, base64
auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
req = urllib.request.Request('https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/524', headers={'Authorization': f'Basic {auth}'})
d = json.loads(urllib.request.urlopen(req).read())
content = d['content']
by_id = {e['id']: e for e in content}

# Save fresh copy
with open(r'C:\Users\Willb\Claude\CFC\bricks_live.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)

# Roots
print("=== ROOTS ===")
for e in content:
    if e.get('parent') == 0:
        print(f"  {e['id']:8s} {e['name']:15s} label={e.get('label','')!r} children={len(e.get('children',[]))}")

# All H2s with their parent chain
print("\n=== H2 HEADINGS + PARENT ===")
for e in content:
    s = e.get('settings', {})
    if isinstance(s, dict) and e['name'] == 'heading' and s.get('tag') == 'h2':
        pid = e.get('parent')
        parent = by_id.get(pid, {})
        gp_id = parent.get('parent')
        gp = by_id.get(gp_id, {})
        print(f"  H2 id={e['id']} parent={pid}({parent.get('name','?')}) grand={gp_id}({gp.get('name','?')}) text={s.get('text','')[:60]!r}")

# Map the main "Content Section" hierarchy 2 levels deep
print("\n=== Content Section (a2711d) children ===")
cs = by_id.get('a2711d')
if cs:
    for cid in cs.get('children', []):
        c = by_id.get(cid, {})
        s = c.get('settings', {})
        print(f"  {cid} {c.get('name','?'):12s} label={c.get('label','')!r} children={c.get('children', [])}")

# Find a "model" H2 section: show a complete H2-introduced block structure
print("\n=== Sample H2 block (types section a55b98) with all descendants ===")
def walk(eid, depth=0):
    e = by_id.get(eid)
    if not e:
        return
    s = e.get('settings', {})
    preview = ''
    if isinstance(s, dict):
        if 'text' in s:
            t = s['text']
            preview = str(t)[:90] if isinstance(t, str) else '<dict/list>'
        gc = s.get('_cssGlobalClasses', [])
        tag = s.get('tag', '')
    else:
        gc = []
        tag = ''
    print(f"{'  '*depth}[{e['name']:12s}] id={eid} label={e.get('label',''):20s} tag={tag:3s} classes={gc} parent={e.get('parent')}")
    if preview:
        print(f"{'  '*depth}  text: {preview!r}")
    for c in e.get('children', []):
        walk(c, depth+1)

# Find the container for a55b98 (Types H2)
a55b98 = by_id.get('a55b98')
if a55b98:
    pid = a55b98.get('parent')
    # walk the parent's parent to get the whole section
    section_id = by_id.get(pid, {}).get('parent', pid)
    print(f"Walking from section root: {section_id}")
    walk(section_id)
