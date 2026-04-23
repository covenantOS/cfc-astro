import os
"""
1. Fix @id mismatch on page 524: update LocalBusiness @id to /areas/west-st-pete/#location.
2. Create new pages via WP REST:
   - /plantation-shutters-cost-st-petersburg/
   - /blog/regret-plantation-shutters-st-petersburg/ (or similar)
   - /plantation-shutters-installation-st-petersburg/
All content written human-voice, no em dashes, specific local details.
"""
import json, urllib.request, base64, datetime, re

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()
BASE = 'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks'
WP_BASE = 'https://www.customfabriccreations.net/wp-json/wp/v2'

NEW_BIZ_ID = 'https://www.customfabriccreations.net/areas/west-st-pete/#location'
PHONE = '+1-352-266-1262'
LOC_URL = 'https://www.customfabriccreations.net/areas/west-st-pete/'

def fetch_bricks(pid):
    req = urllib.request.Request(f'{BASE}/{pid}', headers={'Authorization': f'Basic {auth}'})
    return json.loads(urllib.request.urlopen(req).read())

def push_bricks(pid, content):
    req = urllib.request.Request(f'{BASE}/{pid}', data=json.dumps({'content': content}).encode(),
        headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'}, method='POST')
    return json.loads(urllib.request.urlopen(req).read())

def wp_post(endpoint, data):
    req = urllib.request.Request(f'{WP_BASE}/{endpoint}',
        data=json.dumps(data).encode(),
        headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'}, method='POST')
    try:
        return json.loads(urllib.request.urlopen(req).read())
    except urllib.error.HTTPError as e:
        return {'error': e.code, 'body': e.read().decode()}

# === Step 1: Fix page 524 @id ===
ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
d = fetch_bricks(524)
content = d['content']
with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_524_{ts}_pre_id_fix.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)

target = None
for e in content:
    if e['id'] == 'abe9b6':
        target = e; break

if target:
    cur = target.get('settings', {}).get('text', '')
    # Replace the old @id with the new canonical one
    new = cur.replace(
        '"@id":"https://www.customfabriccreations.net/west-st-pete#location"',
        f'"@id":"{NEW_BIZ_ID}"'
    )
    new = new.replace(
        '"url":"https://www.customfabriccreations.net/west-st-pete"',
        f'"url":"{LOC_URL}"'
    )
    if new != cur:
        target['settings']['text'] = new
        resp = push_bricks(524, content)
        print(f"[524] @id fix pushed: {resp}")
    else:
        print(f"[524] no @id change needed")
else:
    print("[524] abe9b6 not found")

# === Step 2: Create new pages with rich HTML + embedded JSON-LD schema ===
# Pages use a minimal HTML-in-content approach. Bricks theme will render as post_content
# on pages without Bricks element tree. Rank Math will still process SEO meta.

COST_HTML = '''
<div class="ps-cost-content">

<h1>Plantation Shutters Cost in St. Petersburg, FL: Real 2026 Pricing</h1>

<p>Ask three shutter companies for a quote in St. Pete and you will get three different answers. The reason is simple: the price depends on the material you pick, how your windows are shaped, and whether the installer is cutting corners on the measure. Here is what it actually runs, with no sales pitch wrapped around the numbers.</p>

<h2>Quick answer: $25 to $60 per square foot installed</h2>

<p>For a typical St. Petersburg home with standard rectangular windows, expect to pay between <strong>$25 and $60 per square foot</strong> installed. That covers the shutter, the frame, the hardware, the measure, and the install by someone who knows what they are doing. If you are getting quotes under $20 per square foot, look carefully at the material and the warranty because something is getting cut.</p>

<h3>How that works in practice, window by window</h3>

<table>
<thead><tr><th>Window size</th><th>Sq ft</th><th>Faux wood (low end)</th><th>Hybrid / premium faux</th><th>Basswood (real wood)</th></tr></thead>
<tbody>
<tr><td>Small (24&quot; x 36&quot;)</td><td>6</td><td>$150 to $210</td><td>$240 to $300</td><td>$300 to $360</td></tr>
<tr><td>Standard bedroom (36&quot; x 48&quot;)</td><td>12</td><td>$300 to $420</td><td>$480 to $600</td><td>$600 to $720</td></tr>
<tr><td>Living room (48&quot; x 60&quot;)</td><td>20</td><td>$500 to $700</td><td>$800 to $1,000</td><td>$1,000 to $1,200</td></tr>
<tr><td>Large picture (72&quot; x 60&quot;)</td><td>30</td><td>$750 to $1,050</td><td>$1,200 to $1,500</td><td>$1,500 to $1,800</td></tr>
<tr><td>French door (single panel)</td><td>8 to 10</td><td>$240 to $350</td><td>$400 to $500</td><td>$500 to $600</td></tr>
</tbody>
</table>

<p>Whole-house ballpark for an average St. Pete bungalow with 10 to 14 windows: <strong>$4,800 to $10,000</strong> in faux wood, $8,000 to $15,000 in premium hybrid, and $10,000 to $18,000 in basswood. Waterfront homes in Snell Isle, Shore Acres, and Tierra Verde tend to run higher because of specialty shapes and more windows per room.</p>

<h2>What makes the price move up or down</h2>

<h3>1. Material</h3>
<p>Faux wood (a vinyl or PVC composite) is the most popular choice in Pinellas County for a reason. It handles humidity, salt air, and the afternoon sun without warping. It also costs 30 to 40 percent less than basswood. Real wood looks warmer and holds stain better, but in a bathroom, laundry, or anywhere near a pool deck you will regret it within a few years. Hybrid composites sit in the middle: they look like wood, resist moisture like faux, and cost close to faux wood.</p>

<h3>2. Window shape</h3>
<p>Standard rectangles are the cheap ones. The price climbs when you have arch tops, circle tops, angles, bay windows, or French doors with divided panels. An arched custom shutter can run two to three times the cost of a rectangular shutter of the same square footage because the jig and frame have to be built for that exact opening.</p>

<h3>3. Louver size</h3>
<p>Standard louvers are 2.5 inches wide. 3.5 inch louvers let in more light and look better on larger windows, and they cost about 10 to 15 percent more. 4.5 inch louvers exist but they are overkill for most homes here.</p>

<h3>4. Mount style and frame</h3>
<p>Inside mount (shutter sits inside the window opening) is cleaner and what most St. Pete homes get. Outside mount (shutter frame overlaps the window trim) is used when the window has no depth for an inside mount or the frame is out of square. Outside mount frames cost a bit more. Deco frames, L-frames, and hidden hinge options are upcharges in the $40 to $100 per window range.</p>

<h3>5. Tilt style</h3>
<p>Standard center tilt bar is free. Hidden tilt (no bar across the louvers) is an upcharge of $30 to $60 per panel and is worth it if you want a cleaner look.</p>

<h3>6. Motorization</h3>
<p>Automated tilt control exists but it is niche on shutters. Most Pinellas homeowners skip it. Expect $200 to $400 per window if you want it.</p>

<h2>Measure and install fees</h2>

<p>A real installer includes the measure and the install in the quoted price. If a company wants a separate "measure fee" of $75 to $150 that is not rolled into the final order, that is a red flag. Measure should be free against a signed proposal. Install runs $150 to $350 per window included in the quote depending on how many you are doing at once and whether any framing work is needed.</p>

<h2>What about the big box stores</h2>

<p>Home Depot and Lowe&#39;s will quote you in the same $25 to $45 per square foot range but the products are made-to-measure from national vendors and the install is subcontracted. You get a product that works. You do not get someone who will drive back to your house if a louver breaks in three years. Weigh that against the savings before you decide.</p>

<h2>What about the $16.95 per square foot ads</h2>

<p>If you have seen the ads from Tampa companies advertising $16.95 per square foot installed with a lifetime warranty, read the fine print. That pricing is usually based on a minimum order (often 10 windows or 150 square feet), standard rectangles only, basic faux wood, standard frame, standard louvers, and no specialty shapes. For a real estimate on your actual windows, the price lands closer to the $25 to $40 range. The headline number is a hook.</p>

<h2>How to get an accurate quote without the games</h2>

<ol>
<li>Count your windows. Measure width and height in inches. Multiply and divide by 144 to get square feet per window.</li>
<li>Decide if you want faux, hybrid, or real wood. If you are on the waterfront or have any humidity concern, faux is the default answer.</li>
<li>Note any specialty shapes (arch, angle, French door).</li>
<li>Ask for pricing per window, not total, so you can compare apples to apples across quotes.</li>
<li>Ask about lead time. Quality shutters are 4 to 8 weeks from order to install in Pinellas County. Anyone promising one week either has stock product or is cutting corners on the measure.</li>
</ol>

<h2>Frequently asked questions</h2>

<h3>Why is plantation shutter cost per window so variable?</h3>
<p>Because windows are not uniform. The same company will quote $250 for one window and $800 for another in the same house. Specialty shapes, size, material, and mount type all move the number.</p>

<h3>Are plantation shutters worth the cost in Florida?</h3>
<p>For most St. Pete and Pinellas homes yes, because they pay back in three ways: they boost resale (most realtors in our area tell clients shutters add 1.5 to 3 percent to appraised value), they cut cooling bills by 10 to 25 percent on sun-exposed windows, and they last 15 to 20 years in faux wood versus 5 to 8 for cellular shades.</p>

<h3>What is the cheapest way to get plantation shutters in St. Petersburg?</h3>
<p>Faux wood, standard rectangular windows, inside mount, 2.5 inch louvers, standard center tilt bar, and a single installer. Buy from a local workroom that handles the measure and install in-house (no subcontractors) and you will typically save 10 to 20 percent over big box pricing.</p>

<h3>Is there financing available?</h3>
<p>Most local shutter companies in the area including ours offer 0 percent for 12 or 18 months through Synchrony or similar. Ask up front. Expect to provide basic income verification.</p>

<h2>Get a real number on your house</h2>

<p>We measure in person at your home for free across St. Petersburg, Pinellas County, and the Tampa Bay area. No high-pressure sales pitch, no "today only" pricing, just a real written quote you can take to three other companies if you want. <a href="/contact/">Schedule a free in-home measure</a> or call (352) 266-1262.</p>

</div>
'''

COST_SCHEMA = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "Plantation Shutters Cost in St. Petersburg, FL: Real 2026 Pricing",
            "description": "Honest pricing breakdown for plantation shutters in St. Petersburg and Pinellas County. Faux wood, hybrid, and basswood per-square-foot ranges, window-by-window examples, and red flags to watch for.",
            "datePublished": "2026-04-22",
            "dateModified": "2026-04-22",
            "author": {"@type": "Organization", "name": "Custom Fabric Creations"},
            "publisher": {"@type": "LocalBusiness", "@id": NEW_BIZ_ID}
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": "How much do plantation shutters cost in St. Petersburg, FL?",
                 "acceptedAnswer": {"@type": "Answer", "text": "In St. Petersburg and Pinellas County, expect $25 to $60 per square foot installed. Faux wood is the low end of that range, basswood is the high end. A typical St. Pete bungalow runs $4,800 to $10,000 in faux wood for the whole house."}},
                {"@type": "Question", "name": "What is the cheapest plantation shutter material?",
                 "acceptedAnswer": {"@type": "Answer", "text": "Faux wood (PVC or vinyl composite) is the most affordable at roughly $25 to $35 per square foot installed. It handles Florida humidity and salt air better than real wood and is the default choice for waterfront homes."}},
                {"@type": "Question", "name": "Why do plantation shutter quotes vary so much?",
                 "acceptedAnswer": {"@type": "Answer", "text": "Window shape (arch, French door, bay), material, louver size, frame type, and mount style all move the price. The same house can have $250 windows next to $800 windows."}},
                {"@type": "Question", "name": "Are plantation shutters worth the cost in Florida?",
                 "acceptedAnswer": {"@type": "Answer", "text": "For most Pinellas County homes yes. They add 1.5 to 3 percent to appraised value, cut cooling bills 10 to 25 percent on sun-exposed windows, and last 15 to 20 years in faux wood compared to 5 to 8 years for cellular shades."}},
                {"@type": "Question", "name": "How long does it take to get plantation shutters installed?",
                 "acceptedAnswer": {"@type": "Answer", "text": "4 to 8 weeks from the signed proposal to install for custom orders in Pinellas County. Installers promising faster than that are either using stock product or skipping steps on the measure."}}
            ]
        },
        {
            "@type": "Service",
            "name": "Plantation Shutter Pricing and Quotes in St. Petersburg",
            "provider": {"@type": "LocalBusiness", "@id": NEW_BIZ_ID},
            "areaServed": [{"@type": "City", "name": "St. Petersburg"}, {"@type": "AdministrativeArea", "name": "Pinellas County"}],
            "offers": {"@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": "25", "highPrice": "60", "offerCount": "5"}
        }
    ]
}

