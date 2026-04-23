import os
"""
Homepage page 14 rendering as default PHP template instead of Bricks.
_bricks_page_content_2 meta has 228 elements (intact), but the editor_mode
flag is probably missing/wrong.

Approach: use WP REST meta to inspect + flip _bricks_editor_mode to 'bricks'.
If the meta isn't REST-exposed, add a helper route to the existing mu-plugin.
"""
import json, urllib.request, base64

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()

# 1. Dump all post meta for page 14 so we can see what's set/missing.
# Use WP REST w/ context=edit to get post; then try the _bricks_editor_mode
# via direct get_post_meta call through our custom endpoint.

# First: try the bricks GET (we know this works) — it returns content/header/footer only,
# no editor_mode. So add a meta dump endpoint, or infer from a known good page.

# Quickest path: compare page 14 raw meta to page 524 (which we know renders fine).
# Since standard wp/v2/pages only exposes whitelisted meta, we need another angle.

# Try: POST a standard wp/v2/pages update with meta key. WP REST blocks private meta
# (keys starting with _) unless registered. Bricks plugin DOES register its meta keys
# via auth_callback — worth trying.

def req(method, url, data=None, headers=None):
    h = {'Authorization': f'Basic {auth}'}
    if headers: h.update(headers)
    if data is not None:
        h['Content-Type'] = 'application/json'
        data = json.dumps(data).encode()
    r = urllib.request.Request(url, data=data, headers=h, method=method)
    try:
        return urllib.request.urlopen(r, timeout=20).read().decode()
    except urllib.error.HTTPError as e:
        return f'HTTP {e.code}: {e.read().decode()[:500]}'

# Step 1: compare raw meta between a healthy page (524) and broken page (14).
for pid in [14, 524]:
    url = f'https://www.customfabriccreations.net/wp-json/wp/v2/pages/{pid}?context=edit'
    r = req('GET', url)
    try:
        d = json.loads(r)
        meta = d.get('meta', {})
        tpl = d.get('template', '')
        print(f'[{pid}] template={tpl!r}')
        print(f'[{pid}] meta keys: {list(meta.keys())}')
    except:
        print(f'[{pid}] err: {r[:200]}')

# Step 2: try to set meta directly via wp/v2/pages
# Bricks plugin registers _bricks_editor_mode as REST-exposed for editors.
print('\n=== Attempting to set editor_mode to bricks ===')
r = req('POST', 'https://www.customfabriccreations.net/wp-json/wp/v2/pages/14',
        data={'meta': {'_bricks_editor_mode': 'bricks'}})
print(r[:400])
