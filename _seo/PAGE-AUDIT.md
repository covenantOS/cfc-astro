# Per-Page Audit — customfabriccreations.net (pre-migration)

**Pulled:** 2026-04-22 · 36 pages scraped · GSC 28-day window

## How to read this

Each page block shows the current state on the live WordPress site:
- **Words / images / clicks / impressions** — scrape + GSC data
- **Title** — current `<title>` text + character count
- **Desc** — current meta description + character count (`0c` = missing)
- **H1s** — extracted `<h1>` text (should be exactly 1)
- **Schema** — JSON-LD types emitted on the page
- **Flags** — issues to fix in port
- **Ranking for** — queries generating impressions (only shown if any)

## Flag legend

| Flag | Meaning |
|---|---|
| `Ocala(N)` | `N` occurrences of \u201cocala\u201d or \u201cmarion county\u201d in body — **rewrite during port** |
| `Title>65c` | Title too long, will truncate in SERPs |
| `Title<35c` | Title too thin, weak SEO value |
| `NoDesc` | No meta description |
| `Desc>160c` | Meta description truncates |
| `NoH1` / `MultiH1` | H1 count wrong |
| `Thin(Xw)` | Under 500-word page |
| `BadSchema(Article)` | Emits `Article` schema on a non-article page — confuses Google about page type |
| `MissingSchema(Service)` | Service page missing `Service` JSON-LD |

## Systemic findings

1. **Every page emits `Article` schema** (except `/contact/`). That\u2019s wrong for service pages, area pages, and hub pages. Article = blog post. Strip on all non-blog pages in the port. **Only the 3 plantation-shutters guides should keep `Article`.**

2. **Every page declares `Place` with geo `31.72424340, -85.67212060`** — **these are Alabama coordinates**. Replace with `27.7676, -82.6403` (St. Petersburg, FL).

3. **26 of 36 titles exceed 65 characters.** The titles appear to be H1s rendered as `<title>` rather than hand-written. The Astro `BaseLayout` already formats titles correctly (`Page Title | Custom Fabric Creations`, joined only when needed); rewrite each page\u2019s title to \u226460c during port.

4. **Service pages say \u201cCentral Florida\u201d instead of \u201cSt. Petersburg\u201d** — that\u2019s too broad. Central Florida means Orlando market to Google. **Change every service page\u2019s targeting to \u201cSt. Petersburg\u201d** during port.

5. **Area pages use the \u201cBlinds Shop\u201d positioning in title/H1** (e.g., \u201cClearwater Blinds Shop | Custom Window Treatments...\u201d). This is intentional positioning for a high-commercial KW. Decide whether to preserve it or shift to \u201cWindow Treatments\u201d — **recommend shifting** because it\u2019s both more accurate (we sell drapery, shutters, upholstery — not just blinds) and more aligned with the luxury direction. Capture the redirect/preservation decision in `URL-MAP.md`.

6. **The 3 plantation-shutters guides already have strong schema** (Article + FAQPage + HowTo). Keep the pattern and extend it to other service/guide pages where FAQs exist.

7. **Near-zero ranking surface**: only `/` gets GSC impressions, and every ranking query is a legacy Ocala keyword. Treat the migration as a greenfield optimization pass, not a defensive preservation.

---

## Per-page details

- **`/`** (879w, 13img, clicks=5, imp=392)
  - Title (30c): Home - Custom Fabric Creations
  - Desc (0c): *(missing)*
  - H1s (1): Custom Window Treatments and Bespoke Upholstery
  - Schema: Article, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title<35c, NoDesc, BadSchema(Article)
  - Ranking for: interior window covering ocala fl, window treatments ocala fl, indoor window treatments ocala fl, window treatment options ocala fl, kitchen window coverings ocala fl

- **`/about/`** (825w, 5img, clicks=0, imp=0)
  - Title (31c): About - Custom Fabric Creations
  - Desc (0c): *(missing)*
  - H1s (1): About Custom Fabric Creations
  - Schema: AboutPage, BreadcrumbList, LocalBusiness, Organization, Person, Place, WebSite
  - **Flags:** Ocala(1), Title<35c, NoDesc

