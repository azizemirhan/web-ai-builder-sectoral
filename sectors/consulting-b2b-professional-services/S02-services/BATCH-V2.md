# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S02` — Services · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — six situations, not six capabilities; the sentence first and the discipline as its label; generic vocabulary only; the media counts and shapes per study (A, A, C, A, A); no named client, logo, ranking or figure — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S02-001` | Universal / Safe | 001 Paper & Indigo | 1 — narrow intro + wide grid | ghost serif ampersand behind the intro | Intro column with the pencil rule and the italic *situations*; three-up grid of six bare 4:3 fields with serif titles, one sentence and a bare `↗` route each; ruled foot with V1's closing line and the bordered action | 6 × 4:3 | 131 |
| `CONS-S02-002` | Premium / Editorial | 002 Sable & Bronze | 2 + the rail | pencil ellipse round *sell* | Head split at the baseline; a CSS snap rail of six tall 3:4 fields, the next peeking past the frame; ruled foot with the underlined route. V1's arrow-button script removed — no JavaScript in the pass; the rail scrolls natively | 6 × 3:4 | 112 |
| `CONS-S02-003` | Structured / Visual Modular | 003 Field & Emerald | 3 — bordered cell grid | ruled margin behind the grid | Head cell with the pencil rule; six cells with serif italic word-numerals *One … Six* and a plus mark, the sentence at reading weight and the discipline as a bordered chip; band-tone foot cell with the question and the bordered action | none, by V1's reasoning | 107 |
| `CONS-S02-004` | Conversion-led | 004 White & Signal | 4 + the featured item | underline stroke under *what to call it.* | Featured item on the band tone with the pencil rule — 3:2 field, START HERE chip, serif title, note and the one action — beside a bordered column of five compact 1:1 items; ruled foot with the closing line and the underlined route | 1 × 3:2 + 5 × 1:1 | 149 |
| `CONS-S02-005` | Art-directed / Distinctive | 005 Chalk & Violet | 8 — offset gallery | bracket grouping the head column, ghost word-numeral *Six* | Narrow head column with the italic *out loud* and the bordered action; six 1:1 fields on three columns with the middle column dropped, serif titles. V1's near-black ground becomes chalk | 6 × 1:1 | 102 |

## What changed from V1

Cards with 14–26px radii, pills and dashed edges become bare flat fields with slate labels, serif titles and hairline structure; word-numerals replace `01–06`; the `002` script is gone. Copy is V1's throughout with two recorded rewordings: `004` "the pill under it" → "the label under it" (the register has no pills), and `005` two columns → three offset columns (design layer only; the six items and their order are V1's). Slates read `AT WORK · ratio` — the honest subject is the team on that kind of engagement, never a desk or a skyline.

## Verification

- `cslcheck.ps1 -Sec S02 -Fields '<six discipline names>'` — ALL CHECKS PASS; parity 30/30. No `<h1>`; no header/nav/footer; no form; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder element (none carried); no claims vocabulary.
- Rendered and read at 1440. Corrections: `004` and `S01-004` underline spans set `inline-block` so the stroke draws under the whole phrase; `005` gallery moved from two to three columns and cells set `align-content: start` (height 1888 → 1107).
