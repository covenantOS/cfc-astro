import os
"""
Area page fixes + schema injection.
1. Fix Snell Isle ca4cac wrong-geo bug (Brandon/Valrico/Hillsborough -> Snell Isle accurate copy).
2. Inject one scoped Service JSON-LD schema per area page (areaServed = specific neighborhood,
   provider references West St Pete LocalBusiness @id).
3. Use text-basic element (confirmed renders raw <script> in Bricks).
"""
import json, urllib.request, base64, datetime, secrets

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
BASE = 'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks'

BIZ_ID = 'https://www.customfabriccreations.net/areas/west-st-pete/#location'
PHONE = '+1-352-266-1262'
LOC_URL = 'https://www.customfabriccreations.net/areas/west-st-pete/'

# Each area: (page_id, neighborhood_name, specific_landmarks_one_line, lat, lng)
AREAS = [
    (1346, 'West St. Pete', 'Central Ave corridor, Grand Central District, Kenwood, Historic Kenwood', 27.7716, -82.6862),
    (1023, 'Largo', 'Pinellas Park border, Ulmerton Road corridor, East Bay', 27.9094, -82.7873),
    (567,  'Tierra Verde', 'Pinellas Point Causeway, Maximo Marina, Fort De Soto approach', 27.6895, -82.7240),
    (573,  'Downtown St. Pete', 'Central Ave downtown, Beach Drive, Pier District, Mirror Lake', 27.7705, -82.6395),
    (574,  'Sand Key', 'Gulf-front condos, Clearwater Pass, Sand Key Park', 27.9670, -82.8276),
    (575,  'St. Petersburg', 'Downtown, Grand Central, Euclid-St. Paul, Crescent Lake, Jungle Prada', 27.7676, -82.6403),
    (576,  'Belleair Shore', 'Gulf Blvd homes, Indian Rocks Beach border, Belleair Country Club', 27.9217, -82.8386),
    (577,  'Treasure Island', 'Sunset Beach, Isle of Capri, 107th Ave boat access, Causeway Blvd', 27.7693, -82.7687),
    (578,  'Old Northeast', 'Coffee Pot Bayou, Vinoy Park, North Shore, 5th Ave N bungalows', 27.7862, -82.6306),
    (579,  'Shore Acres', 'Bayou Grande, Weedon Island approach, Coffee Pot Blvd, 62nd Ave NE', 27.8140, -82.6198),
    (580,  'Snell Isle', 'Snell Isle Blvd, Brightwaters Blvd, Venetian Isles adjacent, Coffee Pot Blvd', 27.7962, -82.6293),
    (581,  'Seminole', 'Seminole City Park, Park Blvd, 113th St N, Lake Seminole', 27.8392, -82.7909),
    (582,  'Clearwater', 'Clearwater Beach, Island Estates, downtown Cleveland Street, Morningside', 27.9659, -82.8001),
    (583,  'St. Pete Beach', 'Pass-a-Grille, Vina del Mar, Don CeSar area, Corey Causeway', 27.7253, -82.7428),
]

def fetch(pid):
    req = urllib.request.Request(f'{BASE}/{pid}', headers={'Authorization': f'Basic {auth}'})
    return json.loads(urllib.request.urlopen(req).read())

