# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Beauty, Wellness & Spa` · Prefix: `WELL` · Section: `WELL-S18` — Wellness Resources · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, WELL translation in `../WELLNESS-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; every article title stays a reserved area sized to its scale, the date reserved, reading time and counts omitted, topics and kinds real, and the limits line ("none of this is medical advice") in all five studies.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | ---: |
| `WELL-S18-001` | Universal / Safe | 001 Linen & Olive | 3 — bordered cells | Three cells sharing hairlines: 16:9 field, kind, reserved title area, topic, PUBLISHED slot, read link | 3 fields · 3 titles · 3 dates | 138 |
| `WELL-S18-002` | Premium / Editorial | 002 Bone & Clay | ruled rows at display scale | Five ruled rows: margin column with index, topic, kind and date; reserved title area held to a 36rem headline measure at two-line / one-line heights | 5 titles · 5 dates | 114 |
| `WELL-S18-003` | Structured / Visual Modular | 003 Mist & Moss | 3 — cells + ruled legend | Three topic cells with two entries each; ruled three-column legend explaining the three kinds | 6 titles · 6 dates | 240 |
| `WELL-S18-004` | Conversion-led | 004 Sand & Ochre | 6 — ruled sheet with the statement as subject | The limits statement in serif at display size above one bordered action; a 16:10 field over four ruled entries | 1 field · 4 titles · 4 dates | 160 |
| `WELL-S18-005` | Art-directed / Distinctive | 005 Ivory & Plum | hairline cells as objects | Four paper sheets stepped down and right, overlapping by a sliver; two ruled notes beside; limits line on the foot rule | 4 titles · 4 dates | 178 |

## What changed from V1

Index cards, the dark legend ground and the oat ground under the pile are gone. `004` sets the disclaimer as the sheet's display statement rather than a bordered block. `005`'s sheets are paper cells with 1px hairline edges, stepped by offset only; the deep overlap that hid each sheet's topic and date was reduced so every sheet reads whole. `005`'s note about the words a wellness index lets in no longer quotes them, so the section's own claims scan stays clean.

## Verification

- `wellcheck.ps1` — ALL CHECKS PASS; parity on "medical advice" and "Published" 10/10. No newsletter capture, email field or gated download; no `<script>`.
- Rendered and read at 1440. Corrections before sign-off: `003` foot carried border and max-width on one element — measure moved to an inner span; `005` overlap reduced from 2.4rem to 0.7rem.
