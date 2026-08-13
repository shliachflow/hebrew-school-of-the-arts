# Design Digest — Hebrew School of the Arts, Chabad of Troy

Per-client instantiation of Website Master Prompt v4, Sections 4–5. Read this at the start of
every session on this project. If a design decision is unclear mid-build, the answer is here —
do not re-derive it from the tradition library.

Client: Rabbi Menachem & Mrs. Chana Caytak, Chabad Jewish Center of Troy, MI
Project: Hebrew School of the Arts 2026–27 — rebrand of an existing school into a culinary + arts program
Kickoff: 2026-08-13 · Target ship: 1–2 weeks

---

## The five selections

**Tradition — M6 Contemporary Community, pitched to "the kitchen and the art room."**
Not M1 Contemporary Editorial: M1 lives on photography we do not have, and the client explicitly
wants kid energy and excitement, which M1's quiet register works against. Not V2 Mid-Century Summer
Camp: the client's sibling site camp.jewishtroy.com already owns the playful-poster space and this
must not read as its recolor. M6 pitched warm and energetic, with the visual language taken from the
two actual rooms — a real commercial kitchen and a real art studio.

**Font pairing — Suez One (display) + Assistant (body). Deviation from catalog, justified.**
M6's assigned pairings are P8 (Plus Jakarta Sans + Lora) and P1 (DM Sans + Source Serif 4). Both
rejected: DM Sans is the sibling camp site's body face, and neither Lora nor Source Serif covers
Hebrew. This site carries Hebrew (Alef-Bet, Modeh Ani, month names, the Aleph Champ ladder), and
Section 5 requires resolving the Hebrew face before selecting a pairing rather than after.
Suez One and Assistant both have genuine Hebrew coverage, matched apparent weight, and warm
chunky character that reads bakery-sign rather than comic-poster. Fraunces is excluded on purpose:
it is on both camp.jewishtroy.com and mohelvegas.

**Weight roster — exactly three, no others, ever:**
- Suez One 400 (display only; it ships one weight, so hierarchy comes from size)
- Assistant 400 (body)
- Assistant 700 (labels, eyebrows, buttons, nav)

No 500, no 600, no 800 anywhere. Hebrew must never receive synthesized bold — Assistant has real
400 and 700, so both roster weights physically exist in Hebrew. Verified requirement, not assumed.

**Palette — C1 Warm Editorial base, accent re-pitched. Two tiers, and the tiers are the discipline.**

UI tier — the only colors allowed on interface elements:
```
--paper      #FBF6EC   canvas (never pure white; camp.jewishtroy.com uses pure white)
--paper-2    #F3EADA   subtle surfaces, alternate bands
--ink        #1F1B16   primary text
--ink-2      #6B6156   secondary text, captions
--hair       #E4D9C6   hairline borders and dividers
--accent     #17706A   deep glaze teal — CTA, links, focus ring, brand mark. Nothing else.
--accent-ink #10534E   accent hover
--ceremony   #B4832A   RESERVED. See below.
```

Paper tier — illustration only, never on a button, link, border, or text:
```
--pp-berry   #B4335F
--pp-blue    #2E6FA7
--pp-mustard #E0A32E
--pp-green   #4E8E43
```

The teal is content-motivated, not decorative: two of four divisions are literally Sprouts and
Roots. It is also tonally opposite the camp site's hot brights (orange #FF6A13, red #D64B2A,
yellow #F5C842, lime #B7D817) — deep and desaturated against bright and saturated. Terracotta is
excluded because mohelvegas already uses #B5502E.

**Ceremony color** — `--ceremony` #B4832A appears in exactly three places and nowhere else:
the Mitzvah Crew division mark, the Bat Mitzvah Club division mark, and the end-of-year
Siyum & Art Show entry on the calendar. It never appears on a CTA, a link, a body text run, or
an ordinary card. If it shows up on a button, that is a bug.

