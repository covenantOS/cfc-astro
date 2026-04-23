# SEO Audit Fixes — 2026-04-23 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement all P0, P1, and P2 items from `_seo/AUDIT-2026-04-23.md` before DNS cutover.

**Architecture:** Targeted edits across content MD files, layout/component `.astro` files, and `public/` static assets — no new routing patterns or dependencies required. Tasks are batched by priority (P0 blockers first) then by file proximity.

**Tech Stack:** Astro 5 (content collections, static pages), TypeScript, Tailwind CSS, Cloudflare Pages. Build command: `npm run build` from `cfc-astro/`. All commands run from `cfc-astro/` unless noted.

---

## ⚠️ Pre-Flight: Operator Confirmations Required Before P1 Work

Before starting Tasks 6–12, get answers to these from the site owner:

1. **Business hours** — Four sources conflict. Which is canonical?
   - `site.ts`: Mon–Sat 9:00am–5:00pm
   - `Schema.astro`: Mon–Sat 09:00–17:00 (same as above, different format)
   - Live WP footer: Mon–Fri 7am–5pm, Sat–Sun 8am–5pm
   - West St. Pete memory: Mon–Sat 8am–8pm, closed Sun
   - **Action needed:** Confirm one set of hours for `site.ts` + `Schema.astro`. Note if West St. Pete has different hours.

2. **`sameAs` URLs** — Need the exact URLs for: Google Business Profile, Facebook page, Yelp listing, Houzz profile. Without these, Task 6 leaves `sameAs: []` as a stub.

3. **Brands decision** (Task 11) — Live WP shows 7 brands; Astro has 5. Three brand logos already exist in `public/images/brands/`: `ALTA Window Fashions.webp`, `Elegant Shutters.webp`, `Horizon Window Fashions.webp`. Decision: add all 3 back? Keep Graber or drop it?

---

## File Map

| File | Tasks |
|---|---|
| `src/content/services/*.md` (7 files) | T1, T5, T7, T9 |
| `src/content/areas/*.md` (14 files) | T1, T8 |
| `src/layouts/BaseLayout.astro` | T2, T13 |
| `src/pages/plantation-shutters-cost-st-petersburg.astro` | T3 |
| `src/pages/about.astro` | T4 |
| `src/pages/index.astro` | T4 |
| `src/components/Schema.astro` | T6, T13 |
| `src/layouts/ServiceLayout.astro` | T10 |
| `src/pages/brands.astro` | T11 |
| `public/_headers` | T12 (new) |
| `public/llms.txt` | T14 (new) |
| `public/robots.txt` | T16 |
| `src/pages/guides/index.astro` | T17 (new) |

---

## Task 1: Fix 15 Truncated Meta Descriptions (P0)

**Files:**
- Modify: `src/content/services/plantation-shutters.md`
- Modify: `src/content/services/custom-banquettes.md`
- Modify: `src/content/services/drapery-hardware.md`
- Modify: `src/content/services/window-shades.md`
- Modify: `src/content/services/custom-cornices-valances.md`
- Modify: `src/content/services/custom-bedding-pillows.md`
- Modify: `src/content/services/outdoor-window-shades.md`
- Modify: `src/content/areas/west-st-pete.md`
- Modify: `src/content/areas/belleair-shore.md`
- Modify: `src/content/areas/old-northeast.md`
- Modify: `src/content/areas/downtown-st-pete.md`
- Modify: `src/content/areas/snell-isle.md`
- Modify: `src/content/areas/tierra-verde.md`
- Modify: `src/content/areas/st-pete-beach.md`
- Modify: `src/content/areas/treasure-island.md`

- [ ] **Step 1: Apply corrected descriptions to all 15 files**

  Apply each description replacement exactly as shown. Every current (broken) value and its replacement:

  **`src/content/services/plantation-shutters.md`**
  ```
  OLD: "Custom plantation shutters in St. Petersburg, FL. Faux wood & basswood built for Florida humidity, Gulf sun, hurricane season. Free consultation. across."
  NEW: "Custom plantation shutters in St. Petersburg, FL. Faux wood and basswood built for Florida humidity, Gulf sun, and hurricane season. Free consultation across Pinellas County."
  ```

  **`src/content/services/custom-banquettes.md`**
  ```
  OLD: "."
  NEW: "Custom banquettes in St. Petersburg, FL. Built-in seating upholstered in premium performance fabrics for residential dining rooms and commercial spaces. Free consultation."
  ```

  **`src/content/services/drapery-hardware.md`**
  ```
  OLD: "Drapery hardware supply & installation in St. Petersburg. Decorative rods, concealed tracks, motorized systems & custom bay window hardware. Built for."
  NEW: "Drapery hardware supply and installation in St. Petersburg. Decorative rods, concealed tracks, motorized systems, and custom bay window hardware built for Florida homes."
  ```

  **`src/content/services/window-shades.md`**
  ```
  OLD: "Custom window shades in St. Petersburg built for Florida's sun & humidity. Roller, roman, solar, cellular & blackout shades by Hunter Douglas, Graber &."
  NEW: "Custom window shades in St. Petersburg built for Florida's sun and humidity. Roller, roman, solar, cellular, and blackout shades by Hunter Douglas, Graber, and Norman."
  ```

  **`src/content/services/custom-cornices-valances.md`**
  ```
  OLD: "Custom cornices & valances in St. Petersburg, built to your exact window dimensions. Fabric valances, box cornices & coordinated top treatments. Free."
  NEW: "Custom cornices and valances in St. Petersburg built to your exact window dimensions. Fabric valances, box cornices, and coordinated top treatments. Free consultation."
  ```

  **`src/content/services/custom-bedding-pillows.md`**
  ```
  OLD: "Custom bedding made to your exact bed dimensions in St. Petersburg. Duvet covers, pillow shams, accent pillows & custom cushions. Fabric coordinated with."
  NEW: "Custom bedding made to your exact bed dimensions in St. Petersburg. Duvet covers, pillow shams, accent pillows, and custom cushions. Fabric coordinated with your space."
  ```

  **`src/content/services/outdoor-window-shades.md`**
  ```
  OLD: "Outdoor window shades & exterior treatments for St. Petersburg homes. Solar screens, patio shades, outdoor curtains & screen enclosures built for."
  NEW: "Outdoor window shades and exterior treatments for St. Petersburg homes. Solar screens, patio shades, outdoor curtains, and screen enclosures built for Florida's coast."
  ```

  **`src/content/areas/west-st-pete.md`**
  ```
  OLD: "West St. Petersburg's premier blinds shop offering custom plantation shutters, blinds, shades & motorized blinds. Free consultations. Serving Pinellas."
  NEW: "West St. Petersburg's premier blinds shop offering custom plantation shutters, blinds, shades, and motorized treatments. Free consultations. Serving Pinellas County."
  ```

  **`src/content/areas/belleair-shore.md`**
  ```
  OLD: "Belleair Shore FL's premier blinds shop offering custom plantation shutters, exterior solar shades & luxury bedding. Furniture re-upholstery & motorized."
  NEW: "Belleair Shore FL's premier blinds shop offering custom plantation shutters, exterior solar shades, and luxury bedding. Furniture reupholstery and motorized options available."
  ```

  **`src/content/areas/old-northeast.md`**
  ```
  OLD: "Old Northeast St. Petersburg's trusted blinds shop offering custom plantation shutters, blackout curtains, roller & roman shades. Professional motorized."
  NEW: "Old Northeast St. Petersburg's trusted blinds shop offering custom plantation shutters, blackout curtains, and roller and roman shades. Professional motorized installation."
  ```

  **`src/content/areas/downtown-st-pete.md`**
  ```
  OLD: "Downtown St. Petersburg's premier blinds shop offering solar shades for heat control, blackout roller shades & luxury custom window treatments. Motorized."
  NEW: "Downtown St. Petersburg's premier blinds shop offering solar shades for heat control, blackout roller shades, and luxury custom window treatments. Motorized options available."
  ```

  **`src/content/areas/snell-isle.md`**
  ```
  OLD: "Snell Isle's premier blinds shop offering roller shades, motorized window treatments & custom plantation shutters. Professional installation. Free."
  NEW: "Snell Isle's premier blinds shop offering roller shades, motorized window treatments, and custom plantation shutters. Professional installation. Free consultation."
  ```

  **`src/content/areas/tierra-verde.md`**
  ```
  OLD: "Tierra Verde FL's premier blinds shop offering exterior solar shades, custom bedding, plantation shutters & furniture re-upholstery. Motorized."
  NEW: "Tierra Verde FL's premier blinds shop offering exterior solar shades, custom bedding, plantation shutters, and furniture reupholstery. Motorized options available."
  ```

  **`src/content/areas/st-pete-beach.md`**
  ```
  OLD: "St. Pete Beach FL's premier blinds shop offering blackout roman shades, motorized exterior shades & luxury drapery. UV protection window fashions. Free."
  NEW: "St. Pete Beach FL's premier blinds shop offering blackout roman shades, motorized exterior shades, and luxury drapery. UV protection window fashions. Free consultation."
  ```

  **`src/content/areas/treasure-island.md`**
  ```
  OLD: "Treasure Island FL's premier blinds shop offering composite plantation shutters, blackout roman shades & commercial motorized blinds. Luxury bedding &."
  NEW: "Treasure Island FL's premier blinds shop offering composite plantation shutters, blackout roman shades, and motorized blinds. Luxury bedding and custom cushions."
  ```

