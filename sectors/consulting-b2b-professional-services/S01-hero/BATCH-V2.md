# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S01` — Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — judgement has no photograph, so the only field is a portrait whose slate says what it is and never who; the firm's own counters as placeholder demo values, marked and declared; no named client, logo, ranking, award or measured figure; one `<h1>`; no header or navigation — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Reserved / placeholder | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S01-001` | Universal / Safe | 001 Paper & Indigo | 1 with 3 — proposition column, portrait, cell row | ghost serif question mark behind the head | Serif display with the italic *wrong* and the pencil rule; 4:5 portrait in a figure with a band-tone tab offset behind it and a one-person caption; the three counters as a bordered cell row in the serif with clock / document / house marks; one bordered action with a speech mark, one underlined route | 1 portrait, 3 placeholders (1998, 340+, 6) | 67 |
| `CONS-S01-002` | Premium / Editorial | 002 Sable & Bronze | 2 — head split at the baseline | pencil ellipse round *analysis* | Serif display left, the second voice as a serif italic statement right; the 21:9 portrait field given the whole frame; ruled foot with the underlined route and two serif counters on hairlines | 1 portrait, 2 placeholders | 63 |
| `CONS-S01-003` | Structured / Visual Modular | 003 Field & Emerald | 3 — bordered cell grid | ruled margin behind the grid | Proposition cell with the pencil rule across two columns, 1:1 portrait cell with a two-people caption; three practice bays with serif italic word-numerals *One / Two / Three*; band-tone foot row with the closing line, the counter and the bordered action | 1 portrait, 1 placeholder | 93 |
| `CONS-S01-004` | Conversion-led | 004 White & Signal | 4 — the band | underline stroke under *brief.*, circled *first* on the band eyebrow | Split head with a narrow 4:5 portrait and a telephone caption; band on the tinted paper with the pencil rule, three bordered cells sharing hairlines (one person / question in a circle / struck document in `--no`) and the one bordered action | 1 portrait, 0 placeholders | 88 |
| `CONS-S01-005` | Art-directed / Distinctive | 005 Chalk & Violet | 5 — display crossing the field edge | tall bracket grouping the statement column | Tall 4:5 portrait held left, the serif display beginning over its edge with the italic *sure*; the second voice as a serif italic statement; ruled foot with the bordered action, a hairline and the counter right-aligned. V1's midnight ground becomes chalk; the violet stays | 1 portrait, 1 placeholder | 51 |

## What changed from V1

The sector's voice is now the serif with one italic word in the accent, and a partner's pencil sits on every study — a ghost glyph, an ellipse, a ruled margin, an underline stroke, a bracket — one figure per study, none repeated. Pills, 14–26px radii, dashed slot edges and the dark 005 ground are gone; portraits are bare flat fields inside `<figure>` with a marked caption; counters are drawn in the serif at counter scale on hairlines rather than in boxes; actions are the thin-bordered rectangle with a leading mark or the underlined route with `↗`. Copy is V1's throughout, placeholder demo values included; the only added words are the figure captions under the portraits (four to six words each, slate-level labels naming what the field is), recorded here: 001 "The person who would run it", 003 "The team, not a stand-in", 004 "Who takes the call", 005 "Mid-sentence, not posed".

## Verification

- `cslcheck.ps1 -Sec S01 -Fields 'Start a conversation|Portrait area'` — ALL CHECKS PASS; parity 10/10. One `<h1>` per study; no header/nav/footer; no form; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a `data-placeholder` element; every study with placeholders declares them in `placeholder-data`.
- Rendered and read at 1440. Corrections: `001` figcaption stacked above the tab; `002` ellipse resized to the whole word; `003` word-numeral selector specificity; `004` portrait column narrowed so the head does not float.
