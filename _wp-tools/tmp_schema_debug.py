import re, os, glob, json

files = {
    'services_plantation-shutters': '/tmp/cfc_schema/services_plantation-shutters.html',
    'areas_west-st-pete': '/tmp/cfc_schema/areas_west-st-pete.html',
    'about': '/tmp/cfc_schema/about.html',
}
# fallback to windows tmp
import tempfile
td = tempfile.gettempdir()
for k in files:
    if not os.path.exists(files[k]):
        files[k] = os.path.join(td, 'cfc_schema', k + '.html')

# 1) Dump services parse error context
html = open(files['services_plantation-shutters'], encoding='utf-8', errors='ignore').read()
blocks = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.DOTALL)
print('=== services/plantation-shutters block 2 raw around error ===')
b2 = blocks[1].strip()
print(f'length: {len(b2)}')
print('around char 2020-2080:')
print(repr(b2[2000:2100]))
print('\n--- first 600 chars ---')
print(b2[:600])
print('\n--- last 400 chars ---')
print(b2[-400:])

# 2) west-st-pete LocalBusiness full detail
print('\n\n=== west-st-pete LocalBusiness full ===')
html2 = open(files['areas_west-st-pete'], encoding='utf-8', errors='ignore').read()
blocks2 = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html2, re.DOTALL)
for b in blocks2:
    if '"LocalBusiness"' in b or '"#location"' in b:
        try:
            d = json.loads(b.strip())
            # find the LocalBusiness node
            def find(o):
                if isinstance(o, dict):
                    if o.get('@type') == 'LocalBusiness':
                        print(json.dumps(o, indent=2, ensure_ascii=False)[:2500])
                        return
                    for v in o.values():
                        find(v)
                elif isinstance(o, list):
                    for x in o:
                        find(x)
            find(d)
        except Exception as e:
            print('err', e)

# 3) about Organization node
print('\n\n=== about Organization node ===')
html3 = open(files['about'], encoding='utf-8', errors='ignore').read()
blocks3 = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html3, re.DOTALL)
for b in blocks3:
    if '"#organization"' in b:
        d = json.loads(b.strip())
        def find_org(o):
            if isinstance(o, dict):
                if o.get('@type') == 'Organization' and o.get('@id','').endswith('#organization'):
                    print(json.dumps(o, indent=2, ensure_ascii=False)[:2000])
                    return
                for v in o.values():
                    find_org(v)
            elif isinstance(o, list):
                for x in o:
                    find_org(x)
        find_org(d)
