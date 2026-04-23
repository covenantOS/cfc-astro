import os
"""Page 524 consolidated fix:

H8 (full sweep): strip em-dashes (U+2014 and &mdash;) across ALL elements
  except abe9b6 (schema JSON-LD) and any element whose content contains
  `<script` (safety guard). Replace with ':' (next word capitalized) or
  ',' (next word lowercase).

H10 (West St. Pete internal link): modify hxhdwa body paragraph:
  - Add 'West St. Pete' to the Pinellas County list, linked to
    /areas/west-st-pete/
  - Also link 'Snell Isle' to /areas/snell-isle/ for bonus cluster
    interlinking (two known area pages with content).
"""
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


SKIP_ELEMENT_IDS = {'abe9b6'}  # schema JSON-LD


def replace_em_dashes(text):
    text = re.sub(r'\s*\u2014\s+(?=[A-Z])', ': ', text)
    text = re.sub(r'\s*\u2014\s+(?=[a-z0-9])', ', ', text)
    text = re.sub(r'\s*&mdash;\s+(?=[A-Z])', ': ', text)
    text = re.sub(r'\s*&mdash;\s+(?=[a-z0-9])', ', ', text)
    return text


def safe_to_replace(element, value):
    """Skip schema/script blocks that must not be regex-modified."""
    if element.get('id') in SKIP_ELEMENT_IDS:
        return False
    if isinstance(value, str) and '<script' in value.lower():
        return False
    return True


TEXT_FIELDS = {'text', 'title', 'subtitle', 'heading', 'content', 'description',
               'label', 'excerpt', 'caption', 'badge'}

ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

d = fetch(524)
content = d['content']

with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_524_{ts}_pre_h8_full_h10.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)

by_id = {e['id']: e for e in content}

# =========================================================================
# H8: Full-page em-dash sweep
# =========================================================================
print('=== H8: full-page em-dash sweep on 524 ===')
h8_changes = 0
h8_dashes_before = 0
h8_dashes_after = 0
for e in content:
    s = e.get('settings') or {}
    for k, v in list(s.items()):
        if k not in TEXT_FIELDS: continue
        if not isinstance(v, str): continue
        if not safe_to_replace(e, v): continue
        em = v.count('\u2014') + v.count('&mdash;')
        if em == 0: continue
        new_v = replace_em_dashes(v)
        em_after = new_v.count('\u2014') + new_v.count('&mdash;')
        h8_dashes_before += em
        h8_dashes_after += em_after
        if new_v != v:
            s[k] = new_v
            h8_changes += 1
            print(f"  {e['id']} [{e.get('name')}].{k}: {em} -> {em_after}")

print(f'\n  H8 total: {h8_changes} fields changed, em-dashes {h8_dashes_before} -> {h8_dashes_after}')

# =========================================================================
# H10: Add West St. Pete (and link Snell Isle) in hxhdwa
# =========================================================================
print('\n=== H10: inject area links into hxhdwa ===')
hxhdwa = by_id.get('hxhdwa')
if not hxhdwa:
    print('  ERROR: hxhdwa not found')
else:
    t_before = hxhdwa['settings'].get('text', '')
    t = t_before

    # Step 1: Insert ", <a href=\"/areas/west-st-pete/\">West St. Pete</a>"
    # after "Downtown St. Pete" — only in the Pinellas County St. Petersburg
    # section to avoid double-inserting.
    if 'West St. Pete' in t or 'west-st-pete' in t:
        print('  West St. Pete already present — skipping insert')
    else:
        # Use a narrow anchor: "Downtown St. Pete, Shore Acres"
        needle = 'Downtown St. Pete, Shore Acres'
        replacement = 'Downtown St. Pete, <a href="/areas/west-st-pete/">West St. Pete</a>, Shore Acres'
        if needle in t:
            t = t.replace(needle, replacement, 1)
            print('  Inserted West St. Pete link')
        else:
            print(f'  WARNING: needle not found: {needle!r}')

    # Step 2: Link Snell Isle — replace first standalone occurrence.
    # Current text has "Snell Isle, Old Northeast" as the opening of the list.
    if '<a href="/areas/snell-isle/">' in t:
        print('  Snell Isle link already present — skipping')
    else:
        needle2 = ' Snell Isle, Old Northeast'
        replacement2 = ' <a href="/areas/snell-isle/">Snell Isle</a>, Old Northeast'
        if needle2 in t:
            t = t.replace(needle2, replacement2, 1)
            print('  Linked Snell Isle -> /areas/snell-isle/')
        else:
            print(f'  WARNING: Snell Isle anchor not found')

    if t != t_before:
        hxhdwa['settings']['text'] = t
        h8_changes += 1  # count it as a push trigger
        print('\n  === hxhdwa text after edit ===')
        print(t[:1400])
    else:
        print('  No changes to hxhdwa')

# =========================================================================
# Push + verify
# =========================================================================
if h8_changes > 0:
    print(f'\n=== Pushing 524 ===')
    resp = push(524, content)
    print(f'  PUSH: {resp}')

    # Post-verify
    print('\n=== Post-verify ===')
    d2 = fetch(524)
    total_em = 0
    for e in d2['content']:
        if e.get('id') in SKIP_ELEMENT_IDS: continue
        s = e.get('settings') or {}
        for k, v in s.items():
            if not isinstance(v, str) or '<script' in v.lower(): continue
            total_em += v.count('\u2014') + v.count('&mdash;')
    print(f'  Residual em-dashes on 524 (excl schema/scripts): {total_em}')

    # Check West St. Pete link
    by_id2 = {e['id']: e for e in d2['content']}
    hxhdwa2 = by_id2.get('hxhdwa')
    if hxhdwa2:
        tt = hxhdwa2['settings'].get('text', '')
        has_wsp = 'west-st-pete' in tt
        has_snell = 'snell-isle' in tt
        print(f'  hxhdwa has West St. Pete link: {has_wsp}')
        print(f'  hxhdwa has Snell Isle link: {has_snell}')
else:
    print('\nNo changes; skipping push.')
