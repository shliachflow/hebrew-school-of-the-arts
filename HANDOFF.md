# Hebrew School of the Arts — handoff

**Start here.** Current state, decisions already made, and what is still open.

- **Live:** https://shliachflow.github.io/hebrew-school-of-the-arts/
- **Repo:** https://github.com/shliachflow/hebrew-school-of-the-arts
- **Target domain:** hebrewschool.jewishtroy.com (not live yet — see Open items)
- **Client:** Rabbi Menachem & Mrs. Chana Caytak, Chabad Jewish Center of Troy, MI

*Last updated 2026-08-27.*

## Picking this up in a new session

    git clone https://github.com/shliachflow/hebrew-school-of-the-arts.git
    cd hebrew-school-of-the-arts

Then tell Claude: **"Read HANDOFF.md, design-digest.md and CONTENT-SOURCES.md, then continue."**

Those three files carry everything. Nothing important lives only in the chat.

| File | What it holds |
|---|---|
| HANDOFF.md | This file — state and open decisions |
| **TALLY-BRIEF.md** | **The next job: the two registration forms.** Self-contained. |
| design-digest.md | Every design decision, why, and each revision. Read before changing any design. |
| CONTENT-SOURCES.md | Provenance of every claim: verified / client-supplied / written-for-the-build |
| README.md | Stack, local preview, content editing, the short design rules |
| uploads/IMAGE-BRIEF.md | Every image slot with dimensions |

## Local preview

    pwsh -NoProfile -ExecutionPolicy Bypass -File .claude/serve.ps1

Serves on http://localhost:8153. **Single-threaded**, so the eight-video homepage will appear to
hang. There is a second launch config, `hsa-threaded`, running `python -m http.server 8154` — use
that for anything involving the reels.

**Browser caching will lie to you.** Chrome served stale CSS across a fresh tab, a new CSS URL and
forced reflows. If a change is not showing, stop and restart the preview server before believing
the measurement. A hidden preview pane also stops re-laying-out entirely and returns frozen
geometry, which looks exactly like "my CSS did nothing".

## What exists

Static HTML and CSS. No framework, no dependencies. GitHub Pages from main.
One optional build step: `build.py` renders `content/site.json` into marked spans in the HTML and
generates `sitemap.xml` and `robots.txt`.
**The site is correct whether or not the build has run** — never change that.

