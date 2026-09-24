# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Beauty, Wellness & Spa` · Prefix: `WELL` · Section: `WELL-S25` — Article / Insight Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, WELL translation in `../WELLNESS-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the rule — reserve the article, author the apparatus — the measures declared in `ch`, the captioned figures, the omitted citations and the `<nav>` permitted only in `003` are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Composition | Measure | Words |
| --- | --- | --- | --- | --- | ---: | ---: |
| `WELL-S25-001` | Universal / Safe | 001 Linen & Olive | 1 — apparatus column beside the measure | Sticky ruled apparatus; reserved title, standfirst, body blocks and sub-heads; a captioned 16:10 figure held to the measure; limits; related reading as reserved title lines | 66ch | 133 |
| `WELL-S25-002` | Premium / Editorial | 002 Bone & Clay | the column alone | Ruled kicker, reserved title at display scale, body blocks, a reserved pull-quote with the accent glyph, two ruled notes; no media | 58ch | 73 |
| `WELL-S25-003` | Dense / Information-heavy | 003 Mist & Moss | sticky ledger + contents nav + ruled policy | Ledger with correction date; ON THIS PAGE as a named nav of reserved heading bars; four reserved sections of uneven length; footnote area; policy as a ruled three-column row | 64ch | 132 |
| `WELL-S25-004` | Conversion-led | 004 Sand & Ochre | captioned plate + ruled two-column close | 21:9 lead figure with figcaption; reserved title and body; the treatment action beside the refusal list; limits on the foot | 64ch | 192 |
| `WELL-S25-005` | Sector-native / Distinctive | 005 Ivory & Plum | hairline paper sheet, centred | The piece as the printed sheet: ruled head with GIVEN OUT SINCE, reserved title and body, the limits as the sheet's foot rule; two ruled notes beneath | 62ch | 161 |

## What changed from V1

Panels, the stone ground and the metadata kicker blocks are gone; the apparatus is ruled ledgers, tracked labels and bordered slots. Reserved prose is drawn as flat media-tone blocks at prose cadence — long, medium, short — so line length and rhythm can be judged before a word exists, which is the only thing this page can be judged on. `005` keeps the sheet as a paper cell with 1px edges.

## Verification

- `wellcheck.ps1 -AllowNav` — ALL CHECKS PASS; parity on "medical advice" and "Skin" 10/10. `<nav>` appears only in `003`, with an accessible name. Every `<figure>` carries a `<figcaption>`. No digit in visible copy beyond indices and ratio labels; no newsletter field, product or sponsored label.
- Rendered and read at 1440. Correction before sign-off: `005` sheet and notes carried max-width on bordered elements — the measure moved to a wrapper column.
