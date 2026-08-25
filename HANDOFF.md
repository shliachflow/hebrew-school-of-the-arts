# Hebrew School of the Arts — handoff

**Start here.** Current state, decisions already made, and what is still open.

- **Live:** https://shliachflow.github.io/hebrew-school-of-the-arts/
- **Repo:** https://github.com/shliachflow/hebrew-school-of-the-arts
- **Target domain:** hebrewschool.jewishtroy.com (not live yet — see Open items)
- **Client:** Rabbi Menachem & Mrs. Chana Caytak, Chabad Jewish Center of Troy, MI

## Picking this up in a new session

    git clone https://github.com/shliachflow/hebrew-school-of-the-arts.git
    cd hebrew-school-of-the-arts

Then tell Claude: **"Read HANDOFF.md, design-digest.md and CONTENT-SOURCES.md, then continue."**

Those three files carry everything. Nothing important lives only in the chat.

| File | What it holds |
|---|---|
| HANDOFF.md | This file — state and open decisions |
| design-digest.md | Every design decision, why, and each revision. Read before changing any design. |
| CONTENT-SOURCES.md | Provenance of every claim: verified / client-supplied / written-for-the-build |
| README.md | Stack, local preview, the short rules |
| uploads/IMAGE-BRIEF.md | Every image slot with dimensions |

## Local preview

    pwsh -NoProfile -ExecutionPolicy Bypass -File .claude/serve.ps1

Serves on http://localhost:8153. Single-threaded, so it handles one request at a time — loading
several videos at once will appear to hang. It also has a dev-only POST /__save?name=x.jpg endpoint
that writes a base64 body into .claude/grabs/, used to pull canvas frames out of the browser for
visual review.

## What exists

Static HTML and CSS. No build step, no framework, no dependencies. GitHub Pages from main.

| Page | Contents |
|---|---|
| index.html | Header, stat row, "You belong here" band, photo strip, 8 Sunday video reels, Sunday timeline, four division colour panels, program teaser, calendar, tuition, FAQ, final CTA, footer |
| program.html | Aleph Champ ladder (10 levels), The Kitchen, The Studio, what they'll know, six curriculum subjects |
| divisions/sprouts.html | Ages 3–5 |
| divisions/roots.html | Ages 6–8 |
| divisions/mitzvah-crew.html | Boys 9–13 |
| divisions/bat-mitzvah-club.html | Girls 9–13 |
| register.html | Tuition figures + empty Tally slot |
| scholarship.html | Scholarship terms + empty Tally slot |

**Design system:** Bespoke Slab 700 (display) + Switzer 400/500 (body), both from Fontshare —
deliberately not Google Fonts, which is where the "AI website" look comes from. Suez One is used
only for the Hebrew letters in the Aleph Champ ladder. Warm paper canvas, teal accent, four deep
division colours plus their pale tints as section bands. No drop shadows anywhere — depth is
hairlines and flat offsets. Tilt applies to photographs only, never cards or buttons.

**Assets:** 8 authentic Sunday videos in uploads/video/ (60MB total, 480x848 vertical). 4 photos in
uploads/photos/. 138 unvetted archive photos are gitignored.

## Open items

### Needs the client

1. **Hero image.** The right panel is built to hold a ~1800x900 landscape image edge-to-edge; it
   currently holds a cut-paper composition. Rabbi is generating one. Recommended concept: a close
   crop of children's hands and upper bodies at a craft table — modest by construction, avoids the
   AI weaknesses around faces and hands in crowds, and unlike camp.jewishtroy.com's wide kitchen
   shot. Drop it at uploads/hero.jpg; the slot has the exact markup to swap in.
2. **Three claims nothing outside the AI draft supports** — that the commercial kitchen exists,
   that there has been a dedicated art teacher from the beginning, and that every division caps
   enrollment. Confirm or pull.
3. **Menachem's confirm list** in CONTENT-SOURCES.md — Sunday hours (his live site says 10:30–12:00,
   this site says 10:00–12:30), term dates, four divisions vs the three on his live site, age bands.
4. **Photo permission.** Every photograph on the site shows identifiable minors and comes from the
   Family Hamantaschen Bake — a supermarket family event, not a school session. Decide: keep for the
   draft and swap later, or pull now.
5. **The two Tally forms** — main registration (with first-year-free built in) and a separate
   scholarship form.

### Decided but not yet done

6. **Shorten the homepage further** — collapse the Sunday timeline and the calendar into expandable
   sections. Homepage is ~12 screens desktop, ~15 mobile.
7. **Pages CMS** — .pages.yml and content/*.json were in the original brief and do NOT exist yet.
   All copy is currently hardcoded.
8. **Team and testimonials** — deliberately omitted. No real names, roles or quotes exist, and
   inventing them is what the client has objected to twice.

### Technical

9. **DNS.** CNAME is parked as CNAME.pending so the github.io preview URL works. To go live: add a
   DNS CNAME hebrewschool -> shliachflow.github.io, then git mv CNAME.pending CNAME. Note
   jewishtroy.com sits on Chabad.org's platform, so confirm who controls the registrar.
10. **Video weight.** 60MB across 8 files, served exactly as downloaded — not re-encoded, not
    compressed, faststart unverified. No ffmpeg was available. Worth optimising before launch.

## Things that will bite you

- **prefers-reduced-motion gates the reveal animation.** The hiding rule sits behind .js-reveal on
  the html element, added by script only after it confirms it can un-hide, with a 2.5s failsafe.
  Never hide content in CSS that only JS can restore — an earlier version blanked 20 sections.
- **Any img with an aspect-ratio needs height: auto.** The width/height attributes make the box
  height definite and silently cancel aspect-ratio.
- **figure has a default UA margin of 1em 40px.** It is reset globally; do not remove that.
- **Hebrew never takes negative letter-spacing, italic, or uppercase.** The .he rules carry
  !important as a guard rail. The Aleph Champ ladder runs direction: rtl on purpose.
- **Measure contrast, do not assume it.** Four real failures were caught this way. Compose alpha and
  element opacity properly, and walk up to the first non-transparent ancestor — measuring against
  rgba(0,0,0,0) returns nonsense.
- **The client's copy document is AI-generated.** It is a statement of intent, not a record of fact.

## Client's stated preferences

- Wants it fun, kid-facing, schoolish, with colour and energy — not restrained editorial.
- Reacts against the "typical AI font" look. Hence Fontshare over Google Fonts.
- Has twice caught invented content. Never write marketing copy over documentary photographs, and
  never publish an unverifiable claim.
- Sibling site camp.jewishtroy.com is the same client. The header structure was deliberately
  modelled on it; everything else must stay distinct. The only match he asked for in writing is the
  wordmark — "the Arts" in accent italic.
- Keep the tagline Make. Bake. Belong.
