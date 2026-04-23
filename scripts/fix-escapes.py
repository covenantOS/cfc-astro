r"""Replace literal backslash-uXXXX escape sequences with actual characters
across all .astro and .ts files. These escapes were written as text and
not interpreted by the Astro compiler, so they render literally on page."""

from pathlib import Path

ROOT = Path(__file__).parent.parent

REPLACEMENTS = {
    r"\u00b7": "\u00b7",  # middle dot
    r"\u2014": "\u2014",  # em dash
    r"\u2013": "\u2013",  # en dash
    r"\u2019": "\u2019",  # right single quote
    r"\u2018": "\u2018",  # left single quote
    r"\u201c": "\u201c",  # left double quote
    r"\u201d": "\u201d",  # right double quote
    r"\u00a0": " ",        # non-breaking space -> space
    r"\u26a0": "\u26a0",  # warning triangle
    r"\u2022": "\u2022",  # bullet
    r"\u00e9": "\u00e9",  # e acute
    r"\u00ae": "\u00ae",  # registered
    r"\u2192": "\u2192",  # right arrow
    r"\u2212": "\u2212",  # minus
}

def fix_file(path):
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return 0
    original = text
    for esc, ch in REPLACEMENTS.items():
        text = text.replace(esc, ch)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return 1
    return 0

count = 0
for base in [ROOT / "src"]:
    if not base.is_dir():
        continue
    for ext in ("*.astro", "*.ts", "*.tsx", "*.js", "*.mjs", "*.css", "*.md"):
        for p in base.rglob(ext):
            count += fix_file(p)

# Also fix the standalone page files
for p in (ROOT / "src" / "pages").rglob("*.astro"):
    count += fix_file(p)

print(f"Fixed {count} files.")
