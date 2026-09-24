# BATCH V1

## Batch Identity

- Sector: `Healthcare & Medical Clinics`
- Prefix: `HC`
- Section ID: `HC-S08`
- Section Name: `Patient Journey`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Direction | Theme | Shape | Composition | Areas | Words |
| --- | --- | --- | :---: | --- | ---: | ---: |
| `HC-S08-001` | Universal / Safe | 001 Linen & Sage | B | Six numbered steps with what happens and *you can* on the left, **the corridor from the waiting room** as a tall frame on the right; at-any-point foot with the action | 1 | 209 |
| `HC-S08-002` | Premium / Editorial | 002 Porcelain & Plum | **A** | **A photo essay of six frames, one per step in order** — reception on the phone, the desk, the consulting room, the couch, the sample room, the letter — with the step in serif beneath | 6 | 229 |
| `HC-S08-003` | Structured / Visual Modular | 003 Sky & Slate | **C** | **A CSS rail of six numbered stops**, then six modules three-by-two, each with the same three fields — *happens*, *asked*, *you can* | 0 | 225 |
| `HC-S08-004` | Conversion-led | 004 Sand & Terracotta | B | Head beside **two seats in the waiting room**; **a terracotta panel — *nothing to prepare* — with one action**, the six steps as a two-column list | 1 | 226 |
| `HC-S08-005` | Art-directed / Distinctive | 005 Night & Mint | B | Dark ground; **a mint spine down the centre with the six steps hung alternately left and right**, ending at **the front door from inside** | 1 | 214 |

Row `B A C B B`. Page two takes the row's `A` (it carried `C B B` across `S05`–`S07`). Page
three takes its `C` after the `A` at `S07`. Page five, after `C B C`, returns to `B`.

## The Governing Idea

> **What happens, in order, what you are asked at each step, and what you can do at each step.**

The sector's journey section is four icons and four verbs — *book, arrive, treat, recover* —
that tell a worried person nothing about the day. This batch walks the **six things that
actually happen**, from the call to the letter:

1. **The call** — four questions about what is wrong; *you can ask for a particular person.*
2. **The desk** — only now do we ask who you are: name and date of birth; *you can bring
   someone with you.*
3. **The conversation** — what is wrong, in your words, usually *half an hour*; *you can ask
   for it said again.*
4. **The examination** — told before it starts; nothing without your yes; *you can ask to stop.*
5. **Tests, if any** — only if the result would change what we do; *you can ask what the result
   would change.*
6. **The letter** — what was found and what happens next, in your hand before you leave; *you
   can ask for a copy for someone else.*

**Identity is asked for at the desk, not before** — the `S05` claim kept at the moment it is
tested. **At any point:** if this is not the place for it, you are told, and referred; emergencies
go to the emergency service. Every action links to the same-variant booking study.

## Density

All five are declared **structured, 170–230**: six steps, each with what happens and what you can
do, is a list-shaped role; `003` carries a third field. First drafts ran 242–299 and were cut to
209–229 by shortening what-happens lines and the foot — never by dropping a *you can* line, which
is the section's reason to exist.

## Placeholder Data

Two demo values in every study, spelled as words and marked `data-placeholder="true"`: the usual
length of the first visit (*half an hour*) and the wait for results (*a few days*). **Clear
before real use.**

## Media

Ten reserved areas across four studies, every one a room or a person by role at work: the
corridor (`001`); the six places of the six steps in order (`002`); two seats together in the
waiting room — the picture of *bring someone* (`004`); the front door from inside at the end of
the visit (`005`). No icon, no progress bar, no stock hand-on-shoulder. `003` is type by intent.

## Verification Record

- Word band structured `170–230`: **209 / 229 / 225 / 226 / 214.**
- Content parity: **23 shared fields across five studies, 115/115 slots present.**
- Reserved areas: **1 / 6 / 0 / 1 / 1.**
- Claims scan clean; no clinician name, outcome, figure, price, telephone, hour or digit.
- Dependencies none; tag balance, namespace, frame, reduced-motion, `<h2>` labelling, no
  solid-border-plus-max-width, relative hrefs only: all pass. `005` stagger uses explicit
  `grid-area` rows for every stop.
- Rendered and read at 1440 and 390; no layout corrections required.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.
