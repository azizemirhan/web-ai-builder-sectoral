# BATCH V1

## Batch Identity

- Sector: `Construction & Contractors`
- Prefix: `CON`
- Section ID: `CON-S23`
- Section Name: `Construction Service Detail`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `CON-S23-001` | Universal / Safe | AUTHORED | `raw/CON-S23-001.html` |
| `CON-S23-002` | Premium / Editorial | AUTHORED | `raw/CON-S23-002.html` |
| `CON-S23-003` | Structured / Visual Modular | AUTHORED | `raw/CON-S23-003.html` |
| `CON-S23-004` | Conversion-led | AUTHORED | `raw/CON-S23-004.html` |
| `CON-S23-005` | Art-directed / Distinctive | AUTHORED | `raw/CON-S23-005.html` |

Twenty-third batch in the `CON` sector, and the first of the detail-page bodies. Role and boundaries
in `./README.md`.

## Authoring Direction

No reference images were supplied for this section. All five studies were originated.

## The Governing Constraint — The Edge Is The Content

    Every service page in this trade lists what is included and stops there. The useful
    part is the edge: what stops being ours, who it becomes, and who owns the joint
    between us.

Buildings do not fail in the middle of a package. They fail at the interfaces, and they fail there
for one reason:

    Water gets in where two trades meet and both thought the other had it.

So the content of this section is **the seam**, and its signature refusal is the claim that there is
not one.

## The Worked Service Is The Building Envelope

Roof, walls, windows and the junctions between them — chosen because it has the richest interface
story in the trade and because the failure mode is unarguable.

| Seam | Who owns the joint |
| --- | --- |
| Roof meets wall | **Ours, both sides.** There is nobody to hand it to and we do not look for one |
| Wall meets window | **Ours to the frame, theirs from it** — drawn on a detail both firms sign before either orders |
| Wall meets ground | **Ours**, and put in writing the day the finished level moves, because it will |
| **Anything that goes through it** | **We take it, and we say so at the start** |

The fourth is the section's real finding: vents, flues, brackets and cables are each a hole in a
thing whose whole job is to have no holes in it, and **on most jobs that joint has no owner at all
until somebody names one.** Every study draws it as unowned before saying who takes it.

## The Three Failure Modes

| Goes wrong | What we do |
| --- | --- |
| **The detail nobody drew.** Standard details cover the typical bay; every job has three junctions the drawings do not show | Draw them and get them signed before we start, not when somebody wants the scaffold down |
| **The sequence.** An envelope is built once and inspected once, from a scaffold already booked to come down | Everything that has to be seen is seen while it is standing, and the sign-off is a condition of striking it |
| **The test.** A water test on a finished building tells you a finished building leaks | **We hose the first bay.** It tests the detail while the detail is still cheap to change |

## The Signature Refusal

> **No turnkey. No one-stop shop. No *we handle everything*.**
>
> A firm claiming there are no interfaces is claiming something no building has — and the interfaces
> it is not claiming are exactly the ones that leak.

## Study Records

| Study | Ground | Model | Anchors |
| --- | --- | --- | --- |
| `001` | `#f0ece1` | The anatomy in five parts, with the seams at the centre | none |
| `002` | `#fcf8ee` | **A walk up one elevation**, stopping where two things meet | none |
| `003` | `#d9dee1` | **The joint as the middle cell**, wider than either party | none |
| `004` | `#161b1e` | **Send us the junctions, not the elevations** | the batch's only ones |
| `005` | `#bcb6ab` | **The dividing rules are the joints** | none |

### `002`, the walk

The description ordered by where you are standing rather than by category — how anybody who builds
an envelope actually explains it: start at the bottom, go up, and every time two things meet, stop
and say whose it is.

**A category list hides the seams between its own categories. A walk cannot**, which is why the
register was chosen rather than decorated onto the content.

### `003`, the joint drawn as a thing

Three cells per seam: the party on one side, **the joint**, the party on the other. The middle cell
is the widest and it is the only one carrying a name.

A scope list gives every package a box and leaves the space between boxes empty, which is exactly
the mistake the buildings make. The sector direction names this variant's trap as *the specification
table*; a table would put packages down one axis and attributes across the other, and the seams
would be nowhere. **These rows have no attributes. They have a middle.**

The fourth row's owner cell is drawn dashed and empty before the answer is given — *on most jobs
this cell is empty* — which is its true state on most jobs.

### `004`, the ask

> **Send us the junctions, not the elevations.**

An elevation shows what a building will look like; a junction detail shows whether it will leak and
whether anybody can price it. Three drawings are named — the parapet, a window head with the tray
drawn rather than noted, and the base with the finished ground level on it — and between them they
say **whether the drawings have been through a building or only through a printer.**

