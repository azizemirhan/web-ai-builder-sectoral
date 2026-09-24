# DENTAL THEME CONTRACT

Sector: `Dental Clinics` · Prefix: `DN` · Written with `DN-S01` and governing all twenty-seven sections.

This file is the sector's register, anti-patterns, media rules, claims limits and five themes. Every
`DN` study is authored against it, and every batch document records where it applies it.

---

## The Sector's Design Problem

Consulting's problem is that judgement has no photograph. Dentistry's is the opposite: **there are
too many photographs, and they are all the same three.**

    A model with teeth that do not occur in nature, laughing.
    A gloved hand holding an instrument near an open mouth.
    An empty white surgery that could be any clinic on earth.

The first is not a patient. The second is a picture of the thing being feared. The third is a picture
of nothing. All three are on almost every dental website, and none of them is evidence of anything.

## The Governing Constraint — Nobody Is Browsing

> **Nobody arrives at a dentist's website in a good mood.**

This is the fact the whole sector designs around wrongly. Dental sites are built as if the visitor
were shopping — comparing, browsing, being tempted. They are not. They are **bracing.** The dominant
emotion is anxiety, and it has three named sources:

| The fear | What the sector does about it | What it should do |
| --- | --- | --- |
| **It will hurt** | Claims *pain-free* and *gentle*, which are unverifiable and in most jurisdictions regulated | Say what happens, and who can stop it |
| **It will cost more than they say** | Advertises *from £X* | Give the whole cost in writing before anything starts |
| **They will judge me for leaving it** | Says nothing at all | **Say it** |

The third is the one nobody addresses and the one that keeps people away for years. A design that
answers it is doing something no competitor is doing, and it costs nothing to be honest about.

---

## Anti-Patterns

Specifically banned as default devices across all twenty-seven sections:

- **The stock smile model.** A person who is not a patient, with teeth that are not real, is the
  single most common image in the sector and it is evidence of nothing.
- **The open mouth.** No study reserves an image of a mouth, teeth in close-up, or a dental chart of
  a jaw. It is the fear image and it belongs in a clinical record, not on a homepage.
- **Instruments near a face.** A drill, a probe or a syringe in frame with a person is the same
  failure with better lighting.
- **The empty white surgery.** A room with nobody in it, shot wide, is a picture of a room that could
  be anywhere.
- **Tooth iconography.** A cartoon molar as a bullet, a logo, or a decorative motif.
- **Aqua and whitening-blue palettes.** The cyan-to-white gradient is the sector's visual default and
  reads as a product claim about tooth colour.
- **Sparkle, shine and gleam effects.** Star glints on teeth, radial gradients behind a smile.
- **Countdown offers on treatment.** Scarcity applied to healthcare.
- **Award badges and star ratings** as a design element.
- **Before/after used as an outcome promise.** See *Claims Limits*.

## The Media Rule

**Ask what the photograph is of.** In this sector three subjects are honest and the rest are not:

| Honest | Why |
| --- | --- |
| **The room the visitor will actually sit in** | It is the room, and they are about to be in it |
| **The people who will actually treat them** | Named by role, mid-work or mid-sentence, never posed against a window |
| **The equipment the text names** | If the copy says a scanner replaces the mould, the scanner is a legitimate subject |

Everything else is a grey rectangle standing in for a photograph. A reserved area's label states
**what the photograph is** and never who is in it, and no label ever describes a mouth.

**Portraits stay reserved.** A name can be placeheld; a face cannot.

---

## Claims Limits

Dental advertising is regulated in most jurisdictions, and the workspace takes a conservative line
rather than a jurisdiction-specific one. These are authoring rules for placeholder studies, not legal
advice; a real clinic's copy must be checked against its own regulator.

**Never written, in any study:**

- **Outcome guarantees.** No *guaranteed results*, *permanent*, *lasts a lifetime*.
- **Comfort claims.** No *pain-free*, *painless*, *completely gentle*. What may be said is what is
  done: an anaesthetic is offered, a signal stops the work, a break is available.
