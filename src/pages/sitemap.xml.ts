// Flat sitemap endpoint — emits every indexable URL as a single <urlset>.
// Replaces @astrojs/sitemap so crawlers don't have to follow an index file.
// The URL list is derived from site.ts (SERVICES, AREAS) plus the static page
// list below; if you add a new indexable page, add it here too.

import type { APIRoute } from 'astro';
import { SITE, SERVICES, AREAS } from '~/lib/site';

const today = new Date().toISOString().slice(0, 10);

type Entry = { path: string; changefreq: 'daily' | 'weekly' | 'monthly' | 'yearly'; priority: string };

const staticPages: Entry[] = [
  { path: '/',            changefreq: 'weekly',  priority: '1.0' },
  { path: '/about/',      changefreq: 'monthly', priority: '0.8' },
  { path: '/services/',   changefreq: 'weekly',  priority: '0.9' },
  { path: '/areas/',      changefreq: 'weekly',  priority: '0.9' },
  { path: '/brands/',     changefreq: 'monthly', priority: '0.7' },
  { path: '/gallery/',    changefreq: 'monthly', priority: '0.7' },
  { path: '/reviews/',    changefreq: 'weekly',  priority: '0.9' },
  { path: '/contact/',    changefreq: 'monthly', priority: '0.8' },
  // Near-me landing pages (low-KD, high-volume targets)
  { path: '/plantation-shutters-near-me/', changefreq: 'weekly',  priority: '0.9' },
  { path: '/drapery-near-me/',             changefreq: 'weekly',  priority: '0.9' },
  // Plantation-shutters guide cluster
  { path: '/plantation-shutters-cost-st-petersburg/',         changefreq: 'monthly', priority: '0.7' },
  { path: '/plantation-shutters-installation-st-petersburg/', changefreq: 'monthly', priority: '0.7' },
  { path: '/plantation-shutters-regret-downsides/',           changefreq: 'monthly', priority: '0.7' },
];

const serviceEntries: Entry[] = SERVICES.map((s) => ({
  path: `/services/${s.slug}/`,
  changefreq: 'monthly',
  priority: '0.8',
}));

const areaEntries: Entry[] = AREAS.map((a) => ({
  path: `/areas/${a.slug}/`,
  changefreq: 'monthly',
  priority: '0.8',
}));

const entries: Entry[] = [...staticPages, ...serviceEntries, ...areaEntries];

export const GET: APIRoute = () => {
  const urls = entries
    .map(
      (e) => `  <url>
    <loc>${SITE.url}${e.path}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>${e.changefreq}</changefreq>
    <priority>${e.priority}</priority>
  </url>`,
    )
    .join('\n');

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls}
</urlset>
`;

  return new Response(xml, {
    status: 200,
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
