# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S20`
- Section Name: `Final Booking CTA`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S20-001` | Universal / Safe | AUTHORED | `raw/WELL-S20-001.html` |
| `WELL-S20-002` | Premium / Editorial | AUTHORED | `raw/WELL-S20-002.html` |
| `WELL-S20-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S20-003.html` |
| `WELL-S20-004` | Conversion-led | AUTHORED | `raw/WELL-S20-004.html` |
| `WELL-S20-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S20-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's role and its boundary with `S01`, `S06` and `S19`
are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint — Two Rules

**1. No mechanism.** `S06` is the booking moment and carries the machinery. A final CTA holding a
booking form is `S06` in the wrong place, and a catalog that allows it can no longer tell the two
sections apart.

    S06 gives you the means. S20 gives you the moment.

**No study in this batch contains a `<form>`, a field, a select, a date or a time.** Verified by
scan across all five. The actions are links, and the space the form would have occupied is spent on
the answer to *what am I agreeing to*.

**2. No pressure.** This is where a wellness site most often loses its register.

| Device | Treatment |
| --- | --- |
| Scarcity count | **Forbidden** — an invented figure and a manufactured pressure |
| Countdown or deadline | **Forbidden** |
| Client or booking counts | **Forbidden** — the `S10` rule |
| Discount, offer, saving | **Forbidden** — the `S12` rule |
| Price | **Omitted** — `S11` owns money |
| Star rating or review score | **Forbidden** — the `S10` rule |

**Not present in any study:** an invented figure of any kind; a countdown, deadline, scarcity or
availability count; a discount, offer, saving or price; a client, booking or review count; a star
rating or testimonial; an invented telephone number, email address or address. Verified by scan —
**no digit appears in visible copy anywhere in the batch.**

Urgency vocabulary does appear, and only in the negative: *no good reason to rush*, *nothing here
expires and nothing is running out*, *you will not find a countdown on this page*. Each occurrence
was listed by the checker with its surrounding sentence and read in context; all seven are
negations. That two-tier scan — hard failures plus soft occurrences reported for an eye check — is
new in this batch and is the right shape for any rule whose vocabulary a study may legitimately
need in order to refuse it.

## What Is Real — Reassurance Instead Of The Push

What moves somebody at the foot of a wellness page is not urgency but the knowledge that the step is
small and reversible. All of it is operating policy, so all of it is authorable:

| The worry | The answer |
| --- | --- |
| I will be locked in | Nothing is confirmed until you have agreed a time |
| Something will come up | Moving it is easy, and nobody is cross about it |
| I will be talked into more | Asking is not buying; a conversation is not a treatment and is not charged for |
| I will not be able to back out | You can say no at the end, and changing your mind in the room is normal |
| I am being rushed | There is no countdown, and there never will be |

**The last row is the batch's defining content.** Naming the pressure the section is *not* applying
is only sayable because the batch gave up the device — and unlike a scarcity line, it is true.

## Study Records

### WELL-S20-001 — Universal / Safe

- **Layout model:** A centred ask with two actions — book one, or talk first — above three
  reassurances in a row.
- **Why two actions:** a single button assumes readiness. The second route costs one line and keeps
  the visitor who is still deciding, which in this sector is a large share of everyone who reaches
  the foot of the page.
- **The reassurance row takes the position a scarcity line normally occupies.** That substitution is
  the batch's whole argument, and `001` states it in the most conventional layout available, which
  is the point of the Universal direction.
- **Responsive strategy:** actions go full width and stack at 768px; the reassurances go 3 → 1.

### WELL-S20-002 — Premium / Editorial

- **Layout model:** One serif sentence at display scale, one action set as a ruled link, one quiet
  line. Nothing else.
- **The editorial argument — the closing ask should be the quietest thing on the page.** A loud
  final CTA reads as a business that needs the booking, which is the opposite of what this sector
  sells. Fewest elements of any study in the `WELL` sector.
- **Why a ruled link rather than a filled pill:** a filled pill is the visual grammar of urgency. A
  large ruled link is unmistakably an action, keeps a 52px target, and does not raise its voice.
  **The only study in the batch whose action is not a filled shape.**
- **Responsive strategy:** measures release at 768px; nothing else changes, because there is nothing
  else.

### WELL-S20-003 — Structured / Visual Modular

- **Layout model:** Four modules in a square. The ask sits on a dark ground in the first; the other
  three answer what happens next, what can still change, and what you are not agreeing to.
- **The device — the small print, promoted.** Everything in those three modules is normally omitted
  or buried behind a link. Set as equals to the ask, they do the work a scarcity line would
  otherwise do.
- **One step, not a schedule:** *what happens next* is a single move — somebody gets in touch — on
  the `S08` rule that a sequence is content and a schedule is a claim.
- **Correction made, recorded:** in the first render the ask module ran much taller than the module
  beside it, and grid stretching left a large empty field in *what happens next*. The ask was
  trimmed and the answer module given a second line, which balanced the row without changing the
  topology.
- **Responsive strategy:** 2 × 2 → single column at 768px; the action goes full width.

### WELL-S20-004 — Conversion-led

- **Layout model:** Two routes side by side with their own actions, above a three-part risk-removal
  row and the statement of what this section refuses to do.
- **Conversion device:** every device that would normally sit here is missing on purpose, **and the
  study says so out loud**. In a sector built on trust, naming the pressure you are not applying
  does the work the pressure was supposed to do.
- **Why the second route is not a form:** `S19` owns the message form. Here it is one line and a
  link, which keeps the section a decision rather than a second contact page.
