# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S04` — Projects · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — one project spotlight whose name, location, type, introduction and context are bracketed placeholders, two reserved images of one verified project and never a person, no client, ownership, capacity or outcome named; the media counts per study (2, 2, 2, 2, 2) — are kept exactly. V1's `<details>` disclosure opens as a row because the register runs no script and folds nothing.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S04-001` | Universal / Safe | 001 Sunlit | 1 — the wide photograph above a split story | arc behind the head | Split head with the lead; a shallow 3:1 overview field on the lead rule; the spotlight beside a 4:3 detail field | 3:1 + 4:3 · 5 | 100 |
| `ENG-S04-002` | Premium / Editorial | 002 Terracotta | 2 — the portrait beside a narrow story | rise above the head | A 4:5 overview field beside the narrow story on the lead rule, the name at display size, a 1:1 detail field beneath | 4:5 + 1:1 · 5 | 100 |
| `ENG-S04-003` | Structured / Visual Modular | 003 Tidal | 3 — the narrative beside a stacked diptych | dot grid behind | A bordered plate with the story as a cell on the band tone beside the overview and detail fields stacked at 3:2 | 2 × 3:2 · 5 | 100 |
| `ENG-S04-004` | Conversion-led | 004 Daybreak | 4 — the wide view paired with the exploration panel | outline round *One place at a time.* | A 3:1 overview field; the spotlight beside a 4:3 detail field; the project-context row on the lead rule inside a band where V1 set its blue panel | 3:1 + 4:3 · 5 | 123 |
| `ENG-S04-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the asymmetric stage with a tall field and an offset story | margin bar along the display column | Display column beside a 4:5 overview field; the story as an offset band where V1 set its lime story, with a 4:3 detail field beside | 4:5 + 4:3 · 5 | 100 |

## What changed from V1

V1's rounded photographs, the blue exploration panel, the dark stage and the lime story panel go; the spotlight is a tracked label with the layers mark, the bracketed name in muted ink, location and type as a tracked line, the introduction and the project context opened as a row with the document mark; the fields are bare 8px areas labelled THE ARRAY and THE EQUIPMENT. The darkened surfaces are the 003 story cell, the 004 context band and the 005 story band. Copy is V1's throughout; no figure appears.

## Verification

- `engcheck.ps1 -Sec S04 -Fields 'Projects|A closer look|Energy takes shape|One place at a time|Look beyond the installation|Project spotlight|Project name|Location|Project type|A concise project introduction|Explore project context|Verified project narrative|Project overview|Installation detail'` — ALL CHECKS PASS; parity 70/70. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy outside placeholders; no claim term; five placeholders per study.
- Rendered and read at 1440. Correction: 004 context row moved into the panel rather than duplicated.
- Correction (22 September 2026): the 001 head rule that lifts children above the arc now excludes the arc itself (`> :not(.arc)`), so the arc stays absolute behind the headline instead of taking a grid cell.
