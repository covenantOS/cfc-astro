"""Take the scraped markdown from scripts/scraped/content/ and emit clean
content collection files at src/content/services/{slug}.md and
src/content/areas/{slug}.md — with all template chrome (nav, testimonials,
feature badges, bottom CTA) stripped and just the real article body kept."""

import re
import json
from pathlib import Path

HERE = Path(__file__).parent
SRC_DIR = HERE / "scraped" / "content"
SERVICES_DIR = HERE.parent / "src" / "content" / "services"
AREAS_DIR = HERE.parent / "src" / "content" / "areas"
SERVICES_DIR.mkdir(parents=True, exist_ok=True)
AREAS_DIR.mkdir(parents=True, exist_ok=True)

# Map scraped filenames -> collection target
# Service slug -> scraped file
SERVICES = {
    "plantation-shutters": "services--plantation-shutters.md",
    "custom-draperies-curtains": "services--custom-draperies-curtains.md",
    "window-shades": "services--window-shades.md",
    "custom-blinds": "services--custom-blinds.md",
    "custom-cornices-valances": "services--custom-cornices-valances.md",
    "drapery-hardware": "services--drapery-hardware.md",
    "outdoor-window-shades": "services--outdoor-window-shades.md",
    "furniture-reupholstery": "services--furniture-reupholstery.md",
    "custom-bedding-pillows": "services--custom-bedding-pillows.md",
    "custom-banquettes": "services--custom-banquettes.md",
    "commercial-window-treatments": "services--commercial-window-treatments.md",
    "services-interior-decor-tampa": "services--services-interior-decor-tampa.md",
}
AREAS = {
    "st-petersburg": "areas--st-petersburg.md",
    "downtown-st-pete": "areas--downtown-st-pete.md",
    "old-northeast": "areas--old-northeast.md",
    "snell-isle": "areas--snell-isle.md",
    "shore-acres": "areas--shore-acres.md",
    "west-st-pete": "areas--west-st-pete.md",
    "tierra-verde": "areas--tierra-verde.md",
    "st-pete-beach": "areas--st-pete-beach.md",
    "treasure-island": "areas--treasure-island.md",
    "clearwater": "areas--clearwater.md",
    "sand-key": "areas--sand-key.md",
    "belleair-shore": "areas--belleair-shore.md",
    "seminole": "areas--seminole.md",
    "largo": "areas--largo.md",
}

# Phone number rewrite — the scraped WP site has a mix of (727) 240-4512 and (352) 266-1262.
# We standardize on the main St. Pete number for the new site.
def rewrite_phones(text):
    text = re.sub(r"\(352\)\s*266-1262", "(727) 240-4512", text)
    return text

def rewrite_geo(text):
    # Already done in scrape step, but belt & suspenders
    text = re.sub(r"\bOcala,?\s*FL\b", "St. Petersburg, FL", text, flags=re.I)
    text = re.sub(r"\bOcala\b", "St. Petersburg", text, flags=re.I)
    text = re.sub(r"\bMarion\s+County\b", "Pinellas County", text, flags=re.I)
    text = re.sub(r"\bCentral\s+Florida\b", "St. Petersburg", text, flags=re.I)
    return text

# Lines/blocks to strip from the scraped content (template chrome)
STRIP_PATTERNS = [
    # "Get Your Free Estimate" sidebar (and the (727) + Request an Estimate after)
    re.compile(r"###\s+Get Your Free Estimate\b.*?(?=\n##\s)", re.S),
    # Testimonial blocks — often rendered as quote lines followed by names
    # The pattern "NAME\u00a0•\u00a0LOCATION" or after quote followed by "NAME."
    # We'll strip the review carousel noise section by looking for known names
    # bottom "Start Your Custom Design Project" CTA
    re.compile(r"##\s+Start Your Custom Design Project.*$", re.S),
    # Service list (sidebar)
    # Matches leading `- Custom Blinds` through the whole service + area list block
]

KNOWN_REVIEWERS = [
    "Jennifer R.", "David M.", "Sarah K.", "Patty Protic", "Beth McCarthy", "Amy Monroe",
]

FEATURE_BADGE_LINES = [
    "5-Star Rated Dozens of 5-star Google reviews",
    "Master Craftsmanship Flawless custom tailoring",
    "Designer Collections Exclusive premium fabric selections",
    "Cohesive Styling Perfectly matched interiors",
]

