import os
"""Strip the duplicate <h1> from page 1390's post_content. The theme
template already renders the page title as H1; the post_content should
start with the intro <p>, not a second H1."""
import json, urllib.request, base64, datetime, re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()

# Fetch current post_content (raw, not rendered)
req = urllib.request.Request(
    'https://www.customfabriccreations.net/wp-json/wp/v2/pages/1390?context=edit&_fields=id,slug,title,content',
    headers={'Authorization': f'Basic {auth}'})
p = json.loads(urllib.request.urlopen(req, timeout=30).read())

raw = p['content']['raw']
print(f'Raw post_content length: {len(raw)}')
print(f'First 400 chars:')
print(raw[:400])

# Save backup
ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
with open(rf'C:\Users\Willb\Claude\CFC\page_1390_backup_{ts}_pre_h1_fix.json', 'w', encoding='utf-8') as f:
    json.dump(p, f, indent=2, ensure_ascii=False)
print(f'\nBackup saved: page_1390_backup_{ts}_pre_h1_fix.json')

# Find and remove the <h1>...</h1> block(s) in post_content
h1_blocks = re.findall(r'<h1[^>]*>.*?</h1>', raw, flags=re.DOTALL | re.IGNORECASE)
print(f'\n<h1> blocks found in post_content: {len(h1_blocks)}')
for i, b in enumerate(h1_blocks):
    print(f'  H1 #{i+1}: {b[:200]!r}')

# Only remove H1s that contain the exact page title (to be safe)
page_title = p['title']['rendered']
# HTML-decode common entities
page_title_decoded = page_title.replace('&amp;', '&').replace('&#8217;', "'").replace('&#8216;', "'")
print(f'\nPage title (for match): {page_title!r}')

def strip_title_h1(m):
    block = m.group(0)
    inner = re.sub(r'<[^>]+>', '', block)  # strip inner tags
    # Compare stripped text loosely
    if page_title.lower().strip() in inner.lower() or page_title_decoded.lower().strip() in inner.lower():
        return ''  # remove
    return block  # keep (not a duplicate of page title)

new_raw = re.sub(r'<h1[^>]*>.*?</h1>\s*', strip_title_h1, raw, flags=re.DOTALL | re.IGNORECASE)

# Also clean up any blank <p></p> or leading whitespace left behind
new_raw = re.sub(r'^\s*<div class="ps-install-content">\s*', '<div class="ps-install-content">', new_raw)

print(f'\nNew post_content length: {len(new_raw)} (was {len(raw)})')
print(f'First 400 chars of new:')
print(new_raw[:400])

if new_raw == raw:
    print('\nNo changes made.')
else:
    # PUT update via WP REST
    payload = {'content': new_raw}
    req2 = urllib.request.Request(
        'https://www.customfabriccreations.net/wp-json/wp/v2/pages/1390',
        data=json.dumps(payload).encode(),
        headers={'Authorization': f'Basic {auth}',
                 'Content-Type': 'application/json'},
        method='POST')
    resp = json.loads(urllib.request.urlopen(req2, timeout=30).read())
    print(f'\nUpdate response: status={resp.get("status")}, modified={resp.get("modified")}')

    # Verify live
    print('\n=== Post-verify live HTML ===')
    import time
    html_req = urllib.request.Request(f'https://www.customfabriccreations.net/plantation-shutters-installation-st-petersburg/?nocache={int(time.time())}')
    html = urllib.request.urlopen(html_req, timeout=30).read().decode('utf-8', errors='replace')
    h1_count = len(re.findall(r'<h1[^>]*>', html))
    h2_count = len(re.findall(r'<h2[^>]*>', html))
    print(f'  h1 count: {h1_count} (was 2, target 1)')
    print(f'  h2 count: {h2_count}')
