# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S17` — Offices & Locations · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — an address is not an office, so each entry says what the place actually is; only the one floor is photographed; no map, pin, skyline, global-presence line or country count; cities, the desk count and the headcount as placeholder demo values; the media counts per study (1, 0, 1, 1, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S17-001` | Universal / Safe | 001 Paper & Indigo | 3 — bordered row | ghost word-numeral *One* behind the head | The four kinds on a mast line with a pin mark; four cells led by marked kind chips (house / struck house / envelope / chair in `--no`), placeholder cities in the serif, the office cell alone carrying a 4:3 field of the floor on the band tone; band with V1's no-map line | 1 × 4:3 · 6 | 204 |
| `CONS-S17-002` | Premium / Editorial | 002 Sable & Bronze | 2 with a ruled row | pencil ellipse round *office* | Four kinds across one ruled row, what the place is in the serif at display size with a mark, the placeholder city as the tracked caption beneath; band. No field, by V1's argument | none · 6 | 172 |
| `CONS-S17-003` | Structured / Visual Modular | 003 Field & Emerald | 3 with a band field | ruled margin behind | The arithmetic as a mast line; 21:9 field of the only floor; four modules in a bordered row narrowing with the substance (1.5 / 1.2 / 1 / 0.85), the type stepping down; band-tone foot cell | 1 × 21:9 · 6 | 180 |
| `CONS-S17-004` | Conversion-led | 004 White & Signal | 4 — the offer first | underline stroke under *near you* | V1's filled offer as a band on the tinted paper with the pencil rule and the one action TELL US WHERE THE WORK IS, beside the 3:2 floor; WHAT IS ACTUALLY AT EACH ADDRESS as a bordered row | 1 × 3:2 · 6 | 178 |
| `CONS-S17-005` | Art-directed / Distinctive | 005 Chalk & Violet | 5 — the plate crossing the field edge | bracket grouping the head | The only floor as a full-width 21:9 field with the office entry as a paper plate crossing its lower edge, the city at display size; the other three a ruled line each; foot line. The near-black ground becomes chalk | 1 × 21:9 · 6 | 184 |

## What changed from V1

The four kinds of address are one system across the batch — house, struck house, envelope, chair (the borrowed desk in `--no`) — as chips, marks or labels; the floor is a bare field at the size it is, never a skyline, and nothing resembling a map or pin is drawn. Cards and the dark 005 ground go. Copy is V1's throughout; cities, the desk count and the headcount keep their placeholder marking.

## Verification

- `cslcheck.ps1 -Sec S17 -Fields 'The office|No office|Registered address|London|Singapore|flew there'` — ALL CHECKS PASS on every rule; parity 29/30, the one absence V1's own (`004` carries no foot line). Six placeholders per study, declared. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder; no map, pin or country count.
- Rendered and read at 1440. No corrections needed.