- [ ] **Step 2: Verify build passes and no descriptions end with "."**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -5
  grep -r "content=\"\." dist/ | grep "meta name=\"description\"" | head -5
  ```
  Expected: build exits 0, grep returns nothing.

- [ ] **Step 3: Spot-check a few description tags in built HTML**

  ```bash
  grep 'meta name="description"' dist/services/plantation-shutters/index.html
  grep 'meta name="description"' dist/services/custom-banquettes/index.html
  grep 'meta name="description"' dist/areas/west-st-pete/index.html
  ```
  Expected: All three show complete sentences that do not end with "&", "for.", "with.", etc.

- [ ] **Step 4: Commit**

  ```bash
  git add src/content/services/plantation-shutters.md \
    src/content/services/custom-banquettes.md \
    src/content/services/drapery-hardware.md \
    src/content/services/window-shades.md \
    src/content/services/custom-cornices-valances.md \
    src/content/services/custom-bedding-pillows.md \
    src/content/services/outdoor-window-shades.md \
    src/content/areas/west-st-pete.md \
    src/content/areas/belleair-shore.md \
    src/content/areas/old-northeast.md \
    src/content/areas/downtown-st-pete.md \
    src/content/areas/snell-isle.md \
    src/content/areas/tierra-verde.md \
    src/content/areas/st-pete-beach.md \
    src/content/areas/treasure-island.md
  git commit -m "fix: repair 15 truncated meta descriptions across service and area pages"
  ```

---

## Task 2: Fix OG Image Default 404 (P0)

**Files:**
- Modify: `src/layouts/BaseLayout.astro:30`

The file `/images/og-default.jpg` doesn't exist in `public/`. Rather than copying a file, point the default at `/images/hero/homepage.webp` which exists and is 1200+ wide.

- [ ] **Step 1: Update default ogImage in BaseLayout.astro**

  In `src/layouts/BaseLayout.astro`, change line 30:
  ```diff
  -  ogImage = '/images/og-default.jpg',
  +  ogImage = '/images/hero/homepage.webp',
  ```

- [ ] **Step 2: Verify build and confirm no 404 on default**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -3
  grep 'og:image' dist/about/index.html
  grep 'og:image' dist/contact/index.html
  grep 'og:image' dist/brands/index.html
  ```
  Expected: All three show `og:image` pointing to `https://www.customfabriccreations.net/images/hero/homepage.webp` and that file exists at `public/images/hero/homepage.webp`.

- [ ] **Step 3: Commit**

  ```bash
  git add src/layouts/BaseLayout.astro
  git commit -m "fix: replace missing og-default.jpg with existing hero image"
  ```

---

## Task 3: Fix Pricing Table on Cost Guide (P0)

**Files:**
- Modify: `src/pages/plantation-shutters-cost-st-petersburg.astro:41`

Line 41 renders the table data as a single `<p>` blob. Replace it with a proper `<table>`.

- [ ] **Step 1: Replace the prose blob with an HTML table**

  In `src/pages/plantation-shutters-cost-st-petersburg.astro`, find and replace the paragraph starting with `<p>Window sizeSq ft...` (line 41) with:

  ```html
  <div class="overflow-x-auto my-8">
    <table class="w-full text-sm border-collapse">
      <thead>
        <tr class="bg-cream-50">
          <th class="border border-line px-4 py-3 text-left font-semibold text-ink-800">Window size</th>
          <th class="border border-line px-4 py-3 text-left font-semibold text-ink-800">Sq ft</th>
          <th class="border border-line px-4 py-3 text-left font-semibold text-ink-800">Faux wood (low end)</th>
          <th class="border border-line px-4 py-3 text-left font-semibold text-ink-800">Hybrid / premium faux</th>
          <th class="border border-line px-4 py-3 text-left font-semibold text-ink-800">Basswood (real wood)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="border border-line px-4 py-3 text-ink-700">Small (24″ × 36″)</td>
          <td class="border border-line px-4 py-3 text-ink-700">6</td>
          <td class="border border-line px-4 py-3 text-ink-700">$150 to $210</td>
          <td class="border border-line px-4 py-3 text-ink-700">$240 to $300</td>
          <td class="border border-line px-4 py-3 text-ink-700">$300 to $360</td>
        </tr>
        <tr class="bg-cream-50/40">
          <td class="border border-line px-4 py-3 text-ink-700">Standard bedroom (36″ × 48″)</td>
          <td class="border border-line px-4 py-3 text-ink-700">12</td>
          <td class="border border-line px-4 py-3 text-ink-700">$300 to $420</td>
          <td class="border border-line px-4 py-3 text-ink-700">$480 to $600</td>
          <td class="border border-line px-4 py-3 text-ink-700">$600 to $720</td>
        </tr>
        <tr>
          <td class="border border-line px-4 py-3 text-ink-700">Living room (48″ × 60″)</td>
          <td class="border border-line px-4 py-3 text-ink-700">20</td>
          <td class="border border-line px-4 py-3 text-ink-700">$500 to $700</td>
          <td class="border border-line px-4 py-3 text-ink-700">$800 to $1,000</td>
          <td class="border border-line px-4 py-3 text-ink-700">$1,000 to $1,200</td>
        </tr>
        <tr class="bg-cream-50/40">
          <td class="border border-line px-4 py-3 text-ink-700">Large picture (72″ × 60″)</td>
          <td class="border border-line px-4 py-3 text-ink-700">30</td>
          <td class="border border-line px-4 py-3 text-ink-700">$750 to $1,050</td>
          <td class="border border-line px-4 py-3 text-ink-700">$1,200 to $1,500</td>
          <td class="border border-line px-4 py-3 text-ink-700">$1,500 to $1,800</td>
        </tr>
        <tr>
          <td class="border border-line px-4 py-3 text-ink-700">French door (single panel)</td>
          <td class="border border-line px-4 py-3 text-ink-700">8 to 10</td>
          <td class="border border-line px-4 py-3 text-ink-700">$240 to $350</td>
          <td class="border border-line px-4 py-3 text-ink-700">$400 to $500</td>
          <td class="border border-line px-4 py-3 text-ink-700">$500 to $600</td>
        </tr>
      </tbody>
    </table>
  </div>
  ```

- [ ] **Step 2: Verify build and check the page renders a table**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -3
  grep -c '<table' dist/plantation-shutters-cost-st-petersburg/index.html
  ```
  Expected: build passes, grep returns `1`.

- [ ] **Step 3: Commit**

  ```bash
  git add src/pages/plantation-shutters-cost-st-petersburg.astro
  git commit -m "fix: convert pricing table from prose blob to HTML table"
  ```

---

## Task 4: Wire FAQ Props in about.astro and index.astro (P0)

**Files:**
- Modify: `src/pages/about.astro`
- Modify: `src/pages/index.astro`

`about.astro` defines `ABOUT_FAQS` (4 items) and renders `<FAQ items={ABOUT_FAQS} />`, but never passes `faqs` to `BaseLayout` — so Schema.astro never sees them. Same pattern on homepage where `<FAQ />` uses DEFAULT_ITEMS but BaseLayout gets no `faqs` prop.

- [ ] **Step 1: Add faqs prop to about.astro BaseLayout**

  In `src/pages/about.astro`, find the `<BaseLayout` block (starts at line 40) and add `faqs={ABOUT_FAQS}`:

  ```diff
   <BaseLayout
     title="About Custom Fabric Creations"
     description="St. Petersburg's premier studio for bespoke window treatments and upholstery since 2000. Locally owned, fully insured, in-house workroom."
     pageType="about"
     breadcrumbs={[{ name: 'Home', url: '/' }, { name: 'About', url: '/about/' }]}
  +  faqs={ABOUT_FAQS}
   >
  ```

- [ ] **Step 2: Add faqs prop to index.astro BaseLayout**

  The homepage `<FAQ />` uses 5 default items hardcoded inside the component. Add those same 5 items to BaseLayout so Schema.astro emits them as JSON-LD.

  In `src/pages/index.astro`, add a `HOME_FAQS` const before the `---` closing fence (in the frontmatter block), then pass it:

  ```diff
  +const HOME_FAQS = [
  +  { q: 'How does the design consultation work?', a: 'We bring our premium fabric library directly to your house. This allows you to evaluate textures and colors in your actual room lighting. Our designers measure your windows precisely and help you select the perfect materials for your space.' },
  +  { q: 'How long does it take to receive custom window treatments?', a: 'Fabrication timelines depend on the specific materials and brands selected. Because every piece is meticulously tailored to your exact measurements, most projects are completed and ready for white-glove installation within four to eight weeks.' },
  +  { q: 'What brands and materials do you carry?', a: 'We are an authorized dealer for the most respected names in interior design, including Hunter Douglas, Norman, Kravet, Graber, and Stout. You receive exclusive access to premium textiles and advanced motorized shade technology.' },
  +  { q: 'Do you charge for the initial consultation?', a: 'No. We offer a complimentary initial design consultation for homeowners in St. Pete and across Pinellas County. We bring samples to your home so you can see them in your actual space and lighting.' },
  +  { q: 'Do you handle installation?', a: 'Yes. Installation is done by our own team, never a subcontractor. We handle the full white-glove process from measurement to final fit.' },
  +];
   ---
   
   <BaseLayout
     title={SITE.name}
     description="St. Pete's premier studio for bespoke window treatments, drapery, shutters, and upholstery. 25+ years of craftsmanship. Free consultations."
     pageType="home"
     ogImage="/images/hero/homepage.webp"
  +  faqs={HOME_FAQS}
   >
  ```

- [ ] **Step 3: Verify FAQPage JSON-LD emits on both pages**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -3
  grep -o '"@type":"FAQPage"' dist/about/index.html
  grep -o '"@type":"FAQPage"' dist/index.html
  ```
  Expected: both greps return `"@type":"FAQPage"`.

- [ ] **Step 4: Commit**

  ```bash
  git add src/pages/about.astro src/pages/index.astro
  git commit -m "fix: wire faqs prop to BaseLayout on about and home pages for FAQPage schema"
  ```

---

## Task 5: Add FAQ Frontmatter to plantation-shutters.md (P0)

**Files:**
- Modify: `src/content/services/plantation-shutters.md`

The file already has 10 FAQ H3s in body prose (lines 185–243). Port them into structured `faqs:` frontmatter so `[slug].astro` can pass them to Schema via `data.faqs`. Keep the prose H3s in the body for visual rendering — the schema FAQs are additive.

