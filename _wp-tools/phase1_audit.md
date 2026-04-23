# Phase 1 Self-Audit — /services/plantation-shutters/

**Date:** 2026-04-22
**Shipped:** Phase 1 (geo-swap) + Phase 1b (body-copy cleanup) + 4 new FAQs
**Method:** Direct Bricks Builder content write via custom REST endpoint

---

## Gap analysis (13 gaps → status)

| # | Gap | Status | Notes |
|---|-----|--------|-------|
| 1 | **Geo targeting wrong (Central FL / Tampa Bay primary)** | CLOSED | H1, meta, badges, all H2s, body paragraphs, FAQ answers, neighborhoods list now St. Pete-primary. "Tampa Bay" retained once as secondary service-area mention in neighborhoods CTA. |
| 2 | **FAQ too thin (5 Qs, missed 4 major PAA features)** | CLOSED | 9 FAQs live: added cost ($25-$60/sq ft), downside (cost/light gap/lead time), style 2026 (+400% QoQ trend stat), home value (70-90% ROI). Each targets a PAA SERP feature. |
| 3 | **No cost/pricing transparency** | CLOSED | New FAQ has itemized ranges by material, per-window + whole-home estimates, explicit "no bundled starting-at pricing" positioning. |
| 4 | **No construction/materials deep-dive** | OPEN (Phase 2) | Current faux-wood vs basswood blurb is short. Needs construction table: core material, finish, hinge type, louver size options. |
| 5 | **No specialty shapes section** | OPEN (Phase 2) | Arched, angled, bay/bow, sidelights not covered. Specialty shapes = premium pricing tier + low-competition keyword. |
| 6 | **No dealer/manufacturer badges** | OPEN (Phase 2) | Hunter Douglas, Norman, Graber, Eclipse trust badges missing. |
| 7 | **Neighborhood density thin** | PARTIAL | Neighborhoods list now lead with Snell Isle, Old NE, Downtown, Shore Acres, St. Pete Beach, Treasure Island, Tierra Verde, Sand Key, Belleair Shore. Could add +10 more for schema LocalBusiness areaServed density. |
| 8 | **In-house workroom differentiator absent** | OPEN (Phase 2) | CFC has an upholstery/drapery studio — competitive wedge vs pure-dealer competitors. Not currently called out on this page. |
| 9 | **Motorization depth thin** | OPEN (Phase 2) | One-liner mention. Should expand: Hunter Douglas PowerView vs Somfy vs generic, battery vs wired, hub/app integration. |
| 10 | **Warranty specifics missing** | OPEN (Phase 2) | Needs explicit warranty table: manufacturer (lifetime limited), finish, hardware, CFC install. |
| 11 | **No before/after gallery** | OPEN (Phase 2) | Visual proof absent. Add 6-8 local project thumbnails w/ neighborhood captions for local signals. |
| 12 | **Schema markup (Service + FAQPage)** | PARTIAL | Rank Math auto-generates basic Article + breadcrumb schema. Service schema w/ areaServed + FAQPage mirroring the 9 FAQs not yet added. Phase 2: add via Rank Math schema builder or JSON-LD injection. |
| 13 | **SEO title + meta description still geo-wrong** | OPEN (blocker staged) | Live `<title>` + `<meta description>` still say "Plantation Shutters Central Florida...". Rank Math stores these in `rank_math_title` / `rank_math_description` post_meta — not exposed via my current REST endpoint. Staged fix: `rank_math_snippet.php` (paste into Code Snippets), then I can push the update. Alternate path: update manually in wp-admin Rank Math UI. **This is the #1 remaining blocker — SEO title is 90%+ of title-tag ranking weight.** |

**Score:** 3 closed, 2 partial, 8 open (7 Phase 2 + 1 Rank Math title blocker).

---

## Verification (live page grep)

Post-Phase-1b `curl /services/plantation-shutters/`:

| Term | Hits | Notes |
|------|------|-------|
| St. Petersburg | 15 | H1, H2s, FAQs, service-area |
| St. Pete | 12 | Body copy, casual references |
| Pinellas | 6 | Neighborhoods list, badge |
| Tampa Bay | 5 | 4 are in Rank Math SEO meta (still needs update), 1 is intentional "Tampa Bay and Gulf Coast region" in neighborhoods CTA |
| Central Florida | 11 | ALL from Rank Math title/meta/schema auto-inject — body copy has ZERO remaining |

**Body copy: 100% geo-swapped. Remaining Central Florida mentions are 100% in Rank Math title/desc/schema, blocked on that endpoint.**

---

## Element delta

- Before: 217 Bricks elements
- After: 233 elements (+16 = 4 new FAQs × (divider + wrapper + heading + text))
- FAQ parent children: 9 → 17
- Backups saved: `bricks_backup_524_20260422_092217_pre_phase1.json`, `..._092334_pre_phase1b.json`

---

## Next actions, in order

1. **[30 sec] Rank Math SEO title/description update** — paste `rank_math_snippet.php` into Code Snippets, OR update directly in wp-admin → Pages → Plantation Shutters → Rank Math SEO box. Target:
   - Title: `Plantation Shutters St. Petersburg FL | Custom Faux Wood & Interior Shutters`
   - Description: `Custom plantation shutters in St. Petersburg, FL. Faux wood & basswood built for Florida humidity, Gulf sun, hurricane season. Free in-home consultation across Pinellas County.`
2. **Phase 2 content build** — construction table, specialty shapes, dealer badges, in-house workroom section, motorization depth, warranty table, before/after gallery, Service + FAQPage schema.
3. **Backlink research** — blocked on DataForSEO Backlinks API subscription activation.
