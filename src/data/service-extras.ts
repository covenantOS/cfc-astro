// Per-service configuration for the new content components:
//   - OwnerTip:    Terry-signed tip (40-70 words, her voice)
//   - StatsBand:   "By the numbers" verified-source stats
//   - InlineReview: contextual Google review pulled by tag
//
// Only services with an entry here render the components. Everything else
// renders the markdown content unchanged. We are rolling these out one
// service at a time so Daniel can react to the format before broad rollout.
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

export interface ServiceExtras {
  tip?: ServiceTip;
  stats?: ServiceStatsBlock;
  reviewTag?: ReviewTag;
  reviewLabel?: string;
}

// Maps service slug to its extras. Order in this map drives the placement
// order of the components on the page (see [slug].astro).
export const SERVICE_EXTRAS: Record<string, ServiceExtras> = {
  'plantation-shutters': {
    tip: {
      // Tip A (locked 2026-05-20 by Daniel as voice anchor).
      body: 'If the room has a shower, a stove, or a window facing the Gulf, go with faux wood. Real wood is beautiful, but I have been called back to too many St. Pete bathrooms where the basswood swelled by the second summer. Save the real wood for a formal dining room or a front sitting room where the AC stays steady and the salt air does not reach. That is where it earns its keep.',
    },
    stats: {
      eyebrow: 'By the numbers',
      heading: 'Why plantation shutters belong in a St. Pete home',
      stats: [
        {
          // Atlantic hurricane season runs June 1 through November 30, six
          // months of the year. Authoritative source: NOAA National
          // Hurricane Center.
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
    reviewTag: 'plantation-shutters',
    reviewLabel: 'What St. Pete homeowners say',
  },
};

export function getServiceExtras(slug: string): ServiceExtras | undefined {
  return SERVICE_EXTRAS[slug];
}
