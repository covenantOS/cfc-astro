import os
"""Audit services hub (145) + sample area page (580 Snell Isle) to plan integration strategy."""
import json, urllib.request, base64

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
BASE = 'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks'

def fetch(pid):
    req = urllib.request.Request(f'{BASE}/{pid}', headers={'Authorization': f'Basic {auth}'})
    return json.loads(urllib.request.urlopen(req).read())

def summarize(pid, label):
    d = fetch(pid)
    content = d['content']
    by_id = {e['id']: e for e in content}
    print(f"\n=== {label} (id={pid}) — {len(content)} elements ===")
    type_counts = {}
    for e in content:
        n = e.get('name', '')
        type_counts[n] = type_counts.get(n, 0) + 1
    print(f"Types: {type_counts}")

    # find text elements containing keywords
    keys = ['plantation', 'shutter', 'window treatment', 'drapery', 'upholster']
    hits = []
    for e in content:
        s = e.get('settings', {}) or {}
        for field in ('text', 'title', 'subtitle', 'heading', 'content'):
            v = s.get(field)
            if isinstance(v, str):
                low = v.lower()
                for k in keys:
                    if k in low:
                        hits.append((e['id'], e.get('name'), field, k, v[:120]))
                        break
    print(f"Matching elements ({len(hits)}):")
    for h in hits[:20]:
        print(f"  {h[0]} [{h[1]}] field={h[2]} key={h[3]}: {h[4]!r}")

    # root sections
    roots = [e for e in content if e.get('parent') in (0, '', None)]
    print(f"Root-level sections: {len(roots)}")
    for r in roots:
        print(f"  {r['id']} name={r.get('name')} label={r.get('label')!r} kids={len(r.get('children', []))}")

for pid, label in [(145, 'Services Hub'), (580, 'Snell Isle'), (1346, 'West St. Pete'), (524, 'Plantation Shutters')]:
    try:
        summarize(pid, label)
    except Exception as e:
        print(f"Error {pid}: {e}")
