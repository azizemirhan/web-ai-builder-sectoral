# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S01` — Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass* (the heavy reading: tracked-uppercase display, hairlines with one 3px tape bar, a drawing layer behind, a stroke-icon set in front). Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — what the firm builds, at what scale, what next; the counter reserved (founded / projects completed / people employed / largest project by value); no safety figure, award, client, price or urgency device; no global header — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Media | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S01-001` | Universal / Safe | 001 Site White & Safety Orange | 2 — head split + 3 — counter cells | dimension line with end ticks behind the head | Eyebrow with hard-hat icon; display; lead at the baseline; bordered action with clipboard icon + underlined route; 21:9 project field; three counter cells under a tape bar with figures at counter scale; position line | project 21:9 | 124 |
| `CON-S01-002` | Premium / Editorial | 002 Bone & Burnt Amber | 10 — tall field beside a standing column with offset tab | levelling circle with crosshair behind the column | 4:5 project field with tape on its top edge beside a ruled column: YEARS IN OPERATION as a tab on the rule, display, one paragraph, iconed actions, a ruled three-line list of what is built | project 4:5 | 86 |
| `CON-S01-003` | Dense / Information-heavy | 003 Steel & Structural Blue | 3 — bordered cells sharing hairlines | setting-out grid behind the whole sheet | Zoned sheet: head cell, WHAT WE BUILD cell with an icon per line, 16:9 project field over two columns, an actions cell with the position line and a WHAT TO SEND list, three counter cells | project 16:9 | 148 |
| `CON-S01-004` | Conversion-led | 004 White & Hi-Vis | 4 — tinted band | chevron run behind the band's right side | Head split with hi-vis tape underlining THREE THINGS; 3:1 project field; the enquiry as a tinted band with hi-vis tape, three iconed underlined native fields and one bordered action; four-cell counter ledger incl. LARGEST PROJECT BY VALUE; the no-budget line | project 3:1 | 142 |
| `CON-S01-005` | Sector-native / Distinctive | 005 Asphalt & Signal | 5 — type crossing the media edge | cut-earth hatching along the foot | 21:9 plant field with tape on its bottom edge; GROUNDWORKS & CIVILS at the section's largest size on a paper plate crossing the field's edge; a ruled row of statement, LARGEST PROJECT BY VALUE at the largest counter scale, iconed actions and an also-list | plant 21:9 | 103 |

## What changed from V1

The gradient hero, the pills, the shadows and the black-and-white-only rule of the earlier V2 language are gone (superseded in the design direction). Every study now runs on paper with one accent, a tracked-uppercase display and hairlines; every figure sits in a bordered slot at counter scale rather than a small inline dash; every action carries a stroke icon; every study has one construction-drawing figure behind it and no two studies share one. `004` keeps its three-question form (`-AllowForm`) because V1's hero is the enquiry; hi-vis yellow appears only as tape (the top rule and the underline), never as a ground.

## Verification

- `concheck.ps1 -Sec S01 -Fields 'Main contractor' -AllowForm` — ALL CHECKS PASS; parity 5/5. One `<h1>` per file; no `<header>`/`<nav>`/`<footer>`; no script, no remote dependency, no gradient, no shadow, no dashed border, no radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy beyond ratio labels; no claim from the CON list.
- Rendered and read at 1440. Corrections: `003` field 16:10 → 16:9 and a WHAT TO SEND list added to fill the actions cell; `004` highlight `<mark>` → thick tape underline (the block highlight collided with the 0.9 line-height); `005` eyebrow moved above the field, display given a paper plate so it reads across the tape bar, hatching shortened to the foot.
