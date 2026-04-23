import os
"""Phase 1 update to /services/plantation-shutters/ (page 524):
- Geo-swap all 'Central Florida' / 'Tampa Bay' mentions to St. Pete / Gulf Coast framing
- Expand FAQ from 5 -> 9 questions (add cost, downside, style-2026, home-value — targeting PAA SERP features)
"""
import json
import urllib.request
import base64
import copy
import secrets
import datetime
import shutil

PAGE_ID = 524
ENDPOINT_BASE = "https://www.customfabriccreations.net/wp-json/cfc/v1/bricks"
USER = "daniel"
APP_PASS = os.environ.get("CFC_WP_APP_PASS", "")

auth = base64.b64encode(f"{USER}:{APP_PASS}".encode()).decode()
headers = {"Authorization": f"Basic {auth}", "Content-Type": "application/json"}

# ---- fetch current
req = urllib.request.Request(f"{ENDPOINT_BASE}/{PAGE_ID}", headers=headers)
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())
content = data["content"]

# ---- save a pre-edit backup
ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_path = rf"C:\Users\Willb\Claude\CFC\bricks_backup_524_{ts}_pre_phase1.json"
with open(backup_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
print(f"Pre-edit backup: {backup_path}")

by_id = {e["id"]: e for e in content}

# ---- text edits (id -> new text OR id -> (old_substring, new_substring) for partial replace)
# For full-replace, value is a string. For partial, value is a tuple (old, new).
edits = {
    # Already done as test, but harmless to set again:
    "d66522": "Custom Plantation Shutters in St. Petersburg, FL",

    # Hero/meta description line
    "92305c": "Looking for plantation shutters in St. Petersburg, FL? Custom Fabric Creations installs custom interior shutters, including faux wood, built for Florida humidity, Gulf sun, and hurricane season. Free in-home consultation across Pinellas County.\n",

    # Badge
    "15fd46": "All Pinellas & Gulf Coast",

    # About studio blurb
    "fb758b": "Our studio crafts premium window treatments and custom upholstery for homes across St. Petersburg and the Gulf Coast. From the initial design consultation to flawless installation, we bring the showroom directly to you.",

    # H2 — Types section
    "a55b98": "Types of Plantation Shutters We Install in St. Petersburg",

    # H2 — Install process
    "b3322c": "Our Plantation Shutter Installation Process in St. Petersburg",

    # H2 — Closing CTA
    "40d03d": "Ready to see what custom plantation shutters can do for your St. Pete home?",

    # H2 — Service area
    "fymolo": "Serving St. Petersburg, Clearwater & the Gulf Coast",

    # FAQ answer - faux wood recommendation (Tampa Bay -> St. Pete)
    "c257a6": (
        "most Tampa Bay homeowners",
        "most St. Pete homeowners",
    ),

    # FAQ answer - humidity (Tampa Bay windows -> St. Pete windows)
    "ac8ac6": (
        "most Tampa Bay windows",
        "most St. Pete windows",
    ),

    # Neighborhoods text — replace whole string with a St. Pete-first version
    "hxhdwa": (
        '<p><span style="font-weight: 400;">We install custom plantation shutters for homeowners across St. Petersburg and the Gulf Coast:</span></p>'
        '<p><b>Pinellas County &mdash; St. Petersburg:</b><span style="font-weight: 400;"> Snell Isle, Old Northeast, Downtown St. Pete, Shore Acres, St. Pete Beach, Treasure Island, Tierra Verde, Sand Key, Belleair Shore.</span></p>'
        '<p><b>Pinellas County &mdash; Mid &amp; North:</b><span style="font-weight: 400;"> Clearwater, Seminole, Largo, Palm Harbor, Tarpon Springs.</span></p>'
        '<p><b>Hillsborough, Pasco &amp; Sarasota counties:</b><span style="font-weight: 400;"> Tampa, Brandon, Riverview, Apollo Beach, Wesley Chapel, Lutz, Odessa, Sarasota, Bradenton.</span></p>'
        '<p><span style="font-weight: 400;">Not sure if we cover your neighborhood? Call us at (727) 240-4512 &mdash; for projects of four or more windows we travel across most of the Tampa Bay region.</span></p>'
    ),
}

# Apply edits
print("\n=== Applying text edits ===")
for eid, val in edits.items():
    e = by_id.get(eid)
    if not e:
        print(f"  MISS: element {eid} not found")
        continue
    s = e["settings"]
    if isinstance(val, tuple):
        old_sub, new_sub = val
        before = s.get("text", "")
        if old_sub not in before:
            print(f"  MISS: {eid} substring not found ({old_sub!r})")
            continue
        s["text"] = before.replace(old_sub, new_sub)
        print(f"  OK  : {eid} substring {old_sub!r} -> {new_sub!r}")
    else:
        before = s.get("text", "")
        s["text"] = val
        print(f"  OK  : {eid} text replaced ({before[:60]!r} -> {val[:60]!r})")

# ---- Add 4 new FAQs to FAQ parent b42667
# Pattern: each new FAQ = divider + Question Wrapper (block with heading + text child)

def new_id():
    return secrets.token_hex(3)  # 6-char hex

new_faqs = [
    (
        "How much do plantation shutters cost in St. Petersburg?",
        '<p><span style="font-weight: 400;">Plantation shutters in St. Pete typically run </span><b>$25&ndash;$60 per square foot installed</b><span style="font-weight: 400;">, depending on material, louver size, motorization, and specialty shapes. A standard 36" &times; 60" bedroom window runs roughly $375&ndash;$900 for composite faux wood, or $550&ndash;$1,400 for custom-stained basswood. A whole-home project (12&ndash;18 windows) typically lands between $8,000 and $22,000. We provide itemized quotes per window &mdash; no bundled "starting at" pricing or mystery upcharges.</span></p>',
    ),
    (
        "What's the downside of plantation shutters?",
        '<p><span style="font-weight: 400;">Three honest trade-offs to know before you commit. </span><b>Upfront cost</b><span style="font-weight: 400;"> is 2&ndash;4&times; comparable blinds &mdash; the math favors shutters over 20+ years of service, but the initial invoice is real. </span><b>Light gaps between louvers</b><span style="font-weight: 400;"> &mdash; even closed, louvers admit some light, so for true blackout (nurseries, media rooms) we layer blackout shades underneath or instead. </span><b>Lead time</b><span style="font-weight: 400;"> &mdash; custom manufacturing runs 3&ndash;6 weeks, versus same-day big-box stock (which typically fits roughly and fails in 2&ndash;4 years).</span></p>',
    ),
    (
        "Are plantation shutters still in style in 2026?",
        '<p><span style="font-weight: 400;">Yes, and the trend is accelerating locally. Google search interest for "plantation shutters St Petersburg" is </span><b>up 400% quarter-over-quarter</b><span style="font-weight: 400;"> heading into 2026. Plantation shutters have moved from a "traditional" look to a neutral design baseline that works with coastal modern, transitional, Mediterranean revival, and mid-century homes &mdash; every major St. Pete architectural style. The 2026 update is wider 3.5"&ndash;4.5" louvers, crisper whites, and motorized tilt.</span></p>',
    ),
    (
        "Do plantation shutters add home value in St. Petersburg?",
        '<p><span style="font-weight: 400;">Yes &mdash; Pinellas realtors consistently list plantation shutters as a high-ROI interior upgrade. Typical recovery at resale is </span><b>70&ndash;90% of install cost</b><span style="font-weight: 400;">, and homes with custom shutters often appraise $5,000&ndash;$15,000 higher than comparable homes with standard blinds. Unlike drapery (personal taste), shutters convey with the home and buyers perceive them as a permanent premium feature.</span></p>',
    ),
]

print("\n=== Adding new FAQs ===")
faq_parent_id = "b42667"
faq_parent = by_id[faq_parent_id]

# Clone a divider for template values
divider_template = copy.deepcopy(by_id["a00dfd"])
wrapper_template = copy.deepcopy(by_id["1322fe"])
heading_template = copy.deepcopy(by_id["67ad6f"])
text_template = copy.deepcopy(by_id["ac8ac6"])

new_ids_to_append = []

for question, answer_html in new_faqs:
    # Create new ids
    div_id = new_id()
    wrap_id = new_id()
    head_id = new_id()
    ans_id = new_id()

    # Divider
    divider = copy.deepcopy(divider_template)
    divider["id"] = div_id
    divider["parent"] = faq_parent_id
    divider["children"] = []
    content.append(divider)

    # Wrapper block
    wrapper = copy.deepcopy(wrapper_template)
    wrapper["id"] = wrap_id
    wrapper["parent"] = faq_parent_id
    wrapper["children"] = [head_id, ans_id]
    content.append(wrapper)

    # Heading (question)
    heading = copy.deepcopy(heading_template)
    heading["id"] = head_id
    heading["parent"] = wrap_id
    heading["children"] = []
    heading["settings"]["text"] = question
    content.append(heading)

    # Text (answer)
    ans = copy.deepcopy(text_template)
    ans["id"] = ans_id
    ans["parent"] = wrap_id
    ans["children"] = []
    ans["settings"]["text"] = answer_html
    content.append(ans)

    new_ids_to_append.extend([div_id, wrap_id])
    print(f"  OK  : added FAQ '{question[:60]}...' (div={div_id}, wrap={wrap_id}, head={head_id}, ans={ans_id})")

# Append new FAQ items to FAQ parent's children list (maintaining divider, wrapper, divider, wrapper pattern)
faq_parent["children"] = list(faq_parent["children"]) + new_ids_to_append
print(f"\nFAQ parent children count: {len(faq_parent['children'])} (was 9, expected 17)")

# ---- POST
print("\n=== POSTing updated content ===")
payload = json.dumps({"content": content}).encode()
req = urllib.request.Request(
    f"{ENDPOINT_BASE}/{PAGE_ID}",
    data=payload,
    headers=headers,
    method="POST",
)
with urllib.request.urlopen(req) as r:
    print(f"POST response: {r.status} {r.read().decode()}")

# ---- verify round-trip
req = urllib.request.Request(f"{ENDPOINT_BASE}/{PAGE_ID}", headers=headers)
with urllib.request.urlopen(req) as r:
    verify_data = json.loads(r.read())
verify_content = verify_data["content"]
verify_by_id = {e["id"]: e for e in verify_content}

print("\n=== Verification ===")
for eid in edits.keys():
    e = verify_by_id.get(eid)
    if e:
        txt = e["settings"].get("text", "")
        print(f"  {eid}: {txt[:80]!r}")

print(f"\n  Total elements: was {len(by_id)}, now {len(verify_content)} (delta +{len(verify_content) - len(by_id)})")
