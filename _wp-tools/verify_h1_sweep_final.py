import os
"""Final verification: all 37 pages should have exactly 1 live <h1>.
Flag any page that still has 0 or 2+."""
import json, urllib.request, base64, re, time, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()

pages = []
page_num = 1
while True:
    req = urllib.request.Request(
        f'https://www.customfabriccreations.net/wp-json/wp/v2/pages?per_page=50&page={page_num}&_fields=id,slug,link,status',
        headers={'Authorization': f'Basic {auth}'})
    try:
        batch = json.loads(urllib.request.urlopen(req, timeout=30).read())
    except urllib.error.HTTPError as e:
        if e.code == 400: break
        raise
    if not batch: break
    pages.extend(batch)
    if len(batch) < 50: break
    page_num += 1

print(f'Checking {len(pages)} pages...\n')
clean, broken = 0, []
for p in pages:
    if p.get('status') != 'publish': continue
    try:
        req = urllib.request.Request(p['link'] + f'?nocache={int(time.time())}')
        html = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', errors='replace')
        n = len(re.findall(r'<h1[^>]*>', html))
        if n == 1: clean += 1
        else: broken.append((p['id'], p['slug'], n))
    except Exception as e:
        broken.append((p['id'], p['slug'], f'err {e}'))

print(f'Clean (h1=1): {clean}')
print(f'Issues: {len(broken)}')
for b in broken:
    print(f'  id={b[0]} slug={b[1]} h1={b[2]}')
