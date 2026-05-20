// Per-service configuration for the content components.
//
// Components, in render order on the service page:
//   1. StatsBand        (multi-stat grid with verified sources)
//   2. OwnerTip         (Terry-signed warm-voice tip)
//   3. FeatureList      (2-column bold:description bullets)
//   4. <markdown body>
//   5. RelatedLink      (dashed-border cross-link callout)
//   6. InlineReview     (contextual Google review by tag)
//   7. ByNumbersBanner  (dark one-liner closing statement)
//
// Only services with an entry render the components; everything else
// renders the markdown unchanged. Rolling out one service at a time so
// Daniel can react to the format before broad rollout.
//
// Voice rules for `tip.body`: see project-cfc-voice-sheet memory. Warm,
// plainspoken, customer-agency framing, no em dashes, no marketing verbs.
//
// Source rules for `stats[i]`: external claims must include `sourceUrl`;
// internal claims set `internal: true`. See StatsBand.astro for details.

import type { ReviewTag } from './reviews';

export interface ServiceTip {
  body: string;
  eyebrow?: string;
  name?: string;
  role?: string;
  portrait?: string;
}

export interface ServiceStat {
  value: string;
  unit?: string;
  label: string;
  sourceUrl?: string;
  sourceLabel?: string;
  internal?: boolean;
}

export interface ServiceStatsBlock {
  eyebrow?: string;
  heading?: string;
  subheading?: string;
  stats: ServiceStat[];
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
  stats?: ServiceStatsBlock;
  tip?: ServiceTip;
  featureList?: ServiceFeatureList;
  relatedLink?: ServiceRelatedLink;
  reviewTag?: ReviewTag;
  reviewLabel?: string;
  closingBanner?: ServiceClosingBanner;
}

export const SERVICE_EXTRAS: Record<string, ServiceExtras> = {

  'custom-draperies-curtains': {
    stats: {
      eyebrow: 'By the numbers',
      heading: 'What custom drapery does for a St. Pete home',
      stats: [
        {
          // US Department of Energy: medium-color draperies with white
          // plastic backings can reduce heat gains by 33%.
          value: '33%',
          label: 'reduction in window heat gain from properly lined drapery, per the Department of Energy',
          sourceUrl: 'https://www.energy.gov/energysaver/energy-efficient-window-coverings',
          sourceLabel: 'US DOE',
        },
        {
          value: '25+',
          unit: 'years',
          label: 'fabricating custom drapery in our own St. Pete workroom',
          internal: true,
        },
        {
          value: 'In-house',
          label: 'cutting, sewing, lining, and installation, no outsourced workroom',
          internal: true,
        },
      ],
    },
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
    stats: {
      eyebrow: 'By the numbers',
      heading: 'Why shades matter on a Florida window',
      stats: [
        {
          // US Department of Energy: cellular (honeycomb) shades can
          // reduce unwanted solar heat through windows by up to 80%.
          value: 'Up to 80%',
          label: 'reduction in unwanted solar heat from cellular shades, per the Department of Energy',
          sourceUrl: 'https://www.energy.gov/energysaver/energy-efficient-window-coverings',
          sourceLabel: 'US DOE',
        },
        {
          value: '25+',
          unit: 'years',
          label: 'installing shades across Pinellas County',
          internal: true,
        },
        {
          value: 'Somfy',
          label: 'authorized motorization for hard-to-reach and oversized windows',
          internal: true,
        },
      ],
    },
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

  'plantation-shutters': {
    stats: {
      eyebrow: 'By the numbers',
      heading: 'Why plantation shutters belong in a St. Pete home',
      stats: [
        {
          // Atlantic hurricane season runs June 1 through November 30.
          // Authoritative source: NOAA National Hurricane Center.
          value: '6',
          unit: 'months',
          label: 'of Atlantic hurricane season every year in Florida',
          sourceUrl: 'https://www.nhc.noaa.gov/climo/',
          sourceLabel: 'NOAA NHC',
        },
        {
          value: '25+',
          unit: 'years',
          label: 'installing custom shutters across Pinellas County',
          internal: true,
        },
        {
          // Hunter Douglas, Norman, Graber, Kravet, Stout. Maintained in
          // src/lib/site.ts BRANDS array.
          value: '5',
          label: 'authorized brand partnerships, no big-box catalog',
          internal: true,
        },
      ],
    },
    tip: {
      // Tip A: locked by Daniel as the voice anchor on 2026-05-20.
      body: 'If the room has a shower, a stove, or a window facing the Gulf, go with faux wood. Real wood is beautiful, but I have been called back to too many St. Pete bathrooms where the basswood swelled by the second summer. Save the real wood for a formal dining room or a front sitting room where the AC stays steady and the salt air does not reach. That is where it earns its keep.',
    },
    featureList: {
      // Scannable summary of the "why faux wood works in Florida" section
      // that already exists in the markdown. The list complements the
      // prose; we will trim the matching paragraphs in a future content
      // pass once the layout is approved.
      items: [
        { label: 'Moisture resistance', body: 'Quality faux wood does not absorb humidity the way real wood does, so louvers stay aligned through Tampa Bay summers.' },
        { label: 'UV stability', body: 'Premium cores resist Gulf-side sun without yellowing or becoming brittle.' },
        { label: 'Storm-season durability', body: 'A built shutter adds an extra layer of window protection through wind-driven rain.' },
        { label: 'Precise light control', body: 'Adjustable louvers redirect light and heat without giving up the view.' },
      ],
      columns: 2,
    },
    relatedLink: {
      body: 'Trying to decide between shutters and a softer treatment over the same window? Our drapery and curtains page covers when each treatment wins, and when to layer both.',
      href: '/services/custom-draperies-curtains/',
      linkText: 'See custom drapery options',
    },
    reviewTag: 'plantation-shutters',
    reviewLabel: 'What St. Pete homeowners say',
    closingBanner: {
      statement: '25+ years installing across Pinellas. Authorized dealer for Hunter Douglas, Norman, Graber, Kravet, and Stout. Built for Florida humidity, Gulf sun, and hurricane season.',
    },
  },
};

export function getServiceExtras(slug: string): ServiceExtras | undefined {
  return SERVICE_EXTRAS[slug];
}
