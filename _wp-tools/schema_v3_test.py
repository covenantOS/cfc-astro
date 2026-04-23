import os
"""Test different Bricks element types to find one that renders raw <script>."""
import json, urllib.request, base64, secrets

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
URL = 'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/524'

# Fetch
req = urllib.request.Request(URL, headers={'Authorization': f'Basic {auth}'})
d = json.loads(urllib.request.urlopen(req).read())
content = d['content']

# Clean previous test elements ('html' named and any 'code' with plantation schema)
to_remove = set()
for e in content:
    if e.get('name') in ('html',) and 'plantation' in str(e.get('settings', {})).lower():
        to_remove.add(e['id'])
    if e.get('name') == 'code' and 'plantation' in str(e.get('settings', {})).lower():
        to_remove.add(e['id'])
content = [e for e in content if e['id'] not in to_remove]
for e in content:
    if 'children' in e:
        e['children'] = [c for c in e['children'] if c not in to_remove]

# Insert a sentinel with a distinct marker text in a 'text-basic' + 'text' + 'code' and see which renders a <script>
sentinel_script = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","name":"CFC_TEST_SENTINEL_5f9a3b"}</script>'

parent_id = '9d29a5'
new_els = []

# text-basic with script
id1 = secrets.token_hex(3)
new_els.append({
    'id': id1, 'name': 'text-basic', 'parent': parent_id, 'children': [],
    'settings': {'text': sentinel_script},
    'label': 'TEST text-basic'
})

# text with script
id2 = secrets.token_hex(3)
new_els.append({
    'id': id2, 'name': 'text', 'parent': parent_id, 'children': [],
    'settings': {'text': sentinel_script},
    'label': 'TEST text'
})

# code with script, noRoot true
id3 = secrets.token_hex(3)
new_els.append({
    'id': id3, 'name': 'code', 'parent': parent_id, 'children': [],
    'settings': {'code': sentinel_script, 'noRoot': True, 'executeCode': True},
    'label': 'TEST code exec'
})

content.extend(new_els)
for e in content:
    if e['id'] == parent_id:
        e.setdefault('children', []).extend([id1, id2, id3])
        break

payload = {'content': content}
req = urllib.request.Request(URL, data=json.dumps(payload).encode(),
    headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'}, method='POST')
resp = json.loads(urllib.request.urlopen(req).read())
print(f"Push: {resp}  inserted ids: {id1}(text-basic) {id2}(text) {id3}(code)")
