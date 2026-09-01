# The two forms — what was built

Built 2026-08-31. Supersedes the "next job" section of **TALLY-BRIEF.md**, which stays in the repo
as the record of *why* these decisions were made and what was never confirmed.

| | Registration | Scholarship |
|---|---|---|
| Tally form id | `ODNABR` | `KYjMP8` |
| Public URL | https://tally.so/r/ODNABR | https://tally.so/r/KYjMP8 |
| Slot | `register.html` → `#registrationForm` | `scholarship.html` → `#scholarshipForm` |
| Pages | 5 + thank-you | 6 + thank-you |
| Status | Published in Tally, **not yet live on the site** | Published in Tally, **not yet live on the site** |

Both live in the same Tally workspace as the sibling project's **Kosher Culinary Camp** pair, and
were deliberately modelled on them — same "how many children" reveal pattern, same section
headings, same notification target. That form has 7 real submissions, so the pattern is proven for
this client rather than invented here.

## Going live is one attribute per page

```html
<div id="registrationForm" data-tally-form="ODNABR" data-tally-live="false" ...>
```

Set `data-tally-live="true"`. That is the whole change. Until then:

- No iframe is created and **`tally.so/widgets/embed.js` is never requested** — verified in the
  browser, not assumed. The page makes no third-party requests at all.
- The "call 248-873-5851" fallback card stays exactly as it was.

The loader sits inline before `</body>` on both pages. It only ever *adds* — it will not clear a
slot unless it has an embed to put in its place, per the project's rule about never hiding content
that only JS can restore.

**It sets the iframe `src` directly.** Tally's `embed.js` is supposed to populate `src` from
`data-tally-src`; `Tally.loadEmbeds()` was called and verifiably did **not** do so, which would
have left families looking at an empty box. `data-tally-src` is kept so `embed.js` can still take
over height management if it hooks in. Fixed fallback height is 900px with `min-height`, so a form
that does not get dynamic height scrolls inside its frame rather than being clipped.

## Registration — field by field

One submission per **family**. `How many children are you registering?` (1–4) reveals the Child
2/3/4 blocks by conditional logic. **Four children is the ceiling** — Tally has no repeating-group
block, so each child is a hard-coded set of fields. A fifth child means either a second submission
or adding a "Child 5" block set.

**Page 1 — intro.** Verified facts only: Sundays 10:00–12:00, 4050 Coolidge Hwy, ages 4–13, first
Sunday Oct 11 2026, 23 sessions, the schedule-coming line in his own wording, $950 tuition, $100
registration fee not covered by scholarship, first-year-free for new families, and that no payment
is collected here. Links to the scholarship page.

**Page 2 — children.** Per child: First name\*, Last name\*, Hebrew name, Date of birth\*,
Grade entering\*, Previous Jewish education, **Allergies or medical conditions we must know
about\***, Anything else.

**Page 3 — parents and contact.** Father: First\*, Last\*, Cell\*. Mother: First\*, Last\*,
Hebrew name, Cell\*. Then Email\*, Street\*, Apt, City\*, State\*, ZIP\*, Best way to send you
updates\* (Cell / Email / Handout), and last on the page, **Mother Jewish by\*** (Birth / Choice).

**Page 4 — enrollment and pickup.** Which applies to your family?\* (Returning — standard /
New — first year free, $100 per child still applies). Adults authorized to pick up your children\*.
Volunteering (optional).

**Page 5 — thank you.** Confirms receipt, says we will be in touch about tuition, the fee and the
schedule, gives the phone number. Promises nothing further.

\* = required. Everything unmarked is optional.

## Scholarship — field by field

**Page 1 — intro.** Long Lake Plaza Fund / H.E.R Management, confidential, **no proof of income and
no financial statements**, apply before registering, award confirmed before registration.

**Page 2 — parents.** Father's name\*, Mother's name\*, Email\*, Phone\*.

**Page 3 — children.** How many (1–4, same reveal pattern), then per child Full name\* and Age\*.

**Page 4 — the request.** States tuition is $950 per child. `What are you able to contribute toward
tuition this year?`\* (part / full assistance). Choosing *part* reveals a required USD amount field,
`Amount you are able to contribute per child, for the year`, minimum 0. Then
`Tell us about your situation`\* — the statement of need, worded to invite as much or as little as
the family wants to share.

