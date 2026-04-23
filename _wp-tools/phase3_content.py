import os
"""Phase 3 — SERP-gap content rebuild based on top-5 competitor analysis.

Additions:
1. Enhance Specialty Shapes body (enumerate shape types)
2. NEW section: Plantation Shutters for French Doors, Sliders & Pass-Throughs
3. NEW section: How It Works — 4-Step Process
4. NEW section: Why Pinellas Homeowners Choose CFC (differentiator)
5. NEW FAQ: What's a cheaper option than plantation shutters?
"""
import json, urllib.request, base64, datetime, secrets, copy

AUTH = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
EP = 'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/524'

def get_live():
    req = urllib.request.Request(EP, headers={'Authorization': f'Basic {AUTH}'})
    return json.loads(urllib.request.urlopen(req).read())

def post_live(content_list):
    body = {'content': content_list}
    req = urllib.request.Request(EP, data=json.dumps(body).encode('utf-8'), method='POST',
        headers={'Authorization': f'Basic {AUTH}', 'Content-Type': 'application/json'})
    return json.loads(urllib.request.urlopen(req).read())

def new_id():
    return secrets.token_hex(3)

d = get_live()
content = d['content']
by_id = {e['id']: e for e in content}
ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_524_{ts}_pre_phase3.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)
print(f"Backup: bricks_backup_524_{ts}_pre_phase3.json")
print(f"Starting elements: {len(content)}")

# -------- 1. Enhance Specialty Shapes body text --------
# Find the Specialty Shapes H2 and its sibling text block
specialty_text_new = (
    "From sunbursts and arched transoms to hexagons, trapezoids, and elongated tombstones — every "
    "specialty-shape window in your St. Petersburg home can wear custom plantation shutters. We build "
    "eyebrow arches, bay and bow window configurations, angled tops for pitched ceilings, and full "
    "sidelight treatments for entries. Each shape is hand-templated from measurements taken on-site, "
    "not ordered from a pre-made catalog. Hexagon and trapezoid shutters mount on radius hinges so "
    "louvers still tilt cleanly across odd angles. Arched tops ship with matching rail curvature and "
    "louver pitch so the profile reads correctly from inside the room. Specialty shapes price 25-40% "
    "above standard rectangular — but an uncovered shape window is the one your eye goes to every "
    "time you walk into the room, and the one every buyer notices during a showing."
)

# locate specialty shapes h2 and following text block
shapes_h2 = None
for e in content:
    s = e.get('settings', {})
    if isinstance(s, dict) and e['name'] == 'heading' and s.get('tag') == 'h2':
        txt = s.get('text', '')
        if isinstance(txt, str) and 'Specialty Shape' in txt:
            shapes_h2 = e
            break

if shapes_h2:
    # find the text-basic sibling right after this h2 in the same parent
    parent = by_id.get(shapes_h2['parent'])
    if parent:
        children = parent.get('children', [])
        idx = children.index(shapes_h2['id'])
        # look for the next text-basic after the h2
        for cid in children[idx+1:idx+4]:
            c = by_id.get(cid)
            if c and c['name'] == 'text-basic':
                old = c['settings'].get('text', '')
                c['settings']['text'] = specialty_text_new
                print(f"Updated Specialty Shapes text: {cid} (was {len(old) if isinstance(old,str) else 0} chars, now {len(specialty_text_new)})")
                break

# -------- Build new sections to append to main container 9d29a5 --------
MAIN = '9d29a5'
main_el = by_id[MAIN]

# Templates to copy style from existing Phase 2 sections
def clone_div():
    # minimal divider
    return {
        'id': new_id(), 'name': 'divider', 'parent': MAIN, 'children': [],
        'settings': {'_cssGlobalClasses': ['oxazza'], 'style': 'solid'}
    }

def clone_h2(text, anchor=None):
    s = {'tag': 'h2', 'text': text, '_cssGlobalClasses': ['fitdee']}
    if anchor:
        s['_cssId'] = anchor
    return {
        'id': new_id(), 'name': 'heading', 'parent': MAIN, 'children': [],
        'settings': s
    }

