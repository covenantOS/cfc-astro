import os
"""Look at page 524 for:
1. Existing area mentions (where we could add WSP contextually)
2. Em-dashes on page 524 and 580 (H8)
3. Founding-date mentions (2000 / 2007 / since / years)
"""
import json, urllib.request, base64, re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()

def fetch(pid):
    req = urllib.request.Request(
        f'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/{pid}',
        headers={'Authorization': f'Basic {auth}'})
    return json.loads(urllib.request.urlopen(req, timeout=20).read())

def scan(pid, label):
    d = fetch(pid)
    content = d['content']
    print(f'\n=== {label} (page {pid}, {len(content)} elements) ===')
    area_hits = []
    emdash_hits = []
    year_hits = []
    for e in content:
        s = e.get('settings', {}) or {}
        for k in ('text','title','subtitle','heading'):
            v = s.get(k)
            if not isinstance(v, str): continue
            # Area mentions
            for city in ['Old Northeast', 'Snell Isle', 'Shore Acres', 'Downtown', 'Tierra Verde', 'St. Pete Beach', 'Seminole', 'Clearwater', 'Sand Key', 'Belleair', 'Treasure Island', 'St. Petersburg', 'West St', 'Kenwood', 'Grand Central']:
                if city in v:
                    area_hits.append((e['id'], e.get('name'), k, city, v[:150]))
                    break
            # Em-dashes
            if '\u2014' in v:
                count = v.count('\u2014')
                emdash_hits.append((e['id'], e.get('name'), k, count, v[:200]))
            # Founding year mentions (2000, 2007, or 'since/years')
            if re.search(r'\b(2000|2005|2006|2007|two decades?|25\+?\s*years?|19\s*years?|18\s*years?|20\s*years?)\b', v, re.IGNORECASE):
                match = re.search(r'\b(2000|2005|2006|2007|two decades?|25\+?\s*years?|19\s*years?|18\s*years?|20\s*years?)\b', v, re.IGNORECASE)
                year_hits.append((e['id'], e.get('name'), k, match.group(0), v[:200]))
    print(f'  Area mentions: {len(area_hits)}')
    for h in area_hits[:6]:
        print(f'    id={h[0]} [{h[1]}] field={h[2]} city={h[3]!r}')
        print(f'      text: {h[4]!r}')
    print(f'  Em-dash elements: {len(emdash_hits)}')
    for h in emdash_hits[:10]:
        print(f'    id={h[0]} [{h[1]}] count={h[3]}')
        print(f'      text: {h[4]!r}')
    print(f'  Founding/year mentions: {len(year_hits)}')
    for h in year_hits[:10]:
        print(f'    id={h[0]} [{h[1]}] matched={h[3]!r}')
        print(f'      text: {h[4]!r}')
    return d

scan(524, 'SERVICES/PLANTATION-SHUTTERS')
scan(580, 'AREAS/SNELL-ISLE')
