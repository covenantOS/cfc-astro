import { AREAS } from '~/lib/site';

// Shared pool of recent-project images (the 2026 client image drop). Used by
// the area pages' "recent work" strip. These are generic project shots (not
// location-specific), so we rotate a different slice onto each area page to
// avoid the same three showing up everywhere.
export const PROJECT_IMAGES: { img: string; title: string }[] = [
  { img: '/images/new/formal-custom-drapery-swag-valance.webp', title: 'Formal Swag Valance' },
  { img: '/images/new/custom-upholstered-cornices-sunroom.webp', title: 'Upholstered Cornices' },
  { img: '/images/new/custom-drapery-layered-bay-window.webp', title: 'Layered Bay Window Drapery' },
  { img: '/images/new/custom-swag-valance-sliding-doors.webp', title: 'Swag Valance on Sliding Doors' },
  { img: '/images/new/custom-sheer-drapery-corner-window.webp', title: 'Corner Window Sheers' },
  { img: '/images/new/commercial-velvet-drapery-sheers-installation.webp', title: 'Commercial Drapery & Sheers' },
  { img: '/images/new/custom-kitchen-banquette-seating.webp', title: 'Kitchen Banquette' },
  { img: '/images/new/dark-plantation-shutters-modern-kitchen.webp', title: 'Dark Kitchen Shutters' },
  { img: '/images/new/crystal-finial-drapery-rod.webp', title: 'Crystal Drapery Finial' },
  { img: '/images/new/sheer-ripple-fold-drapery-bedroom.webp', title: 'Ripple-Fold Sheers' },
  { img: '/images/new/custom-bedding-four-poster-bedroom.webp', title: 'Custom Bedroom Bedding' },
  { img: '/images/new/custom-decorative-bedding-pillows-bolster.webp', title: 'Custom Pillows & Bolster' },
  { img: '/images/new/custom-floral-upholstered-cornice.webp', title: 'Floral Upholstered Cornice' },
  { img: '/images/new/zebra-shades-custom-drapery-slider.webp', title: 'Zebra Shades & Drapery' },
  { img: '/images/new/window-treatment3.webp', title: 'Shutters with Drapery' },
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
  { img: '/images/new/commercial-drapery-consultation-suite.webp', title: 'Consultation Suite Drapery' },
  { img: '/images/new/custom-blinds-and-window-shades.webp', title: 'Blinds & Shades' },
  { img: '/images/new/outdoor-window-shades.webp', title: 'Outdoor Window Shades' },
  { img: '/images/new/cornices-and-valances.webp', title: 'Cornices & Valances' },
  { img: '/images/new/navy-blue-valance-geometric-drapery-panels.webp', title: 'Navy Valance & Geometric Panels' },
  { img: '/images/new/custom-kitchen-banquette-seating.webp', title: 'Custom Banquette Seating' },
  { img: '/images/gallery/custom-upholstery-gallery.webp', title: 'Recovered Dining Chairs' },
  { img: '/images/new/custom-bedding-four-poster-bedroom.webp', title: 'Custom Bedding' },
  { img: '/images/new/custom-decorative-bedding-pillows-bolster.webp', title: 'Bedding & Pillows' },
  { img: '/images/new/commercial-velvet-drapery-sheers-installation.webp', title: 'Commercial Window Treatments' },
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
