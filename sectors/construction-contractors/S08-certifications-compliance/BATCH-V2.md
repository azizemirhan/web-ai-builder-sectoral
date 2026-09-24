# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S08` — Certifications & Compliance · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the number goes where the logo would have been, every scheme name, registration number, body and date reserved, what it lets us do and what it does not cover real, the reader told to check the register, no logo, client, award or safety figure — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S08-001` | Universal / Safe | 001 Site White & Safety Orange | 3 — bordered cells | setting-out grid behind the head | 4 × 2 sheet under a tape rule: seven entries each led by the reserved number as a bordered slot at counter scale, iconed category, WHAT IT LETS US DO / DOES NOT COVER, and a small ruled record of three reserved fields; the eighth cell CHECK EVERY ONE OF THEM on the band tone with a search icon; WHAT NONE OF THIS TELLS YOU on the foot rule | 28 slots | 712 |
| `CON-S08-002` | Premium / Editorial | 002 Bone & Burnt Amber | 2 + 10 — essay beside a sticky ledger | levelling circle behind the head | Display and bold lead; the essay in three iconed ruled chapters beside THE REGISTRATIONS, a sticky tape-topped ledger of seven ruled rows with the reserved number at counter scale, a NOT COVERED line and two small fields | 21 slots | 556 |
| `CON-S08-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 6 — ruled sheet with giant index | dimension line with running ticks behind the head | WHAT WE DO NOT HOLD first as a bordered tape-topped note with a cone icon; six ruled register rows with accent index, iconed category and kind, the reserved number at counter scale, LETS US / DOES NOT COVER and a bordered mini-ledger of three reserved fields; two-column ruled foot | 24 slots | 610 |
| `CON-S08-004` | Conversion-led | 004 White & Hi-Vis | 3 + 4 — answer cells, tinted band | chevron run behind the band | Display with tape underline; three bordered answer cells (closed padlock / open padlock / cone); the compact register as a two-column ruled list with reserved numbers at counter scale and one-line caveats; SEND THE LIST as a hi-vis tape band with one bordered action; foot line | 6 slots | 455 |
| `CON-S08-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 6 — ruled rows at badge scale | north point behind the head | Two-sentence display, the second in the accent; six ruled rows under a tape rule, each led by the reserved number as a 5.2rem bordered slot at badge scale with two small fields under, the iconed category, kind and DOES NOT COVER on a tape edge beside; ruled two-column foot | 18 slots | 426 |

## What changed from V1

The card grid, the serif essay and the dashed / boxed field styling of V1 are re-cut in the register; the inversion — the reserved number set at the scale a logo would have been — is now literally the counter-scale bordered slot of the CON register, at its largest in `005`. Every category carries a stroke icon (clipboard, hard hat, shovel, portico, list, shield, badge) and every check line a search icon. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S08 -Fields 'The paperwork|Quality management|registration number'` — ALL CHECKS PASS; parity 15/15. No `<h1>`; no header/nav/footer; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy beyond indices; no scheme name, number, body, date or logo anywhere — every one is a reserved slot with a visually-hidden label.
- Rendered and read at 1440. Corrections: `003` slot width and `005` does-not-cover max-width moved off bordered elements (checker rule).
