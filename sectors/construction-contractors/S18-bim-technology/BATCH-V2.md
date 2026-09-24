# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Construction & Contractors` · Prefix: `CON` · Section: `CON-S18` — BIM Technology · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CON translation in `../CONSTRUCTION-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — it moves where you find out; the four rooms and what fixing it takes in each; the six coordination items; the survey caveat; sometimes the answer is no; no software, badge, fly-through, maintained-twin claim, wireframe or angle; information manager, level schedule, survey and model reserved — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Drawing layer | Composition | Reserved | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CON-S18-001` | Universal / Safe | 001 Site White & Safety Orange | 3 with 7 — room cells, item rows | horizontal dimension line with vertical ticks behind the head | Four bordered room cells under the tape with a stroke icon each (envelope / document / hard hat / house) and WHAT FIXING IT TAKES at headline size, escalating onto the band tone with the fourth deep-red-edged; six bordered item rows with icons (I-beam / void bars / riser / opening / crosshair / badge), IN THE MODEL in ink and ON SITE IF IT WAS MISSED on the band tone behind a deep-red edge; tape-topped artefact band with the reserved manager, schedule and survey at counter scale; refusal with tags | 3 slots | 762 |
| `CON-S18-002` | Premium / Editorial | 002 Bone & Burnt Amber | 7 — the duct and the beam told four times | levelling circle with a square crosshair behind the head | Four ruled chapters with the room icon at counter scale and WHAT IT TAKES as a bordered cell in the margin and the prose in the centre, the fourth on the band tone behind a deep-red edge; the moral at display size under the tape; the six items as a ruled iconed list beside the filing argument and a bordered ledger of reserved artefacts; closing chapter | 3 slots | 869 |
| `CON-S18-003` | Structured / Visual Modular | 003 Steel & Structural Blue | 3 twice — WITHOUT and WITH sheets | horizontal dimension lines over each sheet, the WITH sheet's ticks bunched left | Two bordered four-column sheets with the rooms as iconed column heads and the six problems as bordered iconed chips in the column where they surface, right-hand columns on the band tone and the last deep-red-edged, empty columns marked NOTHING ARRIVES HERE / NOTHING; the sixth item as a red-edged chip drawn twice; red-topped survey note; bordered two-cell foot with reserved artefacts and refusal tags | 3 slots | 556 |
| `CON-S18-004` | Conversion-led | 004 White & Hi-Vis | 4 + 3 — job rows with one action each | vertical scale-bar ticks behind the band | Display with tape underline; four bordered job-type rows — the answer at headline size with a verdict chip (WORTH IT filled, YES IN THAT ORDER filled, NOT WORTH IT red, A CONTRACT QUESTION open), a square-bulleted list and one bordered iconed action with its note, the refusal row on the band tone; hi-vis band with the reserved manager and survey at counter scale; ruled foot. All anchors in-page | 2 slots | 677 |
| `CON-S18-005` | Art-directed / Distinctive | 005 Asphalt & Signal | 9 — the argument at display size, the evidence at caption scale | vertical datum line with ticks down the left margin | The statement at display size across the full measure over the tape rule; the four rooms as a bordered strip of iconed cells escalating onto the band tone; the six items as a two-column ruled iconed list; the filing argument as an accent-edged band-tone panel; HELD AGAINST EVERY JOB as a bordered four-slot record at counter scale; ruled foot | 4 slots | 620 |

## What changed from V1

The four rooms are drawn as one escalation across the batch — paper, paper, band tone, band tone with a deep-red edge — each with a stroke icon (envelope, document, hard hat, house) and what it takes in tracked uppercase; the six items carry an icon set (I-beam, void bars, riser with lift arrow, opening-in-square, crosshair, badge) with the survey item red where it stays on site; the reserved artefacts are a bordered slot ledger; the refusals are muted tags beside a struck seal. Nothing is drawn at an angle anywhere in the batch: no grid, hatch, chevron or rotated element — the drawing layer is orthogonal dimension lines, datum ticks and one circle. Copy is V1's throughout; word counts equal V1's.

## Verification

- `concheck.ps1 -Sec S18 -Fields 'Name of the information manager|Survey reference'` — ALL CHECKS PASS; parity 10/10. No `<h1>`; no header/nav/footer; no form; no script, remote dependency, gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit in copy; no software, standard, level, figure, clash count, saving or project name; no `transform`, skew or angled path in any study.
- Rendered and read at 1440. Corrections: `002` moral max-width moved to an inner span (checker rule).
