"""Extract clean body content from scraped Bricks HTML pages.
For each page, emits a markdown file with:
  - frontmatter (title, desc, h1, og_image, images, faqs)
  - body markdown (headings, paragraphs, lists) with Ocala/Central FL rewritten
"""

import json
import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

HERE = Path(__file__).parent
HTML_DIR = HERE / "scraped" / "html"
OUT_DIR = HERE / "scraped" / "content"
OUT_DIR.mkdir(exist_ok=True)

BASE = "https://www.customfabriccreations.net"

# Text rewrites applied during extraction
REWRITES = [
    (re.compile(r"\bOcala,?\s*FL\b", re.I), "St. Petersburg, FL"),
    (re.compile(r"\bOcala\b", re.I), "St. Petersburg"),
    (re.compile(r"\bMarion\s+County\b", re.I), "Pinellas County"),
    (re.compile(r"\bCentral\s+Florida\b", re.I), "St. Petersburg"),
    (re.compile(r"\bcfcocala\.com\b", re.I), "customfabriccreations.net"),
    (re.compile(r"since\s+1999", re.I), "since 2000"),
]

def rewrite(text):
    for pat, repl in REWRITES:
        text = pat.sub(repl, text)
    return text

def clean_text(text):
    text = re.sub(r"\s+", " ", text).strip()
    # Fix common unicode smart-quote mojibake from scrape
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u2013", "-").replace("\u2014", "\u2014")
    return rewrite(text)

def extract_main(soup):
    """Return the main content element of the Bricks page, excluding header/footer."""
    # Prefer <main>
    main = soup.find("main") or soup.find(id="brx-content") or soup.find(id="main")
    if main:
        return main
    # Strip header/footer/nav and use body
    for t in soup(["header", "footer", "nav", "script", "style", "noscript", "iframe"]):
        t.decompose()
    return soup.body or soup

def node_to_markdown(node, depth=0):
    """Walk a subtree and emit markdown-ish paragraphs + headings + lists."""
    out = []
    if isinstance(node, NavigableString):
        s = clean_text(str(node))
        if s:
            out.append(s)
        return out
    if not isinstance(node, Tag):
        return out
    tag = node.name
    # Skip wrappers that we've already flattened through
    if tag in ("script", "style", "noscript", "iframe", "svg", "form", "button"):
        return out
    # Headings
    if tag in ("h1", "h2", "h3", "h4"):
        text = clean_text(node.get_text(" ", strip=True))
        if text:
            level = int(tag[1])
            out.append(f"\n\n{'#' * level} {text}\n")
        return out
    # Paragraphs
    if tag == "p":
        text = clean_text(node.get_text(" ", strip=True))
        if text and len(text) > 1:
            out.append(f"\n\n{text}\n")
        return out
    # Lists
    if tag in ("ul", "ol"):
        items = []
        for li in node.find_all("li", recursive=False):
            text = clean_text(li.get_text(" ", strip=True))
            if text:
                items.append(f"- {text}")
        if items:
            out.append("\n\n" + "\n".join(items) + "\n")
        return out
    # Images — emit as markdown so we can re-path later
    if tag == "img":
        src = node.get("src", "")
        alt = clean_text(node.get("alt", ""))
        if src and "wp-content/uploads" in src:
            fname = src.rstrip("/").split("/")[-1].split("?")[0]
            out.append(f"\n\n![{alt}](/images/{fname})\n")
        return out
    # Anchor - inline, preserve text only at this depth
    if tag == "a":
        text = clean_text(node.get_text(" ", strip=True))
        href = node.get("href", "")
        if text and href.startswith(BASE):
            rel = href.replace(BASE, "")
            return [f"[{text}]({rel})"]
        if text:
            return [text]
    # Otherwise recurse children
    for child in node.children:
        out.extend(node_to_markdown(child, depth + 1))
    return out

