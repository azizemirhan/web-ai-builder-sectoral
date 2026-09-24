# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Education & Training` · Prefix: `EDU` · Section: `EDU-S22` — Breadcrumb & Context Navigation · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, EDU translation in `../EDUCATION-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the breadcrumb with Home to the same-variant S01 and the current page, the local navigation labelled *Explore admissions* with three routes to the same-variant S07, S16 and S17, no global navigation, no media — are kept exactly. The two `<nav>` landmarks are V1's and are the only navigations the register allows in this section.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `EDU-S22-001` | Universal / Safe | 001 Apricot | 1 — the inline trail beside the topic links | loop faint behind the strip | One strip on hairlines — the trail with the house mark and the current page left; the tracked label with the layers mark and three underlined links right | none · 0 | 11 |
| `EDU-S22-002` | Premium / Editorial | 002 Mulberry | 2 — the trail above an open row | rise above the trail | The trail with the current page at statement size; the label and three underlined links in a row on the lead rule | none · 0 | 11 |
| `EDU-S22-003` | Structured / Visual Modular | 003 Cobalt | 3 — the trail cell beside a stacked list | cross grid behind | A bordered plate with the trail as a cell on the band tone, where V1 set its blue field, beside the label and three underlined links stacked on hairlines | none · 0 | 11 |
| `EDU-S22-004` | Conversion-led | 004 Iris | 4 — the compact trail above the topic band | outline round the current page | The trail with the outline round *Admissions & enrolment*; V1's band on the band tone split by the lead rule with the label and three underlined links | none · 0 | 11 |
| `EDU-S22-005` | Art-directed / Distinctive | 005 Afterhours, inverted | 5 — the two-level strip with a topic rail | margin bar along the trail | The trail with the current page at display size in the accent; the label and three underlined links as a ruled rail beside, where V1 set its lime rail | none · 0 | 11 |

## What changed from V1

V1's rounded topic pills, the blue and purple fields and the lime rail go; the trail is Home with the house mark, a muted slash and the current page in ink, and the routes are underlined links with the arrow under a tracked label with the layers mark. The darkened surfaces are the 003 trail cell and the 004 band. Copy is V1's throughout.

## Verification

- `educheck.ps1 -Sec S22 -AllowNav -Fields 'Home|enrolment|Explore admissions|Application steps|Tuition|Funding options'` — ALL CHECKS PASS; parity 30/30. `-AllowNav` covers V1's two navigation landmarks, the breadcrumb and the local navigation; no global header, nav or footer. No `<h1>`; no form; four links per study to the same-variant `EDU-S01`, `EDU-S07`, `EDU-S16` and `EDU-S17`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term; no placeholder needed.
- Rendered and read at 1440. No corrections needed.
