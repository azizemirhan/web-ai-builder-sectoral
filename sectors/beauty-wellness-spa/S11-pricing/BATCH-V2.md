# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Beauty, Wellness & Spa` · Prefix: `WELL` · Section: `WELL-S11` — Pricing · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, WELL translation in `../WELLNESS-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; V1's rule — the price is reserved, not omitted, with no currency, figure, duration, badge or discount — is kept exactly, as is the five-point axis of how loud the figure sits beside what it buys.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Composition | Fields | Slots | Words |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| `WELL-S11-001` | Universal / Safe | 001 Linen & Olive | 1 — column + grid | Sticky column with a 4:5 field beside four category groups across two columns as ruled name-and-price rows; ruled three-column policy row | 1 | 10 | 117 |
| `WELL-S11-002` | Premium / Editorial | 002 Bone & Clay | ruled rows, display serif | Five ruled rows with display-size serif names and a small labelled slot beneath each, beside a sticky 4:5 field; policy on the foot rule | 1 | 5 | 69 |
| `WELL-S11-003` | Structured / Visual Modular | 003 Mist & Moss | 3 — bordered cells | Three category cells sharing hairlines, each a 4:3 field and two-tier rows (name + slot, what happens beneath) | 3 | 8 | 194 |
| `WELL-S11-004` | Conversion-led | 004 Sand & Ochre | 4 — tinted band | Band with the promoted treatment, a large slot, one bordered action and a 16:9 field, beside ruled rows at list scale; policy bottom-aligned | 1 | 8 | 92 |
| `WELL-S11-005` | Art-directed / Distinctive | 005 Ivory & Plum | 6 — ruled sheet, giant serif | Six slots at display scale on a staggered two-column ruled grid, names as small tracked labels | 0 | 6 | 70 |

## What changed from V1

The chip is now a thin bordered rectangle at radius 2px, sized to the figure it will hold; the visually hidden "Price" label is unchanged. The cream promoted panel becomes a tinted band; `001` and `002` gain one media field each so the sheet sits beside a picture rather than standing alone; `003` opens each category with a field. Nothing was added that could read as a figure: a scan of visible copy for digits returns only indices and ratio labels, and for currency symbols returns nothing.

## Verification

- `wellcheck.ps1` — ALL CHECKS PASS; parity on "Deep cleansing facial" and "price paid" 10/10. Price slots per study: 10, 5, 8, 8, 6 — 37, all labelled.
- Rendered and read at 1440. Corrections before sign-off: `001` four groups stacked ran to 1230px — laid across two columns; `002` 21:9 field above five display rows ran to 1650px — field moved beside the rows as a sticky 4:5; `004` right column ended well above the band — columns stretched, policy bottom-aligned, field 16:9; `005` slots stretched to column width inside the flex cell — `align-self: flex-start`.
