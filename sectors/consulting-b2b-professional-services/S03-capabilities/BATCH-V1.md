# BATCH V1

## Batch Identity

- Sector: `Consulting & B2B Professional Services`
- Prefix: `CONS`
- Section ID: `CONS-S03`
- Section Name: `Capabilities`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

Third batch in the `CONS` sector. Themes unchanged from `CONS-S01` and `CONS-S02`; authored directly
against *Composition Devices* in `../CONSULTING-THEME-CONTRACT.md`, which was written after the
`S02` rework and is what this batch was designed to satisfy from the first draft rather than the
second.

## Planned Studies

| Study ID | Direction | Theme | Composition device | Status |
| --- | --- | --- | --- | --- |
| `CONS-S03-001` | Universal / Safe | 001 Paper | Three alternating feature bands, media side flipping | AUTHORED |
| `CONS-S03-002` | Premium / Editorial | 002 Sable | Six horizontal magazine cards on two columns | AUTHORED |
| `CONS-S03-003` | Structured / Visual Modular | 003 Field | Full-height media column beside a two-by-three card grid | AUTHORED |
| `CONS-S03-004` | Conversion-led | 004 Signal | Media band with an overlapping claim card, cards closing in tinted limit strips | AUTHORED |
| `CONS-S03-005` | Art-directed / Distinctive | 005 Midnight | Cards that are their media, with the text set over a scrim | AUTHORED |

No device is reused from `CONS-S02`, which used a flat card grid, a snap slider, a mixed-size module
system, a featured card, and an offset gallery.

## The Section Role

What has to be true **inside the firm** for anything in `S02` to be deliverable.

    A service is a promise. A capability is what makes the promise keepable.

## The Governing Constraint — Everybody Claims The Same Six

This is the emptiest section on most consulting websites, and the reason is structural rather than
stylistic: **every firm claims the same capabilities, and none of the claims costs anything to
make.** *Data and analytics. Change management. Benchmarking.* A reader learns nothing, because
nothing on the list could have been left off.

So this batch makes one move, and all five studies make it:

> **A capability is stated with the edge it stops at.**
> A limit is the only part of a capability list a competitor cannot copy without also accepting it,
> and it is the part a serious buyer actually reads.

Each entry carries the name, what it actually is, and where it stops:

| Capability | What it is | Where it stops |
| --- | --- | --- |
| Quantitative modelling | The numbers the decision actually rests on | Not a model you cannot maintain once we leave |
| Primary research | Talking to your market rather than reading about it | Named interviews, not a survey panel |
| Organisation design | Structure, roles, and who decides what | We will not name individuals for the roles |
| Commercial analysis | Margin, mix, and what your contracts actually cost | We do not set your prices |
| Programme direction | Running it after the decision is made | We advise it or we run it, not both |
| Facilitation | Getting a divided board to one answer | We will not manufacture agreement you do not have |

**The limits are policy commitments a firm can honour, not statements about past performance**, so
none of them is a fabricated metric. That distinction is what makes this device usable in a catalog
that forbids invented proof.

The same six appear in all five studies, as with the situations in `S02` and the counters in `S01`:
holding the content constant means a reviewer sees only the design difference.

## Notes Per Study

**`001`** — three alternating bands, each pairing one feature-scale image with two capabilities; the
media side flips on every band so the eye zig-zags rather than scanning a column. Limits are set as
tinted pills. Deliberately not the card grid used at `S02-001` — same theme, different composition,
which is exactly what the theme contract asks a section to vary.

**`002`** — six horizontal magazine cards, image held left inside each. **This study drops the "what
it is" line on purpose.** The section's argument is that the limit is what makes a capability
credible, and the editorial direction earns its place by removing everything that is not the
argument. Lowest density in the batch, as `002` should be.

**`003`** — one reserved image at *column* scale running the full height of the card grid, rather
than media inside cards. Media as a structural element is what makes the study modular rather than
a grid of six. Still no matrix: the grid is a layout, a card's row and column assert nothing, and
the cards could be reordered without changing a claim.

**`004`** — a wide media band with a saturated claim card overlapping its lower edge, then six cards
each closing in a tinted limit strip that fills on hover. The conversion argument is that the limits
*are* the proof, so they are given the loudest element on each card rather than a footnote.

**`005`** — the cards **are** the media: name and limit sit over the image inside a fixed gradient
scrim. Every other study separates picture from words; this one does not, and that is the distinction
it claims. The scrim is a gradient rather than a translucent block so the type stays legible whatever
photograph eventually lands underneath — the condition an empty reserved area has to satisfy to be
honest about what it is reserving.

## Research Metadata

- Sources: no reference images supplied for this section. Composed against *Composition Devices* in
  `../CONSULTING-THEME-CONTRACT.md`.
- Research date: 2026-09-07.
- Differentiation notes: no two studies share a device, and no device is carried over from `S02`.
- Visual-first check: 23 reserved image areas across five studies against 95–157 visible words.
- Document-metaphor justification: `NONE`. Verified mechanically — zero ruled row lists, zero
  right-aligned metadata columns, zero monospace, zero tables.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript: NONE — all five studies are static.

## Media Slots

| Study | Slots | Shape | Intended subject |
| --- | ---: | --- | --- |
| `001` | 3 | 4:3, feature scale | The capability in use — the work, not a meeting about the work |
| `002` | 6 | 1:1 inside each card | As above, one per capability |
| `003` | 1 | Full-height column | As above, at structural scale |
| `004` | 7 | 21:9 band plus 6 at 16:9 | As above, with the band carrying the overlap |
| `005` | 6 | 3:4, filling each card | As above, with type set over it |

Empty reserved media areas are intended output, not defects. Card-level labels are kept to
`Image area` because six long labels would themselves become the text problem this batch avoids; the
intended subject is recorded here.

## Placeholder Demo Data

**None in this section.** A capabilities section has no counter role, and no figures were introduced
merely to have something to fill. Named clients and logos, awards, rankings, certifications, tool
vendors, and any percentage or multiple asserting a measurement nobody ran remain excluded.

## QA

- ID validation: PASS — five IDs matching filenames and `<meta name="study-id">`.
- Raw-format validation: PASS — standalone HTML, scoped CSS, tag balance verified on all five.
- Dependency check: PASS — no framework, CDN, remote dependency or script.
- Text budget: PASS — 95 to 157 visible words against the content-section band of 90–170.
- Theme conformance: PASS — ground, ink and accent verified identical to the matching `CONS-S01`
  study for all five variants.
- Document-idiom scan: PASS — 0 ruled row lists, 0 right-aligned label columns, 0 monospace,
  0 tables.
- Device-reuse check: PASS — no composition device shared with `CONS-S02`.
- Section-shell rule: PASS — no global header, navigation or footer in any study.
- Render check: PASS — all five rendered in headless Chrome; `001`, `004` and `005` inspected in
  full. No defects found.
- Accessibility QA: NOT_RUN — heading order, focus ring and reduced-motion blocks are in place and
  cards are real links, but no full checklist pass has been run. The scrim contrast in `005` should
  be re-checked once real photography is placed behind it.
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

`CONS-S03-001` moved from its previous shape to **C — type and colour**, rebuilt from three alternating media bands into three colour bands, the middle one filled in the accent — the rhythm that was carried by alternating photographs is now carried by colour.


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
