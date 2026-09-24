# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S14` — Reports & Downloads · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — a gate is a price and each report says its price; nothing described as free; the six fields never asked for; what happens to an address; media only ever the report's own cover; titles as placeholder demo values; no form; the media counts per study (4, 0, 1, 4, 0) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S14-001` | Universal / Safe | 001 Paper & Indigo | 8 with the price on the cover | ghost serif at-sign behind the head | Four 3:4 cover fields with the price as a marked bordered chip crossing the field's top edge (tick / envelope / speech line), serif placeholder titles and terms; six never-asked fields as struck chips on a `--no` edge; the address paragraph as a band with the pencil rule | 4 × 3:4 · 4 | 194 |
| `CONS-S14-002` | Premium / Editorial | 002 Sable & Bronze | 2 as an editorial run | pencil ellipse round *price* | Four reports two to a row on hairlines, the price closing each as a marked line in the accent's italic with its terms; six struck chips; the address sentence in the serif italic as the foot | none · 4 | 178 |
| `CONS-S14-003` | Structured / Visual Modular | 003 Field & Emerald | 3 with a band field | ruled margin behind | The sort order as a mast line; 21:9 cover of the first report; four reports as a bordered row led by price chips; band-tone foot cell with the address paragraph | 1 × 21:9 · 4 | 185 |
| `CONS-S14-004` | Conversion-led | 004 White & Signal | 4 with the featured pair | underline stroke under *nothing from you* | Two ungated reports large with 3:2 covers, two costed smaller in bordered cells with 1:1 covers; struck chips; band with the pencil rule, V1's argument and the one action OPEN THE UNGATED TWO | 2 × 3:2 + 2 × 1:1 · 4 | 182 |
| `CONS-S14-005` | Art-directed / Distinctive | 005 Chalk & Violet | the form that does not exist | bracket grouping the head; six red strokes | The six never-asked fields in the serif at display scale, each struck through by a deep-red pencil stroke on its own hairline; V1's argument; four ruled reports with marked prices; foot line. The near-black ground becomes chalk | none · 4 | 178 |

## What changed from V1

The price is one system — tick in a circle (no gate), envelope (one email address), speech line (a conversation) — and the never-asked fields one refusal, struck in `--no` as chips or, in `005`, as display-scale strokes. Cards, badge pills and the dark 005 ground go. Copy is V1's throughout with one recorded change inside a placeholder title: "The stage-03 exits" → "The stage-three exits" (no-digit rule).

## Verification

- `cslcheck.ps1 -Sec S14 -Fields 'No gate|One email address|A conversation|Phone number|How you heard about us|The counterfactual problem'` — ALL CHECKS PASS on every rule; parity 29/30, the one absence V1's own (`003` names the fields in a sentence that omits the last). Four placeholders per study, declared. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit; no "free" or "exclusive".
- Rendered and read at 1440. No corrections needed.
