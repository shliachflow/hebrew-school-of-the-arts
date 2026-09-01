# Hebrew School of the Arts — marketing brief

**For a fresh session working on the enrollment campaign.** Self-contained: you do not need the
website repo to use this. Everything here is either verified or explicitly labelled as not.

*Written 2026-09-01. The website is built, live, and taking registrations and payments.*

---

## The one paragraph

Hebrew School of the Arts is a Sunday Hebrew school at the **Chabad Jewish Center of Troy,
Michigan**, for **ages 4–13**. It is built around a real art studio and a kosher kitchen: children
make things, and the Jewish learning comes through the making. It runs **Sundays 10:00 AM–12:00 PM**
for **23 sessions**, starting **Sunday, October 11, 2026**. Most children arrive knowing no Hebrew
at all, and that is the ordinary starting point rather than the exception. No synagogue membership
is required.

**Tagline: Make. Bake. Belong.**
**Descriptor: Creative. Culinary. Jewish.**

---

## The campaign window is short and real

Today is **September 1, 2026**. The first day is **October 11** — **40 days**, about **5 Sundays**.

This is genuine urgency and can be used. What CANNOT be used is scarcity — see the graveyard below.
There is no evidence of limited places and inventing it has already been corrected once.

---

## The offer — this is the strongest thing you have

> **New families: your first year of tuition is free.** You pay only the $100 registration fee
> per child.

That is the headline offer. A new family with two children pays **$200 for the entire school year**.

Full price for returning families is $950 tuition + $100 registration = **$1,050 per child**.

**Financial assistance exists and is unusually easy to ask for.** Funded by the Long Lake Plaza
Fund and H.E.R Management. It is confidential and **requires no proof of income and no financial
statements**. Families apply *before* registering. The $100 registration fee is never covered by
assistance. "No child is turned away for financial reasons" is the school's own framing and is
safe to use.

---

## Who this is for

- Jewish families across the **Metro Detroit area** — affiliated and unaffiliated, observant and not
- Parents whose children have **no Hebrew background at all** and who worry their child will be
  behind. The school's own line: a beginner is never behind, an advanced reader is never bored
- Parents who are not synagogue members and assume that disqualifies them. It does not
- Parents whose children resist "school on a Sunday" — the counter is that this one is a studio and
  a kitchen, not a classroom

Do not target "observant families looking for supplementary Judaic studies." That is the opposite
of the positioning. The core pitch is **belonging without prerequisites**.

---

## What actually makes it different (all verified)

1. **Art-forward, not craft-as-filler.** A dedicated art teacher comes **every single week**. The
   art room is led by **Ryan Merritt**, a painter based in Troy, trained at the Savannah College of
   Art and Design, who paints landscapes and geometric abstracts in oil and acrylic and teaches art
   history. Children take home an heirloom, not a worksheet — a menorah they designed, a seder plate
   the family will use for twenty years.
2. **A real kitchen, about once a month.** Every group takes its turn. Challah, latkes,
   hamantaschen, matzah. Not a hot plate in a classroom.
3. **Aleph Champ for Hebrew reading.** A real, named programme: ten colour levels (white, red,
   orange, yellow, green, blue, purple, brown, grey, black), three stripes inside each. Children are
   grouped **by reading level, not by age**, so nobody is the slowest child in the room.
4. **Two hours, nothing wasted.** Arrival → Hebrew in small groups → the studio (or the kitchen) →
   Torah and story → tasting what they made, then pickup.
5. **Three divisions:** Sprouts 4–5 · Roots 6–8 · Mitzvah Crew & Bat Mitzvah Club 9–13. The oldest
   division includes Bar and Bat Mitzvah preparation.

### The framing that tests best

The 11:40 block is described in the school's own words as **"the core Jewish ideas that shape how a
child sees themselves."** That is the emotional centre: parents are not buying Hebrew lessons, they
are buying a child who comes home proud. The sub-headline on the site is
*"Where kids create, cook, and come home proud."*

---

## Voice and tone

- **Plain English. No insider vocabulary.** This is a hard rule and it has been enforced across the
  whole site. Banned: tefillos, Shabbos, mitzvos, parsha, kashered, Gemara, haftarah, Alef-Bet,
  sufganiyot, Hebrew month names, "Jewish manhood." Say: prayers, Friday night, traditions, the
  week's Torah portion, certified kosher, Talmud, a memorized reading, Hebrew letters, jelly
  doughnuts, holiday names. **The pitch is that unaffiliated families belong, and it fails the
  moment the copy assumes the reader already knows the words.**