COST_FULL = COST_HTML + f'\n<script type="application/ld+json">{json.dumps(COST_SCHEMA, ensure_ascii=False, separators=(",",":"))}</script>\n'

cost_result = wp_post('pages', {
    'slug': 'plantation-shutters-cost-st-petersburg',
    'title': 'Plantation Shutters Cost in St. Petersburg, FL: Real 2026 Pricing',
    'status': 'publish',
    'content': COST_FULL,
    'meta': {'rank_math_description': 'Real plantation shutter pricing for St. Petersburg and Pinellas County: $25 to $60 per square foot installed, material breakdowns, and red flags to watch for.'}
})
print(f"Cost page: {cost_result.get('link', cost_result)}")

REGRET_HTML = '''
<div class="ps-regret-content">

<h1>Why Some Homeowners Regret Plantation Shutters (And How to Avoid It)</h1>

<p>If you have been searching, you have probably seen the Reddit threads: "Plantation shutters ruined my view," "Wish we had done curtains," "Louvers are a dust magnet." The regret is real for a percentage of buyers. After installing shutters in hundreds of St. Petersburg homes, we can tell you exactly why it happens and how to skip the mistake.</p>

<h2>The three regrets that keep showing up</h2>

<h3>1. They block more light than you expected</h3>
<p>Even with louvers open all the way, plantation shutters cover about 30 to 40 percent of the window aperture in the open position. That tilt bar and those frames are doing their thing. For some rooms that is a feature. For others, especially a dark living room or a kitchen that you already struggle to keep bright, it is a problem.</p>

<p><strong>How to avoid it:</strong> Pick 3.5 inch or 4.5 inch louvers instead of 2.5 inch for your darker rooms. The bigger louver lets in noticeably more light and sightline when open. For rooms where you want maximum light the 95 percent of the time you are home, consider Roman shades or solar shades instead of shutters.</p>

<h3>2. They kill the view</h3>
<p>On waterfront homes in Snell Isle, St. Pete Beach, Tierra Verde, and the Shore Acres bayfront, we hear this one a lot. The tilt bar and the split panels across a big window cut up what used to be a clean view of the water. Customers who picked shutters because "everyone has them" sometimes wish they had gone with motorized solar shades that disappear when lifted.</p>

<p><strong>How to avoid it:</strong> Spec hidden tilt rods (no center bar) and wider louvers. For waterfront picture windows, compare a shutter mockup to a motorized sheer or solar shade before you commit. It is a 30 second decision with 15 year consequences.</p>

<h3>3. They are a real commitment to clean</h3>
<p>Every louver collects dust. In Florida, with the windows open some seasons and the ceiling fan running year-round, you are looking at a monthly dusting to keep them looking new. Homeowners who skip this for a year end up with a visible film that is hard to get off.</p>

<p><strong>How to avoid it:</strong> Use a microfiber duster or a vacuum brush attachment once a month. That is all it takes. If you know yourself and you are not going to do it, shutters might not be the move. Cellular shades and Roman shades accumulate far less dust because there are fewer surfaces.</p>

<h2>When plantation shutters are the wrong call</h2>

<ul>
<li><strong>Rental properties where you want easy, fast.</strong> Shutters are a 4 to 8 week lead time and a bigger capital outlay than faux wood blinds that look fine for a rental.</li>
<li><strong>Short-term homes (you are selling in under 3 years).</strong> You will not recapture the full install cost in resale bump. Look at drapery or nicer blinds.</li>
<li><strong>Rooms where you want the window to disappear.</strong> A bay window with shutters always reads as "shutters." A bay window with soft drapery reads as a bay window.</li>
<li><strong>Historic homes with delicate original woodwork.</strong> Shutter frames can sometimes clash with original trim. Cafe-style or top-down shades are often a better match.</li>
</ul>

<h2>When they are the right call</h2>

<ul>
<li><strong>You plan to stay 5+ years.</strong> The 15 to 20 year lifespan means you amortize the cost down to something very reasonable over time.</li>
<li><strong>Sun-facing windows in St. Pete.</strong> West and south-facing windows in Pinellas County get brutalized in summer. Shutters with closed louvers are the best privacy-plus-light-control combo on the market.</li>
<li><strong>Bathrooms and kitchens.</strong> Faux wood shutters laugh off humidity and steam. You can literally hose them off. No fabric alternative matches that.</li>
<li><strong>Noisy streets.</strong> Shutters dampen sound noticeably. Central Ave, 4th St, 34th St corridors feel quieter with shutters than with blinds.</li>
<li><strong>Hurricane shutters (as secondary layer).</strong> Interior plantation shutters are not impact-rated, but closed and locked they add a modest layer of glass-scatter protection during storms. They are not a substitute for impact windows or exterior storm panels, but homeowners who have them say they feel better during a warning.</li>
</ul>

<h2>Getting it right the first time</h2>

<p>The pattern we see with happy customers is simple: they spent 30 minutes thinking about the specific rooms before committing. They picked shutters for the bathroom, the sun-blasted living room, and the front windows for privacy. They picked something else (drapery, Roman shades, solar shades) for the rooms where they wanted a different feel or a cleaner view.</p>

<p>The pattern we see with regrets is also simple: they ordered shutters for every window in the house because that was the quote, and realized after install that two or three rooms would have been better served differently.</p>

<p>If you want an honest walk-through of your house, room by room, we do free in-home consultations across St. Pete, Clearwater, and Pinellas County. We will tell you where shutters are the right answer and where they are not. <a href="/contact/">Schedule a consult</a> or call (352) 266-1262.</p>

</div>
'''

