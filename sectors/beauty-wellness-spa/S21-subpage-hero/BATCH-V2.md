# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Beauty, Wellness & Spa` · Prefix: `WELL` · Section: `WELL-S21` — Subpage Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, WELL translation in `../WELLNESS-DESIGN-DIRECTION.md` → *Detailing Pass*, read with the ARC rework notes for S21 (title / standfirst spine; contained strip; one contextual action; no metadata grid, dossier framing or folio apparatus). Supersedes `./BATCH-V1.md` for the design layer; the must-fail-as-S01 test is kept — no viewport unit, orienting voice, at most one action, page-name titles, no breadcrumb.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Composition | Height at 1440 | Words |
| --- | --- | --- | --- | --- | ---: | ---: |
| `WELL-S21-001` | Universal / Safe | 001 Linen & Olive | 2 — head split over a contained strip | Parent label and serif title left, standfirst right; a strip at fixed desktop height; closing line on the foot rule | 551 | 58 |
| `WELL-S21-002` | Premium / Editorial | 002 Bone & Clay | ruled sheet, no image | Parent label, serif title with an italic word, standfirst offset right, a hairline — the no-image variant | 280 | 33 |
| `WELL-S21-003` | Dense / Information-heavy | 003 Mist & Moss | reserved areas + one ruled line | Reserved title and standfirst areas at their scale; one hairline row of topic, kind, reserved date and author | 443 | 26 |
| `WELL-S21-004` | Conversion-led | 004 Sand & Ochre | head split with one action | Title and standfirst left, one bordered action right with the honest line; a 21:8 field beneath | 887 | 59 |
| `WELL-S21-005` | Sector-native / Distinctive | 005 Ivory & Plum | 5 — type crossing a field's edge | Serif title left, a short 21:9 field rising beside it, the standfirst crossing the field's left edge | 468 | 33 |

## What changed from V1

The dark ground of `004`, the mauve field of `005` and the panel framing are gone. `003`'s metadata is one hairline row rather than a rail block. `005` keeps V1's lesson — the title is too short to reach the picture, so the standfirst is what crosses — and does it with the register's overlap device rather than a tinted field. Every study stays well under a viewport at 1440.

## Verification

- `wellcheck.ps1` (one `h1` permitted for page-hero sections S21 and S22) — ALL CHECKS PASS. No `vh`/`dvh` unit; link count ≤ 1 per study (only `004` has one); no breadcrumb vocabulary; no digit in visible copy beyond ratio labels.
- Rendered and read at 1440. Corrections before sign-off: `003` reserved title area was an inline span with a height — made block-level; its metadata row lost the flagged max-width; `005` standfirst widened and pulled further right so it visibly crosses the field.
