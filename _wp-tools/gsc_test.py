"""Quick sanity check: confirm the service account can reach GSC."""
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import date, timedelta
import json

KEY_PATH = r"C:\Users\Willb\Claude\CFC\gsc-service-account.json"
SITE = "https://www.customfabriccreations.net/"

creds = service_account.Credentials.from_service_account_file(
    KEY_PATH,
    scopes=["https://www.googleapis.com/auth/webmasters.readonly"],
)
svc = build("searchconsole", "v1", credentials=creds, cache_discovery=False)

print("=== Properties this service account can see ===")
sites = svc.sites().list().execute()
for s in sites.get("siteEntry", []):
    print(f"  {s['permissionLevel']:20s}  {s['siteUrl']}")

end = date.today()
start = end - timedelta(days=28)
print(f"\n=== Top 10 queries for {SITE} ({start} -> {end}) ===")
try:
    req = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "dimensions": ["query"],
        "rowLimit": 10,
    }
    resp = svc.searchanalytics().query(siteUrl=SITE, body=req).execute()
    for r in resp.get("rows", []):
        q = r["keys"][0]
        print(f"  clicks={r['clicks']:>4}  impr={r['impressions']:>6}  ctr={r['ctr']*100:5.2f}%  pos={r['position']:5.2f}  {q}")
    if not resp.get("rows"):
        print("  (no rows returned — property may have no traffic or may need sc-domain: prefix)")
except Exception as e:
    print(f"  ERROR: {e}")
    print("\n  Trying sc-domain:customfabriccreations.net instead...")
    try:
        resp = svc.searchanalytics().query(
            siteUrl="sc-domain:customfabriccreations.net", body=req
        ).execute()
        for r in resp.get("rows", []):
            q = r["keys"][0]
            print(f"  clicks={r['clicks']:>4}  impr={r['impressions']:>6}  ctr={r['ctr']*100:5.2f}%  pos={r['position']:5.2f}  {q}")
    except Exception as e2:
        print(f"  ERROR: {e2}")
