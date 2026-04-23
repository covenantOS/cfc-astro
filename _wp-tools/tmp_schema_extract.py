import re, json, os, glob

files = sorted(glob.glob('/tmp/cfc_schema/*.html'))
# Windows path fallback
if not files:
    import tempfile
    td = tempfile.gettempdir()
    files = sorted(glob.glob(os.path.join(td, 'cfc_schema', '*.html')))

for f in files:
    name = os.path.basename(f).replace('.html','')
    print(f'\n================ {name} ================')
    html = open(f, encoding='utf-8', errors='ignore').read()
    blocks = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.DOTALL)
    print(f'JSON-LD blocks: {len(blocks)}')
    for i, b in enumerate(blocks):
        body = b.strip()
        try:
            data = json.loads(body)
        except Exception as e:
            print(f'  Block {i+1} PARSE ERROR: {e}')
            print(f'    first 200: {body[:200]}')
            continue
        print(f'\n  --- Block {i+1} ---')
        def walk(obj, depth=1):
            pad = '  ' * depth
            if isinstance(obj, dict):
                t = obj.get('@type', '?')
                aid = obj.get('@id', '')
                nm = obj.get('name') or obj.get('headline') or ''
                if isinstance(nm, str):
                    nm = nm[:70]
                print(f'{pad}@type={t}  @id={aid}  name="{nm}"')
                # key fields for validation
                for k in ('url','telephone','address','geo','openingHoursSpecification','datePublished','dateModified','logo','sameAs','areaServed','serviceType','jobTitle'):
                    if k in obj:
                        v = obj[k]
                        if isinstance(v, (dict, list)):
                            print(f'{pad}  [{k}] present ({type(v).__name__})')
                        else:
                            sv = str(v)[:60]
                            print(f'{pad}  [{k}] = {sv}')
                # references
                for k in ('provider','publisher','author','mainEntity','location','founder','owner','worksFor','parentOrganization','isPartOf'):
                    if k in obj:
                        v = obj[k]
                        if isinstance(v, dict):
                            ref = v.get('@id') or v.get('@type','')
                            print(f'{pad}  -> {k} ref: {ref}')
                        elif isinstance(v, list):
                            for x in v:
                                if isinstance(x, dict):
                                    ref = x.get('@id') or x.get('@type','')
                                    print(f'{pad}  -> {k}[]: {ref}')
                if '@graph' in obj:
                    print(f'{pad}  @graph ({len(obj["@graph"])} nodes):')
                    for g in obj['@graph']:
                        walk(g, depth+2)
                # mainEntity array for FAQPage
                if obj.get('@type') == 'FAQPage' and isinstance(obj.get('mainEntity'), list):
                    print(f'{pad}  FAQ questions: {len(obj["mainEntity"])}')
                # HowTo steps
                if obj.get('@type') == 'HowTo' and 'step' in obj:
                    print(f'{pad}  HowTo steps: {len(obj["step"]) if isinstance(obj["step"],list) else 1}')
            elif isinstance(obj, list):
                for x in obj:
                    walk(x, depth)
        walk(data)
