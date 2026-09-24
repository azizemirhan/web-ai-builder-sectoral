# BATCH V1

## Batch Identity

- Sector: `Healthcare & Medical Clinics`
- Prefix: `HC`
- Section ID: `HC-S01`
- Section Name: `Hero`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

First batch in the `HC` sector. It establishes `../HEALTHCARE-THEME-CONTRACT.md` — the sector's
register, anti-patterns, media rules, claims limits, five fixed themes and page-rhythm rules — and
every later batch is authored against it.

## Planned Studies

| Study ID | Direction | Theme | Shape | Composition | Areas | Words |
| --- | --- | --- | :---: | --- | ---: | ---: |
| `HC-S01-001` | Universal / Safe | 001 Linen & Sage | B | Proposition and action left, **the consulting room at the larger half**, three commitments beneath | 1 | 90 |
| `HC-S01-002` | Premium / Editorial | 002 Porcelain & Plum | B | Headline at a narrow measure, **the waiting area as a 21:9 band edge to edge**, commitments as one ruled line | 1 | 90 |
| `HC-S01-003` | Structured / Visual Modular | 003 Sky & Slate | B | **A scroll-snap rail of three frames in visit order** — reception, a nurse at work, the consulting room — with a commitment under each | 3 | 82 |
| `HC-S01-004` | Conversion-led | 004 Sand & Terracotta | B | The treatment room at full width, **commitments and the action in a band pulled over its lower edge** | 1 | 90 |
| `HC-S01-005` | Art-directed / Distinctive | 005 Night & Mint | B | Dark ground, **the doctor at work in a tall frame at full height**, headline large, numbered commitments | 1 | 89 |

All five are shape `B`, as a hero is; no `A` sequence begins. Every study is image-dominant, which is
the sector's reading of what a hero is for.

## The Governing Idea

> **The visitor has a symptom, not a shopping list.**

The sector designs for a comparison shopper. The real visitor is worried, in a hurry, often on a
phone, and wants three things before anything else: *is this the right place for what I have, how
soon can I be seen, what happens when I get there.* The headline answers the first two in one
sentence — *Tell us what is wrong. We will tell you who you need to see, and how soon.* — and the
lead answers the third. Nothing else in this sector opens by taking the symptom seriously.

## Why The Three Facts Are Commitments, Not Adjectives

*Compassionate*, *dedicated* and *patient-centred* are what a clinic writes when it has nothing to
state. Each of the three shared facts is something a visitor could check by asking:

| Commitment | What it replaces |
| --- | --- |
| **The right person first** — told before booking if this is the wrong place, and where to go | "Comprehensive care" |
| **A time you can plan around** — first appointments usually within *a week* (demo value) | "Book online" |
| **What was found, in writing** — what happens next, and who to ring | "Compassionate care" |

## The Three Honest Media Subjects

The contract admits three subjects and this batch uses all of them: **the room** (001 consulting,
002 waiting, 004 treatment), **the people by role** (003's nurse, 005's doctor at work) and **the
desk** (003's reception). Never a stethoscope on a desk, a white-coat line-up, a pulse line, or a
stock doctor with folded arms.

## Placeholder Data

One per study, marked `data-placeholder="true"`: the usual wait for a first appointment, spelled
as a word. No clinician name, credential, outcome figure, price, insurer, address, telephone or
opening hour appears anywhere in the batch. The action links to `#` because `S05` is not yet
authored.

## Verification Record

- Word band `40–90` (hero): **90 / 90 / 82 / 90 / 89.** The first pass came in at 92–106; the lead
  was tightened by two words everywhere, and `003` dropped its lead and its scroll hint because
  the rail shows the visit in order and carries a commitment under each frame.
- Content parity: **9 shared fields across five studies, 45/45 slots present.**
- Reserved areas: **1 / 1 / 3 / 1 / 1.**
- Claims scan clean against the contract's list; no digit in any body text except the marked demo
  value, which is a word.
- Dependencies: **none.** No script, image, iframe, SVG, form, link, import or absolute URL.
- Tag balance, namespace scoping, 1320px frame, `prefers-reduced-motion`, one `<h1>` per study,
  no solid divider carrying its own `max-width`: all pass.
- Measured at 1440, 768, 390 and 320px; rendered and read at 1440 and 390.
- **One fault found by rendering:** `005`'s tall frame overflowed the right edge. `aspect-ratio:
  3/4` with `min-height: 100%` in a stretched grid cell derives the width from the stretched
  height, and the width came out wider than the column. The desktop frame now fills its cell with
  a `min-height` and no ratio; the ratio applies only below 980px where the cell is no longer
  stretched. **A ratio and a stretch cannot both own the same box.**
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Tooling

`node` and `python3` are absent on this machine. Checks run through a PowerShell script
(`hccheck.ps1`: theme tokens, host background, frame, reduced-motion, namespace, dependencies,
tag balance, heading level, claims, digits, relative links, solid-border-plus-max-width, content
parity) and heights and renders through headless Chrome driven by `Start-Process`, with phone
renders captured through a 390px iframe because headless Chrome enforces a wider minimum window.