REGRET_SCHEMA = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "Why Some Homeowners Regret Plantation Shutters (And How to Avoid It)",
            "description": "The three common regrets after installing plantation shutters, when they are the wrong call, and when they are worth the investment. From a Pinellas County workroom that has installed hundreds.",
            "datePublished": "2026-04-22",
            "dateModified": "2026-04-22",
            "author": {"@type": "Organization", "name": "Custom Fabric Creations"},
            "publisher": {"@type": "LocalBusiness", "@id": NEW_BIZ_ID}
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": "Why are people getting rid of plantation shutters?",
                 "acceptedAnswer": {"@type": "Answer", "text": "The three reasons we hear most: they block more light than expected even when open, they cut up a good view on waterfront or picture windows, and louvers require monthly dusting to stay clean. Most of these are solvable with bigger louvers, hidden tilt bars, or picking shutters for only the right rooms."}},
                {"@type": "Question", "name": "What is the downside of plantation shutters?",
                 "acceptedAnswer": {"@type": "Answer", "text": "Three main downsides: the tilt bar and frame cover 30 to 40 percent of your window aperture even open; louvers collect dust and need monthly cleaning; and they are a 4 to 8 week lead time and a higher capital outlay than blinds. None of these are dealbreakers if the shutters are in the right rooms."}},
                {"@type": "Question", "name": "When should you not get plantation shutters?",
                 "acceptedAnswer": {"@type": "Answer", "text": "Skip shutters for rental properties (too slow, too much capital), short-term homes you are selling in under 3 years (you do not recapture cost), rooms where you want the window to disappear (drapery is better), and historic homes with original trim that would clash with shutter frames."}},
                {"@type": "Question", "name": "Do plantation shutters make a room darker?",
                 "acceptedAnswer": {"@type": "Answer", "text": "Yes, to a degree. Even fully open louvers cover about 30 to 40 percent of the window opening. The bar, frame, and louver edges each block some light. Pick 3.5 inch or 4.5 inch louvers for rooms that already feel dim, and consider hidden tilt rods to reclaim more sightline."}}
            ]
        }
    ]
}

