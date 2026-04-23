import os
"""Fix C4 (partial): Snell Isle page 580 has wrong phone 352-624-0162 in body.
Replace with 352-266-1262 (matches schema, matches West St. Pete NAP, matches
memory note). Also handle (352) 624-0162 formatted variants."""
import json, urllib.request, base64, datetime, re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()

def fetch(pid):
    req = urllib.request.Request(
        f'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/{pid}',
        headers={'Authorization': f'Basic {auth}'})
    return json.loads(urllib.request.urlopen(req, timeout=20).read())

def push(pid, content):
    req = urllib.request.Request(
        f'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/{pid}',
        data=json.dumps({'content': content}).encode(),
        headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'},
        method='POST')
    return json.loads(urllib.request.urlopen(req, timeout=20).read())

WRONG_PHONES = [
    r'\(352\)\s*624[\s\-\.]?0162',
    r'352[\s\-\.]?624[\s\-\.]?0162',
    r'\+1[\s\-\.]?352[\s\-\.]?624[\s\-\.]?0162',
    r'\+?1?\s*352\.624\.0162',
]
CANON_DISPLAY = '(352) 266-1262'
CANON_TEL = '+1-352-266-1262'

ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
d = fetch(580)
content = d['content']

with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_580_{ts}_pre_phone_fix.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)

total_replacements = 0
changed_elements = []

for e in content:
    s = e.get('settings', {}) or {}
    changed = False
    # Iterate every string value in settings
    for k, v in list(s.items()):
        if not isinstance(v, str): continue
        before = v
        new_v = v
        for patt in WRONG_PHONES:
            # Keep the same format: if input was `tel:+...`, use +1 form; else display
            def sub_fn(m):
                match = m.group(0)
                # If original had +1 prefix, preserve tel format
                if match.strip().startswith('+'):
                    return CANON_TEL
                # If original uses dots, use dotted display; else use ()
                return CANON_DISPLAY
            new_v = re.sub(patt, sub_fn, new_v, flags=re.IGNORECASE)
        if new_v != before:
            s[k] = new_v
            total_replacements += before.count('624-0162') + before.count('624.0162') + before.count('624 0162') + before.count('6240162')
            changed = True
    if changed:
        changed_elements.append(e.get('id'))

print(f'Elements changed: {len(changed_elements)}: {changed_elements}')
print(f'Phone occurrences replaced: {total_replacements}')

if changed_elements:
    resp = push(580, content)
    print(f'PUSH: {resp}')
else:
    print('No changes needed; skipping push.')

# Check post-state
print('\nScanning for residual 624-0162 references...')
residual = 0
for e in content:
    blob = json.dumps(e.get('settings', {}), ensure_ascii=False)
    if '624-0162' in blob or '6240162' in blob or '624.0162' in blob:
        residual += 1
        print(f'  still has it: {e.get("id")}')
print(f'Residual: {residual}')
