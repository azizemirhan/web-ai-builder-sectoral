# BATCH V1

## Batch Identity

- Sector: `Consulting & B2B Professional Services`
- Prefix: `CONS`
- Section ID: `CONS-S06`
- Section Name: `Experts & Leadership`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

Sixth batch in the `CONS` sector. Themes unchanged from `S01`–`S05`. Shapes chosen against the five
sections above it before drafting.

## Planned Studies

| Study ID | Direction | Theme | Shape | Composition | Media | Words |
| --- | --- | --- | :---: | --- | ---: | ---: |
| `CONS-S06-001` | Universal / Safe | 001 Paper | **A** | Five portrait cards on a three-then-two grid, commitment chip closing each | 5 | 190 |
| `CONS-S06-002` | Premium / Editorial | 002 Sable | **C** | No photographs at all — a saturated argument block and five typographic people blocks | **0** | 183 |
| `CONS-S06-003` | Structured / Visual Modular | 003 Field | **B** | One tall lead portrait card, four compact roster modules beside it | 1 | 174 |
| `CONS-S06-004` | Conversion-led | 004 Signal | **A** | Five portrait cards, each closing on a five-block stage strip | 5 | 204 |
| `CONS-S06-005` | Art-directed / Distinctive | 005 Midnight | **A** | Five credit rows — circular portraits, names at display size | 5 | 182 |

## The Section Role

Who actually works on the engagement — the third of the sector's four questions.

## The Governing Constraint — A Headshot Answers A Question Nobody Asked

Every consulting leadership section is a grid of faces and job titles. It is not that the format is
tired; it is that **it answers the wrong question.** The anxiety behind this section is the oldest
complaint about this industry:

> **Will the person in the pitch be the person on the work?**
> Senior partners sell; juniors deliver. A photograph cannot answer that. Only a commitment can.

So every study makes the commitment a first-class field, and the commitment states **where each
person is not**:

| Role | In the room for | On your engagement |
| --- | --- | --- |
| Managing partner | The decision itself, and the argument with your board | **Stages 01 and 04. Not the middle.** |
| Partner, operating model | Whether the decision survives the organisation | All five stages, named in the contract |
| Director, quantitative | The model, and every assumption inside it | Stages 02 and 03, full time |
| Director, research | The interviews, and what the market actually said | Stage 02, and the readout |
| Principal, delivery | The first ninety days after you decide | Stage 05, and only if you buy it |

The managing partner's line is the one that makes the rest believable. Every other firm implies its
most senior name is on everything; saying **"not the middle"** is the only version of that claim a
buyer can check.

The stages referenced are the five from `CONS-S05`, so the two sections read as one argument when
stacked.

## Names, Portraits, And Where The Line Sits

This section forced a decision the catalog had avoided, now recorded under *The firm's own people*
in `../CONSULTING-THEME-CONTRACT.md`:

- **The firm's own team may carry placeholder names.** A leadership section reserved down to dashes
  is unusable, and a placeholder surname marked `data-placeholder="true"` clears in one pass. The
  form used is an initial and a surname — `A. Whitfield` — so it reads as a placeholder.
- **Third-party people may not.** Named clients, testimonial attributions, quoted analysts and
  referees stay forbidden. The difference is who the invention is about.
- **The portrait stays reserved.** A name can be placeheld; a face cannot. Every portrait slot label
  names the **role**, never the placeholder person, so no study presents a fabricated individual as
  a real one.

## Notes Per Study

**`001`** — the honest default. This is one of the few sections where shape A is the right answer
rather than the lazy one: the subject really is people, and a face is a photograph of something that
exists. Each card closes on the commitment as a filled accent chip.

**`002`** — **a leadership section with no faces, on purpose.** The editorial direction exists to
ask whether the obvious answer is right, and here it is not: removing the photographs leaves the
commitments as the only thing on the page, which is the argument stated as a layout. It also gives
variant 002 its shape-C section.

**`003`** — one portrait, not five. The module system's job is hierarchy, and the hierarchy here is
real: one person runs the engagement and four support it. Giving the photograph to the lead says
which is which without a label saying so.

