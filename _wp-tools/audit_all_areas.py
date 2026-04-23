import os
"""Full audit of all 14 area pages — find content bugs (wrong geo mentions) + schema presence."""
import json, urllib.request, base64, re

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
BASE = 'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks'

AREAS = [
    (1346, 'West St. Pete', 'west-st-pete'),
    (1023, 'Largo', 'largo'),
    (567, 'Tierra Verde', 'tierra-verde'),
    (573, 'Downtown St. Pete', 'downtown-st-pete'),
    (574, 'Sand Key', 'sand-key'),
    (575, 'St. Petersburg', 'st-petersburg'),
    (576, 'Belleair Shore', 'belleair-shore'),
    (577, 'Treasure Island', 'treasure-island'),
    (578, 'Old Northeast', 'old-northeast'),
    (579, 'Shore Acres', 'shore-acres'),
    (580, 'Snell Isle', 'snell-isle'),
    (581, 'Seminole', 'seminole'),
    (582, 'Clearwater', 'clearwater'),
    (583, 'St. Pete Beach', 'st-pete-beach'),
]

# Wrong geo terms that should NOT appear in a St. Pete/Pinellas neighborhood page
WRONG_GEO = ['brandon', 'valrico', 'hillsborough', 'tampa ', 'wesley chapel', 'riverview', 'lutz', 'land o lakes']

def fetch(pid):
    req = urllib.request.Request(f'{BASE}/{pid}', headers={'Authorization': f'Basic {auth}'})
    return json.loads(urllib.request.urlopen(req).read())

def has_schema(content, schema_type):
    for e in content:
        s = e.get('settings', {}) or {}
        text = s.get('text', '')
        if isinstance(text, str) and f'"@type":"{schema_type}"' in text.replace(' ', ''):
            return True
    return False

print(f"{'ID':<6}{'Area':<22}{'Elems':<7}{'Shutter refs':<14}{'Bugs':<6}{'Service Schema'}")
print('-' * 80)

bugs_by_area = {}
for pid, label, slug in AREAS:
    try:
        d = fetch(pid)
        content = d['content']
        shutter_count = 0
        bugs = []
        for e in content:
            s = e.get('settings', {}) or {}
            for field in ('text', 'title', 'subtitle'):
                v = s.get(field)
                if isinstance(v, str):
                    low = v.lower()
                    if 'plantation shutter' in low or 'plantation-shutter' in low:
                        shutter_count += 1
                    for wg in WRONG_GEO:
                        if wg in low:
                            bugs.append((e['id'], e.get('name'), field, wg, v[:160]))
        has_svc = has_schema(content, 'Service')
        has_biz = has_schema(content, 'LocalBusiness')
        print(f"{pid:<6}{label:<22}{len(content):<7}{shutter_count:<14}{len(bugs):<6}Svc:{has_svc} Biz:{has_biz}")
        if bugs:
            bugs_by_area[pid] = bugs
    except Exception as e:
        print(f"{pid:<6}{label:<22}ERROR: {e}")

print('\n\n=== BUG DETAIL ===')
for pid, bugs in bugs_by_area.items():
    print(f"\nPage {pid}:")
    for b in bugs:
        print(f"  {b[0]} [{b[1]}] field={b[2]} wrong_geo={b[3]!r}")
        print(f"    text: {b[4]!r}")
