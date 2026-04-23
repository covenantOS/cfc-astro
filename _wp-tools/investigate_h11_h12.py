import os
"""Quick investigation of H11 (sitemap orphans) and H12 (duplicate OG tags)."""
import json, urllib.request, base64, re, sys
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()

def fetch_html(url, auth_hdr=False):
    h = {}
    if auth_hdr: h['Authorization'] = f'Basic {auth}'
    req = urllib.request.Request(url, headers=h)
    return urllib.request.urlopen(req, timeout=30).read().decode('utf-8', errors='replace')

# --------------------------------------------------------------
# H12: Duplicate OG tags on homepage + pillar page
# --------------------------------------------------------------
print('=== H12: Duplicate OG/Twitter meta tags ===')
for url in ['https://www.customfabriccreations.net/',
            'https://www.customfabriccreations.net/services/plantation-shutters/',
            'https://www.customfabriccreations.net/areas/west-st-pete/']:
    try:
        html = fetch_html(url)
    except Exception as e:
        print(f'  {url}: FAILED {e}'); continue
    # Count meta property and name tags
    og_tags = re.findall(r'<meta\s+property="(og:[a-z:]+)"\s+content="([^"]*)"', html)
    tw_tags = re.findall(r'<meta\s+name="(twitter:[a-z:]+)"\s+content="([^"]*)"', html)
    print(f'\n  URL: {url}')
    og_counter = Counter(p for p, _ in og_tags)
    tw_counter = Counter(p for p, _ in tw_tags)
    dupes = {p: n for p, n in og_counter.items() if n > 1}
    tw_dupes = {p: n for p, n in tw_counter.items() if n > 1}
    if dupes:
        print(f'    OG duplicates: {dupes}')
        for p, n in dupes.items():
            for (prop, val) in og_tags:
                if prop == p:
                    print(f'      {prop} = {val[:120]!r}')
    else:
        print(f'    OG: clean ({len(og_tags)} unique)')
    if tw_dupes:
        print(f'    Twitter duplicates: {tw_dupes}')
    else:
        print(f'    Twitter: clean ({len(tw_tags)} unique)')

    # Also check for multiple canonical tags
    canon = re.findall(r'<link\s+rel="canonical"\s+href="([^"]+)"', html)
    if len(canon) > 1:
        print(f'    CANONICAL DUPES ({len(canon)}): {canon}')
    else:
        print(f'    Canonical: single ({canon[0] if canon else "MISSING"})')

# --------------------------------------------------------------
# H11: Sitemap orphan analysis — URLs in sitemap vs. internal links
# --------------------------------------------------------------
print('\n\n=== H11: Sitemap orphan check ===')
try:
    sm = fetch_html('https://www.customfabriccreations.net/sitemap_index.xml')
    sitemaps = re.findall(r'<loc>([^<]+)</loc>', sm)
    print(f'  Top-level sitemap index references: {len(sitemaps)}')
    all_urls = set()
    for url in sitemaps[:10]:
        try:
            sub = fetch_html(url)
            urls = re.findall(r'<loc>([^<]+)</loc>', sub)
            for u in urls:
                all_urls.add(u)
            print(f'    {url}: {len(urls)} urls')
        except Exception as e:
            print(f'    {url}: FAILED {e}')
    print(f'\n  Total URLs in sitemap: {len(all_urls)}')
except Exception as e:
    print(f'  sitemap index fetch failed: {e}')

# Grab homepage + primary-nav internal links to see what gets linked
print('\n  Internal links collected from homepage and pillar pages:')
linked_urls = set()
for url in ['https://www.customfabriccreations.net/',
            'https://www.customfabriccreations.net/services/plantation-shutters/',
            'https://www.customfabriccreations.net/areas/west-st-pete/']:
    try:
        html = fetch_html(url)
    except: continue
    # Find internal <a href=""> absolute or relative
    for m in re.finditer(r'href="(https?://www\.customfabriccreations\.net[^"#?]+|/[^"#?]+)"', html):
        u = m.group(1)
        if u.startswith('/'):
            u = 'https://www.customfabriccreations.net' + u
        # Normalize trailing slash
        if not u.endswith('/') and '.' not in u.split('/')[-1]:
            u = u + '/'
        linked_urls.add(u)
print(f'  Internal links from sampled pages: {len(linked_urls)}')

# Orphans = in sitemap but not linked from the sample
orphans = all_urls - linked_urls
# Not-in-sitemap = linked from pages but missing from sitemap
not_in_sitemap = linked_urls - all_urls

print(f'\n  URLs in sitemap NOT linked from sampled pages (potential orphans): {len(orphans)}')
for u in sorted(orphans)[:30]:
    print(f'    {u}')

print(f'\n  URLs linked from sampled pages NOT in sitemap: {len(not_in_sitemap)}')
for u in sorted(not_in_sitemap)[:30]:
    print(f'    {u}')
