# Automotive — Theme Contract

Prefix `AUTO`. This contract governs every AUTO study: the register, the five fixed themes, the
media rules, the claims limits, the anti-patterns and the page rhythm. It is derived from
`../../standards/08-VISUAL-REFERENCE-STYLE.md` and adds only what is this sector's own.

---

## The reading — *the job sheet*

A dealership has two halves and the honest one is the workshop. The most trustworthy document
this sector produces is the **itemised job sheet**: what was done, what was found, what was
*not* replaced and why, signed by somebody with a name. Everything the forecourt adds to that —
the gloss, the figure, the badge, the countdown — is the part a visitor has learnt to discount.

So the register is the job sheet given an editorial voice: **a serif display line, hairline
rules, itemised rows, one accent, almost no boxes, and a stated limit on every page.** The page
is set like a page, not assembled from cards.

**The emphasis device is one italic word in the accent**, inside the serif display line — never
bold inside a heading, never a highlighted pill. It is used once per composition.

---

## Typography

| Role | Face | Size | Weight | Leading / tracking |
| --- | --- | --- | --- | --- |
| Display (`h1`/`h2` of the section) | Serif (Georgia stack) | `clamp(2.3rem, 4.4vw, 4.2rem)` | 400 | 1.02 / −0.02em |
| Emphasis inside the display | Serif italic, accent | inherit | 400 | — |
| Statement | Serif | `clamp(1.3rem, 2.2vw, 1.9rem)` | 400 | 1.25 |
| Item title | Sans | 1.0–1.35rem | 600 | 1.25 / −0.005em |
| Eyebrow / label | Sans | 0.72rem | 650 | uppercase, 0.12em |
| Slate label (inside a field) | Sans | 0.62rem | 650 | uppercase, 0.16em |
| Body | Sans | 0.94–1.0rem | 400 | 1.55–1.6, measure ≤ 34rem, muted |
| Index numeral | Sans, bordered chip | 0.68rem | 650 | uppercase, 0.12em, **spelled as a word** |

The sans is the system stack; the serif is Georgia / Times / Iowan Old Style. **No web fonts, no
remote stylesheet.**

---

## The five themes

| # | Name | Paper | Ink | Accent | Refusal `--no` |
| --- | --- | --- | --- | --- | --- |
| 001 | Chalk & Racing Green | `#f6f5f1` | `#1c241f` | `#2f5d46` | `#6a706b` |
| 002 | Paper & Oxide | `#f8f5f2` | `#26211d` | `#9c4a22` | `#736a63` |
| 003 | Steel & Cobalt | `#f1f4f8` | `#1a222c` | `#2b5493` | `#66707a` |
| 004 | Bone & Aubergine | `#f8f5f7` | `#241d25` | `#5e3566` | `#6d6470` |
| 005 | Night & Signal *(inverted)* | `#16181a` | `#edeff0` | `#d9a441` | `#9a9d99` |

Each theme also carries a `--line` hairline, a `--band` tint and a `--media` field tone derived
from its paper. The accent appears on **no more than three small elements** per composition,
plus the one lead rule.

---

## The structure layer — one device per variant, in CSS only

**This register uses no `<svg>` at all.** The reference register rules out icon rows, and this
sector's icon vocabulary — the chequered flag, the speedometer dial, the crossed spanners, the
road with dashes — is exactly what the pass is removing. The structure layer is therefore built
from borders on positioned elements, which is enough:

| Variant | Device | Mechanism |
| --- | --- | --- |
| 001 | **The bay lines** | three absolutely positioned `<span>`s with `border-left`, standing behind the head |
| 002 | **The plate edge** | one span with `border-top` + `border-left` at the head's top-left |
| 003 | **The itemised sheet** | the bordered cell grid itself — cells share 1px lines, the first on the band tone |
| 004 | **The torque mark** | `.u` with `border-bottom` plus `::before`/`::after` risers, under the phrase the page turns on |
| 005 | **The ramp frame** | `.frame` with `border-left` + `border-top` holding the composition |

**One 3px accent lead rule per composition.** Never two.

---

## Media

Three honest subjects, and nothing else:

1. **The place the work happens** — the workshop bay, the ramp, the forecourt, the service
   reception, the parts counter, the handover desk, the wash bay, the road outside.
