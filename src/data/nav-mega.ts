import { AREAS } from '~/lib/site';

export const MEGA_FEATURED_SERVICES = [
  {
    title: 'Window Treatments',
    href: '/window-treatments-st-petersburg/',
    image: '/images/hero/homepage.webp',
  },
  {
    title: 'Window Shades',
    href: '/services/window-shades/',
    image: '/images/hero/window-shades.webp',
  },
  {
    title: 'Wallpaper',
    href: '/services/wallpaper/',
    image: '/images/hero/wallpaper.webp',
  },
  {
    title: 'Custom Banquettes',
    href: '/services/custom-banquettes/',
    image: '/images/hero/custom-banquettes.webp',
  },
  {
    title: 'Custom Drapery',
    href: '/services/custom-draperies-curtains/',
    image: '/images/hero/custom-draperies-curtains.webp',
  },
] as const;

export const MEGA_MORE_SERVICES = [
  { title: 'Plantation Shutters', href: '/services/plantation-shutters/' },
  { title: 'Custom Blinds', href: '/services/custom-blinds/' },
  { title: 'Cornices & Valances', href: '/services/custom-cornices-valances/' },
  { title: 'Drapery Hardware', href: '/services/drapery-hardware/' },
  { title: 'Outdoor Window Shades', href: '/services/outdoor-window-shades/' },
  { title: 'Motorized Shades', href: '/services/motorized-shades/' },
  { title: 'Furniture Reupholstery', href: '/services/furniture-reupholstery/' },
  { title: 'Custom Bedding & Pillows', href: '/services/custom-bedding-pillows/' },
  { title: 'Commercial Window Treatments', href: '/services/commercial-window-treatments/' },
  { title: 'Interior Decor Consultation', href: '/services/services-interior-decor-tampa/' },
] as const;

export const MEGA_SHOWROOM = {
  title: 'Showroom',
  href: '/areas/st-petersburg/',
  image: '/images/areas/st-petersburg.webp',
  body: '5001 4th St N, St. Petersburg. Window treatments, wallpaper, and upholstery. We still come to your house.',
} as const;

const featuredAreaSlugs = new Set(['st-petersburg']);

export const MEGA_AREA_LINKS = AREAS.filter((a) => !featuredAreaSlugs.has(a.slug));
