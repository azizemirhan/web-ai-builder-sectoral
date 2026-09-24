# BATCH V1

## Batch Identity

- Sector: `Healthcare & Medical Clinics`
- Prefix: `HC`
- Section ID: `HC-S05`
- Section Name: `Appointment Booking`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Direction | Theme | Shape | Composition | Areas | Words |
| --- | --- | --- | :---: | --- | ---: | ---: |
| `HC-S05-001` | Universal / Safe | 001 Linen & Sage | B | The four questions as a numbered list beside **reception on the phone**, three routes as a row, what you get and the emergency line | 1 | 169 |
| `HC-S05-002` | Premium / Editorial | 002 Porcelain & Plum | **C** | **The four questions as four large numbered display lines**, routes as a ruled three-column row, what you get as a pair | 0 | 163 |
| `HC-S05-003` | Structured / Visual Modular | 003 Sky & Slate | B | **Three route modules with the same three fields (how / what happens / when you hear)**, then the questions beside **the desk, appointment book open** | 1 | 227 |
| `HC-S05-004` | Conversion-led | 004 Sand & Terracotta | B | **A terracotta panel carrying the four questions and one action**; head, **the waiting room from the door** and the other routes on the right | 1 | 171 |
| `HC-S05-005` | Art-directed / Distinctive | 005 Night & Mint | **C** | Dark ground, **the booking conversation transcribed** — reception's four questions and an empty turn for the visitor after each | 0 | 216 |

Row `B C B B C`. Page two takes a second `C` at `002` (it carried `C B B` across `S02`–`S04`).
Page five takes its `C` at `005` (it carried `C A B B`). No page has two consecutive `A`.

## The Governing Idea

> **Booking is a short conversation about what is wrong, not a form about who you are.**

The sector's booking section is a form: name, date of birth, insurer, address, reason for visit
as a dropdown. It asks a worried person to identify themselves before anyone has asked what is
wrong. This batch says what the conversation actually is — **four questions**: *what is wrong, in
your own words; how long, and whether it is getting worse; whether you would like a particular
person; dates that do not work* — and that the same four are asked whichever of the **three
routes** you take (ring, online, at the desk), so nobody fills in a form to be asked them again
on the phone. **What you get** closes every study: *a time, who you will see by role, and what
the first visit involves, in writing* — the `S01` commitments at the moment they are made.

**No form.** The contract forbids one, and a form in a standalone study would imply submission
through a purely local page. `004` builds the panel a form would occupy and fills it with the
questions instead; `005` shows the conversation as a transcript and leaves the visitor's turns
empty rather than inventing answers, because a fabricated *"I have had this pain for weeks"* is a
testimonial by another name.

**Emergencies are not booked. Use the emergency service.** In every study.

## Density

`001`, `002` and `004` sit in the standard band. `003` is declared **structured** because three
routes compared field by field is a structured role; `005` is declared **structured** because a
transcript restates the four questions as speech and adds a turn after each — cutting turns would
make it not a transcript. Both reasons are recorded in the study headers.

## Placeholder Data

Every study carries the same three demo values, spelled as words and marked
`data-placeholder="true"`: the call-back window for the online route (*the same working day*,
once) and the usual wait for a first appointment (*a week*). **Clear before real use.**

## Media

Three reserved areas, one each in `001`, `003` and `004`: reception on the phone, the desk with
the appointment book open, and the waiting room from the door. The person and the place the
text names; nobody posed, no stock smile. `002` and `005` are type by intent and the reason is
in each header.

## Verification Record

- Word bands: **169 / 163 / 227 / 171 / 216** (standard / standard / structured / standard /
  structured).
- Content parity: **17 shared fields across five studies, 85/85 slots present.**
- Reserved areas: **1 / 0 / 1 / 1 / 0.**
- Claims scan clean; no telephone number, hour, insurer, price, clinician name or digit.
- No `<form>`, `<input>` or `<button>`; the one action in each study is a link to `#`.
- Dependencies none; tag balance, namespace, frame, reduced-motion, `<h2>` labelling, no
  solid-border-plus-max-width: all pass.
- Rendered and read at 1440 and 390. Corrections made: `003` questions restacked in one column
  and the desk frame given the column's height (a 4:3 frame outran the list); `004` panel
  questions enlarged so the action sits at the panel's base without a dead field above it.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.
