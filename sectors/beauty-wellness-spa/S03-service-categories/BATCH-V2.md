# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Beauty, Wellness & Spa` · Prefix: `WELL` · Section: `WELL-S03` — Service Categories · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, WELL translation in `../WELLNESS-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the four categories and their coverage lines are retained.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Composition | Fields | Words |
| --- | --- | --- | --- | --- | ---: | ---: |
| `WELL-S03-001` | Universal / Safe | 001 Linen & Olive | 1 — column + four-field row | Intro column; four 4:5 fields with tracked uppercase titles and one coverage line | 4 | 71 |
| `WELL-S03-002` | Premium / Editorial | 002 Bone & Clay | ruled rows + circular action | Typographic index: four ruled rows, very large serif names, a 1:1 field, coverage, circular arrow | 4 | 66 |
| `WELL-S03-003` | Structured / Visual Modular | 003 Mist & Moss | 3 — bordered cell grid | Two-by-two split panels: 4:5 field, category, coverage, a ruled three-line preview of treatments | 4 | 120 |
| `WELL-S03-004` | Conversion-led | 004 Sand & Ochre | 3 + 4 — cells + band | "What are you here for?" at publication size; four answer cells sharing hairlines; tinted fallback band with one action | 4 | 111 |
| `WELL-S03-005` | Art-directed / Distinctive | 005 Ivory & Plum | 5 — type crossing the media edge, cascaded | Four stepped columns, serif names crossing the top edge of 4:5 fields | 4 | 67 |

## Verification

- `wellcheck.ps1` — ALL CHECKS PASS; parity on the four categories and coverage lines 45/45.
- Rendered and read at 1440 and 390. Corrections: `003` cell rules leaked into the nested preview lists (`.cells li`) — scoped to direct children; `004` first and last cells had zero outer padding and therefore wider fields — padding equalised.