- **`/brands/`** (240w, 8img, clicks=0, imp=0)
  - Title (32c): Brands - Custom Fabric Creations
  - Desc (0c): *(missing)*
  - H1s (0): 
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title<35c, NoDesc, NoH1, Thin(240w), BadSchema(Article)

- **`/contact/`** (337w, 1img, clicks=0, imp=0)
  - Title (33c): Contact - Custom Fabric Creations
  - Desc (0c): *(missing)*
  - H1s (1): Schedule Your Design Consultation
  - Schema: BreadcrumbList, ContactPage, LocalBusiness, Place, WebSite
  - **Flags:** Title<35c, NoDesc, Thin(337w)

- **`/gallery/`** (218w, 10img, clicks=0, imp=0)
  - Title (33c): Gallery - Custom Fabric Creations
  - Desc (0c): *(missing)*
  - H1s (0): 
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title<35c, NoDesc, NoH1, Thin(218w), BadSchema(Article)

- **`/services/`** (873w, 13img, clicks=0, imp=0)
  - Title (34c): Services - Custom Fabric Creations
  - Desc (0c): *(missing)*
  - H1s (1): Custom Window Treatments and Master Upholstery
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Ocala(1), Title<35c, NoDesc, BadSchema(Article)

- **`/services/custom-draperies-curtains/`** (1245w, 6img, clicks=0, imp=0)
  - Title (98c): Custom Draperies &amp; Curtains Central Florida \| Made-to-Measure Curtains &amp; Window Treatments
  - Desc (183c): Custom draperies &amp; curtains made to your exact windows in Central Florida. Sheer, blackout, motorized &amp; luxury d
  - H1s (1): Custom Draperies & Curtains in Central Florida
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Ocala(2), Title>65c, Desc>160c, BadSchema(Article), MissingSchema(Service)

- **`/services/plantation-shutters/`** (3495w, 6img, clicks=0, imp=0)
  - Title (80c): Plantation Shutters St. Petersburg FL \| Faux Wood &amp; Custom Interior Shutters
  - Desc (180c): Custom plantation shutters in St. Petersburg, FL. Faux wood &amp; basswood built for Florida humidity, Gulf sun, hurrica
  - H1s (1): Custom Plantation Shutters in St. Petersburg, FL
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article), MissingSchema(Service)

- **`/services/window-shades/`** (1430w, 5img, clicks=0, imp=0)
  - Title (74c): Window Shades Central Florida \| Roller, Roman, Solar &amp; Blackout Shades
  - Desc (202c): Custom window shades in Central Florida built for Florida&#039;s sun &amp; humidity. Roller, roman, solar, cellular &amp
  - H1s (1): Window Shades in Central Florida
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article), MissingSchema(Service)

- **`/services/custom-blinds/`** (1124w, 3img, clicks=0, imp=0)
  - Title (88c): ustom Blinds Central Florida \| Made-to-Measure Window Treatments Custom Fabric Creations
  - Desc (228c): Looking for custom blinds in Central Florida? Custom Fabric Creations designs and installs made-to-measure window treatm
  - H1s (1): Custom Blinds in Central Florida
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Ocala(2), Title>65c, Desc>160c, BadSchema(Article), MissingSchema(Service)

- **`/services/custom-cornices-valances/`** (1494w, 5img, clicks=0, imp=0)
  - Title (95c): Custom Cornices &amp; Valances in Central Florida � Top Treatments That Finish the Window Right
  - Desc (180c): Custom cornices &amp; valances in Central Florida, built to your exact window dimensions. Fabric valances, box cornices 
  - H1s (1): Custom Cornices & Valances in Central Florida
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Ocala(2), Title>65c, Desc>160c, BadSchema(Article), MissingSchema(Service)

