import os
"""Fetch page 524 (/services/plantation-shutters/) Bricks content, find
text-basic elements that carry JSON-LD blocks, and identify the one whose
JSON fails to parse. The schema audit flagged an unescaped `"` inside an
FAQ Answer around `"Plantation shutters"` — we need to locate it precisely."""
import json, urllib.request, base64

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()

def fetch(pid):
    req = urllib.request.Request(
        f'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/{pid}',
        headers={'Authorization': f'Basic {auth}'})
    return json.loads(urllib.request.urlopen(req).read())

d = fetch(524)
content = d['content']
print(f"Total elements: {len(content)}")

# Find text-basic elements carrying JSON-LD
for e in content:
    if e.get('name') not in ('text-basic', 'text', 'code'):
        continue
    s = e.get('settings', {}) or {}
    t = s.get('text', '') or s.get('code', '')
    if not isinstance(t, str) or 'application/ld+json' not in t:
        continue
    print(f"\n=== Element id={e.get('id')} name={e.get('name')} label={e.get('label')!r} ===")
    # Extract JSON between <script> tags
    i = t.find('>')
    j = t.rfind('</script>')
    if i < 0 or j < 0:
        print("  (no script tags found)")
        continue
    raw = t[i+1:j].strip()
    print(f"  length: {len(raw)}")
    try:
        parsed = json.loads(raw)
        types = []
        if isinstance(parsed, list):
            types = [x.get('@type') for x in parsed if isinstance(x, dict)]
        elif isinstance(parsed, dict):
            if '@graph' in parsed:
                types = [x.get('@type') for x in parsed['@graph'] if isinstance(x, dict)]
            else:
                types = [parsed.get('@type')]
        print(f"  PARSED OK — types: {types}")
    except json.JSONDecodeError as err:
        print(f"  PARSE ERROR at col {err.pos}: {err.msg}")
        # Show context around error
        start = max(0, err.pos - 80)
        end = min(len(raw), err.pos + 80)
        print(f"  context: ...{raw[start:end]}...")
