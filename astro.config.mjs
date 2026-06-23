// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import mdx from '@astrojs/mdx';

// Canonical production host. www is canonical (per GSC: 100% of search traffic
// historically lives at www). Apex 301-redirects to www at the Cloudflare edge.
// Used for canonical URLs, og:url, schema URLs, and the flat /sitemap.xml endpoint.
export default defineConfig({
  site: 'https://www.customfabriccreations.net',
  integrations: [
    mdx(),
  ],
  vite: {
    plugins: [tailwindcss()],
  },
  image: {
    responsiveStyles: true,
  },
  build: {
    inlineStylesheets: 'always',
  },
});
