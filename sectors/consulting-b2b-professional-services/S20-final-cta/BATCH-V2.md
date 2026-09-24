# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S20` — Final CTA · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — four reasons not to act, three of them agreed with; one ask, made once, as a statement with no link, button or form; no *ready to transform*, countdown, newsletter, chat prompt or second offer; nothing new, including no pictures; the decline ratio as a placeholder demo value — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S20-001` | Universal / Safe | 001 Paper & Indigo | 3 — bordered grid | ghost `×` behind the head, for the three refusals | Four reasons as bordered cells on two columns, verdict chips leading each — THEN DO NOT WRITE bordered in `--no` with a struck seal, THEN WRITE in the accent with a tick, that cell on the pencil rule; the ask as a band with a clock mark; foot line | none · 1 | 215 |
| `CONS-S20-002` | Premium / Editorial | 002 Sable & Bronze | 2 in one column | pencil ellipse round *reason* | Four ruled lines at display size, the verdict as a small tracked line in `--no` or the accent, the fourth reason in the accent italic; the ask as a band with the pencil rule; foot line | none · 1 | 209 |
| `CONS-S20-003` | Structured / Visual Modular | 003 Field & Emerald | 3 with no gap | ruled margin behind | Mast line; four modules as one bordered row with verdict chips, the WRITE module on the band tone; the ask directly beneath inside the same border with the pencil rule between, so it is what is left when three are agreed with; foot line | none · 1 | 216 |
| `CONS-S20-004` | Conversion-led | 004 White & Signal | 4 — agreement first | underline stroke under *good ones* | THE THREE WE AGREE WITH as a compact ruled list in the muted tone, each closing on THEN DO NOT WRITE; THE ONE THAT LEADS ANYWHERE as a band with the pencil rule, the reason at display size, the ask with a clock mark inside the band; foot line | none · 1 | 210 |
| `CONS-S20-005` | Art-directed / Distinctive | 005 Chalk & Violet | 5 — the empty field | bracket grouping the ask | The four reasons small along the top as a ruled row; V1's long empty field kept as bare paper between two hairlines; the ask alone at display size at the bottom under the pencil rule; V1's line about the empty space as the foot | none · 1 | 186 |

## What changed from V1

The verdicts become one device across the batch — a struck seal in `--no` for the three the firm agrees with, a tick in the accent for the one that leads anywhere — as chips or tracked lines; the ask carries a clock mark and stays a statement, never a button. Cards and filled bands go; every band is the paper darkened. Copy is V1's throughout; the decline ratio keeps its placeholder marking.

## Verification

- `cslcheck.ps1 -Sec S20 -Fields 'decision waiting|not your call|we are wrong|check us|One hour, with the person who would run the work|Nothing here is new|do not write|reference call'` — ALL CHECKS PASS; parity 40/40. One placeholder per study, declared. No `<h1>`; no header/nav/footer; no form, link or button; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder; no *ready to transform*, countdown or second offer.
- Rendered and read at 1440. One correction: the bordered display heading in 005 sized with `width: min()` rather than `max-width`.
