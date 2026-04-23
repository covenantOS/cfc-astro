# CFC 2026 SEO Action Plan — Plantation Shutters St. Petersburg

**Date:** 2026-04-22
**Goal:** Rank page 1 Google for "plantation shutters st petersburg fl" + map pack
**Current state:** Zero impressions for target kw. 14 ranked kws sitewide, all Ocala legacy.

---

## Diagnosis

### What we shipped (Phase 1 + 2, today)
- Full geo-swap (Central FL → St. Pete) across H1, H2s, body, FAQs, neighborhoods
- 10 FAQs (was 5), each targeting a PAA SERP feature
- 4 new Phase 2 sections: Materials & Construction, Specialty Shapes, Authorized Dealer, In-House Workroom
- Rank Math title/meta/focus-kw updated via custom REST endpoint
- **Element delta:** 217 → 249 Bricks elements (+32)

### SERP reality check (DataForSEO, St. Pete geo-targeted)
Query: `plantation shutters st petersburg fl`
- **Top of SERP:** 4 paid ads
- **Map pack:** West Coast Shutters (81 reviews, 5★), Blind & Shutter Gallery (76 reviews, 5★), Sapphire Shades (123 reviews, 4.9★)
- **First organic (pos 8 overall):** West Coast Shutters (windowshutters.com)
- **CFC:** not in top 20. Not indexed for this query.

### Keyword targets (sorted by opportunity)
| Keyword | SV | KD | Intent | Notes |
|---------|-----|-----|--------|-------|
| plantation shutters near me | 5,400 | 4 | commercial | **PRIMARY** — proximity-weighted, low KD |
| plantation shutters st petersburg | 70 | 8 | commercial | Geo-exact, low comp |
| shutters st petersburg fl | 50 | 12 | commercial | Expansion |
| custom plantation shutters | 880 | 22 | commercial | Broader fallback |
| plantation shutters cost | 2,400 | 18 | informational | Blog target |

### Competitive wedge
**West Coast Shutters is the one to dethrone.** They own map pack #1 AND organic #1. Their weakness: generic "shutter specialist" positioning; no in-house workroom, no upholstery cross-sell. CFC's differentiators = in-house workroom + upholstery/drapery studio — this must be surfaced everywhere.

---

## Priority stack (2026 local SEO weights)

1. **Google Business Profile + reviews (≈40%)** — #1 factor, single biggest gap
2. **On-page + entity signals (≈25%)** — schema, NAP consistency, mentions
3. **Content depth + E-E-A-T (≈20%)** — author bylines, credentials, original photos
4. **Backlinks + citations (≈10%)**
5. **Technical + page experience (≈5%)**

---

## Phase 3 — This week (the ASAP queue)

### 3.1 Submit URL for indexing (5 min) — **DO FIRST**
- GSC → URL Inspection → paste `https://www.customfabriccreations.net/services/plantation-shutters/`
- Click "Request Indexing"
- Do same for homepage + /services/ hub + every page you updated today
- **Why:** page is brand-new in its current form; Google hasn't recrawled

### 3.2 Schema markup (30 min) — Service + FAQPage + LocalBusiness
Write `schema_injection.py` — inject JSON-LD via Rank Math's `rank_math_schema_*` meta or via a Bricks Code element in the page head. Spec:

```json
[
  {
    "@type": "Service",
    "name": "Custom Plantation Shutters Installation",
    "provider": {"@type": "LocalBusiness", "name": "Custom Fabric Creations"},
    "areaServed": ["St. Petersburg", "Pinellas County", "Snell Isle", "Old Northeast", "Downtown St. Pete", "Shore Acres", "Tierra Verde", "St. Pete Beach", "Treasure Island", "Sand Key", "Belleair", "Seminole", "Largo", "Clearwater"],
    "offers": {"@type": "Offer", "priceRange": "$25-$60 per sq ft"}
  },
  {
    "@type": "FAQPage",
    "mainEntity": [/* mirror all 10 live FAQs verbatim */]
  },
  {
    "@type": "LocalBusiness",
    "name": "Custom Fabric Creations",
    "address": {...},
    "geo": {"latitude": 27.7676, "longitude": -82.6403},
    "aggregateRating": {...from GBP...}
  }
]
```