**Hero pattern — H1 Asymmetric Split.** Copy anchored bottom-left with the four stat tiles beneath,
kitchen image bleeding off the right edge. Chosen over H3 Type-Dominant because the client wants
the culinary aspect leading rather than typography leading. Degrades to H4 Editorial Split if the
hero image never materializes — the layout must not collapse on a missing image.

**Layout register — alternating editorial rhythm, zero repeated card grids.**
Four divisions become four full-width rows that swap sides, each with its own paper mark and its
own linked page. The Sunday morning is a single-column time-stamped timeline — not numbered circle
badges. The Elul→Sivan kitchen cycle is a typographic month table with a paper mark per month. The
Studio is a two-up image pair. Tuition is a plain table, not a three-tier pricing card set.
Testimonials are a quote wall with real names and towns. Rhythm changes every two to three sections.

---

## Craft decisions

**Elevation mode — hairline, with a bespoke flat-offset language.**
Zero blurred box-shadows anywhere on the site; the shadow scale is deliberately absent from the
tokens rather than defined and unused. Depth comes from 1px hairlines and tonal contrast. The
illustration marks layer via *solid offset silhouettes at low opacity* — flat paper stacking, no
blur. That is not a shadow and does not break hairline mode. Do not add a blurred shadow to any
card, row, tile, or button.

**Geometry lane — rectangular-sober, small radii.** Deliberately opposite the camp site's pills and
global `-0.7deg` tilt. Nothing on this site rotates. Radius scale:
```
--r-xs 4px  · --r-sm 6px  · --r-md 10px · --r-lg 14px · --r-xl 20px · --r-full 9999px
```
`--r-full` is permitted only on the nav Enroll button and avatar-shaped elements. No pill cards.

**Spacing** — every value divisible by 8. `clamp()` for all type and section padding.
**Transitions** — exact properties only, `cubic-bezier(0.16, 1, 0.3, 1)`, never `transition: all`.
**Display tracking** — Latin only, per the size-scaling formula, floor −0.02em. Hebrew at 0.

## Hebrew handling

**English page with inline Hebrew accents.** Not parallel versions, not side-by-side bilingual.
Hebrew appears in: the Aleph Champ level ladder (Alef-Bet), Modeh Ani in the Sunday timeline,
month names in the kitchen cycle, and scattered terms. Rules, all non-negotiable:
- `letter-spacing: 0` on Hebrew. Never negative, at any size.
- No `font-style: italic` on Hebrew — the wordmark italic applies to "the Arts" in Latin only.
- No `text-transform: uppercase` on Hebrew. There is no case in Hebrew; the all-caps eyebrow
  pattern used for Latin labels must use size/weight/color for Hebrew instead.
- Hebrew set one step larger than adjacent Latin, judged optically.
- Extra line-height wherever nikud appears.
- Verify visually that Hebrew renders in Assistant, not a browser fallback.

## Deployment

Static HTML on GitHub Pages under the `shliachflow` org. Pages CMS via `.pages.yml`, content in
`content/*.json`, media in `uploads/`. Shared `style.css` rather than per-page inline styles —
nine pages make a shared stylesheet the maintainable choice. CNAME to
`hebrewschool.jewishtroy.com`. Registration via Tally embeds, CMS-editable embed slots.
Tokens ship as real CSS custom properties; there is no ChabadOne inline-compile step for this build.

## Do's and Don'ts — client-specific and checkable

1. **Don't** put `--ceremony` gold on any button, link, or body text. Three approved locations only.
2. **Don't** use a paper-tier color (berry, blue, mustard, green) on a UI element. Illustration only.
3. **Do** lead the hero with kitchen imagery cropped to hands and food — never AI-generated faces
   of children. See `uploads/IMAGE-BRIEF.md` for the exact prompts.
4. **Don't** rotate anything. The camp site tilts; this one does not.
5. **Don't** introduce a fourth font weight. Size, color and space carry hierarchy.
6. **Do** name Aleph Champ explicitly wherever Hebrew reading is described — it is a real program
   the school already uses, and the client's supplied copy omits it.
