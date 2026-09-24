# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S07` — Safety Program · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — a programme is a set of standing decisions, each with who holds it and what it costs us; the stop sentence in every study; no incident rate, days-without board, zero-harm claim, certification number or scheme logo, and the page saying why — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Media | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S07-001` | Universal / Safe | 001 Site White & Safety Orange | 6 + 3 — lead sheet, bordered cells | setting-out grid behind the head | The stop authority as a bordered tape-topped sheet with a stop-sign icon and the sentence at display size beside a 4:3 field; six bordered decision cells with holder chips (hard hat = anybody, badge = a named role) and WHAT IT COSTS US on a tape edge with a clock icon; 4:1 field; bordered WHAT IS NOT ON THIS PAGE note | 2 fields | 676 |
| `CON-S07-002` | Premium / Editorial | 002 Bone & Burnt Amber | 7 — question rows at display size | levelling circle behind the proposition | Display proposition; 3:1 field; seven ruled question rows with the question at display size and the holder chip left, the answer and tape-edged cost right, the seventh (WHERE ARE YOUR NUMBERS?) carrying a cone chip; checkability line on the foot rule with a stop-sign icon; closing 3:1 field | 2 fields | 739 |
| `CON-S07-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 4 — phase bands | dimension line with running ticks behind the head | 4:1 field; three alternating phase bands under a tape rule, each with index and name at display size beside bordered decision cells (2 / 2 / 3 columns) carrying holder chips and COSTS US lines; bordered refusal strip | 1 field | 733 |
| `CON-S07-004` | Conversion-led | 004 White & Hi-Vis | 6 — ruled sheet with giant index | chevron run behind the foot | Display with tape underline; five ruled question rows with accent index, holder chip, our answer and tape-edged cost; DO NOT TAKE THESE ANSWERS FROM A WEB PAGE as a bordered tape-topped panel with one bordered action beside a 4:3 field; the sixth question on a ruled foot | 1 field | 671 |
| `CON-S07-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 5 — statement crossing the media edge | stop octagon behind the statement | ANYBODY ON THIS SITE CAN STOP THE WORK at the section's largest size, the second sentence in the accent on a paper plate crossing a 3:1 field's tape edge; six ruled requirement rows at display scale with holder chips in the margin and muted cost lines; 4:1 field; ruled NO FIGURE APPEARS ON THIS PAGE foot | 2 fields | 559 |

## What changed from V1

The deep ground of `004`, the heavy black rules of `005` and the colour panels of `001` are re-cut on paper with hairlines and one tape bar per study; the holder is a stroke-icon chip, the cost carries a clock icon, and the stop authority carries a stop-sign octagon in icon and drawing layer. Copy is V1's throughout; word counts equal V1's — the section is long-form by its content rule.

## Verification

- `concheck.ps1 -Sec S07 -Fields 'How the site is run|stop the work' -AllowClaims 'zero harm|incident rate'` — ALL CHECKS PASS; parity 10/10. The two allowed strings appear only in the refusal lists naming what is absent, as V1 wrote them. No `<h1>`; no header/nav/footer; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy beyond ratio labels and indices; no figure of any kind.
- Rendered and read at 1440. Corrections: `005` the statement's inline paper plates overlapped the line above at 0.86 line-height (the plate moved to the block-level second sentence only); `005` margin column widened so the holder chips do not wrap; `001`/`003`/`005` wide fields 3:1 → 4:1 for height; `003` phase-three cells set to three columns so the last cell does not sit alone.