- [ ] **Step 1: Add faqs frontmatter block**

  In `src/content/services/plantation-shutters.md`, inside the YAML front matter (between the `---` fences), add the following after the `type: service` line:

  ```yaml
  faqs:
    - q: "Are plantation shutters good for Florida humidity?"
      a: "Yes, especially faux wood shutters, which are designed to resist moisture absorption. Real wood can absorb humidity and swell, but faux wood holds its dimensions in high-humidity conditions. We recommend faux wood as the default for most St. Pete windows."
    - q: "What's the difference between plantation shutters and regular interior shutters?"
      a: "Plantation shutters feature wider louvers than traditional interior shutters, which gives better light control and a cleaner architectural look. Most shutters sold today in Florida are plantation style, typically with 2.5-inch, 3.5-inch, or 4.5-inch louvers."
    - q: "Can plantation shutters help with energy efficiency in Florida?"
      a: "Yes. The louver system lets you redirect light without direct sun entering the room, reducing heat gain. Faux wood also provides some insulating value. Combined with Florida's high AC usage, this can meaningfully reduce cooling costs on sun-exposed windows."
    - q: "How long do plantation shutters last in Tampa Bay?"
      a: "Quality faux wood plantation shutters, properly installed, typically last 15–20 years in Florida conditions. Key factors are material quality, installation quality, and the amount of direct sun exposure. Real wood lasts 8–12 years in humid coastal conditions."
    - q: "What's better — faux wood or real wood shutters?"
      a: "For most St. Pete homeowners, faux wood is the better choice. It handles humidity better, resists UV damage, and costs less. Real wood is appropriate when the aesthetic is specifically desired and the homeowner can maintain it in a climate-controlled room."
    - q: "How much do plantation shutters cost in St. Petersburg?"
      a: "In St. Pete, plantation shutters typically run $25–$60 per square foot installed, depending on material, louver size, and specialty shapes. A standard bedroom window runs roughly $375–$900 for faux wood, or $550–$1,400 for custom-stained basswood."
    - q: "What's the downside of plantation shutters?"
      a: "Three honest trade-offs: upfront cost is 2–4× comparable blinds; closed louvers still admit some light, so true blackout rooms need a shade behind; and custom manufacturing takes 3–6 weeks versus same-day big-box stock."
    - q: "Are plantation shutters still in style in 2026?"
      a: "Yes. Plantation shutters have become a neutral design baseline that works with coastal modern, transitional, Mediterranean revival, and mid-century styles — every major St. Pete architectural style. The 2026 update is wider 3.5–4.5-inch louvers and motorized tilt."
    - q: "Do plantation shutters add home value in St. Petersburg?"
      a: "Yes. Pinellas realtors consistently list plantation shutters as a high-ROI interior upgrade, with typical recovery of 70–90% of install cost at resale. Homes with custom shutters often appraise $5,000–$15,000 higher than comparable homes with standard blinds."
    - q: "What's a cheaper option than plantation shutters in St. Petersburg?"
      a: "Solar shades, cellular (honeycomb) blinds, or faux wood 2.5-inch blinds all run $150–$400 per window installed versus $300–$1,200 for plantation shutters. Blinds and shades typically need replacement every 5–8 years in Florida conditions; shutters last 15–20 years."
  ```

- [ ] **Step 2: Verify FAQPage schema emits on the service page**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -3
  grep -o '"@type":"FAQPage"' dist/services/plantation-shutters/index.html
  ```
  Expected: returns `"@type":"FAQPage"`.

- [ ] **Step 3: Commit**

  ```bash
  git add src/content/services/plantation-shutters.md
  git commit -m "feat: add FAQ frontmatter to plantation-shutters for FAQPage schema"
  ```

---

## Task 6: Fix LocalBusiness Schema (P1)

> **Pre-flight dependency:** Confirm correct business hours and sameAs URLs with operator before this task.

**Files:**
- Modify: `src/components/Schema.astro`

Four changes in one file: fix address (street + zip), add AggregateRating, add founder, add sameAs, fix West St. Pete area phone.

- [ ] **Step 1: Fix address in the localBusiness node**

  In `src/components/Schema.astro`, find the `address` block inside `localBusiness` (~line 56) and update:

  ```diff
   address: {
     '@type': 'PostalAddress',
  +  streetAddress: '3026 Central Ave Ste 551',
     addressLocality: 'St. Petersburg',
     addressRegion: 'FL',
  -  postalCode: '33701',
  +  postalCode: '33712',
     addressCountry: 'US',
   },
  ```

  Also update the standalone `place` node (~line 116) to match:
  ```diff
   address: {
     '@type': 'PostalAddress',
  +  streetAddress: '3026 Central Ave Ste 551',
     addressLocality: 'St. Petersburg',
     addressRegion: 'FL',
  -  postalCode: '33701',
  +  postalCode: '33712',
     addressCountry: 'US',
   },
  ```

- [ ] **Step 2: Add AggregateRating and founder to localBusiness**

  Inside the `localBusiness` object (after the `image` property at the bottom, before the closing `};`), add:

  ```diff
   image: {
     '@type': 'ImageObject',
     url: logoUrl,
     caption: SITE.name,
   },
  +aggregateRating: {
  +  '@type': 'AggregateRating',
  +  ratingValue: '4.9',
  +  reviewCount: '100',
  +  bestRating: '5',
  +  worstRating: '1',
  +},
  +founder: {
  +  '@type': 'Person',
  +  name: 'Terry Popick',
  +},
  +sameAs: [
  +  // TODO: operator to supply GBP URL, Facebook, Yelp, Houzz
  +],
  ```

- [ ] **Step 3: Fix West St. Pete area phone override**

  In `src/components/Schema.astro`, inside the `pageType === 'area'` block (~line 167), the area LocalBusiness node always uses the main phone. Add an override for West St. Pete:

  First, destructure `areaSlug` from `Astro.props` — verify it's already destructured (it is, at line 31, but it's missing `areaSlug`). Check line 29–33 of Schema.astro:

  ```
  const {
    ...
    areaSlug,
    areaTitle,
    ...
  } = Astro.props;
  ```

  `areaSlug` is already in the interface but NOT destructured (look at line 29–33 — `areaSlug` is in `Props` interface but not in the destructuring). Add it:

  ```diff
   const {
     pageType,
     title,
     description,
     canonicalUrl,
     breadcrumbs = [],
     serviceSlug,
     serviceTitle,
  +  areaSlug,
     areaTitle,
     articleDate,
     faqs = [],
     image,
   } = Astro.props;
  ```

  Then update the area block:

  ```diff
   if (pageType === 'area' && areaTitle) {
     graph.push({
       '@type': 'LocalBusiness',
       '@id': `${canonicalUrl}#localbusiness`,
       name: `${SITE.name} — ${areaTitle}`,
       description,
       url: canonicalUrl,
       parentOrganization: { '@id': orgId },
       areaServed: { '@type': 'City', name: areaTitle },
  -    telephone: '+1-727-240-4512',
  +    telephone: areaSlug === 'west-st-pete' ? '+1-352-266-1262' : '+1-727-240-4512',
       priceRange: '$$$',
       address: {
         '@type': 'PostalAddress',
  +      ...(areaSlug === 'west-st-pete' && { streetAddress: '3026 Central Ave Ste 551' }),
         addressLocality: areaTitle,
         addressRegion: 'FL',
         addressCountry: 'US',
       },
     });
   }
  ```

- [ ] **Step 4: Verify schema in built HTML**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -3
  # Check address fix
  grep -o '"postalCode":"33712"' dist/index.html
  # Check AggregateRating
  grep -o '"@type":"AggregateRating"' dist/index.html
  # Check founder
  grep -o '"name":"Terry Popick"' dist/index.html
  # Check West St Pete phone
  grep -o '352-266-1262\|1-352-266-1262' dist/areas/west-st-pete/index.html
  ```
  Expected: all four greps return a match.

- [ ] **Step 5: Commit**

  ```bash
  git add src/components/Schema.astro
  git commit -m "fix: LocalBusiness address, AggregateRating, founder, West St Pete phone override"
  ```

---

## Task 7: Add FAQ Frontmatter to Remaining Service MDs (P1)

**Files:** All 11 service MDs except `plantation-shutters.md` (done in Task 5).