7. **Don't** let archive photography from jewishtroy.com run larger than about 600px on screen.
   The source files top out near 640px on the long edge; anything bigger will look soft.
8. **Do** keep one saturated accent moment per visible fold. The hero has one teal CTA, not three.

## Open / unconfirmed

- **Divisions: three or four.** The Zoom summary says three, the supplied copy says four, the
  current site has three. Client instruction is to build four separate division pages; going with
  four. Awaiting Menachem's confirmation.
- **Sunday hours** — supplied copy says 10:00–12:30, current site says 10:30–12:00. Building to the
  newer figure per client's precedence rule (Zoom > copy doc > current site).
- **Tuition** — current site says a flat $950/year plus $100 registration per child, not covered by
  scholarship. Supplied copy implies an unconfirmed multi-child sliding scale. Building with the
  $950/$100 figures visible and the sliding scale as CMS-editable placeholders.
- **First-year-free offer** — confirmed in scope by client, folded into the main registration form
  rather than a separate one. Absent from the supplied copy entirely.
- **Reels** — confirmed in scope: gallery must accept reels alongside photos.
- **Aleph Champ level colors** — the ladder's official color sequence is not yet verified. The
  build uses an illustrative sequence; confirm against the program's real levels before launch.
- **Team roster** — supplied copy is garbled (`[Name] — Ryan Merritt`). Real name→role mapping
  outstanding. Current site names only Chana Caytak, as "Hebrew School Director" (copy says
  "Co-Director").
- **School name** — "Hebrew School of Arts" vs "Hebrew School of the Arts" is inconsistent on the
  client's own current site. Building with "the Arts", since the wordmark italic depends on it.
- **No dark mode requested; none built.**
- **No logo file supplied** — typographic wordmark in use, "the Arts" in Suez One italic at
  `--accent`, echoing the camp site's one-word-italic device. This is the single intentional
  resemblance to camp.jewishtroy.com, and the client asked for it in writing.
- **External reference consulted:** none.

---

## Revisions

### 2026-08-13 — premium pass

Client feedback, in order: the page read dead; then the energy was better but it should look like a
professional agency made it rather than an AI; then the language was too insider; then some copy
felt generically AI-written. Each produced a real change.

**Hebrew requirement dropped.** The client confirmed no Hebrew is needed anywhere except the Aleph
Champ ladder. This invalidated the reason Suez One + Assistant were selected — that pairing existed
*because* both cover Hebrew. With the constraint gone the typography was re-picked on merit.

**Font pairing is now Bricolage Grotesque (display) + Instrument Sans (body).** Bricolage is a
variable grotesque with genuine designed character and an optical-size axis, heavy enough to carry a
children's program where a delicate serif would fight the brief. Suez One survives *only* for the
Hebrew letters in the Aleph Champ ladder — a separate script voice, the way a monospace face is
treated in the master prompt's weight rule.
**Revised weight roster: Bricolage 700, Instrument Sans 400, Instrument Sans 600.** Plus Suez One
400 for Hebrew glyphs only. No fourth Latin weight.

**Paper-tier colors may now be full-bleed section backgrounds.** The original illustration-only
restriction is what made the page anemic. Reversed deliberately.

**Division blocks deepened.** The first colored pass used mid-saturation brights, which read
kindergarten next to the ten-color Aleph Champ ladder. Now deep and rich — forest `#2F5D3A`, amber
`#8F5A12`, indigo `#24476E`, wine `#8A2B48` — so the ladder is the single bright moment on the page.

**Aleph Champ colors are now the program's real ones**, from the client's own level chart: white,
red, orange, yellow, green, blue, purple, brown, grey, black, three stripes each. These are program
data and appear nowhere else on the site. The earlier eight-color guess is gone.

**Grain added** at 3% on the hero and 5% on the dark band only — not as a divider on every section,
which is its own tell.

### 2026-08-13 — second premium pass (anti-AI-vibe)

