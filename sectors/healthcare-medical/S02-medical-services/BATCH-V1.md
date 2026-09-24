# BATCH V1

## Batch Identity

- Sector: `Healthcare & Medical Clinics`
- Prefix: `HC`
- Section ID: `HC-S02`
- Section Name: `Medical Services`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Direction | Theme | Shape | Composition | Areas | Words |
| --- | --- | --- | :---: | --- | ---: | ---: |
| `HC-S02-001` | Universal / Safe | 001 Linen & Sage | B | Six areas as a two-column list beside the consulting room; the not-seen line and the route beneath | 1 | 155 |
| `HC-S02-002` | Premium / Editorial | 002 Porcelain & Plum | **C** | **Six symptom lines at display size**, the area name small beside each, ruled; a quiet foot | 0 | 145 |
| `HC-S02-003` | Structured / Visual Modular | 003 Sky & Slate | **A** | **Six cards pairing each area with the room it happens in**, the reasons people come and the first visit | 6 | ~215 |
| `HC-S02-004` | Conversion-led | 004 Sand & Terracotta | B | **The route for anyone unsure leads in an accent panel**, areas beside it, reception beneath | 1 | 154 |
| `HC-S02-005` | Art-directed / Distinctive | 005 Night & Mint | **C** | **Dark index in two half-step staggered columns**, mint numerals, one stark not-seen line | 0 | 145 |

Row `B C A B C`. `S01` is `B` at every variant, so `A` was free everywhere and taken once; page two
and page five each receive a `C`.

## The Governing Idea

> **Start from what is wrong, not from a list of departments.**

A services section is normally the clinic's org chart — Dermatology, Rheumatology, Cardiology —
which asks a worried person to translate a symptom into a specialty before they can find the door.
This batch is written the other way round: six areas in neutral category vocabulary (*skin;
joints, bones and muscles; heart and circulation; women's health; children; checks and
screening*), each opening with the reasons people actually come, in the words they would use.

**"Not seen here" is in the section.** `S01` promised *the right person first — if we do not see
it here, you are told before you book, and where to go.* A services index that only lists what it
does would break that promise on the next screen, so every study ends with *emergencies are not
seen here — use the emergency service — anything else we do not see, you are told where to go
instead*, and a route for anyone unsure: *tell us what is wrong.*

## Why `003` Takes An `A`

Contract rule 3: a section is not entitled to media because it could have some. This one is
entitled because the six areas happen in six different places, and *where does this happen* is
the question a first visitor asks after *is this the right place*. Each frame is the room or the
equipment the text names — the examination couch, the physiotherapy room, the monitor, the
consulting room, the children's corner, the nurse's room — the first and third honest subjects of
the contract, never a stock picture of a body part.

## The Two `C`s

- `002`: the symptom lines are the object, set at display size with the department as small print
  — the inversion of every services page in the sector. A photograph would compete with them for
  nothing.
- `005`: the hero above it at variant five is a full-height photograph of the doctor at work; a
  second photograph beneath it would be the page saying the same thing twice.

## Verification Record

- Word band `90–170` standard; `003` declared structured `170–230`. All five in band after two
  trims: `003` first came in at 257 words and lost its *First visit:* prefixes, four long slot
  labels and a redundant clause in its lead.
- Content parity: **10 shared fields across five studies, 50/50 slots present.**
- Reserved areas: **1 / 0 / 6 / 1 / 0.**
- Claims scan clean; no digit in any body text; no clinician, credential, outcome, price, insurer,
  telephone, emergency number or opening hour. Category names are neutral areas, never a diagnosis
  with a promise attached.
- Dependencies none; tag balance, namespace, frame, reduced-motion, `<h2>` labelling, no
  solid-border-plus-max-width: all pass.
- Rendered and read at 1440 and 390. Three corrections: a `2.6px` typo in `002`'s foot padding
  (meant `2.6vw`); `003`'s sixth card carried a two-line closing sentence that lifted its shared
  rule off the row's baseline — the reserved-row rule from the dental sector — so all six closing
  lines were cut to one line; and `005`'s stagger only held for the first row because a
  `margin-top` on one item offsets one row, not a column. It is now built with explicit
  `grid-area` placement in which every entry spans two half-rows and the right column starts one
  half-row down, which is a true zigzag at every row.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.
