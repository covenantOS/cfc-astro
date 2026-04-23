import os
"""Scan ALL WP pages for the same duplicate-H1 issue (post_content
contains an <h1> that matches or overlaps with the page title, and the
theme template also renders the title as H1). Fix each one."""
import json, urllib.request, base64, datetime, re, time, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()

ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

# Fetch all pages (edit context to get raw post_content)
pages = []
page_num = 1
while True:
    req = urllib.request.Request(
        f'https://www.customfabriccreations.net/wp-json/wp/v2/pages?per_page=50&page={page_num}&context=edit&_fields=id,slug,title,content,link,status',
        headers={'Authorization': f'Basic {auth}'})
    try:
        batch = json.loads(urllib.request.urlopen(req, timeout=30).read())
    except urllib.error.HTTPError as e:
        if e.code == 400: break  # pagination exhausted
        raise
    if not batch: break
    pages.extend(batch)
    if len(batch) < 50: break
    page_num += 1

print(f'Total pages fetched: {len(pages)}')

affected = []
for p in pages:
    raw = p.get('content', {}).get('raw', '')
    if not raw: continue
    h1_blocks = re.findall(r'<h1[^>]*>(.*?)</h1>', raw, flags=re.DOTALL | re.IGNORECASE)
    if not h1_blocks: continue
    # Does the live HTML also show the theme-template H1?
    # Pull live HTML and count h1 tags
    try:
        html_req = urllib.request.Request(p['link'] + f'?nocache={int(time.time())}')
        html = urllib.request.urlopen(html_req, timeout=30).read().decode('utf-8', errors='replace')
        live_h1_count = len(re.findall(r'<h1[^>]*>', html))
    except Exception as ex:
        live_h1_count = -1
    if live_h1_count > 1 or (live_h1_count >= 1 and len(h1_blocks) >= 1):
        affected.append({
            'id': p['id'],
            'slug': p['slug'],
            'title': p['title']['rendered'],
            'post_content_h1_count': len(h1_blocks),
            'live_h1_count': live_h1_count,
            'first_h1_text': re.sub(r'<[^>]+>', '', h1_blocks[0])[:120],
        })

print(f'\nPages with post_content <h1> AND live h1>1 (duplicate issue): {len(affected)}')
for a in affected:
    print(f"  id={a['id']} slug={a['slug']} post_h1={a['post_content_h1_count']} live_h1={a['live_h1_count']} first={a['first_h1_text']!r}")

# For each affected page, strip post_content H1s that match the page title
print('\n\n=== Applying fixes ===')
fixed = 0
for a in affected:
    pid = a['id']
    # Re-fetch raw (in case)
    req = urllib.request.Request(
        f'https://www.customfabriccreations.net/wp-json/wp/v2/pages/{pid}?context=edit&_fields=id,title,content',
        headers={'Authorization': f'Basic {auth}'})
    p = json.loads(urllib.request.urlopen(req, timeout=30).read())
    raw = p['content']['raw']
    title = p['title']['rendered']
    title_decoded = (title.replace('&amp;','&').replace('&#8217;',"'")
                          .replace('&#8216;',"'").replace('&#8220;','"')
                          .replace('&#8221;','"'))

    # Save backup
    with open(rf'C:\Users\Willb\Claude\CFC\page_{pid}_backup_{ts}_pre_h1_sweep.json', 'w', encoding='utf-8') as f:
        json.dump(p, f, indent=2, ensure_ascii=False)

    def strip_title_h1(m):
        block = m.group(0)
        inner = re.sub(r'<[^>]+>', '', block).strip()
        if title.lower().strip() in inner.lower() or title_decoded.lower().strip() in inner.lower() \
           or inner.lower() in title.lower() or inner.lower() in title_decoded.lower():
            return ''
        return block

    new_raw = re.sub(r'<h1[^>]*>.*?</h1>\s*', strip_title_h1, raw, flags=re.DOTALL | re.IGNORECASE)
    # Collapse leading blank lines inside container divs
    new_raw = re.sub(r'(<div[^>]*>)\s*\n\s*', r'\1', new_raw, count=1)

    if new_raw != raw:
        payload = {'content': new_raw}
        req2 = urllib.request.Request(
            f'https://www.customfabriccreations.net/wp-json/wp/v2/pages/{pid}',
            data=json.dumps(payload).encode(),
            headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'},
            method='POST')
        try:
            resp = json.loads(urllib.request.urlopen(req2, timeout=30).read())
            fixed += 1
            print(f"  {pid} {a['slug']}: stripped {a['post_content_h1_count']} H1(s), len {len(raw)} -> {len(new_raw)}")
        except Exception as e:
            print(f"  {pid}: UPDATE FAILED {e}")
    else:
        print(f"  {pid} {a['slug']}: no matching H1 found to strip (edge case)")

print(f'\n=== Fixed {fixed} pages ===')

# Re-scan live HTML for each affected page
print('\n=== Post-fix live HTML h1 counts ===')
for a in affected:
    try:
        html_req = urllib.request.Request(a['title'] and f"https://www.customfabriccreations.net/{a['slug']}/?nocache={int(time.time())}")
        html = urllib.request.urlopen(html_req, timeout=30).read().decode('utf-8', errors='replace')
        live_h1 = len(re.findall(r'<h1[^>]*>', html))
        print(f"  {a['slug']}: h1 count = {live_h1} (was {a['live_h1_count']})")
    except Exception as e:
        print(f"  {a['slug']}: verify failed {e}")
