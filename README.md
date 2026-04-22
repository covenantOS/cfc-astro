# Custom Fabric Creations — Astro Rebuild

A 1:1 rebuild of [customfabriccreations.net](https://www.customfabriccreations.net) on Astro + Tailwind v4, with a refined luxury design direction.

## Stack

- **Astro 6** (static output)
- **Tailwind CSS v4** via `@tailwindcss/vite`
- **Self-hosted fonts**: Montserrat (body) + Playfair Display (display)
- **@astrojs/sitemap** for `sitemap-index.xml`
- **@astrojs/partytown** for third-party scripts (GA/GTM)
- **sharp** for Astro image optimization

## Project structure

```
src/
  components/    # Header, Footer, Hero, ServiceGrid, AreaGrid, FinalCTA, etc.
  layouts/       # BaseLayout, ServiceLayout, AreaLayout
  lib/           # site.ts — nav, services, areas, brands, contact info
  pages/         # .astro pages, URL-1:1 with live site
    services/    # [slug].astro generates all 12 service pages
    areas/       # [slug].astro generates all 14 area pages
  styles/        # global.css — theme tokens, typography, utilities
public/          # static assets: robots.txt, favicon, /images
scripts/
  scrape-wp.mjs  # pulls live HTML for porting reference
```

## URL map (1:1 with live WP site)

- `/` — home
- `/about/` `/brands/` `/contact/` `/gallery/` `/thank-you/`
- `/services/` + 12 service pages under `/services/{slug}/`
- `/areas/` + 14 area pages under `/areas/{slug}/`
- 3 plantation-shutters root guides

## Local dev

```bash
npm install
npm run dev       # http://localhost:4321
npm run build     # builds to ./dist
npm run preview   # preview build locally
```

Requires Node ≥22.12.

## Scraping live content

To pull the current live HTML for porting reference:

```bash
npm run scrape
```

Output lands in `scripts/scraped/` (gitignored).

## Cloudflare Pages deployment

Connect this repo in Cloudflare Pages with:

| Setting | Value |
|---|---|
| Framework preset | **Astro** |
| Build command | `npm run build` |
| Build output directory | `dist` |
| Root directory | *(leave empty)* |
| Environment variables | `NODE_VERSION` = `22` |

Custom domain: point `www.customfabriccreations.net` at the Pages project.

## Porting content from WordPress

The live site uses Bricks Builder. Content is server-rendered so it\u2019s scrapable:

1. Run `npm run scrape` to snapshot all pages into `scripts/scraped/html/`.
2. Open the corresponding HTML file for the page you\u2019re porting.
3. Copy body copy, headings, image references into the Astro page.
4. Drop images into `public/images/` and reference them from `src/`.

Original CFC brand tokens (from `automatic.css`):
- Primary gold `#bca050`
- Cream `#fcf7e3`
- Charcoal `#333333`

Mapped into Tailwind v4 theme tokens in `src/styles/global.css`.
