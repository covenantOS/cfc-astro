# Content Porting Order

**How to use this doc:** Work top to bottom. Each row is one Astro page file.

For each page:
1. Open the scraped HTML at `scripts/scraped/html/{slug}.html` for the current copy
2. Open the target Astro page (e.g., `src/pages/services/plantation-shutters.astro`)
3. Apply the actions listed
4. Re-run `seo-page` on the new page before moving on

## Priority scoring

| Tier | Meaning |
|---|---|
| **P0** | High commercial intent + has existing ranking signal OR is the hub/home |
| **P1** | High-content page where rewriting "Central Florida" → St. Pete unlocks local ranking |
| **P2** | Greenfield area pages — 3000w of content waiting to rank in St. Pete |
| **P3** | Utility/trust pages — thin but important for conversions |
| **P4** | Already well-written content (cleanest port) |

---

## P0 — Foundation (port first)

| # | Page | Actions |
|---|---|---|
| 1 | `/` (home) | Rewrite title to 45\u201355c with "St. Petersburg" prominent. Write 150c meta desc. Port hero + service cards + area links. Strip `Article` schema. Add `LocalBusiness` with **correct geo** (27.7676, -82.6403). Rewrite any Ocala language. |
| 2 | `/services/` (hub) | Rewrite 1 Ocala mention. Write title/desc. Strip Article schema. Use `CollectionPage`. |
| 3 | `/areas/` (hub) | Rewrite title/desc. Strip Article schema. Use `CollectionPage` with list of 14 areas. |
| 4 | `/contact/` | Port form + contact info. Thicken to 500+ words (add \u201cwhat to expect in a consultation,\u201d parking, service area bullets). Keep `ContactPage` schema. Wire form action to a real endpoint (Cloudflare Function). |

## P1 — Core service pages (rewrite "Central Florida" → "St. Petersburg")

These pages have 1,100\u20133,500 words each. Copy is substantial but **all target Central Florida** (too broad) or reference Ocala. Rewrite geo during port. Strip `Article` schema, add `Service` schema with proper `provider` and `areaServed`.

| # | Page | Notes |
|---|---|---|
| 5 | `/services/plantation-shutters/` | Already targets St. Pete (best-written service page, 3495w). Schema polish + title shortening. |
| 6 | `/services/custom-draperies-curtains/` | 1245w, 2 Ocala, Central FL. High commercial intent \u2014 port carefully. |
| 7 | `/services/window-shades/` | 1430w, Central FL. Title too long. |
| 8 | `/services/custom-blinds/` | 1124w, 2 Ocala, title truncation bug (first char cut). |
| 9 | `/services/furniture-reupholstery/` | 1308w, Central FL. Second most-valuable service after window treatments. |
| 10 | `/services/drapery-hardware/` | 1548w, Central FL. |
| 11 | `/services/custom-cornices-valances/` | 1494w, 2 Ocala, Central FL. |
| 12 | `/services/outdoor-window-shades/` | 1456w, 2 Ocala, Central FL. |
| 13 | `/services/custom-bedding-pillows/` | 1560w, 2 Ocala, Central FL. |
| 14 | `/services/custom-banquettes/` | 972w, 2 Ocala, no description, slug hint of Central FL. |
| 15 | `/services/commercial-window-treatments/` | 1382w, 2 Ocala, Central FL. |
| 16 | `/services/services-interior-decor-tampa/` | 1453w, 2 Ocala, Central FL. **Slug references Tampa** \u2014 this is a legacy slug. Keep as-is for URL preservation but target St. Pete in copy/title. |

## P2 — Area pages (huge greenfield KW opportunity)

Each area page is already 700\u20133,300 words. The \u201cBlinds Shop\u201d positioning is used in all titles/H1s. **Decision during port:** shift title/H1 pattern from \u201cX Blinds Shop\u201d to \u201cWindow Treatments in X\u201d or \u201cCustom Drapery & Upholstery in X.\u201d Reason: broader commercial relevance, aligned with the brand\u2019s full service range and the luxury direction.

