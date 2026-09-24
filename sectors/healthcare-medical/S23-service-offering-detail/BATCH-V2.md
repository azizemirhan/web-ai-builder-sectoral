# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S23` — Service / Offering Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*.
- **This section had no V1 study.** Authored directly in the V2 register; this record carries both the authoring and the design decisions and there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

A detail page needs one real offering, and inventing a treatment would invent clinical content. So the page is the detail view of **an area this sector's own S02 already names** — *Skin: rashes, moles, spots that have changed, wounds that will not close* — and every line is written out of that section's words. Nothing new about the clinic is asserted.

The page answers the four things a visitor who has chosen an area actually needs, and one more that the sector requires:

- **What this covers** — four symptoms, each a sentence, taken from S02's own line.
- **What it does not cover** — cosmetic work, and any diagnosis made before somebody has looked. Then the limit that matters: *bleeding that will not stop, or a spreading rash with a fever, is not seen here.*
- **How the visit runs** — three steps, indexed in words: you say what changed and when; somebody looks, in daylight, and asks; you are told what it looks like, **what it is not**, and what happens next, in writing.
- **Who it is for** — anyone whose skin has changed and who has no answer yet, with the children's area named for the case where it is not.
- **Read next**, then the ask: *Tell us what is wrong.*

There is no price, no waiting time, no success rate, no clinician named, no diagnosis and no advice. The whole page is what the area *is*, which is the only thing a page can honestly say before anyone has looked.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S23-001` | Universal / Safe | 001 Linen & Sage | B | 1 — the page read in order | column rules behind the head | 1 reserved · 1 | 185 |
| `HC-S23-002` | Premium / Editorial | 002 Porcelain & Plum | B | 2 — the editorial reading, baseline-opposed | open bracket at the head | 2 reserved · 2 | 191 |
| `HC-S23-003` | Structured / Visual Modular | 003 Sky & Slate | B | 3 — the whole page as one plate | bordered plate, 1px lines shared | 1 reserved · 1 | 201 |
| `HC-S23-004` | Conversion-led | 004 Sand & Terracotta | C | 4 — the decision, measured | measure rule under the title's last clause | none · 0 | 178 |
| `HC-S23-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | B | 5 — the page held in a frame | corner frame at the head | 1 reserved · 1 | 185 |

All five sit inside the contract's detail band of 170–230 and well under the 250 ceiling.

**004 is the `C`**, and the contract asks a `C` to record why it carries none: the conversion-led reading of a detail page is the decision, and a photograph of a room does not help anyone make it. It is the one study with no reserved area and therefore no caption, so its `placeholder-data` is declared as none rather than left pointing at a caption it does not have.

## What was designed

The same spine, re-composed five ways rather than recoloured five ways. 001 reads top to bottom with the column rules behind the head and the cover list against the steps; 002 opposes the title and the lead at the baseline under the bracket, runs the treatment room across the width at 21:9, sets the cover list against the limit and ends with the person by role at 3:4 baseline-aligned to the audience line; 003 puts the entire page inside one bordered plate whose 1px lines are shared — head row on the band tone, three body cells, an audience row — with the ask beneath on the lead rule; 004 drops the media and carries the measure rule under *wounds that will not close*; 005 holds the head in the corner frame, offsets the cover list against the two chairs at 4:3 and gives the visit its own band-tone panel.

**The refusal is a designed element, not a footnote.** What the area does not cover is set in the graphite `--no` tone with only the urgent sentence in ink, and it is given the lead rule in 001, 002 and 005 — the one 3px accent rule each composition is allowed — so the limit is the strongest horizontal on the page.

The three steps are indexed with **word-numerals in the bordered chip** (`One`, `Two`, `Three`), never digits. Three honest media subjects only: the treatment room, the two chairs in the consulting room, and the doctor at work named by role. No SVG, no icon, no badge, no global header or footer.

## Verification

- `hccheck.ps1 -Sec S23 -Fields 'What this covers|What it does not cover|How the visit runs|Who it is for|Read next|Tell us what is wrong'` — ALL CHECKS PASS; parity 30/30. `<h1>` present and single (detail page); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no claim term; no digit in visible copy outside the field ratio labels; one placeholder per study except 004, which has none. All links point at same-variant S18, S04, S03 and S05 studies and resolve on disk.
- Rendered and read at 1440. Corrections: the step numeral chip was stretching to the row height and was set to start; the read-next label and its list were separating as two flex items in the foot and were wrapped; `padding-right` added to `.lead` was subtracting from the shared `34rem` measure rather than from the column, crushing the 005 lead to a five-word line, and was removed; the 005 square field and the 002 portrait field were each leaving a void beside two lines of text and were retuned to 4:3 and to a baseline-aligned narrower column.