**`004`** — **the stage strip**, and the strongest device in the batch. Five blocks numbered 01–05,
filled for the stages that person is on. A buyer reads an entire staffing plan in two seconds,
including the part firms leave vague. It converts because it is falsifiable: any firm will say its
partners stay close to the work, almost none will publish a strip with gaps in it.
It is **not a chart** — no percentage, no score, no scale. A block is on or off, the strip is
`aria-hidden`, and the sentence beneath every strip says the same thing in words.

**`005`** — a credits sequence. In most team sections the face is large and the name is small; this
reverses it — one person per full-width line, the name at display size, the photograph reduced to a
circle beside it. The only round media in the catalog.

## Page Rhythm

| Variant | S01 | S02 | S03 | S04 | S05 | S06 | Sequence |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | --- |
| 001 | B | A | C | B | A | **A** | `B A C B A A` |
| 002 | B | A | A | C | B | **C** | `B A A C B C` |
| 003 | B | C | B | B | A | **B** | `B C B B A B` |
| 004 | B | A | A | C | B | **A** | `B A A C B A` |
| 005 | B | A | A | B | C | **A** | `B A A B C A` |

Every variant carries a shape C, and no variant runs three shape-A sections in sequence. At variants
001, 004 and 005 this section is A and follows a B, which is why two consecutive A only occurs once
and at the foot of the run.

## Research Metadata

- Sources: no reference images supplied. Composed against *Composition Devices*, *Page Rhythm* and
  the structured text budget in `../CONSULTING-THEME-CONTRACT.md`.
- Research date: 2026-09-07.
- Differentiation notes: no two studies share a composition, and none repeats a device from
  `S02`–`S05`. The stage strip and the circular portrait are both new to the catalog.
- Visual-first check: 16 reserved portrait areas across five studies — 5, 0, 1, 5, 5.
- Document-metaphor justification: `NONE`. Verified mechanically. This mattered most in `002` and
  `005`, where a five-person sequence in one column is one hairline away from a staff register.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE · JavaScript: NONE.

## Media Slots

| Study | Slots | Shape | Label names |
| --- | ---: | --- | --- |
| `001` | 5 | 4:5 and 16:10 | The role |
| `002` | 0 | — | See *Notes Per Study* |
| `003` | 1 | 4:5, lead card only | The role |
| `004` | 5 | 4:5 and 16:10 | The role |
| `005` | 5 | 1:1 circular | The role |

Empty reserved media areas are intended output, not defects.

## Placeholder Demo Data

Person names, all marked `data-placeholder="true"` and declared in each study's meta block:
`A. Whitfield`, `R. Okonjo`, `M. Lindqvist`, `S. Bhatt`, `J. Ferreira`.

Roles, commitments and stage assignments are **not** placeholder data — they are policy statements a
firm can honour. Still excluded sector-wide: named clients, testimonial attributions, rankings,
awards, certifications, qualifications, universities, prior employers, and any percentage asserting
a measurement nobody ran.

## QA

- ID validation: PASS — five IDs matching filenames and `<meta name="study-id">`.
- Raw-format validation: PASS — standalone HTML, scoped CSS, tag balance verified on all five.
- Dependency check: PASS — no framework, CDN, remote dependency or script.
- Text budget: PASS — 174 to 204 visible words against the structured band of 170–230. `005` was
  drafted at 157 and extended back into band.
- Theme conformance: PASS — ground, ink and accent identical to the matching `CONS-S01` study for
  all five variants.
- Document-idiom scan: PASS — 0 ruled row lists, 0 right-aligned label columns, 0 monospace,
  0 tables.
- Page-rhythm check: PASS — every variant carries a C, no three consecutive A.
- Placeholder declaration: PASS — 30 marked instances across the batch; every study carrying a name
  declares `<meta name="placeholder-data">`.
- Fabricated-person check: PASS — no portrait slot label repeats a placeholder name; every slot
  names a role.
- Section-shell rule: PASS — no global header, navigation or footer in any study.
- Render check: PASS — all five rendered in headless Chrome; `004` and `005` inspected in full. No
  defects found.
- Accessibility QA: NOT_RUN — heading order, focus ring and reduced-motion blocks are in place, cards
  are real links, and the stage strip in `004` is `aria-hidden` with a text equivalent beneath it.
  No full checklist pass has been run.
- Responsive QA: NOT_RUN — ladders authored at `980px`, `860px` and `560px`; verified by code review
  only. `review/build-index.py` cannot run on this machine because Python is not installed.
