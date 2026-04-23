import os
"""Phase 2: Insert 4 new H2 sections + 1 new FAQ after existing Types section.

Sections to add (each = divider + heading-h2 + text-basic):
1. Materials & Construction
2. Specialty Shapes & Applications
3. Authorized Dealer (Top 5 brands)
4. In-House Workroom — Since 2000 (CFC USP)

Plus one new FAQ: "Who's the best plantation shutter company in St. Pete?"

Insert into container 9d29a5 immediately after 5c9c3e (Types text), before 8facf4 (next divider).
"""
import json, urllib.request, base64, copy, secrets, datetime

PAGE_ID = 524
ENDPOINT = "https://www.customfabriccreations.net/wp-json/cfc/v1/bricks"
auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
headers = {"Authorization": f"Basic {auth}", "Content-Type": "application/json"}

req = urllib.request.Request(f"{ENDPOINT}/{PAGE_ID}", headers=headers)
data = json.loads(urllib.request.urlopen(req).read())
content = data["content"]
by_id = {e["id"]: e for e in content}

# Backup
ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
bpath = rf"C:\Users\Willb\Claude\CFC\bricks_backup_524_{ts}_pre_phase2.json"
with open(bpath, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
print(f"Backup: {bpath}")

# Templates (existing elements we'll clone)
DIVIDER_T = copy.deepcopy(by_id["8facf4"])   # a divider in the body
HEADING_T = copy.deepcopy(by_id["240e6d"])   # Custom vs Retail H2
TEXT_T = copy.deepcopy(by_id["fd0fcc"])      # Custom vs Retail body text

# FAQ templates (from Phase 1)
FAQ_DIVIDER_T = copy.deepcopy(by_id["a00dfd"])
FAQ_WRAPPER_T = copy.deepcopy(by_id["1322fe"])
FAQ_HEAD_T = copy.deepcopy(by_id["67ad6f"])
FAQ_ANS_T = copy.deepcopy(by_id["ac8ac6"])

MAIN_PARENT = "9d29a5"
FAQ_PARENT = "b42667"

def nid():
    return secrets.token_hex(3)

# ---- NEW SECTIONS ----
sections = [
    {
        "h2": "Materials &amp; Construction &mdash; What You&rsquo;re Actually Buying",
        "body": (
            '<p><span style="font-weight: 400;">Three material tiers. Here&rsquo;s the honest version:</span></p>'
            '<p><b>Faux Wood / Composite (Tech / Hybrid)</b><br>'
            '<span style="font-weight: 400;">Best for: bathrooms, kitchens, laundry rooms, beachfront condos, any window within a mile of the Gulf. '
            'Solid polymer or ABS over an engineered composite core. Mortise-and-tenon joinery on premium lines. '
            'Louver sizes: 2.5&Prime;, 3.5&Prime;, 4.5&Prime;. Factory-applied UV-stable coating with up to 40 standard colors. '
            'Limited lifetime warranty against warping, cracking, fading. Mid-tier pricing &mdash; best dollar-per-year-of-service in Florida.</span></p>'
            '<p><b>Real Wood (Basswood &amp; Poplar)</b><br>'
            '<span style="font-weight: 400;">Best for: formal living rooms, main-living windows, stained-wood interiors, historic Old Northeast and Snell Isle homes where wood tone matters. '
            'Kiln-dried basswood or poplar with mortise-and-tenon construction. '
            '50+ custom stains, 200+ paint colors, color-matched to existing trim or furniture. '
            'Manufacturer limited lifetime warranty. Premium tier &mdash; specify real wood only if the room stays climate-controlled.</span></p>'
            '<p><b>Hybrid / Premier (Wood core + polymer exterior)</b><br>'
            '<span style="font-weight: 400;">Best for: clients who want the look of real wood with composite&rsquo;s humidity resistance. '
            'Hardwood frame with a polymer-wrapped louver face. 3.5&Prime; louvers most common. Stainable or paintable; accepts custom color match. '
            'Premium tier &mdash; the &ldquo;best of both&rdquo; option.</span></p>'
            '<p><b>Quick decision rule:</b><span style="font-weight: 400;"> Bathroom, kitchen, laundry, or within a mile of saltwater &rarr; faux wood. '
            'Climate-controlled and the room&rsquo;s aesthetic calls for stained wood &rarr; basswood. '
            'Wood grain without the maintenance &rarr; hybrid.</span></p>'
        ),
    },
    {
        "h2": "Specialty Shapes &amp; Applications",
        "body": (
            '<p><span style="font-weight: 400;">Every window in St. Pete is different. Sunburst transom over a Coquina-stone bungalow. Trapezoidal gable in a Tierra Verde canal home. '
            'French doors opening to a Snell Isle courtyard. Sliding glass onto a Treasure Island lanai. We build for all of them.</span></p>'
            '<p><b>Arches, sunbursts, eyebrows &amp; angled windows.</b><span style="font-weight: 400;"> Custom-cut frames for true radial arches, half-rounds, eyebrows, octagons, trapezoids, and hexagons. Louvers are cut to the exact radius &mdash; no &ldquo;close enough&rdquo; framing.</span></p>'
            '<p><b>French door shutters.</b><span style="font-weight: 400;"> Low-profile frames clear the door hardware. Tilt rods positioned so the lever handle doesn&rsquo;t bind. Optional cut-outs for lever handles on antique French doors.</span></p>'
            '<p><b>Sliding glass door bypass shutters.</b><span style="font-weight: 400;"> Full-height panels on a bypass or bi-fold track. Hidden control rods so you see clean louver faces from inside and out. Standard on Gulf-facing lanais across St. Pete Beach and Sand Key.</span></p>'
            '<p><b>Closet, pass-through &amp; pantry shutters.</b><span style="font-weight: 400;"> Same premium plantation look in smaller applications &mdash; walk-in closets, butler&rsquo;s pantries, and passage doors where you want airflow without losing privacy.</span></p>'
            '<p><b>Motorized &amp; smart shutters.</b><span style="font-weight: 400;"> Tilt motors from Somfy and Hunter Douglas PowerView&reg;. Control via wall switch, remote, iOS/Android app, or voice via Alexa and Google Assistant. Program scenes &mdash; open at sunrise, close at sunset, full blackout for the guest-room afternoon.</span></p>'
        ),
    },
    {
        "h2": "Authorized Dealer for the Top 5 Plantation Shutter Brands",
        "body": (
            '<p><span style="font-weight: 400;">Big-box retailers source from whoever&rsquo;s cheapest that quarter. We partner directly with the manufacturers who earned their reputation:</span></p>'
            '<p><b>Hunter Douglas</b><span style="font-weight: 400;"> &mdash; NewStyle&reg; hybrid shutters, Palm Beach&trade; polysatin, Heritance&reg; hardwood. Full PowerView&reg; motorization.</span></p>'
            '<p><b>Norman</b><span style="font-weight: 400;"> &mdash; Woodlore&reg; (faux wood), Normandy&reg; (basswood), Sussex&trade; (hardwood hybrid). Known for lifetime warranty and tight finish quality.</span></p>'
            '<p><b>Graber</b><span style="font-weight: 400;"> &mdash; CustomView&reg; and Traditions&reg; shutter lines. Strong custom-color program.</span></p>'
            '<p><b>Kravet</b><span style="font-weight: 400;"> &mdash; Designer-grade finish options, typically paired with custom drapery.</span></p>'
            '<p><b>Stout Textiles</b><span style="font-weight: 400;"> &mdash; Coordinating fabrics for valances and side panels paired with shutters.</span></p>'
            '<p><b>What &ldquo;authorized&rdquo; means for you:</b><span style="font-weight: 400;"> full manufacturer warranty honored, access to every color and option on the spec sheet, certified measurement and installation, direct factory recourse if anything isn&rsquo;t right.</span></p>'
        ),
    },
    {
        "h2": "Our In-House Workroom &mdash; Since 2000",
        "body": (
            '<p><span style="font-weight: 400;">This is the piece no other St. Pete competitor can match: we&rsquo;ve run our own fabric and fabrication workroom on-site for 25 years. '
            'Custom cornices, valances, drapery, bedding, and shutter finishing all happen under the same roof as our design studio.</span></p>'
            '<p><b>What that means for your plantation shutter order:</b></p>'
            '<p><b>Color-coordinated companion pieces.</b><span style="font-weight: 400;"> Shutters on the bottom of a window with a custom valance or cornice above &mdash; built to match exactly, not approximately. One vendor, one finish match, one warranty.</span></p>'
            '<p><b>Faster lead times.</b><span style="font-weight: 400;"> Finish touch-ups, cut-to-fit adjustments, and rush installations don&rsquo;t wait on a distant factory.</span></p>'
            '<p><b>Accountability.</b><span style="font-weight: 400;"> If anything needs correction post-install, it goes back to our workroom &mdash; not shipped to a sub-contracted manufacturer four states away.</span></p>'
            '<p><b>Design continuity.</b><span style="font-weight: 400;"> Plantation shutters this year, custom drapery next year &mdash; your designer already has your window measurements, trim color, and lighting notes on file.</span></p>'
            '<p><span style="font-weight: 400;">Twenty-five years, one family business, one workroom, one phone number.</span></p>'
        ),
    },
]

# Build new elements
new_elements = []
new_ids_in_order = []

for sec in sections:
    div_id = nid()
    h2_id = nid()
    txt_id = nid()

    div = copy.deepcopy(DIVIDER_T)
    div["id"] = div_id
    div["parent"] = MAIN_PARENT
    div["children"] = []

    h2 = copy.deepcopy(HEADING_T)
    h2["id"] = h2_id
    h2["parent"] = MAIN_PARENT
    h2["children"] = []
    h2["settings"]["text"] = sec["h2"]

    txt = copy.deepcopy(TEXT_T)
    txt["id"] = txt_id
    txt["parent"] = MAIN_PARENT
    txt["children"] = []
    txt["settings"]["text"] = sec["body"]

    new_elements.extend([div, h2, txt])
    new_ids_in_order.extend([div_id, h2_id, txt_id])
    print(f"  Built '{sec['h2'][:60]}' -> div={div_id} h2={h2_id} txt={txt_id}")

# Insert into 9d29a5's children after 5c9c3e (Types text)
main = by_id[MAIN_PARENT]
kids = list(main["children"])
insert_after = "5c9c3e"
idx = kids.index(insert_after) + 1
print(f"\nInserting {len(new_ids_in_order)} new IDs into {MAIN_PARENT}.children at position {idx} (after {insert_after})")
kids[idx:idx] = new_ids_in_order
main["children"] = kids

# Append new elements to content array
content.extend(new_elements)

# ---- NEW FAQ ----
faq_q = "Who&rsquo;s the best plantation shutter company in St. Pete?"
faq_a = (
    '<p><span style="font-weight: 400;">Biased opinion: we&rsquo;d argue us. Less-biased criteria to apply when you&rsquo;re shopping:</span></p>'
    '<p><b>Local workroom or warehouse</b><span style="font-weight: 400;"> (not a franchise dispatcher).</span></p>'
    '<p><b>Named installers, not sub-contractors</b><span style="font-weight: 400;"> &mdash; ask if they&rsquo;re W-2 or 1099.</span></p>'
    '<p><b>Authorized dealer status</b><span style="font-weight: 400;"> for at least Hunter Douglas or Norman.</span></p>'
    '<p><b>Written lifetime warranty</b><span style="font-weight: 400;"> on materials, plus a labor warranty in writing.</span></p>'
    '<p><b>Physical showroom</b><span style="font-weight: 400;"> you can visit with real samples.</span></p>'
    '<p><b>Review count and recency</b><span style="font-weight: 400;"> &mdash; not just stars; check whether reviews are this quarter or three years old.</span></p>'
)

fdiv_id, fwrap_id, fhead_id, fans_id = nid(), nid(), nid(), nid()

fdiv = copy.deepcopy(FAQ_DIVIDER_T); fdiv["id"] = fdiv_id; fdiv["parent"] = FAQ_PARENT; fdiv["children"] = []
fwrap = copy.deepcopy(FAQ_WRAPPER_T); fwrap["id"] = fwrap_id; fwrap["parent"] = FAQ_PARENT; fwrap["children"] = [fhead_id, fans_id]
fhead = copy.deepcopy(FAQ_HEAD_T); fhead["id"] = fhead_id; fhead["parent"] = fwrap_id; fhead["children"] = []; fhead["settings"]["text"] = faq_q
fans = copy.deepcopy(FAQ_ANS_T); fans["id"] = fans_id; fans["parent"] = fwrap_id; fans["children"] = []; fans["settings"]["text"] = faq_a

content.extend([fdiv, fwrap, fhead, fans])

faq_parent = by_id[FAQ_PARENT]
faq_parent["children"] = list(faq_parent["children"]) + [fdiv_id, fwrap_id]
print(f"\nAdded new FAQ '{faq_q[:60]}...' -> div={fdiv_id} wrap={fwrap_id} head={fhead_id} ans={fans_id}")
print(f"FAQ parent children count now: {len(faq_parent['children'])}")

# POST
print("\n=== POSTing ===")
payload = json.dumps({"content": content}).encode()
req = urllib.request.Request(f"{ENDPOINT}/{PAGE_ID}", data=payload, headers=headers, method="POST")
r = urllib.request.urlopen(req)
print(f"POST: {r.status} {r.read().decode()}")

# Verify
req = urllib.request.Request(f"{ENDPOINT}/{PAGE_ID}", headers=headers)
v = json.loads(urllib.request.urlopen(req).read())
print(f"\n=== Verification ===")
print(f"Total elements: was {len(by_id)}, now {len(v['content'])} (delta +{len(v['content']) - len(by_id)})")
v_by_id = {e["id"]: e for e in v["content"]}
# Check each new H2 is present with correct text
for sec, ids in zip(sections, [(new_ids_in_order[i*3+1]) for i in range(len(sections))]):
    h2_id = ids
    e = v_by_id.get(h2_id)
    if e:
        print(f"  H2 {h2_id}: {e['settings'].get('text','')[:80]!r}")
