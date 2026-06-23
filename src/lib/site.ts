// Two tracking numbers, one per main location. Both forward to the original
// office line (727-240-4512) which is NEVER displayed on the site, per
// Twilio routing setup. Central is the default for every page except the
// West St. Pete area page.
export const LOCATIONS = {
  central: {
    id: 'central',
    name: 'Central St. Pete (Main)',
    areaSlug: 'st-petersburg',
    phone: '(727) 914-5410',
    phoneHref: 'tel:+17279145410',
    // Mon-Sat 9-5 (Sunday closed by omission).
    openingHours: {
      dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
      opens: '09:00',
      closes: '17:00',
    },
  },
  westStPete: {
    id: 'west-st-pete',
    name: 'West St. Pete',
    areaSlug: 'west-st-pete',
    phone: '(727) 498-2108',
    phoneHref: 'tel:+17274982108',
    // West St. Pete GBP: Mon-Sat 8am-8pm, Sunday closed.
    openingHours: {
      dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
      opens: '08:00',
      closes: '20:00',
    },
  },
} as const;

export type LocationId = keyof typeof LOCATIONS;
export const DEFAULT_LOCATION = LOCATIONS.central;

export function getLocationForArea(areaSlug: string) {
  if (areaSlug === LOCATIONS.westStPete.areaSlug) return LOCATIONS.westStPete;
  return LOCATIONS.central;
}

// Pathname-based lookup for global components (Header, Footer, StickyMobileCTA)
// that do not receive an areaSlug prop. Only the West St. Pete area page
// overrides; everything else uses Central.
export function getLocationForPath(pathname: string) {
  if (pathname.startsWith('/areas/west-st-pete')) return LOCATIONS.westStPete;
  return LOCATIONS.central;
}

export const SITE = {
  name: 'Custom Fabric Creations',
  shortName: 'CFC',
  url: 'https://www.customfabriccreations.net',
  tagline: 'Bespoke Window Treatments & Custom Upholstery',
  description:
    'St. Petersburg’s premier studio for custom window treatments, drapery, plantation shutters, shades, and bespoke upholstery. Established 2000. Free in-home consultations.',
  // Default phone (Central). Pages that need the West St. Pete number import
  // getLocationForArea() or LOCATIONS.westStPete directly.
  phone: DEFAULT_LOCATION.phone,
  phoneHref: DEFAULT_LOCATION.phoneHref,
  email: 'info@customfabriccreations.net',
  address: {
    locality: 'St. Petersburg',
    region: 'FL',
    country: 'US',
  },
  hours: 'Monday-Saturday, 7:00am-7:00pm',
  established: 2000,
} as const;

export const NAV: ReadonlyArray<{ label: string; href: string; children?: ReadonlyArray<{ label: string; href: string; featured?: boolean; divider?: boolean }> }> = [
  { label: 'Home', href: '/' },
  {
    label: 'Services',
    href: '/services/',
    children: [
      { label: 'Window Treatments (Overview)', href: '/window-treatments-st-petersburg/', featured: true },
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
      // Two main locations promoted at the top. `featured: true` marks them
      // for visual emphasis in the dropdown; All Areas link sits below a divider.
      { label: 'St. Petersburg (Central)', href: '/areas/st-petersburg/', featured: true },
      { label: 'West St. Pete', href: '/areas/west-st-pete/', featured: true },
      { label: 'All Areas', href: '/areas/', divider: true },
    ],
  },
  { label: 'Brands', href: '/brands/' },
  { label: 'Gallery', href: '/gallery/' },
  { label: 'Blog', href: '/blog/' },
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
