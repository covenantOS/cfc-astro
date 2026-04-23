import os
"""Fix C2: delete the Reviews section on /about/ (page 103).
The section ajlaux contains only pdrzkf (Testimonial Grid Alpha) which
contains 3 tree-service testimonials for 'Southern Environmental Group' —
wrong business entirely. Delete the whole section rather than leave
fabricated/wrong content live while we wait for real reviews."""
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
d = fetch(103)
content = d['content']

with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_103_{ts}_pre_remove_reviews.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)

by_id = {e['id']: e for e in content}

# Target: Reviews section ajlaux
target = 'ajlaux'
if target not in by_id:
    print(f'Section {target} not found'); raise SystemExit

# Collect all descendants recursively
def collect_descendants(eid, acc):
    acc.add(eid)
    e = by_id.get(eid)
    if not e: return
    for cid in e.get('children', []) or []:
        collect_descendants(cid, acc)

to_remove = set()
collect_descendants(target, to_remove)
print(f'Will remove {len(to_remove)} elements (section + descendants)')
# Quick sanity check for tree-service keywords
tree_hits = 0
for eid in to_remove:
    e = by_id.get(eid)
    if not e: continue
    s = e.get('settings', {}) or {}
    blob = json.dumps(s, ensure_ascii=False).lower()
    if any(k in blob for k in ('sweet gum','stump','tree trim','arborist','southern environmental')):
        tree_hits += 1
print(f'  Tree-service quote hits in removed set: {tree_hits}')

# Remove elements + detach from parent
parent_id = by_id[target].get('parent')
if parent_id and parent_id in by_id:
    parent = by_id[parent_id]
    parent['children'] = [c for c in (parent.get('children') or []) if c != target]
    print(f'Detached {target} from parent {parent_id}')

new_content = [e for e in content if e['id'] not in to_remove]
print(f'Content size: {len(content)} -> {len(new_content)}')

resp = push(103, new_content)
print(f'PUSH: {resp}')