One route says plainly that if those details do not exist yet, drawing them for us is a guess with a
title block on it, and the useful thing is a conversation.

### `005`, the rules are the content

The page is built as an elevation: quiet bands for the parts of the envelope, and **heavy ruled lines
between them carrying the joints and their owners.** In every other layout in this catalog a rule
separates two blocks and means nothing; here the thing a reader would normally read past is the thing
the page is about.

The bottom rule is the only dashed one on the page, because it is the joint that usually has no
owner.

## Compliance

- Structural validation: **PASS.** All five parse; tag nesting verified on a stack for every study.
- Metadata validation: **PASS.** Fourteen research fields plus viewport on all five; `study-id`
  matches filename; territories match the core set in order.
- Isolation: **PASS.** No `<script>`, `<iframe>`, inline `style`, event-handler attribute, remote
  reference, embedded image, inline SVG or form control anywhere in the batch.
- **One-mechanism check: PASS.** Anchors in exactly one study, and it is `004`; all route in-page.
- **Seam check: PASS.** All four seams named in all five studies, and all four owners stated in all
  five.
- **Unowned-joint check: PASS.** The joint that usually has no owner is named as such in all five.
- **Failure-mode check: PASS.** At least two of the three stated per study.
- **Refusal check: PASS.** The no-interfaces claim refused in all five.
- **Scope check: PASS.** The work has a stated outside, with the trade that does it instead, in all
  five.
- **Drawing check: PASS.** Nothing drawn at an angle — carried from `S18`.
- **Placeholder check: PASS.** No em-dash placeholder; every reserved value labelled.
- **Media check: PASS.** The one media area is a reserved area **of a junction**, not of a finished
  elevation.
- **No-refusal-region check: PASS.** The architecture run carries none, so the vocabulary scans ran
  on the complete visible copy.
- **Vocabulary check: PASS.** No *turnkey*, *one-stop*, *end-to-end*, *we handle everything*, no
  guarantee or warranty, no *approved installer* or *certified*, no price and no before-and-after.
- **Digit check: PASS.** No digit in visible copy in any of the five.
- Responsive QA: **PASS.** Verified at 1440px; each study states its ladder.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.**
- Section-shell check: **PASS.**
- Scoped-CSS check: **PASS.**
- **Markdown-artefact check: PASS.**
- Ground check: **PASS.** Five distinct grounds, none used by `S01`–`S22`, and the five separate on a
  contact sheet.
- Render check: **PASS**, after one correction.

## Corrections Before Render

Two genuine content gaps, caught by the checker:

| Study | Was | Now |
| --- | --- | --- |
| `003` | The signature refusal was missing — the study named every seam and never said why a firm would claim it had none | The no-turnkey line added to its foot |
| `004` | No statement of what is outside the work, and only one of the three failure modes | The excluded packages named with the trades that carry them, and the scaffold failure added to the late-stage route |

And one the checker could not see:

| Study | Was | Now |
| --- | --- | --- |
| `003` | **A reserved value rendered as a full-width grey bar.** A `.do span` rule intended for a small label had captured the `.slot` span inside the same paragraph and given it `display: block` | Scoped to the first child |

That is **the third time in this sector a descendant selector on an element type has captured a later
element of the same type** — after `S13-005` and `S17-005`. All three passed every check, all three
looked deliberate, and all three were found by looking at the render. It is now the single most
reliable defect in this catalog's CSS.

## Checker Note

Four rules failed studies for phrasing rather than substance and were broadened: the level-moves
clause, the first-bay clause, the fourth seam's name, and — the checker's own bug — **the
screen-reader-label count, which had been written for one of the two label forms this catalog uses.**
`S22` puts the label immediately before the slot; this section puts it inside. Both are correct, and
the rule now counts both.

The distinction held: two of the six failures were rules written too narrowly, two were genuine gaps
in the studies, and each was fixed in the place where the fault actually was.

## Notes

- Twenty-third authored batch in the `CON` sector. `S01`–`S23` are complete.
- **The reusable outcome is that a service page should be written from its edges inward.** What is
  included is guessable; what stops being yours, who it becomes and who owns the joint is not, and it
  is the only part a client cannot get from a competitor's page.
- The second outcome is `005`'s: **the furniture can be the content.** A rule between two blocks is
  the most ignored element in any layout, and on a page about junctions it is the only element that
  should be loud.
- The third is the fourth seam. **Drawing a joint as unowned before naming an owner is worth more
  than naming the owner** — it tells a reader what normally happens, which is the thing they can
  check against their own experience.
- `S24 Project Detail` is next.
