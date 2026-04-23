import os
"""Extract FAQ Q/A pairs from live Bricks content for schema mirror."""
import json, urllib.request, base64
auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
req = urllib.request.Request('https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/524', headers={'Authorization': f'Basic {auth}'})
d = json.loads(urllib.request.urlopen(req).read())
content = d['content']
by_id = {e['id']: e for e in content}

faq_parent = by_id.get('b42667')
if not faq_parent:
    print("FAQ parent b42667 not found")
    raise SystemExit()

faqs = []
for wrapper_id in faq_parent.get('children', []):
    wrapper = by_id.get(wrapper_id)
    if not wrapper:
        continue
    q = None; a_parts = []
    def collect(eid):
        global q
        e = by_id.get(eid)
        if not e:
            return
        s = e.get('settings', {}) or {}
        if e['name'] == 'heading' and 'text' in s and q is None:
            q = s['text']
        elif e['name'] in ('text-basic','text') and 'text' in s:
            a_parts.append(s['text'])
        for c in e.get('children', []):
            collect(c)
    # Need a non-global approach
    stack = [wrapper_id]
    while stack:
        eid = stack.pop(0)
        e = by_id.get(eid)
        if not e:
            continue
        s = e.get('settings', {}) or {}
        if e['name'] == 'heading' and 'text' in s and q is None:
            q = s['text']
        elif e['name'] in ('text-basic','text') and 'text' in s:
            a_parts.append(s['text'])
        stack.extend(e.get('children', []))
    if q:
        faqs.append({'q': q, 'a': ' '.join(a_parts).strip()})

print(f"Found {len(faqs)} FAQs")
for i, f in enumerate(faqs, 1):
    print(f"\n--- FAQ {i} ---")
    print(f"Q: {f['q']}")
    print(f"A: {f['a'][:200]}...")

with open(r'C:\Users\Willb\Claude\CFC\faqs_extracted.json', 'w', encoding='utf-8') as fp:
    json.dump(faqs, fp, indent=2)
print(f"\nSaved to faqs_extracted.json")
