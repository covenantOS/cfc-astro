import os
"""Fix C3 v2: iteratively fix ALL broken FAQ Answer text values on page 524.

The broken JSON has multiple unescaped `"` characters inside answer text
values — some are word-quotes (e.g., "Plantation shutters"), some are inch
marks (e.g., 36" x 60"). We iterate: parse → find error → locate containing
string value → replace unescaped inner quotes (curly quotes for words,
prime symbol for inch measurements) → retry. Cap at 30 iterations.
"""
import json, urllib.request, base64, datetime, re

auth = base64.b64encode(f"daniel:{os.environ.get('CFC_WP_APP_PASS', '')}".encode()).decode()

def fetch(pid):
    req = urllib.request.Request(
        f'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/{pid}',
        headers={'Authorization': f'Basic {auth}'})
    return json.loads(urllib.request.urlopen(req).read())

def push(pid, content):
    req = urllib.request.Request(
        f'https://www.customfabriccreations.net/wp-json/cfc/v1/bricks/{pid}',
        data=json.dumps({'content': content}).encode(),
        headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'},
        method='POST')
    return json.loads(urllib.request.urlopen(req).read())

def find_containing_value(raw, pos):
    """Walk back from pos to find the `:"` that starts the enclosing string value.
    Returns (start_of_value, None) — caller walks forward to find terminator."""
    # Find last occurrence of `:"` before pos that's the start of a value
    # We want the one whose opening quote is at a position before pos.
    p = pos
    while p > 0:
        p -= 1
        if raw[p] == '"' and p > 0 and raw[p-1] == ':':
            # Make sure this isn't a `:\"` (escaped)
            if p >= 2 and raw[p-2] == '\\':
                continue
            return p + 1  # start of value is after the opening `"`
    return None

def fix_value_quotes(value_text):
    """Replace unescaped inner double quotes. Digit-preceded ones become prime (U+2033).
    Others alternate between left/right curly quotes."""
    out = []
    quote_open = True
    i = 0
    while i < len(value_text):
        c = value_text[i]
        if c == '\\' and i + 1 < len(value_text):
            out.append(value_text[i:i+2])
            i += 2
            continue
        if c == '"':
            # Inch-mark heuristic: previous char is a digit
            prev = value_text[i-1] if i > 0 else ''
            if prev.isdigit():
                out.append('\u2033')  # prime
            else:
                out.append('\u201c' if quote_open else '\u201d')
                quote_open = not quote_open
            i += 1
            continue
        out.append(c)
        i += 1
    return ''.join(out)

def try_fix(raw_json, max_iter=30):
    for it in range(max_iter):
        try:
            parsed = json.loads(raw_json)
            return raw_json, parsed, it
        except json.JSONDecodeError as e:
            pos = e.pos
            start = find_containing_value(raw_json, pos)
            if start is None:
                raise RuntimeError(f"Iter {it}: couldn't locate containing value at pos {pos}: {e.msg}")
            # Walk forward from start to find the true terminator of this value.
            # The terminator is a `"` followed by `}`, `]`, `,` or whitespace-comma.
            # Inside, we may encounter unescaped `"` that we must convert.
            # First: scan forward, fix unescaped quotes that aren't followed by `,` or `}` or `]`.
            # We need to be careful: a quote followed by `,"` is a real terminator.
            end = None
            p = start
            while p < len(raw_json):
                c = raw_json[p]
                if c == '\\':
                    p += 2
                    continue
                if c == '"':
                    # Look ahead
                    lookahead = raw_json[p+1:p+3]
                    if lookahead and lookahead[0] in '}],':
                        end = p
                        break
                    # else: this is an unescaped inner quote — skip and keep scanning
                p += 1
            if end is None:
                raise RuntimeError(f"Iter {it}: couldn't find terminator from start {start}")
            inner = raw_json[start:end]
            fixed = fix_value_quotes(inner)
            if fixed == inner:
                raise RuntimeError(f"Iter {it}: no fix made but still broken at pos {pos}")
            raw_json = raw_json[:start] + fixed + raw_json[end:]
    raise RuntimeError(f"Exceeded {max_iter} iterations")

def main():
    ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    d = fetch(524)
    content = d['content']

    with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_524_{ts}_pre_faq_json_fix_v2.json', 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2)

    target = next((e for e in content if e.get('id') == 'abe9b6'), None)
    if not target:
        print("Element abe9b6 not found"); return

    t = target.get('settings', {}).get('text', '')
    m = re.search(r'(<script[^>]*application/ld\+json[^>]*>)(.*?)(</script>)', t, re.DOTALL)
    if not m:
        print("No JSON-LD script found"); return

    opening, raw, closing = m.group(1), m.group(2), m.group(3)
    print(f"Raw JSON length: {len(raw)}")

    try:
        new_raw, parsed, iters = try_fix(raw)
    except Exception as ex:
        print(f"Fix failed: {ex}")
        return

    print(f"Fixed in {iters} iterations")
    if isinstance(parsed, list):
        types = [x.get('@type') for x in parsed if isinstance(x, dict)]
        print(f"  array of {len(parsed)} items, types: {types}")
        # Count FAQs
        for x in parsed:
            if isinstance(x, dict) and x.get('@type') == 'FAQPage':
                me = x.get('mainEntity', [])
                print(f"  FAQPage has {len(me)} Questions")
    elif isinstance(parsed, dict):
        if '@graph' in parsed:
            print(f"  graph of {len(parsed['@graph'])} items")
        else:
            print(f"  type: {parsed.get('@type')}")

    new_text = t[:m.start()] + opening + new_raw + closing + t[m.end():]
    target['settings']['text'] = new_text
    resp = push(524, content)
    print(f"PUSH: {resp}")

if __name__ == '__main__':
    main()
