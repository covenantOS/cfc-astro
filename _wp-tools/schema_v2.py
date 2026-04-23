import os
"""Retry schema injection — remove dead code element, try 'html' element type which renders raw HTML without code-execution permission."""
import json, urllib.request, base64, datetime, secrets, re

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
URL = 'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/524'
PAGE_URL = 'https://www.customfabriccreations.net/services/plantation-shutters/'

req = urllib.request.Request(URL, headers={'Authorization': f'Basic {auth}'})
d = json.loads(urllib.request.urlopen(req).read())
content = d['content']

ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_524_{ts}_pre_schema_v2.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)

# Remove the dead 'code' element d50b39 from content + its parent's children list
dead_id = 'd50b39'
content = [e for e in content if e['id'] != dead_id]
for e in content:
    if 'children' in e and dead_id in e['children']:
        e['children'] = [c for c in e['children'] if c != dead_id]

# Load FAQs
with open(r'C:\Users\Willb\Claude\CFC\faqs_extracted.json', encoding='utf-8') as fp:
    faqs = json.load(fp)

def strip_html(s):
    s = re.sub(r'<[^>]+>', '', s)
    s = s.replace('&ndash;','–').replace('&mdash;','—').replace('&frac12;','½')
    s = s.replace('&times;','×').replace('&rsquo;','\u2019').replace('&lsquo;','\u2018')
    s = s.replace('&amp;','&').replace('&nbsp;',' ')
    return re.sub(r'\s+',' ', s).strip()

by_id = {e['id']: e for e in content}
fq11_live = by_id.get('df3973', {}).get('settings', {}).get('text', '')
faqs_clean = [{'q': strip_html(f['q']), 'a': strip_html(f['a'])} for f in faqs]
if fq11_live and faqs_clean:
    faqs_clean[-1]['a'] = strip_html(fq11_live)

schema = [
    {
        "@context": "https://schema.org", "@type": "Service",
        "name": "Custom Plantation Shutters Installation",
        "serviceType": "Plantation Shutters",
        "description": "Custom plantation shutter design, measurement, manufacture, and installation serving St. Petersburg and Pinellas County. Faux wood, basswood, hybrid composite, specialty shapes, French doors, sliders, bay/bow windows.",
        "url": PAGE_URL,
        "provider": {"@type": "LocalBusiness", "@id": "https://www.customfabriccreations.net/#localbusiness",
                     "name": "Custom Fabric Creations", "telephone": "+1-727-240-4512",
                     "url": "https://www.customfabriccreations.net/"},
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
        "@id": "https://www.customfabriccreations.net/#localbusiness",
        "name": "Custom Fabric Creations", "alternateName": "CFC",
        "description": "Custom window treatments, plantation shutters, and upholstery studio serving St. Petersburg and Pinellas County, FL.",
        "url": "https://www.customfabriccreations.net/",
        "telephone": "+1-727-240-4512",
        "priceRange": "$$-$$$",
        "areaServed": [{"@type": "City", "name": "St. Petersburg"},
                       {"@type": "City", "name": "Clearwater"},
                       {"@type": "AdministrativeArea", "name": "Pinellas County"}],
        "geo": {"@type": "GeoCoordinates", "latitude": 27.7676, "longitude": -82.6403},
        "makesOffer": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Plantation Shutters"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Custom Drapery"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Roman Shades"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Reupholstery"}}
        ]
    }
]

schema_json = json.dumps(schema, ensure_ascii=False)
script_block = f'<script type="application/ld+json">{schema_json}</script>'

# Try Bricks element name 'html' — renders raw HTML block
new_id = secrets.token_hex(3)
# Place it in the main container 9d29a5 (our known main)
parent_id = '9d29a5' if any(e['id']=='9d29a5' for e in content) else None
if not parent_id:
    # fallback to first root
    for e in content:
        if e.get('parent') in (0, '0', None):
            parent_id = e['id']; break

new_el = {
    'id': new_id,
    'name': 'html',
    'parent': parent_id,
    'children': [],
    'settings': {'code': script_block, 'tag': 'div'},
    'label': 'SEO Schema JSON-LD'
}
content.append(new_el)
for e in content:
    if e['id'] == parent_id:
        e.setdefault('children', []).append(new_id)
        break

payload = {'content': content}
req = urllib.request.Request(URL, data=json.dumps(payload).encode(),
    headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'}, method='POST')
resp = json.loads(urllib.request.urlopen(req).read())
print(f"Push: {resp}  element count: {len(content)}  new element id: {new_id}  parent: {parent_id}")