- Warm, concrete, unpretentious. Short sentences. Specific nouns — "a seder plate their family will
  use for twenty years" beats "meaningful Judaic experiences."
- Confident, never breathless. No exclamation marks stacked up, no "AMAZING," no countdown-timer
  energy.
- Never write marketing copy over a documentary photograph. If a photo shows one child at one
  table, do not caption it "every Sunday, all year."

---

## Visual identity

Match the site or the campaign will look like a different school.

**Type:** Bespoke Slab 700 (display) + Switzer 400/500 (body), both from Fontshare — deliberately
**not** Google Fonts, because the Google top-fifty is where the "AI-generated" look comes from. If
you cannot use Fontshare, a warm slab serif for display and a clean neutral grotesque for body.

**Colour:**

| Token | Hex | Use |
|---|---|---|
| paper | `#FBF6EC` | canvas — **never pure white** |
| ink | `#1F1B16` | primary text |
| ink-2 | `#6B6156` | secondary text |
| hair | `#E4D9C6` | hairlines |
| accent (teal) | `#17706A` | buttons, links — the ONLY accent on interface elements |
| hero word 1 | `#146B64` | "Make." |
| hero word 2 | `#B4560F` | "Bake." |
| hero word 3 | `#A32351` | "Belong." |

Pale section tints: mint `#E6EDE5`, butter `#F6EBD6`, sky `#E4EAF1`, blush `#F5E3E8`.

**Rules that make it look like this school and not a template:**
- **No drop shadows, anywhere.** Depth is 1px hairlines and flat colour. Zero `box-shadow` on the
  whole site; keep it that way.
- Small radii, 4–10px.
- Slight tilt is part of the language (about 1°) on photos and the hero words. Buttons and body copy
  never tilt.
- **Never put opacity on text.** It has caused three separate contrast failures on this project.
- One saturated moment per view. Not three competing ones.

---

## Assets you already have

**In the repo at `uploads/`, ~34MB total.**

- **8 real Sunday videos** (`uploads/video/`), 480×848 **vertical phone video**, 20–61 seconds each.
  These are the school's own weekly recaps from actual Sundays — Dec 22, Jan 12, Jan 19, Jan 26,
  Feb 2, Apr 27, May 4, plus a model matzah bakery. **Native reel format.** This is the single
  most valuable asset for social and it is already shot, already vertical, already authentic.
  Each has a hand-picked poster frame in `uploads/video/posters/`.
- **4 session photographs** (`uploads/photos/`), 1200×1600, supplied by Menachem 2026-08-26:
  a child shaping coloured dough on foil trays · a child drawing with coloured pencils · a child
  holding up a decorated flower pot with classmates behind · a child in a smock with a snack.
- **A 1200×630 share card** (`uploads/og-image.jpg`) — tagline in the three hero colours, wordmark.

**Photo permission:** all four show identifiable children and were supplied by the school for this
purpose; the shliach cleared photography on 2026-08-26. There is still **no documented parental
release**. Fine for the school's own channels. Get explicit confirmation before using a child's
face in paid advertising.

---

## THE GRAVEYARD — claims that must never appear

Every one of these was on the site and was removed because it could not be supported. The client
has caught invented content **three times**. This section is the most important part of this brief.

| Never say | Why |
|---|---|
| "Spots are limited" / "enrollment caps" / "filling fast" | No evidence either way. Six such claims were removed from the site. |
| Anything about **pickup procedure, ID checks, security** | The client said explicitly: *"That's not accurate."* Removed entirely. |
| "A dedicated art teacher **since the beginning**" | He confirmed weekly attendance, not history. Say "every week," never "since the beginning." |
| **Any end date for the school year** | He gave a start and 23 sessions but no end, and has said he does not know yet. 23 Sundays from Oct 11 with no breaks lands on March 14, 2027, so ~9 weeks of breaks are unaccounted for. Say "the full schedule, including breaks, will be published soon." |
| **Testimonials or parent quotes** | None exist. Not one. Do not write a representative one. |
| **Staff names beyond Chana Caytak and Ryan Merritt** | No roster exists. |
| Allergy handling promises — "every allergy accounted for," "reviewed before the year starts" | Unverified **safety** claim. Removed once already. The form *asks* about allergies and promises nothing about what happens next. |
| "We had the kitchen certified kosher" | The kitchen's existence is confirmed by the shliach; the certification wording is not. |
| Captions asserting what a photo does not show | Four invented captions were removed for exactly this. |

**Two amber items — usable, but know their status:**