- **`/services/drapery-hardware/`** (1548w, 7img, clicks=0, imp=0)
  - Title (79c): Drapery Hardware Central Florida \| Curtain Rods, Tracks &amp; Motorized Systems
  - Desc (193c): Drapery hardware supply &amp; installation in Central Florida. Decorative rods, concealed tracks, motorized systems &amp
  - H1s (1): Drapery Hardware in Central Florida
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article), MissingSchema(Service)

- **`/services/outdoor-window-shades/`** (1456w, 3img, clicks=0, imp=0)
  - Title (91c): Outdoor Window Shades Central Florida \| Patio Shades, Solar Screens &amp; Exterior Curtains
  - Desc (207c): Outdoor window shades &amp; exterior treatments for Central Florida homes. Solar screens, patio shades, outdoor curtains
  - H1s (1): Outdoor Window Shades in Central Florida
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Ocala(2), Title>65c, Desc>160c, BadSchema(Article), MissingSchema(Service)

- **`/services/furniture-reupholstery/`** (1308w, 4img, clicks=0, imp=0)
  - Title (78c): Furniture Reupholstery Central Florida \| Sofas, Chairs &amp; Custom Upholstery
  - Desc (176c): Expert furniture reupholstery in Central Florida. We restore sofas, chairs, sectionals &amp; more with premium fabrics. 
  - H1s (1): Furniture Reupholstery in Central Florida
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article), MissingSchema(Service)

- **`/services/custom-bedding-pillows/`** (1560w, 3img, clicks=0, imp=0)
  - Title (80c): Custom Bedding Central Florida \| Duvet Covers, Pillow Shams &amp; Accent Pillows
  - Desc (195c): Custom bedding made to your exact bed dimensions in St. Petersburg. Duvet covers, pillow shams, accent pillows &amp; cus
  - H1s (1): Custom Bedding & Pillows in Central Florida
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Ocala(2), Title>65c, Desc>160c, BadSchema(Article), MissingSchema(Service)

- **`/services/custom-banquettes/`** (972w, 3img, clicks=0, imp=0)
  - Title (43c): Custom Banquettes - Custom Fabric Creations
  - Desc (0c): *(missing)*
  - H1s (1): Custom Banquettes in Central Florida
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Ocala(2), NoDesc, BadSchema(Article), MissingSchema(Service)

- **`/services/commercial-window-treatments/`** (1382w, 5img, clicks=0, imp=0)
  - Title (79c): Commercial Window Treatments Central Florida \| Office Blinds &amp; Solar Shades
  - Desc (189c): Commercial window treatments for offices, medical spaces, restaurants &amp; multi-family properties in Central Florida. 
  - H1s (1): Commercial Window Treatments in Central Florida
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Ocala(2), Title>65c, Desc>160c, BadSchema(Article), MissingSchema(Service)

- **`/services/services-interior-decor-tampa/`** (1453w, 5img, clicks=0, imp=0)
  - Title (75c): Interior Design Central Florida \| Custom Window Treatments &amp; Home Decor
  - Desc (168c): Interior design services in Central Florida focused on custom window treatments, bedding, cushions &amp; soft goods. 25+
  - H1s (1): Interior Design & Products in Central Florida
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Ocala(2), Title>65c, Desc>160c, BadSchema(Article), MissingSchema(Service)

- **`/areas/`** (938w, 16img, clicks=0, imp=0)
  - Title (31c): Areas - Custom Fabric Creations
  - Desc (0c): *(missing)*
  - H1s (1): Bespoke Window Treatments and Master Upholstery
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title<35c, NoDesc, BadSchema(Article)

- **`/areas/st-petersburg/`** (2228w, 3img, clicks=0, imp=0)
  - Title (82c): Blinds Shop St. Petersburg FL \| Custom Window Treatments \| Custom Fabric Creations
  - Desc (200c): St. Petersburg&#039;s premier blinds shop offering custom plantation shutters, blinds, shades &amp; motorized blinds. Fr
  - H1s (1): Blinds Shop & Custom Window Treatment St. Petersburg FL
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article)

