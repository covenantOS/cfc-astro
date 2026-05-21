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

export interface AreaCard {
  title: string;
  body: string;
}

export interface AreaTreatment {
  title: string;
  href: string;
  body: string;
}

export interface AreaStep {
  title: string;
  body: string;
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
  // What homeowners need (3-4 cards)
  needsHeading: string;
  needsIntro: string;
  needs: AreaCard[];
  // Window challenges specific to the area (long-form)
  challengesHeading: string;
  challengesParagraphs: string[];
  challengesList: string[];
  servicesHeading: string;
  // Popular treatments (link cards into service pages)
  treatmentsHeading: string;
  treatmentsIntro: string;
  treatments: AreaTreatment[];
  // How it works (process)
  processHeading: string;
  processIntro: string;
  process: AreaStep[];
  tipBody: string;
  neighborhoodsHeading: string;
  neighborhoodsIntro: string;
  neighborhoods: AreaNeighborhood[];
  // Why homeowners choose CFC (trust points)
  whyHeading: string;
  why: AreaCard[];
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
    needsHeading: 'What St. Petersburg Homeowners Need From Custom Fabric Creations',
    needsIntro: 'St. Pete homes are not built or weathered like homes anywhere else. Here is what we hear from homeowners across the city, and what we build for.',
    needs: [
      { title: 'Treatments that survive the salt air', body: 'Bay-side homes go through cheap blinds fast. Rusting hardware, brittle slats, and faded fabric are the giveaways. We spec corrosion-resistant hardware and marine-tough materials so the treatment lasts.' },
      { title: 'A precise fit for older windows', body: 'The bungalows and mid-century homes here almost never have standard openings. Every window gets measured individually and built to its exact size, so panels close clean with no gaps.' },
      { title: 'Style that fits a historic district', body: 'From Old Northeast craftsman trim to Downtown high-rise glass, the right treatment respects the architecture. We help you choose materials and profiles that suit the home, not fight it.' },
      { title: 'One local team, start to finish', body: 'Design, fabrication, and installation under one roof since 2000. The person who measures your windows is part of the same studio that builds and hangs them.' },
    ],
    challengesHeading: 'Window Challenges Specific to St. Petersburg',
    challengesParagraphs: [
      'Most window-treatment advice is written for mild, dry climates. St. Petersburg is neither. Salt air off Tampa Bay corrodes cheap hardware, the near-constant sun bleaches synthetic fabric and warps low-grade vinyl, and the humidity swells materials that were never meant for the coast.',
      'On top of the climate, the housing stock is unusually varied. A 1920s bungalow near Crescent Lake, a concrete-block ranch in the 1950s neighborhoods, and a glass-walled condo on Beach Drive each demand a different approach to mounting, material, and light control. A one-size product simply does not work here.',
    ],
    challengesList: [
      'Salt-air corrosion on hardware and mechanisms near the water',
      'UV fading and heat gain on south and west exposures',
      'Out-of-square and non-standard openings in older homes',
      'Anchoring into concrete-block walls without cracking the finish',
      'Arched, transom, and floor-to-ceiling windows that need custom shapes',
    ],
    servicesHeading: 'What We Offer in St. Petersburg',
    treatmentsHeading: 'Popular Treatments in St. Pete Homes',
    treatmentsIntro: 'The treatments St. Petersburg homeowners ask for most, and what each one solves here.',
    treatments: [
      { title: 'Plantation Shutters', href: '/services/plantation-shutters/', body: 'Faux-wood shutters that shrug off humidity and salt air, a favorite for historic-district homes that want a permanent, architectural look.' },
      { title: 'Custom Drapery & Curtains', href: '/services/custom-draperies-curtains/', body: 'Floor-length panels in UV-rated fabrics that soften a room and tame the afternoon sun, hand-built in our workroom.' },
      { title: 'Window Shades', href: '/services/window-shades/', body: 'Solar, cellular, and Roman shades for cutting heat and glare on bright exposures without losing the view.' },
      { title: 'Furniture Reupholstery', href: '/services/furniture-reupholstery/', body: 'Reupholster heirloom and statement pieces in performance fabrics, coordinated with your new window treatments.' },
    ],
    processHeading: 'How It Works in St. Petersburg',
    processIntro: 'A straightforward process, from the first call to the final walk-through.',
    process: [
      { title: 'Free in-home consultation', body: 'We bring the fabric library and samples to your home so you can judge color and texture in your own light.' },
      { title: 'Precise on-site measurement', body: 'Every window is measured individually by our team, never estimated, and documented for the workroom.' },
      { title: 'Built in our St. Pete workroom', body: 'Your treatments are cut, sewn, and finished locally to your exact specs, with a clear timeline up front.' },
      { title: 'Professional installation', body: 'Our own installers mount, level, and adjust everything, then walk the result with you before the job is done.' },
    ],
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
    whyHeading: 'Why St. Petersburg Homeowners Choose Custom Fabric Creations',
    why: [
      { title: 'In-house workroom since 2000', body: 'We design, build, and finish on-site, so adjustments and touch-ups happen here, not at a factory three states away.' },
      { title: 'Installers who do only this', body: 'Our own crew, not subcontractors, with years of hanging treatments in St. Pete homes and concrete-block walls.' },
      { title: 'Authorized brand dealer', body: 'Hunter Douglas, Norman, Graber, Kravet, and Stout, with full warranties honored and every color and option available.' },
      { title: 'Local, family-run, and insured', body: 'Fully insured for residential and commercial work, and the person who quotes your job is often the one who finishes it.' },
    ],
    statStatement: '25+ years installing across Pinellas. Authorized dealer for Hunter Douglas, Norman, Graber, Kravet, and Stout. Built for Florida humidity, Gulf sun, and salt air.',
    faqs: [
      { q: 'Do you come to homes throughout St. Petersburg?', a: 'Yes. We bring the fabric library, hardware samples, and measuring tools to your home anywhere in central St. Pete, from Old Northeast to Downtown to Shore Acres. The consultation is free.' },
      { q: 'My house is older with odd window sizes. Is that a problem?', a: 'Not at all. Older St. Pete homes almost never have standard windows. We measure every opening individually and build to those exact dimensions, which is the whole point of going custom.' },
      { q: 'Will window treatments hold up to the salt air?', a: 'They will if they are specified correctly. We steer you toward faux wood, UV-stable fabrics, and corrosion-resistant hardware for homes near the water, and away from the products that fail in a single Florida summer.' },
      { q: 'Can you install on concrete-block walls?', a: 'Yes. Much of St. Pete is block construction. We anchor into block correctly so shutters and hardware sit flush and stay put, without cracking the surrounding finish.' },
      { q: 'Do you handle arched, transom, and floor-to-ceiling windows?', a: 'Yes. Specialty shapes are common in St. Pete homes. We template and build to the exact opening, including arches, transoms, and full-height sliders.' },
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
    needsHeading: 'What West St. Pete Homeowners Need From Custom Fabric Creations',
    needsIntro: 'The west side of St. Pete has its own kind of light and its own kind of homes. Here is what we build for over here.',
    needs: [
      { title: 'Real relief from the afternoon sun', body: 'West-facing glass turns living rooms into greenhouses by 4pm and fades furniture within a couple of seasons. We design treatments that cut the heat and glare while keeping the view.' },
      { title: 'Treatments sized for wide windows and sliders', body: 'Mid-century homes here are full of oversized sliders and picture windows. We build bypass shutters, panel tracks, and large-format shades that fit those openings cleanly.' },
      { title: 'A cooler home without a darker one', body: 'You should not have to choose between comfort and natural light. Solar shades and layered drapery let you keep the brightness and the view while bringing the temperature down.' },
      { title: 'Window treatments and upholstery together', body: 'Because we run our own workroom, we can reupholster the sun-faded sofa and dress the windows in one coordinated project, with fabrics that match.' },
    ],
    challengesHeading: 'Window Challenges Specific to West St. Pete',
    challengesParagraphs: [
      'West St. Pete homes catch the worst of the day. The low afternoon sun pours straight through west-facing glass, driving up indoor temperatures, spiking cooling bills, and bleaching everything it touches, from hardwood floors to upholstery to artwork.',
      'The architecture adds to it. This side of the city leans mid-century, with wide windows, banks of jalousies replaced by modern glass, and big sliding doors built for indoor-outdoor living. Those openings are wonderful for light and views, and brutal without the right treatment to manage the heat.',
    ],
    challengesList: [
      'Intense west-facing afternoon sun and heat gain',
      'UV fading of furniture, flooring, and fabrics',
      'Oversized sliders and picture windows that need large-format treatments',
      'Glare on screens and work surfaces in bright rooms',
      'Keeping the view and the light while cutting the heat',
    ],
    servicesHeading: 'What We Offer in West St. Pete',
    treatmentsHeading: 'Popular Treatments in West St. Pete Homes',
    treatmentsIntro: 'The treatments that work hardest on the west side, and what each one does here.',
    treatments: [
      { title: 'Window Shades', href: '/services/window-shades/', body: 'Solar and cellular shades that block heat and glare on west-facing windows while you keep looking out through the fabric.' },
      { title: 'Custom Drapery & Curtains', href: '/services/custom-draperies-curtains/', body: 'Soft panels in UV-rated fabric layered over shades for warmth in the evening and full light control during the day.' },
      { title: 'Plantation Shutters', href: '/services/plantation-shutters/', body: 'Adjustable louvers that redirect the afternoon sun without closing the room off, built in humidity-proof faux wood.' },
      { title: 'Furniture Reupholstery', href: '/services/furniture-reupholstery/', body: 'Bring sun-faded seating back to life in durable performance fabrics, coordinated with your new treatments.' },
    ],
    processHeading: 'How It Works in West St. Pete',
    processIntro: 'A straightforward process, from the first call to the final walk-through.',
    process: [
      { title: 'Free in-home consultation', body: 'We come to you with samples and look at each window in its real light and exposure, west-facing rooms included.' },
      { title: 'Precise on-site measurement', body: 'Every opening, including wide sliders and picture windows, is measured individually and documented for the workroom.' },
      { title: 'Built in our St. Pete workroom', body: 'Shades, drapery, and shutters are made locally to your exact specs, with a clear timeline before we begin.' },
      { title: 'Professional installation', body: 'Our own installers mount and calibrate everything, including motorized systems, then walk the result with you.' },
    ],
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
    whyHeading: 'Why West St. Pete Homeowners Choose Custom Fabric Creations',
    why: [
      { title: 'In-house workroom since 2000', body: 'Design, fabrication, and finishing on-site, so changes and touch-ups are handled locally, not shipped off to a factory.' },
      { title: 'Installers who do only this', body: 'Our own crew handles oversized sliders, panel tracks, and motorized systems that big-box installers struggle with.' },
      { title: 'Authorized brand dealer', body: 'Hunter Douglas, Norman, Graber, Kravet, and Stout, with full warranties and the complete range of solar and motorized options.' },
      { title: 'Local, family-run, and insured', body: 'Fully insured, locally owned, and accountable. The person who quotes your job is often the one who finishes it.' },
    ],
    statStatement: 'In-house workroom since 2000. Solar, cellular, Roman, and motorized shades plus custom drapery and shutters, measured and installed by the same West St. Pete team.',
    faqs: [
      { q: 'Which window treatment is best for west-facing windows?', a: 'For hard afternoon sun we usually start with solar shades, which cut heat and glare while keeping the view, then layer drapery where the room wants softness. We walk every window and recommend per opening.' },
      { q: 'Do you handle large sliders and Nana doors?', a: 'Yes. Wide sliders and Nana doors are common in West St. Pete homes. We install bypass shutters, panel tracks, and motorized shades sized to the opening, including battery and wired motor options.' },
      { q: 'How much can solar shades reduce heat?', a: 'A good solar shade meaningfully reduces solar heat gain and glare on a west-facing window while preserving the outward view. We help you pick the right openness factor for each room so you keep the light you want.' },
      { q: 'Will treatments stop my furniture from fading?', a: 'They help significantly. UV-filtering shades and lined drapery block much of the radiation that fades wood, fabric, and art. For the worst exposures we layer treatments for the most protection.' },
      { q: 'Can you help with both window treatments and reupholstery?', a: 'Yes. Because we run our own workroom, we can do shades or drapery and reupholster the seating in the same project, with coordinated fabrics, instead of juggling two vendors.' },
      { q: 'Do you offer in-home consultations on the west side?', a: 'Always. We bring samples and measure on-site anywhere in West St. Pete. The consultation is free and there is no obligation.' },
    ],
  },
};

export function getAreaPageConfig(slug: string): AreaPageConfig | undefined {
  return AREA_PAGES[slug];
}
