# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S21` — Subpage Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — it must fail as an `S01`: no counter, no figure, no viewport height, no claim about the firm; the page description describes the page; the title reserved as a labelled fill and never an em-dash; the four metadata slots; at most one in-page action, in `004`; no refusal region; media at interior scale where carried — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S21-001` | Universal / Safe | 001 Site White & Safety Orange | 2 at interior scale | dimension line with ticks under the title fill, measuring the room the name has | Iconed parent label; the reserved title as a labelled fill of two flat bars in the media tone at display height; the description beside; a bordered four-cell metadata rail with a stroke icon each (sector / status / contract / reference) under the tape; one reserved photograph at 3:1 | 1 field, 5 slots | 83 |
| `CON-S21-002` | Premium / Editorial | 002 Bone & Burnt Amber | 7 at interior scale | small levelling circle behind the head | Reading column with the parent label, the title fill of three bars at a longer measure and the description in two paragraphs, beside a tape-topped bordered margin ledger of iconed metadata slots; no media | 0 fields, 5 slots | 102 |
| `CON-S21-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 at interior scale | dimension line across the sheet head | Bordered hero sheet — title fill, description and a four-cell metadata row beside a 4:3 reserved photograph; THE SAME SLOTS ON THE OTHER FOUR INTERIOR PAGES as four bordered cells with page icons (crane / badge / office / document), ruled ledgers of the re-labelled slots, MEDIA KEPT / DROPPED chips and the dropped fourth slot marked as dropped | 1 field, 5 slots | 296 |
| `CON-S21-004` | Conversion-led | 004 White & Hi-Vis | 4 at interior scale | — (tape edge above the title fill) | Parent label; the title fill under a hi-vis tape edge; the description, one bordered in-page action with a down-arrow icon and the sentence explaining why it is the only one; band-tone bordered metadata ledger row with icons; no media | 0 fields, 5 slots | 92 |
| `CON-S21-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 9 at interior scale — the title drawn as three measures | the dimension lines under each measure are the drawing layer | The reserved title as three flat bars at display height — A SHORT NAME, A LONG ONE, WHERE IT WRAPS — each with its own dimension line, ticks and tracked label; the description and the argument for the measures beside a bordered iconed metadata ledger; no media | 0 fields, 5 slots | 131 |

## What changed from V1

The reserved title is drawn as the register's bare flat bars in the media tone with a tracked caption and, where the study measures it, a dimension line with ticks beneath; the parent label carries a stroke icon; the metadata slots are bordered cells or ledgers with an icon each, keeping V1's "Reserved" word rather than a dash; media stays at interior scale (3:1, 4:3) or is dropped as V1 dropped it. The title element is the page's `h1` in every study. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S21 -Fields 'Project name|Job reference|Form of contract'` — ALL CHECKS PASS; parity 15/15. One `<h1>` per study (the subpage hero carries the page title); no header/nav/footer; no form; no viewport-height unit; no counter, figure or digit; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; the anchor in `004` only, in-page; no `data-refusal` block, by the section's rule.
- Rendered and read at 1440. Corrections: `005` dimension spans set to block with unwrapped labels.
