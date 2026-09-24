# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S26` — Person / Profile Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the load as the firm's countable facts; the commitment naming all five stages with the first ninety days shared; no fabricated qualification, registration, membership, award or handle, and the line saying so; the portrait labelled by role and never by the placeholder name; the plain `data-region="page-context"` block with the one `<h1>`; team names, counts, days and dates as placeholder demo values; the media counts per study (1, 0, 1, 0, 0) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S26-001` | Universal / Safe | 001 Paper & Indigo | 1 as a profile | ghost word-numeral *Two* — the load — behind the name | Role as the eyebrow, the placeholder name as the h1, what they work on, the commitment on the pencil rule, beside the 4:5 portrait field labelled by role; THE LOAD as a bordered row with the counts as word-numerals; ATTACHED TO as a ruled list, the written one with the retraction note on `--no`; foot | 1 × 4:5 · 8 | 157 |
| `CONS-S26-002` | Premium / Editorial | 002 Sable & Bronze | 2 in one measure | pencil ellipse round *operating model* | The role as the h1 at display size and the name as its caption — you are sent here by role; the commitment on the pencil rule; the load as three serif lines with the counts in the accent italic; attached-to; the close. No portrait, by V1's argument | none · 8 | 164 |
| `CONS-S26-003` | Structured / Visual Modular | 003 Field & Emerald | 3 — the commitment at stage resolution | ruled margin behind | Identity with the commitment beside; HOW MUCH OF THEM, BY STAGE as a bordered strip of five with roman numerals, the shared fifth on the band tone with the pencil rule; the not-listed line and the ask; rail with the load, attached-to and the 4:5 portrait field. No sticky rail | 1 × 4:5 · 11 | 200 |
| `CONS-S26-004` | Conversion-led | 004 White & Signal | 4 — do not take it on trust | underline stroke under *on trust* | Identity and commitment; the load and attached-to as two ruled columns; DO NOT TAKE ANY OF THAT ON TRUST as a band with the pencil rule and three bordered checks led by word-numerals; foot. No portrait, by V1's argument | none · 8 | 205 |
| `CONS-S26-005` | Art-directed / Distinctive | 005 Chalk & Violet | 5 — no biography | bracket grouping the revision record | Identity with V1's no-career-history line; WHAT THEY HAVE CHANGED THEIR MIND ABOUT as a bracketed pair at display size — STILL HOLDS with a tick, CHANGED THEIR MIND on the `--no` edge with a struck seal and the read-it link; the commitment on the pencil rule beside the load; foot with attached-to and the ask | none · 9 | 222 |

## What changed from V1

The load's counts become serif word-numerals in the accent italic, still marked as placeholders; the stage numbers in 003 and the check numbers in 004 are roman numerals and word-numerals. The retraction note carries the `--no` edge and struck seal wherever the written piece is listed. Cards, filled panels and the badge row go; the darkened surfaces are the 003 rail and shared stage and the 004 band. Copy is V1's throughout.

## Verification

- `cslcheck.ps1 -Sec S26 -AllowClaims ' award' -Fields 'Partner, operating model|A. Whitfield|who decides what|all five stages|R. Adeyemi|Never three|last month|reference calls|Operating model redesign|No qualifications, memberships or awards|Ask for them by name'` — ALL CHECKS PASS; parity 55/55. The one allowed term is V1's own line that no awards are listed. Placeholders declared in every study. One `<h1>` per study; no header, nav or footer element; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder; no credential, handle or career history.
- Rendered and read at 1440. One correction: the 001 ghost glyph replaced with the ghost word-numeral, which reads in the serif at that size.
