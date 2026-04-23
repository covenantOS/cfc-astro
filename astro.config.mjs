// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import partytown from '@astrojs/partytown';

// Active deploy host. Swap to https://www.customfabriccreations.net at DNS cutover.
// Used for canonical URLs, og:url, schema URLs, and the flat /sitemap.xml endpoint.
export default defineConfig({
  site: 'https://cfc-astro.pages.dev',
  integrations: [
    partytown({ config: { forward: ['dataLayer.push', 'gtag'] } }),
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
