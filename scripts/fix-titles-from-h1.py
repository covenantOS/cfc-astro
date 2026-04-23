r"""Regenerate each content file's title from its H1 (which was clean on the
live site even when <title> was corrupted with missing-first-char bugs)."""

import re
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent

# Compact titles — per slug, optimal SEO title (≤60c after brand suffix appended)
SERVICE_TITLES = {
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
    "commercial-window-treatments": "Commercial Window Treatments | St. Pete",
    "services-interior-decor-tampa": "Interior Design in St. Petersburg, FL",
}
AREA_TITLES = {
    "st-petersburg": "Window Treatments in St. Petersburg, FL",
    "downtown-st-pete": "Window Treatments in Downtown St. Pete",
    "old-northeast": "Window Treatments in Historic Old Northeast",
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

# Also clean H1s — normalize to CFC standard
SERVICE_H1S = {
    "plantation-shutters": "Custom Plantation Shutters in St. Petersburg, FL",
    "custom-draperies-curtains": "Custom Draperies & Curtains in St. Petersburg, FL",
    "window-shades": "Custom Window Shades in St. Petersburg, FL",
    "custom-blinds": "Custom Blinds in St. Petersburg, FL",
    "custom-cornices-valances": "Custom Cornices & Valances in St. Petersburg",
    "drapery-hardware": "Drapery Hardware in St. Petersburg, FL",
    "outdoor-window-shades": "Outdoor Window Shades in St. Petersburg",
    "furniture-reupholstery": "Furniture Reupholstery in St. Petersburg, FL",
    "custom-bedding-pillows": "Custom Bedding & Pillows in St. Petersburg",
    "custom-banquettes": "Custom Banquettes in St. Petersburg",
    "commercial-window-treatments": "Commercial Window Treatments in St. Petersburg",
    "services-interior-decor-tampa": "Interior Design & Products in St. Petersburg",
}
AREA_H1S = {
    "st-petersburg": "Custom Window Treatments in St. Petersburg, FL",
    "downtown-st-pete": "Custom Window Treatments in Downtown St. Pete",
    "old-northeast": "Custom Window Treatments in Historic Old Northeast",
    "snell-isle": "Custom Window Treatments in Snell Isle, FL",
    "shore-acres": "Custom Window Treatments in Shore Acres, FL",
    "west-st-pete": "Custom Window Treatments in West St. Pete, FL",
    "tierra-verde": "Custom Window Treatments in Tierra Verde, FL",
    "st-pete-beach": "Custom Window Treatments in St. Pete Beach, FL",
    "treasure-island": "Custom Window Treatments in Treasure Island, FL",
    "clearwater": "Custom Window Treatments in Clearwater, FL",
    "sand-key": "Custom Window Treatments in Sand Key, FL",
    "belleair-shore": "Custom Window Treatments in Belleair Shore, FL",
    "seminole": "Custom Window Treatments in Seminole, FL",
    "largo": "Custom Window Treatments in Largo, FL",
}

def fix(dir_path, title_map, h1_map):
    for md_file in sorted(dir_path.glob("*.md")):
        slug = md_file.stem
        if slug not in title_map:
            print(f"  skip {slug}")
            continue
        text = md_file.read_text(encoding="utf-8")
        new_title = title_map[slug]
        new_h1 = h1_map[slug]
        # Update frontmatter title
        text = re.sub(r'^title:.*$', lambda m: f'title: {json.dumps(new_title)}', text, count=1, flags=re.M)
        text = re.sub(r'^h1:.*$', lambda m: f'h1: {json.dumps(new_h1)}', text, count=1, flags=re.M)
        # Strip any remaining Central Florida / Ocala in body
        text = re.sub(r"\bCentral Florida\b", "St. Petersburg", text)
        text = re.sub(r"\bOcala\b", "St. Petersburg", text)
        text = re.sub(r"\bMarion County\b", "Pinellas County", text)
        md_file.write_text(text, encoding="utf-8")
        print(f"  fixed {slug}")

print("Services:")
fix(ROOT / "src" / "content" / "services", SERVICE_TITLES, SERVICE_H1S)
print("\nAreas:")
fix(ROOT / "src" / "content" / "areas", AREA_TITLES, AREA_H1S)