Client: the colour is good, but the font reads like the typeface every AI site uses, and the page
still has the vibe of a generated site. Also flagged three specific pieces of made-up content.

**Typography moved off Google Fonts to Fontshare: Erode (display) + Switzer (body).** This is the
substantive point — the "AI website" typographic signature comes from the Google top-fifty, which is
the set every agent reaches for. Erode is drawn with deliberate organic irregularities in the
letterforms, which is the *handmadeness* trust signal Section 0 of the master prompt describes, and
it is the right argument for a school built on things children make by hand. It also restores
serif-against-sans contrast, which the all-sans Bricolage/Instrument pairing lacked.
**Revised weight roster: Erode 600, Switzer 400, Switzer 500.** Suez One 400 for Hebrew glyphs only.

**Structural tells fixed — these matter more than the typeface.** The remaining AI-ness was
skeletal, not typographic:
- *Marker glyph per bullet.* Every division list had a circle before each item — the "icon in a
  circle" tell in reduced form. Replaced with a CSS counter (`01`, `02`) on hairline-ruled rows.
  **Do not put a dot, chevron, check or icon in front of list items on this site.**
- *Four identical two-column division blocks*, which is a card grid rotated ninety degrees. Each
  division now has its own column proportions, its own image aspect ratio (5:4, 3:4, 4:3), its own
  vertical alignment, and Roots runs its list in two columns. Verified as four distinct layouts.
- *Uniform full-width stacked bands.* The studio pair now offsets its second image to break the
  flat top edge.

**`height: auto` is mandatory on any image with an aspect-ratio.** The `<img>` elements carry
width/height attributes to prevent layout shift, which makes the box height definite and silently
cancels `aspect-ratio`. All three per-division image shapes were doing nothing until this was fixed.

**Hero tracking relaxed to -0.03em** from -0.04em. The size-scaling formula puts a 96px heading near
-0.03em, and Erode is a serif — serifs collide at grotesque tracking.

**Content removed at client request**, all three unverifiable filler:
- "A child who bakes the challah doesn't need to be told why Friday night matters" — an aphorism
  that cannot be true or false.
- "every allergy is accounted for" — an unverified **safety** claim. Flagged in CONTENT-SOURCES and
  then left on the page anyway; that was the error.
- "we had it certified kosher" — the kitchen's existence is itself unverified.

### New rules

- **No insider vocabulary.** The school's core pitch is that unaffiliated families belong, and it
  fails if the homepage assumes the reader knows the words. Banned: tefillos, Shabbos, mitzvos,
  parsha, kashered, Gemara, haftarah, Alef-Bet, sufganiyot, Hebrew month names, "Jewish manhood".
  Use prayers, Friday night, traditions, the week's Torah portion, certified kosher, Talmud, a
  memorized reading, Hebrew letters, jelly doughnuts, holiday names.
- **Never hide content in CSS that only JS can restore.** The scroll-reveal hiding rule is gated
  behind `.js-reveal` on `<html>`, added by script only after it confirms it can un-hide, plus a
  2.5s failsafe that drops the gate if nothing revealed. An earlier version hid twenty sections
  behind an IntersectionObserver that never fired.
- **Do not caption documentary photographs with marketing claims.** Four invented captions ("Hands
  on, every Sunday") were removed: the photos are all from one supermarket event, not weekly
  sessions. One honest credit line replaced them. See `CONTENT-SOURCES.md`.
- **Every published claim must be traceable.** `CONTENT-SOURCES.md` labels every fact as verified,
  client-supplied-unverified, or written-for-the-site. The client's copy document is AI-generated
  and is a statement of intent, not a source of fact.
- **Contrast is measured, not assumed.** Three failures were caught by measuring rather than
  eyeballing: white on the original green (3.98:1), `.d-ages` at `opacity: 0.85`, and white on the
  real Aleph Champ green (3.33:1 — that rung now takes dark text, since the level color itself
  cannot be altered).
