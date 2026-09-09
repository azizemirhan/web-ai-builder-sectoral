# BATCH V1

## Batch Identity

- Sector: `Consulting & B2B Professional Services`
- Prefix: `CONS`
- Section ID: `CONS-S01`
- Section Name: `Hero`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

First batch in the `CONS` sector. Authored directly against
`../CONSULTING-THEME-CONTRACT.md`, which was written with it and establishes the sector's register,
anti-patterns and five themes for all twenty-seven sections.

## Planned Studies

| Study ID | Authoring Direction | Theme | Status | Raw File |
| --- | --- | --- | --- | --- |
| `CONS-S01-001` | Universal / Safe | 001 Paper | AUTHORED | `raw/CONS-S01-001.html` |
| `CONS-S01-002` | Premium / Editorial | 002 Sable | AUTHORED | `raw/CONS-S01-002.html` |
| `CONS-S01-003` | Structured / Visual Modular | 003 Field | AUTHORED | `raw/CONS-S01-003.html` |
| `CONS-S01-004` | Conversion-led | 004 Signal | AUTHORED | `raw/CONS-S01-004.html` |
| `CONS-S01-005` | Art-directed / Distinctive | 005 Midnight | AUTHORED | `raw/CONS-S01-005.html` |

## The Section Role

The opening proposition of a firm that sells judgement. It answers, in the time somebody takes to
decide whether to scroll: **what kind of decisions do you work on, at what altitude, and who
actually shows up?**

## The Governing Constraint — Judgement Has No Photograph

    Architecture has buildings. Construction has sites. Wellness has treatment rooms.
    Consulting has a decision that already happened in a room nobody photographed.

This is the sector's whole design problem, and the reason its websites default to stock handshakes,
boardroom tables and glass towers. The batch's answer is fixed in the sector direction and applied
in all five studies:

**The one honest photographic subject is people — and specifically the people who would actually be
on the engagement.** Every media slot in this batch therefore states *what the photograph is* and
never who is in it: the partner who would run the work, the team that would be assigned, a partner
mid-sentence rather than posed against a window.

The second constraint follows from it: **the pose is the failure, not the subject.** A slot that
reserves space for a posed executive portrait has not avoided the cliché; it has reserved space for
one. The labels say so.

## Structural Direction, And How The Five Differ

Each study is a different composition carrying the same register, per the theme contract's split
between what is fixed and what is free.

| Study | Composition | Media treatment | Reserved figures |
| --- | --- | --- | --- |
| `001` | Split — proposition left, portrait panel right, hairline figure row beneath | Tall 4:5 panel beside the text | Three |
| `002` | Full-frame display statement, offset second voice, wide band, hairline coda | Wide 21:9 band given the whole frame | Two |
| `003` | Three-column bay grid: proposition bay, portrait bay, three practice bays, action bay | A module in the grid | One, inside the action bay |
| `004` | Split head, then one saturated panel stating what the offered conversation is | Held back to the head so it does not compete | **None** |
| `005` | Tall portrait held left, oversized line crossing back over its edge from the right | The largest field of the five | One |

`004` carries no reserved figure by design: a counter competes with a single action, and the
compositional argument of that study is that one thing dominates.

`005` earns its direction through composition rather than an applied device — the line is set in the
right column and pulled back across the portrait's edge, so the type and the person occupy the same
space. The crossing releases at `860px`, because a crossing that becomes an overlap on a phone is a
defect rather than a signature.

## The Conversion Problem In 004

The generic hero here is a headline and a *Book a consultation* button. It converts badly in this
sector, because a senior buyer does not know what they are agreeing to and assumes it is a sales
call. So the conversion device is not a larger button — it is **stating what the meeting is**: who
is in it, what it is about, and what does not happen afterwards.

Those three statements are policy commitments a firm can honour, not claims about past performance,
so none is a fabricated metric. No response time is promised anywhere in the batch.

## Research Metadata

