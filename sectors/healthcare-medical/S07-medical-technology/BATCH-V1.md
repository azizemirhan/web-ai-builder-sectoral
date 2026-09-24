# BATCH V1

## Batch Identity

- Sector: `Healthcare & Medical Clinics`
- Prefix: `HC`
- Section ID: `HC-S07`
- Section Name: `Medical Technology`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Direction | Theme | Shape | Composition | Areas | Words |
| --- | --- | --- | :---: | --- | ---: | ---: |
| `HC-S07-001` | Universal / Safe | 001 Linen & Sage | B | **The ultrasound room, in use** at column height beside six equipment cards, each with what it answers and its *not for* line; foot with the rule and the action | 1 | 201 |
| `HC-S07-002` | Premium / Editorial | 002 Porcelain & Plum | B | Ruled head; six pieces as a ruled serif column with the limit in italic plum, **a tall frame of the heart trace being taken** on the right | 1 | 207 |
| `HC-S07-003` | Structured / Visual Modular | 003 Sky & Slate | **A** | **Six equipment modules three-by-two, each with a frame of the machine in its room** and the same two labelled fields — *answers* / *not for* | 6 | 229 |
| `HC-S07-004` | Conversion-led | 004 Sand & Terracotta | B | **A terracotta panel with the question to bring — *what would this test change?*** — beside the six pieces as a two-column list; a wide frame of **the take-home monitor being fitted** with the not-held line beside it | 1 | 224 |
| `HC-S07-005` | Art-directed / Distinctive | 005 Night & Mint | **C** | Dark ground; **the six pieces inverted — the limit large in mint, the machine beneath** — as a two-column spread; the rule as a closing line with the action | 0 | 196 |

Row `B B A B C`. Page three takes the row's one `A` (it carried `B B` across `S05`–`S06`).
Page five takes its `C` (it carried `C B`). Page one, after `A` at `S06`, returns to `B`.

## The Governing Idea

> **The machine is named, what it is for is said, and when it is not used is said too.**

The sector's technology section is a gallery of machines with *state-of-the-art* and *latest*
beside each, and no sentence about what the machine answers or what it cannot. This batch names
six pieces a clinic of this kind plausibly holds — **ultrasound, X-ray, heart trace, blood
tests, a pressure monitor to take home, a skin scope** — and for each says, in plain words, the
question it answers and the question it cannot: *not for bone*; *only if the picture would change
what we do*; *rhythm, not blockages*; *only the tests the visit calls for*; *instead of one
nervous reading in a room*; *a look, not a diagnosis*. No brand, no model, no adjective.

**The rule** is in every study: *nothing here is new for the sake of it; if a test would not
change what we do, it is not done, whatever machine we own.* And **not held here**: the scans a
hospital does, arranged for you, and you are told why. `004` turns the rule into the visitor's
question — *what would this test change?* — and makes it the section's offer.

Every action links to the same-variant booking study (`../../S05-appointment-booking/raw/`).

## Density

All five are declared **structured, 170–230**: six named pieces, each with an answer and a limit,
is a list-shaped role. First drafts ran 232–272 and were cut to 196–229 by shortening answers and
limits — never by dropping a limit, which is the honest half of every item. `005`, which sets the
limits at display size, is the shortest.

## Placeholder Data

Two demo values in every study, spelled as words and marked `data-placeholder="true"`: the trace
duration (*ten minutes*) and the blood-test turnaround (*a few days*). **Clear before real use.**

## Media

Ten reserved areas across four studies, all of the contract's third honest subject — *equipment
the text names* — and where a person appears, by role at work: the ultrasound room in use
(`001`); the heart trace being taken — nurse, leads, couch (`002`); six machines each in its room
(`003`); the take-home monitor being fitted (`004`). No diagram, no body part, no rendered
scanner. `005` is type, the limits being the visual.

## Verification Record

- Word band structured `170–230`: **201 / 207 / 229 / 224 / 196.**
- Content parity: **20 shared fields across five studies, 100/100 slots present.**
- Reserved areas: **1 / 1 / 6 / 1 / 0.**
- Claims scan clean; no *state-of-the-art*, *latest*, brand, model, figure, clinician name,
  price, telephone, hour or digit.
- Dependencies none; tag balance, namespace, frame, reduced-motion, `<h2>` labelling, no
  solid-border-plus-max-width, relative hrefs only: all pass.
- Rendered and read at 1440 and 390. Corrections made: `004` frame moved out of the side column
  into a wide band with the not-held line beside it (the column outran the list by a frame's
  height); `003` head measure widened to clear an orphaned last word.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.
