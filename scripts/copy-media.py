"""Copy user-provided media into public/images/ with a sensible naming scheme."""

import shutil
import re
from pathlib import Path

SRC = Path(r"C:\Users\Willb\Claude\CFC\Astro Website Media\Website Media")
DEST = Path(__file__).parent.parent / "public" / "images"
DEST.mkdir(parents=True, exist_ok=True)

# Clear the old wp-content images first — we're replacing with the curated set
print("Clearing old wp-content scrape dump...")
for old in DEST.glob("*"):
    if old.is_file():
        old.unlink()
    elif old.is_dir():
        shutil.rmtree(old)

# Service folder -> target slug
SERVICE_MAP = {
    "Custom Window Treatments (Services)": "_homepage",
    "Plantation Shutters (Services)": "plantation-shutters",
    "Custom Drapery & Curtains (Services)": "custom-draperies-curtains",
    "Custom Blinds (Services)": "custom-blinds",
    "Window Shades (Services)": "window-shades",
    "Cornices & Valances (Services)": "custom-cornices-valances",
    "Drapery Hardware (Services)": "drapery-hardware",
    "Outdoor Window Shades (Services(": "outdoor-window-shades",  # user typo preserved as source folder
    "Furniture Reupholstery (Services)": "furniture-reupholstery",
    "Bedding & Pillows (Services)": "custom-bedding-pillows",
    "Interior Design & Products (Services)": "services-interior-decor-tampa",
}

# Area file -> target slug
AREA_MAP = {
    "St. Petersburg.webp": "st-petersburg.webp",
    "Downtown St. Pete.webp": "downtown-st-pete.webp",
    "Old Northeast.webp": "old-northeast.webp",
    "Snell Isle.webp": "snell-isle.webp",
    "Shore Acres.webp": "shore-acres.webp",
    "Tierra Verde.webp": "tierra-verde.webp",
    "St. Pete Beach.webp": "st-pete-beach.webp",
    "Treasure Island.webp": "treasure-island.webp",
    "Clearwater.webp": "clearwater.webp",
    "Sand key.webp": "sand-key.webp",
    "Belleair Shore.webp": "belleair-shore.webp",
    "Seminole.webp": "seminole.webp",
    "Largo.webp": "largo.webp",
    "custom-window-treatments-reupholstery-west-st-pete-fl.webp": "west-st-pete.webp",
}

def normalize_filename(name: str) -> str:
    """Convert 'Plantation Shutters Top Content Image.webp' -> 'top.webp' or 'hero.webp'."""
    lower = name.lower()
    if "background hero" in lower or lower.endswith(" hero image.webp"):
        return "hero.webp"
    if "top-middle content" in lower or "top middle content" in lower:
        return "top-middle.webp"
    if "bottom-middle content" in lower or "bottom middle content" in lower:
        return "bottom-middle.webp"
    if "top content" in lower:
        return "top.webp"
    if "middle content" in lower:
        return "middle.webp"
    if "bottom content" in lower:
        return "bottom.webp"
    # Fallback: sanitize
    base = Path(name).stem
    slug = re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")
    return f"{slug}.webp"

# --- Services ---
(DEST / "services").mkdir(exist_ok=True)
(DEST / "hero").mkdir(exist_ok=True)
homepage_hero_copied = False

for src_folder, slug in SERVICE_MAP.items():
    sdir = SRC / src_folder
    if not sdir.exists():
        print(f"!! missing source: {sdir}")
        continue

    if slug == "_homepage":
        # homepage hero + 2 content images
        for f in sdir.iterdir():
            if not f.is_file():
                continue
            lower = f.name.lower()
            if "background hero" in lower:
                target = DEST / "hero" / "homepage.webp"
            elif "top content" in lower:
                target = DEST / "homepage-top.webp"
            elif "bottom content" in lower:
                target = DEST / "homepage-bottom.webp"
            else:
                target = DEST / f.name
            shutil.copy2(f, target)
            print(f"  homepage: {f.name} -> {target.relative_to(DEST)}")
            homepage_hero_copied = True
        continue

    tdir = DEST / "services" / slug
    tdir.mkdir(exist_ok=True)
    for f in sdir.iterdir():
        if not f.is_file():
            continue
        new_name = normalize_filename(f.name)
        if new_name == "hero.webp":
            # hero goes into /images/hero/ for quick use
            target_hero = DEST / "hero" / f"{slug}.webp"
            shutil.copy2(f, target_hero)
        target = tdir / new_name
        shutil.copy2(f, target)
        print(f"  {slug}: {f.name} -> services/{slug}/{new_name}")

# --- Areas ---
(DEST / "areas").mkdir(exist_ok=True)
for src_name, target_name in AREA_MAP.items():
    src = SRC / src_name
    if not src.exists():
        print(f"!! missing area image: {src_name}")
        continue
    target = DEST / "areas" / target_name
    shutil.copy2(src, target)
    print(f"  area: {src_name} -> areas/{target_name}")

# St Pete Map
map_src = SRC / "St. Petersburg Map Image.webp"
if map_src.exists():
    shutil.copy2(map_src, DEST / "st-pete-map.webp")
    print("  map: St. Petersburg Map Image.webp -> st-pete-map.webp")

# --- Gallery ---
gallery_src = SRC / "Gallery Photos"
gallery_dest = DEST / "gallery"
gallery_dest.mkdir(exist_ok=True)
if gallery_src.exists():
    for f in gallery_src.iterdir():
        if not f.is_file():
            continue
        base = Path(f.name).stem.replace(" ", "-").lower()
        base = re.sub(r"[^a-z0-9\-]+", "-", base).strip("-")
        target = gallery_dest / f"{base}.webp"
        shutil.copy2(f, target)
        print(f"  gallery: {f.name} -> gallery/{base}.webp")

# Count
files = list(DEST.rglob("*"))
print(f"\nDone. Copied {sum(1 for f in files if f.is_file())} files to {DEST}")
