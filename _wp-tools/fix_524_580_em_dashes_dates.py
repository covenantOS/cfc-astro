import os
"""H8 + H9: Strip em-dashes and normalize founding date to 2007 on pages
524 (services/plantation-shutters) and 580 (areas/snell-isle).

H8 rule: replace ' — X' (U+2014 and &mdash;) with:
  - ': X' when following word is capitalized (label/heading pattern)
  - ', X' when following word is lowercase (prose continuation)

H9 rule: founding year is 2007 (Daniel's memory). 2026 - 2007 = 19y, so
'over two decades' -> 'nearly two decades'. Fix 'Since 2000', '25 years',
'Twenty-five years' references.

Skips the schema element abe9b6 on page 524 (JSON-LD already hand-fixed).
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


def replace_em_dashes(text):
    # U+2014 with optional surrounding whitespace
    text = re.sub(r'\s*\u2014\s+(?=[A-Z])', ': ', text)
    text = re.sub(r'\s*\u2014\s+(?=[a-z0-9])', ', ', text)
    # &mdash; HTML entity
    text = re.sub(r'\s*&mdash;\s+(?=[A-Z])', ': ', text)
    text = re.sub(r'\s*&mdash;\s+(?=[a-z0-9])', ', ', text)
    return text


def apply_date_fixes(text):
    # Explicit "Since 2000" heading
    text = re.sub(r'\bSince\s+2000\b', 'Since 2007', text)
    # Narrative forms of 25 years
    text = re.sub(r'\bfor\s+25\+?\s*years\b', 'since 2007', text, flags=re.IGNORECASE)
    text = re.sub(r'\b25\+?\s*years\s+of\b', 'since 2007,', text, flags=re.IGNORECASE)
    # Long-form "Twenty-five years"
    text = re.sub(r'\bTwenty-five\s+years\b', 'Since 2007, nearly two decades', text)
    text = re.sub(r'\btwenty-five\s+years\b', 'since 2007, nearly two decades', text)
    # "over two decades" (2026-2007=19y -> not yet two)
    text = re.sub(r'\bover\s+two\s+decades\b', 'nearly two decades', text, flags=re.IGNORECASE)
    return text


TARGETS = {
    524: ['5c9c3e', 'caeb7e', 'd361f8', '1e0be8', '435fab', '9d8b84', '4b234e'],
    580: ['42d673'],
}

# Fields to consider (skip URL/class/id fields)
TEXT_FIELDS = {'text', 'title', 'subtitle', 'heading', 'content', 'description',
               'label', 'excerpt', 'caption', 'badge'}

ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

for pid, target_ids in TARGETS.items():
    print(f'\n=== Page {pid} ===')
    d = fetch(pid)
    content = d['content']

    with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_{pid}_{ts}_pre_h8_h9.json', 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2)

    by_id = {e['id']: e for e in content}
    changes = 0
    em_before_total = 0
    em_after_total = 0

    for eid in target_ids:
        e = by_id.get(eid)
        if not e:
            print(f'  {eid}: NOT FOUND'); continue
        s = e.get('settings', {}) or {}
        for k, v in list(s.items()):
            if k not in TEXT_FIELDS: continue
            if not isinstance(v, str): continue
            em_before = v.count('\u2014') + v.count('&mdash;')
            new_v = replace_em_dashes(v)
            new_v = apply_date_fixes(new_v)
            em_after = new_v.count('\u2014') + new_v.count('&mdash;')
            em_before_total += em_before
            em_after_total += em_after
            if new_v != v:
                s[k] = new_v
                changes += 1
                print(f'\n  {eid}.{k}: em-dashes {em_before} -> {em_after}')
                # Line-by-line diff where different
                for lb, la in zip(v.split('\n'), new_v.split('\n')):
                    if lb != la:
                        print(f'    - {lb[:160]!r}')
                        print(f'    + {la[:160]!r}')

    print(f'\n  Total fields changed: {changes}, em-dashes on targets {em_before_total} -> {em_after_total}')
    if changes > 0:
        resp = push(pid, content)
        print(f'  PUSH: {resp}')
    else:
        print(f'  No changes — skipping push.')

print('\nDone.')