- **Superiority claims.** No *best*, *leading*, *number one*, *award-winning*, *voted*.
- **Fabricated credentials.** Registration numbers, specialist titles, qualifications and memberships
  are verifiable facts about real people. **They are reserved, never invented** — the same rule the
  workspace applies to people everywhere.
- **Fabricated prices.** A price stated must be complete. A study that cannot state a complete price
  states the **policy** instead — *the whole cost in writing before anything starts* — which is a
  commitment rather than a figure.
- **Patient testimonials, ratings or reviews with attribution.** No named patients, no star counts.
- **Before/after images as outcome promises.** `S05` and `S24` are scoped to anonymised treatment
  context. A reserved before/after area, where a study uses one, is labelled as **one case, not a
  typical result**, and never carries a face.

**Permitted placeholder data:** the clinic's own countable and checkable facts — how many surgeries,
how many years open, opening days, whether emergency slots are held back, whether anyone works on
commission. Marked `data-placeholder="true"`.

**The clinic's own people** may carry placeholder names in the form initial-and-surname
(`J. Okafor`). Third-party people — patients, referrers, named specialists elsewhere — may not.
Pronouns are never invented: a placeholder person is *they*.

---

## Composition Devices

The anti-pattern list is the negative half. This is the positive half, and it governs every section.

**Banned as default devices:**

- a hairline rule under every item in a list;
- a right-aligned metadata or label column;
- a numeral gutter used as a table column rather than as a graphic element;
- **text-only boxes presented as cards.** A card without media is a table cell with rounded corners.

**Build with these:**

| Device | What it looks like |
| --- | --- |
| **Card grid** | Three or four up, each card carrying its own image area above a short label and a title |
| **Featured card + compacts** | One item given double width and a large image, the rest compact around it |
| **Horizontal snap rail** | Tall image cards, the next peeking past the frame edge |
| **Offset / staggered gallery** | Two columns of image cards, one dropped so pairs never align |
| **Numbered card set** | 01–06 as graphic numerals, one card held in the accent |
| **Badge over media** | A pill sitting on an image area, marking one item |
| **Pill labels** | Category names as pills, never as tracked uppercase in a side column |
| **Big-numeral stat row** | Figures at display size with a small label beside them, no boxes |
| **Joined modules** | A row sharing one `2px` seam so several parts read as one object |

### The test before a section is finished

1. **Where is the media?** Count the reserved areas, and check each against the media rule above.
2. **Would this survive as a table?** If it could be rewritten as rows and columns without losing
   anything, it *is* a table and must be rebuilt.
3. **Is the hierarchy in the scale, or in the rules?** Separate items by size, ground and space.
4. **Has this skeleton been used at this variant already?** Run
   `node review/check-composition-collisions.js dental-clinics`.

---

## Page Rhythm — The Rule Above The Section

**Variant N of every section stacks into one page**, so a rule that makes each section good can still
make the page bad.

| Shape | What it is | Media |
| --- | --- | --- |
| **A — Item grid** | Cards, tiles or panels, media in every item | 5–8 areas |
| **B — Anchored** | One or two large images anchoring text-led content | 1–3 areas |
| **C — Type and colour** | No reserved media. Scale, colour fields, pills and space | 0 areas |

**Shape B is the default.** A page made only of A is a catalogue; a page made only of C is a document.

1. **Never more than two consecutive sections in shape A** at the same variant.
2. **Every assembled page must contain at least one shape C.**
3. **A section is not entitled to media just because it could have some.**
4. A section authored as C records why in its batch document.
5. When a section is authored, **read the two sections above it at the same variant first.**

---

## Text Budget

| Role | Target visible words |
| --- | --- |
| Hero, CTA, breadcrumb | 40–90 |
| Standard content section | 90–170 |
| **Structured content section** | **170–230** |
| Detail page section (`S23`–`S27`) | 150–230 |
| Absolute ceiling, any study | **250** |

The band measures prose, not completeness. A structured section carrying real fields is authored at
full capacity; **cutting a required field to hit a number is the wrong correction.** A single element
that is a paragraph of prose is over budget whatever the total says.

---

## The Five Themes