- [ ] **Step 1: Add faqs to each service MD**

  Add the following `faqs:` block inside each file's YAML frontmatter, after `type: service`.

  **`src/content/services/custom-draperies-curtains.md`**
  ```yaml
  faqs:
    - q: "How long does it take to get custom drapery made in St. Petersburg?"
      a: "Most custom drapery orders take 4–6 weeks from the signed proposal to installation. Timeline depends on fabric availability from our authorized suppliers (Kravet, Stout) and your chosen hardware. We give you a written timeline before we begin."
    - q: "Do you install drapery hardware or just the fabric?"
      a: "We handle everything — hardware selection, installation of rods and tracks, fabrication of the panels, and final hanging. Our in-house installers do not subcontract."
    - q: "What's the difference between drapery and curtains?"
      a: "Drapery refers to lined, structured window treatments that hang to the floor and are typically made from heavier fabrics. Curtains are lighter, often unlined, and can hang at any length. Both are custom-fabricated in our St. Pete workroom to your exact window dimensions."
    - q: "Can you match existing fabric or trim in my room?"
      a: "Yes. We bring our full Kravet and Stout fabric library to your home during the consultation and can match existing colors, patterns, and textures. For heritage or antique fabrics, we can coordinate a close match."
  ```

  **`src/content/services/window-shades.md`**
  ```yaml
  faqs:
    - q: "What window shades work best for Florida's intense sun?"
      a: "Solar shades with a 3–5% openness factor are the default for sun-facing windows in St. Pete. They block 95–97% of solar heat gain while preserving the view. For full privacy and blackout, cellular shades or roller shades with blackout fabric are the standard choice."
    - q: "Are Hunter Douglas shades worth the price in St. Petersburg?"
      a: "For most Pinellas homeowners, yes. Hunter Douglas Silhouette, Duette, and Alustra lines carry lifetime limited warranties and are built to handle Florida's UV load without yellowing or cord failure within a few years. The 20-year cost-per-year math usually favors Hunter Douglas over mid-grade alternatives."
    - q: "What is the difference between roller shades and cellular shades?"
      a: "Roller shades are a single layer of fabric that rolls onto a tube — simple, modern look, easy to motorize. Cellular (honeycomb) shades have a pleated structure that traps air and provides insulation. Cellular shades are better for energy efficiency; roller shades are better for a minimalist aesthetic."
    - q: "Can window shades be motorized in St. Pete homes?"
      a: "Yes. We install Hunter Douglas PowerView and Graber motorized systems compatible with voice control (Alexa, Google Home) and smartphone apps. Motorization is particularly practical for high windows, skylights, and homes with many windows where manual operation becomes inconvenient."
  ```

  **`src/content/services/custom-blinds.md`**
  ```yaml
  faqs:
    - q: "What types of custom blinds do you install in St. Petersburg?"
      a: "We install wood blinds, faux wood blinds, aluminum blinds, and vertical blinds. For Florida homes, faux wood blinds are the most practical choice — they resist humidity and salt air without warping the way real wood does."
    - q: "How are custom blinds different from Home Depot blinds?"
      a: "Custom blinds are built to your exact window dimensions — no cutting, no gaps, no uneven slats. They use heavier-gauge materials, better tilt mechanisms, and come with manufacturer warranties. We also include professional installation and return for any adjustments."
    - q: "What are the best blinds for a waterfront home in Pinellas County?"
      a: "Faux wood blinds (PVC or composite) are the standard for waterfront properties. They handle humidity, salt air, and temperature swings without warping. Real wood blinds are not recommended for windows within a mile of saltwater."
  ```

  **`src/content/services/custom-cornices-valances.md`**
  ```yaml
  faqs:
    - q: "What is the difference between a cornice and a valance?"
      a: "A cornice is a rigid, box-shaped top treatment — typically foam or wood covered in fabric — that mounts to the wall above the window. A valance is a soft fabric treatment that hangs from a rod. Cornices give a more architectural, built-in look; valances are softer and more decorative."
    - q: "Can you match a cornice to my existing drapery?"
      a: "Yes. Because we fabricate both in our St. Pete workroom, we can cut and wrap a cornice in the same fabric as your panels, with the same trim and lining. Exact color match is guaranteed when we build both in the same project."
    - q: "How are cornices mounted?"
      a: "Cornices mount to angle irons screwed directly into the wall or window frame above the window. The mount is hidden once the cornice is in place. Our installers make sure the cornice is level and centered on the window. Typical installation is 30–60 minutes per window."
  ```

  **`src/content/services/drapery-hardware.md`**
  ```yaml
  faqs:
    - q: "Do you supply and install drapery rods, or just install them?"
      a: "Both. We supply decorative rods, concealed tracks, motorized systems, and bay window hardware from our authorized brands, and our in-house installers mount everything. If you have hardware you've already purchased, we can install that too."
    - q: "What drapery hardware works best for high ceilings in St. Pete homes?"
      a: "For ceilings over 10 feet, ceiling-mounted tracks (visible or concealed) give a cleaner look than wall-mounted rods. We carry Kirsch, Integra, and Silent Gliss track systems in custom lengths. Motorized track systems are practical on 12-foot-and-up ceilings where manual operation is awkward."
    - q: "Can you motorize existing drapery rods?"
      a: "In most cases, no — motorization requires a track system designed for it, not a standard rod. We can replace your existing rod with a motorized track and rehang your current panels if the fabric is compatible."
  ```

  **`src/content/services/outdoor-window-shades.md`**
  ```yaml
  faqs:
    - q: "What outdoor shades work best on a Florida lanai or patio?"
      a: "Solar screen roller shades are the most popular outdoor shade in St. Pete. A 5% openness fabric blocks 95% of solar heat while keeping the view. For full privacy or blackout on a covered lanai, an outdoor woven or vinyl fabric is the better choice."
    - q: "Can outdoor shades withstand Florida's hurricane season?"
      a: "Quality exterior roller shades with aluminum or stainless steel hardware hold up to normal Florida wind and rain. They are not hurricane-rated shutters and should be rolled up before a named storm. We specify stainless hardware for all coastal properties to prevent corrosion."
    - q: "How long do outdoor shades last in St. Petersburg's climate?"
      a: "Well-specified outdoor shades in Florida typically last 7–12 years before fabric fading or hardware wear requires replacement. Sunbrella and Mermet fabrics last longer than generic polyester. Salt air exposure and direct UV hours are the biggest variables."
  ```

  **`src/content/services/furniture-reupholstery.md`**
  ```yaml
  faqs:
    - q: "Is it worth reupholstering furniture in St. Petersburg?"
      a: "Yes, when the frame is solid hardwood and the piece has sentimental or design value. Reupholstering typically costs 40–70% of a comparable new piece and produces a result that outperforms most retail furniture. We're honest at the consultation — if the frame isn't worth saving, we'll say so."
    - q: "What furniture can you reupholster?"
      a: "We reupholster sofas, loveseats, sectionals, armchairs, dining chairs, bar stools, headboards, ottomans, and benches. We also recover cushions for built-in window seats and banquettes."
    - q: "How long does reupholstery take in St. Pete?"
      a: "Most reupholstery projects take 4–6 weeks from drop-off or pickup to delivery. A single dining chair is faster; a sectional or an antique with complex tufting takes longer. We give you a written timeline when we take the piece into our workroom."
    - q: "Do you pick up and deliver furniture in the St. Petersburg area?"
      a: "Yes. We offer in-home pickup and delivery across St. Pete and Pinellas County. We bring moving blankets and handle the logistics, so you don't need to transport a sofa."
  ```

  **`src/content/services/custom-bedding-pillows.md`**
  ```yaml
  faqs:
    - q: "Can you make custom bedding to match my window treatments?"
      a: "Yes. Because we fabricate both in our St. Pete workroom, we can build a duvet cover, shams, and euro pillows in the same fabric as your drapery or with complementary coordinating fabrics from Kravet or Stout. Exact color matching across products is one of our specialties."
    - q: "What's the lead time for custom bedding in St. Petersburg?"
      a: "Most custom bedding orders take 3–5 weeks. This includes a fabric consultation, measuring your existing bedding or ordering a standard size, and production in our local workroom. Rush orders are sometimes possible — ask at the consultation."
    - q: "Do you make custom decorative pillows and cushions?"
      a: "Yes. We make accent pillows, bolster pillows, and custom cushions for window seats, sofas, and outdoor furniture. We can coordinate with existing upholstery or window treatments."
  ```

  **`src/content/services/custom-banquettes.md`**
  ```yaml
  faqs:
    - q: "What is a custom banquette?"
      a: "A banquette is built-in bench seating, typically in a dining nook or kitchen corner. We design and install the structural frame and upholster the cushions and back panels in your choice of performance fabric. The result is a permanent architectural feature that can't be replicated with free-standing furniture."
    - q: "What fabrics do you use for banquette cushions in Florida?"
      a: "We recommend performance fabrics — Crypton, Sunbrella, or Kravet Boucle Perform — for banquette cushions in Florida. They handle spills, humidity, and heavy daily use without staining or mildew. We carry hundreds of colors and patterns in performance-grade materials."
    - q: "How long does a custom banquette project take?"
      a: "From signed proposal to installation, most banquette projects take 4–6 weeks. The structural build happens in our workroom; installation is typically one day. We coordinate with your contractor if the project involves any wall work."
  ```

  **`src/content/services/commercial-window-treatments.md`**
  ```yaml
  faqs:
    - q: "Do you handle commercial window treatment projects in St. Petersburg?"
      a: "Yes. We work with offices, medical offices, restaurants, hotels, multi-family residential, and retail spaces across Pinellas County. We provide spec sheets, coordinate with general contractors, and install on a commercial schedule."
    - q: "Can you spec Hunter Douglas or Norman products for a commercial project?"
      a: "Yes, we are an authorized commercial dealer for Hunter Douglas, Norman, and Graber. We can provide contractor pricing, spec documentation, and commercial warranties. Contact us for volume pricing on orders of 20 or more windows."
    - q: "Do you provide light control solutions for medical offices?"
      a: "Yes. We spec blackout roller shades, room-darkening cellular shades, and privacy film for medical examination and procedure rooms. All products we specify for healthcare are antimicrobial-fabric-compatible and installable without disrupting your schedule."
  ```

  **`src/content/services/services-interior-decor-tampa.md`**
  ```yaml
  faqs:
    - q: "What does the interior design consultation include?"
      a: "The in-home consultation covers window treatment recommendations, fabric selection from our curated Kravet and Stout libraries, hardware recommendations, color coordination with your existing furnishings, and lighting analysis. Most consultations are 60–90 minutes."
    - q: "Do you charge for interior design consultations?"
      a: "Initial consultations are complimentary for homeowners in St. Pete and across Pinellas County. We bring our full sample library to your home and provide detailed recommendations at no charge. Fee-based design retainers are available for large or multi-room projects."
    - q: "Can you coordinate window treatments, bedding, and upholstery across a whole house?"
      a: "Yes. Because we fabricate in our own workroom, we can specify window treatments, bedding, and upholstery in the same fabrics and finishes for any room or the entire house. Single-vendor coordination across all soft goods is one of our primary advantages over boutique designers who outsource fabrication."
  ```

