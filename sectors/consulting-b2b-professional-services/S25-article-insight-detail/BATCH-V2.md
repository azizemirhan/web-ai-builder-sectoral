# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S25` — Article / Insight Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the status note before the standfirst, the piece unchanged beneath it; the plain `data-region="page-context"` block with the title as the one `<h1>`; no reading time, view count, share counter, newsletter box, gate or lead image; publication and review dates, the author and the related titles as placeholder demo values; the policy line closing every study; the media counts per study (1, 0, 1, 0, 0) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S25-001` | Universal / Safe | 001 Paper & Indigo | 1 as an article | ghost `‡` — the correction mark — behind the note | The note as a held block on the `--no` edge with a struck seal beside the standfirst; context as a ruled row of four; body in a measure; RELATED; the policy line on the pencil rule; the author as a 4:5 field at the foot with the attribution | 1 × 4:5 · 6 | 170 |
| `CONS-S25-002` | Premium / Editorial | 002 Sable & Bronze | 2 in one measure | pencil ellipse round *wrong* | The note at the standfirst's size on the `--no` edge; one context line; three passages; RELATED; the policy line on the pencil rule and the attribution. No field | none · 6 | 161 |
| `CONS-S25-003` | Structured / Visual Modular | 003 Field & Emerald | 3 — body and rail | ruled margin behind | Body with the held note, standfirst, three passages and the policy line; rail on the band tone with the pencil rule — REVIEW HISTORY as dated chips, the last on the `--no` edge, DISCIPLINE, RELATED, the author as a 4:5 field. No sticky rail | 1 × 4:5 · 6 | 175 |
| `CONS-S25-004` | Conversion-led | 004 White & Signal | 4 — the piece, then the one ask | underline stroke under *tell us* | The note as a struck-seal line under the title; context row; body; IF YOU ACTED ON THIS, TELL US as a band with the pencil rule, a statement and not a form; RELATED and the policy line with the attribution | none · 6 | 187 |
| `CONS-S25-005` | Art-directed / Distinctive | 005 Chalk & Violet | 5 — the annotated piece | bracket grouping the margin | The original text unchanged in the main column; the firm's annotations in a bracketed margin, each led by the placeholder year as a chip and set in the accent italic; RELATED; the policy line on the pencil rule | none · 9 | 199 |

## What changed from V1

The note is one device across the batch — the `--no` edge and the struck seal, never a filled warning; *What we would write now* takes the accent as a heading; the author field is a bare labelled 4:5 area where it appears. Cards, filled panels and the badge go; the darkened surfaces are the 003 rail and the 004 band. Copy is V1's throughout; every placeholder keeps its marking, and the only digits on the page are inside them.

## Verification

- `cslcheck.ps1 -Sec S25 -Fields 'A central function should own the standard|We now think this was wrong|Central delivery becomes a queue|March 2019|June 2024|A. Whitfield|The argument|Where it broke|What we would write now|Nothing is taken down|decision rights|Cost programmes'` — ALL CHECKS PASS; parity 60/60. Placeholders declared in every study. One `<h1>` per study inside the page-context region; no header, nav or footer element; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder; no reading time, counter, newsletter or gate.
- Rendered and read at 1440. No corrections needed.
