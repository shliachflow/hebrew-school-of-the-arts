# Hebrew School of the Arts — handoff

**Start here.** Current state, decisions already made, and what is still open.

- **Live:** https://shliachflow.github.io/hebrew-school-of-the-arts/
- **Repo:** https://github.com/shliachflow/hebrew-school-of-the-arts
- **Target domain:** hebrewschool.jewishtroy.com (not live yet — see Open items)
- **Client:** Rabbi Menachem & Mrs. Chana Caytak, Chabad Jewish Center of Troy, MI

*Last updated 2026-08-26, after Menachem's revision brief.*

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
| README.md | Stack, local preview, content editing, the short design rules |
| uploads/IMAGE-BRIEF.md | Every image slot with dimensions |

## Local preview

    pwsh -NoProfile -ExecutionPolicy Bypass -File .claude/serve.ps1

Serves on http://localhost:8153. **Single-threaded**, so the eight-video homepage will appear to
hang — use `python -m http.server` for anything involving the reels. It also has a dev-only
POST /__save endpoint that writes a base64 body into .claude/grabs/, used to pull canvas frames
out of the browser for visual review.

## What exists

Static HTML and CSS. No framework, no dependencies. GitHub Pages from main.
One optional build step: `build.py` renders `content/site.json` into marked spans in the HTML.
**The site is correct whether or not the build has run** — never change that.

