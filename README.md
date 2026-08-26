# Hebrew School of the Arts — Chabad Jewish Center of Troy

Marketing and enrollment site for the 2026–27 school year.
**Culinary. Creative. Jewish.** · *Make. Bake. Belong.*

- Preview: https://shliachflow.github.io/hebrew-school-of-the-arts/
- Target domain: hebrewschool.jewishtroy.com — **not live yet**, see `HANDOFF.md`

## Stack

Plain static HTML/CSS. No framework, no bundler. GitHub Pages from `main`.

The only build step is `build.py`, and it is optional — it renders
`content/site.json` into marked spans in the HTML. The site is correct whether
or not it has run. Never make the HTML depend on a build having happened.

## Files

| Path | What it is |
|---|---|
| `index.html` | Homepage |
| `program.html` | Aleph Champ ladder, the Kitchen, the Studio, curriculum |
| `divisions/*.html` | One page per division |
| `register.html`, `scholarship.html` | Tuition + Tally form slots (**both slots still empty**) |
| `style.css` | The whole design system. All tokens at the top. |
| `design-digest.md` | **Read before changing any design.** Every decision and why. |
| `CONTENT-SOURCES.md` | **Read before changing any copy.** Provenance of every claim. |
| `HANDOFF.md` | Current state and open decisions |
| `content/site.json` | The facts that change — edited via Pages CMS |
| `build.py` | Renders that JSON into the HTML. `--check` asserts they match. |
| `.pages.yml` | Pages CMS config |
| `uploads/IMAGE-BRIEF.md` | Every image slot with dimensions |

## Local preview

    pwsh -NoProfile -ExecutionPolicy Bypass -File .claude/serve.ps1

Serves on http://localhost:8153. **Single-threaded** — the homepage has eight
videos, so it will appear to hang. For anything involving the reels, use
`python -m http.server` instead.

## Editing content

Facts like hours, dates, ages and tuition live in `content/site.json` and are
editable through Pages CMS. A push to `content/` triggers `.github/workflows/content.yml`,
which runs `build.py` and commits the rendered HTML.

In the HTML those values sit between markers:

    <!--f:hours-->10:00 AM &ndash; 12:00 PM<!--/f-->

Do not hand-edit between markers; `build.py` overwrites it. Change the JSON.
Run `python build.py --check` to verify the two are in sync.

Copy that carries a **factual claim** is deliberately NOT in the CMS. It stays
in the HTML, versioned and reviewed against `CONTENT-SOURCES.md`.

## Before touching the design

Read `design-digest.md`. The short version, as actually shipped:

- **Type is Bespoke Slab 700 (display) + Switzer 400/500 (body)**, both from
  Fontshare. Suez One 400 is used *only* for Hebrew glyphs in the Aleph Champ
  ladder. Fontshare over Google Fonts is deliberate — the Google top-fifty is
  where the "AI website" look comes from. Do not add a fourth Latin weight.
- **No blurred shadows anywhere.** Currently zero `box-shadow` in the stylesheet;
  keep it that way. Depth is 1px hairlines and flat offset silhouettes.
- **Tilt is a real, tokenised part of the design** — `--tilt-a/-b/-c`
  (−1.3deg / 1.1deg / −0.8deg), applied to the hero headline words, the tag
  chip, the hero cards, division photos and the studio pair. 21 rotations in
  all. `design-digest.md` still carries an early "nothing rotates" rule; that
  was reversed by the header rebuild and the digest was never updated. **Buttons
  and body copy still never tilt** — that part of the rule holds.
- **Teal `--accent` is the only colour on buttons, links and focus rings.**
- **`--ceremony` gold appears in exactly three places** — the two Bar/Bat Mitzvah
  division marks and the Siyum calendar entry. Never on a button.
- **Paper-tier colours may be full-bleed section backgrounds.** The original
  illustration-only restriction was reversed in the premium pass; it is what made
  the page anemic.
- **Any `img` with an `aspect-ratio` needs `height: auto`** — the width/height
  attributes make the box height definite and silently cancel `aspect-ratio`.
- **No marker glyphs before list items.** No dots, chevrons, checks or icons.
  Lists use a CSS counter on hairline-ruled rows.
- **Hebrew never takes negative letter-spacing, italic, or uppercase.**
- **Contrast is measured, not assumed.** Four real failures were caught that way.

## Outstanding

See the "Open items" section of `HANDOFF.md`. The launch blockers are the two
empty Tally form slots and DNS.
