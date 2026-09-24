# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Beauty, Wellness & Spa` · Prefix: `WELL` · Section: `WELL-S06` — Consultation / Booking · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, WELL translation in `../WELLNESS-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the request's fields, the not-booked-not-charged line and the what-happens-after list are retained.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Composition | Fields | Words |
| --- | --- | --- | --- | --- | ---: | ---: |
| `WELL-S06-001` | Universal / Safe | 001 Linen & Olive | 1 — column + working area | Intro column with a ruled what-happens list; the request as ruled rows with underlined fields | 0 | 125 |
| `WELL-S06-002` | Premium / Editorial | 002 Bone & Clay | 2 — head split | Serif statement; two-column underlined form beside a ruled what-happens list | 0 | 165 |
| `WELL-S06-003` | Structured / Visual Modular | 003 Mist & Moss | 3 — bordered cells | One form as three cells sharing hairlines with serif indices; one full-width action | 0 | 97 |
| `WELL-S06-004` | Conversion-led | 004 Sand & Ochre | 6 — ruled sheet | Accent index and serif invitation; one underlined field, one action, the not-asked line | 0 | 79 |
| `WELL-S06-005` | Art-directed / Distinctive | 005 Ivory & Plum | sentence form | The request as one serif sentence at display size with inline underlined controls | 0 | 171 |

## What changed from V1

The boxed form card, the black editorial hero, the saturated ground and the white pills are gone. Forms are native controls drawn as underlined fields on the paper with tracked micro-labels; the one action is a bordered rectangle. The register's form reference is `ARC-S19-001`–`004` (KEEP).

## Verification

- `wellcheck.ps1 -AllowForm` — ALL CHECKS PASS (form, input and button are permitted for this role only). No JavaScript; no action targets.
- Rendered and read at 1440 and 390. Correction: `001` what-happens list carried a rule and a `max-width` — replaced with a right margin.