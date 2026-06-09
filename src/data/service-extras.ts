// Per-service configuration for the content components.
//
// Components, in render order on the service page:
//   1. OwnerTip         (Terry-signed warm-voice tip)
//   2. FeatureList      (2-column bold:description bullets)
//   3. <markdown body>
//   4. RelatedLink      (dashed-border cross-link callout)
//   5. InlineReview     (contextual Google review by tag)
//   6. ByNumbersBanner  (brown one-liner closing statement)
//
// Only services with an entry render the components; everything else
// renders the markdown unchanged. Rolling out one service at a time so
// Daniel can react to the format before broad rollout.
//
// Voice rules for `tip.body`: see project-cfc-voice-sheet memory. Warm,
// plainspoken, customer-agency framing, no em dashes, no marketing verbs.
//
// The multi-stat StatsBand grid was removed 2026-05-21 (Daniel did not
// like the look). Verified external stats (e.g. DOE figures) now live in
// the markdown body with an inline citation; internal headline numbers
// live in the ByNumbersBanner one-liner.

import type { ReviewTag } from './reviews';

export interface ServiceTip {
  body: string;
  eyebrow?: string;
  name?: string;
  role?: string;
  portrait?: string;
}

export interface ServiceFeatureItem {
  label: string;
  body: string;
}

export interface ServiceFeatureList {
  items: ServiceFeatureItem[];
  columns?: 1 | 2 | 3;
}

export interface ServiceRelatedLink {
  body: string;
  href: string;
  linkText: string;
}

export interface ServiceClosingBanner {
  eyebrow?: string;
  statement: string;
}

export interface ServiceExtras {
  tip?: ServiceTip;
  featureList?: ServiceFeatureList;
  relatedLink?: ServiceRelatedLink;
  reviewTag?: ReviewTag;
  reviewLabel?: string;
  closingBanner?: ServiceClosingBanner;
}

export const SERVICE_EXTRAS: Record<string, ServiceExtras> = {

  'custom-draperies-curtains': {
    tip: {
      // Tip B: locked by Daniel as the voice anchor on 2026-05-20.
      body: 'Before I bring out the fabric library, I always ask clients to show me one thing in the room they already love. A pillow, a rug, a piece of art. We build the drape from that, not the other way around. It is a small step, but it is the difference between drapes that feel like part of the room and drapes that just hang in the window.',
    },
    featureList: {
      items: [
        { label: 'Florida-rated fabrics', body: 'UV-resistant weaves for west-facing rooms, mildew-resistant linings for screened porches, blackout for bedrooms.' },
        { label: 'Custom lengths and stack-back', body: 'Built to your floor-to-rod measurement and your window framing, not a catalog standard.' },
        { label: 'Hardware that fits the home', body: 'Concealed tracks, decorative rods, and finials matched to your architecture from Craftsman bungalow to modern condo.' },
        { label: 'Layered with hard treatments', body: 'Drapery installed over shutters or shades when the room calls for both warmth and light control.' },
      ],
      columns: 2,
    },
    relatedLink: {
      body: 'If your room needs both softness and precise light control, drapery over plantation shutters is the layered look we build most. Our plantation shutters page walks through how the two combine.',
      href: '/services/plantation-shutters/',
      linkText: 'See plantation shutters',
    },
    reviewTag: 'custom-draperies-curtains',
    reviewLabel: 'What St. Pete homeowners say',
    closingBanner: {
      statement: 'Custom drapery built in our own St. Pete workroom. UV-rated fabrics. Hardware matched to the home. Hung by the installer who measured it.',
    },
  },

  // window-shades is now an .mdx file with components interleaved inline
  // throughout the article (same pattern as plantation-shutters), so it is
  // intentionally NOT configured here. Adding it back would double-render.

  // plantation-shutters is now an .mdx file with components interleaved
  // inline throughout the article, so it is intentionally NOT configured
  // here. Adding it back would double-render the components.
};

export function getServiceExtras(slug: string): ServiceExtras | undefined {
  return SERVICE_EXTRAS[slug];
}
