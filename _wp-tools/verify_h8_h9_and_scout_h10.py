import os
"""Post-fix verification + H10 scouting.

1. Verify 524 and 580 no longer contain em-dashes or old date phrases.
2. Show full text of elements that changed to confirm grammar reads cleanly.
3. Scout page 524 for where to insert a West St. Pete contextual area link:
   - List all elements mentioning St. Petersburg neighborhoods
   - Identify the containing section
   - Check if any <a href> already points to /areas/
"""
import json, urllib.request, base64, re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()

def fetch(pid):
    req = urllib.request.Request(
        f'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/{pid}',
        headers={'Authorization': f'Basic {auth}'})
    return json.loads(urllib.request.urlopen(req, timeout=20).read())

print('=== Verify H8 + H9 on 524 ===')
d524 = fetch(524)
total_em = 0
residual_dates = []
for e in d524['content']:
    s = e.get('settings') or {}
    for k, v in s.items():
        if not isinstance(v, str): continue
        if k == 'code' or 'schema' in (e.get('name') or '').lower():
            continue  # skip schema/code blocks
        em = v.count('\u2014') + v.count('&mdash;')
        if em:
            total_em += em
            print(f"  em-dash residual in {e['id']}.{k} ({e.get('name')}): {em}")
            print(f"    ...{v[:200]}...")
        for patt in [r'\bSince\s+2000\b', r'\bfor\s+25\+?\s*years\b',
                     r'\bTwenty-five\s+years\b', r'\bover\s+two\s+decades\b',
                     r'\b25\s*years\s+of\b']:
            if re.search(patt, v, re.IGNORECASE):
                residual_dates.append((e['id'], k, patt, v[:160]))
print(f'  Total residual em-dashes (non-schema) on 524: {total_em}')
print(f'  Residual date phrases on 524: {len(residual_dates)}')
for r in residual_dates:
    print(f'    {r[0]}.{r[1]} [{r[2]}]: {r[3]!r}')

print('\n=== Verify H8 + H9 on 580 ===')
d580 = fetch(580)
total_em = 0
residual_dates = []
for e in d580['content']:
    s = e.get('settings') or {}
    for k, v in s.items():
        if not isinstance(v, str): continue
        if k == 'code' or 'schema' in (e.get('name') or '').lower():
            continue
        em = v.count('\u2014') + v.count('&mdash;')
        if em:
            total_em += em
            print(f"  em-dash residual in {e['id']}.{k}: {em}")
        for patt in [r'\bover\s+two\s+decades\b', r'\btwo\s+decades\b']:
            if re.search(patt, v, re.IGNORECASE):
                residual_dates.append((e['id'], k, patt, v[:160]))
print(f'  Total residual em-dashes (non-schema) on 580: {total_em}')
print(f'  Residual "two decades" phrases on 580: {len(residual_dates)}')
for r in residual_dates:
    print(f'    {r[0]}.{r[1]} [{r[2]}]: {r[3]!r}')

# Show full text of 4b234e to confirm it reads cleanly
print('\n=== Full text of 524/4b234e (founding-date narrative) ===')
by_id = {e['id']: e for e in d524['content']}
text_4b = (by_id.get('4b234e') or {}).get('settings', {}).get('text', '')
print(text_4b[:1500])

print('\n=== Full text of 524/9d8b84 (workroom heading) ===')
text_9d = (by_id.get('9d8b84') or {}).get('settings', {}).get('text', '')
print(text_9d[:400])

print('\n=== Full text of 580/42d673 (Snell Isle narrative) ===')
by_id_580 = {e['id']: e for e in d580['content']}
text_42 = (by_id_580.get('42d673') or {}).get('settings', {}).get('text', '')
print(text_42[:1500])

# === H10 scouting ===
print('\n\n=== H10 scouting: find where to insert West St. Pete link on 524 ===')
neighborhoods = ['Old Northeast', 'Snell Isle', 'Shore Acres', 'Downtown',
                 'Tierra Verde', 'St. Pete Beach', 'Seminole', 'Clearwater',
                 'Sand Key', 'Belleair', 'Treasure Island', 'West St. Pete',
                 'West St Pete', 'Kenwood', 'Grand Central', 'Historic Kenwood',
                 'Bayway Isles', 'Pinellas Point']
hits = []
for e in d524['content']:
    s = e.get('settings') or {}
    for k, v in s.items():
        if not isinstance(v, str) or not v: continue
        # Look for any neighborhood name
        for n in neighborhoods:
            if n in v:
                parent = e.get('parent')
                hits.append((e['id'], e.get('name'), e.get('label'), parent, k, n, v[:180]))
                break
print(f'\nNeighborhood mentions: {len(hits)}')
for h in hits:
    print(f"  {h[0]} [{h[1]}] parent={h[3]} field={h[4]} hit={h[5]!r}")
    print(f"    text: {h[6]!r}")

# Find all /areas/ href in the page
print('\n\n=== Existing /areas/ links on 524 ===')
area_links = []
for e in d524['content']:
    blob = json.dumps(e.get('settings', {}), ensure_ascii=False)
    for m in re.finditer(r'/areas/[a-z0-9\-]+/?', blob):
        area_links.append((e['id'], e.get('name'), m.group(0)))
for a in area_links:
    print(f"  {a[0]} [{a[1]}] -> {a[2]}")

# Also check existing /services/ cross-links and /contact
print('\n=== Existing /services/ cross-links on 524 ===')
for e in d524['content']:
    blob = json.dumps(e.get('settings', {}), ensure_ascii=False)
    for m in re.finditer(r'/services/[a-z0-9\-]+/?', blob):
        print(f"  {e['id']} [{e.get('name')}] -> {m.group(0)}")
