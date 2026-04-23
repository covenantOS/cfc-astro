"""Generate the seed keyword list for CFC St. Pete SEO research."""
import json
from itertools import product

SERVICES = [
    "custom drapery",
    "custom curtains",
    "plantation shutters",
    "roman shades",
    "cellular shades",
    "roller shades",
    "custom blinds",
    "motorized blinds",
    "motorized shades",
    "window treatments",
    "reupholstery",
    "furniture reupholstery",
    "custom bedding",
    "custom headboards",
    "commercial window treatments",
    "valances",
    "cornices",
]

GEOS = [
    "st petersburg fl",
    "st pete",
    "snell isle",
    "downtown st pete",
    "shore acres st pete",
    "tierra verde fl",
    "st pete beach",
    "treasure island fl",
    "clearwater fl",
    "sand key fl",
    "belleair fl",
    "seminole fl",
    "largo fl",
]

BRANDS = ["hunter douglas", "norman shutters", "graber", "kravet"]
BRAND_GEOS = ["st petersburg", "st pete", "clearwater"]

MODIFIERS = ["cost", "installation", "near me"]
MODIFIER_SERVICES = [
    "plantation shutters",
    "custom drapery",
    "motorized blinds",
    "reupholstery",
    "roman shades",
    "window treatments",
]

seeds = set()

for s, g in product(SERVICES, GEOS):
    seeds.add(f"{s} {g}")

for s in SERVICES:
    seeds.add(s)
    seeds.add(f"{s} near me")

for b, g in product(BRANDS, BRAND_GEOS):
    seeds.add(f"{b} {g}")
    seeds.add(f"{b} dealer {g}")

for s, m in product(MODIFIER_SERVICES, MODIFIERS):
    if m == "near me":
        continue
    seeds.add(f"{s} {m}")
    seeds.add(f"{s} {m} st petersburg")

EXTRAS = [
    "window treatment store st petersburg",
    "drapery workroom st petersburg",
    "custom drapery maker st pete",
    "drapery installation st petersburg",
    "blind installer st petersburg",
    "interior designer st petersburg window treatments",
    "best window treatments st petersburg",
    "window treatment showroom st petersburg",
    "motorized window shades cost",
    "smart blinds st petersburg",
    "drapery cleaning st petersburg",
    "plantation shutters tampa bay",
    "window treatments tampa bay",
    "st petersburg drapery",
    "st pete curtains",
    "custom drapes florida",
]
for e in EXTRAS:
    seeds.add(e)

seeds = sorted(seeds)
print(f"Total seeds: {len(seeds)}")
with open(r"C:\Users\Willb\Claude\CFC\seeds.json", "w") as f:
    json.dump(seeds, f, indent=2)
print(f"Written to seeds.json")
print("\nFirst 20:")
for k in seeds[:20]:
    print(f"  {k}")