- **A correction to the copy, recorded:** the no-pressure line originally read *"no offer ending on
  Sunday"*. Even inside a negation, a named day reads as a deadline at a glance, so it became *"no
  offer that expires while you are thinking about it"*. Worth recording because it is the failure
  mode of this whole rhetorical device: **a negated urgency line still prints the urgency word.**

### WELL-S20-005 — Art-directed / Distinctive

- **Layout model:** One sentence at display scale with **the action set inside the sentence**, above
  a wide reserved media band.
- **The device — the button is a word in the line.** It cannot be skimmed past as page furniture,
  and it makes the sentence do the persuading rather than the colour. The pill is set at `0.62em`
  so it reads as part of the line rather than a badge dropped into it, and it keeps a 52px target.
- **Why an inline action holds up here:** it is the only interactive thing in the section, and it
  sits in the largest type on the page — so the thing you cannot miss and the thing you can press
  are the same object.
- **The batch's only reserved media.** A 21:9 band at the foot, becoming 4:3 below 768px. It sits
  *after* the decision rather than behind it, so the picture supports the ask instead of competing
  with it.
- **Correction made, recorded:** the band sat at 1.24:1 against its ground and depended on its
  dashed edge alone; deepened to `#2a1a0e` for 1.46:1, the same fix as `S19-005` and `S10-005`.

## Structural Diversity

| Study | Topology | Actions | Media | Ground |
| --- | --- | --- | --- | --- |
| 001 | Centred ask + three reassurances | 2, pills | None | Pale sage `#eaeeec` |
| 002 | One display sentence | 1, ruled link | None | Warm parchment `#f6f1ea` |
| 003 | Four-module square | 1 pill + 1 text link | None | Pale lilac `#e6e3ec` |
| 004 | Two routes + risk row + refusal | 2, pill and ghost | None | Deep forest `#123a35` |
| 005 | Display sentence with an inline action | 1 inline + 1 text link | One 21:9 band | Deep bark `#4a3524` |

Grounds do not repeat any used in `WELL-S01`–`S19`; verified by scan across all 100 studies.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-02.
- **Visual-first check:** no study derives its distinctiveness from copy. The differentiator is how
  much page a single action deserves — a centred pair, a ruled line in white space, a corner of a
  modular square, one of two routes, or a word inside the largest sentence on the page.
- **Document-metaphor justification:** `NONE`.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** All five studies are fully static. No `<script>`, no `<iframe>`,
  no inline `style` attribute, and — uniquely to this batch — no form element of any kind.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| The room | `005` — a wide band at the foot | Still image, 21:9 (4:3 below 768px) | Empty tonal surface with a quiet label |

The other four studies reserve nothing. **A closing ask does not need a picture**, and four of five
studies test that position while `005` provides the media-carrying alternative for the catalog.

## QA

- ID validation: **PASS.** All five IDs exist and match their filenames.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport. Nesting validated with a stack-based parser; all five parse correctly.
- Accessibility QA: **PASS.** `lang`, scoped `:focus-visible`, `aria-labelledby`,
  `prefers-reduced-motion`. Every action is at least 52px tall, including `005`'s inline pill and
  `002`'s ruled link.
- Responsive QA: **PASS.** Breakpoints authored per study; verified at 1440px and 720px with no
  horizontal overflow. `005`'s inline action stays inside its line at both widths.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image, script, iframe
  or inline style.
- CSS-validity scan: **PASS.** No malformed hex, no accidental 8-digit hex, no `clamp()` with the
  wrong arity.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status.
- Scoped-CSS check: **PASS.** Every declaration outside the host baseline is namespaced to the
  study's own `.well-s20-00N` root.
- **No-mechanism check: PASS — this batch's defining check.** No `<form>`, `<input>`, `<textarea>`
  or `<select>` in any of the five files.
- **Pressure and figure check: PASS.** Visible text only, scanned for **any digit**, currency
  symbols, percentages, *only N left*, *book by*, *limited*, *join N clients*, *save*, *discount*,
  *off*, *deal*, *sale*, *stars*, *rated*, *reviews*, *testimonial*, *price*, *per session*, *act
  now*, *selling fast*, *filling up*. **Zero matches in all five.** Seven soft occurrences of
  urgency vocabulary were listed with context and confirmed to be negations.
- Render check: **PASS, after three corrections.** All five rendered in headless Chrome at 1440px
  and inspected: `003`'s module row was rebalanced, `004`'s negated urgency line lost its named day,
  and `005`'s media band was deepened for contrast. All recorded above.

## Notes

- This is the twentieth authored batch in the `WELL` sector, the eighteenth authored entirely
  without references, and **it completes the sector's core catalog, `S01`–`S20` — one hundred
  studies.**
- **The reusable outcome is that a final CTA is defined by what it gives up.** Strip the form
  (it belongs to the booking section) and strip the pressure (it belongs to nobody), and what is
  left is a decision plus the reassurance that makes the decision small. Every sector with a
  considered purchase — clinics, studios, practices, anything booked rather than bought — can take
  this batch unchanged in structure.
- The two-tier scan is the batch's reusable tooling contribution: **hard failures, plus soft
  occurrences printed with their surrounding sentence for a human check.** Any rule a study might
  legitimately need to name in order to refuse it needs that second tier, or the checker starts
  punishing honesty.
- `S01`–`S20` now hold the full arc: `S01` opens, `S02`–`S18` argue, `S19` answers questions, `S20`
  closes. `S21`–`S27` remain scaffolded and unauthored.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a Windows Store placeholder
  rather than an interpreter. Headless Chrome, which the generator uses for measurement, is present
  and working, so a Node port of `review/build-index.py` would restore it — and with the core
  catalog now complete at one hundred studies, that contact sheet is the one thing missing from
  being able to review the sector in one place.