**Page 5 — acknowledgements.** Two required checkboxes: the $100 fee is not covered; consistent
Sunday attendance, with illness and emergencies understood.

**There is no file upload, and there must never be one.** The page promises no financial paperwork.
A file field would contradict a verified claim.

## Decisions taken, and by whom

| Decision | Who | Note |
|---|---|---|
| One submission per family, not per child | client-side call, 2026-08-31 | Overrode the recommendation of one-per-child |
| Father / Mother exactly as the old form, both required | client-side call | See the known gap below |
| Keep `Mother Jewish by`, required, placed late | client-side call | The sibling camp form words this differently — see below |
| Build and embed, but keep the phone fallback | client-side call | Nothing public points at either form yet |
| No payment collection; Stripe later | client-side call | Additive change, not a rebuild |
| Allergies get their own required field per child | TALLY-BRIEF spec | Deviation from the sibling form, see below |
| Grade *and* date of birth, not one or the other | this build | Birth date gives age for division placement; grade matches the old form |
| Added `Pre-K` to the grade list | this build | The old form starts at Kindergarten, which a confirmed age floor of 4 cannot answer |
| Added an Email field | this build | The old form's recorded field list has none, but "best way to send updates: Email" implies one |
| No photo/media release, no medical-consent language | this build | The camp form has both. Not in the HSA spec and not written here — inventing consent text is exactly the drift this project keeps undoing |

### Deviation from the sibling form, on purpose

The camp form's allergy field is a required textarea **pre-filled with "None"**, which means a
parent can click straight past it. Allergy handling is flagged in CONTENT-SOURCES as a safety claim
and was already pulled from this site once for being unverified. Here the field is required with
**no default** and a placeholder telling the parent to type None if there are none. Same shape,
one less way to skip it.

Note also that the form *asks* about allergies and promises nothing about what happens next. The
claim "allergies reviewed before the year starts, severe allergies discussed directly" is still
unverified `[C]` and stays off both the site and the forms.

Likewise `Adults authorized to pick up your children` collects the names and describes **no
procedure**, because the pickup and ID procedure was removed from this site as not accurate.

## Known gaps

1. **A family with one parent cannot complete registration.** Father's First, Last and Cell and
   Mother's First, Last and Cell are all required, which is the old form's behaviour and was chosen
   deliberately. It will block single-parent, widowed and guardian households. Cheapest fix if it
   ever bites: make the second parent's three fields optional. Nothing else has to change.
2. **`Mother Jewish by: Birth / Choice`** is the old HSA form's wording. The sibling camp form asks
   `Religious background: Jewish by birth / Jewish by conversion / Not Jewish` of **both** parents.
   Two forms for one family of sites now ask this differently. Worth one decision from Menachem.
3. **Four children maximum**, both forms. See above.
4. **Notifications reach `rabbi@jewishtroy.com` — verified.** Tally warned
   `selfEmailTo: defaulted to current user` while saving, but reloading both forms afterwards
   confirms `selfEmailTo: rabbi@jewishtroy.com` on each, same as the camp form. The account owner
   is that address, so the default landed on the intended value. What is *not* possible without
   Tally Pro is adding a **second** recipient — so **Chana Caytak does not currently get these**,
   and she directs the school. Forwarding rule or a Pro seat, whichever is cheaper.
5. **No submission confirmation email to the family.** Also Pro. Families get the thank-you screen
   and nothing in writing.
6. **Input and button border radius could not be set** — Tally Pro. Colours *did* apply:
   background `#FBF7F0`, text `#1A1712`, accent and button `#17706A`. Fontshare faces (Bespoke Slab,
   Switzer) cannot load in Tally at all, so the forms use Tally's default face. They will read as
   close-but-not-identical to the site.
