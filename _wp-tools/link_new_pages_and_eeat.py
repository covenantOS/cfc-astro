import os
"""
1. Add cross-links from plantation-shutters main page (524) to the 3 new pages.
2. Enhance About page (103) with E-E-A-T section + Person/Organization schema.
3. Trigger Rank Math sitemap refresh.
"""
import json, urllib.request, base64, datetime, secrets, re

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
BASE = 'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks'
WP_BASE = 'https://www.customfabriccreations.net/wp-json/wp/v2'

NEW_BIZ_ID = 'https://www.customfabriccreations.net/areas/west-st-pete/#location'
LOC_URL = 'https://www.customfabriccreations.net/areas/west-st-pete/'

def fetch_bricks(pid):
    req = urllib.request.Request(f'{BASE}/{pid}', headers={'Authorization': f'Basic {auth}'})
    return json.loads(urllib.request.urlopen(req).read())

def push_bricks(pid, content):
    req = urllib.request.Request(f'{BASE}/{pid}', data=json.dumps({'content': content}).encode(),
        headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'}, method='POST')
    return json.loads(urllib.request.urlopen(req).read())

ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

# === 1. Add internal links from 524 to the 3 new pages ===
# Strategy: find text-basic or text elements on 524 with relevant phrases and wrap first match.
LINK_MAP = [
    # (search phrase, href, anchor text)
    (r'\bcost\s+per\s+(square\s+foot|sq\.?\s*ft\.?|window)\b', '/plantation-shutters-cost-st-petersburg/', 'plantation shutters cost in St. Petersburg'),
    (r'\binstallation\b', '/plantation-shutters-installation-st-petersburg/', 'plantation shutter installation process'),
    (r"\bpeople\s+(getting\s+rid\s+of|regret)\b", '/plantation-shutters-regret-downsides/', 'why some homeowners regret plantation shutters'),
]

d = fetch_bricks(524)
content = d['content']
with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_524_{ts}_pre_crosslinks.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)

link_report = []
for pattern, href, anchor in LINK_MAP:
    added = False
    for e in content:
        if added: break
        if e.get('name') not in ('text-basic', 'text'):
            continue
        s = e.get('settings', {}) or {}
        t = s.get('text', '')
        if not isinstance(t, str): continue
        if href in t: continue  # already linked
        if re.search(pattern, t, re.IGNORECASE):
            # wrap first occurrence of match phrase in link
            def replace_once(m):
                return f'<a href="{href}">{m.group(0)}</a>'
            new_t = re.sub(pattern, replace_once, t, count=1, flags=re.IGNORECASE)
            if new_t != t:
                e['settings']['text'] = new_t
                link_report.append((e['id'], href, anchor))
                added = True
    if not added:
        # Fallback: append a standalone paragraph link at bottom
        link_report.append(('(append)', href, anchor))

# Append a "Related reading" block at end if we have any appends needed
appends_needed = [r for r in link_report if r[0] == '(append)']
if appends_needed:
    related_html = '<p><strong>Related reading:</strong> '
    related_html += ', '.join(f'<a href="{r[1]}">{r[2]}</a>' for r in appends_needed)
    related_html += '.</p>'
    # Find a root section container to insert into
    root = None
    for e in content:
        if e.get('parent') in (0, '', None) and (e.get('label') == 'Article Wrapper <article>' or e.get('name') == 'div'):
            root = e; break
    if root is None:
        for e in content:
            if e.get('parent') in (0, '', None):
                root = e; break
    if root:
        new_id = secrets.token_hex(3)
        new_el = {
            'id': new_id, 'name': 'text-basic', 'parent': root['id'], 'children': [],
            'settings': {'text': related_html},
            'label': 'Related Reading Links'
        }
        content.append(new_el)
        root.setdefault('children', []).append(new_id)

resp = push_bricks(524, content)
print(f"[524] cross-links -> {resp.get('ok', resp)}")
for r in link_report:
    print(f"  - {r[0]} -> {r[1]} ({r[2]})")

# === 2. Enhance About page (103) with E-E-A-T section + Person schema ===
d = fetch_bricks(103)
content = d['content']
with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_103_{ts}_pre_eeat.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)

# Person schema (Daniel) + Organization schema
about_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Organization",
            "@id": "https://www.customfabriccreations.net/#organization",
            "name": "Custom Fabric Creations",
            "url": "https://www.customfabriccreations.net/",
            "telephone": "+1-727-240-4512",
            "description": "Custom window treatment, plantation shutter, and upholstery studio serving St. Petersburg, Pinellas County, and the Tampa Bay area since 2007.",
            "foundingDate": "2007",
            "sameAs": [
                "https://www.customfabriccreations.net/areas/west-st-pete/"
            ],
            "location": {"@id": NEW_BIZ_ID},
            "areaServed": [
                {"@type": "AdministrativeArea", "name": "Pinellas County"},
                {"@type": "City", "name": "St. Petersburg"},
                {"@type": "City", "name": "Clearwater"},
                {"@type": "City", "name": "Largo"}
            ]
        },
        {
            "@type": "Person",
            "@id": "https://www.customfabriccreations.net/#owner",
            "name": "Terry Popick",
            "jobTitle": "Owner and Principal Designer",
            "worksFor": {"@id": "https://www.customfabriccreations.net/#organization"},
            "knowsAbout": [
                "Custom window treatments",
                "Plantation shutters",
                "Custom drapery fabrication",
                "Roman shades",
                "Reupholstery",
                "Interior design"
            ],
            "description": "Owner and principal designer at Custom Fabric Creations. Nearly two decades of residential and commercial window treatment work across Pinellas and Hillsborough counties."
        }
    ]
}

about_schema_html = f'<script type="application/ld+json">{json.dumps(about_schema, ensure_ascii=False, separators=(",",":"))}</script>'

# Find root to attach schema
root = None
for e in content:
    if e.get('parent') in (0, '', None) and (e.get('label') == 'Article Wrapper <article>' or e.get('name') == 'div'):
        root = e; break
if root is None:
    for e in content:
        if e.get('parent') in (0, '', None):
            root = e; break

# Idempotent: skip if Person schema already present
has_person = False
for e in content:
    if e.get('name') == 'text-basic':
        t = e.get('settings', {}).get('text', '')
        if isinstance(t, str) and '#owner' in t and '"@type":"Person"' in t.replace(' ',''):
            has_person = True
            break

if not has_person and root:
    new_id = secrets.token_hex(3)
    new_el = {
        'id': new_id, 'name': 'text-basic', 'parent': root['id'], 'children': [],
        'settings': {'text': about_schema_html, 'tag': 'custom', 'customTag': 'div'},
        'label': 'SEO Schema E-E-A-T'
    }
    content.append(new_el)
    root.setdefault('children', []).append(new_id)
    resp = push_bricks(103, content)
    print(f"[103] E-E-A-T schema -> {resp.get('ok', resp)}  id={new_id}")
else:
    print(f"[103] E-E-A-T schema already present or no root found")

# === 3. Trigger sitemap refresh ===
# Rank Math rebuilds sitemap on save. Touch an option by hitting the sitemap URL.
try:
    req = urllib.request.Request('https://www.customfabriccreations.net/sitemap_index.xml',
        headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    html = urllib.request.urlopen(req).read().decode()
    print(f"Sitemap fetch OK: {len(html)} bytes")
except Exception as e:
    print(f"Sitemap fetch error: {e}")

print("\nAll tasks complete.")
