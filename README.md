# Hebrew School of the Arts — Chabad Jewish Center of Troy

Marketing and enrollment site for the 2026–27 school year.
**Culinary. Creative. Jewish.** · *Make. Bake. Belong.*

Live: https://hebrewschool.jewishtroy.com

## Stack

Plain static HTML/CSS. No framework, no build step. Hosted on GitHub Pages.
Content is edited through [Pages CMS](https://pagescms.org) via `.pages.yml`;
editable copy lives in `content/*.json` and images in `uploads/`.

## Files

| Path | What it is |
|---|---|
| `index.html` | Homepage |
| `style.css` | The whole design system — all tokens live at the top |
| `design-digest.md` | **Read this first.** Every design decision and why. Rules that govern the tokens. |
| `uploads/IMAGE-BRIEF.md` | Every image slot: size, filename, and a ready-to-use generation prompt |
| `content/` | CMS-editable copy (JSON) |
| `.claude/serve.ps1` | Local preview server on port 8153 |

## Local preview

```bash
pwsh -NoProfile -ExecutionPolicy Bypass -File .claude/serve.ps1
```

Then open http://localhost:8153.

## Before touching the design

Read `design-digest.md`. The short version:

- **No blurred shadows anywhere.** Depth comes from 1px hairlines and flat offset silhouettes.
- **Three font weights total** — Suez One 400, Assistant 400, Assistant 700. Do not add a fourth.
- **Two color tiers.** Teal `--accent` is the only color allowed on buttons, links and focus rings.
  The paper-tier colors (berry, blue, mustard, green) are for illustration and surface tints only.
- **`--ceremony` gold appears in exactly three places** — the two Bar/Bat Mitzvah division marks and
  the Siyum calendar entry. Never on a button.
- **Nothing rotates.** The sibling camp site tilts; this one does not.
- **Hebrew never takes negative letter-spacing, italic, or uppercase.** See the digest.

## Outstanding

Tracked in the "Open / unconfirmed" section of `design-digest.md` — division count, Sunday hours,
tuition figures, the team roster, and the official Aleph Champ level colors.