2. **People named by role only** — the technician at work, the service adviser at the desk, the
   parts keeper, the driver at the handover. Never a name, never a face presented as a
   testimonial.
3. **The thing the copy names** — the part on the bench, the tyre, the key on the counter, the
   job sheet, the inspection sheet, the tools laid out.

Rules:

- A field is **flat, bare and large**: one tone, no dashed border, no inner icon, no centred
  badge. Radius **6px**.
- One tiny uppercase tracked **slate label pinned bottom-left inside the field**, carrying the
  subject and the ratio: `THE BAY · 4:3`.
- Ratios are deliberate and mixed for rhythm: 4:3 and 16:9 for places, 3:4 and 4:5 for people,
  1:1 for a part, 21:9 for a long view.
- **Reserved areas stay empty.** No image, no `background-image`, no `data:` URI, no remote
  reference of any kind.
- **Never a vehicle presented as a specific vehicle.** No manufacturer name, wordmark, badge,
  model name, number plate or registration appears in a field label or a caption.

---

## Claims — what this sector may not say

No study may contain, as its own assertion:

- **Any manufacturer, wordmark, badge, model name, number plate or registration.**
- **Any figure**: price, monthly payment, APR, deposit, part-exchange value, mileage, service
  interval in miles, horsepower, top speed, nought-to-sixty, emissions, range, stock count,
  number of vehicles sold, years in business.
- **Any performance or economy claim** of any kind.
- **Any rating, review count, star, award, "voted", or testimonial attributed to a customer.**
- **Any urgency device**: countdown, "limited", "while stocks last", "ends soon", "only a few
  left", a deadline.
- The words *best, unbeatable, cheapest, lowest, guaranteed, risk-free, number one, leading,
  world-class, award-winning, top-rated, five-star, approved by, certified by, accredited by*
  applied to the business or its work.
- **Any invented trade body, scheme, standard, certification or warranty term.**
- **Any invented price, fee, opening hour, address, telephone number or email.**

Where a section's role *is* one of these — offers, finance, stats, reviews, certifications —
the study carries the **structure** with every value reserved, and says on the page why the
value is not printed. That refusal is the design, not an apology for it.

---

## The refusal tone

Every study states at least one limit, and every sentence that states a limit is set in the
`--no` graphite token, with only the operative clause in ink. This is the sector's signature
device in this pass. It is a *design* element: give it space, give it a rule, and in most
compositions give it the one accent lead rule.

---

## Anti-patterns

Never:

- A chequered flag, a speedometer dial, a gear-stick, crossed spanners, a wrench, a road with
  centre dashes, a tyre-tread motif, a gauge, a badge shape, a shield.
- A dark hero with a floodlit car and a gradient laid over it.
- Stat tiles in coloured boxes; a "why choose us" row of icons; pill tags on every card.
- A price table, a finance calculator, a stock ticker, a vehicle-specification matrix.
- Star glyphs, review cards with portraits, a logo wall of manufacturer marks.
- Alarm red as a UI colour. Gradients, shadows, dashed borders, pills, `background-image`.
- A global header, primary navigation or footer in any study.
- Any `<script>`, `<form>`, `<input>`, `<button>`, `<iframe>`, `<img>`, `<svg>`, `<table>`, or
  any remote resource.

---

## Layout

- Frame **1320px**, insets `clamp(22px, 3.6vw, 58px)`.
- Breakpoints **1100 / 980 / 860 / 560**; nothing overflows at 320.
- Radius **6px** on fields, bands and panels; **2px** on controls and chips. This supersedes the
  10–28px radius seen in older scaffolds.
- **Never put a `border` and a `max-width` on the same element** — the rule belongs to the
  section, the measure to the text. Where the bordered element is the paragraph, use
  `padding-right`.
- Structure by rules and bands, not by cards.
- One action per composition, thin-bordered or underlined. No heavy fills.

---

## Copy bands

| Role | Words |
| --- | ---: |
| Hero, CTA, breadcrumb | 40–90 |
| Standard section | 90–170 |
| Structured section, detail page | 170–230 |
| **Absolute ceiling** | **250** |

Numerals in visible copy are **spelled as words**. Digits appear only inside a reserved field's
ratio label.

`<h1>` appears only in **S01, S21, S23, S24, S25, S26, S27** — the hero, the subpage hero and the
five detail pages. Every other section's title is an `<h2>`.

---

