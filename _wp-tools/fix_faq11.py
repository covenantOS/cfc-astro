import os
"""Fix FAQ 11 wrong answer — clone of FAQ 1 text block that didn't get replaced."""
import json, urllib.request, base64, datetime
auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()

# Fetch live
req = urllib.request.Request('https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/524', headers={'Authorization': f'Basic {auth}'})
d = json.loads(urllib.request.urlopen(req).read())
content = d['content']
by_id = {e['id']: e for e in content}

# Backup
ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_524_{ts}_pre_faq11_fix.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)

# Walk FAQ 11 wrapper b33399
def walk(eid, depth=0, lines=None):
    if lines is None:
        lines = []
    e = by_id.get(eid)
    if not e:
        return lines
    s = e.get('settings', {}) or {}
    text_preview = ''
    if isinstance(s, dict) and 'text' in s:
        t = s.get('text','')
        if isinstance(t, str):
            text_preview = t[:100]
    lines.append(f"{'  '*depth}[{e['name']}] id={eid} text={text_preview!r}")
    for c in e.get('children', []):
        walk(c, depth+1, lines)
    return lines

print("=== FAQ 11 wrapper b33399 BEFORE fix ===")
for ln in walk('b33399'):
    print(ln)

# The correct answer for FAQ 11
CORRECT_ANSWER = (
    '<p><span style="font-weight: 400;">Short answer: solar shades, cellular (honeycomb) blinds, or '
    'faux wood 2&frac12;-inch blinds &mdash; all run <b>$150&ndash;$400 per window installed</b> '
    'versus $300&ndash;$1,200+ for plantation shutters. That&rsquo;s 40&ndash;60% less upfront.</span></p>'
    '<p><span style="font-weight: 400;">The catch: blinds and shades typically need replacement every '
    '5&ndash;8 years in Florida conditions (sun-brittle cords, warped vanes, yellowed cells). '
    'Plantation shutters last 15&ndash;20 years. Run the 20-year math and shutters win &mdash; but if '
    'cash flow is tight <i>right now</i> or you plan to move within 3&ndash;5 years, quality faux wood '
    '2&frac12;-inch blinds are a legitimate step down that still looks intentional.</span></p>'
    '<p><span style="font-weight: 400;">We install all three categories, so the recommendation '
    'depends on your budget, tenure in the home, and aesthetic. Ask for a side-by-side quote.</span></p>'
)

# Find the text-basic element(s) inside FAQ 11 that carry the wrong answer text
def find_texts(eid, results=None):
    if results is None:
        results = []
    e = by_id.get(eid)
    if not e:
        return results
    if e['name'] in ('text-basic','text'):
        results.append(eid)
    for c in e.get('children', []):
        find_texts(c, results)
    return results

text_ids = find_texts('b33399')
print(f"\nText elements inside FAQ 11: {text_ids}")

if len(text_ids) >= 1:
    # Replace the first/primary text element with correct answer
    target = text_ids[0]
    old = by_id[target].get('settings', {}).get('text','')[:120]
    print(f"\nReplacing text in {target}. Old preview: {old!r}")
    by_id[target]['settings']['text'] = CORRECT_ANSWER
    # If there are additional text elements (leftover clones), strip their text
    for extra in text_ids[1:]:
        by_id[extra]['settings']['text'] = ''
        print(f"Cleared extra text element {extra}")

# Push
new_content = list(by_id.values())
# Preserve original ordering via original content list
orig_order = [e['id'] for e in content]
new_content_ordered = [by_id[eid] for eid in orig_order]

payload = {'content': new_content_ordered}
req = urllib.request.Request(
    'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/524',
    data=json.dumps(payload).encode(),
    headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'},
    method='POST'
)
resp = json.loads(urllib.request.urlopen(req).read())
print(f"\nPush: {resp}")