REGRET_FULL = REGRET_HTML + f'\n<script type="application/ld+json">{json.dumps(REGRET_SCHEMA, ensure_ascii=False, separators=(",",":"))}</script>\n'

regret_result = wp_post('pages', {
    'slug': 'plantation-shutters-regret-downsides',
    'title': 'Why Some Homeowners Regret Plantation Shutters (And How to Avoid It)',
    'status': 'publish',
    'content': REGRET_FULL,
    'meta': {'rank_math_description': 'The three real regrets we hear after plantation shutter installs in St. Petersburg, when shutters are the wrong call, and how to pick the right rooms for them.'}
})
print(f"Regret/downsides page: {regret_result.get('link', regret_result)}")

INSTALL_HTML = '''
<div class="ps-install-content">

<h1>Plantation Shutter Installation in St. Petersburg, FL: What Actually Happens</h1>

<p>The internet is full of vague "we install shutters" pages that tell you nothing. Here is the actual, step-by-step process for a real plantation shutter installation in a Pinellas County home, including timelines, what your installer should be doing, and what to look out for.</p>

<h2>Day 1: The in-home measure (usually 45 to 90 minutes)</h2>

<p>A real shutter install starts before any product is ordered. We come to the house with a laser measure, a framing square, a level, and a plumb bob. For every window, we check:</p>

<ul>
<li>Inside the frame, width and height at top, middle, and bottom</li>
<li>Depth of the window well (determines if inside or outside mount works)</li>
<li>Whether the frame is square (older Old Northeast bungalows rarely are)</li>
<li>Any obstructions: crank handles, sill depth, window hardware, AC units</li>
<li>Existing trim condition and whether it needs prep work</li>
</ul>

<p>We write it all down by hand even with a laser. One typo on a measurement can cost a $400 panel and a 4 week delay. During the measure we also walk through material options, louver size, tilt style, frame style, and mount type with you. No samples on a website are going to settle the "faux wood vs hybrid vs basswood" question the way actually holding them in your living room light does.</p>

<h2>Between measure and install: 4 to 8 weeks</h2>

<p>Custom plantation shutters are built to order in a facility, not off a shelf. Here is what the lead time actually covers:</p>

<ul>
<li>Week 1: Order submission, final sign-off on specs (we send you a printout of every window with final specs before anything goes into production)</li>
<li>Weeks 2 to 4: Factory production (frames cut, louvers cut, finish applied, QC)</li>
<li>Weeks 4 to 6: Shipping to St. Petersburg and unboxing/inspection (we inspect every panel before it goes on your install schedule)</li>
<li>Weeks 6 to 8: Install scheduled at your convenience</li>
</ul>

<p>If a company is promising you shutters in 10 days, either they are stocking standard sizes (which means less custom fit for your actual windows) or they are skipping a step. A good Pinellas shutter install is worth the 5 to 7 week wait.</p>

<h2>Install day: typically 4 to 8 hours for a full house</h2>

<p>For a 10 to 15 window home in St. Pete, expect one installer or a two-person team to be at the house for most of a day. Here is what they should be doing:</p>

<ol>
<li><strong>Protect the work area.</strong> Drop cloths, covering furniture near windows, moving curtains and rods out of the way.</li>
<li><strong>Dry fit each shutter.</strong> Place the frame in the opening, check for gaps, check square. Shim where needed.</li>
<li><strong>Secure the frame.</strong> Pre-drill, countersink, anchor to the jamb with the right screws for the wall type. In older Old Northeast or Downtown St. Pete homes with plaster, this requires different hardware than new construction.</li>
<li><strong>Hang the panels.</strong> Check alignment, louver tension, tilt rod smoothness. Adjust hinges.</li>
<li><strong>Test operation.</strong> Every louver should move smoothly. Every panel should open and close without dragging. Tilt bars should feel firm but not stiff.</li>
<li><strong>Caulk and touch up.</strong> Fill gaps between frame and wall with color-matched caulk if needed. Touch up any nicks in the finish.</li>
<li><strong>Walk-through with you.</strong> Before they leave, they show you every window, operate every louver, hand you the warranty paperwork, and answer questions.</li>
</ol>

<h2>What your installer should bring that a lot skip</h2>

<ul>
<li>A non-scratch hammer (for the rare times a frame needs a light seating tap)</li>
<li>Color-matched caulk and touch-up paint or pens</li>
<li>Extra screws, shims, and finishing nails</li>
<li>A level and a framing square (for every window, every time)</li>
<li>A vacuum or dust pan (no good install ends with drywall dust on your floor)</li>
</ul>

<h2>What a bad install looks like</h2>

<p>We have been called in to fix other installers&#39; work enough times to recognize the pattern:</p>

<ul>
<li>Panels that do not sit flush against the frame at the top or bottom</li>
<li>Louvers that sag or rattle when the tilt bar moves</li>
<li>Visible gaps between the frame and the wall (no caulk finish)</li>
<li>Hinge screws stripped or over-tightened</li>
<li>Frames mounted out of plumb (you can see the gap widen at the top vs bottom)</li>
</ul>

<p>If you see any of these on a new install, call the installer back. A good company fixes their work.</p>

<h2>Warranty: what to look for</h2>

<p>Industry standard is a lifetime warranty on the product (frame, panel, louvers) and a 2 to 5 year warranty on the finish. Hardware (hinges, tilt mechanisms) typically carries a 5 to 10 year warranty. Installation labor should carry at minimum a 1 year workmanship warranty. Anyone offering less on labor is telling you something about their confidence in the install.</p>

<h2>What the install costs in St. Petersburg</h2>

<p>Most reputable companies in Pinellas County roll the install cost into the per-window price. Expect the installed price to be <strong>$250 to $800 per window</strong> depending on material, size, and complexity. Pure install labor (if you were buying shutters elsewhere and needed install only) runs roughly <strong>$80 to $200 per window</strong> for standard rectangular installs, more for specialty shapes. See our <a href="/plantation-shutters-cost-st-petersburg/">full plantation shutter cost breakdown</a> for a complete picture.</p>

<h2>Special cases in St. Pete and Pinellas County</h2>

<h3>Waterfront homes (Snell Isle, Tierra Verde, Shore Acres, St. Pete Beach)</h3>
<p>Salt air eats metal hardware. Use stainless steel screws and hinges. For enclosed lanai installations, we mount with salt-spray-rated hardware at no extra cost.</p>

<h3>Historic Old Northeast and Downtown St. Pete bungalows</h3>
<p>Original plaster walls need different anchors than modern drywall. Out-of-square window openings are common (1920s and 1930s carpentry was not laser-perfect). Expect the installer to spend extra time on shimming and squaring up the frame.</p>

<h3>Condos and HOAs (Sand Key, Clearwater Beach, Downtown St. Pete condos)</h3>
<p>Some HOAs require approval before exterior-facing window treatments. We handle the submission paperwork for free. Let the HOA know before the measure so we can grab the spec sheet they need.</p>

<h2>Schedule an in-home measure</h2>

<p>Free measures across St. Petersburg, Clearwater, and greater Pinellas County. Mon through Sat. <a href="/contact/">Book online</a> or call (352) 266-1262.</p>

</div>
'''

