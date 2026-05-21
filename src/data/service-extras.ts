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

  'window-shades': {
    tip: {
      body: 'The shade you choose mostly depends on what the room is for. Bedrooms and media rooms need blackout, no shortcuts. Living and dining rooms usually want a Roman shade in fabric, something warm. Any west-facing window in St. Pete benefits from a solar shade that cuts the heat without losing the view. When in doubt, we layer two.',
    },
    featureList: {
      items: [
        { label: 'Solar shades', body: 'Reduce solar heat gain on west-facing windows and lanais while keeping the view through the fabric.' },
        { label: 'Cellular (honeycomb) shades', body: 'Trap air to insulate hot or cold windows, useful in bedrooms and on glass facing the Gulf.' },
        { label: 'Roman shades', body: 'Fabric folds with no chain mechanism, hand-stitched in our workroom, made to match drapery or upholstery.' },
        { label: 'Motorized shades', body: 'Somfy-powered systems for high windows, sliders, and Nana doors, with quiet operation and battery or wired options.' },
      ],
      columns: 2,
    },
    relatedLink: {
      body: 'Looking at shades for an oversized slider or a lanai? Our outdoor window shades page covers the wind-rated exterior options we install for screened patios and pool cages.',
      href: '/services/outdoor-window-shades/',
      linkText: 'See outdoor window shades',
    },
    reviewTag: 'window-shades',
    reviewLabel: 'What St. Pete homeowners say',
    closingBanner: {
      statement: 'Solar, cellular, Roman, and motorized shades, all measured, fabricated, and installed by the same St. Pete team since 2000.',
    },
  },

  // plantation-shutters is now an .mdx file with components interleaved
  // inline throughout the article, so it is intentionally NOT configured
  // here. Adding it back would double-render the components.
};

export function getServiceExtras(slug: string): ServiceExtras | undefined {
  return SERVICE_EXTRAS[slug];
}