- [ ] **Step 2: Verify all service pages emit FAQPage schema**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -3
  for slug in custom-draperies-curtains window-shades custom-blinds custom-cornices-valances drapery-hardware outdoor-window-shades furniture-reupholstery custom-bedding-pillows custom-banquettes commercial-window-treatments services-interior-decor-tampa; do
    count=$(grep -c '"@type":"FAQPage"' dist/services/$slug/index.html 2>/dev/null || echo 0)
    echo "$slug: $count"
  done
  ```
  Expected: each line shows `1`.

- [ ] **Step 3: Commit**

  ```bash
  git add src/content/services/
  git commit -m "feat: add FAQ frontmatter to all 11 remaining service pages"
  ```

---

## Task 8: Add FAQ Frontmatter to Area MDs (P1)

**Files:** All 14 area MD files.

- [ ] **Step 1: Add faqs to each area MD**

  Add the following `faqs:` block to each file's YAML frontmatter, after `type: area`.

  **`src/content/areas/st-petersburg.md`**
  ```yaml
  faqs:
    - q: "Do you serve all neighborhoods in St. Petersburg, FL?"
      a: "Yes. We provide in-home consultations and installation throughout the entire city of St. Petersburg, including Snell Isle, Old Northeast, Downtown St. Pete, West St. Pete, Shore Acres, and all surrounding communities."
    - q: "How do I schedule a window treatment consultation in St. Petersburg?"
      a: "Call (727) 240-4512 or use the contact form on this site. We'll schedule a time to bring our full sample library to your home — no charge for the consultation, no deposit required."
    - q: "What window treatments are most popular in St. Petersburg homes?"
      a: "Plantation shutters (faux wood) and motorized roller shades are the most-requested products in St. Pete. Shutters are the go-to for permanent architectural value; motorized solar shades are popular for their heat control on west and south-facing windows."
  ```

  **`src/content/areas/downtown-st-pete.md`**
  ```yaml
  faqs:
    - q: "Do you work in condos and high-rises in Downtown St. Pete?"
      a: "Yes. We handle condo installations regularly in Downtown St. Pete — the 400, ONE St. Petersburg, Parkshore Plaza, and many others. We coordinate with building management for elevator reservations and insurance documentation as required."
    - q: "What window treatments are best for a downtown condo with floor-to-ceiling windows?"
      a: "For large modern windows in Downtown St. Pete condos, motorized solar shades are the most popular choice — they manage solar heat and glare without obscuring the view. For privacy at night, we layer a sheer or blockout roller shade on the same fascia."
    - q: "Can you match HOA-required window treatment colors for a Downtown condo?"
      a: "Yes. Most Downtown St. Pete HOAs specify a neutral liner or shade color facing the exterior. We match HOA requirements exactly and provide documentation to your HOA if needed."
  ```

  **`src/content/areas/old-northeast.md`**
  ```yaml
  faqs:
    - q: "What window treatments work best in Old Northeast historic homes?"
      a: "Old Northeast's Craftsman bungalows and Mediterranean revival homes are classic candidates for real wood plantation shutters or custom drapery with wooden poles and rings. The period aesthetic calls for warm, natural materials — shutters in stained basswood or custom drapes in textured linen are the most popular choices."
    - q: "Can you work around historic trim and deep window sills in Old Northeast?"
      a: "Yes. Deep sills and historic window casings are standard for us. We do inside-mount shutters on wide sills and work around existing trim profiles without damaging the millwork."
    - q: "Do you install window treatments in Old Northeast rental properties?"
      a: "Yes. We work with both homeowners and landlords. For rental properties, we recommend faux wood shutters or motorized roller shades — durable, easy to clean, and strong selling points for tenants."
  ```

  **`src/content/areas/snell-isle.md`**
  ```yaml
  faqs:
    - q: "What window treatments are popular in Snell Isle waterfront homes?"
      a: "Faux wood plantation shutters are the top choice for Snell Isle — they handle salt air, Gulf humidity, and direct sun without warping. For lanai openings, exterior solar roller shades in stainless-hardware systems are standard."
    - q: "Do you handle large window installations in Snell Isle custom homes?"
      a: "Yes. Snell Isle homes regularly have oversized windows, floor-to-ceiling glass, and custom shapes. We build to exact measurements and handle specialty shapes including arches, transoms, and full-height bypass shutter systems."
    - q: "How long does a full-home window treatment project take in Snell Isle?"
      a: "A full Snell Isle home with 12–20 windows typically installs in one day. Lead time from signed proposal to install day is 4–6 weeks for faux wood shutters, 6–8 weeks for custom motorized systems."
  ```

  **`src/content/areas/shore-acres.md`**
  ```yaml
  faqs:
    - q: "What window treatments handle Shore Acres humidity and waterfront exposure?"
      a: "Faux wood shutters and exterior solar shades are both well-suited to Shore Acres' waterfront conditions. We specify stainless hardware for all outdoor applications to prevent corrosion, and use UV-stabilized fabrics on all sun-exposed windows."
    - q: "Do you serve the Shore Acres area for furniture reupholstery?"
      a: "Yes. We serve Shore Acres for all services — window treatments, custom drapery, furniture reupholstery, custom bedding, and banquettes. We offer in-home pickup and delivery for upholstery projects."
    - q: "Can you install window treatments in a Shore Acres waterfront condo?"
      a: "Yes, including condos in Shore Acres with HOA requirements. We coordinate with building management and match any exterior shade color specifications."
  ```

  **`src/content/areas/west-st-pete.md`**
  ```yaml
  faqs:
    - q: "Do you have a showroom in West St. Pete?"
      a: "Yes. Our West St. Pete studio is at 3026 Central Ave Ste 551, St. Petersburg, FL 33712. You can call (352) 266-1262 to schedule an appointment or an in-home consultation."
    - q: "What services are available at the West St. Pete location?"
      a: "All services — custom window treatments, plantation shutters, motorized shades, custom drapery, furniture reupholstery, custom bedding, and banquettes. Our in-house workroom and design team serve all of West St. Pete and Pinellas County from this location."
    - q: "What are your hours at the West St. Pete location?"
      a: "Please call (352) 266-1262 or use the contact form to confirm current hours and schedule your consultation. In-home appointments are available evenings and weekends by request."
  ```

  **`src/content/areas/tierra-verde.md`**
  ```yaml
  faqs:
    - q: "What window treatments work best for Tierra Verde canal and waterfront homes?"
      a: "Faux wood plantation shutters are the top choice for Tierra Verde — they handle the humidity, salt air, and intense Gulf sun without warping or fading. For lanai openings, exterior solar roller shades in stainless-hardware systems are standard."
    - q: "Do you serve Tierra Verde for custom window treatment installation?"
      a: "Yes. Tierra Verde is in our standard service area. We provide in-home consultations and same-day installation for most full-home projects."
    - q: "Can plantation shutters be installed on a Tierra Verde lanai or screen enclosure?"
      a: "Interior plantation shutters install on the inside of your sliding glass doors. For the lanai side, exterior roller shades or screen enclosure panels are the right product. We handle both."
  ```

  **`src/content/areas/st-pete-beach.md`**
  ```yaml
  faqs:
    - q: "What window treatments are best for a St. Pete Beach vacation rental or condo?"
      a: "Faux wood shutters are the most popular choice for St. Pete Beach rental properties — they're durable, easy to clean, look premium to guests, and add to the property's appraised value. Motorized blackout roller shades are popular for bedrooms."
    - q: "Do you work with vacation rental managers in St. Pete Beach?"
      a: "Yes. We work with individual owners and property managers. For rental properties, we can schedule installations between guest stays and provide documentation for HOA approvals."
    - q: "How do window treatments handle St. Pete Beach salt air and humidity?"
      a: "We always specify faux wood or aluminum for any window within a half-mile of the Gulf. Stainless or nylon hardware is specified for all outdoor and marine-adjacent applications. Real wood is explicitly not recommended for beachfront properties."
  ```

  **`src/content/areas/treasure-island.md`**
  ```yaml
  faqs:
    - q: "What window treatments are best for a Treasure Island beachfront home?"
      a: "Faux wood plantation shutters are the default for Treasure Island homes — they resist salt air and Gulf humidity without warping. For the lanai or outdoor areas, exterior solar shades with marine-grade stainless hardware are the standard specification."
    - q: "Do you provide luxury bedding and custom cushions in the Treasure Island area?"
      a: "Yes. We serve Treasure Island for all custom fabric services — bedding, decorative pillows, custom cushions, and furniture reupholstery. We bring fabric samples to your home during the consultation."
    - q: "What's the lead time for plantation shutters in Treasure Island?"
      a: "4–6 weeks from signed proposal to installation for standard faux wood shutters. Specialty shapes (arches, French doors, bay windows) are 6–8 weeks. We provide a written timeline at the time of order."
  ```

  **`src/content/areas/clearwater.md`**
  ```yaml
  faqs:
    - q: "Do you serve Clearwater for custom window treatments?"
      a: "Yes. Clearwater is in our standard service area. We provide free in-home consultations and installation across Clearwater Beach, Island Estates, Harbor Bluffs, and all Clearwater neighborhoods."
    - q: "What window treatments are popular in Clearwater Beach condos?"
      a: "Motorized solar roller shades are the top choice for Clearwater Beach condos — they manage solar heat and glare on large west-facing windows while preserving Gulf views. For bedrooms, motorized blackout shades are standard."
    - q: "Can you match Clearwater HOA exterior shade color requirements?"
      a: "Yes. We work with most Clearwater Beach HOAs regularly and are familiar with the standard exterior-facing color specifications. We provide HOA documentation on request."
  ```

  **`src/content/areas/sand-key.md`**
  ```yaml
  faqs:
    - q: "Do you serve Sand Key for plantation shutters and window treatments?"
      a: "Yes. Sand Key is in our standard service area. We provide in-home consultations and installation throughout Sand Key, including the Sand Key Club, Ultimar, and beachfront condos on Gulf Blvd."
    - q: "What window treatments handle Sand Key's intense Gulf sun?"
      a: "Solar shade roller shades (3–5% openness) are the most popular on Sand Key for west-facing Gulf views — they block 95%+ of solar heat while keeping the water view. Faux wood shutters are the standard for interior rooms."
    - q: "Can you install motorized blinds in a Sand Key high-rise condo?"
      a: "Yes. We install Hunter Douglas PowerView and Graber motorized systems in high-rise condos regularly. We coordinate with building management for elevator access and insurance documentation as required."
  ```

  **`src/content/areas/belleair-shore.md`**
  ```yaml
  faqs:
    - q: "Do you serve Belleair Shore for custom window treatments?"
      a: "Yes. Belleair Shore is in our service area. We provide free in-home consultations and installation for all window treatment and upholstery services."
    - q: "What's the best window treatment for a Belleair Shore waterfront home?"
      a: "Faux wood plantation shutters on interior windows and exterior marine-grade solar shades on lanai openings. We specify all hardware in stainless or nylon for any installation within a quarter-mile of Clearwater Harbor."
    - q: "Do you offer furniture reupholstery in Belleair Shore?"
      a: "Yes. We serve Belleair Shore for all services including furniture reupholstery. We offer in-home pickup and delivery across Pinellas County."
  ```

  **`src/content/areas/seminole.md`**
  ```yaml
  faqs:
    - q: "Do you serve Seminole, FL for window treatments?"
      a: "Yes. Seminole is in our standard service area. We provide free in-home consultations and professional installation for all window treatment services across Seminole."
    - q: "What window treatments are popular in Seminole for solar control?"
      a: "Solar roller shades and cellular (honeycomb) shades are the most popular in Seminole for blocking intense afternoon sun without losing natural light. For more traditional homes, faux wood plantation shutters are the leading choice."
    - q: "How do I get a quote for window treatments in Seminole?"
      a: "Call (727) 240-4512 or use our contact form to schedule a free in-home consultation. We bring our full sample library to your home and provide a written itemized quote within 24–48 hours of the measure."
  ```

  **`src/content/areas/largo.md`**
  ```yaml
  faqs:
    - q: "Do you serve Largo, FL for custom window treatments?"
      a: "Yes. Largo is in our service area. We provide free in-home consultations and professional installation across all Largo neighborhoods."
    - q: "Can you handle commercial window treatment projects in Largo?"
      a: "Yes. We work with offices, medical practices, restaurants, and multi-family properties in Largo. We provide spec documentation and commercial warranties. Contact us for volume pricing."
    - q: "What's your lead time for window treatments in Largo?"
      a: "4–6 weeks from signed proposal to installation for most products. Motorized systems and specialty shapes are 6–8 weeks. We provide a written timeline at the time of order."
  ```

- [ ] **Step 2: Verify area pages emit FAQPage schema**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -3
  for slug in st-petersburg downtown-st-pete old-northeast snell-isle shore-acres west-st-pete tierra-verde st-pete-beach treasure-island clearwater sand-key belleair-shore seminole largo; do
    count=$(grep -c '"@type":"FAQPage"' dist/areas/$slug/index.html 2>/dev/null || echo 0)
    echo "$slug: $count"
  done
  ```
  Expected: each line shows `1`.