### 3.3 Internal linking audit (15 min)
- Homepage → add link to `/services/plantation-shutters/` with anchor "plantation shutters in St. Petersburg"
- `/services/` hub → verify link exists + update anchor to geo-keyword
- Every other service page → add sidebar/footer link to plantation shutters
- Blog posts (if any) → contextual links
- **Why:** Google needs internal signals for topical relevance; current orphan state is killing us

### 3.4 GBP content push (30 min)
- 3 new GBP posts this week (offer, update, event)
- Upload 10+ new photos (plantation shutter install, workroom, team, before/after)
- Add all 10 FAQs to GBP Q&A section (pre-empt competitor planting)
- Verify category is "Window Treatment Store" + secondary "Interior Designer"
- **Review velocity plan:** request 2 reviews/week from past 60 days of customers (text + email with direct link). Target: 20 reviews in 90 days (gets us above Blind & Shutter Gallery's 76 by Q4).

---

## Phase 4 — Weeks 2-4

### 4.1 Neighborhood area pages (13 pages)
Spec from `plantation_shutters_v2.md`. Each 600-800 words, unique:
- `/areas/snell-isle-plantation-shutters/`
- `/areas/old-northeast-plantation-shutters/`
- `/areas/downtown-st-pete-plantation-shutters/`
- `/areas/shore-acres-plantation-shutters/`
- `/areas/tierra-verde-plantation-shutters/`
- `/areas/st-pete-beach-plantation-shutters/`
- `/areas/treasure-island-plantation-shutters/`
- `/areas/sand-key-plantation-shutters/`
- `/areas/belleair-plantation-shutters/`
- `/areas/seminole-plantation-shutters/`
- `/areas/largo-plantation-shutters/`
- `/areas/clearwater-plantation-shutters/`
- `/areas/gulfport-plantation-shutters/`

Each page: local landmarks, typical home styles, humidity/salt-air angle, past project callout, link back to main plantation shutters page + GBP + 2-3 cross-neighborhood links. This is the bulk of the entity/areaServed signal.

### 4.2 Before/after gallery
- 8-12 images uploaded via WP media library
- Alt text: "Plantation shutters install in [neighborhood] St. Petersburg FL"
- Caption format: "[Style] plantation shutters — [neighborhood], [year]"
- Insert into page via Bricks as ImageGallery block between Specialty Shapes + Authorized Dealer sections

### 4.3 Author/E-E-A-T signals
- Add "About the installer" block to page: photo, credentials, years experience, local tenure
- Create `/about/daniel-bio/` page with:
  - Years doing fabric + window treatments
  - Certifications (Hunter Douglas, Norman dealer credentials, any install training)
  - Press mentions / community involvement
  - Photo
- Link from plantation shutters page author byline → bio page
- Schema: `Person` + `knowsAbout` properties

### 4.4 Google Reviews widget on page
- Embed GBP reviews (via WP plugin or custom shortcode)
- Place right after FAQs, before final CTA
- Live review count builds trust + refreshes content for crawlers

---

## Phase 5 — Months 1-3

### 5.1 Blog content (PAA attack)
Publish these in order:
1. **"Are plantation shutters out of style in 2026?"** — strong PAA, easy win. 1200 words, link to services page.
2. **"Why are people getting rid of plantation shutters?"** — counter-narrative to contrarian PAA; position as "some remove because of X; but here's why they're worth it in FL climate"
3. **"Plantation shutters cost in St. Petersburg, FL (2026 guide)"** — intercepts cost searchers. Itemized ranges, per-window + whole-home pricing.
4. **"Plantation shutters vs. blinds vs. roller shades in Florida humidity"** — comparison table, captures comparative intent.
5. **"Hunter Douglas vs. Norman plantation shutters — 2026 buyer's guide"** — brand comparison, brings dealer brand searchers.

Each post: 1000-1500 words, H2 structure, internal link to services page + 2-3 area pages, FAQ block at bottom.

### 5.2 Local citation sweep
NAP consistency audit across:
- Yelp, BBB, Angi, HomeAdvisor, Houzz, Thumbtack
- Local chamber (St. Pete Chamber of Commerce — paid listing worth it)
- Florida business directories
- Industry-specific: IWCE (Int'l Window Coverings Expo) member directory, Hunter Douglas dealer locator

### 5.3 Backlink outreach (once DataForSEO Backlinks API unblocked)
- Run backlink gap analysis vs. West Coast Shutters + Blind & Shutter Gallery
- Target the links they have that we don't
- Local angle: St. Pete home design blogs, interior designer partnerships, real estate agent partnerships ("shutter consult" referral deals)

### 5.4 Core Web Vitals + technical
- Run Lighthouse on plantation shutters page
- Image compression (WebP, target <100KB each)
- Preload LCP image
- Verify HTTPS, canonical tags, no render-blocking JS
- Mobile usability audit

---

## 2026 E-E-A-T checklist (Google's updated rater guidelines)

**Experience (first-hand)**
- [ ] Original install photos (not stock)
- [ ] Before/after from actual CFC projects
- [ ] Video walkthrough of workroom (embed on page)
- [ ] Customer testimonials with names + neighborhoods

**Expertise (subject-matter knowledge)**
- [ ] Author bio w/ credentials
- [ ] Cite manufacturer specs (hinge gauges, louver sizes, finish specs) — already partially done in Materials section
- [ ] Reference industry standards (WCMA safety, CPSC)

**Authoritativeness (recognition)**
- [ ] Hunter Douglas / Norman / Graber dealer badges (images + schema)
- [ ] Press mentions page
- [ ] Awards / memberships
- [ ] Structured data for certifications

**Trust (the hardest; 2026 emphasis)**
- [ ] Reviews on-page (widget)
- [ ] Schema aggregateRating
- [ ] Physical address + local phone on every page
- [ ] Privacy policy, terms, warranty page
- [ ] SSL, no security warnings
- [ ] Contact methods: phone, email, form, in-person visit option

---

## Tracking + targets (90 days)

| Metric | Today | 30d | 60d | 90d |
|--------|-------|-----|-----|-----|
| GSC impressions, plantation shutters kw family | 0 | 200 | 1,500 | 5,000 |
| GSC clicks on `/services/plantation-shutters/` | 0 | 5 | 40 | 150 |
| Ranked keywords sitewide | 14 | 40 | 120 | 300 |
| GBP reviews | ~current | +8 | +16 | +20 |
| Position for "plantation shutters st petersburg fl" | >100 | 30-50 | 15-25 | 5-12 |
| Map pack inclusion | No | Maybe | Top 5 | Top 3 |

**Weekly check-in:** GSC performance report filtered to `/services/plantation-shutters/` + DataForSEO ranked_keywords delta.

---

## What's blocking

1. **DataForSEO Backlinks API subscription** — needed for gap analysis vs. competitors
2. **GBP admin access** — I can draft posts but Daniel must post them
3. **Review outreach list** — need past 60d customer contact list to launch velocity plan
4. **Physical address confirmation for LocalBusiness schema** — need exact NAP string

---

## Order of operations (the actual do-list)

Today:
1. ✅ Ship Phase 2 content (done)
2. ✅ Update Rank Math meta (done)
3. GSC Request Indexing × 5 pages (Daniel, 5 min)
4. Write schema_injection.py + push (Claude)
5. Internal linking from homepage + /services/ hub (Claude)

This week:
6. GBP: 3 posts, 10 photos, FAQ sync (Daniel)
7. Review velocity outreach drafted (Claude writes, Daniel sends)
8. Before/after gallery — Daniel provides images, Claude uploads + places

Next 2 weeks:
9. Area pages (13) — Claude drafts, Daniel reviews, Claude publishes
10. Author/E-E-A-T bio page (Claude)
11. Reviews widget embedded (Claude)

Month 2-3:
12. Blog content (5 posts in order)
13. Citations sweep
14. Backlinks (once DataForSEO unblocked)
15. Technical / CWV pass

---

**Bottom line:** The page is now properly built. The war is now won on **reviews + indexing + internal signals + area pages** — in that order. West Coast Shutters is beatable; they have no in-house workroom and no upholstery cross-sell, and their content is thinner than our new page. Execute the next 10 days aggressively and we should see first impressions for target kw within 2-3 weeks.
