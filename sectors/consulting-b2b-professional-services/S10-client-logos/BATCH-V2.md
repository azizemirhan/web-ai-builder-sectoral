# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S10` — Client Logos · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — a logo wall shows the clients who did not mind; no logo is drawn, filled, approximated or placeheld; the four reasons for absence; the permissions note; client counts as placeholder demo values, marked and declared; the logo-area counts per study (8, 3, 8, 4, 6) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S10-001` | Universal / Safe | 001 Paper & Indigo | 3 — bordered cell wall | ghost serif double dagger behind the head | Three serif counts on a ruled row; a twelve-cell wall on six tracks — eight bare flat logo fields with a slate, four withheld cells on the band tone with a `--no` edge and a struck-seal tag; permissions note; foot with the statement and one action | 8 logo areas · 4 | 190 |
| `CONS-S10-002` | Premium / Editorial | 002 Sable & Bronze | 2 with 8 — three large fields | pencil ellipse round *show* | Display statement with its placeholder count; three large flat logo fields between ink rules; the permissions note in the serif italic; four reasons as a ruled red-edged list with marks; closing band with the pencil rule | 3 logo areas · 2 | 199 |
| `CONS-S10-003` | Structured / Visual Modular | 003 Field & Emerald | 3 as two declared blocks | ruled margin behind | MAY SHOW THE MARK with its count and a bento of eight flat fields at four sizes; MAY NOT with its count on the band tone behind a `--no` edge and the four reasons on hairlines; foot cell with the statement and the action | 8 logo areas · 5 | 195 |
| `CONS-S10-004` | Conversion-led | 004 White & Signal | 4 — the offer first | underline stroke under *your own problem* | V1's filled offer as a band on the tinted paper with the pencil rule, placeholder counts and the one action DESCRIBE YOUR SITUATION; a bordered row of four flat logo fields with the proof note; four reasons as a bordered red-edged row | 4 logo areas · 5 | 180 |
| `CONS-S10-005` | Art-directed / Distinctive | 005 Chalk & Violet | 8 as a sparse field | bracket grouping the head | One six-track hairline field, mostly empty: six small flat logo fields and four red-edged reasons placed across it, the counts and V1's foot paragraph in a band-tone cell. The near-black ground becomes chalk | 6 logo areas · 3 | 185 |

## What changed from V1

Logo areas are bare flat media-tone fields with a `CLIENT LOGO AREA` slate — never dashed, never a placeheld mark; the four reasons carry the deep-red edge and the struck-seal mark in every study; counts are serif figures or placeholder spans in running copy. Cards and the dark 005 ground go. Copy is V1's throughout; the counts keep V1's placeholder demo values.

## Verification

- `cslcheck.ps1 -Sec S10 -Fields 'Client logo area|A live transaction|A regulated process|They said no|written permission'` — ALL CHECKS PASS; parity 25/25; placeholders declared in every study. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder element; no name, mark or initial anywhere.
- Rendered and read at 1440. Correction: `005` field switched from a line-tone gap grid to hairline cell borders so the empty areas read as paper.
