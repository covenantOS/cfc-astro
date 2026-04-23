"""GSC performance query for customfabriccreations.net — last 90 days."""
import json, datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

KEY = r"C:\Users\Willb\Claude\CFC\gsc-service-account.json"
SITE = "sc-domain:customfabriccreations.net"
creds = Credentials.from_service_account_file(KEY, scopes=["https://www.googleapis.com/auth/webmasters.readonly"])
svc = build("searchconsole", "v1", credentials=creds)

end = datetime.date.today()
start = end - datetime.timedelta(days=90)
print(f"Date range: {start} to {end}")
print()

def q(dims, rowLimit=50, filters=None):
    req = {
        "startDate": start.isoformat(),
        "endDate": end.isoformat(),
        "dimensions": dims,
        "rowLimit": rowLimit,
    }
    if filters:
        req["dimensionFilterGroups"] = [{"filters": filters}]
    return svc.searchanalytics().query(siteUrl=SITE, body=req).execute().get("rows", [])

# 1. Top queries (sitewide, last 90d)
print("=== TOP 30 QUERIES SITEWIDE (last 90d) ===")
rows = q(["query"], rowLimit=30)
print(f"{'CLICKS':>6} {'IMPR':>8} {'CTR':>6} {'POS':>6}  QUERY")
for r in rows:
    print(f"{r['clicks']:>6.0f} {r['impressions']:>8.0f} {r['ctr']*100:>5.1f}% {r['position']:>6.1f}  {r['keys'][0]}")

# 2. Top pages
print("\n=== TOP 20 PAGES ===")
rows = q(["page"], rowLimit=20)
for r in rows:
    print(f"{r['clicks']:>6.0f} {r['impressions']:>8.0f} {r['ctr']*100:>5.1f}% {r['position']:>6.1f}  {r['keys'][0]}")

# 3. Plantation-shutters page queries
print("\n=== QUERIES FOR /plantation-shutters/ PAGE ===")
rows = q(["query"], rowLimit=50, filters=[
    {"dimension": "page", "operator": "contains", "expression": "/plantation-shutters"}
])
print(f"{'CLICKS':>6} {'IMPR':>8} {'CTR':>6} {'POS':>6}  QUERY")
for r in rows:
    print(f"{r['clicks']:>6.0f} {r['impressions']:>8.0f} {r['ctr']*100:>5.1f}% {r['position']:>6.1f}  {r['keys'][0]}")

# 4. Queries on position 11-30 (page 2 opportunity)
print("\n=== QUERIES RANKING 11-30 (LOW-HANGING FRUIT) ===")
all_q = q(["query"], rowLimit=500)
opps = [r for r in all_q if 11 <= r["position"] <= 30 and r["impressions"] >= 10]
opps.sort(key=lambda r: -r["impressions"])
print(f"{'CLICKS':>6} {'IMPR':>8} {'CTR':>6} {'POS':>6}  QUERY")
for r in opps[:30]:
    print(f"{r['clicks']:>6.0f} {r['impressions']:>8.0f} {r['ctr']*100:>5.1f}% {r['position']:>6.1f}  {r['keys'][0]}")

# 5. High-impression zero-click (missing CTR)
print("\n=== HIGH-IMPRESSION, LOW-CTR (title/snippet fix opp) ===")
hi_lo = [r for r in all_q if r["impressions"] >= 50 and r["ctr"] < 0.03]
hi_lo.sort(key=lambda r: -r["impressions"])
for r in hi_lo[:15]:
    print(f"{r['clicks']:>6.0f} {r['impressions']:>8.0f} {r['ctr']*100:>5.1f}% {r['position']:>6.1f}  {r['keys'][0]}")
