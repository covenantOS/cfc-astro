# CFC Astro — Project Handoff

**Last updated:** 2026-04-22
**Outgoing operator:** Claude (Opus 4.7) working with Daniel
**Incoming operator:** Open Claw

This doc is the single source of truth for picking up the Custom Fabric Creations (CFC) migration + SEO engagement without re-reading every conversation. Read this top to bottom before touching anything.

---

## 1. What this project is

CFC is **Custom Fabric Creations** — a custom window treatments + upholstery studio that moved its base from Ocala to St. Petersburg, FL. Daniel is the operator driving SEO. Two parallel workstreams:

1. **Live WordPress site** — `https://www.customfabriccreations.net` on WP + Bricks Builder. Ongoing on-page SEO: content rewrites, schema, internal linking, NAP updates.
2. **Astro rebuild** (this repo) — 1:1 port of the WP site onto Astro 6 + Tailwind v4, destined for Cloudflare Pages. The rebuild is the long-term home. WP is currently live.

**Client business facts:**
- Established 2000 (25+ years), locally owned, in-house workroom, fully insured
- Main phone: **(727) 240-4512** (sitewide footer)
- West St. Pete location (confirmed NAP): **3026 Central Ave Suite 551, St. Petersburg FL 33712 / (352) 266-1262**
- Main office address TBD (phone inconsistency will drag GBP NAP until resolved — flag it, don't auto-unify)
- Correct geo for schema: **27.7676, -82.6403**
- Service area (14 neighborhoods): St. Petersburg, Downtown St. Pete, Old Northeast, Snell Isle, Shore Acres, West St. Pete, Tierra Verde, St. Pete Beach, Treasure Island, Clearwater, Sand Key, Belleair Shore, Seminole, Largo
- Brands carried: Hunter Douglas, Norman, Graber, Kravet, Stout

---

## 2. Daniel — how to work with him

- Wants **fast, practical execution** — less theory, more "here's what I'm doing next"
- Comfortable with SEO concepts (KD, SERP, E-E-A-T) — don't over-explain fundamentals
- Prefers we set up tooling (MCPs, API access) rather than hand-run repeat tasks
- Lead with **what I'm pushing now** (code, Bricks REST, DataForSEO pulls) vs. what he has to do manually (GBP, review requests, indexing submission)
- **Don't pad deliverables with manual tasks I can't execute** (GBP, review outreach, "submit for indexing"). Those belong in a short separate list, not a priority block.
- Don't cite "site not indexed / no rankings" as a finding on a freshly-launched page — that's the starting state, not an insight.
- He gets blunt (sometimes colorful) when I'm wrong — take the feedback and fix it without re-litigating.

---

## 3. Repo layout

```
cfc-astro/
├── HANDOFF.md                ← YOU ARE HERE
├── README.md                 ← stack, dev commands, deployment
├── astro.config.mjs          ← site URL, sitemap, partytown, tailwind
├── package.json              ← Astro 6.1.8, Tailwind v4.2.2, Node ≥22.12
├── src/
│   ├── components/           ← Header, Footer, Hero, HeroBend, ServiceGrid, AreaGrid, FinalCTA, Schema, etc.
│   ├── layouts/              ← BaseLayout, ServiceLayout, AreaLayout
│   ├── lib/
│   │   ├── site.ts           ← SITE / NAV / SERVICES / AREAS / BRANDS — single source of truth
│   │   ├── service-content.ts
│   │   └── area-content.ts
│   ├── pages/                ← URL-1:1 with live site (see _seo/URL-MAP.md)
│   │   ├── services/[slug].astro  ← generates all 12 service pages
│   │   └── areas/[slug].astro     ← generates all 14 area pages
│   ├── content/
│   │   ├── services/*.md     ← 12 service page bodies (markdown)
│   │   └── areas/*.md        ← 14 area page bodies (markdown)
│   └── styles/global.css     ← Tailwind v4 theme tokens, typography, utilities
├── public/
│   ├── images/               ← shipped images (already used by the site)
│   ├── hero-video.mp4
│   ├── favicon.svg
│   ├── robots.txt
│   └── _redirects            ← Cloudflare Pages redirect rules
├── functions/api/contact.ts  ← Cloudflare Pages Function handling contact form
├── scripts/                  ← scrape-wp.mjs + content-porting Python helpers
├── _seo/                     ← migration plan, URL map, porting order, audit CSV, 2026 action plan
├── _media-source/            ← original designer PNG/WEBP source assets (42MB)
└── _wp-tools/                ← Python scripts + data for interacting with the LIVE WP/Bricks site
```

**`_` prefix** = not shipped, reference-only folders. Ignored by Astro (underscore prefix). Kept in repo for operator context.

---

## 4. Credentials & access (LOCAL-ONLY — do not commit)

These live on Daniel's machine outside the repo. Incoming operator needs to know where to find them locally:

| Resource | Location | Purpose |
|---|---|---|
| Memory files | `C:\Users\Willb\.claude\projects\C--Users-Willb-Claude-CFC\memory\` | User profile, project context, credentials references, feedback rules |
| GSC service account | `C:\Users\Willb\Claude\CFC\gsc-service-account.json` | **SECRET** — read-only GSC access. Scope: `webmasters.readonly`. Property: `sc-domain:customfabriccreations.net` |
| WP application password | memory file `cfc_wp_access.md` | User `daniel`, REST API base `https://www.customfabriccreations.net/wp-json/wp/v2/` |
| Bricks backups | `C:\Users\Willb\Claude\CFC\bricks_backup_*.json` | Historical Bricks snapshots (pre-phase fallbacks). Not committed — bulky, recoverable. |

**Never commit** `gsc-service-account.json` or any WP password to this repo.

**GSC sanity check:** `python _wp-tools/gsc_test.py` (or original at `C:\Users\Willb\Claude\CFC\gsc_test.py`). Always pass `siteUrl="sc-domain:customfabriccreations.net"` — URL-prefix form 403s.

---

## 5. What's been shipped (Astro rebuild)

Git log summary (newest first):

- `7049e6a` — Hero curve fix (home-only), wider richer sticky sidebar, about rebuild
- `aa654a1` — Homepage matches live section order + content audit pass
- `8822548` — Fix missing first-char bug (ustom→Custom), rebuild ServiceSidebar, stronger HeroBend
- `9acef78` — Major overhaul: new sections + real images + hero bend + logo everywhere
- `f0c32f9` — Fix critical bugs + ship real content: logo, video, escapes, full WP port
- `0900f85` — Ship full content port, design system, schema, media, and CF Function
- `cc55d5d` — Add SEO migration plan + per-page audit (seo-plan skill output)
- `18b88ec` — Initial scaffold: Astro 6 + Tailwind v4 + 1:1 URL structure

**Current in-flight change (this commit):** HeroBend curve direction flipped — was "concave dip down in middle," now "convex arc up in middle" to match the designer's comp. See `src/components/HeroBend.astro`.

---

## 6. What's been shipped (live WP site, 2026-04-22)

Separate workstream — these changes live on the WP+Bricks production site, not in this repo. See `_wp-tools/` for the Python scripts that made the edits via Bricks REST.

Snapshot of phases completed today (driven by `_wp-tools/phase1_update.py`, `phase2_content.py`, `phase3_content.py`, `schema_*`, `fix_*`, etc.):

- **Plantation Shutters page (post 524)** — full geo-swap Central FL → St. Pete, 10 FAQs (was 5), 4 new Phase-2 sections (Materials & Construction, Specialty Shapes, Authorized Dealer, In-House Workroom), schema graph (Service + FAQPage + LocalBusiness with correct geo), NAP block (H7), Rank Math title/meta/focus-kw set. Element delta: 217 → 249.
- **Area pages (14)** — cross-linked, E-E-A-T signals added, wrong phone/desc fixed
- **About page** — removed broken testimonials, rebuild
- **Homepage (post 103)** — E-E-A-T, crosslinks, mode fix
- **Sitewide NAP** — updated where discoverable; West St. Pete location schema live

Full details: [`_seo/2026-action-plan.md`](_seo/2026-action-plan.md), [`_wp-tools/phase1_audit.md`](_wp-tools/phase1_audit.md), [`_wp-tools/plantation_shutters_v2.md`](_wp-tools/plantation_shutters_v2.md).

---

## 7. Migration state (Astro port)

**Ranking-preservation risk:** LOW. GSC shows only 1 of 37 URLs gets any impressions and every top-ranking query is legacy Ocala. This is near-greenfield — migrate WITH improvements, don't port verbatim.

**URL structure:** 1:1 preserved. 38/38 routes match (see [`_seo/URL-MAP.md`](_seo/URL-MAP.md)).

### What's done

- ✅ Astro 6 scaffold, Tailwind v4, Node 22+ pinned
- ✅ All 37 URLs routed via `[slug].astro` dynamics
- ✅ Content ported into `src/content/services/*.md` and `src/content/areas/*.md`
- ✅ Design system: Montserrat + Playfair Display, luxury palette (`#bca050` gold, `#fcf7e3` cream, `#333333` charcoal)
- ✅ Global `LocalBusiness` schema with correct geo (27.7676, -82.6403) — fixes the Alabama-coordinate bug
- ✅ Contact form → Cloudflare Pages Function with Resend + webhook fallback
- ✅ Sitemap via `@astrojs/sitemap` (excludes `/thank-you/`)
- ✅ Sticky mobile CTA, hero video, logo treatments
- ✅ Homepage hero-bend curve (just flipped to correct direction)
- ✅ Build output: `dist/` is clean (16MB)

### What's still open

- ⏳ Cloudflare Pages deployment (repo isn't wired to CF yet — see README deployment section)
- ⏳ OG images per page (1200×630)
- ⏳ Gallery captions per installation (neighborhood + service type)
- ⏳ Brands page thickening (240w → 800+ per-brand sections)
- ⏳ Ocala residue still in source MD files — check each `_seo/PORTING-ORDER.md` P1 page for "Central Florida" / "Ocala" mentions and rewrite to St. Pete / Pinellas
- ⏳ DNS cutover: when Astro is approved, repoint `www` at CF Pages; keep WP reachable at a staging URL for 30-day rollback window
- ⏳ Schema coverage: verify every page type emits the correct JSON-LD (see table in `_seo/MIGRATION-PLAN.md` §Schema Plan)

---

## 8. Deployment

Cloudflare Pages, Astro preset.

| Setting | Value |
|---|---|
| Framework preset | Astro |
| Build command | `npm run build` |
| Build output directory | `dist` |
| Root directory | *(leave empty)* |
| Environment variables | `NODE_VERSION=22` |

**Contact form env vars** (set in CF Pages dashboard after repo is connected):
- `CONTACT_EMAIL_TO` — e.g. `info@customfabriccreations.net`
- `CONTACT_WEBHOOK_URL` — optional Slack/Zapier/Make
- `RESEND_API_KEY` — for Resend email delivery

Custom domain: `www.customfabriccreations.net` → Pages project. Keep WP reachable on a staging URL for 30 days post-cutover (rollback window).

---

## 9. Local dev

```bash
npm install
npm run dev       # http://localhost:4321
npm run build     # dist/
npm run preview   # preview local build
npm run scrape    # refresh scripts/scraped/ from live WP (gitignored)
```

Requires **Node ≥22.12**.

---

## 10. How to work on the LIVE WP site

All tooling for the WP workstream is in `_wp-tools/`. Python + `requests` + the WP REST API, authenticated with Daniel's application password (loaded from the memory file, not committed).

Common patterns already written:

- **Fetch a page's Bricks data:** `inspect_bricks.py`, `inspect_phase2.py`, `scout_524_*.py`
- **Patch a page's Bricks data:** `phase1_update.py`, `phase2_content.py`, `phase3_content.py`, `fix_*.py`
- **Schema injection:** `schema_injection.py`, `schema_v2.py`, `schema_final.py`, `schema_update_nap.py`
- **NAP + phone fixes:** `fix_all_wrong_phone_desc.py`, `fix_snell_phone.py`, `schema_update_nap.py`
- **Cross-linking:** `internal_links.py`, `link_new_pages_and_eeat.py`
- **GSC data pulls:** `gsc_test.py`, `gsc_perf_query.py`

**Safety habit:** every mutating script writes a timestamped backup (`bricks_backup_{POSTID}_{YYYYMMDD_HHMMSS}_pre_{phase}.json`) before patching. Locally there are ~40 of these at `C:\Users\Willb\Claude\CFC\` — not committed (bulky and recoverable). If you run a new mutation, follow the same pattern.

**Bricks REST endpoint:** CFC has a custom endpoint at `cfc-bricks-rest.php` (copy in `_wp-tools/`) that exposes Bricks page data via the REST API. Rank Math helper snippet also in `_wp-tools/rank_math_snippet.php`.

---

## 11. Design / brand tokens

Source of truth: [`src/styles/global.css`](src/styles/global.css) + [`src/lib/site.ts`](src/lib/site.ts).

- **Gold:** `#bca050` (primary CTA, accents, hero stroke)
- **Cream:** `#fcf7e3`
- **Charcoal:** `#333333`
- **Display font:** Playfair Display
- **Body font:** Montserrat Variable
- **Hero curve:** convex arc, middle rises into the dark hero (see `src/components/HeroBend.astro`). Original live-WP designer comps are in `_media-source/Website Layouts/Homepage/`.

---

## 12. Where to find things fast

| Looking for… | Look in… |
|---|---|
| Nav menu / services list / areas list | `src/lib/site.ts` |
| A service page's body copy | `src/content/services/{slug}.md` |
| An area page's body copy | `src/content/areas/{slug}.md` |
| Per-page schema strategy | `_seo/MIGRATION-PLAN.md` §Schema Plan |
| Which pages still need rewrite work | `_seo/PORTING-ORDER.md` |
| Current live WP state (Bricks JSON snapshot) | `_wp-tools/bricks_live.json` |
| SERP + keyword research | `_wp-tools/keyword_data.json`, `_wp-tools/seeds.json` |
| FAQs extracted from live | `_wp-tools/faqs_extracted.json` |
| Designer source PNGs / WEBPs | `_media-source/` |
| Cloudflare Function for contact form | `functions/api/contact.ts` |

---

## 13. Open threads / next suggested moves

Priority stack if you inherit cold:

1. **Finalize CF Pages deployment** — wire the repo to CF Pages, set env vars, get a preview URL in front of Daniel
2. **Ocala rewrite sweep** — grep `src/content/` for "Ocala", "Marion", "Central Florida"; rewrite each to St. Pete / Pinellas County. See `_seo/PORTING-ORDER.md` P1.
3. **Schema audit** — walk every page type, confirm the correct JSON-LD emits (no Article on non-articles, correct `LocalBusiness` geo everywhere)
4. **Brands page expansion** — from 240w to 800+ with a section per brand
5. **Gallery captions** — pair each gallery image with neighborhood + service type
6. **OG image generation** — 1200×630 per page type (use the brand gold + a hero image background)
7. **Post-cutover:** monitor GSC coverage daily for 14 days; Astro replaces WP on DNS cutover.

**Live-WP side (parallel workstream):**
- West St. Pete and main-office NAP consistency — phone conflict (727 vs 352) still open until main office is locked
- Keep monitoring the plantation-shutters page rank for the primary KWs (`plantation shutters st petersburg fl`, `plantation shutters near me`). See `_seo/2026-action-plan.md` for the full 2026 roadmap.

---

## 14. Contact

- GitHub: `covenantOS/cfc-astro`
- Operator: Daniel (SEO lead, CFC)
- Live site: https://www.customfabriccreations.net
- Target market: St. Petersburg, FL + Pinellas County

Good luck. Everything else is in the code.