| Page | Contents |
|---|---|
| index.html | Header, stat row, "You belong here" band, photo strip, 8 Sunday video reels, Sunday timeline, four division colour panels, program teaser, calendar, tuition, FAQ, final CTA, footer |
| program.html | Aleph Champ ladder (10 levels), The Kitchen, The Studio, what they'll know, six curriculum subjects |
| divisions/*.html | Sprouts 4–5 · Roots 6–8 · Mitzvah Crew boys 9–13 · Bat Mitzvah Club girls 9–13 |
| register.html | Tuition figures + empty Tally slot |
| scholarship.html | Scholarship terms + empty Tally slot |

**Design system:** Bespoke Slab 700 (display) + Switzer 400/500 (body), both from Fontshare —
deliberately not Google Fonts. Suez One only for Hebrew in the Aleph Champ ladder. Warm paper
canvas, teal accent, four deep division colours plus pale tints as full-bleed section bands. No
drop shadows anywhere. Nothing rotates except the cut-paper spot marks' reveal animation.

**Assets:** 8 Sunday videos in uploads/video/, re-encoded 2026-08-26 with faststart. 4 photos in
uploads/photos/. 138 unvetted archive photos are gitignored.

## Open items

### Needs Menachem — these block finishing

1. **Three or four divisions, and the age bands.** His live site has three (4–5, 6–12, 12–13); the
   site is built with four. The gender split at 9–13 is the least evidenced part. **This is the one
   that changes how the site is built** — merging two division pages after launch is far worse than
   before. The minimum age is settled at 4; the bands inside the range are not.
2. **Art-forward vs. the tagline.** He asked for the program positioned art-forward with cooking
   secondary, and separately asked in writing to keep **"Make. Bake. Belong."** Baking is a third of
   the tagline, the band eyebrow is "Culinary. Creative. Jewish.", and program.html's centrepiece is
   a month-by-month baking cycle. Both can hold — tagline as slogan, surrounding copy re-weighted to
   the studio — but it is his call. **Nothing has been re-positioned yet.**
3. **How kitchen and studio are actually assigned.** He questioned "next week they switch"; it has
   been removed from the homepage. Two other pages still assert a rotation — `program.html:186`
   ("every division rotates through the kitchen every month") and `divisions/roots.html` ("full
   kitchen rotations", also in its meta description). **The site currently contradicts itself.** His
   answer fixes all three at once, which is why they were left rather than patched twice.
4. **Ryan Merritt.** To feature him prominently, per the brief: medium, where the work sells, a
   photo, and two or three sentences. Right now there is a name and one adjective.
5. **Pickup and ID.** The index.html FAQ states only people on the registration form may collect a
   child, and to bring ID. CONTENT-SOURCES flagged this as an unverified placeholder — **do not
   publish until confirmed** — and it was published anyway. Confirm or pull.
6. **Term end and break dates.** He gave a start (Oct 11) and a count (23) but no end. 23 sessions
   from Oct 11 with no breaks lands on **March 14, 2027**, so about nine weeks of breaks are
   unaccounted for. The site no longer publishes an end date.
7. **Hero image.** The right panel holds a ~1800x900 landscape image edge-to-edge; it currently
   holds a cut-paper composition and degrades correctly without one. He is sending photos.

### Decided

8. **Homepage length — leave it.** Previously "collapse the timeline and calendar into expandable
   sections". Dropped: he approved the design and said no redesign is requested.
9. **Photo permission — resolved.** Cleared to keep the Hamantaschen Bake photos.
10. **Team and testimonials** — still omitted. No real names, roles or quotes exist beyond Ryan
    Merritt, and inventing them is what the client has objected to twice.

### Technical

11. **The two Tally forms** — main registration (first-year-free built in) and a separate
    scholarship form. Both slots are empty, so **the site cannot take a registration.** Client is
    handling. Required fields are commented in the slot markup on each page.
12. **DNS.** Deferred by the client. CNAME is parked as CNAME.pending so the github.io URL works.
    To go live: DNS CNAME hebrewschool -> shliachflow.github.io, then git mv CNAME.pending CNAME.
    jewishtroy.com sits on Chabad.org's platform — confirm who controls the registrar.

## Things that will bite you

- **prefers-reduced-motion gates the reveal animation.** The hiding rule sits behind .js-reveal on
  the html element, added by script only after it confirms it can un-hide, with a 2.5s failsafe.
  Never hide content in CSS that only JS can restore — an earlier version blanked 20 sections.
- **Never make the HTML depend on build.py having run.** Same principle. The markers are comments;
  the real value sits between them in the file and is correct on its own.
- **Any img with an aspect-ratio needs height: auto.** The width/height attributes make the box
  height definite and silently cancel aspect-ratio.
- **figure has a default UA margin of 1em 40px.** It is reset globally; do not remove that.
- **Hebrew never takes negative letter-spacing, italic, or uppercase.** The .he rules carry
  !important as a guard rail. The Aleph Champ ladder runs direction: rtl on purpose.
- **Measure contrast, do not assume it.** Four real failures were caught this way. Compose alpha and
  element opacity properly, and walk up to the first non-transparent ancestor — measuring against
  rgba(0,0,0,0) returns nonsense.
- **Video rotation lives in metadata, not in the stored dimensions.** `hsa-2025-04-27.mp4` probes as
  848x480 but carries a -90 degree display matrix, so it renders vertically and always did. Read
  `side_data_list` rotation before concluding a clip is the wrong shape. Separately: the reel row is
  a 9:16 box with `object-fit: cover`, so a genuinely landscape source *would* be cropped to a
  zoomed centre sliver.
- **The client's copy document is AI-generated.** It is a statement of intent, not a record of fact.
  Two claims that reached the live site came from it and were never supported: enrollment caps, and
  the art teacher "since the beginning". Both are now gone.

## Client's stated preferences

- Wants it fun, kid-facing, schoolish, with colour and energy — not restrained editorial.
- Reacts against the "typical AI font" look. Hence Fontshare over Google Fonts.
- Has twice caught invented content. Never write marketing copy over documentary photographs, and
  never publish an unverifiable claim.
- Sibling site camp.jewishtroy.com is the same client. The header structure was deliberately
  modelled on it; everything else must stay distinct. The only match he asked for in writing is the
  wordmark — "the Arts" in accent italic.
- Keep the tagline Make. Bake. Belong. — but see open item 2.
- **Design is approved as of 2026-08-25.** No redesign requested.
