// All published Google reviews for Custom Fabric Creations.
// Suzanne Rice (rating only, no body) intentionally excluded per client
// decision 2026-05-20: only reviews with written content are surfaced.
// Dates derived from "X weeks ago" values captured on 2026-05-20.

export type ReviewTag =
  | 'plantation-shutters'
  | 'custom-draperies-curtains'
  | 'window-shades'
  | 'custom-blinds'
  | 'custom-cornices-valances'
  | 'drapery-hardware'
  | 'outdoor-window-shades'
  | 'furniture-reupholstery'
  | 'custom-bedding-pillows'
  | 'custom-banquettes'
  | 'commercial-window-treatments'
  | 'services-interior-decor-tampa'
  | 'motorized'
  | 'whole-home'
  | 'budget'
  | 'design-guidance'
  | 'repeat-client'
  | 'general';

export interface Review {
  id: string;
  name: string;
  initials: string;
  avatar?: string;
  avatarColor: string;
  // ISO date (YYYY-MM-DD) when the review was posted.
  dateISO: string;
  // Pre-formatted display date for cards (e.g., "Jan 2026" for recent,
  // "Apr 2023" for older). Calculated relative to 2026-05-20 capture.
  dateLabel: string;
  rating: 1 | 2 | 3 | 4 | 5;
  body: string;
  source: 'Google';
  tags: ReviewTag[];
  // Optional neighborhood/area attribution. Only set when explicitly stated
  // or strongly implied by the review content; otherwise omitted.
  area?: string;
  // True for the single review that should appear as the large featured
  // card by default.
  featured?: boolean;
}

