# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S13` — Case Studies · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — a case study is WHAT WE FOUND / WHAT WE CHOSE / WHAT IT COST, never a before-and-after; every case names the one decision we got wrong; project, client, value and duration reserved; cost described, never counted; no outcome claim, no quotation — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S13-001` | Universal / Safe | 001 Site White & Safety Orange | 2 + 7 — case chapters as ruled sheets | setting-out grid behind the head | Two case chapters under the tape rule, each with a four-field reserved record row, a 3:1 project field with a slate label, three bordered FOUND / CHOSE / COST rows led by search / clipboard / clock icons, and THE ONE WE GOT WRONG as a tape-topped panel on the band tone; the refusal note as a bordered cell with muted tags | 2 fields, 8 slots | 797 |
| `CON-S13-002` | Premium / Editorial | 002 Bone & Burnt Amber | 7 — site log in reading order | levelling circle behind the head | One case told as a seven-entry site log: giant index on each ruled entry, a kind chip (FOUND / CHOSE / COST) as a bordered square, the wrong entry tape-topped and in the display voice, 3:1 fields opening and closing the log, reserved record as a margin ledger; the statement of practice as a closing chapter | 2 fields, 4 slots | 714 |
| `CON-S13-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 + 4 — discovery bands, bordered job cells | dimension line with running ticks behind the head | Four tinted bands, one per kind of thing found on site, each with an iconed head, a bordered job cell holding the reserved record and a 4:1 field, and CHOSE / COST as ruled lines; THE DECISIONS WE GOT WRONG collected into one tape-ruled band of three bordered cells at the foot | 4 fields, 12 slots | 754 |
| `CON-S13-004` | Conversion-led | 004 White & Hi-Vis | 4 + 3 — request band, index cells | chevron run behind the band | Display with tape underline; the ask as a hi-vis band with one bordered action and WHAT YOU GET as an iconed list beside a 3:1 field; four bordered index cells, one per case, each with the reserved record, a one-line FOUND and the wrong decision as a tape-edged line; foot line | 1 field, 8 slots | 405 |
| `CON-S13-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 9 — hierarchy inverted | cut-earth hatching down the left margin | Three ruled chapters each opening with WHAT WE GOT WRONG at display size under the tape rule, its cost and what changed beside, a 3:2 field, and AND THE REST OF IT at caption size as a bordered three-cell FOUND / CHOSE / COST row with the reserved record; the closing line at display size; ruled foot with muted tags | 3 fields, 9 slots | 675 |

## What changed from V1

The three-part structure is drawn as the register's bordered rows and cells with a stroke-icon set (search, clipboard, clock) and the wrong decision is always the tape-marked element — panel, entry, band, line or display headline by variant; the reserved record (project, client, sector, value) is a bordered slot row at ledger scale; project fields are bare flat media at 3:1 / 4:1 / 3:2. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S13 -Fields 'got wrong|asbestos|Project name'` — ALL CHECKS PASS; parity 15/15. No `<h1>`; no header/nav/footer; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy; no project, client, value, duration, outcome or quotation anywhere — every record field is a reserved slot with a visually-hidden label.
- Rendered and read at 1440. Corrections: `005` chapter paragraph rule scoped to `.top > div > p` so the field's slate label kept its own size.
