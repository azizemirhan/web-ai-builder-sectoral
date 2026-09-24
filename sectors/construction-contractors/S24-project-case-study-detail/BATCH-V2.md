# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S24` — Project / Case Study Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the record worth having is the difference; the four classes of change with who decided and who paid; the fourth class is why the page exists; project, client, particulars and the client's words reserved; one photograph of the work in progress, never a pair; no value, duration, logo or "on time and on budget"; anchors in `004` only; no em-dash — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S24-001` | Universal / Safe | 001 Site White & Safety Orange | 3 with 7 — entry sheets | setting-out grid behind the head | Four bordered entry sheets sharing hairlines — class column with a stroke icon (search / exchange / pen / struck seal), the entry with its reserved particular as a bordered slot, and DECIDED BY / WHO PAID on the band tone, the fourth behind a deep-red edge; the client's words as the reserved quotation block beside the red-topped refusal; bordered four-slot record row; 3:1 reserved photograph of the work in progress | 1 field, 1 quotation, 8 slots | 590 |
| `CON-S24-002` | Premium / Editorial | 002 Bone & Burnt Amber | 7 — a publisher's correction | levelling circle behind the head | Four ruled chapters with iconed ordinals, centre prose, FOR WHAT THE DRAWINGS SHOWED, READ as a bordered slot line, and ON WHOSE AUTHORITY / PAID BY as an accent-edged margin cell, the fourth in deep red on the band tone; closing chapter beside a tape-topped record ledger with the reserved quotation as a taller slot | 8 slots | 598 |
| `CON-S24-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 — columns sized by how much there is to say | dimension line with ticks at the column widths | Four bordered columns sorted by who paid, the two client columns widest, nobody narrower, us narrowest behind a deep-red edge — each with a square payer chip (filled / open / red), class icon, the moment in tracked uppercase, the reserved slot and DECIDED BY on the band tone; bordered width note with the refusal; bordered five-slot record row | 9 slots | 526 |
| `CON-S24-004` | Conversion-led | 004 White & Hi-Vis | 4 + 3 — ask every firm for one | chevron run behind the ask band | Display with tape underline; hi-vis band with THE CHANGE REGISTER FROM A FINISHED JOB, the two useful answers as a bordered two-cell row with struck seals, one bordered action and its note; our register as a bordered four-cell row with payer chips, icons and reserved slots, the fourth red-edged on the band tone; red-topped suspicion note; tape-topped four-slot record row | 8 slots | 481 |
| `CON-S24-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 9 — the comparison done in text | cut-earth hatching down the left margin | Bordered two-column comparison sheet — WHAT WAS DRAWN in the muted tone, WHAT WAS BUILT, AND WHY in ink with the reserved particular inline and DECIDED BY, AND PAID BY on the band tone — with a 3px accent rule down the centre and the fourth row in deep red; two bordered cells for why this comparison and the missing phrase; bordered four-slot record row | 8 slots | 570 |

## What changed from V1

The four classes carry one icon set across the batch (search, exchange arrows, pen, struck seal) and the fourth class — we got it wrong — is always the deep-red-edged element; who paid is a square chip (filled for the client, open for nobody, red for us) or a band-tone cell; the reserved particulars are bordered slots reading *Reserved*, the client's words a reserved quotation block or slot, and the record a bordered ledger row. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S24 -Fields 'What this firm got wrong on this project|Project name|Handover file reference' -AllowClaims 'on time and on budget'` — ALL CHECKS PASS; parity 15/15. The allowed string is the phrase every study names as refused, V1's words. No `<h1>`; no header/nav/footer; no form; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit, value, duration, logo or pair of images; the anchor in `004` only, in-page; no em-dash placeholder.
- Rendered and read at 1440. No corrections needed.