def extract_faqs(soup):
    """Pull FAQPage schema from JSON-LD and return list of {q,a} dicts."""
    faqs = []
    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        try:
            data = json.loads(script.string or "")
        except Exception:
            continue
        graph = data.get("@graph", [data]) if isinstance(data, dict) else []
        for node in graph:
            if not isinstance(node, dict):
                continue
            t = node.get("@type")
            if t == "FAQPage" or (isinstance(t, list) and "FAQPage" in t):
                for q in node.get("mainEntity", []):
                    question = q.get("name", "").strip()
                    ans = q.get("acceptedAnswer", {}).get("text", "").strip()
                    if question and ans:
                        faqs.append({
                            "q": clean_text(question),
                            "a": clean_text(re.sub(r"<[^>]+>", "", ans)),
                        })
    return faqs

def path_to_slug(p):
    if p == "/":
        return "home"
    return p.strip("/").replace("/", "--")

def extract_file(html_path):
    html = html_path.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(html, "lxml")

    # Meta
    title_el = soup.find("title")
    title = clean_text(title_el.get_text()) if title_el else ""
    desc_el = soup.find("meta", attrs={"name": "description"})
    desc = clean_text(desc_el.get("content", "")) if desc_el else ""
    canonical_el = soup.find("link", rel="canonical")
    canonical = canonical_el.get("href", "") if canonical_el else ""
    og_el = soup.find("meta", property="og:image")
    og_image = og_el.get("content", "") if og_el else ""

    # Main content tree
    main = extract_main(soup)
    # Remove known non-content containers inside main (Bricks review strips, etc)
    for sel in [
        "#brx-footer",
        ".fr-subfooter-alpha",
        ".fr-footer-alpha",
        ".fr-header-foxtrot",
        ".cfc-sw-avatar",
    ]:
        for n in main.select(sel):
            n.decompose()

    md_parts = []
    for child in main.children:
        md_parts.extend(node_to_markdown(child))
    body_md = "".join(md_parts)
    body_md = re.sub(r"\n{3,}", "\n\n", body_md).strip()

    # Extract H1 / H2s
    h1s = [clean_text(h.get_text(" ", strip=True)) for h in main.find_all("h1")]
    h2s = [clean_text(h.get_text(" ", strip=True)) for h in main.find_all("h2")]

    # Images referenced
    imgs = []
    for img in main.find_all("img"):
        src = img.get("src", "")
        if "wp-content/uploads" in src:
            fname = src.rstrip("/").split("/")[-1].split("?")[0]
            alt = clean_text(img.get("alt", ""))
            imgs.append({"src": f"/images/{fname}", "alt": alt})

    faqs = extract_faqs(soup)

    return {
        "title": title,
        "description": desc,
        "canonical": canonical,
        "og_image": og_image,
        "h1": h1s[0] if h1s else "",
        "h2s": h2s,
        "images": imgs,
        "faqs": faqs,
        "body_md": body_md,
    }

def main():
    index = {}
    for html_file in sorted(HTML_DIR.glob("*.html")):
        slug = html_file.stem
        try:
            data = extract_file(html_file)
        except Exception as e:
            print(f"ERR {slug}: {e}", file=sys.stderr)
            continue
        # write md file
        md = OUT_DIR / f"{slug}.md"
        fm_lines = [
            "---",
            f'title: "{data["title"].replace(chr(34), chr(39))}"',
            f'description: "{data["description"].replace(chr(34), chr(39))}"',
            f'h1: "{data["h1"].replace(chr(34), chr(39))}"',
            f'canonical: "{data["canonical"]}"',
            f'og_image: "{data["og_image"]}"',
            f'images: {json.dumps(data["images"])}',
            f'faqs: {json.dumps(data["faqs"])}',
            "---",
            "",
            data["body_md"],
        ]
        md.write_text("\n".join(fm_lines), encoding="utf-8")
        index[slug] = {
            "title": data["title"],
            "description": data["description"],
            "h1": data["h1"],
            "image_count": len(data["images"]),
            "faq_count": len(data["faqs"]),
            "body_length": len(data["body_md"]),
        }
    (OUT_DIR / "_index.json").write_text(json.dumps(index, indent=2))
    print(f"Extracted {len(index)} pages -> {OUT_DIR}")

if __name__ == "__main__":
    main()
