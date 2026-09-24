# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S05` — Capabilities · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the four-value holding marker on everything, the depth reserved and the consequence of reaching it real, the not-held list kept, no figure, percentage, rate, certification, operator card, client, project or safety record — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Media | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S05-001` | Universal / Safe | 001 Site White & Safety Orange | 3 + 9 — bordered cells in chapters | dimension line with running ticks behind the head | Four-cell iconed marker legend under the tape rule; three family chapters (TRADES / PLANT / TECHNICAL) each a ruled head, a 4:1 site field and bordered capability cells with marker chip, AT THE LIMIT line and reserved depth slot; bordered WHAT WE DO NOT HOLD note | 3 fields, 14 slots | 739 |
| `CON-S05-002` | Premium / Editorial | 002 Bone & Burnt Amber | 9 — chapters with standing essay | levelling circle behind the proposition | Display proposition and lead over a 3:1 site field; three ruled chapters of a sticky essay column beside a ruled register (name, marker chip, sentence, depth slot right-aligned); the gaps on the foot rule; 4:1 yard field | 2 fields, 11 slots | 649 |
| `CON-S05-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 — bordered columns by marker | setting-out grid behind the head | 3:1 site field; four bordered columns headed by icon at 2.4rem and definition, each a ruled register with family tags and depth slots, the column lengths reading the proportion; NOT HELD AT ALL as a full-width bordered strip with an accent head (V1's dashed rule replaced, the register has none) | 1 field, 14 slots | 507 |
| `CON-S05-004` | Conversion-led | 004 White & Hi-Vis | 4 — tinted band | chevron run behind the band | Display with tape underline beside a 4:3 site field; four-cell ruled marker row; the resource check as a hi-vis tape band with three iconed underlined selects and one bordered action; the no-booking line; not-held line | 1 field | 327 |
| `CON-S05-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 4 ×4 — alternating bands | cut-earth hatching down the left margin | Four full-width bands alternating paper and band tone under a tape rule, each with the marker at display size and icon, holdings as bordered tags, AT THE LIMIT on a tape edge, the depth at the largest counter scale and a 3:2 field swapping sides; NOT HELD in a hairline frame with tags | 4 fields, 4 slots | 436 |

## What changed from V1

The saturated marker columns, colour spines, dashed not-held strip and marker pills are gone; the marker is a stroke icon (hard hat, shovel, cycle arrows, clipboard) on a bordered chip, the depth a bordered slot at counter scale, and structure hairlines, bordered cells and tinted bands with one tape bar per study. Copy is V1's throughout ("calibrated" → "checked" in `003` to clear the claims scan's "rated" match); word counts equal V1's — the section is long-form by its content rule.

## Verification

- `concheck.ps1 -Sec S05 -Fields 'What we hold|Directly employed|Retained specialist' -AllowForm` — ALL CHECKS PASS; parity 15/15. No `<h1>`; no header/nav/footer; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy beyond ratio labels; no claim from the CON list.
- Rendered and read at 1440. Corrections: `001` family fields 3:1 → 4:1 and `002`/`003` lead fields 21:9 → 3:1 for height; `004` the band's drawing layer had been caught by the `> *` positioning rule and took space (excluded); `005` even bands were swapping order without swapping column widths (columns mirrored).
