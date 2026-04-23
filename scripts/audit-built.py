"""Audit the built Astro site (dist/) against the same flags that produced
_seo/PAGE-AUDIT.md from the live WP site. Verifies the migration resolved
each issue."""

import json
import re
import sys
from pathlib import Path
from html.parser import HTMLParser

HERE = Path(__file__).parent
DIST = HERE.parent / "dist"
OUT = HERE / "scraped" / "audit-built.json"
OUT.parent.mkdir(exist_ok=True)

PATHS = [
    "/", "/about/", "/brands/", "/contact/", "/gallery/",
    "/services/",
    "/services/custom-draperies-curtains/",
    "/services/plantation-shutters/",
    "/services/window-shades/",
    "/services/custom-blinds/",
    "/services/custom-cornices-valances/",
    "/services/drapery-hardware/",
    "/services/outdoor-window-shades/",
    "/services/furniture-reupholstery/",
    "/services/custom-bedding-pillows/",
    "/services/custom-banquettes/",
    "/services/commercial-window-treatments/",
    "/services/services-interior-decor-tampa/",
    "/areas/",
    "/areas/st-petersburg/",
    "/areas/downtown-st-pete/",
    "/areas/old-northeast/",
    "/areas/snell-isle/",
    "/areas/shore-acres/",
    "/areas/west-st-pete/",
    "/areas/tierra-verde/",
    "/areas/st-pete-beach/",
    "/areas/treasure-island/",
    "/areas/clearwater/",
    "/areas/sand-key/",
    "/areas/belleair-shore/",
    "/areas/seminole/",
    "/areas/largo/",
    "/plantation-shutters-cost-st-petersburg/",
    "/plantation-shutters-installation-st-petersburg/",
    "/plantation-shutters-regret-downsides/",
]

class Extractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.headings = {"h1": [], "h2": [], "h3": []}
        self._current_tag = None
        self._current_text = []
        self.body_parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript", "iframe", "header", "footer", "nav"):
            self.skip += 1
        if tag in ("h1", "h2", "h3"):
            self._current_tag = tag
            self._current_text = []

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "iframe", "header", "footer", "nav"):
            self.skip = max(0, self.skip - 1)
        if tag in ("h1", "h2", "h3") and self._current_tag == tag:
            text = " ".join(self._current_text).strip()
            if text:
                self.headings[tag].append(text)
            self._current_tag = None

    def handle_data(self, data):
        if self.skip:
            return
        s = data.strip()
        if s:
            self.body_parts.append(s)
            if self._current_tag:
                self._current_text.append(s)

def audit(path):
    if path == "/":
        html_file = DIST / "index.html"
    else:
        html_file = DIST / path.strip("/") / "index.html"
    if not html_file.exists():
        return {"path": path, "error": "file not found"}
    html = html_file.read_text(encoding="utf-8", errors="replace")

    title = re.search(r"<title>([^<]+)</title>", html)
    title = title.group(1).strip() if title else ""

    desc = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', html, re.I)
    desc = desc.group(1).strip() if desc else ""

    canonical = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', html, re.I)
    canonical = canonical.group(1).strip() if canonical else ""

    robots = re.search(r'<meta\s+name="robots"\s+content="([^"]+)"', html, re.I)
    robots = robots.group(1).strip() if robots else ""

    # Schema
    schema_types = []
    has_bad_article_on_nonarticle = False
    has_alabama_geo = False
    for m in re.finditer(r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>', html, re.S):
        try:
            data = json.loads(m.group(1).strip())
        except Exception:
            continue
        graph = data.get("@graph", [data]) if isinstance(data, dict) else [data]
        for node in graph:
            if not isinstance(node, dict):
                continue
            t = node.get("@type")
            if isinstance(t, list):
                schema_types.extend(t)
            elif isinstance(t, str):
                schema_types.append(t)
            # check geo
            geo = node.get("geo")
            if isinstance(geo, dict):
                lat = str(geo.get("latitude", ""))
                if lat.startswith("31.72") or lat.startswith("31."):
                    has_alabama_geo = True

    is_article = path.startswith("/plantation-shutters-")
    if "Article" in schema_types and not is_article:
        has_bad_article_on_nonarticle = True

    # Body + headings
    p = Extractor()
    try:
        p.feed(html)
    except Exception:
        pass

    body = " ".join(p.body_parts)
    body = re.sub(r"\s+", " ", body)
    word_count = len(body.split())

    ocala = len(re.findall(r"\bocala\b", body, re.I)) + len(re.findall(r"\bmarion\s+county\b", body, re.I))
    central_fl = len(re.findall(r"\bcentral\s+florida\b", body, re.I))

    return {
        "path": path,
        "title": title,
        "title_length": len(title),
        "description": desc,
        "description_length": len(desc),
        "canonical": canonical,
        "robots": robots,
        "schema_types": sorted(set(schema_types)),
        "has_bad_article_schema": has_bad_article_on_nonarticle,
        "has_alabama_geo": has_alabama_geo,
        "h1": p.headings["h1"],
        "h1_count": len(p.headings["h1"]),
        "h2_count": len(p.headings["h2"]),
        "word_count": word_count,
        "ocala_residue": ocala,
        "central_fl_residue": central_fl,
    }

def main():
    audits = [audit(p) for p in PATHS]
    OUT.write_text(json.dumps({"pages": audits}, indent=2))

    print("=== BUILD AUDIT — migration verification ===")
    print(f"Audited {len(audits)} pages")

    missing = [a for a in audits if a.get("error")]
    if missing:
        print(f"\n!! {len(missing)} pages missing from build:")
        for a in missing:
            print(f"   {a['path']}")
        return

    flags = {
        "Alabama geo coords": [a for a in audits if a.get("has_alabama_geo")],
        "Article schema on non-article": [a for a in audits if a.get("has_bad_article_schema")],
        "Title > 65c": [a for a in audits if a["title_length"] > 65],
        "Title < 30c": [a for a in audits if a["title_length"] < 30],
        "Missing meta description": [a for a in audits if not a["description"]],
        "Desc > 160c": [a for a in audits if a["description_length"] > 160],
        "Missing H1": [a for a in audits if a["h1_count"] == 0],
        "Multiple H1": [a for a in audits if a["h1_count"] > 1],
        "Thin (<500 words)": [a for a in audits if a["word_count"] < 500],
        "Ocala residue": [a for a in audits if a["ocala_residue"] > 0],
        "Central FL residue": [a for a in audits if a["central_fl_residue"] > 0],
    }

    any_failed = False
    for flag, bad_pages in flags.items():
        if bad_pages:
            any_failed = True
            print(f"\n  [FAIL] {flag}: {len(bad_pages)} pages")
            for b in bad_pages[:10]:
                extra = f" ({b['title_length']}c: {b['title']})" if 'title' in flag.lower() else ""
                if 'description' in flag.lower():
                    extra = f" ({b['description_length']}c)"
                if 'word' in flag.lower():
                    extra = f" ({b['word_count']}w)"
                print(f"      {b['path']}{extra}")
            if len(bad_pages) > 10:
                print(f"      ... +{len(bad_pages) - 10} more")
        else:
            print(f"  [OK] {flag}")

    if not any_failed:
        print("\n\u2705 All migration flags clear.")
    else:
        print("\n\u26a0 Some flags still present. Review and fix before cutover.")
    print(f"\nFull results: {OUT}")

if __name__ == "__main__":
    main()