Variant = theme, fixed for all twenty-seven sections. The palette deliberately avoids the sector's
aqua-and-white default; no theme uses cyan, and no theme uses red as its accent, because red in a
dental context reads as blood and emergency.

| Variant | Theme | Ground | Ink | Accent | Radius |
| --- | --- | --- | --- | --- | ---: |
| `001` | **Chalk** | `#f6f4f1` | `#16181b` | `#1f6f5c` forest | `16px` |
| `002` | **Linen** | `#f3efe8` | `#1b1714` | `#a2543a` terracotta | `2px` |
| `003` | **Slate** | `#eef0f2` | `#0f1316` | `#2c5fd0` ultramarine | `20px` |
| `004` | **Daylight** | `#ffffff` | `#0a0b0d` | `#e08b2c` amber | `24px`, pills |
| `005` | **Dusk** | `#14161a` | `#f2f1ef` | `#6ea8a0` sea green | `26px` |

Supporting tokens per theme are set in each study and must not drift: `--ink-soft` for secondary text
at AA or better, `--line` for hairlines, `--card` for raised grounds, and `--slot` / `--slot-edge` /
`--slot-ink` for reserved media areas.

### Fixed across all themes

- Frame `max-width: 1320px`; breakpoints at `1100`, `980`, `860` and `560px`.
- A `prefers-reduced-motion` block in every study.
- Scoped CSS namespaced to `.dn-sNN-VVV`. No framework, CDN or remote runtime dependency of any kind.
- No global header, primary navigation or footer — the section-shell rule.
- Secondary text must reach **AA**. A colour that is deliberately quiet is still content.

---

## What Moving Toward Looks Like

Large confident type, generous negative space, warm grounds rather than clinical white, real
photography of rooms and people, one decisive accent, and **a stated commitment rather than a
described feeling.** *Gentle, caring dentistry* is what a clinic says when it has nothing to state.

---

# Detailing Pass — the modern register applied to DN

Status: ACTIVE from 18 September 2026. Governs the V2 re-authoring of all one hundred and
thirty-five `DN` studies. Source: `../../standards/08-VISUAL-REFERENCE-STYLE.md`, read through
the sector's own constraint — *nobody is browsing, they are bracing* — and through the one word
the pass was asked for: **modern**. Everything above this line (the anti-patterns, the media rule,
the claims limits, the placeholder rule, the page rhythm, the text budget) stays in force; the pass
rewrites only the design layer. The V1 content spine of every study is kept whole.

## The DN reading in one sentence

**A calm, modern clinic page: a confident sans display with one word in the accent, bare warm
fields of the room and the people, hairline structure, soft 6px corners, and one thin line of
geometry drawn behind the composition — never a badge, a sparkle, a tooth or a shade of blue.**

Where the reference register's voice is a serif magazine, DN's is a contemporary clinic identity:
the serif is dropped, the sans carries the display, and the softness the sector's language needs is
carried by corner radius on large fields (6px, never more) rather than by pills or shadows.

## What DN translates

| Reference device | DN reading |
| --- | --- |
| Serif display with one italic word | **Sans display**, weight 600, `clamp(2.4rem, 4.6vw, 5rem)`, line-height 0.98, tracking −0.035em, sentence case, **one word or phrase in the accent** (`.ac`), never italic, never bold-inside-bold |
| Statement line | Sans 400, `clamp(1.15rem, 1.8vw, 1.6rem)`, line-height 1.3, ink |
| Item title | Sans 600, 1.05–1.4rem, tracking −0.02em |
| Eyebrow | 0.64rem, 700, 0.2em tracked, accent, with a 24px stroke mark |
| Index numeral | **Word-numeral chip** — ONE … SIX as a bordered 4px chip in the accent, 0.58rem tracked — never a digit, never a giant numeral |
| Hairlines + one 3px accent rule | Kept exactly: `--line` soft, ink strong, one 3px accent bar per composition (the *lead rule*) |
| Tinted band | Paper darkened (`--band`), 6px radius, never a card stack |
| Bare media field | Flat `--media`, 6px radius, slate label bottom-left: `THE ROOM · 4:3`, `IN USE · 21:9`, `THE PERSON · 4:5`, `THE SCANNER · 1:1`, `THE CEILING · 21:9`, `THE DOOR · 3:2`, `WAITING ROOM · 16:9`; never a mouth, never a face |
| Bordered rectangle action | 1px ink border, **4px radius**, uppercase 0.68rem tracked, leading mark; second action an underlined link with `→` |
| Pencil layer (WELL/CON/CONS) | **Geometry layer**, one thin stroke per variant, in the line tone or the accent at low weight — see below |
| `--no` deep red | **`--no` is not red in this sector** (red reads as blood and emergency): the refusal token is a dusk plum, `#5a4a57`, used as an edge, a chip border or a struck-circle stroke — never a surface |

