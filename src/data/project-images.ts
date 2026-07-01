import { AREAS } from '~/lib/site';

// Shared pool of recent-project images (the 2026 client image drop). Used by
// the area pages' "recent work" strip. These are generic project shots (not
// location-specific), so we rotate a different slice onto each area page to
// avoid the same three showing up everywhere.
export const PROJECT_IMAGES: { img: string; title: string }[] = [
  { img: '/images/new/window-treatment3.webp', title: 'Floor-to-Ceiling Drapery' },
  { img: '/images/new/custom-window-treatments.webp', title: 'Custom Window Treatments' },
  { img: '/images/new/custom-window-treatments-geometric-pattern.webp', title: 'Geometric Pattern Treatments' },
  { img: '/images/new/custom-curtains-and-drapery.webp', title: 'Custom Curtains & Drapery' },
  { img: '/images/new/custom-curtains.webp', title: 'Custom Curtains' },
  { img: '/images/new/custom-mauve-drapery-on-gold-hardware.webp', title: 'Mauve Drapery on Gold Hardware' },
  { img: '/images/new/modern-blackout-drapes-nailhead-trim-custom-fabrics.webp', title: 'Nailhead-Trim Blackout Drapes' },
  { img: '/images/new/custom-drapes-leather-armchairs-cow-art.webp', title: 'Drapery with Leather Seating' },
  { img: '/images/new/custom-sliding-glass-door-window-treatments.webp', title: 'Sliding Glass Door Treatments' },
  { img: '/images/new/integrated-drapery-and-shades-open-plan-living.webp', title: 'Layered Drapery & Shades' },
  { img: '/images/new/integrated-shades-and-drapery-system.webp', title: 'Shade & Drapery System' },
  { img: '/images/new/window-shades.webp', title: 'Custom Window Shades' },
  { img: '/images/new/custom-blinds.webp', title: 'Custom Blinds' },
  { img: '/images/new/custom-blinds-and-window-shades.webp', title: 'Blinds & Shades' },
  { img: '/images/new/outdoor-window-shades.webp', title: 'Outdoor Window Shades' },
  { img: '/images/new/cornices-and-valances.webp', title: 'Cornices & Valances' },
  { img: '/images/new/navy-blue-valance-geometric-drapery-panels.webp', title: 'Navy Valance & Geometric Panels' },
  { img: '/images/new/custom-banquettes.webp', title: 'Custom Banquette Seating' },
  { img: '/images/new/furniture-reupholstery.webp', title: 'Furniture Reupholstery' },
  { img: '/images/new/custom-bedding.webp', title: 'Custom Bedding' },
  { img: '/images/new/custom-bedding-and-pillows.webp', title: 'Bedding & Pillows' },
  { img: '/images/new/custom-bedding-and-pillows-master-bedroom.webp', title: 'Master Bedroom Bedding' },
  { img: '/images/new/commercial-window-treatments.webp', title: 'Commercial Window Treatments' },
  { img: '/images/new/commercial-window-curtains.webp', title: 'Commercial Drapery' },
  { img: '/images/new/interior-consultation-design.webp', title: 'Interior Design Consultation' },
  { img: '/images/new/interior-decor-consultation.webp', title: 'Interior Decor Consultation' },
  { img: '/images/new/interior-curtains.webp', title: 'Interior Curtains' },
  { img: '/images/new/window-treatments-big-window.webp', title: 'Treatments for Large Windows' },
];

// Return `count` images for an area, rotated by the area's position in AREAS so
// adjacent areas do not repeat the same set.
export function getAreaProjectImages(slug: string, count = 3) {
  const i = AREAS.findIndex((a) => a.slug === slug);
  const idx = i < 0 ? 0 : i;
  const out: { img: string; title: string }[] = [];
  for (let n = 0; n < count; n++) {
    out.push(PROJECT_IMAGES[(idx * count + n) % PROJECT_IMAGES.length]);
  }
  return out;
}
