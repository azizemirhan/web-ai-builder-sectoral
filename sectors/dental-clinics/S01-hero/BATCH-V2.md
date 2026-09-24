# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Dental Clinics` · Prefix: `DN` · Section: `DN-S01` — Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, DN translation in `../DENTAL-THEME-CONTRACT.md` → *Detailing Pass* (the modern reading: sans display with one accent phrase, bare 6px fields, hairlines, one geometry stroke per variant). Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the proposition *we are not going to ask why you left it*; the three commitments as checkable facts, never adjectives; one action with its qualifier and no form; the room, the people and the ceiling as the only photographed subjects, never a model, a mouth or an instrument; no comfort, outcome or superiority claim; the surgery count as a placeholder demo value; the media counts per study (1, 1, 3, 1, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Geometry layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `DN-S01-001` | Universal / Safe | 001 Chalk | 1 — type beside the room | ring in the line tone behind the head | Sans display with *why you left it* in the accent, the lead, the bordered action with a calendar mark and its qualifier; the room as a 4:3 field taking the larger half; three commitments as a ruled row on the lead rule with struck-speech, document and struck-person marks | 1 × 4:3 · 1 | 93 |
| `DN-S01-002` | Premium / Editorial | 002 Linen | 2 — statement over a band | arc in the accent at the head's corner | The display at full measure; the room as a 21:9 field edge to edge *under* the type with V1's *the room, not a smile*; the lead and action beside the three commitments as ruled lines | 1 × 21:9 · 1 | 93 |
| `DN-S01-003` | Structured / Visual Modular | 003 Slate | 3 — rail and cells | dot grid behind the composition | Three fields on a CSS snap rail — waiting room, surgery, the dentist you would see — with word-numeral chips; head split; commitments as bordered cells; action on the lead rule. No script | 3 × 4:3 · 0 | 101 |
| `DN-S01-004` | Conversion-led | 004 Daylight | 4 — the refusals first | bar under *will not happen* | The room as a 21:9 field; THREE THINGS THAT WILL NOT HAPPEN HERE as a bordered band pulled up over its lower edge, the marks in `--no`; display, lead and action beneath | 1 × 21:9 · 0 | 93 |
| `DN-S01-005` | Art-directed / Distinctive | 005 Dusk, inverted | 5 — the asymmetry named | corner marks framing the display column | *You cannot see what we are doing. So we say it out loud.*; the four things said out loud as a ruled list with chips, the stop line on the lead rule with a hand mark; the ceiling as a 3:1 field; commitments as a ruled row with the action. V1's dark ground becomes the pale Dusk paper | 1 × 3:1 · 0 | 98 |

## What changed from V1

The pill buttons, 16–26px radii and filled bands go: the action is a 1px bordered rectangle at 4px, fields are bare flat areas at 6px with a slate label, bands are the paper darkened. The display is the system sans at 600 with one accent phrase; the three commitments carry the same three marks in every study; the refusal marks in 004 take `--no`, a plum rather than a red. Copy is V1's throughout; the surgery count keeps its placeholder marking.

## Verification

- `dncheck.ps1 -Sec S01 -Fields 'No lecture|whole cost|commission|Book the first appointment|Nothing is done unless you ask|why you left it'` — ALL CHECKS PASS on every rule; parity 29/30, the one absence V1's own (`005` opens on the asymmetry line instead). One `<h1>` per study; no header/nav/footer; no form; no script; no gradient, shadow, dashed border, pill or radius above 8px; inline SVG only, all `aria-hidden`; no digit outside a placeholder; no comfort, outcome or superiority term; no tooth mark.
- Rendered and read at 1440. Corrections: the 004 band heading held on one line under its bar; the 005 ceiling field set to 3:1.
