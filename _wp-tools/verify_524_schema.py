"""Verify the fix — fetch the live page and try to parse every JSON-LD block."""
import json, urllib.request, re

url = 'https://www.customfabriccreations.net/services/plantation-shutters/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
html = urllib.request.urlopen(req, timeout=20).read().decode('utf-8', errors='replace')
blocks = re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', html, re.DOTALL)
print(f"Found {len(blocks)} JSON-LD blocks on /services/plantation-shutters/")
for i, b in enumerate(blocks):
    try:
        parsed = json.loads(b.strip())
        types = []
        if isinstance(parsed, list):
            types = [x.get('@type') for x in parsed if isinstance(x, dict)]
        elif isinstance(parsed, dict):
            if '@graph' in parsed:
                types = [x.get('@type') for x in parsed['@graph'] if isinstance(x, dict)]
            else:
                types = [parsed.get('@type')]
        print(f"  [{i}] OK ({len(b)} chars) - types: {types}")
    except json.JSONDecodeError as e:
        print(f"  [{i}] BROKEN: {e.msg} at col {e.pos}")
        start = max(0, e.pos - 60)
        print(f"     ctx: ...{b[start:e.pos+60]}...")