def push(pid, content):
    req = urllib.request.Request(f'{BASE}/{pid}', data=json.dumps({'content': content}).encode(),
        headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'}, method='POST')
    return json.loads(urllib.request.urlopen(req).read())

ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

# Snell Isle ca4cac replacement — real, specific, no AI tells, no em dashes
SNELL_FIX = (
    "Looking for plantation shutters or custom window treatments in Snell Isle? "
    "Our team at Custom Fabric Creations has been measuring and installing along "
    "Snell Isle Boulevard, Brightwaters, and the streets off Coffee Pot Boulevard for years. "
    "We handle the waterfront setup challenges specific to this neighborhood, deep window "
    "returns in the older estate homes, salt exposure on the bayfront sides, custom arch tops "
    "and transoms on the Mediterranean Revival houses near the Vinoy Golf Club. "
    "Shutters here hold up to the humidity when you pick the right material, and we'll walk "
    "through faux wood versus basswood in person so you're not guessing."
)

report = []

for pid, name, landmarks, lat, lng in AREAS:
    d = fetch(pid)
    content = d['content']
    by_id = {e['id']: e for e in content}

    with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_{pid}_{ts}_pre_area_push.json', 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2)

    changes = []

    # 1. Snell Isle content bug
    if pid == 580 and 'ca4cac' in by_id:
        el = by_id['ca4cac']
        cur = el.get('settings', {}).get('text', '')
        if 'brandon' in cur.lower() or 'valrico' in cur.lower():
            el['settings']['text'] = SNELL_FIX
            changes.append('fixed ca4cac wrong-geo text')

    # 2. Scoped Service JSON-LD schema
    page_url = f'https://www.customfabriccreations.net/areas/{[a[2] for a in [(1346,"West St. Pete","west-st-pete"),(1023,"Largo","largo"),(567,"Tierra Verde","tierra-verde"),(573,"Downtown St. Pete","downtown-st-pete"),(574,"Sand Key","sand-key"),(575,"St. Petersburg","st-petersburg"),(576,"Belleair Shore","belleair-shore"),(577,"Treasure Island","treasure-island"),(578,"Old Northeast","old-northeast"),(579,"Shore Acres","shore-acres"),(580,"Snell Isle","snell-isle"),(581,"Seminole","seminole"),(582,"Clearwater","clearwater"),(583,"St. Pete Beach","st-pete-beach")] if a[0]==pid][0]}/'

    schema = [
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": f"Custom Plantation Shutters and Window Treatments in {name}",
            "serviceType": ["Plantation Shutters", "Custom Drapery", "Roman Shades", "Custom Blinds", "Reupholstery"],
            "description": f"Custom window treatment and upholstery service for {name} homes. Plantation shutters, drapery, Roman shades, solar shades, and reupholstery measured and installed by a local workroom. Landmarks served: {landmarks}.",
            "url": page_url,
            "provider": {
                "@type": "LocalBusiness",
                "@id": BIZ_ID,
                "name": "Custom Fabric Creations \u2013 West St. Pete",
                "telephone": PHONE,
                "url": LOC_URL
            },
            "areaServed": {"@type": "Place", "name": name, "containedInPlace": {"@type": "AdministrativeArea", "name": "Pinellas County, FL"}, "geo": {"@type": "GeoCoordinates", "latitude": lat, "longitude": lng}},
            "offers": {"@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": "25", "highPrice": "60"}
        }
    ]

    # West St. Pete page also gets the canonical LocalBusiness with full NAP
    if pid == 1346:
        schema.append({
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "@id": BIZ_ID,
            "name": "Custom Fabric Creations \u2013 West St. Pete",
            "alternateName": ["Custom Fabric Creations", "CFC West St. Pete"],
            "description": "Custom window treatments, plantation shutters, and upholstery studio on Central Avenue in West St. Petersburg. In-house workroom for drapery, Roman shades, bedding, and reupholstery. Serving St. Petersburg, Pinellas County, and the Tampa Bay area.",
            "url": LOC_URL,
            "telephone": PHONE,
            "priceRange": "$$-$$$",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "3026 Central Ave Suite 551",
                "addressLocality": "St. Petersburg",
                "addressRegion": "FL",
                "postalCode": "33712",
                "addressCountry": "US"
            },
            "geo": {"@type": "GeoCoordinates", "latitude": 27.7716, "longitude": -82.6862},
            "openingHoursSpecification": [
                {"@type": "OpeningHoursSpecification",
                 "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
                 "opens": "08:00", "closes": "20:00"}
            ],
            "areaServed": [{"@type": "City", "name": "St. Petersburg"},
                           {"@type": "City", "name": "Clearwater"},
                           {"@type": "AdministrativeArea", "name": "Pinellas County"}],
            "makesOffer": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Plantation Shutters"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Custom Drapery"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Roman Shades"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Reupholstery"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Custom Bedding"}}
            ]
        })

    schema_json = json.dumps(schema, ensure_ascii=False, separators=(',',':'))
    script_block = f'<script type="application/ld+json">{schema_json}</script>'

    # Attach to root <article> wrapper's first section (or just first root section)
    # Look for "Article Wrapper" div or first section
    root = None
    for e in content:
        if e.get('parent') in (0, '', None) and (e.get('label') == 'Article Wrapper <article>' or e.get('name') == 'div'):
            root = e; break
    if root is None:
        # fallback — first root section
        for e in content:
            if e.get('parent') in (0, '', None):
                root = e; break

    # Skip if schema already present (idempotent)
    already_has_schema = False
    for e in content:
        if e.get('name') == 'text-basic':
            t = e.get('settings', {}).get('text', '')
            if isinstance(t, str) and 'application/ld+json' in t and f'"@type":"Service"' in t.replace(' ', '') and name.replace(' ','').lower() in t.replace(' ','').lower():
                already_has_schema = True
                break

    if not already_has_schema:
        new_id = secrets.token_hex(3)
        new_el = {
            'id': new_id, 'name': 'text-basic', 'parent': root['id'], 'children': [],
            'settings': {'text': script_block, 'tag': 'custom', 'customTag': 'div'},
            'label': f'SEO Schema {name}'
        }
        content.append(new_el)
        root.setdefault('children', []).append(new_id)
        changes.append(f'added Service schema id={new_id}' + (' + LocalBusiness' if pid == 1346 else ''))

    if changes:
        resp = push(pid, content)
        print(f"[{pid}] {name}: {', '.join(changes)} -> {resp.get('ok', resp)}")
        report.append((pid, name, changes, resp))
    else:
        print(f"[{pid}] {name}: no changes needed")

print(f"\n=== Done. {len(report)} pages updated. ===")
