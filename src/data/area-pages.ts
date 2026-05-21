// Config for the two main area LANDING pages (St. Petersburg Central and
// West St. Pete). These render as full section-based pages via
// AreaLanding.astro, not the content+sidebar AreaLayout used by the other
// areas. Keep these two slugs excluded from src/pages/areas/[slug].astro.

export interface AreaNeighborhood {
  name: string;
  note?: string;
}

export interface AreaFaq {
  q: string;
  a: string;
}

export interface AreaPageConfig {
  slug: string;
  locationKey: 'central' | 'westStPete';
  name: string;
  heroTitle: string;
  heroSubtitle: string;
  heroImage: string;
  introEyebrow: string;
  introHeading: string;
  introParagraphs: string[];
  introImage: string;
  servicesHeading: string;
  tipBody: string;
  neighborhoodsHeading: string;
  neighborhoodsIntro: string;
  neighborhoods: AreaNeighborhood[];
  statStatement: string;
  faqs: AreaFaq[];
}

export const AREA_PAGES: Record<string, AreaPageConfig> = {
  'st-petersburg': {
    slug: 'st-petersburg',
    locationKey: 'central',
    name: 'St. Petersburg',
    heroTitle: 'Custom Window Treatments in St. Petersburg',
    heroSubtitle: 'Plantation shutters, drapery, shades, and upholstery built for Tampa Bay salt air and St. Pete homes, from the historic bungalows to the waterfront high-rises. In-home consultation, in-house workroom, since 2000.',
    heroImage: '/images/areas/st-petersburg.webp',
    introEyebrow: 'Central St. Pete',
    introHeading: 'A Local Studio That Knows St. Pete Windows',
    introParagraphs: [
      'St. Petersburg is not a one-size-fits-all town. The 1920s bungalows near Crescent Lake, the waterfront condos along Beach Drive, and the concrete-block ranches in between all bring different window challenges, and salt air off the bay is hard on cheap hardware.',
      'We have measured, built, and installed window treatments across the city for more than two decades. You are not guessing whether the fit will be right or whether the product survives the humidity. You are working with the team that has already learned what lasts here.',
    ],
    introImage: '/images/areas/st-petersburg.webp',
    servicesHeading: 'What We Offer in St. Petersburg',
    tipBody: 'In the older St. Pete neighborhoods, the windows are rarely true to size and the walls are often concrete block. I always measure every opening individually, never off one sample, and we anchor into block the right way so shutters sit flush years later. It is the unglamorous part, but it is why the job still looks right in year ten.',
    neighborhoodsHeading: 'Neighborhoods We Serve Around Central St. Pete',
    neighborhoodsIntro: 'We bring the showroom to your door across central St. Petersburg, including:',
    neighborhoods: [
      { name: 'Historic Old Northeast' },
      { name: 'Snell Isle' },
      { name: 'Shore Acres' },
      { name: 'Downtown St. Pete' },
      { name: 'Crescent Lake' },
      { name: 'Historic Kenwood' },
      { name: 'Euclid - St. Paul' },
      { name: 'Coffee Pot Bayou' },
    ],
    statStatement: '25+ years installing across Pinellas. Authorized dealer for Hunter Douglas, Norman, Graber, Kravet, and Stout. Built for Florida humidity, Gulf sun, and salt air.',
    faqs: [
      { q: 'Do you come to homes throughout St. Petersburg?', a: 'Yes. We bring the fabric library, hardware samples, and measuring tools to your home anywhere in central St. Pete, from Old Northeast to Downtown to Shore Acres. The consultation is free.' },
      { q: 'My house is older with odd window sizes. Is that a problem?', a: 'Not at all. Older St. Pete homes almost never have standard windows. We measure every opening individually and build to those exact dimensions, which is the whole point of going custom.' },
      { q: 'Will window treatments hold up to the salt air?', a: 'They will if they are specified correctly. We steer you toward faux wood, UV-stable fabrics, and corrosion-resistant hardware for homes near the water, and away from the products that fail in a single Florida summer.' },
      { q: 'How long does a project take?', a: 'Most custom orders run a few weeks from approval to install, depending on the product and any specialty shapes. We give you a clear timeline before anything is ordered.' },
    ],
  },

  'west-st-pete': {
    slug: 'west-st-pete',
    locationKey: 'westStPete',
    name: 'West St. Pete',
    heroTitle: 'Custom Window Treatments in West St. Pete',
    heroSubtitle: 'Solar shades, drapery, plantation shutters, and reupholstery for West St. Pete homes, built for the wide windows and hard afternoon sun on this side of the city. In-home consultation, made in our own workroom.',
    heroImage: '/images/areas/west-st-pete.webp',
    introEyebrow: 'West St. Pete',
    introHeading: 'Window Treatments Built for the West-Side Sun',
    introParagraphs: [
      'West St. Pete leans mid-century, which usually means wide windows, big sliders, and a lot of west-facing glass. The afternoon sun here is relentless, and it fades furniture and drives up cooling bills faster than most homeowners expect.',
      'We design around that. The right mix of solar shades, drapery, and shutters keeps these rooms cool and livable without giving up the light or the view, and every piece is built and installed by our own St. Pete team.',
    ],
    introImage: '/images/areas/west-st-pete.webp',
    servicesHeading: 'What We Offer in West St. Pete',
    tipBody: 'West St. Pete homes lean mid-century, which usually means wide windows and big sliders that face west. The afternoon sun in here is no joke. It will fade a sofa in two seasons. For most of my West St. Pete clients I start with solar shades on the sliders and layer a soft drape on top. You keep the view, you keep the room cool, and the furniture lasts.',
    neighborhoodsHeading: 'Neighborhoods We Serve Around West St. Pete',
    neighborhoodsIntro: 'We serve homeowners across the west side of St. Petersburg, including:',
    neighborhoods: [
      { name: 'Pasadena' },
      { name: 'Jungle Prada' },
      { name: 'Causeway Isles' },
      { name: 'Tyrone' },
      { name: 'Disston Heights' },
      { name: 'Bear Creek' },
      { name: 'Broadwater' },
      { name: 'Yacht Club Estates' },
    ],
    statStatement: 'In-house workroom since 2000. Solar, cellular, Roman, and motorized shades plus custom drapery and shutters, measured and installed by the same West St. Pete team.',
    faqs: [
      { q: 'Which window treatment is best for west-facing windows?', a: 'For hard afternoon sun we usually start with solar shades, which cut heat and glare while keeping the view, then layer drapery where the room wants softness. We walk every window and recommend per opening.' },
      { q: 'Do you handle large sliders and Nana doors?', a: 'Yes. Wide sliders and Nana doors are common in West St. Pete homes. We install bypass shutters, panel tracks, and motorized shades sized to the opening, including battery and wired motor options.' },
      { q: 'Can you help with both window treatments and reupholstery?', a: 'Yes. Because we run our own workroom, we can do shades or drapery and reupholster the seating in the same project, with coordinated fabrics, instead of juggling two vendors.' },
      { q: 'Do you offer in-home consultations on the west side?', a: 'Always. We bring samples and measure on-site anywhere in West St. Pete. The consultation is free and there is no obligation.' },
    ],
  },
};

export function getAreaPageConfig(slug: string): AreaPageConfig | undefined {
  return AREA_PAGES[slug];
}
