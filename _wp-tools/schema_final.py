import os
"""Final schema injection — use text-basic element (confirmed to render raw <script> tags)."""
import json, urllib.request, base64, datetime, secrets, re

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
URL = 'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/524'
PAGE_URL = 'https://www.customfabriccreations.net/services/plantation-shutters/'

req = urllib.request.Request(URL, headers={'Authorization': f'Basic {auth}'})
d = json.loads(urllib.request.urlopen(req).read())
content = d['content']

ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_524_{ts}_pre_schema_final.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)

# Purge all test sentinels + prior failed schema attempts
remove_ids = set()
for e in content:
    s = str(e.get('settings', {})).lower()
    if 'cfc_test_sentinel' in s:
        remove_ids.add(e['id'])
    # dead code/html attempts
    if e.get('name') in ('code','html') and ('plantation shutter' in s or 'localbusiness' in s):
        remove_ids.add(e['id'])

print(f"Removing {len(remove_ids)} dead/test elements: {remove_ids}")
content = [e for e in content if e['id'] not in remove_ids]
for e in content:
    if 'children' in e:
        e['children'] = [c for c in e['children'] if c not in remove_ids]

by_id = {e['id']: e for e in content}

# Build schema
with open(r'C:\Users\Willb\Claude\CFC\faqs_extracted.json', encoding='utf-8') as fp:
    faqs = json.load(fp)

def strip_html(s):
    s = re.sub(r'<[^>]+>','', s)
    s = s.replace('&ndash;','–').replace('&mdash;','—').replace('&frac12;','½').replace('&times;','×')
    s = s.replace('&rsquo;','\u2019').replace('&lsquo;','\u2018').replace('&amp;','&').replace('&nbsp;',' ')
    return re.sub(r'\s+',' ', s).strip()

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

schema_json = json.dumps(schema, ensure_ascii=False, separators=(',',':'))
script_block = f'<script type="application/ld+json">{schema_json}</script>'

new_id = secrets.token_hex(3)
parent_id = '9d29a5'
new_el = {
    'id': new_id, 'name': 'text-basic', 'parent': parent_id, 'children': [],
    'settings': {'text': script_block, 'tag': 'custom', 'customTag': 'div'},
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
print(f"Push: {resp}  elements: {len(content)}  new schema el: {new_id}")
