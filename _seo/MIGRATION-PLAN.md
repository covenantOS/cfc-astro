# Custom Fabric Creations — WP → Astro Migration Plan

**Generated:** 2026-04-22
**Source site:** https://www.customfabriccreations.net (WordPress + Bricks Builder)
**Target:** [covenantOS/cfc-astro](https://github.com/covenantOS/cfc-astro) (Astro 6 + Tailwind v4, static, Cloudflare Pages)
**Market:** St. Petersburg, FL + Pinellas County
**Total pages:** 37 content pages (+1 404)

---

## Executive Summary

### Ranking-preservation risk: **LOW**

GSC 28-day data shows **only 1 of 37 URLs** gets any impressions (the homepage — 392 impressions, 5 clicks, avg position 20). Every top-ranking query is from the old Ocala market ("window treatments ocala fl", etc.). **There are effectively no St. Pete rankings to preserve** — the migration is a near-greenfield opportunity, not a defensive port.

### What this means for the port

1. **URL structure**: preserve 1:1 (already done — Astro routes match WP slugs exactly). This protects the handful of Ocala rankings while they decay naturally and prevents any indexation churn.
2. **Copy**: rewrite, don't port verbatim. Ten pages still contain Ocala language. Titles are too long on 26 pages. Eight pages lack meta descriptions. We migrate WITH improvements.
3. **Schema**: fix the Alabama-coordinate bug (see Critical Issues) and rationalize the schema graph — current site puts Article schema on service pages, which is wrong.
4. **Greenfield opportunity**: all 14 area pages and most service pages are either unindexed or ranking nowhere. The port is a chance to ship them properly.

---

## Critical Issues Found in Current Site

### 🚨 Geo coordinates are wrong

Every page\u2019s `LocalBusiness` / `Place` schema declares:
```
latitude:  31.72424340
longitude: -85.67212060
```

**That is in rural Alabama, near Tuskegee.** St. Petersburg, FL is at roughly `27.7676, -82.6403`.

This has been broadcasting for who-knows-how-long. It will not directly block Google from understanding the business (address text is correct), but it poisons any map/distance signals and is a trust hit. **Fix before cutover.**

### 🚨 Schema misuse

- **34 of 36 pages have `Article` schema.** Service pages and area pages are not articles. This likely inflates rich-result eligibility for the wrong page type and can suppress the correct type (Service, LocalBusiness).
- **Only 2 pages have `Service` schema.** Should be on all 12 service pages.
- **FAQPage schema on only 3 pages.** Most service + area pages have FAQ-able content.

### ⚠️ Title/description hygiene

- **26 pages have titles >65 characters** (Google truncates at ~60). The long titles appear to be raw rendered H1s, not hand-written `<title>` tags.
- **7 pages have titles <35 characters** (thin — `/`, `/about/`, `/areas/`, `/brands/`, `/contact/`, `/gallery/`, `/services/`).
- **8 pages have no meta description** — the top-level utility pages + `/services/custom-banquettes/`.

### ⚠️ Ocala residue (10 pages)

Still references Ocala or Marion County in body copy. These must be rewritten during port, not copy-pasted:

| Pages | Ocala mentions |
|---|---|
| `/services/custom-draperies-curtains/` | 2 |
| `/services/custom-blinds/` | 2 |
| `/services/custom-cornices-valances/` | 2 |
| `/services/outdoor-window-shades/` | 2 |
| `/services/custom-bedding-pillows/` | 2 |
| `/services/custom-banquettes/` | 2 |
| `/services/commercial-window-treatments/` | 2 |
| `/services/services-interior-decor-tampa/` | 2 |
| `/about/` | 1 |
| `/services/` | 1 |

### ⚠️ Structural gaps

- **`/brands/` and `/gallery/` are missing H1s**
- **`/brands/` is thin (240 words)** — per prior project context, brand/authorized-dealer pages are commercial-intent money pages and should be 800+ words
- **`/gallery/` is thin (218 words)** — needs actual project captions per installation

---

## Preservation Checklist (do these on every page port)

For each page, copy AND verify:

- [ ] **URL slug** (1:1 — no changes during initial cutover)
- [ ] **`<title>`** → rewrite to ≤60c, include primary keyword + \u201cSt. Petersburg\u201d or neighborhood where relevant
- [ ] **Meta description** → 140\u2013160c, distinct from title, contains CTA hook
- [ ] **Canonical URL** → must point to the target URL (handled automatically by `BaseLayout.astro`)
- [ ] **H1** → one per page, matches intent, includes primary keyword naturally
- [ ] **H2/H3 hierarchy** → preserve section structure from WP
- [ ] **Body copy** → port full content, but rewrite any Ocala/Marion County mentions → St. Pete / Pinellas
- [ ] **Internal links** → preserve all internal anchors. Add new ones from service\u2194area interlinking
- [ ] **Images** → preserve original file names (where sensible) + alt text + position
- [ ] **OG image** → carry over or regenerate
- [ ] **Schema** → emit correct type per page (see schema plan below). Do NOT emit Article schema for non-articles.
- [ ] **Robots meta** → `/thank-you/` stays noindex; everything else indexable

## Schema Plan (target post-migration)

| Page type | Schema types |
|---|---|
| Homepage (`/`) | `LocalBusiness` + `WebSite` + `Organization` + `BreadcrumbList` |
| `/about/` | `AboutPage` + `LocalBusiness` + `BreadcrumbList` |
| `/contact/` | `ContactPage` + `LocalBusiness` (with full geo/hours/areaServed) + `BreadcrumbList` |
| `/services/` (hub) | `CollectionPage` + `BreadcrumbList` |
| `/services/{slug}/` | `Service` (with `provider` → LocalBusiness, `areaServed`, `serviceType`) + `BreadcrumbList` + `FAQPage` where FAQs exist |
| `/areas/` (hub) | `CollectionPage` + `BreadcrumbList` |
| `/areas/{slug}/` | `LocalBusiness` (with proper geo for the area) + `BreadcrumbList` + `FAQPage` where FAQs exist |
| `/brands/` | `CollectionPage` + `BreadcrumbList` (list `Brand` entities for Hunter Douglas, Norman, Graber, Kravet, Stout) |
| `/gallery/` | `ImageGallery` + `BreadcrumbList` |
| 3 plantation guides | `Article` + `BreadcrumbList` (these ARE articles) |

**`LocalBusiness` canonical:** emit one global LocalBusiness node from `BaseLayout.astro` with correct geo (27.7676, -82.6403), proper address, phone `(727) 240-4512`, opening hours, `areaServed` listing all 14 service areas.

---

## Cutover Sequence

### Phase A — pre-cutover (this Astro build)

1. ✅ URL structure in place (1:1 with WP)
2. ⏳ Port content (page-by-page, see `PORTING-ORDER.md`)
3. ⏳ Add schema blocks (single `Schema.astro` component emitting type-appropriate JSON-LD)
4. ⏳ Download + optimize all 204 unique images to `public/images/`
5. ⏳ Form submissions → wire to Cloudflare Function → email or webhook
6. ⏳ Sitemap verified — already configured via `@astrojs/sitemap`

### Phase B — DNS cutover

1. Deploy Astro build to Cloudflare Pages, test on preview URL
2. Submit new sitemap to GSC (on the same `sc-domain:` property — domain property already covers `www.`)
3. Point `www.customfabriccreations.net` DNS at Cloudflare Pages
4. Verify all 37 URLs return 200 on production
5. Request indexing of key pages via GSC URL Inspection

### Phase C — post-cutover (week 1\u20132)

1. Monitor GSC coverage report daily — watch for any 404/soft-404 reports on previously-indexed URLs
2. Keep the old WP install accessible at a staging URL for 30 days in case of emergency rollback
3. Monitor Cloudflare analytics for any URLs generating 404s from referrers
4. Build the first 1\u20132 backlinks to the new site (even an internal GBP website field update counts)

### Rollback plan

If migration causes unexpected drop:
1. Re-point `www` DNS back to WP host (TTL is short — revert is minutes)
2. No data is lost — the WP install is untouched throughout
3. Astro build stays on Pages preview URL until fixed

Since current St. Pete rankings are effectively zero, the downside of migration is bounded.

---

## KPI Targets

| Metric | Current (28d, Apr 2026) | 90d target | 180d target | 365d target |
|---|---|---|---|---|
| GSC impressions | 976 | 5,000 | 15,000 | 40,000 |
| GSC clicks | 15 | 80 | 300 | 900 |
| Indexed URLs | ~37 | 38 | 42 | 50 |
| Ranking KWs (pos \u226420) | ~10 (all Ocala) | 40 (St. Pete) | 120 | 300 |
| Avg CWV (mobile LCP) | ?? (WP on Bricks) | <2.5s | <2.0s | <1.8s |
| Pages with correct schema | 2/36 | 37/37 | 37/37 | 37/37 |

---

## Files in this plan

- `MIGRATION-PLAN.md` — this document
- `PAGE-AUDIT.md` — per-page current state + issue flags
- `PORTING-ORDER.md` — priority-ranked porting sequence
- `URL-MAP.md` — old-to-new URL mapping (confirming 1:1)
- `audit.csv` — machine-readable audit dump
