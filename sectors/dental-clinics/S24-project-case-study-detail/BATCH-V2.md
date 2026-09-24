# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S24` — Project / Case Study Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the page's `<h1>`, the pending notice, four bracketed chapter placeholders and the care-involved line all marked `data-placeholder`, no patient material, no before or after, the two disclaimers, one primary action to the contact study and one secondary to the service detail; the media counts per study (3, 3, 5, 3, 3) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S24-001` | Universal / Safe | 001 Chalk | 1 — the opening diptych over a paired narrative | ring behind the h1 | Two 3:2 fields; ONE and TWO as ruled chapters; the review room at 3:1; THREE and FOUR as ruled chapters; CARE INVOLVED on the lead rule with the disclaimers on the plum edge; two actions | 2 × 3:2 + 3:1 · 6 | 174 |
| `DN-S24-002` | Premium / Editorial | 002 Linen | 2 — the editorial opening with alternating chapters | arc above the h1 | The consultation room edge to edge at 21:9 captioned *Understanding the starting point.*; two ruled chapters; two 3:2 fields under *What happened. What remains.*; two ruled chapters; care involved on the lead rule; two actions | 21:9 + 2 × 3:2 · 6 | 178 |
| `DN-S24-003` | Structured / Visual Modular | 003 Slate | 3 — five field-led chapters as one plate | dot grid behind | One bordered plate of five rows on ink seams, each a 3:2 field beside its chapter, the fields alternating sides, the fifth holding CARE INVOLVED and the disclaimers on the plum edge; two actions on the lead rule | 5 × 3:2 · 6 | 193 |
| `DN-S24-004` | Conversion-led | 004 Daylight | 4 — case context beside a vertical narrative | bar under *treatment decision* | A sticky context column with the h1, the chip, the disclaimers on the plum edge and care involved; a vertical narrative of three 2:1 fields and four ruled chapters with *Your starting point may be different.* as an inline band holding the two actions; V1's follow-up note on the plum edge | 3 × 2:1 · 6 | 197 |
| `DN-S24-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — the oversized opening with offset frames | corner marks framing the h1 | Two 3:1 frames offset — flush then indented; the four chapters as a ruled spine with word-numeral labels in the left column; a third indented 3:1 frame; care involved on the lead rule with the disclaimers on the plum edge; two actions | 3 × 3:1 · 6 | 174 |

## What changed from V1

The pending notice becomes a plum-bordered chip and the two disclaimers sit on the plum edge in every study — the case is a refusal to promise, and the token says so. Bracketed placeholders print in muted ink so they read as placeholders; the fields are settings and roles, never a mouth or a result. Word-numerals count the chapters. The darkened surfaces are the 004 inline band only. Copy is V1's throughout.

## Verification

- `dncheck.ps1 -Sec S24 -Fields 'not a typical result|Case account pending|The starting point|A considered approach|Care, in stages|At the follow-up|Care involved|not a prediction of your own care|do not demonstrate a treatment outcome|Discuss your own questions|Explore a first consultation'` — ALL CHECKS PASS; parity 55/55. One `<h1>` per study; no header/nav/footer; no form; two links per study; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no outcome, name or claim term; six placeholders per study.
- Rendered and read at 1440. One correction: the 004 inline band squeezed its sentence beside the two actions and the 3:2 frames ran the column long — the band now stacks and the narrative fields are 2:1.
