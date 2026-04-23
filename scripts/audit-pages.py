"""Per-page audit — reads scraped HTML + GSC data, emits a structured
audit JSON used by the migration planner."""

import json
import re
from pathlib import Path
from html.parser import HTMLParser

HERE = Path(__file__).parent
HTML_DIR = HERE / "scraped" / "html"
GSC_FILE = HERE / "scraped" / "gsc.json"
OUT = HERE / "scraped" / "audit.json"

BASE = "https://www.customfabriccreations.net"

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

def path_to_slug(p):
    if p == "/":
        return "home"
    return p.strip("/").replace("/", "--")

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip_stack = 0
        self.parts = []
        self.headings = {"h1": [], "h2": [], "h3": []}
        self._current_tag = None
        self._current_text = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript", "iframe", "header", "footer", "nav"):
            self.skip_stack += 1
            return
        if tag in ("h1", "h2", "h3"):
            self._current_tag = tag
            self._current_text = []

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "iframe", "header", "footer", "nav"):
            self.skip_stack = max(0, self.skip_stack - 1)
            return
        if tag in ("h1", "h2", "h3") and self._current_tag == tag:
            text = " ".join(self._current_text).strip()
            if text:
                self.headings[tag].append(text)
            self._current_tag = None
            self._current_text = []

    def handle_data(self, data):
        if self.skip_stack:
            return
        stripped = data.strip()
        if stripped:
            self.parts.append(stripped)
            if self._current_tag:
                self._current_text.append(stripped)

def audit_page(path, html, gsc_by_page):
    slug = path_to_slug(path)

    title = None
    m = re.search(r"<title>([^<]+)</title>", html)
    if m:
        title = m.group(1).strip()

    desc = None
    m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', html, re.I)
    if m:
        desc = m.group(1).strip()

    og_img = None
    m = re.search(r'<meta\s+property="og:image"\s+content="([^"]+)"', html, re.I)
    if m:
        og_img = m.group(1).strip()

    canonical = None
    m = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', html, re.I)
    if m:
        canonical = m.group(1).strip()

    robots = None
    m = re.search(r'<meta\s+name="robots"\s+content="([^"]+)"', html, re.I)
    if m:
        robots = m.group(1).strip()

    # Schema extraction
    schema_types = []
    for sm in re.finditer(r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>', html, re.S):
        try:
            data = json.loads(sm.group(1).strip())
            if isinstance(data, dict) and "@graph" in data:
                for node in data["@graph"]:
                    t = node.get("@type")
                    if t:
                        schema_types.append(t if isinstance(t, str) else t[0])
            elif isinstance(data, dict) and "@type" in data:
                t = data["@type"]
                schema_types.append(t if isinstance(t, str) else t[0])
        except Exception:
            pass

    # Body text + headings
    parser = TextExtractor()
    try:
        parser.feed(html)
    except Exception:
        pass
    body_text = " ".join(parser.parts)
    body_text = re.sub(r"\s+", " ", body_text)
    word_count = len(body_text.split())

    # Ocala residue detection
    ocala_count = len(re.findall(r"\bocala\b", body_text, re.I))
    ocala_count += len(re.findall(r"\bmarion\s+county\b", body_text, re.I))

    # Image count (unique src)
    imgs = re.findall(r'<img[^>]+src="([^"]+)"', html)
    img_count = len(set(imgs))

    # Internal link count
    int_links = re.findall(r'href="https://www\.customfabriccreations\.net/[^"]*"', html)
    int_links += re.findall(r'href="/[^"]*"', html)

    gsc = gsc_by_page.get(BASE + path, {})

    return {
        "path": path,
        "slug": slug,
        "title": title,
        "title_length": len(title) if title else 0,
        "description": desc,
        "description_length": len(desc) if desc else 0,
        "canonical": canonical,
        "robots": robots,
        "og_image": og_img,
        "schema_types": sorted(set(schema_types)),
        "h1": parser.headings["h1"],
        "h1_count": len(parser.headings["h1"]),
        "h2": parser.headings["h2"],
        "h2_count": len(parser.headings["h2"]),
        "h3_count": len(parser.headings["h3"]),
        "word_count": word_count,
        "image_count": img_count,
        "internal_links": len(int_links),
        "ocala_residue": ocala_count,
        "gsc_clicks": gsc.get("clicks", 0),
        "gsc_impressions": gsc.get("impressions", 0),
        "gsc_position": gsc.get("position"),
        "top_queries": [q["query"] for q in gsc.get("top_queries", [])[:5]],
    }

def main():
    gsc = json.loads(GSC_FILE.read_text())
    gsc_by_page = {p["page"]: p for p in gsc["pages"]}

    audits = []
    for path in PATHS:
        slug = path_to_slug(path)
        html_file = HTML_DIR / f"{slug}.html"
        if not html_file.exists():
            print(f"MISSING: {html_file}")
            continue
        html = html_file.read_text(encoding="utf-8", errors="replace")
        a = audit_page(path, html, gsc_by_page)
        audits.append(a)

    OUT.write_text(json.dumps({"pages": audits}, indent=2))
    print(f"Audited {len(audits)} pages -> {OUT}")

    # Summary
    print("\n--- FLAGS ---")
    print(f"Thin content (<500 words): {sum(1 for a in audits if a['word_count'] < 500)}")
    print(f"Pages with Ocala residue:   {sum(1 for a in audits if a['ocala_residue'] > 0)}")
    print(f"Missing meta description:   {sum(1 for a in audits if not a['description'])}")
    print(f"Missing H1:                 {sum(1 for a in audits if a['h1_count'] == 0)}")
    print(f"Multiple H1s:               {sum(1 for a in audits if a['h1_count'] > 1)}")
    print(f"Pages with GSC impressions: {sum(1 for a in audits if a['gsc_impressions'] > 0)}")
    print(f"Pages with GSC clicks:      {sum(1 for a in audits if a['gsc_clicks'] > 0)}")

if __name__ == "__main__":
    main()
