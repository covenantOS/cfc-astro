"""Pull GSC 28-day data per URL and per query for customfabriccreations.net.
Used to build the page-by-page porting priority map — pages with ranking
signals get ported first so we don't lose them at cutover."""

import json
import sys
from datetime import date, timedelta
from pathlib import Path

try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
except ImportError:
    print("Run: pip install google-auth google-auth-httplib2 google-api-python-client", file=sys.stderr)
    sys.exit(1)

KEY = r"C:\Users\Willb\Claude\CFC\gsc-service-account.json"
SITE = "sc-domain:customfabriccreations.net"
OUT_DIR = Path(__file__).parent / "scraped"
OUT_DIR.mkdir(parents=True, exist_ok=True)

today = date.today()
start = today - timedelta(days=28)
end = today - timedelta(days=1)

creds = service_account.Credentials.from_service_account_file(
    KEY, scopes=["https://www.googleapis.com/auth/webmasters.readonly"]
)
svc = build("searchconsole", "v1", credentials=creds, cache_discovery=False)

def query(dimensions, limit=1000):
    req = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "dimensions": dimensions,
        "rowLimit": limit,
    }
    rows = svc.searchanalytics().query(siteUrl=SITE, body=req).execute().get("rows", [])
    return rows

# Per-page aggregates
pages = []
for r in query(["page"], limit=1000):
    pages.append({
        "page": r["keys"][0],
        "clicks": r["clicks"],
        "impressions": r["impressions"],
        "ctr": round(r["ctr"], 4),
        "position": round(r["position"], 2),
    })

# Per-page + query (for ranking KW attribution)
page_queries = {}
for r in query(["page", "query"], limit=5000):
    page, q = r["keys"]
    page_queries.setdefault(page, []).append({
        "query": q,
        "clicks": r["clicks"],
        "impressions": r["impressions"],
        "position": round(r["position"], 2),
    })

for p in pages:
    p["top_queries"] = sorted(
        page_queries.get(p["page"], []),
        key=lambda x: -x["impressions"],
    )[:10]

out = {
    "property": SITE,
    "window": {"start": start.isoformat(), "end": end.isoformat()},
    "pages": sorted(pages, key=lambda x: -x["impressions"]),
}

(OUT_DIR / "gsc.json").write_text(json.dumps(out, indent=2))
print(f"Wrote {len(pages)} pages to {OUT_DIR / 'gsc.json'}")
print(f"Total clicks: {sum(p['clicks'] for p in pages)}")
print(f"Total impressions: {sum(p['impressions'] for p in pages)}")
