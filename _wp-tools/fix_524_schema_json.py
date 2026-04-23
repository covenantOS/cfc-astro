import os
"""Fix C3: broken FAQ JSON-LD on /services/plantation-shutters/ page 524 element abe9b6.
Unescaped inner quotes around "Plantation shutters" in an Answer text.

Strategy: pull the raw JSON string out of the <script> tag, find the specific
Answer text with unescaped quotes, replace inner `"Plantation shutters"` with
curly-quoted equivalents (safest, preserves meaning, reads correctly in SERP).
Validate with json.loads before pushing back.
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

ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
d = fetch(524)
content = d['content']

# Backup
with open(rf'C:\Users\Willb\Claude\CFC\bricks_backup_524_{ts}_pre_faq_json_fix.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)

# Find element abe9b6
target = None
for e in content:
    if e.get('id') == 'abe9b6':
        target = e
        break

if not target:
    print("Element abe9b6 not found"); raise SystemExit

s = target.get('settings', {}) or {}
t = s.get('text', '')
print(f"Original text length: {len(t)}")

# Extract JSON payload between <script> tags
m = re.search(r'(<script[^>]*application/ld\+json[^>]*>)(.*?)(</script>)', t, re.DOTALL)
if not m:
    print("No JSON-LD script block found in element"); raise SystemExit

opening, raw_json, closing = m.group(1), m.group(2), m.group(3)
print(f"JSON payload length: {len(raw_json)}")

# Try parsing as-is
try:
    json.loads(raw_json)
    print("JSON is already valid — nothing to fix"); raise SystemExit
except json.JSONDecodeError as e:
    print(f"JSON broken at col {e.pos}: {e.msg}")

# Strategy: find the broken Answer text. The pattern is:
#   "text":""Plantation shutters" refers to...
# We want to replace the unescaped inner quotes. Cleanest: use curly quotes.
# The string spans from `"text":"` through to the closing `"` of the field.

# Find the Answer text field value. The broken text starts at "text":" followed by a `"`.
# Use a regex to find the acceptedAnswer that has this issue and fix only that field.
#
# Pattern: "acceptedAnswer":{"@type":"Answer","text":"<BROKEN>"
# The broken text starts with `"Plantation shutters"` and is the content of that field.
# Replace inner double quotes with curly double quotes in JUST this answer text.

# More robust approach: iterate character-by-character from the first broken Answer onwards,
# track JSON nesting, and when inside an Answer's text field value, convert unescaped
# double quotes to curly quotes. Actually simpler: just find the specific broken substring
# and patch it. The audit pinpointed `"text":""Plantation shutters"` as the failure.

# Direct surgical patch: find the broken pattern and fix it.
# The broken Answer text almost certainly starts: "Plantation shutters" refers to the
# wide-louver style that originated in Florida ...

# Replace every occurrence of `"text":""Plantation shutters"` with `"text":"\u201cPlantation shutters\u201d`
# (opening+closing curly quotes). Then scan the Answer text forward to find its terminator
# and escape any other internal double quotes we find before the next `","` field boundary.

# Find the broken Answer text boundaries
idx = raw_json.find('"text":""Plantation shutters"')
if idx < 0:
    print("Expected broken pattern not found — bail")
    raise SystemExit

# Walk forward from idx to find the true end of this Answer text.
# The Answer text value starts at idx + len('"text":"') and ends at the closing `"`
# followed by `}` (closing acceptedAnswer) or `","` (next field).
start_of_value = idx + len('"text":"')

# Walk from start_of_value, tracking when we see a `"` followed by `}`, `,"` or similar
# — that's the real terminator. Anything in between should be treated as content.
p = start_of_value
terminator = None
while p < len(raw_json):
    c = raw_json[p]
    if c == '"':
        # Check what follows — is this the real terminator?
        nxt = raw_json[p+1:p+3]
        if nxt.startswith('}') or nxt.startswith(','):
            terminator = p
            break
    elif c == '\\':
        p += 1  # skip escaped char
    p += 1

if terminator is None:
    print("Couldn't find terminator of broken Answer text — bail")
    raise SystemExit

inner_text = raw_json[start_of_value:terminator]
print(f"\nBroken Answer text ({len(inner_text)} chars):")
print(f"  {inner_text[:200]}...")
print(f"  ...{inner_text[-100:]}")

# Replace unescaped double quotes in inner_text with curly quotes.
# Assume any `"` not preceded by `\` is a literal meant as a display quote.
fixed_inner = ''
i = 0
quote_open = True  # alternate between opening and closing curly quote
while i < len(inner_text):
    c = inner_text[i]
    if c == '\\' and i + 1 < len(inner_text):
        fixed_inner += inner_text[i:i+2]
        i += 2
        continue
    if c == '"':
        fixed_inner += '\u201c' if quote_open else '\u201d'
        quote_open = not quote_open
        i += 1
        continue
    fixed_inner += c
    i += 1

print(f"\nFixed Answer text:")
print(f"  {fixed_inner[:200]}...")

# Rebuild raw_json
new_raw = raw_json[:start_of_value] + fixed_inner + raw_json[terminator:]

# Validate
try:
    parsed = json.loads(new_raw)
    print(f"\nFixed JSON parses OK — top-level type: {type(parsed).__name__}")
    if isinstance(parsed, list):
        print(f"  array of {len(parsed)} items, types: {[x.get('@type') for x in parsed if isinstance(x, dict)]}")
    elif isinstance(parsed, dict):
        if '@graph' in parsed:
            print(f"  graph of {len(parsed['@graph'])} items")
        else:
            print(f"  type: {parsed.get('@type')}")
except json.JSONDecodeError as e:
    print(f"\nSTILL BROKEN at col {e.pos}: {e.msg}")
    start = max(0, e.pos - 80)
    end = min(len(new_raw), e.pos + 80)
    print(f"  context: ...{new_raw[start:end]}...")
    raise SystemExit

# Rebuild element text and push
new_text = t[:m.start()] + opening + new_raw + closing + t[m.end():]
target['settings']['text'] = new_text

resp = push(524, content)
print(f"\nPUSH: {resp}")