7. **The conditional logic is verified by construction and by production evidence, but not
   click-tested.** Both forms were reloaded from Tally after saving and every rule reads back
   correctly, on the right page, against the right option UUIDs. The one genuine risk was that
   Child 2-4 fields are left *required while hidden* — if Tally validated those, a family
   registering one child could never submit. **The camp form's real submissions settle it: five of
   its seven completed submissions chose "1" child**, with the hidden Child 2-4 required fields
   never filled. Tally does not validate hidden fields. The same holds for the scholarship form's
   conditional amount field when a family requests full assistance.

   Not verified: nobody has watched the reveal happen in a browser. This environment cannot lay out
   `tally.so` pages at all. **One test submission per form is still the right final check.**

   Worth knowing while testing: the camp form pre-fills its hidden allergy fields with "None", and
   its submissions therefore record "None" allergies for children who do not exist. These forms
   carry no defaults, so an unused child's fields come back genuinely empty.

## On calculations

There are none, in either form, by design — no payment step means no totals to compute. Worth
stating plainly because it is the obvious thing to want checked:

- **Registration** does no arithmetic. It states $950 tuition and $100 registration fee per child
  as fixed text and collects nothing.
- **Scholarship** has exactly one money field, `Amount you are able to contribute per child, for
  the year`. Verified: `$` prefix, US_DOLLAR format, minimum 0, required, and hidden until the
  family picks "We can contribute part of the tuition". Picking "We are requesting full assistance"
  leaves it hidden and the form still submits.
- **Nothing multiplies that amount by the number of children.** A family of three offering $200
  each shows as `$200`, and whoever reviews the application does the multiplication. A calculated
  total could be added — the camp form does exactly this for its pricing and its totals check out
  ($300 × weeks × children matched every one of its seven Stripe charges). It was left out here
  because the brief asked only for "the amount the family can contribute" and inventing a total
  implies a policy nobody has stated.

When Stripe is added later, that is where calculated fields will be needed, and the camp form is
the working reference for how to wire them.

## What the kickoff-call Zoom summary confirms

The full AI summary of the client call surfaced 2026-08-31. TALLY-BRIEF quotes one sentence of it;
the rest adds three things, none of which change what was built:

1. **Scholarship-separate is firmer than "likely".** The summary's body says they agreed on
   "including the first-year free option in the regular registration form and keeping scholarship
   applications separate." TALLY-BRIEF flagged an earlier session for hardening "likely as a
   separate form" into a certainty; that hardening now looks defensible rather than invented. The
   source is still internally inconsistent — "likely" in the action items, "deciding" in the
   summary — so it is corroboration, not proof. What got built matches either reading.
2. **Three divisions is corroborated** — the summary states the project "will have three
   divisions", independent of the 2026-08-26 answers. This strengthens the case for fixing
   `register.html`, which still says "four divisions".
3. **An open branding decision that no other file records.** Menachem was to "decide whether to
   keep the name or add 'Culinary' as a tagline", and the summary says he leaned toward keeping the
   name with a culinary tagline. This predates the 2026-08-25 art-forward instruction and the
   2026-08-26 kitchen-is-monthly answer, both of which point the other way. Neither form mentions
   culinary anything, so nothing is blocked — but the decision was assigned and appears never to
   have been closed.

Treat this summary the way CONTENT-SOURCES treats the copy document: **it is AI-generated meeting
notes, not a transcript.** It is evidence of what was discussed, not a record of exact words.

## At DNS cutover

Both forms hard-code `shliachflow.github.io` URLs in their intro text — registration links to the
scholarship page, scholarship links to the registration page. When `hsa.jewishtroy.com`
goes live those two links need editing **inside Tally**; `build.py` and `content/site.json` do not
reach into the forms.

## Still needs Menachem

Unchanged from TALLY-BRIEF.md and untouched by this build:

- **The registration-fee discrepancy.** His live Chabad.org form charges $950 or $750 as the whole
  amount and has no $100 fee. Our site says $950 + $100. Both figures on our side are verified from
  his own scholarship page, so either the old form is stale or the fee is collected another way.
  These forms take no money, so nothing is broken meanwhile — but the question is still open.
- **The $750 "Subsidized Tuition" figure**, which appears nowhere on the new site. The scholarship
  form asks families for an open amount instead of offering tiers, so it neither uses nor
  contradicts $750.
- **Early-bird deadline and the multi-child tuition scale.** Still missing entirely. Neither form
  mentions either, because no numbers exist.
- Whether a **photo/media release** belongs on the registration form. The camp form has one, the
  site publishes photographs of identifiable minors, and CONTENT-SOURCES flags parental permission
  as unconfirmed for launch. This is the strongest candidate for the next addition.
