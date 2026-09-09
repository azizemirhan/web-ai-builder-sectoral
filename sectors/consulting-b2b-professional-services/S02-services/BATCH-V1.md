# BATCH V1

## Batch Identity

- Sector: `Consulting & B2B Professional Services`
- Prefix: `CONS`
- Section ID: `CONS-S02`
- Section Name: `Services`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`
- Revision: `V2` — all five studies rebuilt after review. See *V1 Was Rejected* below.

Second batch in the `CONS` sector. Themes are unchanged from `CONS-S01`, which is the point of
`../CONSULTING-THEME-CONTRACT.md` — variant N of this section assembles with variant N of the hero
into one website.

## Planned Studies

| Study ID | Authoring Direction | Theme | Composition | Status |
| --- | --- | --- | --- | --- |
| `CONS-S02-001` | Universal / Safe | 001 Paper | Six media cards on a three-column grid | AUTHORED |
| `CONS-S02-002` | Premium / Editorial | 002 Sable | Editorial statement and a horizontal snap slider of tall media cards | AUTHORED |
| `CONS-S02-003` | Structured / Visual Modular | 003 Field | Mixed-size card modules, one wide media card, one saturated live module | AUTHORED |
| `CONS-S02-004` | Conversion-led | 004 Signal | Featured card with a large image and the entry action, five compact cards, closing panel | AUTHORED |
| `CONS-S02-005` | Art-directed / Distinctive | 005 Midnight | Offset two-column image gallery on a near-black field | AUTHORED |

## V1 Was Rejected, And Why It Matters

The first version of this batch was reviewed and rejected as **technical-looking**. The finding was
precise and it was not about colour:

> V1 built four of the five studies out of **full-width ruled rows** — a numeral gutter on the left,
> the text in the middle, a right-aligned uppercase label column on the right, and a hairline between
> every row. **That is a table.** It is the same document idiom this workspace already ruled out for
> `ARC` under the names *register*, *ledger*, *schedule* and *index*, reproduced here under the name
> "editorial". `CONS-S02-002`'s own `layout-model` metadata literally read *typographic index*.

The second finding was the more useful one:

> **None of the cards contained an image.** Every supplied reference builds its content sections out
> of cards or slides that carry photography — a three-up card row, a four-card numbered set, a
> horizontal slider of image cards, an offset image gallery. V1 put text in a box and called it a
> card. A card without media is a table cell with rounded corners.

Both findings are now written into `../CONSULTING-THEME-CONTRACT.md` under *Composition Devices*, as
a positive list rather than only a prohibition, because a prohibition alone is what allowed the same
mistake to be made twice.

### What changed between V1 and V2

| | V1 | V2 |
| --- | --- | --- |
| Dominant device | Ruled rows with a metadata column | Cards, a slider and a gallery |
| Reserved image areas in the batch | 4 | **25** |
| Studies with media in every item | 0 | 3 (`001`, `004`, `005`) |
| Hairline row rules | 24 | 0 |
| Right-aligned label columns | 3 | 0 |

Content did not change. The six situations, the governing idea and the word budget are identical;
only the form was rebuilt. That is deliberate — it isolates what was actually wrong.

## The Section Role

What the firm sells, and — the part that decides whether the section works — **whether the reader can
find themselves in it.** This section answers the first of the sector's four questions: *do you
understand my problem?*

## The Governing Constraint — A Capability List Is Not A Services Section

    A capability list tells the buyer what the firm sells.
    A situation list tells them whether the firm has met their problem.

The default consulting services section is six nouns — *Digital Transformation*, *Operational
Excellence*, *Growth Strategy* — and it fails because **it asks the buyer to translate their problem
into the firm's vocabulary before they are allowed to proceed.** They cannot do that reliably, so
they pick wrong or leave.

So every study makes the situation the card title and demotes the discipline to a pill or a small
label:

| Situation | Discipline |
| --- | --- |
| The market moved and the plan did not. | Strategy and positioning |
| The strategy is agreed and nothing has changed. | Operating model |
| It costs more to run than it should. | Performance and cost |
| Growth stalled and the reasons contradict each other. | Growth and commercial |
| The programme is late and reporting says it is fine. | Transformation delivery |
| A decision is coming and the evidence is thin. | Diligence and decision support |

**The same six appear in all five studies**, matching the approach taken with the counters in `S01`:
holding content constant means a reviewer sees only the design difference.

## Notes Per Study

**`001`** — the safe modern pattern: a three-column card grid where every card carries a 4:3 image,
a discipline pill, the situation as the card title and an arrow affordance. Lifts on hover.

**`002`** — a horizontal snap rail with the next card peeking past the frame edge, which is what
signals a slider without a scrollbar. Cards are 3:4, the tallest per-card media in the batch. This is
the only study in the batch with script: **~10 lines of vanilla JavaScript** step the rail by one
card when the arrows are pressed. Native scroll, touch and trackpad work without it; the arrows exist
because a rail with no visible control reads as a static row.

**`003`** — a module system rather than a flat grid: a wide reserved image card spanning two modules,
six numbered situation cards, one held in the accent as the live module, and a dark CTA module
closing the composition. Still no matrix — the grid is a layout, not a diagram of axes, so a card's
position asserts nothing about it.

**`004`** — one featured card spanning two columns and two rows, carrying a large image, the badge
*Start here*, and the entry action; five compact cards around it; a saturated panel closing the grid
for the reader none of the six fits. A grid of six equal cards asks for six decisions; a featured
card asks for one. The badge is a recommendation the firm can make, deliberately **not** "most
common" or a percentage, which would be a statistic nobody measured.

**`005`** — an offset gallery: two columns of square media cards with the right column dropped by a
fixed amount so pairs never align, which makes the eye travel diagonally instead of in rows. The
offset releases at `860px`, where a stagger would only produce ragged whitespace.

## Research Metadata

- Sources: no reference images supplied for this section. Composed against the modern-web register
  the user set for the workspace — card grids, sliders, featured cards, offset galleries, media in
  every card — read for this sector in `../CONSULTING-THEME-CONTRACT.md`.
- Research date: 2026-09-07. Rebuilt same day after review.
- Differentiation notes: no two studies share a layout or a device. Content is held constant so that
  composition is the only variable.
- Visual-first check: 25 reserved image areas across five studies, against 100–148 visible words.
  Every study is now media-led except `003`, which is module-led by direction.
- Document-metaphor justification: `NONE`. Verified mechanically — zero hairline row rules, zero
  right-aligned metadata columns, zero monospace, zero tables across the batch.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript: `002` only, ~10 lines, vanilla, for the slider arrow controls. Justified above under
  *Notes Per Study*; the rail degrades to native horizontal scroll without it.

## Media Slots

| Study | Slots | Shape | Intended subject |
| --- | ---: | --- | --- |
| `001` | 6 | 4:3 per card | The work each situation produces, one per service |
| `002` | 6 | 3:4 per card | As above, portrait-oriented for the rail |
| `003` | 1 | Wide, two modules | The work itself, not a meeting about the work |
| `004` | 6 | 21:9 featured, 4:3 compact | As above, with size hierarchy marking the entry route |
| `005` | 6 | 1:1 per card | As above, square for the offset gallery |

Empty reserved media areas are intended output, not defects. Slot labels are kept to `Image area` in
the card grids because six long labels would themselves become the text problem this batch exists to
avoid; the intended subject is recorded here instead.

## Placeholder Demo Data

**None in this section.** `S01` carries placeholder counters because a hero has a counter role to
fill; a services section has none, and no figures were introduced merely to have something to fill.

Still excluded, as everywhere in this sector: named clients and logos, awards, rankings,
certifications, and any percentage or multiple asserting a measurement nobody ran.

## QA

- ID validation: PASS — five IDs matching filenames and `<meta name="study-id">`.
- Raw-format validation: PASS — standalone HTML, scoped CSS, tag balance verified on all five.
- Dependency check: PASS — no framework, CDN or remote dependency. One documented inline script.
- Text budget: PASS — 96 to 148 visible words against the content-section band of 90–170.
- Theme conformance: PASS — ground, ink and accent verified identical to the matching `CONS-S01`
  study for all five variants.
- Document-idiom scan: PASS — 0 ruled row lists, 0 right-aligned label columns, 0 monospace, 0
  tables.
- Section-shell rule: PASS — no global header, navigation or footer in any study.
- Render check: PASS — all five rendered in headless Chrome and inspected. Two defects found and
  corrected during the rebuild: the compact card beside the featured card in `004` stretched to the
  featured card's height and left dead space, fixed by spanning the feature across two rows; and the
  `005` cards were sized 4:5, which made the section unnecessarily long, reduced to 1:1.
- Accessibility QA: NOT_RUN — heading order, focus ring and reduced-motion blocks are in place, cards
  are real links and the slider buttons carry `aria-label`, but no full checklist pass has been run.
- Responsive QA: NOT_RUN — ladders authored at `980px`, `860px` and `560px`; verified by code review
  only. `review/build-index.py` cannot run on this machine because Python is not installed.


## V3 — Media Reduction Pass

Reviewed against the assembled page rather than the section, and rejected:

> Not every section should have an image area either.

The count made the case. **Twenty-four of the catalog's twenty-five studies carried a reserved image
area.** Shape C existed in the theme contract as a rule and almost never in practice, because the
rule was written as "at least one C in any run of six" — satisfiable by ignoring it. It is now per
variant: read down a variant's five sections, and if none is C, one of them is wrong.

A second rule was added with it, and it is the one that decides these cases:

> **A section is not entitled to media just because it could have some.** Ask what the photograph is
> *of*. If the honest answer is "something related to this topic", there is no photograph — there is
> a grey rectangle standing in for one, and the section is better built from type and colour.

That test is decisive for abstractions. There is no honest photograph of *quantitative modelling*,
of *financial services*, or of a process stage called *Options*: only an illustration, and an
illustration of an abstraction is a stock photograph — the first thing this sector's anti-patterns
rule out.

### What changed here

`CONS-S02-003` moved from its previous shape to **C — type and colour**, its wide media module removed; the live accent module now spans the two cells it occupied, so the size hierarchy that made this a system rather than a grid is intact.


### Shape distribution after the pass

Across the twenty-five authored `CONS` studies: **A = 9, B = 11, C = 5.** Shape B is now the
plurality, which is what the theme contract says it should be, and every variant's assembled page
carries exactly one shape-C section.

| Variant | S01 | S02 | S03 | S04 | S05 |
| --- | :---: | :---: | :---: | :---: | :---: |
| 001 | B | A | **C** | B | A |
| 002 | B | A | A | **C** | B |
| 003 | B | **C** | B | B | A |
| 004 | B | A | A | **C** | B |
| 005 | B | A | A | B | **C** |