## The geometry layer, by variant

| Variant | Device | Where |
| --- | --- | --- |
| `001` | **Ring** — one thin stroke circle, `clamp(14rem, 26vw, 24rem)`, in the line tone | behind the head, right, clipped by the shell |
| `002` | **Arc** — a quarter-circle stroke in the accent at 1.5px | top-right of the head, `.head > svg.arc` |
| `003` | **Dot grid** — 1px dots on a 32px grid in the line tone, an SVG `<pattern>` | behind the whole composition, `.draw` |
| `004` | **Bar** — a straight 4px accent bar with rounded ends under the key phrase | `.u` + `svg`, inline-block |
| `005` | **Corner marks** — four short L-strokes framing the display column | `.frame` absolute, `.frame > svg` |

One device per study; the device is drawn once. It sits behind text (`z-index: 0`) or on the edge
of a phrase, never across a field.

## DN themes for the detailing pass

The five contract themes are kept by name and accent; the grounds are tuned to the register (warm,
never clinical white floating on white) and **Dusk is inverted** — the register forbids a dark
panel as a page ground, so `005` keeps the sea-green accent on a pale cool paper and the accent is
darkened to reach AA as text.

| Variant | Theme | `--paper` | `--ink` | `--muted` | `--line` | `--media` | `--band` | `--accent` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `001` | Chalk | `#f6f4f1` | `#16181b` | `#5b5f64` | `#dcd9d3` | `#e7e4de` | `#eeece7` | `#1f6f5c` forest |
| `002` | Linen | `#f3efe8` | `#1b1714` | `#68625a` | `#dad2c6` | `#e6dfd4` | `#ebe5da` | `#a2543a` terracotta |
| `003` | Slate | `#eef0f2` | `#0f1316` | `#535b63` | `#d2d7dc` | `#dfe3e7` | `#e6e9ec` | `#2c5fd0` ultramarine |
| `004` | Daylight | `#fdfdfc` | `#0a0b0d` | `#565a5f` | `#e3e3e0` | `#ededea` | `#f3f3f0` | `#c9781f` amber (darkened from `#e08b2c` for AA) |
| `005` | Dusk, inverted | `#eef2f1` | `#14161a` | `#55605d` | `#d1dad7` | `#dfe6e3` | `#e6ebe9` | `#2f7a70` sea green (darkened from `#6ea8a0` for AA) |

`--no: #5a4a57` on every theme. `--line-strong` is the ink. The sans is the system stack; no
serif anywhere in DN; no web font.

## Sector rules that remain in force

The anti-pattern list above, unchanged: no stock smile, no open mouth, no instrument near a face,
no empty surgery shot wide, **no tooth iconography** (no molar mark, ever), no aqua or cyan, no
sparkle, no countdown, no award badge or star rating, no before/after as an outcome promise.
The claims limits: no *pain-free* / *painless* / *gentle*, no guarantee / permanent / lifetime,
no *best* / *leading* / *number one* / *award-winning* / *voted*, no fabricated credential or
price, no attributed testimonial or rating. Placeholder demo values stay marked
`data-placeholder="true"` and declared in a `placeholder-data` meta; **no digit appears in visible
copy outside a placeholder element** (word-numerals elsewhere). Portraits stay reserved and are
labelled by role. Pronouns are never invented.

## The checker

