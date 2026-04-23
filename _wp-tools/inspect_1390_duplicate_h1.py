import os
"""Dump Bricks content of 1390 and pull the live HTML to find the two H1
sources."""
import json, urllib.request, base64, re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()

# Full Bricks content
req = urllib.request.Request('https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/1390',
    headers={'Authorization': f'Basic {auth}'})
d = json.loads(urllib.request.urlopen(req, timeout=20).read())
print(f'Total Bricks elements: {len(d["content"])}')
print('\nAll elements:')
for e in d['content']:
    s = e.get('settings') or {}
    preview = ''
    for k in ('text','title','heading','subtitle','content','label'):
        v = s.get(k)
        if isinstance(v, str) and v:
            preview = v[:200].replace('\n', ' ')
            break
    print(f"  {e['id']} name={e.get('name')} label={e.get('label')} parent={e.get('parent')} | {preview!r}")

# Fetch WP page meta (including post_content fallback and _bricks_* flags)
req2 = urllib.request.Request(
    'https://www.customfabriccreations.net/wp-json/wp/v2/pages/1390?_fields=id,title,content,slug,link,status,meta',
    headers={'Authorization': f'Basic {auth}'})
p = json.loads(urllib.request.urlopen(req2, timeout=30).read())
print(f'\n\nWP page title: {p["title"]["rendered"]!r}')
print(f'WP post_content length: {len(p["content"]["rendered"])}')
print(f'WP post_content preview: {p["content"]["rendered"][:500]}')

# Fetch live HTML and locate both H1 tags with context
print('\n\n=== Live HTML H1 scan ===')
import ssl, time
ts = int(time.time())
req3 = urllib.request.Request(f'https://www.customfabriccreations.net/plantation-shutters-installation-st-petersburg/?nocache={ts}')
html = urllib.request.urlopen(req3, timeout=30).read().decode('utf-8', errors='replace')

# Find all <h1> tags with some surrounding context
for i, m in enumerate(re.finditer(r'<h1[^>]*>.*?</h1>', html, flags=re.DOTALL)):
    print(f'\n--- H1 #{i+1} ---')
    # Get 200 chars before and the full H1
    start = max(0, m.start() - 200)
    ctx = html[start:m.end() + 50]
    print(ctx[:700])

# Count headings by level
print('\n=== All heading counts ===')
for lvl in (1, 2, 3):
    n = len(re.findall(f'<h{lvl}[^>]*>', html))
    print(f'  h{lvl}: {n}')