def clone_text(html):
    return {
        'id': new_id(), 'name': 'text-basic', 'parent': MAIN, 'children': [],
        'settings': {'text': html, '_cssGlobalClasses': ['exkkzs'], 'tag': 'custom', 'customTag': 'div'}
    }

# -------- 2. NEW: Plantation Shutters for Doors section --------
doors_div = clone_div()
doors_h2 = clone_h2("Plantation Shutters for French Doors, Sliders & Pass-Throughs", anchor="doors")
doors_txt = clone_text(
    "<p>Not every opening in your home is a standard window. French doors, sliding glass doors, "
    "and kitchen pass-throughs call for specialty shutter mounting — and it is one of the installs "
    "we build most often in St. Petersburg.</p>"
    "<p><strong>French doors.</strong> We use a flush-mount frame that clears your lever handle "
    "without the oversized rectangular cutout block most dealers default to. The result: more "
    "louver coverage, a cleaner profile, and no gap around the handle.</p>"
    "<p><strong>Sliding glass doors.</strong> Bypass shutters run on top-mounted tracking and stack "
    "against the adjacent wall when open, so nothing interferes with floor thresholds, rugs, or "
    "sliding screen-door clearance. Standard 4½-inch louvers with hidden control rods.</p>"
    "<p><strong>Pass-throughs and café windows.</strong> Half-height café-style shutters on kitchen "
    "pass-throughs let you keep airflow and sightlines between rooms while still getting the "
    "built-in look. Common in Snell Isle bungalows and Old Northeast remodels.</p>"
    "<p><strong>Bay and bow windows.</strong> Mullion-free corner details mean your shutters wrap "
    "the curve without visual breaks. Hinge geometry is calculated per window so louvers align "
    "across all panels.</p>"
)

# -------- 3. NEW: How It Works section --------
how_div = clone_div()
how_h2 = clone_h2("How We Build Your Shutters — Our 4-Step Process", anchor="process")
how_txt = clone_text(
    "<p><strong>1. Free in-home consultation.</strong> We come to your St. Pete home with material "
    "samples, finish swatches, hinge hardware, and louver-size mockups so you can compare 2½-inch, "
    "3½-inch, and 4½-inch louvers against your actual window. Typically one hour, no sales pressure, "
    "no deposit required to start.</p>"
    "<p><strong>2. Laser measurement and photo documentation.</strong> Every opening is measured to "
    "1/16 inch. Specialty shapes (arches, hexagons, bays) get a physical template taken on-site, "
    "not estimated off a drawing. Photos of the opening, sill, and adjacent trim go into your file "
    "so installers have the full context.</p>"
    "<p><strong>3. Order placed and built.</strong> You approve final specs — frame style, louver "
    "size, finish color, mount type, tilt control. Lead time: 3-5 weeks for standard rectangular, "
    "5-7 weeks for specialty shapes and motorized. We call when your shutters ship to the local "
    "warehouse for final QC before install day.</p>"
    "<p><strong>4. Installation.</strong> Two-person crew, one-day install for most whole-home "
    "projects. We bring touch-up paint, extra slats, and the manufacturer warranty card. "
    "Drop cloths, cleanup, and a walk-through of operation and care are included. If anything "
    "needs a tweak, we handle it before we leave.</p>"
)

# -------- 4. NEW: Why CFC differentiator section --------
why_div = clone_div()
why_h2 = clone_h2("Why Pinellas Homeowners Choose CFC Over Other Shutter Installers", anchor="why-cfc")
why_txt = clone_text(
    "<p>Most shutter companies in St. Petersburg are resellers. They take your measurements, place "
    "the order with an out-of-state factory, and drive back when the truck shows up. We are "
    "structured differently.</p>"
    "<p><strong>In-house workroom and upholstery studio.</strong> CFC operates a full fabrication "
    "and upholstery workroom on-site. When your shutters need a tweak after install — a louver "
    "adjustment, a finish touch-up, a panel re-hung after a remodel — we handle it here, often "
    "same day. No shipping the panel to a factory three states away.</p>"
    "<p><strong>Installers who do only this.</strong> Our install crew averages 12+ years hanging "
    "shutters in Florida homes, not general contractors moonlighting on shutters between other "
    "jobs. They know how St. Petersburg's older Craftsman trim profiles behave, how concrete-block "
    "walls take anchors, and how to hang specialty shapes without callbacks.</p>"
    "<p><strong>Whole-window-treatment coverage under one roof.</strong> Because we also build "
    "custom drapery, cornices, Roman shades, and upholstery, we are the only St. Pete shop that "
    "can layer drapery over your new shutters in a single project instead of coordinating "
    "between two vendors. That matters for Snell Isle and Old Northeast formal rooms where the "
    "shutter-plus-drapery layered look is standard.</p>"
    "<p><strong>Local, family-run, insured, and on your side.</strong> We carry full liability and "
    "workman's comp, we pull permits when required, and the person who quoted your job is often "
    "the person who walks the install with you at the end.</p>"
)

