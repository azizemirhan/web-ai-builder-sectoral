# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S14` — Sales & Service Stats · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

A stats section is the contract's hardest case: it exists to print figures, and no figure may be printed. So the page publishes the **conditions** instead of the numbers:

> **Every figure here is *somebody's* to check.** A statistic on a dealer page is usually a sentence with a number dropped into it. These are the four we would publish, and where each one comes from.

**The four** — *cars sold* and *jobs completed*, each reserved with the period it covers; **come-backs**, reserved, defined on the page as *the jobs that had to be done again*; and *where these come from*, a reserved source a visitor can check.

The third one is the section's argument:

> **Why the third one is there.** Come-backs are the figure nobody publishes, and the only one that says whether the work was right the first time. It goes above the other two, or it does not go up at all.

> **What gets printed.** Nothing until its period and its source are printed with it. A figure without those is decoration, and decoration is what this page is trying not to be.

**No number of any kind appears in the five studies** — not a count, not a year, not a percentage.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S14-001` | Universal / Safe | 001 Chalk & Racing Green | C | 1 — the four on the lead rule, argument opposed | the bay lines behind the head | none · 4 | 162 |
| `AUTO-S14-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — the job board as the lead image | the plate edge at the head | 1 reserved · 4 | 166 |
| `AUTO-S14-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the four as one itemised sheet | bordered plate, 1px lines shared | 2 reserved · 4 | 170 |
| `AUTO-S14-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — *somebody's*, measured | the torque mark under *somebody's* | none · 4 | 162 |
| `AUTO-S14-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | B | 5 — the four framed against the old part | the ramp frame | 1 reserved · 4 | 166 |

All five sit inside the contract's standard band of 90–170.

**Two studies are `C`, and each records why.** 001: four empty figures beside a photograph would make the photograph the evidence, which is the substitution this page exists to refuse. 004: the conversion-led reading is the offer to hand over the source, and nothing else earns the space.

## What was designed

**No stat tile, no coloured box, no animated counter** — the four sit in the same bare labelled register used for addresses and rates elsewhere in this sector, so a figure gets no more visual authority than an opening hour.

The media is the honest object behind a count: **the job board on the workshop wall**, where the count lives before anybody rounds it, and **the part that came off, on the bench beside the new one** — which is what a come-back looks like.

## Verification

- `autocheck.ps1 -Sec S14 -Fields 'The numbers|Every figure here is|The four we would publish|Cars sold|Jobs completed|Come-backs|Where these come from|Why the third one is there|What gets printed'` — ALL CHECKS PASS; parity 45/45. No `<h1>` (not a hero); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; nothing counts or animates; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; **no figure of any kind**; no manufacturer, model, badge or plate; no rating, award or urgency device; no digit in visible copy outside the field ratio labels; four placeholders per study. Both links point at same-variant S04 and S19 studies.
- Rendered and read at 1440.
