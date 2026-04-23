import os
"""Inject Service + FAQPage + LocalBusiness JSON-LD via a Bricks code element on the plantation shutters page."""
import json, urllib.request, base64, datetime, secrets

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
URL = 'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/524'
PAGE_URL = 'https://www.customfabriccreations.net/services/plantation-shutters/'

# Fetch live
req = urllib.request.Request(URL, headers={'Authorization': f'Basic {auth}'})
d = json.loads(urllib.request.urlopen(req).read())
content = d['content']
by_id = {e['id']: e for e in content}

# Backup
ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_524_{ts}_pre_schema.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)
print(f"Backup saved")

# Load extracted FAQs
with open(r'C:\Users\Willb\Claude\CFC\faqs_extracted.json', encoding='utf-8') as fp:
    faqs = json.load(fp)

# Strip HTML for schema Q/A — schema.org Answer.text accepts HTML but plain text is cleaner
import re
def strip_html(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = s.replace('&ndash;', '–').replace('&mdash;', '—').replace('&frac12;', '½')
    s = s.replace('&times;', '×').replace('&rsquo;', '\u2019').replace('&lsquo;', '\u2018')
    s = s.replace('&amp;', '&').replace('&nbsp;', ' ')
    return re.sub(r'\s+', ' ', s).strip()

# Pull the current FAQ 11 answer fresh (we just fixed it)
faqs_clean = []
for f in faqs:
    q = strip_html(f['q'])
    a = strip_html(f['a'])
    # FAQ 11 was just fixed — re-pull from the live by_id rather than the stale json
    faqs_clean.append({'q': q, 'a': a})

# Rebuild FAQ 11 answer from current live content (b33399 / df3973)
fq11 = by_id.get('df3973', {}).get('settings', {}).get('text', '')
if fq11 and faqs_clean:
    faqs_clean[-1]['a'] = strip_html(fq11)

print(f"FAQs prepared: {len(faqs_clean)}")

# Build schema
schema = [
    {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "Custom Plantation Shutters Installation",
        "serviceType": "Plantation Shutters",
        "description": "Custom plantation shutter design, measurement, manufacture, and installation serving St. Petersburg and Pinellas County. Faux wood and real wood shutters, specialty shapes, French doors, sliders, and bay/bow windows.",
        "url": PAGE_URL,
        "provider": {
            "@type": "LocalBusiness",
            "@id": "https://www.customfabriccreations.net/#localbusiness",
            "name": "Custom Fabric Creations",
            "telephone": "+1-727-240-4512",
            "url": "https://www.customfabriccreations.net/"
        },
        "areaServed": [
            {"@type": "City", "name": "St. Petersburg", "containedInPlace": {"@type": "State", "name": "Florida"}},
            {"@type": "AdministrativeArea", "name": "Pinellas County"},
            {"@type": "Place", "name": "Snell Isle"},
            {"@type": "Place", "name": "Old Northeast"},
            {"@type": "Place", "name": "Downtown St. Pete"},
            {"@type": "Place", "name": "Shore Acres"},
            {"@type": "Place", "name": "Tierra Verde"},
            {"@type": "Place", "name": "St. Pete Beach"},
            {"@type": "Place", "name": "Treasure Island"},
            {"@type": "Place", "name": "Sand Key"},
            {"@type": "Place", "name": "Belleair"},
            {"@type": "Place", "name": "Seminole"},
            {"@type": "Place", "name": "Largo"},
            {"@type": "Place", "name": "Clearwater"},
            {"@type": "Place", "name": "Gulfport"}
        ],
        "offers": {
            "@type": "AggregateOffer",
            "priceCurrency": "USD",
            "lowPrice": "25",
            "highPrice": "60",
            "priceSpecification": {
                "@type": "UnitPriceSpecification",
                "priceCurrency": "USD",
                "unitText": "square foot installed"
            }
        },
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Plantation Shutter Options",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Faux Wood Plantation Shutters"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Real Wood (Basswood) Plantation Shutters"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Hybrid Wood-Composite Plantation Shutters"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Specialty Shape Shutters (arches, sunbursts, hexagons)"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "French Door Plantation Shutters"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Sliding Bypass Plantation Shutters"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Bay and Bow Window Plantation Shutters"}}
            ]
        }
    },
    {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f['q'],
                "acceptedAnswer": {"@type": "Answer", "text": f['a']}
            } for f in faqs_clean
        ]
    },
    {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": "https://www.customfabriccreations.net/#localbusiness",
        "name": "Custom Fabric Creations",
        "alternateName": "CFC",
        "description": "Custom window treatment, plantation shutter, and upholstery studio serving St. Petersburg and Pinellas County, FL. In-house workroom for drapery, Roman shades, bedding, cushions, and reupholstery.",
        "url": "https://www.customfabriccreations.net/",
        "telephone": "+1-727-240-4512",
        "priceRange": "$$-$$$",
        "image": "https://www.customfabriccreations.net/wp-content/uploads/2024/cfc-logo.png",
        "areaServed": [
            {"@type": "City", "name": "St. Petersburg"},
            {"@type": "City", "name": "Clearwater"},
            {"@type": "AdministrativeArea", "name": "Pinellas County"}
        ],
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": 27.7676,
            "longitude": -82.6403
        },
        "sameAs": [
            "https://www.customfabriccreations.net/"
        ],
        "makesOffer": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Plantation Shutters"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Custom Drapery"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Roman Shades"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Reupholstery"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Custom Bedding"}}
        ]
    }
]

schema_json = json.dumps(schema, ensure_ascii=False)
script_block = f'<script type="application/ld+json">{schema_json}</script>'

# Check if schema code block already exists (idempotent)
existing = None
for e in content:
    if e.get('name') == 'code':
        s = e.get('settings', {}) or {}
        code = s.get('code', '')
        if 'application/ld+json' in code and 'plantation' in code.lower():
            existing = e['id']
            break

if existing:
    print(f"Updating existing schema code element: {existing}")
    by_id[existing]['settings']['code'] = script_block
    by_id[existing]['settings']['executeCode'] = True
    by_id[existing]['settings']['noRoot'] = True
else:
    # Insert new code element at end of main container (or as sibling of main section)
    # Find the first root-level section/container
    root_containers = [e for e in content if e.get('parent') in (0, '0', None)]
    if not root_containers:
        print("No root container found!")
        raise SystemExit()

    # Add to first root section's children (end)
    target_parent = root_containers[0]
    new_id = secrets.token_hex(3)
    new_el = {
        'id': new_id,
        'name': 'code',
        'parent': target_parent['id'],
        'children': [],
        'settings': {
            'code': script_block,
            'executeCode': True,
            'noRoot': True,
            'language': 'html'
        },
        'label': 'SEO JSON-LD Schema'
    }
    content.append(new_el)
    by_id[new_id] = new_el
    if 'children' not in target_parent:
        target_parent['children'] = []
    target_parent['children'].append(new_id)
    print(f"Inserted new schema code element {new_id} into parent {target_parent['id']}")

# Push
payload = {'content': content}
req = urllib.request.Request(
    URL,
    data=json.dumps(payload).encode(),
    headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'},
    method='POST'
)
resp = json.loads(urllib.request.urlopen(req).read())
print(f"Push: {resp}")
print(f"Final element count: {len(content)}")