- [ ] **Step 3: Commit**

  ```bash
  git add src/content/areas/
  git commit -m "feat: add FAQ frontmatter to all 14 area pages"
  ```

---

## Task 9: Fix Stale Content and Duplicate Sections in plantation-shutters.md (P1)

**Files:**
- Modify: `src/content/services/plantation-shutters.md`

Three changes: fix "nearly two decades" (line 107), fix "since 2000" workroom claim (line 93 and 107), and remove two duplicate section pairs.

- [ ] **Step 1: Fix stale temporal phrases**

  In `src/content/services/plantation-shutters.md`:

  ```diff
  -## Our In-House Workroom: Since 2000
  +## Our In-House Workroom: Since 2007
  ```

  ```diff
  -Since 2000, nearly two decades, one family business, one workroom, one phone number.
  +Since 2007, 25+ years of combined experience, one family business, one workroom, one phone number.
  ```

- [ ] **Step 2: Remove the first duplicate section (keep the 4-step process, remove the shorter version)**

  The shorter version "Our Plantation Shutter Installation Process in St. Petersburg" (lines 124–130) duplicates the more detailed "How We Build Your Shutters: Our 4-Step Process" (lines 161–169). Remove the shorter version entirely:

  Delete the section from `## Our Plantation Shutter Installation Process in St. Petersburg` through the bulleted list that ends with `- Professional installation. We install and level every shutter...`.

- [ ] **Step 3: Remove the second duplicate section (keep "Specialty Shapes & Applications", remove "French Doors, Sliders & Pass-Throughs")**

  "Plantation Shutters for French Doors, Sliders & Pass-Throughs" (lines 149–159) covers the same content as "Specialty Shapes & Applications" (lines 58–70). Remove the later duplicate section:

  Delete from `## Plantation Shutters for French Doors, Sliders & Pass-Throughs` through the bay and bow windows paragraph.

- [ ] **Step 4: Verify build passes**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -3
  ```
  Expected: exits 0, no errors.

- [ ] **Step 5: Commit**

  ```bash
  git add src/content/services/plantation-shutters.md
  git commit -m "fix: update stale workroom date and remove duplicate content sections on plantation-shutters"
  ```

---

## Task 10: Mount MeetTheOwner Card on Service Pages (P1)

**Files:**
- Modify: `src/layouts/ServiceLayout.astro`

`MeetTheOwner.astro` exists and is already used on `about.astro`. Adding it to `ServiceLayout` puts Terry Popick's name and bio on every service page, addressing the E-E-A-T gap the audit flagged.

- [ ] **Step 1: Import and add MeetTheOwner to ServiceLayout**

  In `src/layouts/ServiceLayout.astro`:

  ```diff
  +import MeetTheOwner from '~/components/MeetTheOwner.astro';
   import FinalCTA from '~/components/FinalCTA.astro';
  ```

  Then, between `<GlobalContactMap />` and the closing, add:

  ```diff
   {faqs && faqs.length > 0 && (
     <FAQ items={faqs} heading={`${serviceTitle} — Frequently Asked Questions`} eyebrow="Common Questions" subtitle={`Answers about our ${serviceTitle.toLowerCase()} process.`} />
   )}
  
  +<MeetTheOwner
  +  image="/images/services/custom-draperies-curtains/top.webp"
  +/>
  +
   <GlobalContactMap />
  ```

- [ ] **Step 2: Verify build and spot-check a service page**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -3
  grep -c 'Terry Popick\|meet-owner\|MeetTheOwner' dist/services/plantation-shutters/index.html
  ```
  Expected: build passes, grep returns > 0.

- [ ] **Step 3: Commit**

  ```bash
  git add src/layouts/ServiceLayout.astro
  git commit -m "feat: add MeetTheOwner component to all service pages for E-E-A-T"
  ```

---

## Task 11: Fix Brands Page — Add 3 Missing Brands (P1)

> **Pre-flight dependency:** Confirm with operator which brands to add and whether to keep/drop Graber.

**Files:**
- Modify: `src/pages/brands.astro`

Three brand logos already exist in `public/images/brands/`: `ALTA Window Fashions.webp`, `Elegant Shutters.webp`, `Horizon Window Fashions.webp`. This task adds them to the BRANDS array and adds logo display to the brand cards.

- [ ] **Step 1: Add the three missing brands to the BRANDS array in brands.astro**

  In `src/pages/brands.astro`, add three entries to the `BRANDS` array after the Stout entry:

  ```diff
   {
     name: 'Stout',
     tagline: 'Distinctive textiles and trims',
     body: 'Stout specializes in distinctive, character-driven fabrics...',
     highlights: [...],
   },
  +{
  +  name: 'Horizons Window Fashions',
  +  tagline: 'Specialty soft treatments for Florida',
  +  body: 'Horizons is known for its soft roller shades, silhouette sheers, and specialty vane treatments. A strong choice for clients who want the look of sheers with the structure of a shade system.',
  +  highlights: ['Roller and soft-fold shades', 'Silhouette-style vane sheers', 'Solar and privacy fabrics', 'Custom colors and textures'],
  +},
  +{
  +  name: 'Elegant Shutters',
  +  tagline: 'Premium plantation shutters',
  +  body: 'Elegant Shutters produces high-quality faux wood and real wood plantation shutters with a clean Florida aesthetic. Available in custom sizes, paint colors, and stains with a comprehensive warranty program.',
  +  highlights: ['Faux wood plantation shutters', 'Real wood basswood options', 'Custom paint and stain', 'Lifetime limited warranty'],
  +},
  +{
  +  name: 'ALTA Window Fashions',
  +  tagline: 'Broad catalog at competitive price points',
  +  body: 'ALTA covers the full window treatment spectrum — cellular shades, roller shades, Roman shades, wood blinds, and plantation shutters — at competitive price points without sacrificing quality. Popular for multi-room or whole-home projects where budget management matters.',
  +  highlights: ['Cellular and roller shades', 'Wood and faux wood blinds', 'Roman shades', 'Plantation shutters'],
  +},
  ```

- [ ] **Step 2: Add logo display to the brand card template**

  Update the `BRANDS.map()` template to show logos where available. First, add a `logo` field to each brand object (only where logos exist in `public/images/brands/`):

  The existing five brands get:
  - Hunter Douglas → `/images/brands/Hunter Douglas.webp`
  - Norman → `/images/brands/Norman-Shutters.webp`
  - Graber → no existing logo
  - Kravet → `/images/brands/Kravet-Fabric.webp`
  - Stout → `/images/brands/Stout.webp`

  New brands:
  - Horizons → `/images/brands/Horizon Window Fashions.webp`
  - Elegant Shutters → `/images/brands/Elegant Shutters.webp`
  - ALTA → `/images/brands/ALTA Window Fashions.webp`

  Add a `logo?: string` field to each brand object, then update the template:

  ```diff
   <div class:list={['grid md:grid-cols-[220px_1fr] gap-10 items-start', i !== BRANDS.length - 1 && 'pb-16 border-b border-line']}>
     <div>
  +    {b.logo && <img src={b.logo} alt={b.name} class="h-10 w-auto object-contain mb-4" loading="lazy" />}
       <p class="eyebrow">{b.tagline}</p>
       <h2 class="font-display text-3xl text-ink-800 mb-0">{b.name}</h2>
     </div>
  ```

