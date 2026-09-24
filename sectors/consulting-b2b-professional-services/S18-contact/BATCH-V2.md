# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S18` — Contact · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — a form is a way of not giving you an address, so no `<form>`, `<input>` or submit button anywhere; four routes, each naming who receives it; no map, social icon set, response-time promise or `info@` inbox; the three things that will not happen; the desk rather than the lobby as the only photographable thing; the name and address line in 005 as placeholder demo values; the media counts per study (0, 1, 0, 0, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S18-001` | Universal / Safe | 001 Paper & Indigo | 3 — bordered grid | ghost `@` glyph behind the head | Four routes as bordered cells on two columns, each led by its mark (speech / envelope / telephone / door) and closing on two labelled fields — WHO YOU GET on an accent edge, WHAT HAPPENS on a hairline; the *Not yet* cell edged in `--no` because it is the route out; the three refusals as a band with struck seals | none · 0 | 221 |
| `CONS-S18-002` | Premium / Editorial | 002 Sable & Bronze | 2 with a ruled row | pencil ellipse round *address* | Display statement with the voice line and V1's desk-not-lobby note beside; the desk as a full-width 3:1 plate with its slate label; the four routes across one ruled row, who you get in the ink over a hairline, what happens in the muted tone; band | 1 × 3:1 · 0 | 223 |
| `CONS-S18-003` | Structured / Visual Modular | 003 Field & Emerald | 3 with a closing strip | ruled margin behind | Head with the mast line and pencil rule; four bordered modules in one row, each closing on the same band-tone strip WHO RECEIVES IT — the last thing in the module, by V1's argument — the fourth strip edged in `--no`; the three refusals as a ruled foot | none · 0 | 230 |
| `CONS-S18-004` | Conversion-led | 004 White & Signal | 4 — the commitment first | underline stroke under *we do not chase* | V1's no-chase line at the largest size on the page as a band on the tinted paper with the pencil rule, the other two refusals and the no-form line as a marked list beside; FOUR ROUTES, AND WHO IS AT THE END OF EACH as one bordered row, the fourth cell edged in `--no`. No action rectangle — the route names are the actions | none · 0 | 218 |
| `CONS-S18-005` | Art-directed / Distinctive | 005 Chalk & Violet | 5 — the address is the artwork | bracket grouping the head column | The one named person at display size in the serif with the address line as a tracked caption, both placeholders, under the pencil rule; the desk as a 4:3 field beside; the other three routes as one ruled line each with who receives it in the ink; the three refusals as one closing line. The near-black ground of V1 becomes chalk | 1 × 4:3 · 2 | 185 |

## What changed from V1

The four routes carry one mark each across the batch — speech, envelope, telephone, door — and *Not yet* is the route edged in `--no` wherever it appears, because it is the one that ends with you leaving. The three refusals are struck seals in every study. Cards, filled strips and the dark 005 ground go; the strip in 003 is the paper darkened. Copy is V1's throughout; 005's name and address line keep their placeholder marking.

## Verification

- `cslcheck.ps1 -Sec S18 -Fields 'A first conversation|A direct address|A reference call|Not yet|we do not chase|does not add you to a list|budget, timeline or company size'` — ALL CHECKS PASS on every rule; parity 34/35, the one absence V1's own (`005` carries no route named *A direct address* because the named person **is** the address). Two placeholders in 005, declared; none elsewhere. No `<h1>`; no header/nav/footer; no form, input or button; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder.
- Rendered and read at 1440. Corrections: 002's desk resized from a 3:2 plate to a full-width 3:1 strip; 005's desk from 4:5 to 4:3; 004's band heading widened to break on two lines.