- **`/areas/downtown-st-pete/`** (3015w, 3img, clicks=0, imp=0)
  - Title (101c): Downtown St. Pete Blinds Shop \| Custom Window Treatments &amp; Solar Shades \| Custom Fabric Creations
  - Desc (216c): Downtown St. Petersburg&#039;s premier blinds shop offering solar shades for heat control, blackout roller shades &amp; 
  - H1s (1): Blinds Shop & Custom Window Treatments in Downtown St. Pete FL
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article)

- **`/areas/old-northeast/`** (2729w, 3img, clicks=0, imp=0)
  - Title (104c): Old Northeast Blinds Shop \| Custom Window Treatments &amp; Plantation Shutters \| Custom Fabric Creations
  - Desc (215c): Old Northeast St. Petersburg&#039;s trusted blinds shop offering custom plantation shutters, blackout curtains, roller &
  - H1s (1): Blinds Shop & Custom Window Treatment Historic Old Northeast FL
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article)

- **`/areas/snell-isle/`** (2525w, 3img, clicks=0, imp=0)
  - Title (95c): Snell Isle Blinds Shop \| Custom Window Treatments &amp; Roller Shades \| Custom Fabric Creations
  - Desc (198c): Snell Isle&#039;s premier blinds shop offering roller shades, motorized window treatments &amp; custom plantation shutte
  - H1s (1): Blinds Shop & Custom Window Treatment Snell Isle FL
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article)

- **`/areas/shore-acres/`** (2964w, 3img, clicks=0, imp=0)
  - Title (105c): Shore Acres Blinds Shop \| Custom Window Treatments &amp; Motorized Solar Shades \| Custom Fabric Creations
  - Desc (202c): Shore Acres FL&#039;s premier blinds shop offering motorized solar shades, cordless cellular shades &amp; custom plantat
  - H1s (1): Blinds Shop & Custom Window Treatment in Shore Acres FL
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article)

- **`/areas/west-st-pete/`** (772w, 3img, clicks=0, imp=0)
  - Title (75c): West St. Petersburg FL \| Custom Window Treatments \| Custom Fabric Creations
  - Desc (205c): West St. Petersburg&#039;s premier blinds shop offering custom plantation shutters, blinds, shades &amp; motorized blind
  - H1s (1): Custom Window Treatments and Reupholstery in West St Pete
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article)

- **`/areas/tierra-verde/`** (3170w, 3img, clicks=0, imp=0)
  - Title (96c): Tierra Verde Blinds Shop \| Custom Window Treatments &amp; Solar Shades \| Custom Fabric Creations
  - Desc (205c): Tierra Verde FL&#039;s premier blinds shop offering exterior solar shades, custom bedding, plantation shutters &amp; fur
  - H1s (1): Blinds Shop & Custom Window Treatment in Tierra Verde FL
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article)

- **`/areas/st-pete-beach/`** (3311w, 3img, clicks=0, imp=0)
  - Title (102c): St. Pete Beach Blinds Shop \| Custom Window Treatments &amp; Motorized Shades \| Custom Fabric Creations
  - Desc (195c): St. Pete Beach FL&#039;s premier blinds shop offering blackout roman shades, motorized exterior shades &amp; luxury drap
  - H1s (1): Blinds Shop & Custom Window Treatment in St. Pete Beach
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article)

- **`/areas/treasure-island/`** (3210w, 3img, clicks=0, imp=0)
  - Title (106c): Treasure Island Blinds Shop \| Custom Window Treatments &amp; Plantation Shutters \| Custom Fabric Creations
  - Desc (212c): Treasure Island FL&#039;s premier blinds shop offering composite plantation shutters, blackout roman shades &amp; commer
  - H1s (1): Blinds Shop & Custom Window Treament in Treasure Island FL
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article)

- **`/areas/clearwater/`** (3197w, 3img, clicks=0, imp=0)
  - Title (103c): Clearwater Blinds Shop \| Custom Window Treatments &amp; Exterior Patio Shades \| Custom Fabric Creations
  - Desc (181c): Clearwater FL&#039;s premier blinds shop offering exterior patio shades, custom plantation shutters &amp; designer drape
  - H1s (1): Blind Shop & Custom Window Treatment in Clearwater FL
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article)

