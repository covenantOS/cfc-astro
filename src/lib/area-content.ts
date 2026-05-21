// Per-area content for /areas/[slug] dynamic routes.
export interface AreaBlock {
  slug: string;
  title: string;
  seoTitle: string;
  description: string;
  heroTitle: string;
  heroSubtitle: string;
  sections: Array<{
    heading: string;
    body: string;
  }>;
  faqs: Array<{ q: string; a: string }>;
}

Const SHARED_FAQS = [
  {
    q: 'Do you charge for the in-home consultation?',
    a: 'No. Initial in-home consultations are complimentary across the St. Pete coast. We bring fabric samples, finishes, and hardware options to your space.',
  },
  {
    q: 'How long does a typical project take?',
    a: 'Most custom window treatment projects take 4-8 weeks from consultation to installation, depending on the products and fabrics selected.',
  },
  {
    q: 'Do you handle installation?',
    a: 'Yes. Every installation is done by our own team, never a subcontractor. We handle the full white-glove process from measurement to final fit.',
  },
];

export const AREA_CONTENT: Record<string, AreaBlock> = {
  'st-petersburg': {
    slug: 'st-petersburg',
    title: 'St. Petersburg',
    seoTitle: 'Window Treatments & Upholstery in St. Petersburg, FL',
    description: 'Custom window treatments, drapery, shutters, and upholstery for St. Petersburg homes. Locally owned studio, in-house workroom, free consultation.',
    heroTitle: 'Custom Window Treatments in St. Petersburg, FL',
    heroSubtitle: 'From Beach Drive condos to Snell Isle estates, our St. Pete studio has dressed windows and reupholstered furniture across every corner of the city for 25 years.',
    sections: [
      {
        heading: 'A Studio Built for St. Pete Homes',
        body: `St. Petersburg is a city of distinct neighborhoods, Craftsman bungalows in the Historic Old Northeast, mid-century ranches in Shore Acres, high-rise condos on Beach Drive, estate waterfront homes on Snell Isle. Each has different window profiles, different light conditions, different architectural sensibilities.

We've designed window treatments for every one of them. When we come to your home for an in-home consultation, we're not reading a pattern book, we're drawing on 25 years of knowing what works in each St. Pete neighborhood.`,
      },
      {
        heading: 'Services We Offer in St. Petersburg',
        body: `Custom drapery and curtains · plantation shutters (faux wood and basswood) · window shades (roller, roman, cellular, solar, motorized) · custom blinds (wood, faux wood, aluminum) · cornices and valances · drapery hardware · outdoor solar screens · furniture reupholstery · custom bedding, pillows, and headboards · commercial window treatments.

Everything is measured in person, cut and sewn in our St. Pete workroom, and installed by our own team.`,
      },
      {
        heading: 'Why Locals Choose Custom Fabric Creations',
        body: `**In-house workroom.** Most window treatment retailers in the Tampa Bay area outsource sewing to third-party workrooms in other states. We cut and sew every drapery panel, cornice, cushion, and headboard in our St. Pete workroom.

**Authorized dealer for the brands designers trust.** Hunter Douglas, Norman, Graber, Kravet, Stout.

**Established 2000.** Locally owned. Fully insured. 25+ years of St. Pete work behind our name.`,
      },
    ],
    faqs: SHARED_FAQS,
  },

  'downtown-st-pete': {
    slug: 'downtown-st-pete',
    title: 'Downtown St. Pete',
    seoTitle: 'Window Treatments in Downtown St. Pete, FL',
    description: 'Custom window treatments for Beach Drive, the 400 Block, Sundial, and downtown St. Pete condos and high-rises.',
    heroTitle: 'Custom Window Treatments in Downtown St. Pete',
    heroSubtitle: 'Beach Drive condos, 400 Block residences, Sundial towers, we specialize in window treatments designed around high-rise light, hurricane-impact glass, and HOA requirements.',
    sections: [
      {
        heading: 'High-Rise Living, Designed Right',
        body: `Downtown St. Pete high-rises present a specific set of window treatment challenges, large glass, dramatic light shifts through the day, hurricane-impact glass systems, HOA limitations on exterior modifications, and often spectacular Gulf or bay views you don't want to lose.

We've worked in most of the downtown towers, 400 Beach Drive, ONE, Bliss, Saltaire, Sundial. We know which products HOAs allow, which tracks work with impact windows, and how to preserve the view while controlling heat gain.`,
      },
      {
        heading: 'The Right Products for Downtown',
        body: `**Solar shades** preserve your view while blocking UV and heat. The workhorse of downtown St. Pete condos.

**Motorized treatments** are essential on 12-foot glass sliders and clerestory windows that don't have accessible hardware.

**Layered drapery** adds softness to hard modern interiors, linen or velvet sheers over solar shades.`,
      },
      {
        heading: 'HOA-Friendly',
        body: `We know which products satisfy most downtown HOAs, typically requiring either white or cream facing-out fabrics, no exterior projections, and specific track types. We handle the HOA approval paperwork on your behalf.`,
      },
    ],
    faqs: SHARED_FAQS,
  },

  'old-northeast': {
    slug: 'old-northeast',
    title: 'Historic Old Northeast',
    seoTitle: 'Window Treatments in Historic Old Northeast, St. Petersburg',
    description: 'Custom drapery and shutters for the Historic Old Northeast, bungalows, Mediterranean revivals, and Craftsman homes.',
    heroTitle: 'Window Treatments in Historic Old Northeast',
    heroSubtitle: 'The Historic Old Northeast deserves window treatments that honor its bungalows, Mediterranean revivals, and Craftsman architecture.',
    sections: [
      {
        heading: 'Honoring the Architecture',
        body: `The Historic Old Northeast is one of Florida's most architecturally significant neighborhoods, a registered historic district with Craftsman bungalows, Mediterranean revivals, colonials, and frame vernaculars dating back to the 1910s.

Window treatments in these homes need to respect the architecture. That means avoiding modern looks that fight the period details (no vertical blinds, no plastic faux wood in historic dining rooms). It means recommending drapery, plantation shutters, and woven wood shades that complement rather than compete.`,
      },
      {
        heading: 'Period-Appropriate Products',
        body: `**Basswood plantation shutters** are our default recommendation for historic interiors, real wood, period-correct, stainable to match original trim.

**Roman shades** in natural linens, grasscloths, and patterned fabrics suit Craftsman and bungalow light.

**Layered drapery** in period-appropriate textiles (florals, damasks, solid velvets) brings formal dining and primary bedrooms to life without looking kitschy.`,
      },
      {
        heading: 'Working Around Original Windows',
        body: `Many ONE homes still have their original double-hung wood windows. These are beautiful, and they're often out of square, with deep brick molding and tricky sightlines. We've measured hundreds of these windows. We know what works.`,
      },
    ],
    faqs: SHARED_FAQS,
  },

  'snell-isle': {
    slug: 'snell-isle',
    title: 'Snell Isle',
    seoTitle: 'Window Treatments & Upholstery in Snell Isle, FL',
    description: 'Bespoke drapery, plantation shutters, and reupholstery for Snell Isle waterfront estates. In-home consultation with designer fabric library.',
    heroTitle: 'Bespoke Window Treatments in Snell Isle',
    heroSubtitle: 'Estate-scale drapery, shutters, and upholstery for Snell Isle’s waterfront homes. Our work has been installed on Venetian Boulevard, Brightwaters, and Coffee Pot Boulevard for 20+ years.',
    sections: [
      {
        heading: 'Estate-Scale Work',
        body: `Snell Isle estates demand a different level of work than standard residential. Floor-to-ceiling glass. 20-foot ceilings. Architectural windows with arch tops, bay windows, and bow windows. Custom-length drapery that extends 12+ feet.

Our workroom is built for this scale. We have the looms, the tracks, and the install experience to handle estate-scale projects end-to-end.`,
      },
      {
        heading: 'Waterfront-Specific Products',
        body: `Snell Isle's waterfront homes deal with intense UV exposure, salt-air corrosion, and hurricane-impact glass. We spec every product for waterfront conditions, UV-stabilized fabrics, marine-grade hardware, motorized systems that handle glass wall openings.`,
      },
      {
        heading: 'Designer Collaboration',
        body: `Many Snell Isle homes work with an interior designer. We love collaborating, we're a trusted soft-goods partner for several Tampa Bay-area designers working on Snell Isle estates.`,
      },
    ],
    faqs: SHARED_FAQS,
  },

  'shore-acres': {
    slug: 'shore-acres',
    title: 'Shore Acres',
    seoTitle: 'Window Treatments in Shore Acres, St. Petersburg',
    description: 'Practical, elegant window treatments for Shore Acres family homes. Waterfront-friendly fabrics, hurricane-aware installation, family-durable finishes.',
    heroTitle: 'Window Treatments in Shore Acres',
    heroSubtitle: 'Practical elegance for Shore Acres, waterfront-friendly fabrics, hurricane-aware installation, family-durable finishes that hold up to kids, pets, and Florida sun.',
    sections: [
      {
        heading: 'Family Homes, Designed for Real Life',
        body: `Shore Acres is a family neighborhood. Window treatments here need to look beautiful in photos and survive a 10-year-old, two dogs, and Florida humidity. We recommend materials that do both, faux wood plantation shutters that clean with a damp rag, indoor-outdoor fabrics from Sunbrella and Crypton, motorized cordless shades that are child- and pet-safe.`,
      },
      {
        heading: 'Hurricane Considerations',
        body: `Shore Acres sits low. Hurricane preparation matters. We install window treatments compatible with hurricane shutter systems, and we spec outdoor products that can be retracted before a storm arrives.`,
      },
      {
        heading: 'Services in Shore Acres',
        body: `Custom drapery · plantation shutters · window shades · blinds · reupholstery · custom bedding and pillows.`,
      },
    ],
    faqs: SHARED_FAQS,
  },

  'west-st-pete': {
    slug: 'west-st-pete',
    title: 'West St. Pete',
    seoTitle: 'Window Treatments in West St. Pete, FL',
    description: 'Custom window treatments and upholstery for West St. Pete homes, from Central Avenue bungalows to newer builds. Free in-home consultation.',
    heroTitle: 'Custom Window Treatments in West St. Pete',
    heroSubtitle: 'West St. Pete homes, from Central Avenue bungalows to newer builds, get the same studio craftsmanship and white-glove service.',
    sections: [
      {
        heading: 'Serving West St. Pete',
        body: `West St. Pete includes some of the city's most architecturally diverse neighborhoods, Jungle Prada, Jungle Terrace, Azalea, Pasadena. From 1920s Spanish bungalows to 2020s new builds. We work on all of it.`,
      },
      {
        heading: 'In-Home Consultation',
        body: `We come to you with a full fabric library. You see textiles in your actual light, against your actual walls. No showroom trips, no guesswork.`,
      },
      {
        heading: 'Full Service List',
        body: `Custom drapery, plantation shutters, window shades, blinds, cornices, reupholstery, custom bedding, exterior solar screens, everything built and installed by our team.`,
      },
    ],
    faqs: SHARED_FAQS,
  },

  'tierra-verde': {
    slug: 'tierra-verde',
    title: 'Tierra Verde',
    seoTitle: 'Window Treatments in Tierra Verde, FL',
    description: 'Tierra Verde waterfront homes demand Florida-tough fabrics and UV-resistant shades. Bespoke window treatments and exterior solar screens.',
    heroTitle: 'Window Treatments in Tierra Verde',
    heroSubtitle: 'Tierra Verde waterfront estates demand Florida-tough fabrics, UV-resistant shades, and exterior treatments built for the elements.',
    sections: [
      {
        heading: 'Waterfront, Island Living',
        body: `Tierra Verde sits on a barrier island at the mouth of Tampa Bay. That means intense sun, salt air, and waterfront views you absolutely do not want to block with the wrong window treatments.

We specialize in solutions that preserve view while controlling heat, solar shades, motorized drapery tracks behind crown molding, UV-stabilized exterior products for lanais and pool cages.`,
      },
      {
        heading: 'Exterior Shade Systems',
        body: `Tierra Verde homes often have massive lanais, pool cages, and outdoor living areas that need exterior shade to be usable. We install motorized solar screens, drop-down bug screens, and weatherproof shades that handle the salt air.`,
      },
    ],
    faqs: SHARED_FAQS,
  },

  'st-pete-beach': {
    slug: 'st-pete-beach',
    title: 'St. Pete Beach',
    seoTitle: 'Window Treatments in St. Pete Beach, FL',
    description: 'Custom window treatments for St. Pete Beach condos and homes, sun-durable shades, salt-air-ready hardware, resort-level finish.',
    heroTitle: 'Window Treatments in St. Pete Beach',
    heroSubtitle: 'St. Pete Beach condos and homes, sun-durable shades, salt-air-ready hardware, resort-level finish.',
    sections: [
      {
        heading: 'Beach Condos Designed Right',
        body: `St. Pete Beach condos have specific window treatment needs, direct beach-facing sun, impact glass, HOA rules about exterior-facing fabric colors. We know the buildings, we know the rules, and we know which products hold up in beach conditions.`,
      },
      {
        heading: 'Products We Recommend',
        body: `**Solar shades** protect flooring and furniture from UV without killing your beach view. **Blackout roller shades** in bedrooms for proper sleep. **Motorized tracks** for tall slider doors.`,
      },
    ],
    faqs: SHARED_FAQS,
  },

  'treasure-island': {
    slug: 'treasure-island',
    title: 'Treasure Island',
    seoTitle: 'Window Treatments in Treasure Island, FL',
    description: 'Custom window treatments for Treasure Island beach bungalows and high-rise condos. Built for Florida sun and salt air.',
    heroTitle: 'Window Treatments in Treasure Island',
    heroSubtitle: 'From beach bungalows to high-rise condos, Treasure Island homes get custom treatments sized for the sun and the view.',
    sections: [
      {
        heading: 'Two Treasure Islands',
        body: `Treasure Island has two distinct markets: mid-century beach bungalows (often recently renovated) and high-rise condos. Each has different needs. Bungalows often get plantation shutters and roman shades, classic Florida interior. Condos get solar shades and motorized drapery, modern, view-preserving.`,
      },
      {
        heading: 'Salt Air Considerations',
        body: `Everything installed in Treasure Island gets specified for coastal conditions. Marine-grade hardware. UV-stabilized fabrics. Corrosion-resistant tracks.`,
      },
    ],
    faqs: SHARED_FAQS,
  },

  'clearwater': {
    slug: 'clearwater',
    title: 'Clearwater',
    seoTitle: 'Window Treatments in Clearwater, FL',
    description: 'Clearwater estates and Island Estates homes, bespoke window fashions and reupholstery with full in-home service.',
    heroTitle: 'Window Treatments in Clearwater',
    heroSubtitle: 'Clearwater estates and Island Estates homes, bespoke window fashions and reupholstery with full in-home service.',
    sections: [
      {
        heading: 'Serving Clearwater',
        body: `We serve all of Clearwater, Island Estates waterfront, Harbor Oaks, Countryside, Belleair-adjacent neighborhoods. Full-service window treatments, reupholstery, and custom soft goods.`,
      },
      {
        heading: 'Why Clearwater Homeowners Choose Us',
        body: `In-house workroom. Authorized dealer for Hunter Douglas, Norman, Kravet, Stout. 25 years in Pinellas County. White-glove install by our own team.`,
      },
    ],
    faqs: SHARED_FAQS,
  },

  'sand-key': {
    slug: 'sand-key',
    title: 'Sand Key',
    seoTitle: 'Window Treatments in Sand Key, FL',
    description: 'Sand Key condos get treatments engineered for floor-to-ceiling glass, salt air, and direct sun exposure.',
    heroTitle: 'Window Treatments in Sand Key',
    heroSubtitle: 'Sand Key condos get treatments engineered for floor-to-ceiling glass, salt air, and direct sun exposure.',
    sections: [
      {
        heading: 'Sand Key Condo Living',
        body: `Sand Key is dominated by waterfront high-rises. Window treatments here must handle 10-20-foot glass walls, direct Gulf sun, and HOA rules about exterior appearance.

Our typical Sand Key spec: motorized solar shades for view preservation, layered drapery for softness, blackout shades in bedrooms.`,
      },
    ],
    faqs: SHARED_FAQS,
  },

  'belleair-shore': {
    slug: 'belleair-shore',
    title: 'Belleair Shore',
    seoTitle: 'Window Treatments in Belleair Shore, FL',
    description: 'Belleair Shore private homes deserve designer-quality drapery and upholstery. We come to you.',
    heroTitle: 'Window Treatments in Belleair Shore',
    heroSubtitle: 'Belleair Shore’s private homes deserve designer-quality drapery and upholstery. We come to you.',
    sections: [
      {
        heading: 'Quiet, Discreet Service',
        body: `Belleair Shore is small, private, and discreet. Our clients here expect in-home consultation, designer-quality product, and installation that doesn't disrupt the household. That's what we deliver.`,
      },
    ],
    faqs: SHARED_FAQS,
  },

  'seminole': {
    slug: 'seminole',
    title: 'Seminole',
    seoTitle: 'Window Treatments in Seminole, FL',
    description: 'Custom window treatments for Seminole families. Modern construction, view-preserving products, 25+ years of local experience.',
    heroTitle: 'Window Treatments in Seminole',
    heroSubtitle: 'Seminole families get bespoke treatments that fit modern construction, preserve view lines, and last for decades.',
    sections: [
      {
        heading: 'Serving Seminole',
        body: `Seminole is a mix of established neighborhoods and newer construction. We work across both, from 1970s ranch windows to 2020s new-construction Pella-and-Andersen openings.`,
      },
    ],
    faqs: SHARED_FAQS,
  },

  'largo': {
    slug: 'largo',
    title: 'Largo',
    seoTitle: 'Window Treatments in Largo, FL',
    description: 'Largo homeowners get the same studio craftsmanship, precision measurement, in-house sewing, installation by our own team.',
    heroTitle: 'Window Treatments in Largo',
    heroSubtitle: 'Largo homeowners get the same studio craftsmanship, precision measurement, in-house sewing, installation by our own team.',
    sections: [
      {
        heading: 'Serving Largo',
        body: `Largo is Pinellas County’s third-largest city and one of the most architecturally varied in the region. Bay-area ranches, mid-century homes, newer construction, and established estate neighborhoods all sit within its borders. We’ve worked across that full range and understand what fits each house type.

Whether you’re in Harbor Bluffs, Country Club, Pinebrook Estates, or Ridgecrest, we come to your home with the full studio, fabric library, hardware samples, and design consultation included.`,
      },
      {
        heading: 'Services in Largo',
        body: `Custom drapery and curtains · plantation shutters in faux wood and basswood · roller, roman, solar, and cellular shades · motorized window systems · blinds in wood, faux wood, and aluminum · cornices, valances, and drapery hardware · furniture reupholstery · custom bedding, headboards, and pillows · commercial window treatments.

Every piece is measured in person, fabricated in our St. Pete workroom, and installed by our own team. No subcontractors, no outsourcing.`,
      },
      {
        heading: 'Why Largo Homeowners Choose Us',
        body: `**In-house workroom.** Every drapery panel, cornice, cushion, and headboard is cut and sewn in our St. Petersburg workroom, not shipped in from a national manufacturer.

**Authorized dealer.** Hunter Douglas, Norman, Graber, Kravet, Stout. Lifetime limited warranties on most products.

**25+ years.** We’ve been doing window treatments and upholstery across Pinellas County since 2000. Established, insured, locally owned.`,
      },
    ],
    faqs: SHARED_FAQS,
  },
};
