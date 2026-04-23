# CFC Astro — Project Handoff

**Last updated:** 2026-04-22
**Outgoing operator:** Claude (Opus 4.7)
**Incoming operator:** Open Claw

Pickup doc for the Custom Fabric Creations (CFC) Astro rebuild. **This is a 1:1 port of the live WP site** — don't invent work, read the code to see current state.

> ⚠️ **Don't trust the "open threads" list** of a prior handoff over what the code actually shows. If you think something is unfinished, grep first. Example: Ocala/Central-FL rewrites are already done.

---

## 1. What this project is

CFC is **Custom Fabric Creations** — a custom window treatments + upholstery studio in St. Petersburg, FL. Two workstreams:

1. **Live WordPress site** — `https://www.customfabriccreations.net` on WP + Bricks Builder. Ongoing on-page SEO via Python scripts in `_wp-tools/`.
2. **Astro rebuild** (this repo) — **1:1 port** of the WP site onto Astro 6 + Tailwind v4, destined for Cloudflare Pages. Match what's live; don't redesign.

**Single source of truth for facts:** [`src/lib/site.ts`](src/lib/site.ts) — SITE constants, NAV, 12 SERVICES, 14 AREAS, 5 BRANDS. Pull from there, don't duplicate here.

Known live-WP facts (match these when building):
- Main phone: **(727) 240-4512** (sitewide footer)
- West St. Pete NAP: **3026 Central Ave Suite 551, St. Petersburg FL 33712 / (352) 266-1262**
- Schema geo: **27.7676, -82.6403**

---

## 2. Working style

- Operator wants fast, practical execution — less theory, more "here's what I'm doing next"
- Comfortable with SEO concepts — don't over-explain fundamentals
- Lead with what you're pushing now, not what you'd need a human to do manually
- Gets blunt when you're wrong or inventing work — take the feedback, fix, don't re-litigate
- **1:1 rebuild means 1:1.** Don't add "suggested improvements" unless asked.

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

These live on the operator's machine outside the repo:

| Resource | Location | Purpose |
|---|---|---|
| Memory files | `C:\Users\Willb\.claude\projects\C--Users-Willb-Claude-CFC\memory\` | Project context, credentials references, feedback rules |
| GSC service account | `C:\Users\Willb\Claude\CFC\gsc-service-account.json` | **SECRET** — read-only GSC access. Scope: `webmasters.readonly`. Property: `sc-domain:customfabriccreations.net` |
| WP application password | memory file `cfc_wp_access.md` | WP user `daniel`, REST API base `https://www.customfabriccreations.net/wp-json/wp/v2/` |
| Bricks backups | `C:\Users\Willb\Claude\CFC\bricks_backup_*.json` | Historical Bricks snapshots. Not committed — bulky, recoverable. |

**Never commit** `gsc-service-account.json` or any WP password to this repo.

**GSC sanity check:** `python _wp-tools/gsc_test.py` (or original at `C:\Users\Willb\Claude\CFC\gsc_test.py`). Always pass `siteUrl="sc-domain:customfabriccreations.net"` — URL-prefix form 403s.

---

## 5. Commit history

Run `git log --oneline -20` for current state. Don't trust a frozen list here.

**Last change before handoff:** HeroBend curve flipped to convex (middle arcs up into dark hero). See [`src/components/HeroBend.astro`](src/components/HeroBend.astro).

---

## 6. Live WP workstream (separate)

Parallel — not part of this Astro repo. Python scripts in `_wp-tools/` hit the live WP + Bricks REST endpoint. See [`_wp-tools/README.md`](_wp-tools/README.md) for categorized index (inspection vs. mutation vs. GSC/keyword data). Planning docs live at [`_wp-tools/phase1_audit.md`](_wp-tools/phase1_audit.md), [`_wp-tools/plantation_shutters_v2.md`](_wp-tools/plantation_shutters_v2.md), [`_seo/2026-action-plan.md`](_seo/2026-action-plan.md).

Ask the operator what the current state of the WP workstream is — don't assume from doc dates.

---

## 7. Migration state (Astro port)

**Rebuild is 1:1 with live WP.** Match the existing site; improvements only when asked.

**URL structure:** 1:1 preserved. See [`_seo/URL-MAP.md`](_seo/URL-MAP.md).

**Known in the box:**
- Astro 6.1.8 + Tailwind v4.2.2, Node ≥22.12
- All URLs routed via `[slug].astro` dynamics against `src/lib/site.ts`
- Content in `src/content/services/*.md` and `src/content/areas/*.md`
- Global `LocalBusiness` schema with geo `27.7676, -82.6403`
- Contact form → Cloudflare Pages Function (`functions/api/contact.ts`) with Resend + webhook fallback
- Sitemap via `@astrojs/sitemap` (excludes `/thank-you/`)
- `npm run build` produces a clean `dist/`

**What's actually done vs. not:** check the code and ask the operator. Don't take a bullet list's word for it.

> ⚠️ `_media-source/` holds the **designer's original comps/assets**. The current live WP site doesn't necessarily match these pixel-for-pixel — they're reference material, not ground truth. If the Astro port needs to match the LIVE site, scrape the live site (see `scripts/scrape-wp.mjs`) or ask.

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

Custom domain: `www.customfabriccreations.net`. DNS cutover is coordinated with the operator — don't assume timing.

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

All tooling for the WP workstream is in `_wp-tools/`. Python + `requests` + the WP REST API, authenticated with the operator's application password (loaded from the memory file `cfc_wp_access.md` via `$env:CFC_WP_APP_PASS`, not committed).

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

## 13. Starting work

**Don't trust a stale priority list.** Ask the operator what the current focus is. If pushed to infer:

1. `git log --oneline -10` to see last changes
2. `npm run build && npm run preview` to see current state of the port
3. Compare against `https://www.customfabriccreations.net` — this is a 1:1 rebuild, so deltas = work
4. Ask

Don't fabricate "open threads" (Ocala rewrite, schema audit, brand expansion, etc.) unless the code actually shows them open.

---

## 14. Contact

- GitHub: `covenantOS/cfc-astro`
- Live site: https://www.customfabriccreations.net
- Target market: St. Petersburg, FL + Pinellas County

Everything else is in the code.
