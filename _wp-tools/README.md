# `_wp-tools/` — Live WordPress tooling

These scripts + data files are for working with the **live WP + Bricks Builder** site at `customfabriccreations.net`, not the Astro rebuild. They're kept here so the incoming operator has everything needed to continue on-page SEO work on the live site while the Astro cutover is prepared.

## Requirements

- Python 3.10+ with `requests`, `google-api-python-client`, `google-auth`
- WP application password exported as `CFC_WP_APP_PASS` env var (the value lives in local memory file `cfc_wp_access.md` — user `daniel`). Scripts read `os.environ.get("CFC_WP_APP_PASS", "")` — never commit the value.
- GSC service account at `C:\Users\Willb\Claude\CFC\gsc-service-account.json` (local-only, not in repo)

```bash
# Before running any _wp-tools script — pull the value from the local memory file cfc_wp_access.md, then:

# PowerShell
$env:CFC_WP_APP_PASS = "<paste application password here>"

# bash
export CFC_WP_APP_PASS="<paste application password here>"
```

**REST API base:** `https://www.customfabriccreations.net/wp-json/wp/v2/`
**Custom Bricks endpoint:** provided by `cfc-bricks-rest.php` (copy here for reference)

## Categories

### Inspection (read-only)
- `inspect_bricks.py`, `inspect_phase2.py`, `inspect_faq_and_central.py`
- `inspect_524_*.py` — plantation shutters page (post 524)
- `inspect_1390_duplicate_h1.py`, `inspect_testimonial_cards.py`, `inspect_about_testimonials.py`
- `find_duplicate_h1_page.py`, `investigate_h*.py`
- `audit_pages.py`, `audit_all_areas.py`
- `scout_524_*.py`

### Mutation (writes to live site — always backs up first)
- `phase1_update.py`, `phase1b_cleanup.py`, `phase2_content.py`, `phase3_content.py` — staged content rollout
- `fix_524_*.py` — plantation shutters page fixes (NAP, schema, H7/H8/H9/H10, em-dashes, FAQ fixes)
- `fix_*_phone*.py` — sitewide phone/NAP corrections
- `fix_about_remove_reviews.py`, `fix_homepage_bricks_mode.py`
- `fix_1383_thankyou_h1.py`, `fix_1390_duplicate_h1.py` — H1 hygiene
- `fix_and_schema_areas.py` — area pages
- `link_new_pages_and_eeat.py`, `internal_links.py` — interlinking
- `schema_injection.py`, `schema_v2.py`, `schema_v3_test.py`, `schema_final.py`, `schema_update_nap.py`
- `sweep_duplicate_h1.py`, `verify_h1_sweep_final.py`, `verify_h8_h9_and_scout_h10.py`

### GSC + keyword data
- `gsc_test.py` — sanity check service account access
- `gsc_perf_query.py` — pull GSC performance data
- `build_seeds.py` — generate keyword seed list
- `rank_keywords.py`

### Data files
- `bricks_live.json` — snapshot of live Bricks data (as of 2026-04-22). Useful reference for what lives where.
- `bricks_raw.json` — raw Bricks export
- `keyword_data.json`, `seeds.json` — keyword research output
- `faqs_extracted.json` — FAQs pulled from live pages
- `plantation_shutters_v2.md` — content plan for the flagship service page
- `phase1_audit.md` — initial audit findings

### PHP helpers (install in WP)
- `cfc-bricks-rest.php` — custom REST endpoint exposing Bricks page data. Drop into the child theme or a must-use plugin.
- `rank_math_snippet.php` — Rank Math programmatic title/meta/focus-kw setter. Needed for the `phase1_update.py` flow.

## Safety conventions

- **Always back up before mutating:** every mutating script writes `bricks_backup_{POSTID}_{YYYYMMDD_HHMMSS}_pre_{phase}.json` to the CFC root before patching. Follow this convention for any new script.
- **Read-then-write:** fetch the full Bricks payload, patch in memory, PUT the full payload back — don't try partial updates.
- **Element IDs:** Bricks generates element IDs on creation; preserve them on patches or you'll break saved layouts.
