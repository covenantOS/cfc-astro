import os
"""Page 1383 'thank-you': demote the in-content <h1>Your estimate is on
the way.</h1> to <h2> so the theme-rendered 'Thank You' title is the
single H1."""
import json, urllib.request, base64, datetime, re, time, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

req = urllib.request.Request(
    'https://www.customfabriccreations.net/wp-json/wp/v2/pages/1383?context=edit&_fields=id,slug,title,content',
    headers={'Authorization': f'Basic {auth}'})
p = json.loads(urllib.request.urlopen(req, timeout=30).read())
raw = p['content']['raw']
print(f'Raw length: {len(raw)}')

with open(rf'C:\Users\Willb\Claude\CFC\page_1383_backup_{ts}_pre_h1_demote.json', 'w', encoding='utf-8') as f:
    json.dump(p, f, indent=2, ensure_ascii=False)

# Demote all <h1>...</h1> blocks to <h2>...</h2> (page has 1, easy)
new_raw = re.sub(r'<h1(\b[^>]*)>', r'<h2\1>', raw, flags=re.IGNORECASE)
new_raw = re.sub(r'</h1>', r'</h2>', new_raw, flags=re.IGNORECASE)

print(f'New length: {len(new_raw)}')
if new_raw == raw:
    print('No change.')
else:
    payload = {'content': new_raw}
    req2 = urllib.request.Request(
        'https://www.customfabriccreations.net/wp-json/wp/v2/pages/1383',
        data=json.dumps(payload).encode(),
        headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'},
        method='POST')
    json.loads(urllib.request.urlopen(req2, timeout=30).read())
    print('Updated.')

# Verify
time.sleep(1)
html_req = urllib.request.Request(f'https://www.customfabriccreations.net/thank-you/?nocache={int(time.time())}')
html = urllib.request.urlopen(html_req, timeout=30).read().decode('utf-8', errors='replace')
h1 = len(re.findall(r'<h1[^>]*>', html))
h2 = len(re.findall(r'<h2[^>]*>', html))
print(f'\nLive: h1={h1}, h2={h2}')
