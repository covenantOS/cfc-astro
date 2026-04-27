# CFC — 7-Day Pinellas Domination Plan

**Target:** Dominate Pinellas County local-intent SERPs in 7 days.
**Constraint:** Pinellas only — Ocala is NOT the goal (the old WP site historically ranked there; that's wasted authority).
**North star:** First non-branded Pinellas click within 7 days; 10+ qualified clicks/week within 14.

---

## State of play (audit, 2026-04-27)

**GSC last 90 days:**
- 7 clicks / 375 impressions / 111 queries
- **216 impressions are Ocala terms** (we're ranking in the wrong city)
- Only 20 impressions are Pinellas/Tampa
- Sitemap submitted, **0 of 36 URLs indexed yet** ← #1 blocker

**Already winning:**
- `custom drapery st petersburg` — **#9 on page 1** (defend + push to top 3)
- `fabric stores ocala` — #9 (Ocala junk, deprioritize)
- `fabric creations` — #9 (branded)

**Striking distance (GSC, Pinellas-relevant):**
- `fabric stores near me` (pos 5.8, 10 imp)
- `window treatments near me` (pos 12.6, 7 imp)

**Competitor set (St Pete SERPs):**
| Competitor | Reviews | Strength | Beatable? |
|---|---|---|---|
| Sapphire Shades & Shutters | 123 | top 3 organic everywhere | YES — design weaker, generic copy |
| Blind & Shutter Gallery (bsgstpete.com) | 76 | Hunter Douglas authority | YES — thin content, no neighborhood pages |
| Shutter Guy St. Pete | — | shutters-only authority | YES — single-service site |
| West Coast Shutters | 81 | local pack #1 | HARD — 32 yrs, deep authority |
| Sunburst Shutters Tampa | — | Tampa Bay broad | YES — generic franchise content |
| Gotcha Covered | 73 | franchise | YES — franchise template |
| Budget Blinds (multiple locations) | 62-649 | volume reviews | HARD — chain |

**KEY KEYWORD GOLDMINES (low KD, real volume, local intent):**

| Keyword | Volume/mo | KD | Trend | Note |
|---|---|---|---|---|
| `drapery near me` | 22,200 | **3** | flat | Massive. KD-3. CFC has drapery focus. ⭐⭐⭐ |
| `plantation shutters near me` | 5,400 | **4** | +23% Q | Local intent gold ⭐⭐⭐ |
| `best plantation shutters` | 260 | **4** | +24% Q | Comparison content opportunity |
| `shutters near me` | 6,600 | **11** | -33% Y | Still high-volume |
| `fabric store st petersburg` | 390 | **1** | flat | We have brand authority here |
| `fabric store st petersburg fl` | 390 | **1** | flat | Same |
| `interior shutters tampa` | 20 | **1** | +33% Y | Tampa term, low vol but easy |
| `window treatments tampa` | 140 | **7** | **+136% Y** | Booming Tampa Bay term ⭐⭐⭐ |
| `plantation shutters tampa fl` | 320 | low | -18% Y | LOW competition |
| `shutters tampa` | 320 | low | flat | LOW competition |
| `plantation shutters st petersburg fl` | 20 | 17 | -50% Y | Hometown anchor — must rank |
| `window treatments st petersburg fl` | 20-50 | 14 | **+400% Q** | Booming |
| `blinds st petersburg fl` | 70 | 17 | flat | Solid hometown |

**Content gaps (from PAA + related searches):**
- "plantation shutters cost" — covered, push it
- "Why are people getting rid of plantation shutters" — covered, push it
- "best plantation shutters st petersburg fl" — MISSING (build comparison page)
- "plantation shutters reviews" — MISSING (build /reviews/ page)
- "is it cheaper to reupholster or buy new" — answer this in upholstery page (AI Overview)
- "average price to reupholster a chair" — pricing transparency on upholstery page
- "Mobile window treatments" — emphasize "we come to you" angle

---

## THE 30-STEP PINELLAS DOMINATION CHECKLIST

### DAY 1 (Monday) — INDEX & FOUNDATION

**1. Force indexing of all 36 URLs.**
Submit each URL via GSC URL Inspection API (live test + request indexing). Sitemap alone won't move 36 URLs in 24h; manual inspection requests do.

**2. Rewrite 12 service-page titles to add "near me" + Tampa Bay regional anchor.**
Current: "Plantation Shutters in St. Petersburg, FL" (generic, geo-anchor only)
New: "Plantation Shutters St. Petersburg & Tampa Bay | Free In-Home Quote"
Why: matches SERP-winners (Shutter Guy uses "Tampa, St Petersburg, FL" in title). Pulls "near me" intent. Adds CTA.

**3. Rewrite 14 area-page titles with full keyword anchor.**
Current: "Window Treatments in Snell Isle, FL"
New: "Snell Isle Window Treatments, Shutters & Drapery | Custom Fabric Creations"

**4. Create AggregateRating schema with verified Google review count.**
The site claims "hundreds of reviews" — we need a numerically-anchored AggregateRating in the LocalBusiness JSON-LD: `aggregateRating: {ratingValue: 5.0, reviewCount: <real_count>}`. Without it, no star rich result. Get the real Google count first.

**5. Build `/reviews/` page with 10-20 real reviews + Google Reviews embed.**
Targets: `plantation shutters st petersburg fl reviews`, `best plantation shutters st petersburg fl`, `[brand] reviews`. Schema: `Review` items.

### DAY 2 (Tuesday) — LOW-KD CONTENT WEDGES

**6. Build `/plantation-shutters-near-me/` landing page.**
Target: KD-4, 5,400/mo. Page format: hero with H1 "Plantation Shutters Near Me — St. Pete & Tampa Bay", clear "we serve all 14 Pinellas neighborhoods" list with internal links, CTA, FAQ. 800+ words, schema FAQ + LocalBusiness with `serviceArea` covering Pinellas zip codes.

**7. Build `/drapery-near-me/` landing page.**
Target: KD-3, 22,200/mo. Same template as #6 but drapery-anchored.

**8. Build `/best-plantation-shutters-st-petersburg/` comparison page.**
Target: KD-4 + the "best ... st pete" related searches. Honest comparison: faux wood vs. basswood vs. composite, brands (Hunter Douglas / Norman / Graber), warranty, price ranges. Itemized "How to pick" buying guide. 2,000+ words. Schema: HowTo + FAQ.

**9. Update `/services/plantation-shutters/` body to target "plantation shutters tampa" + "plantation shutters tampa fl".**
Add a section: "Tampa Bay Plantation Shutters — One Workroom, Whole Bay Coverage." 200 words. Internal link from Tampa Bay regional anchor. The 320/mo Tampa term is LOW competition — easy add.

**10. Update `/services/custom-draperies-curtains/` to defend + push #9 ranking.**
Currently #9 organic for "custom drapery st petersburg". Audit content vs. top-3 (joannsinteriors, gotchacovered). Add: section comparison tables, more local proof, internal links from /plantation-shutters/ and /upholstery/. Aim: top 3 in 14 days.

### DAY 3 (Wednesday) — GBP + CITATIONS + LOCAL SIGNAL DENSITY

**11. Audit + optimize Google Business Profile.**
Verify: hours, services list (all 12), service areas (all 14 neighborhoods + zip codes), photos (10+ recent project photos with geo EXIF), Q&A populated, products (with prices), posts (weekly), website link to https://www.customfabriccreations.net (canonical), phone matches. CFC's primary phone (727) 240-4512.

**12. Add 5 GBP services (matches our top SEO pages):**
- "Plantation Shutters" → links to /services/plantation-shutters/
- "Custom Drapery" → /services/custom-draperies-curtains/
- "Window Shades" → /services/window-shades/
- "Furniture Reupholstery" → /services/furniture-reupholstery/
- "Custom Bedding" → /services/custom-bedding-pillows/

**13. NAP consistency sweep across 20+ citations.**
Required: Yelp, Bing Places, Apple Maps, Houzz, Angi, BBB, Yellow Pages, Foursquare, MapQuest, Manta, BrownBook, Hotfrog, MerchantCircle, eLocal, City-Data, ChamberOfCommerce, Local.com, Cylex, Tupalo, Citysearch. Same name "Custom Fabric Creations", same address (the West St. Pete location 3026 Central Ave Suite 551), same phone (727) 240-4512, same canonical URL.

**14. Submit to 5 industry directories:**
- Houzz (free pro listing) — competitors there: yes
- Angi
- Hunter Douglas dealer locator
- Norman Window Fashions dealer locator
- Kravet trade directory (we're an authorized workroom)

**15. Get listed in 3 local Pinellas neighborhood-specific spots:**
- St Pete Chamber of Commerce
- Pinellas County Convention & Visitors Bureau partner directory
- Tampa Bay Business Journal company directory

### DAY 4 (Thursday) — REVIEW VELOCITY + PROOF

**16. Send a review request to last 30 customers via email.**
Goal: 5 new Google reviews this week. Frame: "If we earned a 5, share on Google. If we didn't, let me know first." Personal from owner Terry. Use actual project specifics ("the Snell Isle Vignette job", etc.). Reviews mentioning neighborhood = local SEO gold.

**17. Build a `/portfolio/` or expand `/gallery/` with location captions.**
Each project: city, neighborhood, services used, brands. Format captions as "Roman shades and motorized drapery — Snell Isle, St. Petersburg." Adds entity-rich localness signal Google associates the domain with these neighborhoods.

**18. Add testimonials with neighborhood + service in alt text on 5 pages.**
Schema `Review` per testimonial. Real names where consented. "Beth M., Old Northeast" outranks "anonymous customer" on every signal.

### DAY 5 (Friday) — INTERNAL LINKING + ENTITY DENSITY

**19. Build a hub-and-spoke internal link map.**
Hubs: /services/, /areas/. Spokes: each individual service & area page. Cross-links: every area page → top 6 services. Every service page → top 5 areas (Snell Isle, Old Northeast, Tierra Verde, St Pete Beach, Clearwater). Use descriptive anchor text ("plantation shutters in Snell Isle") not "click here".

**20. Add neighborhood mentions to homepage above the fold.**
Currently homepage doesn't list neighborhoods until /areas/. Add a "Serving" strip: "Snell Isle • Old Northeast • Tierra Verde • Shore Acres • St. Pete Beach • Clearwater + 8 more". Inline links. Direct entity association on homepage.

**21. Add brand mentions (Hunter Douglas / Norman / Kravet / Graber / Stout) inline on 12 service pages.**
Currently on /brands/ only. Inline mentions on relevant service pages → entity association ("we install Hunter Douglas Silhouette shades in St Petersburg" beats "we install shades in St Petersburg").

**22. Add a "Cost & Pricing" section to top 5 service pages (above the FAQ).**
Pricing transparency = trust + answers PAA "what's the cost" queries. We already have detail in the plantation-shutters FAQ — surface it as a structured table. Schema `Offer` with priceRange.

### DAY 6 (Saturday) — BACKLINKS, SOCIAL, SAB SIGNALS

**23. Reclaim 5+ backlink opportunities.**
- Manufacturer dealer pages (Hunter Douglas, Norman, Graber, Kravet, Stout) — get listed as authorized dealer with link back. These are DA 70+ links.
- Local interior designer sites: 5 St Pete designers we've worked with — request reciprocal listing.
- Old WP site → if it's still up, ensure 301s are pointing at the new URLs (we already use `customfabriccreations.net/old-path` redirects).

**24. Submit guest pitch to 3 local publications:**
- Tampa Bay Times Home section ("How St Pete homeowners are upgrading window treatments in 2026")
- St Pete Catalyst
- Pinellas County Living magazine

**25. Post 3 video walkthroughs to YouTube + embed.**
- "Plantation shutters install in Snell Isle, FL"
- "Roman shades vs roller shades for Florida sun"
- "Reupholstering a Kravet chair"
Each: title with target keyword + neighborhood, full description with link back to canonical service page, keyword-rich tags. YouTube → Google entity graph.

### DAY 7 (Sunday) — SEARCH EXPERIENCE + AI OVERVIEWS

**26. Optimize for AI Overview citations on 5 PAA-targeted questions.**
PAA questions Google is showing AI Overviews for:
- "Is it cheaper to reupholster or buy new furniture?" → answer in /services/furniture-reupholstery/ at top of page in 30-50 words
- "What's the average cost for plantation shutters?" → already in FAQ, surface as featured snippet target
- "Why are people getting rid of plantation shutters?" → /plantation-shutters-regret-downsides/ already targets this — push it via internal links
Pattern: clear question H2, 30-50 word direct answer, supporting paragraph below. Schema `FAQPage`.

**27. Add `BreadcrumbList` + `Service` schema to all area pages explicitly mentioning Pinellas zip codes in `serviceArea`.**
Currently we have `LocalBusiness` and `BreadcrumbList`. Adding `serviceArea: { @type: GeoCircle }` with explicit zip codes (33701, 33702, 33703, 33704, 33705, 33706, 33707, 33708, 33709, 33710, 33711, 33712, 33713, 33714, 33715, 33716) gives Google an explicit "this business serves these zips" signal.

**28. Add `LocalBusiness` schema with verified `aggregateRating` and `review` items.**
Currently the schema lacks aggregate review data. Add real-data ratings (do not fabricate). This is the single biggest "rich result" upgrade we haven't shipped.

### ALWAYS-ON (start now, continuous)

**29. Track rankings daily for 25 priority keywords.**
Use a tracker (DataForSEO Tracker or DIY via the live SERP API I have access to). Watch:
- Top 5 hometown anchors (`plantation shutters st petersburg`, etc.)
- Top 5 near-me terms
- Top 5 Tampa Bay regional terms
- Top 10 long-tail neighborhood combos

Move kept positions for 7+ days = real ranking. Watch for index → rank → click funnel.

**30. Weekly content cadence: 1 long-tail neighborhood post + 1 service-deep post.**
Examples week 2:
- "Custom Plantation Shutters for Snell Isle Mediterranean Revival Homes"
- "Hunter Douglas Silhouette vs Pirouette: A St Pete Designer's Honest Take"

Each: 1,200+ words, real photos with geo-tagged EXIF, FAQ schema, internal links to 3-5 service/area pages, external link to 1 manufacturer or industry source, optimized title + meta. Compound effect over 30+ days.

---

## What "domination" looks like at end of week 1

| Metric | Day 0 | Day 7 target |
|---|---|---|
| URLs indexed | 0/36 | 30+/36 |
| GSC clicks/wk | <2 | 5-10 |
| Pinellas non-branded clicks | 0 | 2+ |
| Page-1 rankings (Pinellas) | 1 | 3-5 |
| Top-3 rankings (Pinellas) | 0 | 1-2 |
| Google reviews (90d delta) | TBD | +5 |
| GBP profile completeness | TBD | 100% |
| Citations consistent | TBD | 20+ |
| AggregateRating in schema | NO | YES |
| /reviews/ page live | NO | YES |
| /plantation-shutters-near-me/ live | NO | YES |
| /drapery-near-me/ live | NO | YES |

## What "domination" looks like at end of week 4

- 8-12 page-1 Pinellas keywords
- 3-5 top-3 Pinellas keywords
- "drapery near me" ranking page-2 (with 22k vol, page-2 is real traffic)
- 25+ qualified clicks/week
- New leads from organic (track via /contact/ form fills with `?utm=organic` UTM tagging)
- Google Maps visible in 3 grid points around Pinellas (track with rank-grid tool)
