# URL Map — WordPress to Astro

**Policy:** 1:1 preservation. Zero URL changes at cutover.

**Reason:** With near-zero existing rankings, no URL changes are *needed* to protect traffic. But changing slugs while also changing CMS + hosting is two variables at once \u2014 hard to diagnose if something goes sideways. Preserve URLs now, iterate later.

## Confirmed mapping (all 37)

| # | Current URL | Astro file | Status |
|---|---|---|---|
| 1 | `/` | `src/pages/index.astro` | \u2705 1:1 |
| 2 | `/about/` | `src/pages/about.astro` | \u2705 1:1 |
| 3 | `/brands/` | `src/pages/brands.astro` | \u2705 1:1 |
| 4 | `/contact/` | `src/pages/contact.astro` | \u2705 1:1 |
| 5 | `/gallery/` | `src/pages/gallery.astro` | \u2705 1:1 |
| 6 | `/thank-you/` | `src/pages/thank-you.astro` | \u2705 1:1 |
| 7 | `/services/` | `src/pages/services/index.astro` | \u2705 1:1 |
| 8 | `/services/custom-draperies-curtains/` | `src/pages/services/[slug].astro` | \u2705 via getStaticPaths |
| 9 | `/services/plantation-shutters/` | `src/pages/services/[slug].astro` | \u2705 |
| 10 | `/services/window-shades/` | `src/pages/services/[slug].astro` | \u2705 |
| 11 | `/services/custom-blinds/` | `src/pages/services/[slug].astro` | \u2705 |
| 12 | `/services/custom-cornices-valances/` | `src/pages/services/[slug].astro` | \u2705 |
| 13 | `/services/drapery-hardware/` | `src/pages/services/[slug].astro` | \u2705 |
| 14 | `/services/outdoor-window-shades/` | `src/pages/services/[slug].astro` | \u2705 |
| 15 | `/services/furniture-reupholstery/` | `src/pages/services/[slug].astro` | \u2705 |
| 16 | `/services/custom-bedding-pillows/` | `src/pages/services/[slug].astro` | \u2705 |
| 17 | `/services/custom-banquettes/` | `src/pages/services/[slug].astro` | \u2705 |
| 18 | `/services/commercial-window-treatments/` | `src/pages/services/[slug].astro` | \u2705 |
| 19 | `/services/services-interior-decor-tampa/` | `src/pages/services/[slug].astro` | \u2705 legacy slug preserved |
| 20 | `/areas/` | `src/pages/areas/index.astro` | \u2705 1:1 |
| 21 | `/areas/st-petersburg/` | `src/pages/areas/[slug].astro` | \u2705 |
| 22 | `/areas/downtown-st-pete/` | `src/pages/areas/[slug].astro` | \u2705 |
| 23 | `/areas/old-northeast/` | `src/pages/areas/[slug].astro` | \u2705 |
| 24 | `/areas/snell-isle/` | `src/pages/areas/[slug].astro` | \u2705 |
| 25 | `/areas/shore-acres/` | `src/pages/areas/[slug].astro` | \u2705 |
| 26 | `/areas/west-st-pete/` | `src/pages/areas/[slug].astro` | \u2705 |
| 27 | `/areas/tierra-verde/` | `src/pages/areas/[slug].astro` | \u2705 |
| 28 | `/areas/st-pete-beach/` | `src/pages/areas/[slug].astro` | \u2705 |
| 29 | `/areas/treasure-island/` | `src/pages/areas/[slug].astro` | \u2705 |
| 30 | `/areas/clearwater/` | `src/pages/areas/[slug].astro` | \u2705 |
| 31 | `/areas/sand-key/` | `src/pages/areas/[slug].astro` | \u2705 |
| 32 | `/areas/belleair-shore/` | `src/pages/areas/[slug].astro` | \u2705 |
| 33 | `/areas/seminole/` | `src/pages/areas/[slug].astro` | \u2705 |
| 34 | `/areas/largo/` | `src/pages/areas/[slug].astro` | \u2705 |
| 35 | `/plantation-shutters-cost-st-petersburg/` | `src/pages/plantation-shutters-cost-st-petersburg.astro` | \u2705 1:1 |
| 36 | `/plantation-shutters-installation-st-petersburg/` | `src/pages/plantation-shutters-installation-st-petersburg.astro` | \u2705 1:1 |
| 37 | `/plantation-shutters-regret-downsides/` | `src/pages/plantation-shutters-regret-downsides.astro` | \u2705 1:1 |
| 38 | 404 | `src/pages/404.astro` | \u2705 |

**Result:** 38/38 routes match. No redirects needed at cutover.

## Future URL changes (NOT for initial cutover)

If we later consolidate, redirect in Cloudflare Pages via `public/_redirects`:

### Legacy slug candidates (defer to v2)

- `/services/services-interior-decor-tampa/` \u2192 `/services/interior-decor-consultation/` (slug says Tampa but company is in St. Pete; fix in v2 after establishing rankings on the current slug)

### Hypothetical consolidations

- None recommended right now. Keep every URL and let them accrue signals individually.

## Redirect file (for cutover safety)

Create `public/_redirects` with blanket trailing-slash behavior to match WP:

```
# Normalize trailing slashes to match legacy WordPress URLs
/about        /about/    301
/brands       /brands/   301
/contact      /contact/  301
/gallery      /gallery/  301
/services     /services/ 301
/areas        /areas/    301
# (Astro 6 auto-generates trailing-slash URLs by default, so this is defensive only)
```

Note: Astro's default `trailingSlash: "ignore"` with `build.format: "directory"` (the default) will generate `/about/index.html`, so both `/about` and `/about/` resolve. The `_redirects` file is a belt-and-suspenders measure.

## External backlinks to watch

Run `gh api` / backlink tool post-cutover to check that:
- Any existing backlinks still resolve (they will \u2014 URLs are 1:1)
- GBP website URL points to the new property
- Yelp/directory listings point to the new site
- Social profile links are updated

Audit backlinks via `seo-backlinks` skill once DNS cuts over.
