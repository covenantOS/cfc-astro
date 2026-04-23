"""Inspect FAQ structure + find all 'Central Florida' / 'Tampa Bay' mentions."""
import json

d = json.load(open(r"C:\Users\Willb\Claude\CFC\bricks_raw.json"))
content = d["content"]
by_id = {e["id"]: e for e in content}

# Find all elements containing 'Central Florida', 'Tampa Bay', 'Central FL'
print("=== Elements mentioning 'Central Florida' / 'Tampa Bay' / 'Tampa' ===")

def find_geo_strings(obj, path="", hits=None):
    if hits is None:
        hits = []
    if isinstance(obj, str):
        if "Central Florida" in obj or "Tampa Bay" in obj or "Central FL" in obj:
            hits.append((path, obj[:200]))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            find_geo_strings(v, f"{path}.{k}", hits)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            find_geo_strings(v, f"{path}[{i}]", hits)
    return hits

for e in content:
    s = e.get("settings", {})
    hits = find_geo_strings(s)
    if hits:
        print(f"\n  Element {e['id']} ({e['name']}) parent={e.get('parent')} label={e.get('label','')!r}")
        for path, val in hits:
            print(f"    {path} = {val!r}")

# Dump the FAQ structure
print("\n\n=== FAQ structure (look for pattern to clone) ===")
faq_heading = by_id.get("c347f4")
if faq_heading:
    faq_parent = faq_heading.get("parent")
    print(f"FAQ H2 parent (the FAQ section container): {faq_parent}")

    # Find the FAQ container's children = the individual FAQ Q&A blocks
    faq_section = by_id.get(faq_parent)
    if faq_section:
        print(f"FAQ section: {faq_section['name']} children={faq_section.get('children',[])}")
        for child_id in faq_section.get("children", []):
            child = by_id.get(child_id)
            if child:
                print(f"  Child {child_id} {child['name']} children={child.get('children',[])}")

# Dump the first FAQ Q&A block in full (so we can clone it)
print("\n\n=== First FAQ block (Q: 'Are plantation shutters good for Florida humidity?') ===")
q1 = by_id.get("67ad6f")
if q1:
    q1_parent = q1.get("parent")  # This is the Q&A container
    container = by_id.get(q1_parent)
    print(f"Q&A container: id={q1_parent} name={container['name']} children={container.get('children',[])}")
    # Show the Q&A container + all its descendants

    def walk(elem_id, depth=0):
        e = by_id.get(elem_id)
        if not e:
            return
        s = e.get("settings", {})
        preview = ""
        if "text" in s:
            preview = str(s["text"])[:100]
        print(f"{'  '*depth}[{e['name']}] id={elem_id} label={e.get('label','')!r}")
        print(f"{'  '*depth}  settings keys: {list(s.keys())}")
        if preview:
            print(f"{'  '*depth}  text preview: {preview!r}")
        for c in e.get("children", []):
            walk(c, depth + 1)

    walk(q1_parent)
