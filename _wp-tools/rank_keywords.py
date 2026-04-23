"""Rank CFC target keywords by opportunity score. Print in tiers."""
import json

with open(r"C:\Users\Willb\Claude\CFC\keyword_data.json") as f:
    data = json.load(f)

def score(row):
    kd = row.get("kd") or 20
    sv = row.get("sv") or 0
    cpc = row.get("cpc") or 5
    # Opportunity = volume × CPC (as proxy for commercial value) / difficulty
    return round((sv * cpc) / (kd + 1), 1)

for row in data["keywords"]:
    row["score"] = score(row)

ranked = sorted(data["keywords"], key=lambda r: -r["score"])

def tier(row):
    kd = row.get("kd") or 99
    if kd <= 10:
        return "EASY"
    if kd <= 20:
        return "MEDIUM"
    return "HARD"

print(f"{'Score':>8}  {'KW':<42s}  {'SV':>6s}  {'KD':>3s}  {'CPC':>6s}  Tier   Intent")
print("-" * 100)
for r in ranked:
    kd_str = str(r["kd"]) if r.get("kd") is not None else "-"
    cpc_str = f"${r['cpc']:.2f}" if r.get("cpc") else "-"
    sv_str = str(r.get("sv") or "-")
    print(f"{r['score']:>8.1f}  {r['kw']:<42s}  {sv_str:>6s}  {kd_str:>3s}  {cpc_str:>6s}  {tier(r):<6s} {r.get('intent','')}")

print("\n=== TOP 10 QUICK-WIN TARGETS (KD ≤ 20, sorted by opportunity score) ===\n")
easy_wins = [r for r in ranked if (r.get("kd") or 99) <= 20]
for i, r in enumerate(easy_wins[:10], 1):
    sv = r.get("sv") or 0
    cpc = r.get("cpc") or 0
    print(f"{i:>2}. {r['kw']:<42s}  SV={sv:>5}  KD={r.get('kd')}  CPC=${cpc:.2f}  Score={r['score']}")
