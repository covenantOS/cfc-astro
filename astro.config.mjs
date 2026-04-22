// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';
import partytown from '@astrojs/partytown';

export default defineConfig({
  site: 'https://www.customfabriccreations.net',
  integrations: [
    sitemap({
      filter: (page) =>
        !page.includes('/thank-you/') &&
        !page.endsWith('/rss.xml'),
    }),
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
