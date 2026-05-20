// Per-service content for /services/[slug] dynamic routes.
// Kept in one file for easy editing. Each block maps to a full service page.

export interface ServiceBlock {
  slug: string;
  title: string;
  seoTitle: string;
  description: string;
  heroTitle: string;
  heroSubtitle: string;
  sections: Array<{
    heading: string;
    body: string; // HTML/markdown-style paragraphs joined with \n\n
    image?: string; // optional inline image path
  }>;
  faqs: Array<{ q: string; a: string }>;
}

export const SERVICE_CONTENT: Record<string, ServiceBlock> = {
  'plantation-shutters': {
    slug: 'plantation-shutters',
    title: 'Plantation Shutters',
    seoTitle: 'Plantation Shutters in St. Petersburg, FL',
    description: 'Custom plantation shutters in St. Petersburg, FL. Faux wood and basswood built for Florida humidity and Gulf sun. Free in-home consultation.',
    heroTitle: 'Custom Plantation Shutters in St. Petersburg, FL',
    heroSubtitle: 'Looking for plantation shutters in St. Pete? We install custom interior shutters in faux wood and basswood — built for Florida humidity, Gulf sun, and hurricane season. Free in-home consultation across Pinellas County.',
    sections: [
      {
        heading: 'Why Plantation Shutters Work Better in Florida',
        body: `There's a reason plantation shutters have been one of the most requested window treatments in Florida for decades. It's not just about looks — though the look is real. Shutters do something most other window treatments don't: they add structural presence to a window, which changes the feel of an entire room.

They also handle Florida's climate better than almost any other material option, which is why St. Pete homeowners keep choosing them.

But not all plantation shutters are built the same, and the difference shows up fastest in a Florida home. At Custom Fabric Creations, we install custom plantation shutters across St. Pete and the Gulf Coast — measured, fitted, and installed to perform in Florida conditions, not just look good in a showroom photo.`,
        image: '/images/services/plantation-shutters/top.webp',
      },
      {
        heading: 'Faux Wood vs. Real Wood in Florida',
        body: `Most window treatment advice is written for temperate climates. Florida is not a temperate climate. The combination of high humidity, intense UV exposure, and salt air near the coast does things to window treatments that standard materials weren't designed for.

**Faux wood** handles Florida conditions better than almost any other window treatment option. Moisture resistance is the biggest reason — faux wood shutters don't absorb humidity the way real wood does. Swelling, warping, and sticking louvers are problems that come from the wrong material choice, not from shutters generally.

**Real basswood** is still the right call for interior rooms where humidity isn't a factor — studies, offices, formal dining rooms. It takes paint and stain beautifully and has a warmth faux wood can't quite match.

We'll walk every window with you and recommend the right material per room — not a blanket "everything gets faux" or "everything gets wood."`,
        image: '/images/services/plantation-shutters/top-middle.webp',
      },
      {
        heading: 'Precision Measurement and Installation',
        body: `We measure every window in person. Width, height, squareness, depth, obstructions. Rough openings lie. Actual measurements don't. Our lead designer has 25+ years of experience with window treatments in Florida, and that experience shows up in how shutters fit.

Installation is done by our own team — never a subcontractor. A typical home install takes a few hours to a day, depending on window count and complexity. We handle the debris, protect your floors, and don't leave until every louver tracks correctly.`,
        image: '/images/services/plantation-shutters/bottom-middle.webp',
      },
      {
        heading: 'Brands We Install',
        body: `We're an authorized dealer for **Hunter Douglas** NewStyle and **Norman** Woodlore — two of the most respected shutter lines in the industry. Hunter Douglas offers the widest customization (specialty shapes, motorization options, arch tops). Norman is our workhorse for faux wood in Florida homes.

Both come with lifetime limited warranties. Both are built to our exact measurements in the factory, then installed by our team in your home. No big-box shortcuts. No one-size-fits-most.`,
        image: '/images/services/plantation-shutters/bottom.webp',
      },
    ],
    faqs: [
      {
        q: 'How much do plantation shutters cost in St. Petersburg?',
        a: 'Real pricing depends on material (faux wood vs. basswood), window size, and complexity. A typical standard window in faux wood ranges $400–$700 installed; basswood runs $600–$1,000+. Arch tops, French doors, and specialty shapes cost more. We provide a written estimate after in-home measurement.',
      },
      {
        q: 'How long does installation take?',
        a: 'Production takes 4–6 weeks after your order is placed. Installation is usually a half-day to full day depending on how many windows you have.',
      },
      {
        q: 'Will plantation shutters hold up to Florida humidity and sun?',
        a: 'Yes, when you pick the right material for the room. Faux wood handles humidity, bathrooms, and direct sun exposure without warping. Basswood is perfect for dry, lower-UV rooms. We help you pick the right material per window.',
      },
    ],
  },

  'custom-draperies-curtains': {
    slug: 'custom-draperies-curtains',
    title: 'Custom Drapery & Curtains',
    seoTitle: 'Custom Drapery & Curtains in St. Petersburg, FL',
    description: 'Custom drapery and curtains for St. Petersburg homes. Sheer, blackout, and motorized options — sewn in our St. Pete workroom.',
    heroTitle: 'Custom Drapery & Curtains in St. Petersburg',
    heroSubtitle: 'Hand-crafted drapery and curtains, cut and sewn in our St. Pete workroom. From full-length pinch-pleat panels to layered sheers, every drape is measured and finished for your windows.',
    sections: [
      {
        heading: 'Crafted Drapery for the St. Pete Coast',
        body: `Drapery is the single most transformative window treatment in any room. The right panels add scale, warmth, and acoustic softness that shutters and shades simply can't. The wrong ones look boxy, hem-too-short, or out of proportion.

We specialize in floor-length, properly weighted, pleated drapery — the style that reads instantly as custom. We measure to the eighth of an inch, pleat to spec, and hang hardware to ceiling or crown molding when the architecture calls for it.`,
        image: '/images/services/custom-draperies-curtains/top.webp',
      },
      {
        heading: 'Fabrics from Kravet, Stout, and More',
        body: `As an authorized workroom for **Kravet** and **Stout**, we have access to thousands of designer textiles — from heavy cotton velvets to unlined linen sheers. We bring a full sample library to your home so you can see fabrics in your actual light.

**Lined vs. unlined.** Florida sun requires lining. A beautiful silk or linen without lining will fade and rot within a year on a south-facing window. We spec every panel with the right interlining and blackout lining where appropriate.

**Sheer, blackout, or layered.** Bedrooms typically layer a sheer under a blackout. Living rooms often use a single medium-weight unlined panel for softness. Dining rooms can handle heavier formal drapery. We'll guide you through it.`,
        image: '/images/services/custom-draperies-curtains/middle.webp',
      },
      {
        heading: 'Motorized and Manual Hardware',
        body: `Every drapery needs hardware that does two things: support the panel weight without sag, and operate cleanly for years. We spec decorative rods, ripplefold tracks, and motorized systems depending on your window and use case.

For large openings — sliders, floor-to-ceiling glass, curtain walls — we install concealed motorized tracks that open and close on a remote or schedule. These are a quiet luxury most homeowners don't realize is available until they see them work.`,
        image: '/images/services/custom-draperies-curtains/bottom.webp',
      },
    ],
    faqs: [
      {
        q: 'How long does custom drapery take?',
        a: 'Typical production is 4–8 weeks depending on fabric availability. Complex treatments (lined, blackout, motorized) take longer.',
      },
      {
        q: 'Can you match existing fabric?',
        a: 'Often yes. Bring us a swatch and we’ll source a match through Kravet, Stout, or one of our specialty mills.',
      },
      {
        q: 'Do you provide the hardware?',
        a: 'Yes. We supply and install all drapery rods, rings, tracks, and finials. No DIY required.',
      },
    ],
  },

  'window-shades': {
    slug: 'window-shades',
    title: 'Window Shades',
    seoTitle: 'Custom Window Shades in St. Petersburg, FL',
    description: 'Roller, Roman, cellular, solar, and motorized window shades for St. Petersburg homes. Measured and installed by our in-house team.',
    heroTitle: 'Custom Window Shades in St. Petersburg',
    heroSubtitle: 'Roman, cellular, roller, woven wood, and motorized shades — the full range of window shades, measured and installed in-home.',
    sections: [
      {
        heading: 'The Right Shade for Every Window',
        body: `Shades are the most versatile window treatment category. The right pick depends entirely on what you need the window to do — block heat, preserve view, blackout a bedroom, dim a home theater. There is no single "best" shade.

**Roller shades** are our workhorse. Simple, clean, affordable, available in blackout and solar-screen fabrics. Works on almost any window.

**Roman shades** add tailored fabric softness — great for dining rooms, powder baths, and guest bedrooms where drapery would be too much.

**Cellular (honeycomb) shades** are the top performer for energy efficiency. Trap air in the cells, insulate against the heat and cold. Perfect for kitchens and laundry rooms where you want privacy + insulation without the bulk.

**Woven wood (natural shades)** add texture and warmth — an easy upgrade to any room with lots of natural light.

**Solar shades** filter UV and heat while preserving outward visibility. The right call for water-facing windows where you don't want to lose the view.`,
        image: '/images/services/window-shades/top.webp',
      },
      {
        heading: 'Motorized Shades for Large Openings',
        body: `Motorized shades are where technology meets luxury. Quiet, battery or hardwired, controlled via remote or phone app. We install **Hunter Douglas PowerView** and **Norman SmartFit** motorized systems across St. Pete homes with large glass.

Typical use cases: 12-foot sliders in a living room, clerestory windows above the front door, multi-shade great rooms where you want a single "all up / all down" button.`,
        image: '/images/services/window-shades/middle.webp',
      },
      {
        heading: 'Measured Precisely, Installed Professionally',
        body: `Shade accuracy lives or dies at the measurement. A 1/8" error turns a clean inside-mount install into a gappy, light-leaking mess. We measure every window twice, order to spec, and handle the full install.

Most shade installs finish in a half-day. Motorized systems sometimes need a second visit for programming.`,
        image: '/images/services/window-shades/bottom.webp',
      },
    ],
    faqs: [
      {
        q: 'Which shade is best for a bedroom?',
        a: 'Blackout roller shades are the most popular choice — clean, full blackout, affordable. Some clients layer a sheer drapery over for softness.',
      },
      {
        q: 'Do motorized shades require wiring?',
        a: 'Not always. Hunter Douglas PowerView runs on rechargeable batteries. Hardwired options exist for new construction or heavy daily use.',
      },
      {
        q: 'How long do custom shades take?',
        a: '3–6 weeks production depending on brand and fabric, plus a half-day install.',
      },
    ],
  },

  'custom-blinds': {
    slug: 'custom-blinds',
    title: 'Custom Blinds',
    seoTitle: 'Custom Blinds in St. Petersburg, FL',
    description: 'Wood, faux wood, aluminum, and vertical blinds for St. Petersburg homes. Made-to-measure, installed by our team, built to last in Florida conditions.',
    heroTitle: 'Custom Blinds in St. Petersburg, FL',
    heroSubtitle: 'We design, measure, and install made-to-measure blinds built specifically for St. Pete homes — balancing light control, privacy, and style.',
    sections: [
      {
        heading: 'Why Go Custom? Here’s What Off-the-Rack Can’t Give You',
        body: `Most retail blinds come in a set of predetermined widths and lengths. What that means in practice: gaps on the sides, awkward overlaps, and a look that says "I grabbed whatever was available."

Custom blinds eliminate those compromises. **Precise fit, every time.** We measure each window individually. The result is a clean, tailored appearance — the kind that makes a room feel finished rather than accessorized.

**Better light control.** Florida sun doesn't negotiate. Custom blackout blinds, cellular shades, and room-darkening treatments are measured to seal the window properly, not just cover it.

**Options that actually work for your life.** Motorized shades you can control from your phone. Privacy blinds with multiple opacity levels. Plantation shutters that let you redirect light without fully opening the window.`,
        image: '/images/services/custom-blinds/top.webp',
      },
      {
        heading: 'Wood vs. Faux Wood vs. Aluminum',
        body: `**Real wood blinds** offer the richest look — natural grain, stain options, genuine warmth. Best for living rooms, formal dining rooms, home offices. Not recommended for bathrooms or high-humidity spaces.

**Faux wood blinds** deliver 90% of the look at a lower price with far better humidity resistance. Our recommended default for most St. Pete homes — they survive humidity, they're affordable, and the finish quality is better than it used to be.

**Aluminum blinds** are the best value for utility spaces — laundry rooms, garages, home gyms. They won't warp, they're easy to clean, and they come in dozens of colors.`,
        image: '/images/services/custom-blinds/middle.webp',
      },
      {
        heading: 'Cordless and Child-Safe Options',
        body: `Every custom blind we install is child- and pet-safe. Cordless lift systems are standard on all new orders. Motorized systems eliminate cords entirely. Safe, clean, modern.

Our cordless lift mechanisms use a consistent tension system — no looped cords, no pull strings, no strangulation risk. Motorized blinds can be programmed to open and close on schedule, integrate with Alexa or Google Home, and be controlled from your phone.`,
      },
      {
        heading: 'How We Measure, Fabricate, and Install',
        body: `Every custom blind project starts with a complimentary in-home consultation. We bring samples — real wood, faux wood, aluminum, in every available color — so you can hold them up against your trim and flooring in your actual light.

Next we measure every window individually. Inside mount requires at least 2" of depth; outside mount is used when depth is insufficient or when you want to visually enlarge the window.

Fabrication takes 2–4 weeks depending on brand and finish. On install day our team arrives with everything needed — ladders, brackets, hardware, drop cloths — and finishes every window before leaving, with a walk-through to make sure every blind operates cleanly.`,
      },
    ],
    faqs: [
      {
        q: 'How much do custom blinds cost?',
        a: 'Faux wood blinds start around $150–$300 per standard window installed. Real wood and motorized options run higher.',
      },
      {
        q: 'Are custom blinds child-safe?',
        a: 'Yes. All blinds we install are cordless or motorized — no looped cords, no strangulation risk.',
      },
      {
        q: 'Can I order custom blinds for irregular windows?',
        a: 'Yes. We make blinds for arch tops, angled tops, bay windows, and French doors. Specialty shapes require extra measurement time.',
      },
    ],
  },

  'custom-cornices-valances': {
    slug: 'custom-cornices-valances',
    title: 'Cornices & Valances',
    seoTitle: 'Custom Cornices & Valances in St. Petersburg, FL',
    description: 'Custom upholstered cornices and soft valances built to your window dimensions. Fabric valances, box cornices, and layered top treatments.',
    heroTitle: 'Custom Cornices & Valances in St. Petersburg',
    heroSubtitle: 'Top treatments that finish the window right. Custom cornices and valances built in our workroom to your exact window dimensions.',
    sections: [
      {
        heading: 'The Finishing Touch on a Window',
        body: `Cornices and valances are the architectural cap on a window. They hide rod hardware, add height to a room, and soften the visual line between wall and window.

**Box cornices** are upholstered wooden frames — the most formal and architectural option. Great for dining rooms, primary bedrooms, and formal spaces.

**Fabric valances** (swag, scalloped, pleated) add softness without committing to a full drapery. Perfect for kitchens, breakfast nooks, and powder baths.

**Layered top treatments** combine a cornice or valance with drapery or shades underneath — the full custom look.`,
        image: '/images/services/custom-cornices-valances/top.webp',
      },
      {
        heading: 'Built in Our Workroom',
        body: `Every cornice and valance is built in our St. Pete workroom. Frames cut, fabric stretched, welting applied, trim added — all by hand. We match fabric to your drapery, shades, or upholstery so the whole room reads as one composition.`,
        image: '/images/services/custom-cornices-valances/middle.webp',
      },
      {
        heading: 'Sized to Your Architecture',
        body: `We size cornice heights proportionate to the ceiling and window — never a standard "one height fits all." A 10-foot ceiling calls for a taller cornice than an 8-foot ceiling. These proportions are what separate custom work from factory boxes.

For living rooms, dining rooms, and primary bedrooms, we typically spec cornices between 12 and 20 inches tall, with the bottom edge 4–6 inches below the top of the window. The exact ratio depends on window-to-ceiling gap and the visual weight of the drapery underneath.`,
      },
      {
        heading: 'Coordinating with Drapery, Shades, and Upholstery',
        body: `Cornices and valances rarely stand alone. They sit above drapery, roman shades, or motorized systems. The magic is in how those layers coordinate.

We typically pick cornice fabric that either matches drapery exactly (most formal), picks up a secondary color from the drapery (more relaxed), or pulls from a nearby upholstered piece (sofa, headboard, accent chair). The result is a room that reads as designed rather than decorated.

Every cornice frame is built to exact window width plus appropriate returns for the drapery hardware below. We handle the coordination so the whole window treatment composition reads as one piece.`,
        image: '/images/services/custom-cornices-valances/bottom.webp',
      },
    ],
    faqs: [
      {
        q: 'Can a cornice go over existing blinds or shades?',
        a: 'Yes. Cornices and valances layer beautifully over almost any window treatment.',
      },
      {
        q: 'How long do custom cornices take?',
        a: '4–6 weeks including fabrication and finishing in our workroom.',
      },
      {
        q: 'What’s the difference between a cornice and a valance?',
        a: 'A cornice is a structured, upholstered wood frame. A valance is soft fabric only, usually gathered, pleated, or swagged. Cornices are more architectural; valances are more decorative.',
      },
    ],
  },

  'drapery-hardware': {
    slug: 'drapery-hardware',
    title: 'Drapery Hardware',
    seoTitle: 'Drapery Hardware in St. Petersburg, FL',
    description: 'Custom drapery rods, rings, finials, and motorized tracks for St. Petersburg homes. Decorative and concealed hardware options.',
    heroTitle: 'Drapery Hardware in St. Petersburg',
    heroSubtitle: 'Decorative rods, concealed tracks, motorized systems, and finials — the hardware that makes drapery look finished.',
    sections: [
      {
        heading: 'Hardware That Holds Up',
        body: `Most drapery failures aren't fabric failures — they're hardware failures. Sagging rods, loose brackets, finials that fall off, tracks that stick. The right hardware does two things: supports the drapery weight for decades and operates silently.

We supply and install decorative rods, ripplefold tracks, motorized systems, and specialty hardware for every type of drapery we sell.`,
        image: '/images/services/drapery-hardware/top.webp',
      },
      {
        heading: 'Decorative vs. Concealed',
        body: `**Decorative rods** are meant to be seen — wrought iron, polished brass, wood, acrylic. They carry most traditional and transitional drapery.

**Concealed tracks** are meant to disappear. Install behind crown molding or drywall. The drapery floats from nowhere. The modern luxury look.

**Ripplefold tracks** give drapery a clean, wavy modern profile — contract-grade and residential-grade options.`,
        image: '/images/services/drapery-hardware/middle.webp',
      },
      {
        heading: 'Motorization',
        body: `We install motorized drapery tracks from Somfy, Rollease Acmeda, and Lutron. Quiet operation, remote control, and schedule integration with smart home systems like Control4, Savant, and Crestron.

Battery-powered systems use rechargeable lithium-ion packs that last 6–12 months between charges — good for retrofits in homes where running wires isn’t practical. Hardwired systems are the right choice for new construction and major renovations where the wall is already open.`,
        image: '/images/services/drapery-hardware/bottom.webp',
      },
      {
        heading: 'Installation That Holds',
        body: `Drapery hardware has to anchor into something structural. Drywall alone won’t support heavy linen or velvet panels over a long span. We locate studs, use toggle anchors where needed, and install ceiling-mount brackets in older St. Pete homes where window trim is decorative rather than structural.

Every installation includes a weight calculation — we spec hardware that supports at least 2x the drapery weight, with a safety margin for dynamic loads from opening and closing. Rods don’t sag, brackets don’t pull out, finials don’t fall off. Built to last.`,
      },
    ],
    faqs: [
      {
        q: 'Can you match my existing drapery hardware?',
        a: 'Usually yes. Bring us photos and measurements and we’ll source the closest match.',
      },
      {
        q: 'Do you install ripplefold (modern) drapery tracks?',
        a: 'Yes. Ripplefold is our most-requested modern track. Clean, simple, no pinch pleats. We carry residential and contract-grade ripplefold systems.',
      },
    ],
  },

  'outdoor-window-shades': {
    slug: 'outdoor-window-shades',
    title: 'Outdoor Window Shades',
    seoTitle: 'Outdoor Window Shades in St. Petersburg, FL',
    description: 'Patio shades, solar screens, and exterior window treatments for St. Petersburg homes — built for Florida sun, wind, and salt air.',
    heroTitle: 'Outdoor Window Shades in St. Petersburg',
    heroSubtitle: 'Exterior solar screens, lanai shades, and patio treatments built for Florida sun, wind, and salt air. Protect your furniture and your view.',
    sections: [
      {
        heading: 'Shade for Lanais, Patios, and Pool Cages',
        body: `A Florida lanai without shade is unusable half the year. Mid-day sun turns outdoor living space into an oven; afternoon rain turns it into a sponge. Properly specified exterior shades fix both.

**Solar screen shades** filter 90% of UV while preserving outward visibility. Drop them when the sun's direct; retract them when the afternoon breeze picks up.

**Weatherproof roller shades** are motorized, wind-rated, and built with aluminum housing to survive Florida storms. These stay up year-round on screened lanais.

**Bug-screen shades** double as insect barriers — clear bug mesh built into the shade fabric. One system, two jobs.`,
        image: '/images/services/outdoor-window-shades/hero.webp',
      },
      {
        heading: 'Materials That Survive Florida',
        body: `Standard indoor shade fabrics disintegrate outdoors in Florida within a season. Everything we install outdoors is UV-stabilized, marine-grade, and rated for coastal installation.

We've installed exterior shades in Tierra Verde, St. Pete Beach, Treasure Island, and other salt-air environments — we know which products hold up. Phifer SheerWeave, Hunter Douglas exterior lines, and Insolroll exterior shades are our go-to brands for Florida coastal conditions.`,
        image: '/images/services/outdoor-window-shades/bottom.webp',
      },
      {
        heading: 'Pool Cages, Lanais, and Covered Patios',
        body: `Florida outdoor living is different from most of the country. Pool cages are technically screened outdoor rooms. Lanais are open-air but covered. Covered patios are exposed to rain and wind. Each has slightly different requirements.

For **pool cages**, we typically install solar screens on the sunny side to cut UV without restricting airflow. For **lanais**, we install motorized drop-down shades that can be closed during midday sun or afternoon rain. For **fully exposed patios**, we use wind-rated weatherproof systems that retract into protective housing during storms.

We also install bug-mesh shades that double as insect barriers — valuable for evenings when the no-see-ums are active.`,
      },
    ],
    faqs: [
      {
        q: 'Can outdoor shades handle hurricane winds?',
        a: 'Properly installed motorized exterior shades are wind-rated to 90+ mph. For stronger storms we recommend retracting before landfall.',
      },
      {
        q: 'Are solar screens see-through?',
        a: 'Yes — from inside you keep your view. From outside they provide privacy during daylight hours.',
      },
    ],
  },

  'furniture-reupholstery': {
    slug: 'furniture-reupholstery',
    title: 'Furniture Reupholstery',
    seoTitle: 'Furniture Reupholstery in St. Petersburg, FL',
    description: 'Frame-up furniture reupholstery in St. Petersburg. Sofas, chairs, sectionals, headboards, ottomans — restored with Kravet and Stout fabrics.',
    heroTitle: 'Furniture Reupholstery in St. Petersburg',
    heroSubtitle: 'Bring a cherished chair, sofa, or headboard back to life. Frame-up reupholstery with designer fabrics from Kravet, Stout, and beyond.',
    sections: [
      {
        heading: 'Why Reupholster Instead of Replace',
        body: `Well-built vintage and antique furniture is better constructed than almost anything you can buy new. Solid hardwood frames, coil springs, hand-tied knots — you can't buy that quality at a modern furniture store, at any price.

Reupholstery restores the piece you love to like-new condition with a fabric of your choice. It's usually 40–60% the cost of a new comparable-quality piece, and the finished product will outlast any new import.`,
        image: '/images/services/furniture-reupholstery/top.webp',
      },
      {
        heading: 'Frame-Up Restoration',
        body: `Our reupholstery is frame-up — every piece is stripped down to bare wood. We inspect and re-glue the frame, retie the springs, re-webb the base, and rebuild the foam and batting to period-correct specifications.

Then we apply the fabric of your choice. Kravet, Stout, Fabricut, or a fabric you bring yourself (COM — customer's own material).`,
        image: '/images/services/furniture-reupholstery/bottom.webp',
      },
      {
        heading: 'What We Work On',
        body: `Sofas, sectionals, wingback chairs, Louis XV and Louis XVI chairs, Chesterfield sofas, ottomans, benches, banquettes, headboards, dining chairs, outdoor cushions, boat cushions.

If it has fabric and a frame, we probably work on it. Antique heirlooms, mid-century furniture, estate pieces, and commercial-grade hospitality seating all pass through our workroom regularly.`,
      },
      {
        heading: 'When Reupholstery Makes Sense — and When It Doesn’t',
        body: `Reupholstery is worth doing on pieces with **solid hardwood frames** (usually pre-1980s), **coil or 8-way hand-tied springs**, and **sentimental or aesthetic value** worth preserving. Estate-quality furniture, family heirlooms, custom-built pieces — all worth restoring.

Reupholstery is **not** worth doing on **particleboard-frame furniture**, **stapled-web seating** (the cheap stuff), or pieces with **structural damage** in the frame. We’ll tell you honestly during consultation if we think a piece isn’t worth the investment.

For borderline cases, we can do a full inspection during pickup and give you a go/no-go recommendation before starting work.`,
      },
    ],
    faqs: [
      {
        q: 'How much does reupholstery cost?',
        a: 'Varies widely by piece and fabric. A wingback chair typically runs $800–$1,500 including labor and mid-range fabric. A sofa $2,500–$5,000. We provide a written estimate after seeing the piece.',
      },
      {
        q: 'How long does it take?',
        a: 'Typical reupholstery is 4–8 weeks depending on fabric availability and frame repair scope.',
      },
      {
        q: 'Can I bring my own fabric?',
        a: 'Yes. We welcome COM (customer’s own material) with a fabric inspection on drop-off.',
      },
    ],
  },

  'custom-bedding-pillows': {
    slug: 'custom-bedding-pillows',
    title: 'Custom Bedding & Pillows',
    seoTitle: 'Custom Bedding & Pillows in St. Petersburg, FL',
    description: 'Custom duvets, shams, pillows, headboards, bed skirts — made to your bed dimensions in our St. Petersburg workroom.',
    heroTitle: 'Custom Bedding & Pillows in St. Petersburg',
    heroSubtitle: 'Custom headboards, bed skirts, duvets, shams, and throw pillows. The bedding that finishes the room.',
    sections: [
      {
        heading: 'Bedding, Tailored Like Drapery',
        body: `Most retail bedding is sized for the box. Real bed dimensions — especially on custom or antique beds — don't match retail sizing. The result: duvets that drape wrong, bed skirts that ripple, shams that don't match your pillows.

Custom bedding fixes all of that. We measure your bed, build the duvet to hang exactly the way you want, sew bed skirts in the exact drop length for your frame, and match shams to throw pillows to headboards for a finished look.`,
        image: '/images/services/custom-bedding-pillows/hero.webp',
      },
      {
        heading: 'What We Make',
        body: `Duvets and duvet covers · bed skirts · pillow shams (Euro, standard, king) · decorative throw pillows · upholstered headboards · bench cushions · window seat cushions · daybed covers · bolster pillows.

Every piece is cut and sewn in our St. Pete workroom. We can match fabrics across a full bedroom composition — drapery, bedding, headboard, and throw pillows all coordinated.`,
        image: '/images/services/custom-bedding-pillows/bottom.webp',
      },
      {
        heading: 'Headboards',
        body: `A custom upholstered headboard is one of the highest-impact changes you can make to a primary bedroom. We build headboards to any height, shape, tufting pattern, and fabric. Nailhead trim, welting, and button tufting all available.

Standard residential headboard heights run 54–66 inches, but we regularly build 72–84 inch headboards for high-ceiling bedrooms where a standard-height piece would look undersized. Tall wingback silhouettes, channel-tufted contemporary designs, and classic button-tufted shapes are all in our portfolio.`,
      },
      {
        heading: 'Coordinating a Full Bedroom',
        body: `The most striking bedrooms we’ve done coordinate drapery, bedding, throw pillows, headboard, and sometimes a bench at the foot of the bed — all in a considered palette across 2–4 fabrics.

We plan the whole composition together. A feature fabric on the headboard. A secondary solid on the drapery. A tertiary pattern on throw pillows and shams. The result reads as a curated suite, not a collection of individually-purchased items.`,
      },
    ],
    faqs: [
      {
        q: 'Can you match my existing drapery fabric?',
        a: 'Yes. If the fabric is still available, we’ll order matching yardage. If it’s discontinued, we’ll source a close match.',
      },
      {
        q: 'How long does custom bedding take?',
        a: '4–6 weeks typical production.',
      },
      {
        q: 'Can you build a custom headboard for my existing bed frame?',
        a: 'Yes. We need the bed frame dimensions and mounting approach. Most headboards mount to standard metal bed frames with adjustable bolts.',
      },
    ],
  },

  'custom-banquettes': {
    slug: 'custom-banquettes',
    title: 'Custom Banquettes',
    seoTitle: 'Custom Banquettes in St. Petersburg, FL',
    description: 'Built-in banquette seating for St. Petersburg dining nooks, kitchens, and window seats. Cushions, backs, and details built to last.',
    heroTitle: 'Custom Banquettes in St. Petersburg',
    heroSubtitle: 'Built-in banquette seating for dining nooks and kitchens. Cushions, backs, and details designed to last.',
    sections: [
      {
        heading: 'Banquettes Done Right',
        body: `A well-designed banquette is the warmest seat in a house. It turns a breakfast nook into the room the family actually uses. It adds seating without the visual bulk of chairs. It lets you seat more people at a smaller footprint.

A poorly designed banquette is an uncomfortable, squeaky, non-cleanable mess. The difference is almost always in the cushion construction and the fabric choice.`,
        image: '/images/services/custom-bedding-pillows/hero.webp',
      },
      {
        heading: 'Cushion Construction',
        body: `We build banquette cushions with a foam + down wrap core, hand-stitched welting, and a removable cover for cleaning. Zipper access, Scotchguard treatment, and fabric-backed cushions that won't slide.`,
      },
      {
        heading: 'Backs and Side Panels',
        body: `Full upholstered backs — tufted, nailheaded, or smooth — take a banquette from "bench with a pillow" to "built-in bespoke seating." We design these in consultation with your builder, cabinetmaker, or designer.

Channel-tufted banquette backs are particularly popular right now — clean vertical lines that look tailored without being overly traditional. Button-tufted backs read more classic. Smooth upholstered backs with a decorative welting line read most modern.`,
      },
      {
        heading: 'Breakfast Nook and Kitchen Banquettes',
        body: `The most common CFC banquette project is a breakfast nook — an L-shaped or U-shaped bench built into a kitchen corner with a pedestal table in front. This configuration seats 5–6 people in a space that would fit 2 chairs, and feels like a cafe.

For kitchen banquettes, we recommend indoor-outdoor performance fabrics from Sunbrella or Crypton — spill-resistant, bleach-cleanable, and kid/pet-friendly. Hidden zippers on cushion covers make seasonal cleaning easy.`,
      },
      {
        heading: 'Window Seats and Custom Built-In Seating',
        body: `Beyond kitchen banquettes, we build cushions, backs, and upholstery for window seats, bay window nooks, mudroom benches, hallway benches, and custom built-in seating throughout the home. Any built-in seating benefits from a properly sized, properly filled, removable-cover cushion — the difference between "hard seat with a pillow" and "actual comfortable seating you’ll actually use."

We coordinate with your builder, designer, or cabinetmaker on cushion sizing, fabric selection, and any upholstered back or side panels. Every cushion includes a zippered cover for cleaning, proper foam density for the use case, and welting or piping to tighten the profile.`,
      },
    ],
    faqs: [
      {
        q: 'Do you build the banquette frame too?',
        a: 'We coordinate with your builder or cabinetmaker on the wood frame. We build the cushions, backs, and upholstery. If you don’t have a builder, we have partners we can recommend.',
      },
      {
        q: 'What’s the right cushion depth for a banquette?',
        a: 'Seat depth is typically 18–22 inches. Cushion thickness runs 3–6 inches depending on comfort preference and aesthetic. We mock it up during consultation.',
      },
    ],
  },

  'commercial-window-treatments': {
    slug: 'commercial-window-treatments',
    title: 'Commercial Window Treatments',
    seoTitle: 'Commercial Window Treatments in St. Petersburg, FL',
    description: 'Window treatments for St. Petersburg hotels, restaurants, medical offices, and commercial properties. Contract-grade materials, scheduled installation.',
    heroTitle: 'Commercial Window Treatments in St. Petersburg',
    heroSubtitle: 'Window treatments for hotels, restaurants, medical offices, and commercial properties across the St. Pete coast. Contract-grade materials, scheduled installation.',
    sections: [
      {
        heading: 'Contract-Grade, Not Residential',
        body: `Commercial environments demand different materials, fire ratings, and warranties than residential installations. We install contract-grade window treatments that meet NFPA 701 flame resistance, ADA-compliant operation, and commercial warranty standards.

Typical commercial projects: hotel guest rooms, restaurant dining rooms, medical exam rooms, corporate offices, multi-family apartment buildouts, waiting rooms, conference spaces.`,
        image: '/images/services/commercial-window-treatments/hero.webp',
      },
      {
        heading: 'Scheduled Installation',
        body: `We work around your operations. After-hours installs for occupied hotels and restaurants. Weekend work for offices. Phased installs for multi-floor buildings. Our install team has been doing commercial work for 20+ years — we know how to finish without disrupting your business.`,
        image: '/images/services/commercial-window-treatments/bottom.webp',
      },
      {
        heading: 'Product Range',
        body: `Motorized solar shades · blackout roller shades · drapery with hospital track · cubicle curtains · hurricane-rated exterior screens · commercial plantation shutters · contract-grade upholstery.

Every product we install for commercial clients meets or exceeds relevant building code — fire ratings, ADA operation, warranty terms. We handle the spec sheets, submittals, and closeout documentation that commercial GCs and architects require.`,
      },
      {
        heading: 'Specifying for Architects and GCs',
        body: `We work with architects, general contractors, and design-build firms across the St. Pete area. We provide CSI-format spec sheets, compete with national bids on pricing, and hold CGL insurance appropriate for commercial jobsites.

If you’re spec’ing window treatments on a new commercial build — hotel, restaurant, office, medical, multi-family — we’d love the chance to bid. Call (727) 914-5410 or email info@customfabriccreations.net.`,
      },
      {
        heading: 'Multi-Phase and Repeat Projects',
        body: `For property managers and corporate clients, we handle multi-phase rollouts and ongoing replacement contracts. Hotel guest room refreshes, corporate office suite updates, multi-unit apartment turnovers, and restaurant tenant improvements all benefit from a single point of contact who knows the property and the product specifications.

We keep spec records so that follow-up phases match the original install exactly — same fabric, same finish, same hardware — even years later.`,
      },
    ],
    faqs: [
      {
        q: 'Do you work on multi-unit properties?',
        a: 'Yes. We’ve done apartment complexes, condo communities, hotel rollouts. Contact us with your property size and we’ll put together a proposal.',
      },
      {
        q: 'Can you meet fire-safety codes?',
        a: 'Yes. All commercial fabrics we install are NFPA 701 rated or inherently flame-resistant.',
      },
    ],
  },

  'services-interior-decor-tampa': {
    slug: 'services-interior-decor-tampa',
    title: 'Interior Decor Consultation',
    seoTitle: 'Interior Design Consultation in St. Petersburg, FL',
    description: 'Interior design consultation in St. Petersburg focused on custom window treatments, bedding, cushions, and soft goods. 25+ years of design experience.',
    heroTitle: 'Interior Design & Products in St. Petersburg',
    heroSubtitle: 'We help you develop a cohesive design direction — room by room. Focused specifically on window treatments, bedding, and upholstered soft goods.',
    sections: [
      {
        heading: 'Design Services Focused on Soft Goods',
        body: `Most interior designers work across every category — furniture, rugs, lighting, paint, art, window treatments. That's a valuable service, but it's not what we do.

We focus specifically on soft goods — window treatments, bedding, upholstery, cushions, pillows. This is what we've built over 25+ years, and it's where we can add the most value.

If you're working with another designer on the broader room, we love collaborating. If you're going it alone and just need guidance on the window and fabric decisions, we can walk you through it.`,
        image: '/images/services/services-interior-decor-tampa/top.webp',
      },
      {
        heading: 'How We Work',
        body: `**Discovery call.** We start with a conversation about the room, your style, your budget, and what's already in place.

**In-home consultation.** We come to you with a full fabric library. You see textiles in your actual light, against your actual walls and furniture.

**Design direction.** We present 2–3 directions for each window and piece. You pick what resonates.

**Quotation.** Written estimate for all recommended items.

**Fabrication and install.** Everything is built in our workroom and installed by our team.`,
        image: '/images/services/services-interior-decor-tampa/bottom.webp',
      },
      {
        heading: 'Whole-Room and Whole-Home Projects',
        body: `We take on projects ranging from a single-window refresh to whole-home window treatment packages. Most common project size: 3–5 rooms at once, typically the ones a family spends the most time in.

For whole-home projects, we coordinate a unified palette across primary living spaces. Drapery in the formal living room pairs with bedding in the primary bedroom. Shades in the kitchen coordinate with window treatments in the breakfast nook. Every decision connects to the next.`,
      },
      {
        heading: 'What We Don’t Do',
        body: `We’re focused specifically on the soft-goods layer of interior design. That means we don’t pick paint colors, rugs, art, lighting fixtures, or furniture. We don’t redesign kitchens or baths. We don’t do tile or flooring selection.

What we do is the soft goods — window treatments, bedding, upholstery, cushions, headboards, pillows — with the depth of specialization that comes from 25+ years of doing only this. If you need a full interior designer, we can refer you to trusted partners in the St. Pete area. If you need the soft-goods expert on your project team, that’s us.`,
      },
    ],
    faqs: [
      {
        q: 'Do you charge for the consultation?',
        a: 'First in-home consultation is free. Ongoing design work beyond that is billed at an hourly rate.',
      },
      {
        q: 'Can you work with my existing designer?',
        a: 'Absolutely. We collaborate with designers regularly.',
      },
    ],
  },
};