def strip_template_chrome(body):
    # Apply regex-based section strips
    for pat in STRIP_PATTERNS:
        body = pat.sub("", body)

    lines = body.split("\n")
    out = []
    in_list = False
    skip_list = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip lines that are known feature badges
        if any(badge in stripped for badge in FEATURE_BADGE_LINES):
            i += 1
            continue

        # Skip Google rating line like "4.9100+ Google Reviews"
        if re.match(r"^4\.9\d*\+?\s*Google Reviews?$", stripped):
            i += 1
            continue

        # Skip reviewer attributions
        if any(r in stripped for r in KNOWN_REVIEWERS):
            i += 1
            # Also skip adjacent quote line — usually the previous non-empty line
            continue

        # Skip quote lines that pair with reviewer names (heuristic: quoted praise)
        if stripped.startswith('"') and stripped.endswith('"') and len(stripped) < 300:
            # Check next non-empty lines for a reviewer name
            next_non_empty = None
            for j in range(i + 1, min(i + 5, len(lines))):
                if lines[j].strip():
                    next_non_empty = lines[j].strip()
                    break
            if next_non_empty and any(r in next_non_empty for r in KNOWN_REVIEWERS):
                i += 1
                continue

        # Skip the sidebar service/area list (they're at the top of content)
        # Heuristic: a run of `- Service/Area Name` items early in the file
        if stripped.startswith("- ") and i < 80:
            # Check if the next several lines are also `- ` items (list)
            list_items = [stripped[2:]]
            j = i + 1
            while j < len(lines):
                if lines[j].strip().startswith("- "):
                    list_items.append(lines[j].strip()[2:])
                    j += 1
                elif not lines[j].strip():
                    j += 1
                else:
                    break
            # If it's a known service list OR known area list, skip
            services_hint = {"Custom Blinds", "Window Shades", "Plantation Shutters", "Draperies & Curtains"}
            areas_hint = {"St. Petersburg", "Snell Isle", "Old Northeast", "Downtown St. Pete"}
            items_set = set(s.strip() for s in list_items)
            if len(items_set & services_hint) >= 3 or len(items_set & areas_hint) >= 3:
                # skip this entire list
                i = j
                continue

        out.append(line)
        i += 1

    body = "\n".join(out)

    # Collapse multiple blank lines
    body = re.sub(r"\n{3,}", "\n\n", body)

    # Strip ALL H1s — the hero component emits the page H1
    body = re.sub(r"^#\s+[^\n]+\n", "", body, flags=re.M)

    # Strip the intro blob that contains breadcrumb junk like `[Home]()/[Areas]...`
    body = re.sub(r"\[Home\]\([^)]*\)/\[[^\]]+\]\([^)]*\)[^\n]+", "", body)

    # Remove phone/Request-an-Estimate artifacts on their own or at end of paragraphs
    body = re.sub(r"\(727\)\s*240-4512\[Request an Estimate\]\(/contact/\)", "", body)
    body = re.sub(r"\[Request an Estimate\]\(/contact/\)", "", body)

    body = rewrite_phones(body)
    body = rewrite_geo(body)
    return body.strip()