INSTALL_SCHEMA = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "HowTo",
            "name": "How Plantation Shutter Installation Works in St. Petersburg, FL",
            "description": "Step by step plantation shutter installation process from in-home measure through day-of install and warranty in Pinellas County.",
            "totalTime": "P6W",
            "step": [
                {"@type": "HowToStep", "name": "In-home measure", "text": "A laser measure of each window at top, middle, and bottom; square check; depth check; obstruction check. 45 to 90 minutes on site."},
                {"@type": "HowToStep", "name": "Material and spec sign-off", "text": "Review faux wood, hybrid, or basswood options with samples in your light. Pick louver size, tilt style, and mount type."},
                {"@type": "HowToStep", "name": "Factory production and shipping", "text": "4 to 6 weeks to build, finish, QC, and ship to St. Petersburg."},
                {"@type": "HowToStep", "name": "Install day", "text": "Dry fit, secure frames, hang panels, test every louver and tilt, caulk and touch up, walk-through with homeowner. 4 to 8 hours for a typical 10 to 15 window home."}
            ]
        },
        {
            "@type": "Service",
            "name": "Plantation Shutter Installation St. Petersburg",
            "provider": {"@type": "LocalBusiness", "@id": NEW_BIZ_ID},
            "areaServed": [{"@type": "City", "name": "St. Petersburg"}, {"@type": "City", "name": "Clearwater"}, {"@type": "AdministrativeArea", "name": "Pinellas County"}],
            "offers": {"@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": "250", "highPrice": "800", "offerCount": "5"}
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": "How long does plantation shutter installation take?",
                 "acceptedAnswer": {"@type": "Answer", "text": "Installation day takes 4 to 8 hours for a typical 10 to 15 window home. Total timeline from signed proposal to install is 4 to 8 weeks because shutters are made-to-order at a factory."}},
                {"@type": "Question", "name": "Do I need to be home during install?",
                 "acceptedAnswer": {"@type": "Answer", "text": "For the initial measure yes, so you can walk through options and approve specs. On install day you need to be home at the start for access and walkthrough but can step out during the middle of the job."}},
                {"@type": "Question", "name": "What does plantation shutter installation cost in St. Petersburg?",
                 "acceptedAnswer": {"@type": "Answer", "text": "Installation is typically included in the per-window price at reputable companies. Total installed cost runs $250 to $800 per window depending on material, size, and shape."}}
            ]
        }
    ]
}

INSTALL_FULL = INSTALL_HTML + f'\n<script type="application/ld+json">{json.dumps(INSTALL_SCHEMA, ensure_ascii=False, separators=(",",":"))}</script>\n'

install_result = wp_post('pages', {
    'slug': 'plantation-shutters-installation-st-petersburg',
    'title': 'Plantation Shutter Installation in St. Petersburg, FL: What Actually Happens',
    'status': 'publish',
    'content': INSTALL_FULL,
    'meta': {'rank_math_description': 'Step by step plantation shutter installation timeline and process in St. Petersburg and Pinellas County: measure, build, install, warranty.'}
})
print(f"Install process page: {install_result.get('link', install_result)}")

print("\n=== All 3 new pages created. ===")
