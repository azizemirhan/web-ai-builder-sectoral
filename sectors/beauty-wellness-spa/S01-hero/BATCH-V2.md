# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Beauty, Wellness & Spa` · Prefix: `WELL`
- Section: `WELL-S01` — Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md` (derived from the Architecture
  KEEP set), translated for WELL in `../WELLNESS-DESIGN-DIRECTION.md` → *Detailing Pass*.
- Supersedes `./BATCH-V1.md` for the design layer. The role, the copy spine and the claims
  limits of V1 are retained; the composition, typography, colour and media treatment are
  rewritten.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Composition | Fields | Words |
| --- | --- | --- | --- | --- | ---: | ---: |
| `WELL-S01-001` | Universal / Safe | 001 Linen & Olive | 1 — narrow column + dominant field | Serif display with one italic word, lead, bordered action and text link; a tall 5:6 field; hairline foot with slate captions | 1 | 51 |
| `WELL-S01-002` | Premium / Editorial | 002 Bone & Clay | 5 — type overlapping the media edge | "A slower kind / of *beauty.*" at publication size crossing a 21:9 field; lead and text link beneath; an offset 4:5 still life | 2 | 35 |
| `WELL-S01-003` | Structured / Visual Modular | 003 Mist & Moss | 1 + 8 — column + mosaic | Intro column beside a four-field mosaic (lead field spanning two rows, two 4:3, one tall), each captioned with a treatment family | 4 | 41 |
| `WELL-S01-004` | Conversion-led | 004 Sand & Ochre | 6 — ruled sheet | Mast line, accent index `01`, serif display, a field inside the sheet, a ruled three-line list and one bordered action | 1 | 76 |
| `WELL-S01-005` | Art-directed / Distinctive | 005 Ivory & Plum | 3 — bordered cell grid | "THE LONG EXHALE" in tracked uppercase, right-aligned lead at the baseline, a two-cell grid sharing hairlines with ruled captions and a circular arrow | 2 | 37 |

## What changed from V1

- Pill buttons, 20px radii, tinted tile rails, centred stacks and a saturated full-bleed stage
  are gone. Every study now composes with bare flat fields, a serif display voice, hairline
  rules and one small accent.
- Copy is unchanged in substance and shorter in count: 35–76 words against the hero band 40–90.
- Media fields carry a corner slate (`IMAGE AREA · THE ROOM`, `DETAIL · 4:5`) instead of a
  centred label; ratios are deliberate and change per breakpoint.
- No study reserves an image it cannot name: the room, the couch, hands with stones, steam over
  water, a stone-and-linen still life.

## Verification

- `wellcheck.ps1`: themes, host background, namespace, reduced-motion, tag balance, hero `h1`,
  no dependencies, no shell, no pills / dashed boxes / drop shadows / radii over 8px, claims
  scan — **ALL CHECKS PASS**.
- Rendered and read at 1440 and 390; heights 1013 / 1292 / 629 / 816 / 981 at 1440. Corrections
  made: `002` offset field had collapsed to zero width (auto margin with an absolutely
  positioned label) — given an explicit width; `003` mosaic spans were on `figure` instead of
  the grid children — moved to `li`, and the display size reduced so "Treatments" fits the
  column; `004` sheet deepened and its field column widened so the hero is image-dominant.
- Cross-browser and assistive-technology testing not run. Design Lab ingestion not performed.