| Page | Contents |
|---|---|
| index.html | Header, stat row, "You belong here" band, photo strip, 8 Sunday video reels, Sunday timeline, three division colour panels, program teaser, calendar, tuition, FAQ, final CTA, footer |
| program.html | Aleph Champ ladder (10 levels), The Kitchen, The Studio + Ryan Merritt, what they'll know, six curriculum subjects |
| divisions/*.html | Sprouts 4–5 · Roots 6–8 · Mitzvah Crew & Bat Mitzvah Club 9–13 |
| register.html | Tuition figures + **empty Tally slot** |
| scholarship.html | Scholarship terms + **empty Tally slot** |

**Design system:** Bespoke Slab 700 (display) + Switzer 400/500 (body), both from Fontshare —
deliberately not Google Fonts. Suez One only for Hebrew in the Aleph Champ ladder. Warm paper
canvas, teal accent, deep division colours plus pale tints as full-bleed section bands. No drop
shadows anywhere. Tilt IS part of the system — `--tilt-a/-b/-c`, 21 rotations, on the hero words,
tag chip, hero cards, division photos and studio pair. Buttons and body copy never tilt.
The digest still carries an early "nothing rotates" rule; that was reversed by the header rebuild.

**Content system:** `content/site.json` holds the 20 facts that change (hours, dates, ages,
tuition, `site_url`). Editable through Pages CMS via `.pages.yml`. A push to `content/` triggers
`.github/workflows/content.yml`, which runs `build.py` and commits the rendered HTML.
`python build.py --check` asserts the HTML matches the JSON.

**Assets:** 8 Sunday videos in uploads/video/, re-encoded with faststart (59MB → 32MB). 4 photos in
uploads/photos/. `uploads/og-image.jpg` is a generated 1200×630 share card. 138 unvetted archive
photos are gitignored.

## Open items

### The next job

1. **The two Tally forms.** See **TALLY-BRIEF.md** — it is self-contained and has the existing
   form's full field list. Both slots are empty, so **the site cannot take a registration.**

### Needs Menachem

2. **Term end and break dates.** He gave a start (Oct 11) and a count (23) but no end. 23 sessions
   from Oct 11 with no breaks lands on **March 14, 2027**, so about nine weeks of breaks are
   unaccounted for. He has said he does not know yet. The site publishes no end date and says the
   full schedule is coming, which is honest meanwhile.
3. **Roots at 6–8.** He confirmed the floor (4) and the top band (9–13 together) but never this
   one. His live site says 6–12. Weakest link in the age structure.
4. **Hero image.** The right panel holds a ~1800x900 landscape image edge-to-edge; it currently
   holds a cut-paper composition and degrades correctly without one. He is sending photos.

### Technical

5. **DNS — now the highest-value item on the project.** Deferred by the client, but every day the
   site is indexed at the github.io URL is authority built on a URL that gets abandoned. CNAME is
   parked as CNAME.pending. To go live: DNS CNAME hebrewschool -> shliachflow.github.io, then
   `git mv CNAME.pending CNAME`, then change `site_url` in `content/site.json` and run `build.py`
   — that one field drives every canonical, og:url, the sitemap and robots.txt.
   jewishtroy.com sits on Chabad.org's platform — confirm who controls the registrar.
6. **Google Search Console.** After DNS: verify the domain, submit the sitemap. Also get
   jewishtroy.com to link to the new site — one link from the established parent site is worth more
   than every on-page tweak. And check the Chabad center's Google Business Profile, which outranks
   websites for local queries.

### Settled — do not reopen

- **Three divisions**, ages 4–5 / 6–8 / 9–13. The boys/girls split at 9–13 was never real.
- **Kitchen runs about monthly**; the art studio is the weekly activity.
- **Art-forward positioning**, tagline "Make. Bake. Belong." retained. Copy re-weighted by
  reordering only — no claims changed.
- **Pickup/ID procedure** — he said it is not accurate. Removed.
- **Enrollment caps** — never had evidence. All six claims removed.
- **Homepage length** — leave it. He approved the design; no redesign requested.
- **Photo permission** — cleared for the Hamantaschen Bake photos.
- **Ryan Merritt** — bio published on program.html and the homepage teaser.

## Things that will bite you

- **prefers-reduced-motion gates the reveal animation.** The hiding rule sits behind .js-reveal on
  the html element, added by script only after it confirms it can un-hide, with a 2.5s failsafe.
  Never hide content in CSS that only JS can restore — an earlier version blanked 20 sections.
- **Never make the HTML depend on build.py having run.** The markers are comments; the real value
  sits between them in the file and is correct on its own.
- **Anything build.py rewrites must be idempotent.** A URL rewrite that parsed the existing URL
  matched its own output and doubled the repo segment on every run. Derive from the filename, not
  from what is already there. `--check` exists to catch exactly this.
- **Any img with an aspect-ratio needs height: auto.** The width/height attributes make the box
  height definite and silently cancel aspect-ratio.
- **align-self: stretch silently cancels a height on a grid item.** The hero panel ignored every
  height until align-self was overridden too.
- **figure has a default UA margin of 1em 40px.** It is reset globally; do not remove that.
- **Hebrew never takes negative letter-spacing, italic, or uppercase.** The .he rules carry
  !important as a guard rail. The Aleph Champ ladder runs direction: rtl on purpose.
- **Measure contrast, do not assume it.** Five real failures found this way, the last being
  `.rung-n` at opacity 0.75 failing on five of ten Aleph Champ rungs. **Opacity on text is the
  recurring bug on this project** — it has now caused three separate failures. Also:
  `querySelectorAll` does not see `::before`, so a sweep that ignores pseudo-elements misses them.
- **Video rotation lives in metadata, not stored dimensions.** `hsa-2025-04-27.mp4` probes as
  848x480 but carries a -90 degree display matrix, so it renders vertically and always did.
- **The client's copy document is AI-generated.** A statement of intent, not a record of fact.
  Two claims from it reached the live site and were never supported: enrollment caps, and the art
  teacher "since the beginning". Both are gone.

## Client's stated preferences

- Wants it fun, kid-facing, schoolish, with colour and energy — not restrained editorial.
- Reacts against the "typical AI font" look. Hence Fontshare over Google Fonts.
- Has twice caught invented content. Never write marketing copy over documentary photographs, and
  never publish an unverifiable claim.
- Sibling site camp.jewishtroy.com is the same client. The header structure was deliberately
  modelled on it; everything else must stay distinct. The only match he asked for in writing is the
  wordmark — "the Arts" in accent italic.
- Keep the tagline **Make. Bake. Belong.**
- **Design is approved as of 2026-08-25.** No redesign requested.
- **Do not assume anyone's gender.** Ryan Merritt's bio is written pronoun-free on purpose; an
  earlier draft inferred a pronoun from the name and was corrected.
