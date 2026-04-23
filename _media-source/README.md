# `_media-source/` — Original designer assets

Reference-only PNG/WEBP source assets from the website designer. Shipped site images already live in [`/public/images/`](../public/images/) at their production file names. This folder is preserved so the incoming operator can:

- Regenerate production images at different sizes, crops, or formats
- Reference the original section layout comps when rebuilding/redesigning
- Diff against the current Astro render to spot design drift

## Folders

- **`Website Layouts/`** — full-section composition mockups (PNG)
  - `Homepage/` — hero, services grid, areas, brand strip, FAQ, CTA, footer, mobile variants
  - Service/Area page templates (hero, column+content, global contact section, mobile)
  - Component closeups (info/feature cards, meet-the-owner, why-choose-us, Google review widget)

- **`Website Media/`** — individual production-ready WEBP images
  - Service hero + content images (one folder per service)
  - Area thumbnails (one WEBP per area)
  - Gallery photos (9 curated installations)
  - Brand logos, St. Petersburg map

## Naming

Originals use prose names ("Plantation Shutters Background Hero Image.webp"). The Astro port normalizes these into `/public/images/services/{slug}/hero.webp`, `.../top.webp`, `.../middle.webp`, `.../bottom.webp` etc. If you add new images, follow the normalized pattern — not the prose originals.
