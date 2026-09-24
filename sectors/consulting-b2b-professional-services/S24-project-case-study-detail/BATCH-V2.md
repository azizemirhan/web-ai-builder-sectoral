# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S24` — Project / Case Study Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — *What we got wrong* at the weight of what we did; the redaction named rather than hidden; every field an artefact of ours and never the client's premises, people or product, each collapsing to its caption; the plain `data-region="page-context"` block with the one `<h1>`; no client name, sector, logo, testimonial, outcome or percentage; the media set and its per-slot purposes as recorded in BATCH-V1; length, team, interview counts, week numbers, the ninety days and the service link as placeholder demo values; the media counts per study (3, 1, 5, 1, 0) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S24-001` | Universal / Safe | 001 Paper & Indigo | 3 — bordered rows | ghost `?` behind the situation | Situation with the facts as a ruled row; the decision map as a 3:1 lead field; HOW IT RAN as a bordered row of three with word-numerals; the interview wall and the room as 2:1 fields; WHAT WAS DELIVERED on the pencil rule; WHAT WE GOT WRONG as a band on the `--no` edge; foot | 3 (3:1, 2:1, 2:1) · 5 | 215 |
| `CONS-S24-002` | Premium / Editorial | 002 Sable & Bronze | 2 in one measure | pencil ellipse round *stuck* | Situation at display size; facts as one line; three decision lines; delivered on the pencil rule; the ownership model on screen as a 2:1 field immediately before the errors with V1's caption; two error lines on the `--no` edge; close | 1 × 2:1 · 5 | 203 |
| `CONS-S24-003` | Structured / Visual Modular | 003 Field & Emerald | 3 — three tracks and the set | ruled margin behind | THE SITUATION, WHAT WE GOT WRONG (on `--no`) and WHAT WAS DELIVERED (band tone, pencil rule) as three bordered tracks; THE DOCUMENTED SET as five bordered 4:5 artefact cells with week chips and V1's lines; foot with the dates-as-evidence line | 5 × 4:5 · 10 | 245 |
| `CONS-S24-004` | Conversion-led | 004 White & Signal | 4 — is this evidence about you | underline stroke under the question | Situation beside the title; facts as a ruled row; the account as ruled lines with the errors on `--no` beside the decision map as a 4:5 field; delivered; IS THIS EVIDENCE ABOUT YOU? as a band with two verdicts — IT TRANSFERS with a tick, IT DOES NOT with a struck seal and the different-work link; foot | 1 × 4:5 · 6 | 215 |
| `CONS-S24-005` | Art-directed / Distinctive | 005 Chalk & Violet | 5 — the dated column | bracket grouping the column | V1's ordering line with the facts beside; the engagement as one ruled column of unknowns with week chips, the two weeks we got it wrong on the `--no` edge with struck seals; foot on the pencil rule with delivered, the still-unknown line and the service link. No field, by V1's argument | none · 11 | 224 |

## What changed from V1

The decision numbers become the serif word-numerals *One*–*Three*; the week markers stay as placeholder chips so the only digits on the page are declared demo values. The errors carry the `--no` edge and the struck seal in every study; the withheld line carries the same mark. Fields are bare, labelled by what the artefact is, never who is in it. Cards, filled panels and the gallery go; the darkened surfaces are the 001 band and the 003 delivered track. Copy is V1's throughout.

## Verification

- `cslcheck.ps1 -Sec S24 -Fields 'The strategy was agreed and nothing had changed|Signed off twice|Fourteen weeks|Three, one full-time|The tenth said what the ninth had|wrong sponsor|under-scoped the interviews|decision map, a redesigned ownership model|Two firms operate in it|Operating model redesign'` — ALL CHECKS PASS on every rule; parity 49/50, the one absence V1's own (`005` words the second error as *how many interviews it really needed*). Placeholders declared in every study. One `<h1>` per study inside the page-context region; no header, nav or footer element; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder; no client name, sector, logo, outcome or figure.
- Rendered and read at 1440. Corrections: the 001 fields set to 3:1 and 2:1 and the 002 field to 2:1 so the page reads without a screen of grey between the account and the errors.