## Page Rhythm

Every section is one of three shapes, read across the assembled page.

| Shape | Meaning |
| --- | --- |
| **A** | Item grid, media in every item, five to eight reserved areas |
| **B** | Anchored, one to three reserved areas |
| **C** | Type and colour, no reserved area |

1. Never more than two consecutive `A` sections at one variant.
2. Every assembled page needs at least one `C`.
3. A section is not entitled to media because it could have some.
4. A `C` records why it carries none.
5. Read the two sections above at the same variant before authoring.

A batch whose five shapes exactly repeat a previous batch's row is a flatness signal, not a rule
violation; break it when the content allows.

---

## The checker

`autocheck.ps1` enforces the shell and dependency list (no script, svg, form, iframe, img, table,
header, nav, footer or remote reference), the radius ceiling, the banned-decoration list, the
automotive claims vocabulary, the digit rule, the `border`-plus-`max-width` rule, the `h1` rule,
the theme tokens and content parity across the five studies of a section.

`-AllowClaims '<pipe|separated|terms>'` and `-AllowDigits '<terms>'` are **string** parameters
carrying an allow list, not switches. A section that names a forbidden word **in order to refuse
it** is allowed that word, and the allowance is recorded in that section's batch document.

---

## Completion record — 24 September 2026

All **27 sections, 135 studies** are authored in the detailing pass and verified by measurement.

### What each section carries

Every section has a `BATCH-V2.md`. **S01 and S02** had V1 studies and were re-authored from that
content spine. **S03–S27** had none: their content and design were authored together in one pass,
their records say so explicitly, and no fictional V1 stage was written for them.

| | Sections | Studies |
| --- | --- | ---: |
| Re-authored from a V1 spine | S01–S02 | 10 |
| Authored directly in the V2 register | S03–S27 | 125 |

### Verified, not asserted

- `autocheck.ps1` over all 27 sections — **27/27 ALL CHECKS PASS**.
- 135/135 studies carry the `V2-detailing` batch token.
- `<h1>` appears only in **S01, S21, S23, S24, S25, S26, S27**.
- No `<script>`, `<svg>`, `<iframe>`, `<img>`, `<form>`, `<input>`, `<button>`, `<table>`,
  `<details>`, `<header>`, `<nav>` outside the S22 breadcrumb, or `<footer>` in any study.
- No remote reference of any kind: no `http://`, no `https://`, no `@import`, no `data:image`,
  no `tel:` and no `mailto:`.
- No gradient, shadow, dashed border, pill or `background-image`; radius ceiling 6px on fields,
  bands and panels, 2px on controls and chips.
- No alarm red anywhere.
- **Not one manufacturer, wordmark, badge, model name, number plate or registration** appears in
  any of the 135 studies.
- No price, payment, rate, deposit, total, mileage, performance figure, rating, star, review
  count, award or urgency device.
- No digit in visible copy outside the reserved-field ratio labels. Every numeral in prose is
  spelled as a word.

### One legitimate checker allowance

| Section | Allowance | Why |
| --- | --- | --- |
| S06 Financing | `deposit` | the word appears only inside the reserved field *[Approved deposit, after a check]* and inside the refusal that says no deposit is printed |

S22 additionally needs `-AllowNav`, because the breadcrumb itself is the `nav` landmark.

**A trap worth recording:** `-AllowClaims` and `-AllowDigits` are `[string]` parameters taking a
pipe-separated allow list, not switches. Passing them bare, or as `$true`, sets the value to
`True`, matches nothing, and the section still fails. Pass the actual terms.

One word was **reworded rather than allowed**: S18's sixth answer read *nobody will hurry you out
of it*, and `hurry` is on the claims list as an urgency device. It is now *nobody moves you out of
it*, and the checker is clean without an exception.

### Where the copy bands did not fit the role

**S21** (31–39 words) and **S22** (23–43) sit under the contract's 40–90 hero and breadcrumb band.
Both are template roles whose page-specific values are all reserved; the only way to reach forty
would be filler or an invented hierarchy. Each record states this.

### The one sentence added to a V1 spine

**S01** and **S02** carry V1's copy word for word, plus one added block each: the contract requires
a stated limit on every page and V1 had none. A refusal removes a claim rather than making one,
which is why it is the only addition the pass allowed itself. Both additions are recorded in
their batch documents.
