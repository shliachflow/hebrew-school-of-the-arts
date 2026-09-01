#!/usr/bin/env python3
r"""
Render content/site.json into the HTML, and generate sitemap.xml / robots.txt.

Three mechanisms, because HTML comments are only legal in some places:

  1. MARKERS - for visible body copy.
         <!--f:hours-->10:00 AM &ndash; 12:00 PM<!--/f-->
     Everything between the markers is replaced by that field's value. The
     markers are invisible in a browser, and the HTML remains correct even if
     this script never runs. That is the point: the site is never dependent on
     a build having happened.

  2. RULES - for <meta> content attributes and JSON-LD, where an HTML comment
     would be invalid. These are anchored per-file regexes, deliberately narrow.

     They are per-file and heavily anchored ON PURPOSE. A broad pattern like
     r"ages \d+-\d+" also matches "ages 4-5" on the Sprouts page and would
     silently rewrite a division's age band into the whole-school range.

  3. ABSOLUTE SELF-REFERENCES - canonical, og:url, og:image, twitter:image.
     Rewritten to site_url. These were hard-coded to hebrewschool.jewishtroy.com,
     which does not resolve. A canonical pointing at a dead host tells Google the
     page it is crawling is a duplicate of something that does not exist, so
     nothing gets indexed: not the live URL, not the canonical target. Driving
     them from one field makes the move to the real domain a single edit.

Safety property: running this with an unchanged site.json produces a zero-byte
diff. `python build.py --check` asserts exactly that and is what CI runs.
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).parent
PAGES = ["index.html", "program.html", "register.html", "scholarship.html",
         "divisions/sprouts.html", "divisions/roots.html",
         "divisions/mitzvah-crew.html", "divisions/bat-mitzvah-club.html"]

MARKER = re.compile(r"(<!--f:([a-z0-9_]+)-->)(.*?)(<!--/f-->)", re.S)

# JSON-LD @id and url. These were hard-coded to hebrewschool.jewishtroy.com and
# build.py did not touch them, so structured data declared a host that does not
# exist - the same failure the canonical tags had, in the one place Google reads
# to identify the entity. Driven from site_url like everything else.
LD_URL = re.compile(r'("(?:@id|url)":\s*")https?://[^"#]*(#[^"]*)?(")')

# canonical / og:url point at the page itself; og:image / twitter:image at the card.
# The path is derived from the FILENAME, never parsed out of the existing URL - an
# earlier version matched its own output and doubled the repo segment on every run,
# so the build was not idempotent. --check would have caught it; this is why that
# assertion exists.
SELF_URL = re.compile(r'((?:rel="canonical" href|property="og:url" content)=")[^"]*(")')
CARD_URL = re.compile(r'((?:property="og:image" content|name="twitter:image" content)=")[^"]*(")')

# Anchored, per-file. Each entry: (regex with one capture group each side, template).
RULES = {
    "index.html": [
        (r"(three divisions for ages )[\d-]+(\. Troy)",            "{age_range_plain}"),
        (r"(Ages )[\d-]+(, Sundays in Troy)",                      "{age_range_plain}"),
        (r'("audienceType": "Children ages )[\d a-z]+?(")',        "{age_range_prose}"),
        (r'("text": "Ages )\d+ through \d+(, across)',             "{age_min} through {age_max}"),
        (r"(Tuition is \$)\d+( per child for the full school)",    "{tuition_num}"),
        (r"(plus a \$)\d+( registration fee per child\. New)",     "{reg_fee_num}"),
    ],
    "program.html": [
        (r"(Sundays, ages )[\d-]+(\.)",                            "{age_range_plain}"),
    ],
    "register.html": [
        (r"(Tuition is \$)\d+( for the year)",                     "{tuition_num}"),
        (r"(plus a \$)\d+( registration fee per child)",           "{reg_fee_num}"),
    ],
}


def load():
    d = json.loads((ROOT / "content" / "site.json").read_text(encoding="utf-8"))
    f = {k: v for k, v in d.items() if not k.startswith("_")}
    f["age_range_prose"] = "%s to %s" % (f["age_min"], f["age_max"])
    f["tuition_num"] = f["tuition"].lstrip("$")
    f["reg_fee_num"] = f["reg_fee"].lstrip("$")
    return f


def render(page, text, f):
    unknown = []

    def sub(m):
        key = m.group(2)
        if key not in f:
            unknown.append(key)
            return m.group(0)
        return m.group(1) + str(f[key]) + m.group(4)

    text = MARKER.sub(sub, text)
    for pat, tmpl in RULES.get(page, []):
        text = re.sub(pat, lambda m: m.group(1) + tmpl.format(**f) + m.group(2), text)

    base = f["site_url"].rstrip("/")
    self_url = base + "/" + ("" if page == "index.html" else page)
    card_url = base + "/uploads/og-image.jpg"
    text = SELF_URL.sub(lambda m: m.group(1) + self_url + m.group(2), text)
    text = CARD_URL.sub(lambda m: m.group(1) + card_url + m.group(2), text)
    # JSON-LD lives inside <script>, where an HTML comment marker is illegal,
    # so it is rewritten by pattern like the meta tags. Any #fragment is kept:
    # "...#school" and "...#faq" are entity ids and must stay distinct.
    text = LD_URL.sub(lambda m: m.group(1) + base + "/" + (m.group(2) or "") + m.group(3), text)
    return text, unknown


def sitemap(f, pages):
    base = f["site_url"].rstrip("/")
    rows = []
    for p in pages:
        loc = base + "/" + ("" if p == "index.html" else p)
        pri = "1.0" if p == "index.html" else ("0.8" if "/" not in p else "0.7")
        rows.append("  <url>\n    <loc>%s</loc>\n    <priority>%s</priority>\n  </url>" % (loc, pri))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(rows) + "\n</urlset>\n")


def robots(f):
    base = f["site_url"].rstrip("/")
    return "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % base


def main(check=False):
    f = load()
    changed, problems = [], []

    for p in PAGES:
        path = ROOT / p
        if not path.exists():
            continue
        before = path.read_text(encoding="utf-8")
        after, unknown = render(p, before, f)
        problems += ["%s: unknown field '%s'" % (p, k) for k in unknown]
        if before != after:
            changed.append(p)
            if not check:
                with open(path, "w", encoding="utf-8", newline="") as fh:
                    fh.write(after)

    existing = [p for p in PAGES if (ROOT / p).exists()]
    for name, content in (("sitemap.xml", sitemap(f, existing)),
                          ("robots.txt", robots(f))):
        path = ROOT / name
        old = path.read_text(encoding="utf-8") if path.exists() else None
        if old != content:
            changed.append(name)
            if not check:
                with open(path, "w", encoding="utf-8", newline="") as fh:
                    fh.write(content)

    for m in problems:
        print("  !", m, file=sys.stderr)
    if check:
        if changed:
            print("OUT OF DATE - run `python build.py`:", ", ".join(changed))
            return 1
        print("HTML, sitemap and robots match content/site.json")
        return 0 if not problems else 1
    print("rendered:", ", ".join(changed) if changed else "no changes needed")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(check="--check" in sys.argv))
