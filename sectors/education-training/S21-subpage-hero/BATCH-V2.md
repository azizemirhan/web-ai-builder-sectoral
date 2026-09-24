# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S21` — Subpage Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the page title *Admissions & enrolment.*, lead and scope line kept as written, one route to the same-variant S07, no navigation, no form; the media counts per study (1, 1, 0, 0, 1) — are kept exactly. The page title is set as the `<h1>` this page owns, as the register sets every subpage hero; V1's scope line is three accent chips.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S21-001` | Universal / Safe | 001 Apricot | 1 — the page title beside the field | loop behind the head | Split page title with the lead; the action with the arrow mark and the scope chips on the lead rule; a shallow 3:1 field of the entrance beneath | 3:1 · 0 | 48 |
| `EDU-S21-002` | Premium / Editorial | 002 Mulberry | 2 — the page heading above a shallow field | rise above the head | Page heading with the lead, the action and the scope chips on the lead rule; a shallow 3:1 field beneath | 3:1 · 0 | 48 |
| `EDU-S21-003` | Structured / Visual Modular | 003 Cobalt | 3 — the title beside guidance | cross grid behind | Split page title with the lead; V1's title field as a band on the band tone split by the lead rule with the action and the scope chips | none · 0 | 40 |
| `EDU-S21-004` | Conversion-led | 004 Iris | 4 — the centred title band with the focused handoff | outline round *enrolment.* | Centred page title, lead at a measured width, the action and the scope chips centred on the lead rule | none · 0 | 40 |
| `EDU-S21-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the large title with a compact field | margin bar along the display column | Display column with the lead, the action and the scope chips; a compact 4:5 field dropped beside | 4:5 · 0 | 48 |

## What changed from V1

V1's contained and curved photographs, the blue title field and the purple title band go; the page title is the h1 with one accent word, the route the 1px action with the arrow mark, the scope line three accent chips, the fields bare 8px areas labelled THE ENTRANCE. The only darkened surface is the 003 band. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S21 -Fields 'Study information|enrolment|Understand how to prepare for an application|Read the admissions guide|Application preparation|Programme requirements|Enrolment steps'` — ALL CHECKS PASS; parity 35/35. One `<h1>` per study (S21 is a hero); no header/nav/footer; no form; one link per study to the same-variant `EDU-S07`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term; no placeholder needed.
- Rendered and read at 1440. Correction: 001 and 002 fields set to a shallow 3:1 so V1's panoramic reading holds at full width.
