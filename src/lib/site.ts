export const SITE = {
  name: 'Custom Fabric Creations',
  shortName: 'CFC',
  // Canonical production host. www is canonical (per GSC: 100% of search traffic
  // historically lives at www). Apex 301-redirects to www at the Cloudflare edge.
  url: 'https://www.customfabriccreations.net',
  tagline: 'Bespoke Window Treatments & Custom Upholstery',
  description:
    'St. Petersburg’s premier studio for custom window treatments, drapery, plantation shutters, shades, and bespoke upholstery. Established 2000. Free in-home consultations.',
  phone: '(727) 240-4512',
  phoneHref: 'tel:+17272404512',
  email: 'info@customfabriccreations.net',
  address: {
    locality: 'St. Petersburg',
    region: 'FL',
    country: 'US',
  },
  hours: 'Monday–Saturday, 7:00am–7:00pm',
  established: 2000,
} as const;

export const NAV: ReadonlyArray<{ label: string; href: string; children?: ReadonlyArray<{ label: string; href: string }> }> = [
  { label: 'Home', href: '/' },
  {
    label: 'Services',
    href: '/services/',
    children: [
      { label: 'Custom Drapery & Curtains', href: '/services/custom-draperies-curtains/' },
      { label: 'Plantation Shutters', href: '/services/plantation-shutters/' },
      { label: 'Window Shades', href: '/services/window-shades/' },
      { label: 'Custom Blinds', href: '/services/custom-blinds/' },
      { label: 'Cornices & Valances', href: '/services/custom-cornices-valances/' },
      { label: 'Drapery Hardware', href: '/services/drapery-hardware/' },
      { label: 'Outdoor Window Shades', href: '/services/outdoor-window-shades/' },
      { label: 'Furniture Reupholstery', href: '/services/furniture-reupholstery/' },
      { label: 'Custom Bedding & Pillows', href: '/services/custom-bedding-pillows/' },
      { label: 'Custom Banquettes', href: '/services/custom-banquettes/' },
      { label: 'Commercial Window Treatments', href: '/services/commercial-window-treatments/' },
      { label: 'Interior Decor Consultation', href: '/services/services-interior-decor-tampa/' },
    ],
  },
  {
    label: 'Areas',
    href: '/areas/',
    children: [
      { label: 'St. Petersburg', href: '/areas/st-petersburg/' },
      { label: 'Downtown St. Pete', href: '/areas/downtown-st-pete/' },
      { label: 'Historic Old Northeast', href: '/areas/old-northeast/' },
      { label: 'Snell Isle', href: '/areas/snell-isle/' },
      { label: 'Shore Acres', href: '/areas/shore-acres/' },
      { label: 'West St. Pete', href: '/areas/west-st-pete/' },
      { label: 'Tierra Verde', href: '/areas/tierra-verde/' },
      { label: 'St. Pete Beach', href: '/areas/st-pete-beach/' },
      { label: 'Treasure Island', href: '/areas/treasure-island/' },
      { label: 'Clearwater', href: '/areas/clearwater/' },
      { label: 'Sand Key', href: '/areas/sand-key/' },
      { label: 'Belleair Shore', href: '/areas/belleair-shore/' },
      { label: 'Seminole', href: '/areas/seminole/' },
      { label: 'Largo', href: '/areas/largo/' },
    ],
  },
  { label: 'Brands', href: '/brands/' },
  { label: 'Gallery', href: '/gallery/' },
  { label: 'About', href: '/about/' },
  { label: 'Contact', href: '/contact/' },
];

export const SERVICES = [
  { slug: 'custom-draperies-curtains', title: 'Custom Drapery & Curtains' },
  { slug: 'plantation-shutters', title: 'Plantation Shutters' },
  { slug: 'window-shades', title: 'Window Shades' },
  { slug: 'custom-blinds', title: 'Custom Blinds' },
  { slug: 'custom-cornices-valances', title: 'Cornices & Valances' },
  { slug: 'drapery-hardware', title: 'Drapery Hardware' },
  { slug: 'outdoor-window-shades', title: 'Outdoor Window Shades' },
  { slug: 'furniture-reupholstery', title: 'Furniture Reupholstery' },
  { slug: 'custom-bedding-pillows', title: 'Custom Bedding & Pillows' },
  { slug: 'custom-banquettes', title: 'Custom Banquettes' },
  { slug: 'commercial-window-treatments', title: 'Commercial Window Treatments' },
  { slug: 'services-interior-decor-tampa', title: 'Interior Decor Consultation' },
] as const;

export const AREAS = [
  { slug: 'st-petersburg', title: 'St. Petersburg', descriptor: 'Our home base' },
  { slug: 'downtown-st-pete', title: 'Downtown St. Pete', descriptor: 'High-rises & lofts' },
  { slug: 'old-northeast', title: 'Historic Old Northeast', descriptor: 'Bungalows & craftsman' },
  { slug: 'snell-isle', title: 'Snell Isle', descriptor: 'Waterfront estates' },
  { slug: 'shore-acres', title: 'Shore Acres', descriptor: 'NE St. Pete' },
  { slug: 'west-st-pete', title: 'West St. Pete', descriptor: 'Mid-century homes' },
  { slug: 'tierra-verde', title: 'Tierra Verde', descriptor: 'Gulf-front estates' },
  { slug: 'st-pete-beach', title: 'St. Pete Beach', descriptor: 'Coastal condos' },
  { slug: 'treasure-island', title: 'Treasure Island', descriptor: 'Beach community' },
  { slug: 'clearwater', title: 'Clearwater', descriptor: 'Pinellas County' },
  { slug: 'sand-key', title: 'Sand Key', descriptor: 'Barrier island' },
  { slug: 'belleair-shore', title: 'Belleair Shore', descriptor: 'Coastal village' },
  { slug: 'seminole', title: 'Seminole', descriptor: 'Mid-Pinellas' },
  { slug: 'largo', title: 'Largo', descriptor: 'Central Pinellas' },
] as const;

export const BRANDS = [
  { name: 'Hunter Douglas', slug: 'hunter-douglas' },
  { name: 'Norman', slug: 'norman' },
  { name: 'Graber', slug: 'graber' },
  { name: 'Kravet', slug: 'kravet' },
  { name: 'Stout', slug: 'stout' },
] as const;
