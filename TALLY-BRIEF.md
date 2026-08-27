# The two Tally forms — brief for a fresh session

**The job:** build two Tally forms and embed them. The site cannot take a registration until this
is done; both slots currently say "call this number instead."

This file is self-contained. You do not need the rest of the project to do this work, but read
**HANDOFF.md** for the site's state and **CONTENT-SOURCES.md** before writing any copy that makes a
factual claim.

---

## Context in one paragraph

Hebrew School of the Arts is a Sunday school at the Chabad Jewish Center of Troy, Michigan, for
ages 4–13. The site is plain static HTML on GitHub Pages, no framework. It is built and the design
is client-approved — **no redesign is wanted.** What is left is the forms, DNS, and a hero photo.
The client is Rabbi Menachem Caytak; his wife Mrs. Chana Caytak directs the school. He has twice
caught invented content on this project, so nothing goes on the page that cannot be traced.

## Two forms, and why they are separate

Confirmed on the client call and recorded in `design-digest.md` and the slot comments:

1. **Registration** — `register.html`, slot `#registrationForm`
2. **Scholarship application** — `scholarship.html`, slot `#scholarshipForm`

**They are deliberately separate.** A family applies for assistance *before* registering. The
scholarship page says so and links accordingly. Do not merge them.

The **first-year-free** offer is folded into the *registration* form, not a third form.

## What each form must capture

Taken from the slot comments in the HTML, which are the recorded spec:

### Registration
1. Standard registration
2. **First-year-free option** — new families; the $100 registration fee still applies
3. **Every child's allergies — required field**
4. Authorized pickup names

### Scholarship
- Parents / guardians
- Children and ages
- Statement of need
- **The amount the family can contribute toward tuition**

Note the scholarship page states, verified from the client's own site, that assistance requires
**no proof of income and no financial statements**. The form must not contradict that by asking for
tax returns or pay stubs.

## The existing form to copy from

Live at **jewishtroy.com/HSA → Enroll**, i.e. `https://www.jewishtroy.com/6481699`.
It runs on Chabad.org's platform. Full field list as it stands:

**Student**
- Full Name * (first, last)
- Hebrew Name (first, last)
- Birth Date *
- Previous Jewish Education
- Grade entering * (dropdown: Kindergarten through 9th)
- Address * (street, line 2, city, state, zip, country)
- Additional notable information (free text — this is where allergies currently go)

**Parents**
- Father's Name * · Father's Cell *
- Mother's Name * · Mother's Hebrew Name · Mother's Cell *
- Mother Jewish by: * (Birth / Choice)
- Best way to send updates: * (Cell / Email / Handout)
- "I am willing to assist in school activities, please contact me" (checkbox)

**Payment**
- Full Tuition $950
- Subsidized Tuition $750
- Credit card (Visa / MC / Amex / Discover), security code, name, expiry, billing address
- Total, Submit

### Four things to resolve before copying it straight over

1. **Allergies are a free-text "additional notable information" field on the old form. The spec
   says allergies must be their own required field.** Allergy handling is a safety claim on this
   project and was already removed once from the site for being unverified. Make it explicit.

2. **The old form has no $100 registration fee.** It charges $950 or $750 as the whole amount. Our
   site says $950 tuition **plus** $100 registration per child, and that the registration fee is
   **not** covered by scholarship — both verified from the client's own scholarship page. Either
   the old form is out of date or the fee is collected some other way. **Ask before building the
   payment step.**

3. **"Subsidized Tuition $750" is a figure that appears nowhere on the new site.** It may be the
   scholarship rate, or a sliding scale, or stale. Worth confirming — it changes what the
   scholarship form should ask for.

4. **Payments.** The old form takes card details inline via Chabad.org. Tally does not do that the
   same way; it integrates with Stripe. Decide with the client whether the Tally form collects
   payment at all or registration stays free and payment is handled separately. **Do not build a
   card-collection flow without an explicit decision.**

Also note the old form asks "Grade entering" (Kindergarten–9th) while the new site is organised by
**age** (4–5, 6–8, 9–13). Pick one and be consistent, or ask for both.

## How to embed

Each slot is a `<div>` with a placeholder card inside. Replace the inner placeholder `<div>`, keep
the outer `<div id="...">`:

```html
<div id="registrationForm" style="margin-top:var(--s-8)">
  <!-- placeholder card lives here; swap it for the Tally embed -->
</div>
```

The slot comment above each one lists the required fields. **Update that comment if the spec
changes** — it is the only record of it in the code.

Keep the "until it is connected, call 248-873-5851" fallback text somewhere sensible until the form
is actually live.

## Style, if you style the form at all

- Warm paper canvas, **never pure white**: `--paper #FBF6EC`
- Text `--ink #1F1B16`, secondary `--ink-2 #6B6156`, hairlines `--hair #E4D9C6`
- The one accent, for buttons/links/focus: `--accent #17706A`
- **No drop shadows anywhere.** Depth is 1px hairlines. There is currently zero `box-shadow` in
  the stylesheet; keep it that way.
- Small radii, 4–10px. Fonts are Bespoke Slab 700 (display) and Switzer 400/500 (body).
- **Never put opacity on text.** It has caused three separate contrast failures on this project.

## What I could not give you

**I do not have the Zoom call notes or transcript.** What is above comes from `design-digest.md`,
`CONTENT-SOURCES.md` and the slot comments, which are what previous sessions recorded *from* that
call. Two things are recorded as decided on it and I would treat them as reliable:

- the scholarship form is **separate** from registration
- first-year-free lives **inside** the registration form

If the shliach still has the Zoom notes, they may settle the payment and registration-fee questions
above faster than asking Menachem again.

Also still missing entirely, from CONTENT-SOURCES: the early-bird deadline and the multi-child
tuition scale. If either is meant to be in the form, someone has to supply the numbers.
