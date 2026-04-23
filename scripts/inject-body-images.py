"""Inject inline body images into service + area content collection markdown.
Uses the top/middle/bottom content images from user's media folder."""

import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
SERVICES_DIR = ROOT / "src" / "content" / "services"
AREAS_DIR = ROOT / "src" / "content" / "areas"
PUBLIC = ROOT / "public" / "images"

def image_candidates(slug, kind):
    """Return list of image paths to distribute across the body, in order."""
    candidates = []
    if kind == "service":
        folder = PUBLIC / "services" / slug
        for name in ["top.webp", "top-middle.webp", "middle.webp", "bottom-middle.webp", "bottom.webp"]:
            p = folder / name
            if p.exists():
                candidates.append(f"/images/services/{slug}/{name}")
    elif kind == "area":
        # One area image, use as a single mid-article feature
        area_img = PUBLIC / "areas" / f"{slug}.webp"
        if area_img.exists():
            candidates.append(f"/images/areas/{slug}.webp")
    return candidates

def inject_images(md, images):
    if not images:
        return md

    # Split frontmatter vs body
    fm_match = re.match(r"^(---\n.*?\n---\n)", md, re.S)
    if not fm_match:
        return md
    fm, body = md[:fm_match.end()], md[fm_match.end():]

    # Find H2 positions
    h2_positions = [m.start() for m in re.finditer(r"^## ", body, re.M)]
    if len(h2_positions) < 2:
        return md

    # Strategy: place image right BEFORE H2 2, 4, 6 (after 1st, 3rd, 5th section) — skip first H2
    # Limit to number of available images
    # Remove any existing image markdown that's already in the body (to avoid duplicates on re-run)
    body = re.sub(r"\n!\[[^\]]*\]\(/images/[^)]+\)\n", "\n", body)

    # Recompute H2 positions after stripping existing images
    h2_positions = [m.start() for m in re.finditer(r"^## ", body, re.M)]

    # Pick insert points: before H2 index 1, 3, 5, ...
    slots = []
    for i, pos in enumerate(h2_positions):
        if i == 0:
            continue  # skip first H2 (it goes right after the hero)
        if (i % 2) == 1:  # insert before every other H2 starting at H2 #2 (index 1)
            slots.append(pos)
        if len(slots) >= len(images):
            break

    # Insert in reverse order so positions don't shift
    for img, pos in zip(reversed(images[: len(slots)]), reversed(slots)):
        alt = img.split("/")[-1].replace(".webp", "").replace("-", " ").title()
        insert = f"\n![{alt}]({img})\n\n"
        body = body[:pos] + insert + body[pos:]

    return fm + body

def process(directory, kind):
    count = 0
    for md_file in sorted(directory.glob("*.md")):
        slug = md_file.stem
        imgs = image_candidates(slug, kind)
        if not imgs:
            continue
        md = md_file.read_text(encoding="utf-8")
        new_md = inject_images(md, imgs)
        if new_md != md:
            md_file.write_text(new_md, encoding="utf-8")
            count += 1
            print(f"  [{kind}] {slug}: injected {len([i for i in imgs if i in new_md])} images")
    return count

total = process(SERVICES_DIR, "service")
total += process(AREAS_DIR, "area")
print(f"Injected images into {total} files.")
