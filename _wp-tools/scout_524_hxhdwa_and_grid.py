import os
"""Get full text of hxhdwa (neighborhood list paragraph) and map out the
neighborhood card grid on page 524 so we can plan H10 (West St. Pete link)."""
import json, urllib.request, base64, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
req = urllib.request.Request('https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/524',
    headers={'Authorization': f'Basic {auth}'})
d = json.loads(urllib.request.urlopen(req, timeout=20).read())
by_id = {e['id']: e for e in d['content']}

# Full hxhdwa text
print('=== FULL TEXT 524/hxhdwa ===')
t = by_id['hxhdwa']['settings']['text']
print(t)

# Map out the grid — cards are children of card parents; neighborhoods listed earlier
# had parents like aowglf (Snell Isle), yjmtmy (Old Northeast), etc.
# These parents are likely siblings of one another in a grid container.

# Find the grid container (grandparent of headings)
HEADINGS = [('Snell Isle','ggphqh','aowglf'),
            ('Old Northeast','wrekwe','yjmtmy'),
            ('Downtown','ddfbeb','wctogi'),
            ('Shore Acres','jwdwtc','oqbhcm'),
            ('St. Pete Beach','vfddjo','zsluop'),
            ('Treasure Island','eolpji','nxfpny'),
            ('Tierra Verde','yjyyrg','udwejo'),
            ('Sand Key','foqgsp','odfwod'),
            ('Clearwater Area','mbjqnp','sgyhkp'),
            ('Clearwater','zqjcld','wloayw'),
            ('Belleair Shore','ysdxua','tdsoeu'),
            ('Seminole','ezccvy','gkvrrd')]

# Find the grandparent that contains all card containers as children
grandparents = {}
for name, hid, parent_id in HEADINGS:
    p = by_id.get(parent_id)
    if p:
        gp = p.get('parent')
        grandparents.setdefault(gp, []).append((name, hid, parent_id))

print('\n\n=== Card grandparents (grid containers) ===')
for gp, cards in grandparents.items():
    print(f"\n  Grid container: {gp} has {len(cards)} neighborhood cards")
    gpe = by_id.get(gp)
    if gpe:
        print(f"    name={gpe.get('name')} label={gpe.get('label')}")
        print(f"    all children: {gpe.get('children')}")
    for n, h, p in cards:
        print(f"    - '{n}' heading={h} card={p}")

# Now dump full structure of ONE card so we know what to clone for West St. Pete
print('\n\n=== Structure of one card (Old Northeast / yjmtmy) ===')

def walk(eid, depth=0):
    e = by_id.get(eid)
    if not e: return
    s = e.get('settings') or {}
    preview = ''
    for k in ('text','title','subtitle','heading','content','label'):
        v = s.get(k)
        if isinstance(v, str) and v:
            preview = v[:140].replace('\n', ' ')
            break
    indent = '  ' * depth
    link = ''
    blob = json.dumps(s, ensure_ascii=False)
    if '/areas/' in blob:
        import re
        m = re.search(r'/areas/[a-z0-9\-]+/?', blob)
        if m: link = f'  LINK={m.group(0)}'
    print(f"{indent}{eid} [{e.get('name')}] parent={e.get('parent')}{link} | {preview!r}")
    for cid in (e.get('children') or []):
        walk(cid, depth + 1)

walk('yjmtmy')

print('\n=== Structure of Snell Isle card (aowglf) for comparison ===')
walk('aowglf')
