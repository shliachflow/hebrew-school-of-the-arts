#!/usr/bin/env python3
r"""
Render content/site.json into the HTML.

Two mechanisms, because HTML comments are only legal in some places:

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

Safety property: running this with an unchanged site.json produces a zero-byte
diff. `python build.py --check` asserts exactly that and is what CI runs.
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).parent
PAGES = ["index.html", "program.html", "register.html", "scholarship.html",
         "divisions/sprouts.html", "divisions/roots.html",
         "divisions/mitzvah-crew.html", "divisions/bat-mitzvah-club.html"]

MARKER = re.compile(r"(<!--f:([a-z0-9_]+)-->)(.*?)(<!--/f-->)", re.S)

# Anchored, per-file. Each entry: (regex with one capture group each side, template).
RULES = {
    "index.html": [
        (r"(four divisions for ages )[\d-]+(\. Troy)",            "{age_range_plain}"),
        (r"(Ages )[\d-]+(, Sundays in Troy)",                      "{age_range_plain}"),
        (r'("audienceType": "Children ages )[\d a-z]+?(")',        "{age_range_prose}"),
        (r'("text": "Ages )\d+ through \d+(, across)',            "{age_min} through {age_max}"),
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
    f["age_range_prose"] = f"{f['age_min']} to {f['age_max']}"
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
    return text, unknown


def main(check=False):
    f = load()
    changed, problems = [], []
    for p in PAGES:
        path = ROOT / p
        if not path.exists():
            continue
        before = path.read_text(encoding="utf-8")
        after, unknown = render(p, before, f)
        problems += [f"{p}: unknown field '{k}'" for k in unknown]
        if before != after:
            changed.append(p)
            if not check:
                with open(path, "w", encoding="utf-8", newline="") as fh:
                    fh.write(after)

    for m in problems:
        print("  !", m, file=sys.stderr)
    if check:
        if changed:
            print("OUT OF DATE - run `python build.py`:", ", ".join(changed))
            return 1
        print("HTML matches content/site.json")
        return 0 if not problems else 1
    print("rendered:", ", ".join(changed) if changed else "no changes needed")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(check="--check" in sys.argv))