def parse_front_matter(md):
    m = re.match(r"---\n(.*?)\n---\n", md, re.S)
    if not m:
        return {}, md
    fm_raw = m.group(1)
    rest = md[m.end():]
    fm = {}
    for line in fm_raw.split("\n"):
        mm = re.match(r'^(\w+):\s*"?(.*?)"?\s*$', line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip('"')
        else:
            mm = re.match(r"^(\w+):\s*(.*)$", line)
            if mm:
                fm[mm.group(1)] = mm.group(2).strip()
    return fm, rest

def trim_title(title, kind, slug):
    # Strip " - Custom Fabric Creations" and " | Custom Fabric Creations"
    title = re.sub(r"\s*[-|]\s*Custom Fabric Creations\s*$", "", title)
    # If still too long, strip known templated suffixes
    title = re.sub(r"\s*\|\s*(Custom Window Treatments &.*|Custom Window Treatments.*|Made-to-Measure.*)$", "", title)
    title = title.strip()

    # If STILL too long for SEO (ideal ≤ ~45c to leave room for brand suffix),
    # use a compact area/service title.
    AREA_SHORT = {
        "st-petersburg": "Window Treatments in St. Petersburg, FL",
        "downtown-st-pete": "Window Treatments in Downtown St. Pete",
        "old-northeast": "Window Treatments in Old Northeast, St. Pete",
        "snell-isle": "Window Treatments in Snell Isle, FL",
        "shore-acres": "Window Treatments in Shore Acres, FL",
        "west-st-pete": "Window Treatments in West St. Pete, FL",
        "tierra-verde": "Window Treatments in Tierra Verde, FL",
        "st-pete-beach": "Window Treatments in St. Pete Beach, FL",
        "treasure-island": "Window Treatments in Treasure Island, FL",
        "clearwater": "Window Treatments in Clearwater, FL",
        "sand-key": "Window Treatments in Sand Key, FL",
        "belleair-shore": "Window Treatments in Belleair Shore, FL",
        "seminole": "Window Treatments in Seminole, FL",
        "largo": "Window Treatments in Largo, FL",
    }
    SERVICE_SHORT = {
        "plantation-shutters": "Plantation Shutters in St. Petersburg, FL",
        "custom-draperies-curtains": "Custom Drapery & Curtains in St. Petersburg",
        "window-shades": "Custom Window Shades in St. Petersburg, FL",
        "custom-blinds": "Custom Blinds in St. Petersburg, FL",
        "custom-cornices-valances": "Cornices & Valances in St. Petersburg, FL",
        "drapery-hardware": "Drapery Hardware in St. Petersburg, FL",
        "outdoor-window-shades": "Outdoor Window Shades in St. Petersburg",
        "furniture-reupholstery": "Furniture Reupholstery in St. Petersburg, FL",
        "custom-bedding-pillows": "Custom Bedding in St. Petersburg, FL",
        "custom-banquettes": "Custom Banquettes in St. Petersburg, FL",
        "commercial-window-treatments": "Commercial Window Treatments \u2014 St. Pete",
        "services-interior-decor-tampa": "Interior Design in St. Petersburg, FL",
    }
    if len(title) > 48:
        if kind == "area" and slug in AREA_SHORT:
            return AREA_SHORT[slug]
        if kind == "service" and slug in SERVICE_SHORT:
            return SERVICE_SHORT[slug]
    return title

def trim_desc(desc, slug):
    desc = re.sub(r"Call \(352\)\s*266-1262!?", "", desc)
    desc = re.sub(r"Call \(727\)\s*240-4512!?", "", desc)
    desc = re.sub(r"Free in-home consultation\.?", "Free consultation.", desc)
    desc = desc.replace("  ", " ").strip().strip(".,").rstrip(".") + "."
    # Truncate at word boundary if over 155c
    if len(desc) > 155:
        cut = desc[:155].rsplit(" ", 1)[0]
        desc = cut.rstrip(".,;") + "."
    return desc

def emit_file(slug, scraped_md, target_dir, collection_type):
    fm, body = parse_front_matter(scraped_md)
    clean_body = strip_template_chrome(body)

    # Extract FAQs if present in scraped frontmatter
    faqs = []
    faqs_raw = fm.get("faqs", "[]")
    if faqs_raw and faqs_raw != "[]":
        try:
            faqs = json.loads(faqs_raw)
        except Exception:
            faqs = []

    # Titles/descriptions from the scraped WP page
    title = trim_title(fm.get("title", slug), collection_type, slug)
    desc = trim_desc(rewrite_geo(rewrite_phones(fm.get("description", ""))), slug)
    h1 = rewrite_geo(rewrite_phones(fm.get("h1", "")))

    # Emit a yaml frontmatter + markdown file suitable for Astro Content Collections
    frontmatter = [
        "---",
        f"title: {json.dumps(title)}",
        f"description: {json.dumps(desc)}",
        f"h1: {json.dumps(h1)}",
        f"slug: {slug}",
        f'type: {collection_type}',
    ]
    if faqs:
        frontmatter.append(f"faqs: {json.dumps(faqs)}")
    frontmatter.append("---")
    frontmatter.append("")

    target = target_dir / f"{slug}.md"
    target.write_text("\n".join(frontmatter) + clean_body + "\n", encoding="utf-8")
    return len(clean_body.split())

# Process
def process(mapping, target_dir, collection_type):
    total = 0
    for slug, fname in mapping.items():
        scraped = SRC_DIR / fname
        if not scraped.exists():
            print(f"!! missing source: {fname}")
            continue
        md = scraped.read_text(encoding="utf-8")
        wc = emit_file(slug, md, target_dir, collection_type)
        total += wc
        print(f"  [{collection_type}] {slug}: {wc} words")
    print(f"Total {collection_type} words: {total}")

process(SERVICES, SERVICES_DIR, "service")
process(AREAS, AREAS_DIR, "area")
print("Done.")
