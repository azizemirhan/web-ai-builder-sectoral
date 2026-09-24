# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S05` — Methodology & Process · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — every stage names its exit; YOU GET and STOP HERE AND on every stage; the durations as placeholder demo values, marked and declared; the exits are policy commitments; the media counts and shapes per study (A, B, A, B, C) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S05-001` | Universal / Safe | 001 Paper & Indigo | 1 with 7's labelled captions | ghost word-numeral *Five* behind the head | Five stage rows on hairlines, the 3:2 field alternating side; each row a serif italic word-numeral, the duration with a clock mark, a serif title, the line and YOU GET / STOP HERE AND as two labelled fields with the exit red-edged (`--no`); ruled foot with the closing line and one action | 5 × 3:2 · 5 | 236 |
| `CONS-S05-002` | Premium / Editorial | 002 Sable & Bronze | 9's pacing — head, wide field, ruled stages, offset field | pencil ellipse round *stop* | Head split; 21:9 field; five ruled stages in a narrow column with word-numerals, labelled fields and the duration set right in the serif; a smaller 4:3 field offset right and sticky with a caption; underlined route | 1 × 21:9 + 1 × 4:3 · 5 | 219 |
| `CONS-S05-003` | Structured / Visual Modular | 003 Field & Emerald | 3 with a sticky index | ruled margin behind | Bordered index of five rows (word-numeral, stage, duration) held left and sticky, each an in-page route; five bordered panels stacked right with 16:9 fields, serif titles with the word-numeral inline, labelled fields with the exit red-edged; band-tone foot | 5 × 16:9 · 5 | 235 |
| `CONS-S05-004` | Conversion-led | 004 White & Signal | 4 with 3 — anchor field, bordered grid | underline stroke under *does not commit you* | 21:9 anchor field; five cells in a bordered three-then-two grid where the exit is the biggest thing — serif at reading-display size on a red edge, set before YOU GET — the first cell on the band tone with the pencil rule; ruled foot with V1's longer closing line and the one action START AT STAGE ONE | 1 × 21:9 · 5 | 229 |
| `CONS-S05-005` | Art-directed / Distinctive | 005 Chalk & Violet | 6 on a rail — sheets with a giant index | bracket grouping the head | CSS snap rail of five bordered sheets, the next peeking; each opens on the band tone with the word-numeral at display scale and the duration, then the serif title, the line and the labelled fields. V1's near-black ground becomes chalk; V1's arrow buttons and script are gone | none · 5 | 213 |

## What changed from V1

Numerals `01–05` become serif italic word-numerals, and the exit — V1's whole argument — carries the deep-red edge on every study. Cards become hairline rows, cells and sheets; the 005 dark ground and the rail script go. Copy is V1's throughout with two recorded rewordings for the no-digit rule: "Most engagements stop at 03" → "stop at stage three" (all five), and `004`'s action "Start at 01" → "Start at stage one". One added caption in `002` under the offset field: "The room, not the diagram". Durations keep V1's placeholder demo values (2 / 4 / 3 / 2 / 12 weeks; `003` index "wks").

## Verification

- `cslcheck.ps1 -Sec S05 -Fields 'Frame|Evidence|Options|Decision|Delivery|You get|A one-page decision statement|no sixth stage'` — ALL CHECKS PASS; parity 40/40; five placeholders per study, each declared. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder element.
- Rendered and read at 1440. Corrections: `001` alternating rows re-templated so the field keeps its column width on even rows and the field ratio moved to 3:2 (height 3152 → 2382).
