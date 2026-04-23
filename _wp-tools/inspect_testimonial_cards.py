import os
"""Map out the full 3 tree-service testimonial cards on /about/ so we know
what to delete. Each quote is in a Body block inside a grandparent card.
We need siblings (author name, role, star ratings) and the full card container."""
import json, urllib.request, base64, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
req = urllib.request.Request('https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/103',
    headers={'Authorization': f'Basic {auth}'})
d = json.loads(urllib.request.urlopen(req, timeout=20).read())
content = d['content']
by_id = {e['id']: e for e in content}

# The 3 quote IDs and their grandparents (card containers)
cards = [('nljztr', 'xojgrg'), ('oimbkq', 'ggiyny'), ('ggtbbs', 'ztpejz')]

def walk(eid, depth=0):
    e = by_id.get(eid)
    if not e: return
    s = e.get('settings', {}) or {}
    preview = ''
    for k in ('text', 'title', 'subtitle'):
        v = s.get(k)
        if isinstance(v, str) and v:
            preview = v[:120].replace('\n', ' ')
            break
    indent = '  ' * depth
    print(f"{indent}{eid} [{e.get('name')}] {e.get('label')!r} parent={e.get('parent')} | {preview!r}")
    for cid in e.get('children', []) or []:
        walk(cid, depth + 1)

for qid, card_id in cards:
    print(f"\n=== Card {card_id} (contains quote {qid}) ===")
    walk(card_id)

# Look for the "row" that contains all 3 cards — these are probably siblings
# of a common container. Print parents of card containers
print("\n\n=== Card parents ===")
for _, card_id in cards:
    e = by_id.get(card_id)
    if e:
        print(f"  card={card_id} parent={e.get('parent')}")

# Walk the parent to see all children (probably the testimonial row)
parent_of_cards = by_id.get(cards[0][1], {}).get('parent')
if parent_of_cards:
    print(f"\nParent container {parent_of_cards} and all its children:")
    walk(parent_of_cards)
