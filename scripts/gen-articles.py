"""Generate the 3 plantation-shutters article Astro pages from extracted markdown."""

import json
import re
from pathlib import Path

HERE = Path(__file__).parent
CONTENT_DIR = HERE / "scraped" / "content"
PAGES_DIR = HERE.parent / "src" / "pages"

ARTICLES = {
    "plantation-shutters-cost-st-petersburg": {
        "title": "Plantation Shutters Cost in St. Petersburg, FL: Real 2026 Pricing",
        "description": "What plantation shutters actually cost in St. Petersburg in 2026 \u2014 real price ranges by material, window size, and brand, from a local studio with 25 years of install history.",
        "date": "2026-04-01",
    },
    "plantation-shutters-installation-st-petersburg": {
        "title": "Plantation Shutter Installation in St. Petersburg, FL: What Actually Happens",
        "description": "A step-by-step look at what plantation shutter installation actually involves in a St. Petersburg home \u2014 from measurement to finish, by a local installer.",
        "date": "2026-04-10",
    },
    "plantation-shutters-regret-downsides": {
        "title": "Why Some Homeowners Regret Plantation Shutters (And How to Avoid It)",
        "description": "The real downsides of plantation shutters \u2014 and how to decide if they\u2019re right for your St. Petersburg home. A candid guide from a local installer.",
        "date": "2026-04-15",
    },
}

def md_to_html(text: str) -> str:
    """Very simple markdown -> HTML conversion for the article bodies we extracted."""
    lines = text.split("\n")
    out = []
    in_list = False
    in_para = False
    para_buf = []

    def flush_para():
        nonlocal para_buf
        if para_buf:
            para = " ".join(para_buf).strip()
            if para:
                out.append(f"  <p>{escape_inline(para)}</p>")
            para_buf = []

    def flush_list():
        nonlocal in_list
        if in_list:
            out.append("  </ul>")
            in_list = False

    def escape_inline(s: str) -> str:
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        return s

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            flush_para()
            flush_list()
            continue
        # Heading
        m = re.match(r"^(#{1,4})\s+(.+)$", line)
        if m:
            flush_para()
            flush_list()
            level = len(m.group(1))
            if level == 1:
                continue  # skip H1s (hero handles it)
            tag = f"h{level}"
            out.append(f"  <{tag}>{escape_inline(m.group(2).strip())}</{tag}>")
            continue
        # List item
        if line.lstrip().startswith("- "):
            flush_para()
            if not in_list:
                out.append("  <ul>")
                in_list = True
            item = line.lstrip()[2:]
            out.append(f"    <li>{escape_inline(item)}</li>")
            continue
        # Image
        m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)", line.strip())
        if m:
            flush_para()
            flush_list()
            continue  # skip inline images for these articles (articles use minimal imagery)
        # Regular paragraph line
        flush_list()
        para_buf.append(line.strip())

    flush_para()
    flush_list()
    return "\n".join(out)

def extract_body(md: str) -> str:
    """Strip frontmatter and nav noise (first ~30% tends to be chrome), return body markdown."""
    # Strip frontmatter
    md = re.sub(r"^---.*?---\n", "", md, count=1, flags=re.S)

    # Skip noise: everything before the first H2 that's substantive
    # Look for the first ## that isn't "Get Your Free Estimate"
    parts = md.split("## ", 1)
    if len(parts) == 2 and not parts[1].startswith("Get "):
        # Keep everything from first real H2 onwards, but include pre-H2 intro if it's long
        pre = parts[0]
        # Find the intro paragraph (first big paragraph in the pre-H2 section)
        intro_match = re.search(r"\n\n([A-Z][^\n]{100,})\n", pre)
        intro = intro_match.group(1).strip() if intro_match else ""
        body = (intro + "\n\n## " + parts[1]) if intro else ("## " + parts[1])
        return body
    return md

for slug, meta in ARTICLES.items():
    md_file = CONTENT_DIR / f"{slug}.md"
    if not md_file.exists():
        print(f"!! missing {md_file}")
        continue
    md = md_file.read_text(encoding="utf-8")

    # Load extracted faqs from frontmatter
    fm_match = re.search(r"^---\n(.*?)\n---", md, re.S)
    faqs = []
    if fm_match:
        for fm_line in fm_match.group(1).split("\n"):
            if fm_line.startswith("faqs:"):
                faq_json = fm_line[5:].strip()
                try:
                    faqs = json.loads(faq_json)
                except Exception:
                    faqs = []
                break

    body_md = extract_body(md)
    body_html = md_to_html(body_md)

    faqs_js = json.dumps(faqs, indent=0).replace("\n", " ")

    page = f'''---
import BaseLayout from '~/layouts/BaseLayout.astro';
import Hero from '~/components/Hero.astro';
import FAQ from '~/components/FAQ.astro';
import FinalCTA from '~/components/FinalCTA.astro';

const faqs = {faqs_js};
---

<BaseLayout
  title="{meta['title'].replace('"', '&quot;')}"
  description="{meta['description'].replace('"', '&quot;')}"
  pageType="article"
  articleDate="{meta['date']}"
  faqs={{faqs}}
  breadcrumbs={{[
    {{ name: 'Home', url: '/' }},
    {{ name: 'Guides', url: '/' }},
    {{ name: '{meta['title'].split(':')[0].replace(chr(39), chr(39))}', url: '/{slug}/' }},
  ]}}
  ogImage="/images/hero/plantation-shutters.webp"
>
  <Hero
    eyebrow="Guide"
    title="{meta['title'].replace('"', '&quot;')}"
    image="/images/hero/plantation-shutters.webp"
    breadcrumbs={{[
      {{ name: 'Home', url: '/' }},
      {{ name: 'Plantation Shutters', url: '/services/plantation-shutters/' }},
      {{ name: 'Guide', url: '/{slug}/' }},
    ]}}
  />

  <article class="py-20 md:py-28 bg-white">
    <div class="container-narrow prose-cfc">
{body_html}

      <div class="mt-12 p-8 bg-cream border-l-4 border-brand-500">
        <h3 class="font-display text-2xl text-ink-800 mb-3">Questions About Your Project?</h3>
        <p class="text-ink-600 mb-5">Call <a href="tel:+17272404512">(727) 240-4512</a> or <a href="/contact/">schedule a free in-home consultation</a>.</p>
      </div>
    </div>
  </article>

  {{faqs.length > 0 && <FAQ items={{faqs}} heading="Frequently Asked Questions" eyebrow="FAQ" subtitle="Common questions about plantation shutters in St. Pete." />}}

  <FinalCTA />
</BaseLayout>
'''
    target = PAGES_DIR / f"{slug}.astro"
    target.write_text(page, encoding="utf-8")
    print(f"  wrote {target}")

print("Done.")
