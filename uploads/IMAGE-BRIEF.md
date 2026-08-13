# Image brief — Hebrew School of the Arts

Every image slot on the site, with its exact intent, dimensions, filename, and a ready-to-use
generation prompt. Whoever fills these — a Codex pass, a designer, or the client with real
photography — should not have to guess.

## The one hard rule

**No AI-generated faces of children.** Crop to hands, food, tools, and finished work.

Two reasons. Image models still produce tells in children's faces and hands that people notice,
and a fake photo of fake children on a real school's website is a trust problem the moment anyone
looks closely. Hands-and-flour compositions dodge both, and they are what good food editorial does
anyway. Real photography of real students replaces these as it arrives.

Where a face is genuinely unavoidable, use a real photo or leave the slot empty. Do not generate one.

## Shared style direction

Applies to every generated image so the set reads as one shoot:

> Warm natural window light from the left, slightly overexposed highlights. Warm paper and cream
> tones, deep teal and ochre accents. Shallow depth of field. Real domestic-commercial kitchen
> surfaces — stainless steel, butcher block, flour dust. Documentary food-editorial style, not
> stock-photo styling. No text, no logos, no watermarks, no faces. Photographic, not illustrated,
> not 3D rendered.

Avoid: cool blue light, glossy studio product lighting, perfectly clean surfaces, symmetrical
centered compositions, anything that looks staged.

## Slots

### 1. Hero — `uploads/hero-kitchen.webp`
- **Where:** homepage hero, right column, bleeds off the right edge
- **Size:** 1600 × 1800 px minimum (tall crop; it fills a full-height column on desktop and a
  341px-tall band on mobile, so keep the subject centered vertically)
- **Needs:** `fetchpriority="high"`, explicit width/height, real alt text
- **Prompt:**
  > Close overhead-angled shot of children's hands braiding challah dough on a floured butcher
  > block counter, flour dust suspended in warm window light, a metal mixing bowl and wooden rolling
  > pin at the edge of frame. Hands only, no faces visible. Warm cream and paper tones. Documentary
  > food-editorial photography, shallow depth of field.

### 2. Photo band — `uploads/band-studio.webp`
- **Where:** behind the dark "Messy Aprons. Big Ideas. Jewish Pride." band (currently flat ink,
  image optional — only add it if it beats the flat color, and keep a dark scrim over it)
- **Size:** 2000 × 900 px
- **Prompt:**
  > Wide shot of a children's art studio table from above: paint-stained palettes, brushes in jars,
  > ceramic tiles mid-mosaic, scraps of colored paper. No people. Warm overhead light, deep teal and
  > ochre paint visible. Documentary style.

### 3. The Kitchen section — `uploads/kitchen-wide.webp`
- **Size:** 1600 × 1100 px
- **Prompt:**
  > A real commercial kitchen with stainless steel counters and a large oven, set up for a children's
  > baking session: rows of small dough portions on trays, aprons hanging on hooks, bowls of flour and
  > sugar. Empty of people. Warm natural light from high windows.

### 4. The Studio section — `uploads/studio-pair-a.webp`, `uploads/studio-pair-b.webp`
- **Size:** 1200 × 1200 px each (square pair)
- **Prompt A:**
  > A hand-built ceramic seder plate, glazed in deep teal, sitting on a wooden table in warm light.
  > Slightly imperfect, clearly handmade by a child. Close crop, shallow depth of field.
- **Prompt B:**
  > A child-made mosaic menorah in colored tiles leaning against a cream plaster wall, warm side
  > light casting a soft shadow. Handmade and slightly uneven. Close crop.

### 5. Month cycle marks — SVG, not photography
Elul (challah), Kislev (latkes and sufganiyot), Adar (hamantaschen), Nissan (matzah),
Sivan (cheesecake). These are **flat cut-paper SVG shapes drawn in-repo**, using the paper-tier
palette from `design-digest.md` — not generated images. Do not replace them with photos.

### 6. Division marks — SVG, not photography
One flat paper mark per division: Sprouts, Roots, Mitzvah Crew, Bat Mitzvah Club. Mitzvah Crew and
Bat Mitzvah Club are the only two permitted to use `--ceremony` gold.

### 7. Open Graph card — `uploads/og-image.jpg`
- **Size:** exactly 1200 × 630 px, JPG or PNG (**not SVG** — SVG og:images do not render on
  Facebook, LinkedIn or iMessage)
- **Content:** the wordmark and "Make. Bake. Belong." set on the paper canvas over a cropped
  detail of the hero image. Text must be legible at thumbnail size.

### 8. Gallery — from the client's existing site
Real archive photography, pulled from the Chabad.org galleries on jewishtroy.com. See
`design-digest.md` for the extraction method (`photoArray[].LargeImage` on each gallery page).

**Resolution ceiling: about 640px on the long edge.** Fine for a gallery grid and small insets.
Never display one larger than ~600px or it will look soft. Do not use archive photos for the hero.

Albums available: Family Hamantash Bake (71 photos), Chanukah on ICE, Purim in the Jungle,
Purim: Under Construction, 1-Day Trip to NY, Letters for Life. Video (reels) lives on the Media
page as MP4s on `www1.clhosting.org`.

## Output format

Deliver every raster slot as **WebP**, plus a JPG fallback for the OG card. Include explicit
`width` and `height` attributes on every `<img>` to prevent layout shift. Lazy-load everything
below the fold; the hero image is the only one that gets `fetchpriority="high"`.
