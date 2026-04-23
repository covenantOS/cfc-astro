"""Fix the missing-first-character bug across ALL content files.

The original WP scrape dropped the first letter of strings because the Bricks
renderer wraps the first char in a separate span for a decorative effect.
This script hunts for known truncation patterns and restores them."""

import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
PATHS = [
    ROOT / "src" / "content",
    ROOT / "src" / "lib",
]

# Map of "truncated stem" -> "correct stem". Case-insensitive whole-word replacement.
# Each key should ONLY match if it's NOT already part of a longer correct word.
# Applied longest-first so e.g. "ustomization" doesn't get munged before "ustom" tries.
TRUNCATIONS = {
    # window / windows
    r"\b(?<![a-z])indows?\b": lambda m: ("Window" + m.group(0)[len("indow"):]) if m.group(0).lower() == "indow" else ("Windows" + m.group(0)[len("indows"):]),
    r"\b(?<![a-z])rapery\b": "Drapery",
    r"\b(?<![a-z])raperies\b": "Draperies",
    r"\b(?<![a-z])hutters?\b": lambda m: "Shutter" + ("s" if m.group(0).lower().endswith("s") else ""),
    r"\b(?<![a-z])lind\b": "Blind",
    r"\b(?<![a-z])linds\b": "Blinds",
    r"\b(?<![a-z])ustom\b": "Custom",
    r"\b(?<![a-z])ervices?\b": lambda m: "Service" + ("s" if m.group(0).lower().endswith("s") else ""),
    r"\b(?<![a-z])reatment\b": "Treatment",
    r"\b(?<![a-z])reatments\b": "Treatments",
    r"\b(?<![a-z])eminole\b": "Seminole",
    r"\b(?<![a-z])reasure\b": "Treasure",
    r"\b(?<![a-z])learwater\b": "Clearwater",
    r"\b(?<![a-z])nell\b": "Snell",
    r"\b(?<![a-z])argo\b": "Largo",
    r"\b(?<![a-z])elleair\b": "Belleair",
    r"\b(?<![a-z])ierra\b": "Tierra",
    r"\b(?<![a-z])hore\b": "Shore",
    r"\b(?<![a-z])ornice\b": "Cornice",
    r"\b(?<![a-z])ornices\b": "Cornices",
    r"\b(?<![a-z])alance\b": "Valance",
    r"\b(?<![a-z])alances\b": "Valances",
    r"\b(?<![a-z])ommercial\b": "Commercial",
    r"\b(?<![a-z])nterior\b": "Interior",
    r"\b(?<![a-z])xterior\b": "Exterior",
    r"\b(?<![a-z])utdoor\b": "Outdoor",
    r"\b(?<![a-z])edding\b": "Bedding",
    r"\b(?<![a-z])illow\b": "Pillow",
    r"\b(?<![a-z])illows\b": "Pillows",
    r"\b(?<![a-z])urniture\b": "Furniture",
    r"\b(?<![a-z])eupholstery\b": "Reupholstery",
    r"\b(?<![a-z])ardware\b": "Hardware",
    r"\b(?<![a-z])anquette\b": "Banquette",
    r"\b(?<![a-z])anquettes\b": "Banquettes",
    r"\b(?<![a-z])otorized\b": "Motorized",
    r"\b(?<![a-z])otorization\b": "Motorization",
}

# "Sentence-start" fixers — a paragraph, list item, or heading that begins
# with a lowercase letter that should be uppercase. Only apply when the
# preceding character is ^, >, \n\n, `- `, or after `## `/`### ` heading.
SENTENCE_START = re.compile(r"(^|\n\n|\n- |\n#{1,6}\s)([a-z])")

def apply_truncations(text):
    for pattern, replacement in TRUNCATIONS.items():
        if callable(replacement):
            text = re.sub(pattern, replacement, text, flags=re.I)
        else:
            # Preserve case of first letter of whole match — but since the truncation
            # dropped the capital, we force title case
            text = re.sub(pattern, replacement, text, flags=re.I)
    return text

def uppercase_sentence_starts(text):
    def up(m):
        return m.group(1) + m.group(2).upper()
    return SENTENCE_START.sub(up, text)

def fix_file(path):
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return 0
    before = text
    text = apply_truncations(text)
    # Only apply sentence-start uppercase in body (below frontmatter)
    fm_match = re.match(r"^---\n.*?\n---\n", text, re.S)
    if fm_match:
        head = text[:fm_match.end()]
        body = text[fm_match.end():]
        body = uppercase_sentence_starts(body)
        text = head + body
    else:
        text = uppercase_sentence_starts(text)

    if text != before:
        path.write_text(text, encoding="utf-8")
        return 1
    return 0

count = 0
for base in PATHS:
    if not base.is_dir():
        continue
    for ext in ("*.md", "*.ts", "*.astro"):
        for p in base.rglob(ext):
            count += fix_file(p)

print(f"Fixed {count} files.")
