# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S02` — Construction Services · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — every service carries the delivery marker (self-delivered / managed / joint), the turn-down position, no figure, price, lead time, certification, client or project name, per-service media reserved — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Media | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S02-001` | Universal / Safe | 001 Site White & Safety Orange | 8 — mixed-ratio gallery | cutting-plane line with arrowheads behind the head | Featured 21:9 field with tape bar and a name + marker chip on a paper plate; five 3:2 fields in a hairline grid with the same tag and a one-line description on a hairline; the sixth cell WHAT WE TURN DOWN as a bordered note with a cone icon | 6 fields | 155 |
| `CON-S02-002` | Premium / Editorial | 002 Bone & Burnt Amber | 9 — chapter pacing with giant index | levelling staff down the left margin | Four ruled chapters: index 01–04, a 16:10 field swapping sides, a centred column with the marker as a bordered iconed chip spelling out who, the name and one sentence; turn-down line on the foot rule | 4 fields | 195 |
| `CON-S02-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 — bordered cells as a twelve-column mosaic | datum line with level triangles behind the head | Seven tiles at 6/4 columns (2:1 and 3:2 fields) grouped BELOW GROUND / STRUCTURE & ENVELOPE / INSIDE, each with zone eyebrow, name, line and iconed marker; three-cell marker legend under a tape bar | 7 fields | 153 |
| `CON-S02-004` | Conversion-led | 004 White & Hi-Vis | 6 — ruled decision sheet | dimension line with running offsets | Display with hi-vis tape underline; 16:10 field beside WE ARE RIGHT FOR THIS (tape rule, iconed rows) and ASK SOMEBODY ELSE (muted rows); six-cell bordered ledger of services with marker chips; one bordered action with a phone icon | 1 field | 141 |
| `CON-S02-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 6 ×3 — ruled sheets with giant index | I-beam section outline behind the head | Services sorted by marker: OURS / JOINT / BOUGHT IN as three ruled columns with index, display-scale icon, definition and four ruled rows; 21:9 field of our own gangs with tape bar; WHAT WE WILL NOT TAKE ON as three indexed lines beside the checkability note | 1 field | 222 |

## What changed from V1

The gradient placeholder fills, dark tiles with veils, floating white card and cinematic stage of V1 rev 2 are gone; every field is a flat paper-darkened area with a tracked label, and the marker is a stroke icon (hard hat, clipboard, overlapping squares) wherever it appears. `005`'s twelve descriptions are cut to one clause each so the study sits under the 250 ceiling (V1 was well over it); its structure and argument are unchanged, and "specialist guaranteed" is dropped from the roofing line.

## Verification

- `concheck.ps1 -Sec S02 -Fields 'What we are hired to do|Groundworks'` — ALL CHECKS PASS; parity 10/10. No `<h1>`; no header/nav/footer; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy beyond ratio labels and indices; no claim from the CON list.
- Rendered and read at 1440. Corrections: `001` turn-down note inherited the cell hairline (reset); `002` fields 3:2 → 16:10 and columns centred against the field (rows were top-heavy); `003` tiles 3:2/4:3 → 2:1/3:2 for height; `005` trimmed 303 → 222 words and the I-beam figure brought inside the frame.
