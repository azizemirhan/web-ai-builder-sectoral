# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S26` — Person / Profile Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — will this person be on my job, and what happens the week they are not; what they settle and what they must ring about; what is only in their head and what is written down; name, jobs at once, telephones and cover reserved; no credential, count, quotation, biography or social handle; portrait and name paired in one figure; `002` without a portrait; anchors in `004` only — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S26-001` | Universal / Safe | 001 Site White & Safety Orange | 3 with 7 — figure, cells and columns | setting-out grid behind the head | The portrait as a bare 4:5 field in one figure with the reserved name, post and jobs-at-once as a bordered caption ledger, beside WHAT THE POST COVERS; HOW OFTEN as three bordered cells with clock / calendar / stop icons; SETTLES and HAS TO RING as two columns, the second red-edged on the band tone; three iconed absence cells (case / cross / exchange) and a tape-topped written-down list; routes ledger beside the red-topped refusal | 1 portrait, 7 slots | 814 |
| `CON-S26-002` | Premium / Editorial | 002 Bone & Burnt Amber | 7 — the handover note as the profile | levelling circle behind the head | A tape-topped bordered document sheet — header ledger of LEFT BY / FOR / REWRITTEN, an opening line, first-person ruled chapters with iconed eyebrows, the written-down list as a band-tone panel, and a signature ledger; three bordered cells beneath, the refusal red-topped. No portrait, by design | 6 slots | 677 |
| `CON-S26-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 — a week in the post | dimension line over the day bars | The figure (1:1 portrait + caption ledger) beside the head; five bordered banded day bars in five flat tones (your site in the accent, another site in grey, the office on the band tone, the road in the line tone, the half day something eats in ink) with a square-chip legend; two fortnight cells; settles / ring columns; three absence cells and the written-down list; routes beside the refusal | 1 portrait, 7 slots | 706 |
| `CON-S26-004` | Conversion-led | 004 White & Hi-Vis | 4 + 3 — who you should actually ring | chevron run behind the have-ready band | The figure beside the display with the tape underline; BEFORE YOU RING as a hi-vis band with three bordered iconed cells and two in-page actions; WHO YOU SHOULD ACTUALLY RING as a bordered four-row ledger with reserved numbers and the away row red-edged on the band tone; what they will tell you and the weeks away as two cells; red-topped refusal | 1 portrait, 6 slots | 899 |
| `CON-S26-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 9 — in their head against written down | cut-earth hatching down the left margin | A bordered two-column sheet: IN THEIR HEAD drawn as reserved measures behind a deep-red edge, WRITTEN DOWN as three iconed rows on the band tone behind the accent edge; three bordered answer cells; the smallest figure beside the routes ledger and the refusal | 1 portrait, 7 slots | 571 |

## What changed from V1

The two halves of the answer are drawn with one geometry across the batch — what is settled in ink, what has to be rung about behind a deep red (`--no`) edge, absence as case / cross / exchange icons — and the portrait, where carried, is a bare flat field inside a `<figure>` with the reserved name in its `<figcaption>` as a bordered ledger; the week in `003` is five flat banded bars with a square-chip legend; what is only in their head in `005` is reserved measures. Every reserved value reads *Reserved*. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S26 -Fields 'Name of the person|Number of jobs this person runs at once|Name of the person covering'` — ALL CHECKS PASS; parity 15/15. No `<h1>`; no header/nav/footer; no form; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit, credential, count, quotation or date; every portrait inside a figure with the name in its figcaption; `002` carries no portrait; the anchors in `004` only, in-page.
- Rendered and read at 1440. Corrections: `002` opening line width moved to `width: min()` (checker rule).
