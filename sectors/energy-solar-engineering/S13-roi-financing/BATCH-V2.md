# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Energy, Solar & Engineering` · Prefix: `ENG` · Section: `ENG-S13` — ROI & Financing · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, ENG translation in `../ENERGY-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — kicker and title kept as written, the investment summary, financing option and evaluation details bracketed placeholders, no cost, saving, payback period, return, rate, term, provider or offer named; no media in any study — are kept exactly. "Payback" and "savings" appear only inside V1's placeholders as the things a verified summary must state. V1's `<details>` disclosure opens as a row because the register runs no script and folds nothing. The five compositions follow V1's own five arrangements.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Plotted layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `ENG-S13-001` | Universal / Safe | 001 Sunlit | 1 — the open introduction beside the evaluation panel | arc behind the head | Head and lead in a left column; the story as a panel on the band tone beside, its evaluation row on the lead rule | none · 3 | 105 |
| `ENG-S13-002` | Premium / Editorial | 002 Terracotta | 2 — the editorial overview above a two-column narrative | rise above the head | The story in two columns on the lead rule — kicker with the title at display size, then the bracketed paragraphs and the opened evaluation row | none · 3 | 105 |
| `ENG-S13-003` | Structured / Visual Modular | 003 Tidal | 3 — the context panel paired with the introductory column | dot grid behind | A bordered plate: head and lead as an open cell beside the story cell on the band tone, its evaluation row on the lead rule | none · 3 | 105 |
| `ENG-S13-004` | Conversion-led | 004 Daybreak | 4 — the wide evaluation invitation beneath a compact introduction | outline round *Understand the assumptions.* | The story as a full-width band on the band tone — kicker and title beside the paragraphs, the evaluation row on the lead rule across the band | none · 3 | 105 |
| `ENG-S13-005` | Art-directed / Distinctive | 005 Night Current, inverted | 5 — the oversized statement above an offset panel | margin bar along the display column | The story as an offset band on the band tone, its evaluation row on the lead rule | none · 3 | 105 |

## What changed from V1

V1's warm panel, editorial overview, teal panel, blue invitation, lime panel and the plus-marked disclosure go; the story is V1's kicker as a tracked label with the layers mark, the title as type, the two bracketed paragraphs in muted ink and the evaluation disclosure opened as a row with the document mark and its bracketed placeholder. The darkened surfaces are the 001, 003, 004 and 005 story panels. Copy is V1's throughout; no figure, rate, term or offer appears anywhere.

## Verification

- `engcheck.ps1 -Sec S13 -AllowClaims 'payback' -Fields 'Bring the financial questions|Scope|Assumptions|Terms|Put the proposal in context|Project-specific investment summary|Available financing option|View evaluation details|Verified estimate source'` — ALL CHECKS PASS; parity 45/45. No `<h1>`; no header/nav/footer; no form; no link; no `<details>`; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit in visible copy; no claim term outside V1's placeholder ("payback" allowed there as a required disclosure item, not a claim); three placeholders per study.
- Rendered and read at 1440. Correction: the 001 head rule that lifts children above the arc excludes the arc itself (`> :not(.arc)`), applied across all ENG 001 studies.
- Correction (22 September 2026): 004 head widened and its display size reduced so the outlined phrase stays inside its column.