Order these by neighborhood affluence + search volume potential:

| # | Page | Words | Notes |
|---|---|---|---|
| 17 | `/areas/st-petersburg/` | 2228 | Primary geo hub. Must be strongest area page. |
| 18 | `/areas/downtown-st-pete/` | 3015 | Affluent condo market, high intent. |
| 19 | `/areas/snell-isle/` | 2525 | Estates, highest-AOV zone. |
| 20 | `/areas/old-northeast/` | 2729 | Historic district \u2014 interior design sophistication. |
| 21 | `/areas/tierra-verde/` | 3170 | Waterfront estates. |
| 22 | `/areas/st-pete-beach/` | 3311 | Condo + resort market. |
| 23 | `/areas/shore-acres/` | 2964 | Family market. |
| 24 | `/areas/clearwater/` | 3197 | Large population, outside St. Pete core. |
| 25 | `/areas/sand-key/` | 2994 | Condos + waterfront. |
| 26 | `/areas/treasure-island/` | 3210 | Beach + waterfront. |
| 27 | `/areas/belleair-shore/` | 3019 | Private, smaller area. |
| 28 | `/areas/seminole/` | 2864 | Title truncation bug on current site. |
| 29 | `/areas/largo/` | 2966 | Large population. |
| 30 | `/areas/west-st-pete/` | 772 | Thinnest area page \u2014 expand during port. |

## P3 — Utility & trust pages

| # | Page | Actions |
|---|---|---|
| 31 | `/about/` | 825w, 1 Ocala mention. Rewrite Ocala. Port story, establish since-2000 + 25-year positioning + in-house workroom detail. Add `AboutPage` + `LocalBusiness` schema. |
| 32 | `/brands/` | 240w \u2014 **must thicken to 800+ words.** Add a section per brand (Hunter Douglas, Norman, Graber, Kravet, Stout) explaining what CFC does with each and why it matters. Add H1. Add `CollectionPage` schema listing `Brand` entities. |
| 33 | `/gallery/` | 218w \u2014 expand. Add H1. Real project captions with neighborhood + service type. Schema: `ImageGallery`. Consider filtering by service/area. |
| 34 | `/thank-you/` | Already scaffolded. Keep noindex. |

## P4 — Blog guides (cleanest port)

These are already well-written and have strong schema. Port verbatim, strip "Custom Fabric Creations" suffix from titles, and keep `Article` + `FAQPage` + `HowTo` where present.

| # | Page | Notes |
|---|---|---|
| 35 | `/plantation-shutters-cost-st-petersburg/` | 1258w, has Article + FAQPage + Service schema. |
| 36 | `/plantation-shutters-installation-st-petersburg/` | 1035w, has HowTo + FAQPage + Service schema. |
| 37 | `/plantation-shutters-regret-downsides/` | 859w, has FAQPage schema. |

---

## Cross-cutting work (do once, applies to all)

These happen in `src/layouts/BaseLayout.astro` and a new `src/components/Schema.astro`:

- [ ] Ship a single `Schema.astro` component that emits type-appropriate JSON-LD based on a `pageType` prop
- [ ] Emit global `LocalBusiness` node from `BaseLayout.astro` with correct geo (27.7676, -82.6403), full address, hours, `areaServed` = all 14 areas
- [ ] Emit `BreadcrumbList` automatically from URL path
- [ ] Wire the contact form to a Cloudflare Function that sends to `info@customfabriccreations.net` (or Slack/webhook)
- [ ] Add sticky mobile CTA component (call button) \u2014 mobile is where this audience lives
- [ ] Download all 204 unique images from `scripts/scraped/images.txt` into `public/images/` with proper names
- [ ] Generate OG images per page type (1200x630)
- [ ] Verify Montserrat + Playfair Display pairing against actual copy once ported
