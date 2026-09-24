# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S08` — Outcomes & Metrics · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — nobody runs the company twice, so the firm counts the work rather than the effect; five counts with one source each; the four refused figures named only to refuse them; every figure a placeholder demo value, marked and declared; the counting note with its year; the media counts per study (0, 1, 1, 1, 0) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S08-001` | Universal / Safe | 001 Paper & Indigo | 6 — the ruled sheet | ghost serif ellipsis behind the head | Top and bottom ink rules; the counting note as a mast line with a clock mark; five figure cells sharing hairlines, the serif figure at counter scale, label, note and a source chip (document / speech mark), the client-sourced cell on the band tone; V1's saturated panel as a band with the pencil rule and the four refused figures as struck chips on a deep-red edge | none · 6 | 208 |
| `CONS-S08-002` | Premium / Editorial | 002 Sable & Bronze | 2 with an editorial numeral field | pencil ellipse round *twice* | Head split with the counting note as the italic standfirst; five figures in a ruled two-column field at display scale with the source as a tracked label; a sticky 4:5 artefact column with the missing-number argument and the struck chips | 1 × 4:5 · 6 | 190 |
| `CONS-S08-003` | Structured / Visual Modular | 003 Field & Emerald | 3 with a band field | ruled margin behind | 21:9 artefact field; five-across bordered figure cells with source chips, the client cell on the band tone; band-tone foot cell with the argument and struck chips | 1 × 21:9 · 6 | 193 |
| `CONS-S08-004` | Conversion-led | 004 White & Signal | 4 with 3 — bordered row, band | underline stroke under *rather not print*; pencil ellipse round the live figure | Five figure cells with the fifth live on the band tone and its figure circled; 21:9 artefact band; refusal band with the pencil rule, struck chips and the one action ASK ABOUT THE 47, its figure a placeholder | 1 × 21:9 · 7 | 186 |
| `CONS-S08-005` | Art-directed / Distinctive | 005 Chalk & Violet | 3 with 6 — slots with a giant index | bracket grouping the head | Six bordered slots on three columns, figures at display scale, the sixth the hole — V1's `?,???` in the line tone on the band tone with UNKNOWABLE struck on a red edge; ruled foot with the argument and three struck chips. V1's near-black ground becomes chalk | none · 6 | 203 |

## What changed from V1

The refused four are drawn as struck chips on a deep-red (`--no`) edge in every study — line-through, red border, red ink — so the refusal reads as one device across the batch; figures are set in the serif at counter or display scale on hairlines rather than in boxes, sources as chips or tracked labels. "At stage 03 or before" is written "at stage three or before" (no-digit rule; recorded for all five). Figures keep V1's placeholder demo values; the `004` action wraps its figure in a placeholder span. The 005 dark ground goes. No other copy changed.

## Verification

- `cslcheck.ps1 -Sec S08 -Fields '<five labels>|Counted from' -AllowClaims 'satisfaction| roi '` — ALL CHECKS PASS; parity 30/30; six or seven placeholders per study, declared. The two allowed claim words appear only inside the struck refusal list, which is V1's content. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder element.
- Rendered and read at 1440. Correction: `001` ghost ellipsis lifted clear of the lead paragraph.
