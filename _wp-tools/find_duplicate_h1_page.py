import os
"""Find the install cluster page with the duplicate H1 and identify the
two heading elements so we can delete one."""
import json, urllib.request, base64, re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()

# Search WP pages for the distinctive title
target_phrase = 'Plantation Shutter Installation in St. Petersburg'
req = urllib.request.Request(
    f'https://www.customfabriccreations.net/wp-json/wp/v2/pages?per_page=100&_fields=id,slug,title,link,status',
    headers={'Authorization': f'Basic {auth}'})
pages = json.loads(urllib.request.urlopen(req, timeout=30).read())

candidates = []
for p in pages:
    t = p['title']['rendered']
    s = p['slug']
    if 'install' in s or 'install' in t.lower() or target_phrase.lower() in t.lower():
        candidates.append(p)
        print(f"  candidate id={p['id']} slug={s} title={t!r} status={p['status']}")

# For each candidate, fetch Bricks content and find H1/heading elements
for p in candidates:
    pid = p['id']
    print(f"\n=== Scanning Bricks for {pid} ({p['slug']}) ===")
    try:
        req2 = urllib.request.Request(
            f'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/{pid}',
            headers={'Authorization': f'Basic {auth}'})
        d = json.loads(urllib.request.urlopen(req2, timeout=20).read())
    except Exception as e:
        print(f'  fetch failed: {e}'); continue

    headings = []
    for e in d['content']:
        s = e.get('settings') or {}
        nm = e.get('name')
        if nm in ('heading',) or ('heading' in (nm or '')):
            txt = s.get('text', '') or s.get('title', '')
            tag = s.get('tag', 'h2')
            if isinstance(txt, str) and txt:
                headings.append((e['id'], tag, e.get('parent'), txt[:200]))
    print(f'  {len(headings)} heading elements:')
    for h in headings:
        print(f"    {h[0]} tag={h[1]} parent={h[2]} | {h[3]!r}")

    # Spot duplicates
    by_text = {}
    for h in headings:
        by_text.setdefault(h[3], []).append(h)
    dupes = {t: hs for t, hs in by_text.items() if len(hs) > 1}
    if dupes:
        print(f'\n  DUPLICATE HEADING TEXTS:')
        for t, hs in dupes.items():
            print(f"    text={t!r} appears {len(hs)} times:")
            for h in hs:
                print(f"      id={h[0]} tag={h[1]} parent={h[2]}")
