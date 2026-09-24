# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S14` — Service Areas · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — a service area is not a circle, it is how far attendance survives; four bands described by what you lose; no miles, minutes, radius or pin; region, town and yard reserved; the map a reserved area only; we do not bid beyond the last band and will name a firm nearer — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S14-001` | Universal / Safe | 001 Site White & Safety Orange | 3 with 7 — bordered band sheets | setting-out grid behind the head | Tape-topped yard strip with the reserved location at counter scale; four bordered band sheets sharing one hairline system — index column with an attendance meter of filled and open squares that empties band by band, reserved region slots, three iconed fact cells (sunrise / low-loader / wrench) and WHAT YOU LOSE on the band tone, the refusal band with a stop octagon; the reserved map beside the no-pins note with muted tags | 1 map, 7 slots | 601 |
| `CON-S14-002` | Premium / Editorial | 002 Bone & Burnt Amber | 7 — the map argued with | levelling circle behind the head | The reserved map sticky at the size a finished page would give it, a struck-pin icon on its slate, and the argument as the reading column beside; four ruled band chapters with a margin index, centre prose and a bordered right-margin ledger of reserved regions with the attendance meter; the closing question in the display voice under the tape rule | 1 map, 6 slots | 697 |
| `CON-S14-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 — cells that widen as attendance degrades | dimension line with ticks behind the head; the same line under the sheet as a width scale | Twelve-column bordered sheet: band cells at three, four and five columns, the refusal at nine under the tape with the admission in the display voice on a tape-edged band, and the reserved map as the smallest cell beside it with the no-pins note; giant indices, attendance meters, reserved slots and iconed facts on hairlines | 1 map, 6 slots | 521 |
| `CON-S14-004` | Conversion-led | 004 White & Hi-Vis | 4 + 3 — hi-vis ask band, bordered ledger | chevron run behind the band | Display with tape underline; the ask as a hi-vis band with one bordered action (pin icon) and the small reserved map beside; three bordered iconed answer cells, the third on the band tone; the four bands as a bordered ledger row under a tape rule with indices, meters, one-line promises and reserved slots; ruled foot with muted tags | 1 map, 4 slots | 501 |
| `CON-S14-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 9 — the page steps darker | cut-earth hatching down the left margin through every tone | Four full-bleed bands stepping from paper through two flat greys to ink with paper type — discrete tones, no CSS gradient — each with a margin index and emptying meter, YOU LOSE one size larger than the last up to display, prose and a bordered ledger of reserved regions; no map; WHY THERE IS NO MAP HERE AT ALL as a bordered note with muted tags on the paper foot | 0 maps, 6 slots | 521 |

## What changed from V1

The four bands are drawn as the register's bordered sheets, ruled chapters, widening cells, ledger row or stepped tones, always with a word index, an attendance meter of squares that empties outward and a stop octagon for the refusal band; the mornings / plant / fitter facts carry a stroke-icon set (sunrise, low-loader, wrench); the reserved map is a bare flat field with a struck-pin slate wherever V1 reserved one, and absent where V1 refused one. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S14 -Fields 'Regions in band|Regions we do not cover' -AllowClaims guarantee` — ALL CHECKS PASS; parity 10/10. The allowed string is "no longer guaranteed the machine" in `005`, V1's words. No `<h1>`; no header/nav/footer; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy; no region, town, yard, distance, drive time, radius, pin or nationwide claim — every place name is a reserved slot with a visually-hidden label.
- Rendered and read at 1440. Corrections: word indices set at 2.9–3rem so THREE sits inside its column (`001`, `002`, `005`); `003` head dimension line dropped under the display; `005` foot heading aligned to the top of its cell.
