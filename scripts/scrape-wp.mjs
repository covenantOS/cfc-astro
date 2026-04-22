#!/usr/bin/env node
// Scrape the current WordPress site for content porting reference.
// Output: scripts/scraped/{html,json,images.txt}
// This is a one-shot reference tool — run manually when you need to pull
// down the live content for a page you're about to port into Astro.

import { mkdir, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const OUT_DIR = join(__dirname, 'scraped');
const BASE = 'https://www.customfabriccreations.net';

const URLS = [
  '/', '/about/', '/brands/', '/contact/', '/gallery/',
  '/services/',
  '/services/custom-draperies-curtains/',
  '/services/plantation-shutters/',
  '/services/window-shades/',
  '/services/custom-blinds/',
  '/services/custom-cornices-valances/',
  '/services/drapery-hardware/',
  '/services/outdoor-window-shades/',
  '/services/furniture-reupholstery/',
  '/services/custom-bedding-pillows/',
  '/services/custom-banquettes/',
  '/services/commercial-window-treatments/',
  '/services/services-interior-decor-tampa/',
  '/areas/',
  '/areas/st-petersburg/',
  '/areas/downtown-st-pete/',
  '/areas/old-northeast/',
  '/areas/snell-isle/',
  '/areas/shore-acres/',
  '/areas/west-st-pete/',
  '/areas/tierra-verde/',
  '/areas/st-pete-beach/',
  '/areas/treasure-island/',
  '/areas/clearwater/',
  '/areas/sand-key/',
  '/areas/belleair-shore/',
  '/areas/seminole/',
  '/areas/largo/',
  '/plantation-shutters-cost-st-petersburg/',
  '/plantation-shutters-installation-st-petersburg/',
  '/plantation-shutters-regret-downsides/',
];

const pathToSlug = (p) => (p === '/' ? 'home' : p.replace(/^\/|\/$/g, '').replace(/\//g, '--'));

async function scrape() {
  await mkdir(join(OUT_DIR, 'html'), { recursive: true });
  const imageSet = new Set();
  const pages = [];

  for (const path of URLS) {
    const url = BASE + path;
    process.stdout.write(`  ${path} ... `);
    try {
      const res = await fetch(url, { headers: { 'User-Agent': 'cfc-astro-scraper/1.0' } });
      if (!res.ok) { console.log(`HTTP ${res.status}`); continue; }
      const html = await res.text();
      const slug = pathToSlug(path);
      await writeFile(join(OUT_DIR, 'html', `${slug}.html`), html);

      const titleMatch = html.match(/<title>([^<]+)<\/title>/);
      const descMatch = html.match(/<meta\s+name="description"\s+content="([^"]+)"/i);
      const ogImgMatch = html.match(/<meta\s+property="og:image"\s+content="([^"]+)"/i);

      const imgUrls = [...html.matchAll(/https:\/\/www\.customfabriccreations\.net\/wp-content\/uploads\/[^"' )]+?\.(?:jpe?g|png|webp|svg|gif|avif)/gi)].map((m) => m[0]);
      imgUrls.forEach((u) => imageSet.add(u));

      pages.push({
        path,
        title: titleMatch?.[1]?.trim(),
        description: descMatch?.[1]?.trim(),
        ogImage: ogImgMatch?.[1]?.trim(),
        imageCount: imgUrls.length,
      });
      console.log(`ok (${imgUrls.length} images)`);
    } catch (err) {
      console.log(`err: ${err.message}`);
    }
  }

  await writeFile(join(OUT_DIR, 'pages.json'), JSON.stringify(pages, null, 2));
  await writeFile(join(OUT_DIR, 'images.txt'), [...imageSet].sort().join('\n'));
  console.log(`\nDone. ${pages.length} pages, ${imageSet.size} unique images.`);
  console.log(`Output: ${OUT_DIR}`);
}

scrape();