- **"Ryan Merritt's work sells internationally"** — published on the shliach's authority. His own
  site does not say it; it records a first show in 2023 at Arts, Beats and Eats in Royal Oak. Fine
  to repeat because the client vouched for it. Do not embellish it further.
- **Ryan Merritt's gender is never stated** on his own site, which is written in the first person.
  The site's bio is deliberately **pronoun-free**. Keep it that way unless told otherwise.

---

## The verified fact sheet

| | |
|---|---|
| School | Hebrew School of the Arts |
| Run by | Chabad Jewish Center of Troy, MI |
| Director | Mrs. Chana Caytak · Rabbi Menachem Caytak |
| Address | 4050 Coolidge Hwy, Troy, MI 48098 |
| Phone | 248-873-5851 |
| Ages | 4 to 13 |
| Day & time | Sundays, 10:00 AM – 12:00 PM |
| First day | Sunday, October 11, 2026 |
| Length | 23 sessions (end date not yet set) |
| Tuition | $950 per child, per year |
| Registration fee | $100 per child — separate, and never covered by assistance |
| New families | First year of tuition free; the $100 still applies |
| Divisions | Sprouts 4–5 · Roots 6–8 · Mitzvah Crew & Bat Mitzvah Club 9–13 |
| Hebrew | Aleph Champ, 10 colour levels, grouped by level not age |
| Art | Weekly, led by Ryan Merritt |
| Kitchen | About once a month per group |
| Catchment | Across the Metro Detroit area |

**Do not list Troy, Auburn Hills and Rochester Hills as the catchment.** He corrected that
explicitly: say "families come from across the Metro Detroit area."

**Spelling:** **Chanukah** with a "Ch." He asked for this specifically.

---

## Where traffic goes

- **Website:** https://shliachflow.github.io/hebrew-school-of-the-arts/
- **Register:** `/register.html` — live, and **takes payment by card**
- **Financial assistance:** `/scholarship.html` — live. Families apply **before** registering.

**⚠️ The domain is about to change to `hsa.jewishtroy.com`.** DNS is with the ChabadOne team and
not yet done. **Do not print the github.io URL on anything durable** — flyers, banners, anything
that outlives a week. Wait for the real domain, or drive to a short link you control.

**What a family experiences when they register:** one submission per family, up to 4 children, and
a card payment at the end. A new family with 2 children is charged $200; a returning family with 2
is charged $2,100.

---

## Open questions that constrain the campaign

1. **The end date.** Cannot promise "runs through May." Not known.
2. **Scholarship families and the payment form.** A family with an approved award who selects
   "Returning family" is currently charged the full $1,050 per child — the form cannot apply an
   award. Until that is resolved, **any campaign aimed at families who need assistance should send
   them to the scholarship page or the phone, not straight to registration.**
3. **The culinary tagline.** The kickoff call had Menachem leaning toward adding a tagline about the
   culinary side. That predates his later art-forward instruction and the "kitchen is monthly"
   answer, which point the other way. Unresolved. **Make. Bake. Belong. is confirmed and safe.**
4. **DNS**, as above.

---

## Angles worth exploring

Offered as starting points, not a plan. All are supportable by the facts above.

- **"Your first year is free."** The offer is unusually strong and it is being buried. For a new
  family with two children this is a full school year for $200. Lead with it.
- **The reels are the campaign.** Eight authentic vertical videos of real Sundays, already shot.
  Most schools in this position are commissioning a video; this one has eight.
- **"Most kids start with zero Hebrew."** Aimed squarely at the parent who thinks their child is
  too far behind to start. This is the school's own verified line and it removes the biggest
  objection.
- **"No membership needed."** Removes the second biggest objection, and it is his own wording.
- **Ryan Merritt as a named draw.** A working painter teaching every week is a real differentiator
  and most competitors have nothing comparable.
- **Bar/Bat Mitzvah preparation** for the 9–13 division — a concrete reason for parents of older
  children who think they have left it too late.

---

## If you need more detail

The website repo carries the deeper records, and they are the source of truth for anything
factual:

| File | What it holds |
|---|---|
| `CONTENT-SOURCES.md` | Provenance of **every** claim: verified / client-supplied / written-for-the-build. Read before publishing any new factual statement. |
| `HANDOFF.md` | Site state, open decisions, settled decisions |
| `design-digest.md` | Every design decision and why |
| `FORMS-SPEC.md` | The registration and scholarship forms, including the payment logic |

**The governing rule of this project, which applies to marketing at least as much as to the site:
every published claim must be traceable. When in doubt, ask Menachem rather than writing something
plausible.**