new_sections_els = [doors_div, doors_h2, doors_txt, how_div, how_h2, how_txt, why_div, why_h2, why_txt]
new_section_ids = [e['id'] for e in new_sections_els]

# Add to content list and to main container's children
content.extend(new_sections_els)
main_el['children'].extend(new_section_ids)
print(f"Added {len(new_sections_els)} new section elements to main container {MAIN}")

# -------- 5. NEW FAQ: cheaper option --------
# FAQ parent is b42667. Clone template from one of the existing FAQ sets.
# Template IDs from prior work: a00dfd (div), 1322fe (wrap), 67ad6f (heading), ac8ac6 (text)
FAQ_PARENT = 'b42667'
faq_parent = by_id[FAQ_PARENT]

# Find an existing FAQ wrapper to copy as template
template_wrap = None
for cid in faq_parent.get('children', []):
    c = by_id.get(cid)
    if c and c['name'] == 'block':
        template_wrap = c
        break

if template_wrap:
    # Clone the wrapper + its heading + text children
    def deep_clone_tree(src_id, new_parent):
        src = by_id.get(src_id)
        if not src:
            return None
        new_el = copy.deepcopy(src)
        new_el['id'] = new_id()
        new_el['parent'] = new_parent
        new_el['children'] = []
        # recurse children
        for child_id in src.get('children', []):
            child_clone = deep_clone_tree(child_id, new_el['id'])
            if child_clone:
                new_el['children'].append(child_clone['id'])
                content.append(child_clone)
                by_id[child_clone['id']] = child_clone
        return new_el

    # Clone divider (last divider in faq parent before wrappers) - simplified: just clone wrapper
    new_wrap = deep_clone_tree(template_wrap['id'], FAQ_PARENT)
    content.append(new_wrap)
    by_id[new_wrap['id']] = new_wrap

    # Find heading + text inside cloned wrapper and set text
    q_text = "What's a cheaper option than plantation shutters in St. Petersburg?"
    a_text = (
        "Budget alternatives include faux-wood blinds ($150-$300 per window installed), woven-wood "
        "shades ($200-$400), cellular/honeycomb shades ($150-$350), and Roman shades ($100-$350). "
        "These run 40-60% less than plantation shutters up front. For Florida homes the math often "
        "flips over a 15-20 year window: plantation shutters last 20-25 years; blinds and shades "
        "typically need replacement at 5-8 years because of humidity, Gulf-sun fading, and cord or "
        "lift-mechanism failure. Replacing blinds three or four times over two decades usually "
        "equals or exceeds a single shutter install. If budget is tight today, faux-wood blinds "
        "are a respectable placeholder — we install them too — until you are ready to upgrade."
    )
    for child_id in new_wrap.get('children', []):
        c = by_id.get(child_id)
        if c and c['name'] == 'heading':
            c['settings']['text'] = q_text
        elif c and c['name'] == 'text-basic':
            c['settings']['text'] = f"<p>{a_text}</p>"
    # append to FAQ parent children
    faq_parent['children'].append(new_wrap['id'])
    print(f"Added new FAQ wrapper {new_wrap['id']} to FAQ parent {FAQ_PARENT}")

print(f"Final elements: {len(content)}")

# -------- Push --------
resp = post_live(content)
print(f"Push response: {resp}")
print("Phase 3 complete.")
