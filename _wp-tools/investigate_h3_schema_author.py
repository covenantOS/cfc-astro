import os
"""Investigate H3: where is 'daniel' appearing as a schema author?

Scan schema-bearing elements across known pages (524, 103, 580, 1346)
and the live homepage HTML for Article/Person schema with author name
'daniel' (lowercase) instead of 'Terry Popick' (canonical owner).
"""
import json, urllib.request, base64, re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()

def fetch_bricks(pid):
    req = urllib.request.Request(
        f'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/{pid}',
        headers={'Authorization': f'Basic {auth}'})
    return json.loads(urllib.request.urlopen(req, timeout=20).read())

def fetch_html(url):
    req = urllib.request.Request(url)
    return urllib.request.urlopen(req, timeout=30).read().decode('utf-8', errors='replace')

PAGES = [524, 103, 580, 1346]

for pid in PAGES:
    try:
        d = fetch_bricks(pid)
    except Exception as e:
        print(f'{pid}: fetch failed {e}'); continue
    found = []
    for e in d['content']:
        s = e.get('settings') or {}
        for k, v in s.items():
            if not isinstance(v, str): continue
            if '"daniel"' in v.lower() or '"author"' in v.lower():
                # Look specifically for author with daniel
                if re.search(r'"author"\s*:\s*\{[^}]*"name"\s*:\s*"daniel"', v, re.IGNORECASE):
                    found.append((e['id'], e.get('name'), k, 'author=daniel'))
                if re.search(r'"author"\s*:\s*"daniel"', v, re.IGNORECASE):
                    found.append((e['id'], e.get('name'), k, 'author=daniel (string)'))
                if '"@type":"Person"' in v and '"daniel"' in v.lower():
                    found.append((e['id'], e.get('name'), k, 'Person daniel'))
    print(f'\nPage {pid}: {len(found)} findings')
    for f in found:
        print(f'  {f}')

# Live homepage HTML scan
print('\n\n=== Live homepage schema scan ===')
try:
    html = fetch_html('https://www.customfabriccreations.net/')
except Exception as e:
    print(f'homepage fetch failed: {e}')
else:
    # Extract all JSON-LD blocks
    for m in re.finditer(r'<script type="application/ld\+json"[^>]*>(.*?)</script>',
                         html, flags=re.DOTALL):
        raw = m.group(1).strip()
        if 'author' not in raw.lower() and 'person' not in raw.lower(): continue
        # Try to parse; print compact preview
        try:
            obj = json.loads(raw)
            # Find author fields
            def walk(o, path=''):
                if isinstance(o, dict):
                    for k, v in o.items():
                        p = path + '.' + k
                        if k.lower() == 'author':
                            print(f'  [{p}] author = {v!r}')
                        elif k == '@type' and v == 'Person':
                            print(f'  [{p}] Person node = {o!r}')
                        walk(v, p)
                elif isinstance(o, list):
                    for i, x in enumerate(o):
                        walk(x, f'{path}[{i}]')
            walk(obj)
        except Exception as ex:
            # Raw regex-search for author patterns
            for mm in re.finditer(r'"author"\s*:\s*(\{[^}]+\}|"[^"]+")', raw):
                print(f'  raw author match: {mm.group(0)[:200]}')

# Check a sample blog post (latest)
print('\n\n=== Latest blog posts (checking first 3 for author=daniel) ===')
try:
    posts_req = urllib.request.Request(
        'https://www.customfabriccreations.net/wp-json/wp/v2/posts?per_page=3&_fields=id,slug,title,link',
        headers={'Authorization': f'Basic {auth}'})
    posts = json.loads(urllib.request.urlopen(posts_req, timeout=20).read())
    for p in posts:
        print(f"\n  Post {p['id']} ({p['slug']}): {p['title']['rendered']}")
        try:
            h = fetch_html(p['link'])
            has_daniel_author = bool(re.search(r'"author"\s*:\s*\{[^}]*"name"\s*:\s*"daniel"', h, re.IGNORECASE))
            has_terry = 'Terry Popick' in h
            print(f'    author=daniel in schema: {has_daniel_author}')
            print(f'    Terry Popick present:    {has_terry}')
            # Grab author snippets
            for mm in re.finditer(r'"author"\s*:\s*\{[^}]{0,200}\}', h):
                print(f'    author node: {mm.group(0)[:250]}')
        except Exception as ex:
            print(f'    fetch failed: {ex}')
except Exception as e:
    print(f'posts list failed: {e}')
