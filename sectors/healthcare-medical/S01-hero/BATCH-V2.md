# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S01` — Hero · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the eyebrow, the headline, the lead, the action label and the three commitments kept word for word, the usual wait a demo value spelled as words, no clinician named, no condition claimed, no waiting time promised — are kept exactly. V1's own reserved-area count per study is kept: one in 001, 002, 004 and 005, three in 003.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Structure layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S01-001` | Universal / Safe | 001 Linen & Sage | 1 — the promise beside the room | column rules behind the head | Copy left with the 4:3 consulting room right; the three commitments as columns on the lead rule | 1 reserved · 1 | 86 |
| `HC-S01-002` | Premium / Editorial | 002 Porcelain & Plum | 2 — the headline against the answer | open bracket at the head | Head split, headline left and the lead and action at the baseline right; a 21:9 waiting-area band; three commitment columns on the lead rule | 1 reserved · 1 | 87 |
| `HC-S01-003` | Structured / Visual Modular | 003 Sky & Slate | 3 — the visit as three shared cells | bordered cell grid, 1px lines shared | Head with the action opposite; reception, a nurse at work and the consulting room as three cells at 4:3, one per commitment | 3 reserved · 1 | 77 |
| `HC-S01-004` | Conversion-led | 004 Sand & Terracotta | 4 — the promise measured | measure rule under the key phrase | Head with the lead opposite; a 21:9 treatment-room field; the three commitments and the action together in a band on the band tone | 1 reserved · 1 | 87 |
| `HC-S01-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | 5 — the promise framed | corner frame around the copy column | Framed copy column with the 3:4 field of the doctor at work beside it; the commitments as ruled rows | 1 reserved · 1 | 86 |

## What changed from V1

V1's rounded blocks at 20–28px, its filled action and its plain stacked commitments go. The headline is the display `<h1>` at weight 550 with `how soon.` — the visitor's actual question — carried in the accent, and in 004 under the measure rule. Each reserved area is a bare flat field with its slate label set inside the bottom-left corner (`THE ROOM · 4:3`, `THE WAITING AREA · 21:9`, `THE DOCTOR · 3:4`), at the radius the pass sets, 6px, not the contract's per-theme blob. The three commitments are structured by a single 3px accent lead rule and hairlines rather than by cards. The action is a thin-bordered rectangle with a trailing arrow character, 48px tall.

**No SVG, no icon, no badge anywhere.** The structure layer is drawn entirely in CSS: the 001 column rules are three absolutely positioned spans with a `border-left`, the 002 bracket is one span with two borders, the 003 device is the bordered cell grid itself, the 004 measure rule is the key phrase's own `border-bottom` with two `::before`/`::after` risers, and the 005 corner frame is two borders on the copy column.

## Verification

- `hccheck.ps1 -Sec S01 -Fields 'Clinic|Tell us what is wrong|…|What happens next, and who to ring'` — ALL CHECKS PASS; parity 60/60. One `<h1>` per study; no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the placeholder and the field ratio labels; no claim term from the healthcare vocabulary; one placeholder per study, declared in the `placeholder-data` meta; the single action held at `#`, as V1 left it, because S05 is not yet authored.
- Rendered and read at 1440. Correction: the 001 column rules were moved in to 13 / 30 / 47 per cent so the layer stays behind the copy column — at their first positions the third rule ran up the media column, which the register forbids.