- **`/areas/sand-key/`** (2994w, 3img, clicks=0, imp=0)
  - Title (103c): Sand Key Blinds Shop \| Custom Window Treatments &amp; Motorized Roller Shades \| Custom Fabric Creations
  - Desc (212c): Sand Key FL&#039;s premier blinds shop offering motorized roller shades, custom bedding, plantation shutters &amp; black
  - H1s (1): Blind Shop & Custom Window Treatment in Sand Key FL
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article)

- **`/areas/belleair-shore/`** (3019w, 3img, clicks=0, imp=0)
  - Title (52c): Belleair Shore Blinds Shop \| Custom Fabric Creations
  - Desc (198c): Belleair Shore FL&#039;s premier blinds shop offering custom plantation shutters, exterior solar shades &amp; luxury bed
  - H1s (1): Blind Shop & Custom Window Treatment in BelleAir Shore FL
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Desc>160c, BadSchema(Article)

- **`/areas/seminole/`** (2864w, 3img, clicks=0, imp=0)
  - Title (94c): eminole FL Blinds Shop \| Custom Window Treatments &amp; Roman Shades \| Custom Fabric Creations
  - Desc (201c): Seminole FL&#039;s premier blinds shop offering custom roman shades, motorized blinds, blackout shades &amp; plantation 
  - H1s (1): Blind Shop & Custom Window Treatment in Seminole FL
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article)

- **`/areas/largo/`** (2966w, 3img, clicks=0, imp=0)
  - Title (99c): Largo FL Blinds Shop \| Custom Window Treatments &amp; Plantation Shutters \| Custom Fabric Creations
  - Desc (194c): Largo FL&#039;s premier blinds shop offering custom plantation shutters, motorized window shades &amp; custom drapery. F
  - H1s (1): Blind Shop & Custom Window Treatment in Largo FL
  - Schema: Article, BreadcrumbList, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c, BadSchema(Article)

- **`/plantation-shutters-cost-st-petersburg/`** (1258w, 1img, clicks=0, imp=0)
  - Title (91c): Plantation Shutters Cost in St. Petersburg, FL: Real 2026 Pricing - Custom Fabric Creations
  - Desc (153c): Ask three shutter companies for a quote in St. Pete and you will get three different answers. The reason is simple: the 
  - H1s (1): Plantation Shutters Cost in St. Petersburg, FL: Real 2026 Pricing
  - Schema: Article, BreadcrumbList, FAQPage, LocalBusiness, Person, Place, Service, WebPage, WebSite
  - **Flags:** Title>65c

- **`/plantation-shutters-installation-st-petersburg/`** (1035w, 1img, clicks=0, imp=0)
  - Title (102c): Plantation Shutter Installation in St. Petersburg, FL: What Actually Happens - Custom Fabric Creations
  - Desc (161c): The internet is full of vague &quot;we install shutters&quot; pages that tell you nothing. Here is the actual, step-by-s
  - H1s (1): Plantation Shutter Installation in St. Petersburg, FL: What Actually Happens
  - Schema: Article, BreadcrumbList, FAQPage, HowTo, LocalBusiness, Person, Place, Service, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c

- **`/plantation-shutters-regret-downsides/`** (859w, 1img, clicks=0, imp=0)
  - Title (94c): Why Some Homeowners Regret Plantation Shutters (And How to Avoid It) - Custom Fabric Creations
  - Desc (182c): If you have been searching, you have probably seen the Reddit threads: &quot;Plantation shutters ruined my view,&quot; &
  - H1s (1): Why Some Homeowners Regret Plantation Shutters (And How to Avoid It)
  - Schema: Article, BreadcrumbList, FAQPage, LocalBusiness, Person, Place, WebPage, WebSite
  - **Flags:** Title>65c, Desc>160c