export const REVIEWS: Review[] = [
  {
    id: 'patty-profeto',
    name: 'Patty Profeto',
    initials: 'PP',
    avatarColor: 'rgb(217, 119, 54)',
    dateISO: '2025-10-17',
    dateLabel: '7 months ago',
    rating: 5,
    body: "I have been working with Terry and her team for years. Very talented decorator with beautiful and unique designs. The quality of her products is superior. I love working with her on my projects because she listens to what I want to do and goes far past my expectations. Just a true delight to work with. The best part: she always stayed in my budget for every project.",
    source: 'Google',
    tags: ['repeat-client', 'design-guidance', 'budget', 'general'],
    featured: true,
  },
  {
    id: 'beth-mccarthy',
    name: 'Beth McCarthy',
    initials: 'BM',
    avatar: '/images/reviews/beth-mccarthy.png',
    avatarColor: 'rgb(82, 140, 158)',
    dateISO: '2026-01-22',
    dateLabel: 'Jan 2026',
    rating: 5,
    body: 'Terry and team did an amazing job reupholstering my 10-1/2 foot bench. The quality of work, communication, and speed were A++. Thank you!',
    source: 'Google',
    tags: ['furniture-reupholstery', 'custom-banquettes'],
  },
  {
    id: 'florence-perez-arriaga',
    name: 'Florence Perez Arriaga',
    initials: 'FP',
    avatar: '/images/reviews/florence-perez-arriaga.png',
    avatarColor: 'rgb(120, 78, 163)',
    dateISO: '2025-10-10',
    dateLabel: '7 months ago',
    rating: 5,
    body: "I've used Custom Fabric Creations several times for drapes, cornices, and a remote shade. The custom work around my already existing crown molding was amazing. Anytime I need window treatments I would use them again.",
    source: 'Google',
    tags: ['custom-draperies-curtains', 'custom-cornices-valances', 'window-shades', 'motorized', 'repeat-client'],
  },
  {
    id: 'rhonda-bellet',
    name: 'Rhonda Bellet',
    initials: 'RB',
    avatarColor: 'rgb(38, 92, 128)',
    dateISO: '2025-10-10',
    dateLabel: '7 months ago',
    rating: 5,
    body: "I've known Terry for 20+ years. Her commitment to quality craftsmanship and attention to detail is unmatched. Her ability to tailor designs to meet specific aesthetic and functional needs ensures every project fits client expectations perfectly. The team's professionalism, from consultation to installation, reflects their dedication to customer satisfaction. Custom Fabric Creations is an outstanding choice.",
    source: 'Google',
    tags: ['repeat-client', 'design-guidance', 'general'],
  },
  {
    id: 'dayna-middlebrooks',
    name: 'Dayna Middlebrooks',
    initials: 'DM',
    avatarColor: 'rgb(180, 83, 9)',
    dateISO: '2025-10-10',
    dateLabel: '7 months ago',
    rating: 5,
    body: 'Terry designed a banquette for my curved eat-in kitchen. We had many options for fabric color and design, and she guided me through the assortment with care to make sure I would love it. And I do!',
    source: 'Google',
    tags: ['custom-banquettes', 'design-guidance'],
  },
  {
    id: 'amy-monroe',
    name: 'Amy Monroe',
    initials: 'AM',
    avatarColor: 'rgb(234, 179, 8)',
    dateISO: '2025-10-10',
    dateLabel: '7 months ago',
    rating: 5,
    body: "Terry was a blast and very professional. I had her and her team make custom curtains for my mom's outdoor sitting area. She came over and helped us go through fabric choices. In the end my mom is very pleased. I would recommend them.",
    source: 'Google',
    tags: ['custom-draperies-curtains', 'outdoor-window-shades', 'design-guidance'],
  },
  {
    id: 'x-v',
    name: 'X V',
    initials: 'XV',
    avatar: '/images/reviews/x-v.png',
    avatarColor: 'rgb(82, 140, 158)',
    dateISO: '2025-10-10',
    dateLabel: '7 months ago',
    rating: 5,
    body: 'Terry is always a pleasure to work with and my home has never looked better!',
    source: 'Google',
    tags: ['general', 'repeat-client'],
  },
  {
    id: 'darlyn-huto',
    name: 'Darlyn Huto',
    initials: 'DH',
    avatarColor: 'rgb(120, 78, 163)',
    dateISO: '2025-10-10',
    dateLabel: '7 months ago',
    rating: 5,
    body: 'I just had Terry at Custom Fabric Creations make draperies for the glass sliders in my living room and kitchen area. I would like to thank her. She did an excellent job. She worked with me to find what I would like and the wait time was right on schedule. I would definitely recommend her to anyone.',
    source: 'Google',
    tags: ['custom-draperies-curtains', 'design-guidance'],
  },
  {
    id: 'john',
    name: 'John',
    initials: 'J',
    avatarColor: 'rgb(38, 92, 128)',
    dateISO: '2025-10-03',
    dateLabel: '7 months ago',
    rating: 5,
    body: 'Terry and her team are fantastic to work with, from design to installation. She is very creative and has an excellent talent for design with an almost limitless selection of colors, patterns, and options. With her help we were able to develop a custom solution for each room in our house. Everything turned out just as she had designed and planned!',
    source: 'Google',
    tags: ['whole-home', 'design-guidance', 'general'],
  },
  {
    id: 'abigail-stockman',
    name: 'Abigail Stockman',
    initials: 'AS',
    avatar: '/images/reviews/abigail-stockman.png',
    avatarColor: 'rgb(217, 119, 54)',
    dateISO: '2025-07-25',
    dateLabel: '10 months ago',
    rating: 5,
    body: "We love our custom shades! Terry is a master at what she does and she's a pleasure to work with. We needed a custom shower curtain with a fun pattern, an extra large motorized shade for a Nana door, and a roller shade for a floor-to-ceiling window. Terry made it happen and everything turned out flawless.",
    source: 'Google',
    tags: ['window-shades', 'motorized', 'custom-bedding-pillows'],
  },
  {
    id: 'barbara-staras',
    name: 'Barbara Staras',
    initials: 'BS',
    avatarColor: 'rgb(180, 83, 9)',
    dateISO: '2023-04-13',
    dateLabel: 'Apr 2023',
    rating: 5,
    body: "Terry made drapes for my entire house. Her work is flawless. The choice of fabrics is limitless. I moved from Atlanta, where access to quality, custom draperies was plentiful. Terry's work is as good, if not better, than the drapery makers I encountered in Atlanta. I highly recommend Terry.",
    source: 'Google',
    tags: ['custom-draperies-curtains', 'whole-home'],
  },
  {
    id: 'rena-cantway',
    name: 'Rena R. Cantway',
    initials: 'RC',
    avatarColor: 'rgb(82, 140, 158)',
    dateISO: '2018-05-27',
    dateLabel: 'May 2018',
    rating: 5,
    body: 'I have worked with and known Terry as a friend for 10 years. She is very creative and does awesome quality work. I have seen many of the drapery and bedding packages she has sewn and they are beautiful and amazing. She has incredible design talent and helps her customers choose the best for their home.',
    source: 'Google',
    tags: ['custom-draperies-curtains', 'custom-bedding-pillows', 'design-guidance'],
  },
  {
    id: 'darla-priest',
    name: 'Darla Priest',
    initials: 'DP',
    avatarColor: 'rgb(120, 78, 163)',
    dateISO: '2018-04-11',
    dateLabel: 'Apr 2018',
    rating: 5,
    body: 'I have done a few projects with Terry and have been pleased every time. She is professional and has a great sense of style when putting it all together. Whether you need one room or a whole house, Terry will guide you to the right choices of fabric and style, all in a timely manner.',
    source: 'Google',
    tags: ['repeat-client', 'design-guidance', 'whole-home'],
  },
  {
    id: 'diane-teska',
    name: 'Diane Teska',
    initials: 'DT',
    avatarColor: 'rgb(217, 119, 54)',
    dateISO: '2018-03-08',
    dateLabel: 'Mar 2018',
    rating: 5,
    body: 'I had plantation shutters installed in my home and it was a pleasure to do business with Terry. She is an expert decorator and made excellent recommendations. The shutters were delivered on the date we agreed on and her husband did an excellent job on the installation. The shutters are a beautiful addition to my home. I wholeheartedly recommend Custom Fabric Creations.',
    source: 'Google',
    tags: ['plantation-shutters', 'design-guidance'],
  },
  {
    id: 'joann-johnson',
    name: 'JoAnn Johnson',
    initials: 'JJ',
    avatar: '/images/reviews/joann-johnson.png',
    avatarColor: 'rgb(38, 92, 128)',
    dateISO: '2018-03-08',
    dateLabel: 'Mar 2018',
    rating: 5,
    body: 'Terry is a pleasure to work with. She listened patiently to what I wanted to do, helped to keep me within budget, and her work is of the highest quality. A+',
    source: 'Google',
    tags: ['budget', 'design-guidance', 'general'],
  },
  {
    id: 'bonnie-farr',
    name: 'Bonnie Farr',
    initials: 'BF',
    avatarColor: 'rgb(180, 83, 9)',
    dateISO: '2018-03-07',
    dateLabel: 'Mar 2018',
    rating: 5,
    body: 'Terry is an amazing talent. She brings her expertise and style to all projects. I have used her multiple times and recommend her to everyone I know.',
    source: 'Google',
    tags: ['repeat-client', 'general'],
  },
];

// Helpers for downstream components.

export function getFeaturedReview(): Review {
  return REVIEWS.find((r) => r.featured) ?? REVIEWS[0];
}

export function getReviewsByTag(tag: ReviewTag, limit = 3): Review[] {
  return REVIEWS.filter((r) => r.tags.includes(tag)).slice(0, limit);
}

// Sorted most-recent first, used for the carousel + grid rows.
export function getReviewsByRecency(limit?: number): Review[] {
  const sorted = [...REVIEWS].sort((a, b) => b.dateISO.localeCompare(a.dateISO));
  return limit ? sorted.slice(0, limit) : sorted;
}