`dncheck.ps1` — theme tokens per variant, the `.dn-sNN-vvv` namespace, `batch = V2-detailing`,
`data-study-id`, reduced-motion, no script / iframe / img / remote URL / form / header / nav /
footer (form and nav allowed only where the role carries them), balanced tags, inline SVG only with
`aria-hidden`, radius ≤ 8px, no gradient / shadow / dashed / pill, no solid border with max-width on
one rule, the dental claims vocabulary, the digit rule, one `<h1>` on hero-like and detail pages
only, and field parity across the five studies.

## Completion record — 21 September 2026

The detailing pass is applied to all one hundred and thirty-five `DN` studies, S01 through S27.
Every section carries a `BATCH-V2.md` design record beside its `BATCH-V1.md`; every study passes
`dncheck.ps1` (tokens, namespace, flat register, inline-SVG-only, reduced-motion rule, shell rule,
h1 rule, digit and dental claims vocabulary, placeholder declaration, field parity) and was rendered
and read at 1440. The only parity gaps recorded are V1's own wordings, listed per section.

What the pass settled beyond the tables above, and what the next sector should inherit:

- **The geometry layer is assigned by variant, not by section**: `001` the hairline ring behind
  the head, `002` the accent arc above the display line, `003` the dot grid drawn once behind the
  whole composition, `004` the 4px bar under the phrase that carries the ask, `005` the corner
  marks framing the display column. S22 puts the lead mark, the bar and the corner marks on five
  words and omits the ring, the arc and the grid, because a breadcrumb cannot carry them.
- **Word-numerals, never digits, outside a placeholder.** V1's `01 … 06` frames (S17) and every
  step or reason index became *One … Six* as chips, keys or tracked labels; demo counts stay digits
  only inside `data-placeholder` elements. `3D` in S06 is the one allowed digit token, recorded.
- **`--no` (dusk plum, `#5a4a57`) carries every refusal in the sector, and nothing is red**: the
  irreversible side (S03), the not-registered chip (S04), the does-not line (S06), *go somewhere
  else if* (S08), *it cannot tell you* (S09), *cannot be quoted until somebody looks* (S10), the
  slowest route (S11), *hospital, not us* (S12), the letters line (S13), the room you will not be
  in (S14), *three we cannot answer* (S15), the insurer's side (S16), every part that fails (S17),
  whitening and the monthly post (S18), *nothing has been sent* (S19), the pending chips and
  disclaimers (S24–S27). It is a rule, an edge, a chip border or a struck-circle stroke — never a
  surface behind body text, never a second accent.
- **Fields are bare, soft-cornered (6px) and labelled by what they are**, never by who is in them:
  THE ROOM, THE DESK, THE CEILING, THE CLINICIAN · IN CONVERSATION, THE STERILISATION ROOM, THE
  BRUSH SIZES · ACTUAL SIZE, LOCATION MAP · VERIFIED LOCATION PENDING. Ratios are stated in the
  label and chosen so a field never outruns its caption column (3:1 strips, 3:2 and 4:3 panels,
  4:5 portraits, 21:9 edge to edge, 1:1 objects); the sixth room in S14-005 has no field because
  it has no vantage.
- **The one ask is a bordered rectangle with a leading mark, never a filled button**: 1px ink
  border, 4px radius, 0.68rem tracked uppercase, the calendar or speech mark before it; the
  secondary is an underlined line with the arrow. S19's form keeps V1's fields, drops the script
  and says *Nothing has been sent* on the plum edge; V1's `<details>` disclosures open as chips
  and ruled rows everywhere, because the register folds nothing.
- **Detail pages S23–S27 keep V1's `<h1>` as the page title** (the bracketed name, location or
  article title), printed in muted ink where it is a placeholder; the checker's hero list covers
  S01, S21 and S23–S27 for that reason. Variant N of S21–S27 routes to variant N of S02, S04,
  S11, S17, S18, S19 and S23, so the pages assemble into one site.
- **Three claims tokens are allowed by exception and recorded**: ` best` in S05 where V1 admits
  *the best of a year*, `award` in S26 where V1's placeholder reads *awarding institutions*, and
  the digit token `3D` in S06.