- Sources: no reference images were supplied for this section. All five studies were originated
  against the modern-web register the user supplied for the workspace as a whole, read for this
  sector in `../CONSULTING-THEME-CONTRACT.md`.
- Research date: 2026-09-07.
- Structural direction rationale: recorded above and per study in each file's comment header.
- Differentiation notes: see the composition table. No two studies share a layout, a ground or an
  accent.
- Visual-first check: every study is differentiated by composition, media treatment and scale rather
  than by copy volume. The heaviest study is 90 visible words and the lightest is 47.
- Document-metaphor justification: `NONE`. No study uses a technical or professional document
  metaphor. This is load-bearing in this sector — the 2×2 matrix is its signature ornament, and the
  direction rules it out.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: NONE — all five studies are static.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Portrait area (`001`) | The partner who would run the engagement | Portrait photograph, 4:5 | Labelled reserved area; legible empty; alt text describes the person's role, never a fabricated name |
| Portrait area (`002`) | The people who would be in the room, as themselves | Group photograph, 21:9 | As above |
| Portrait bay (`003`) | The team that would be assigned, at working size | Photograph, module-sized | As above |
| Portrait area (`004`) | The person who takes the first call and would run the work | Portrait photograph, 4:5 | As above |
| Portrait area (`005`) | A partner mid-sentence, not posed against a window | Portrait photograph, 3:4 | As above |

Empty reserved media areas are intended output, not defects.

## Counter Values — Placeholder Demo Data

The counters are filled with demo values rather than left as em dashes, so the compositions can be
judged with content in them. Per *Placeholder Demo Values* in `../CONSULTING-THEME-CONTRACT.md`:

| Field | Demo value | Appears in |
| --- | --- | --- |
| Year the practice was founded | `1998` | `001`, `002`, `003`, `005` |
| Engagements completed | `340+` | `001`, `002` |
| Offices | `6` | `001` |

The same values are used across the batch on purpose: a reviewer comparing the five studies then
sees identical facts presented five ways, which isolates the design difference instead of adding a
second variable.

Every filled figure carries `data-placeholder="true"`, and each study declares
`<meta name="placeholder-data">`, so all of them can be found and cleared mechanically before real
use. Removing the dashed box also changed the styling: the figure is now set as display numerals,
which is what stops it reading as an unfilled field.

**Still excluded, demo or not:** named clients and logos (confidentiality, sector-wide), awards,
rankings, certifications, and any percentage or multiple that asserts a measurement nobody ran.

**Media areas remain reserved.** A photograph cannot be placeheld the way a number can, so the
portrait slots are unchanged and their empty state is still intended output.

## QA

- ID validation: PASS — five IDs matching filenames and `<meta name="study-id">`.
- Raw-format validation: PASS — standalone HTML, scoped CSS, tag balance verified on all five.
- Dependency check: PASS — no framework, CDN, remote dependency or script.
- Text budget: PASS — 47 to 90 visible words against the contract's hero band of 40–90.
- Theme conformance: PASS — one chromatic accent per study, one per theme, no two alike.
- Placeholder declaration: PASS — every filled counter carries `data-placeholder="true"` and every
  study carrying one declares `<meta name="placeholder-data">`. `004` carries no counter and no
  declaration, which is correct.
- Section-shell rule: PASS — no global header, navigation or footer in any study.
- Render check: PASS — all five rendered in headless Chrome at 1440 and inspected. A three-line
  wrap on the reserved-figure label in `003` and `005` was found and corrected.
- Accessibility QA: NOT_RUN — reserved fields expose their meaning to assistive technology through
  visually hidden labels, and focus ring, heading order and a reduced-motion block are in place, but
  no full checklist pass has been run.
- Responsive QA: NOT_RUN — ladders authored at `860px` and `560px` in all five and at `980px` in
  `003`; verified by code review only. `review/build-index.py` cannot run on this machine because
  Python is not installed, so the contact sheet has not been regenerated for this batch.