- [ ] **Step 3: Verify build**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -3
  grep -c 'Horizons Window Fashions\|Elegant Shutters\|ALTA Window Fashions' dist/brands/index.html
  ```
  Expected: build passes, grep returns `3`.

- [ ] **Step 4: Commit**

  ```bash
  git add src/pages/brands.astro
  git commit -m "feat: add Horizons, Elegant Shutters, and ALTA to brands page with logos"
  ```

---

## Task 12: Ship `public/_headers` for Security Headers (P1)

**Files:**
- Create: `public/_headers`

Cloudflare Pages reads `_headers` from the publish directory and applies the directives as response headers sitewide.

- [ ] **Step 1: Create public/_headers**

  Create `cfc-astro/public/_headers` with this content:

  ```
  /*
    Strict-Transport-Security: max-age=31536000; includeSubDomains
    X-Content-Type-Options: nosniff
    X-Frame-Options: SAMEORIGIN
    Referrer-Policy: strict-origin-when-cross-origin
    Permissions-Policy: camera=(), microphone=(), geolocation=()
  ```

  Note: No `Content-Security-Policy` header yet — adding CSP on a site with inline scripts and third-party Google Maps embeds requires an audit of all inline scripts first. The four headers above are safe to ship immediately.

- [ ] **Step 2: Verify build includes _headers**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -3
  cat dist/_headers
  ```
  Expected: build passes, `_headers` content is visible.

- [ ] **Step 3: Commit**

  ```bash
  git add public/_headers
  git commit -m "feat: add Cloudflare Pages _headers for HSTS, X-Frame-Options, X-Content-Type-Options"
  ```

---

## Task 13: Schema Improvements — BlogPosting, WebPage, dateModified, VideoObject (P1/P2)

**Files:**
- Modify: `src/components/Schema.astro`
- Modify: `src/layouts/BaseLayout.astro`

Four targeted schema improvements.

- [ ] **Step 1: Add articleDateModified prop to BaseLayout**

  In `src/layouts/BaseLayout.astro`, add `articleDateModified` to the Props interface and destructuring:

  ```diff
   interface Props {
     ...
     articleDate?: string;
  +  articleDateModified?: string;
     faqs?: Array<{ q: string; a: string }>;
     ...
   }

   const {
     ...
     articleDate,
  +  articleDateModified,
     faqs,
     ...
   } = Astro.props;
  ```

  Pass it through to Schema:
  ```diff
   <Schema
     ...
     articleDate={articleDate}
  +  articleDateModified={articleDateModified}
     faqs={faqs}
     ...
   />
  ```

- [ ] **Step 2: Update Schema.astro — BlogPosting + dateModified**

  In `src/components/Schema.astro`, add `articleDateModified` to Props interface and destructuring:

  ```diff
   interface Props {
     ...
     articleDate?: string;
  +  articleDateModified?: string;
     faqs?: Array<{ q: string; a: string }>;
   }

   const {
     ...
     articleDate,
  +  articleDateModified,
     faqs = [],
     ...
   } = Astro.props;
  ```

  Change `'Article'` to `'BlogPosting'` and fix `dateModified`:

  ```diff
  -if (pageType === 'article' && articleDate) {
  +if (pageType === 'article' && articleDate) {
     graph.push({
  -    '@type': 'Article',
  +    '@type': 'BlogPosting',
       '@id': `${canonicalUrl}#article`,
       headline: title,
       description,
       author: { '@id': orgId },
       publisher: { '@id': orgId },
       datePublished: articleDate,
  -    dateModified: articleDate,
  +    dateModified: articleDateModified ?? articleDate,
       image: imageUrl,
       mainEntityOfPage: canonicalUrl,
     });
   }
  ```

- [ ] **Step 3: Add WebPage node for service, area, contact, about page types**

  In `src/components/Schema.astro`, add after the `if (pageType === 'home')` block:

  ```diff
  +if (['service', 'area', 'contact', 'about', 'gallery', 'brands', 'collection', 'page'].includes(pageType)) {
  +  graph.push({
  +    '@type': 'WebPage',
  +    '@id': `${canonicalUrl}#webpage`,
  +    url: canonicalUrl,
  +    name: title,
  +    description,
  +    isPartOf: { '@id': websiteId },
  +    primaryImageOfPage: imageUrl ? { '@type': 'ImageObject', url: imageUrl } : undefined,
  +  });
  +}
  ```

- [ ] **Step 4: Add VideoObject for the homepage hero video**

  In `src/components/Schema.astro`, inside the `if (pageType === 'home')` block, add a VideoObject node:

  ```diff
   if (pageType === 'home') {
     graph.push({
       '@type': 'WebPage',
       ...
     });
  +  graph.push({
  +    '@type': 'VideoObject',
  +    '@id': `${SITE.url}/#hero-video`,
  +    name: 'Custom Fabric Creations — St. Pete Window Treatments Studio',
  +    description: 'A look inside the Custom Fabric Creations workroom and showroom in St. Petersburg, FL. Custom drapery, plantation shutters, and upholstery for Pinellas County homes.',
  +    thumbnailUrl: `${SITE.url}/images/hero/homepage.webp`,
  +    contentUrl: `${SITE.url}/hero-video.mp4`,
  +    uploadDate: '2024-01-01',
  +    publisher: { '@id': orgId },
  +  });
   }
  ```

- [ ] **Step 5: Add CollectionPage handler for brands pageType**

  Currently `pageType="brands"` falls through to the base graph with no page-specific node. Add:

  ```diff
  +if (pageType === 'brands') {
  +  graph.push({
  +    '@type': 'CollectionPage',
  +    '@id': `${canonicalUrl}#collection`,
  +    url: canonicalUrl,
  +    name: title,
  +    description,
  +  });
  +}
  ```

- [ ] **Step 6: Verify build and spot-check schema**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -3
  grep -o '"@type":"BlogPosting"' dist/plantation-shutters-cost-st-petersburg/index.html
  grep -o '"@type":"WebPage"' dist/services/plantation-shutters/index.html
  grep -o '"@type":"VideoObject"' dist/index.html
  grep -o '"@type":"CollectionPage"' dist/brands/index.html
  ```
  Expected: all four return a match.

- [ ] **Step 7: Commit**

  ```bash
  git add src/components/Schema.astro src/layouts/BaseLayout.astro
  git commit -m "feat: improve schema — BlogPosting, WebPage nodes, VideoObject, CollectionPage for brands"
  ```

---

## Task 14: Ship `public/llms.txt` (P2)

**Files:**
- Create: `public/llms.txt`

`llms.txt` is a plain-text brand summary for AI crawlers (ChatGPT, Perplexity, Claude). It should be at the site root and cover: brand identity, services, NAP, and key claims.

- [ ] **Step 1: Create public/llms.txt**

  Create `cfc-astro/public/llms.txt` with:

  ```
  # Custom Fabric Creations

  Custom Fabric Creations is a locally owned custom window treatment and upholstery studio in St. Petersburg, Florida. Established in 2000 and operated by founder Terry Popick, the studio has served Pinellas County and the Tampa Bay area for 25+ years.

  ## Services

  - Custom plantation shutters (faux wood, basswood, hybrid)
  - Custom drapery and curtains
  - Window shades (roller, cellular, roman, solar, motorized)
  - Custom blinds (faux wood, real wood, aluminum)
  - Cornices and valances
  - Drapery hardware (rods, tracks, motorized systems)
  - Outdoor window shades and patio treatments
  - Furniture reupholstery
  - Custom bedding, pillows, and cushions
  - Custom banquettes
  - Commercial window treatments
  - Interior design consultation

  ## Location

  3026 Central Ave Ste 551, St. Petersburg, FL 33712
  Phone: (727) 240-4512
  Email: info@customfabriccreations.net
  Website: https://www.customfabriccreations.net

  ## Service Area

  St. Petersburg, FL and Pinellas County: Downtown St. Pete, Old Northeast, Snell Isle, Shore Acres, West St. Pete, Tierra Verde, St. Pete Beach, Treasure Island, Clearwater, Sand Key, Belleair Shore, Seminole, Largo.

  ## Authorized Brands

  Hunter Douglas, Norman, Graber, Kravet, Stout, Horizons Window Fashions, Elegant Shutters, ALTA Window Fashions.

  ## Credentials

  - Locally owned and operated since 2000
  - In-house fabrication workroom (not outsourced)
  - In-house installation crew (not subcontracted)
  - Fully insured for residential and commercial work
  - 4.9-star Google rating, 100+ verified reviews
  - Free in-home design consultations across Pinellas County
  ```

- [ ] **Step 2: Verify file is in build output**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -3
  cat dist/llms.txt | head -5
  ```
  Expected: build passes, first 5 lines of llms.txt are visible.

- [ ] **Step 3: Commit**

  ```bash
  git add public/llms.txt
  git commit -m "feat: add llms.txt for AI crawler brand summary"
  ```

---

## Task 15: Fix Placeholder Alt Text in Content MDs (P2)

**Files:** Multiple content MD files that use `![Top](...)`, `![Top Middle](...)`, `![Bottom Middle](...)`, `![Bottom](...)`.

- [ ] **Step 1: Grep for placeholder alt text to find all occurrences**

  ```bash
  cd cfc-astro && grep -rn '!\[Top\]\|!\[Top Middle\]\|!\[Bottom Middle\]\|!\[Bottom\]\|!\[West St Pete\]' src/content/
  ```
  Note the output — it will list every file and line that needs updating.

- [ ] **Step 2: Replace placeholder alt text in each file**

  The replacement rule: `![Alt text](path)` → use a descriptive alt that names the service and what's shown.

  Apply these replacements across all content MD files (the pattern is consistent — each service and area page has 1–3 inline images):

  For service pages, use the format `[Service name] by Custom Fabric Creations in St. Petersburg, FL`:

  - `![Top](/images/services/plantation-shutters/top.webp)` → `![Plantation shutters installed in a St. Petersburg, FL living room by Custom Fabric Creations](/images/services/plantation-shutters/top.webp)`
  - `![Top Middle](/images/services/plantation-shutters/top-middle.webp)` → `![Custom plantation shutter louver detail showing 3.5-inch slat width](/images/services/plantation-shutters/top-middle.webp)`
  - `![Bottom Middle](/images/services/plantation-shutters/bottom-middle.webp)` → `![Hunter Douglas and Norman shutter brand samples at Custom Fabric Creations](/images/services/plantation-shutters/bottom-middle.webp)`
  - `![Bottom](/images/services/plantation-shutters/bottom.webp)` → `![Plantation shutters on a St. Pete Beach waterfront home by Custom Fabric Creations](/images/services/plantation-shutters/bottom.webp)`
  - `![West St Pete](/images/areas/west-st-pete.webp)` → `![Custom window treatments installed in a West St. Pete home by Custom Fabric Creations](/images/areas/west-st-pete.webp)`

  Apply the same descriptive pattern to every other service and area MD that has placeholder alt text found in Step 1. For each image, the alt text should state: what type of treatment is shown + the location context (St. Petersburg, FL) + Custom Fabric Creations.

- [ ] **Step 3: Verify build**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -3
  grep -rn '!\[Top\]\|!\[Top Middle\]\|!\[Bottom\]' dist/ | grep -v node_modules | head -5
  ```
  Expected: build passes, grep returns nothing (no placeholder alt text in output).

- [ ] **Step 4: Commit**

  ```bash
  git add src/content/
  git commit -m "fix: replace placeholder alt text with descriptive alternatives across all content MDs"
  ```

---

## Task 16: Update robots.txt with AI Crawler Rules (P2)

**Files:**
- Modify: `public/robots.txt`

Current file has only `User-agent: * / Allow: /` and a sitemap line. Add explicit Allow directives for known AI crawlers to signal intent.

- [ ] **Step 1: Update public/robots.txt**

  Replace the entire file with:

  ```
  User-agent: *
  Allow: /

  # AI search crawlers — explicit allow for indexing
  User-agent: GPTBot
  Allow: /

  User-agent: ChatGPT-User
  Allow: /

  User-agent: OAI-SearchBot
  Allow: /

  User-agent: PerplexityBot
  Allow: /

  User-agent: Claude-Web
  Allow: /

  User-agent: ClaudeBot
  Allow: /

  User-agent: Google-Extended
  Allow: /

  User-agent: Googlebot
  Allow: /

  Sitemap: https://www.customfabriccreations.net/sitemap-index.xml
  ```

- [ ] **Step 2: Verify build output**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -3
  cat dist/robots.txt
  ```
  Expected: all AI crawler entries visible in output.

- [ ] **Step 3: Commit**

  ```bash
  git add public/robots.txt
  git commit -m "feat: add explicit AI crawler Allow rules to robots.txt"
  ```

---

## Task 17: Build /guides/ Collection Page (P2)

**Files:**
- Create: `src/pages/guides/index.astro`
- Modify: `src/content/services/plantation-shutters.md` (add a cross-link to /guides/)

Creates a hub page linking the 3 existing plantation shutters blog posts and sets up the collection for future guides. The three existing guide pages are:
- `/plantation-shutters-cost-st-petersburg/`
- `/plantation-shutters-installation-st-petersburg/`
- `/plantation-shutters-regret-downsides/`

- [ ] **Step 1: Create src/pages/guides/index.astro**

  ```astro
  ---
  import BaseLayout from '~/layouts/BaseLayout.astro';
  import Hero from '~/components/Hero.astro';
  import FinalCTA from '~/components/FinalCTA.astro';

  const GUIDES = [
    {
      title: 'Plantation Shutters Cost in St. Petersburg, FL: Real 2026 Pricing',
      href: '/plantation-shutters-cost-st-petersburg/',
      description: 'What plantation shutters actually cost in St. Petersburg in 2026 — real price ranges by material, window size, and brand. No sales pitch around the numbers.',
      eyebrow: 'Pricing Guide',
      date: 'April 2026',
    },
    {
      title: 'Plantation Shutter Installation in St. Petersburg: What to Expect',
      href: '/plantation-shutters-installation-st-petersburg/',
      description: 'A step-by-step walkthrough of the plantation shutter installation process in St. Pete — from the measure appointment to the final walk-through.',
      eyebrow: 'Installation Guide',
      date: 'April 2026',
    },
    {
      title: 'Plantation Shutter Regrets & Downsides: What Nobody Tells You',
      href: '/plantation-shutters-regret-downsides/',
      description: 'The honest trade-offs of plantation shutters that most dealers skip. Light gaps, lead time, cost, and what to know before you sign a proposal.',
      eyebrow: 'Buyer\'s Guide',
      date: 'April 2026',
    },
  ];
  ---

  <BaseLayout
    title="Plantation Shutter Guides for St. Petersburg, FL"
    description="In-depth guides on plantation shutters for St. Petersburg homeowners — real pricing, installation walkthroughs, and honest trade-offs."
    pageType="collection"
    breadcrumbs={[{ name: 'Home', url: '/' }, { name: 'Guides', url: '/guides/' }]}
    ogImage="/images/hero/plantation-shutters.webp"
  >
    <Hero
      eyebrow="Resource Library"
      title="Plantation Shutter Guides for St. Pete Homeowners"
      subtitle="Real information for Pinellas County homeowners researching plantation shutters — pricing, installation, and honest trade-offs."
      image="/images/hero/plantation-shutters.webp"
      breadcrumbs={[{ name: 'Home', url: '/' }, { name: 'Guides', url: '/guides/' }]}
      goldLine
    />

    <section class="py-20 md:py-28 bg-white">
      <div class="container-site max-w-4xl mx-auto">
        <div class="text-center mb-14">
          <p class="eyebrow" style="letter-spacing: 0.3em;">Resource Library</p>
          <h2 class="font-display text-4xl md:text-5xl text-ink-800 mb-4">Plantation Shutter Guides</h2>
          <p class="text-ink-500 text-lg max-w-2xl mx-auto">Written from 25+ years of installing shutters across Pinellas County — not from a marketing brief.</p>
        </div>
        <div class="space-y-8">
          {GUIDES.map((g) => (
            <a href={g.href} class="group block bg-cream-50 border border-line hover:border-brand-400 rounded-sm p-8 transition-colors">
              <p class="eyebrow mb-2" style="letter-spacing: 0.2em;">{g.eyebrow} — {g.date}</p>
              <h3 class="font-display text-2xl text-ink-800 group-hover:text-brand-600 transition-colors mb-3">{g.title}</h3>
              <p class="text-ink-500 leading-relaxed">{g.description}</p>
              <span class="inline-flex items-center gap-2 mt-4 text-brand-600 font-medium text-sm">
                Read guide
                <svg class="w-4 h-4" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 10h12M10 4l6 6-6 6"/></svg>
              </span>
            </a>
          ))}
        </div>
      </div>
    </section>

    <FinalCTA
      heading="Ready to Get a Real Quote on Your Home?"
      subtitle="We measure in person at no charge across St. Petersburg and Pinellas County. No pressure, no bundled pricing."
    />
  </BaseLayout>
  ```

- [ ] **Step 2: Add cross-link from plantation-shutters.md service page to /guides/**

  In `src/content/services/plantation-shutters.md`, add a sentence at the bottom of the file body (after the last FAQ H3):

  ```markdown
  ## Plantation Shutter Resources

  Before you request a quote, our St. Pete homeowner guides walk you through [real 2026 pricing](/plantation-shutters-cost-st-petersburg/), the [installation process](/plantation-shutters-installation-st-petersburg/), and the [honest trade-offs](/plantation-shutters-regret-downsides/) most dealers skip. All guides are available in our [resource library](/guides/).
  ```

- [ ] **Step 3: Verify /guides/ builds and links render**

  ```bash
  cd cfc-astro && npm run build 2>&1 | tail -3
  ls dist/guides/
  grep -c 'plantation-shutters-cost\|plantation-shutters-installation\|plantation-shutters-regret' dist/guides/index.html
  ```
  Expected: build passes, `dist/guides/` contains `index.html`, grep returns `3`.

- [ ] **Step 4: Commit**

  ```bash
  git add src/pages/guides/index.astro src/content/services/plantation-shutters.md
  git commit -m "feat: add /guides/ collection page with cross-links to plantation shutter guide articles"
  ```

---

## Verification Checklist Before DNS Cutover

Run these after all P0 and P1 tasks are complete:

- [ ] `npm run build` exits 0 with 39+ pages (38 original + /guides/)
- [ ] No meta description ends with `&`, `for.`, `with.`, or any truncation artifact
- [ ] `/about/`, `/contact/`, `/brands/` all have `og:image` pointing to an existing file
- [ ] `dist/plantation-shutters-cost-st-petersburg/index.html` contains a `<table>` tag
- [ ] `dist/services/plantation-shutters/index.html` contains `"@type":"FAQPage"`
- [ ] `dist/about/index.html` contains `"@type":"FAQPage"`
- [ ] `dist/index.html` contains `"@type":"FAQPage"`
- [ ] `dist/index.html` contains `"postalCode":"33712"`
- [ ] `dist/index.html` contains `"@type":"AggregateRating"`
- [ ] `dist/areas/west-st-pete/index.html` contains `352-266-1262`
- [ ] `dist/_headers` exists and contains `Strict-Transport-Security`
- [ ] `dist/llms.txt` exists and contains `Terry Popick`
- [ ] `dist/robots.txt` contains `GPTBot`

---

## Post-DNS Cutover (separate session)

- Re-run PageSpeed Insights on `customfabriccreations.net`
- Submit sitemap to GSC; test URL inspection on 5 sample pages
- Pull CrUX history via `seo-google` skill
- Full `seo-audit` run on the live apex domain
