import os
"""Locate tree-service testimonials on /about/ page 103.
Keywords from the E-E-A-T audit: 'sweet gum stump', 'tree stump', 'tree trimming',
'Southern Environmental Group', 'arborist'."""
import json, urllib.request, base64

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
req = urllib.request.Request('https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/103',
    headers={'Authorization': f'Basic {auth}'})
d = json.loads(urllib.request.urlopen(req, timeout=20).read())
content = d['content']
print(f"Total elements: {len(content)}")

# Identify testimonials: review-type elements, or text elements mentioning tree/stump
patterns = ['sweet gum', 'stump', 'tree trim', 'tree removal', 'arborist',
            'Southern Environmental', 'sweetgum']
by_id = {e['id']: e for e in content}

hits = []
for e in content:
    s = e.get('settings', {}) or {}
    blob = json.dumps(s, ensure_ascii=False).lower()
    for p in patterns:
        if p.lower() in blob:
            hits.append((e.get('id'), e.get('name'), e.get('label'), p, e.get('parent')))
            break

print(f"\nHits ({len(hits)}):")
for h in hits:
    print(f"  id={h[0]} name={h[1]} label={h[2]!r} matched={h[3]!r} parent={h[4]}")

# Also dump testimonial-looking blocks by name
print("\nReview/testimonial elements by name:")
for e in content:
    n = e.get('name', '')
    if any(k in n.lower() for k in ('testimonial', 'review', 'quote')):
        print(f"  id={e['id']} name={n} label={e.get('label')!r} parent={e.get('parent')}")

# Print parent containers of hits to understand scope of deletion
print("\nParent containers of hits:")
parents = set(h[4] for h in hits if h[4])
for pid in parents:
    if pid in by_id:
        p = by_id[pid]
        print(f"  parent={p['id']} name={p.get('name')} label={p.get('label')!r} grandparent={p.get('parent')}")
