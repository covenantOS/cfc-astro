import os
"""Update existing JSON-LD schema (text-basic element abe9b6) with West St. Pete NAP + hours."""
import json, urllib.request, base64, datetime, re

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
URL = 'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/524'
PAGE_URL = 'https://www.customfabriccreations.net/services/plantation-shutters/'
LOC_URL = 'https://www.customfabriccreations.net/west-st-pete'

req = urllib.request.Request(URL, headers={'Authorization': f'Basic {auth}'})
d = json.loads(urllib.request.urlopen(req).read())
content = d['content']
by_id = {e['id']: e for e in content}

ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_524_{ts}_pre_nap_update.json','w',encoding='utf-8') as f:
    json.dump(d, f, indent=2)

# Re-pull FAQs from live (ground truth)
faq_parent = by_id.get('b42667')
def strip_html(s):
    s = re.sub(r'<[^>]+>','', s)
    s = s.replace('&ndash;','–').replace('&mdash;','—').replace('&frac12;','½').replace('&times;','×')
    s = s.replace('&rsquo;','\u2019').replace('&lsquo;','\u2018').replace('&amp;','&').replace('&nbsp;',' ')
    return re.sub(r'\s+',' ', s).strip()

faqs_clean = []
for wid in faq_parent.get('children', []):
    w = by_id.get(wid)
    if not w: continue
    q = None; a_parts = []
    stack = [wid]
    while stack:
        eid = stack.pop(0)
        e = by_id.get(eid)
        if not e: continue
        s = e.get('settings', {}) or {}
        if e['name'] == 'heading' and 'text' in s and q is None:
            q = s['text']
        elif e['name'] in ('text-basic','text') and 'text' in s:
            a_parts.append(s['text'])
        stack.extend(e.get('children', []))
    if q:
        faqs_clean.append({'q': strip_html(q), 'a': strip_html(' '.join(a_parts))})
print(f"FAQs rebuilt from live: {len(faqs_clean)}")

# West St. Pete NAP
BIZ_ID = 'https://www.customfabriccreations.net/west-st-pete#location'
PHONE = '+1-352-266-1262'

schema = [
    {
        "@context": "https://schema.org", "@type": "Service",
        "name": "Custom Plantation Shutters Installation",
        "serviceType": "Plantation Shutters",
        "description": "Custom plantation shutter design, measurement, manufacture, and installation serving St. Petersburg and Pinellas County. Faux wood, basswood, hybrid composite, specialty shapes, French doors, sliders, bay/bow windows.",
        "url": PAGE_URL,
        "provider": {"@type": "LocalBusiness", "@id": BIZ_ID,
                     "name": "Custom Fabric Creations — West St. Pete",
                     "telephone": PHONE, "url": LOC_URL},
        "areaServed": [
            {"@type": "City", "name": "St. Petersburg"},
            {"@type": "AdministrativeArea", "name": "Pinellas County"},
            {"@type": "Place", "name": "Snell Isle"}, {"@type": "Place", "name": "Old Northeast"},
            {"@type": "Place", "name": "Downtown St. Pete"}, {"@type": "Place", "name": "Shore Acres"},
            {"@type": "Place", "name": "Tierra Verde"}, {"@type": "Place", "name": "St. Pete Beach"},
            {"@type": "Place", "name": "Treasure Island"}, {"@type": "Place", "name": "Sand Key"},
            {"@type": "Place", "name": "Belleair"}, {"@type": "Place", "name": "Seminole"},
            {"@type": "Place", "name": "Largo"}, {"@type": "Place", "name": "Clearwater"},
            {"@type": "Place", "name": "Gulfport"}
        ],
        "offers": {"@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": "25", "highPrice": "60"}
    },
    {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": f['q'],
                        "acceptedAnswer": {"@type": "Answer", "text": f['a']}} for f in faqs_clean]
    },
    {
        "@context": "https://schema.org", "@type": "LocalBusiness",
        "@id": BIZ_ID,
        "name": "Custom Fabric Creations — West St. Pete",
        "alternateName": ["Custom Fabric Creations", "CFC West St. Pete"],
        "description": "Custom window treatments, plantation shutters, and upholstery studio in West St. Petersburg. In-house workroom for drapery, Roman shades, bedding, and reupholstery. Serving St. Petersburg, Pinellas County, and the greater Tampa Bay area.",
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
             "opens": "08:00", "closes": "20:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "00:00", "closes": "00:00"}
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
    }
]

schema_json = json.dumps(schema, ensure_ascii=False, separators=(',',':'))
script_block = f'<script type="application/ld+json">{schema_json}</script>'

# Update existing schema element abe9b6
target = by_id.get('abe9b6')
if not target:
    print("Schema element abe9b6 not found; aborting")
    raise SystemExit()
target['settings']['text'] = script_block

payload = {'content': content}
req = urllib.request.Request(URL, data=json.dumps(payload).encode(),
    headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'}, method='POST')
resp = json.loads(urllib.request.urlopen(req).read())
print(f"Push: {resp}")
