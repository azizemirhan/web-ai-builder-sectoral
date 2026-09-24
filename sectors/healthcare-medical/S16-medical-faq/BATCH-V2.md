# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S16` — Medical FAQ · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*.
- **This section had no V1 study.** It is authored directly in the V2 register, so this record carries both the authoring and the design decisions and there is no `BATCH-V1.md`. The nine questions and their answers are shared across all five studies.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

The sector's FAQ role is an accordion of marketing questions. The honest version is **the questions reception is actually asked**, in the words they are asked in — plus the three a page must decline, named rather than quietly omitted.

Answered: *How soon can I be seen? · Who will I see? · What happens at the first visit? · Do I need a referral? · Can somebody come with me? · What does it cost?*

**Not answered here**, and said so: *What is wrong with me?* · *Is this serious?* · *What should I take?* — the first two because they need the room, the third because a dose depends on the person. The urgent case is sent to the emergency service, as the contract requires.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S16-001` | Universal / Safe | 001 Linen & Sage | B | 1 — the questions read down one measure | column rules behind the head | 1 reserved · 1 | 221 |
| `HC-S16-002` | Premium / Editorial | 002 Porcelain & Plum | C | 2 — the questions set as an editorial index | open bracket at the head | none · 1 | 218 |
| `HC-S16-003` | Structured / Visual Modular | 003 Sky & Slate | B | 3 — the questions as shared cells | bordered cell grid, 1px lines shared | 1 reserved · 1 | 227 |
| `HC-S16-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — the three that need the room, raised | measure rule under the key phrase | 1 reserved · 1 | 223 |
| `HC-S16-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | C | 5 — the questions read as they are asked | corner frame at the head | none · 1 | 218 |

Shapes read B · C · B · B · C.

## What was designed

**Every answer is open on the page.** There is no accordion, no disclosure to expand, no search box and no script — the register prefers the whole thing readable, and a worried visitor should not have to click to find out how soon they can be seen. The question is the ink, the answer the muted tone; in 002 and 005 the question rises to statement size, and in 005 it takes the mint accent so the page reads as a list of questions before it reads as a list of answers.

**The three refused questions are set in the graphite refusal token** in all five — as a ruled trio in 001, 002 and 005, as a band-tone row closing the plate in 003, and as a bordered panel in 004 where the conversion-led variant would otherwise be tempted to bury them. The usual wait is a demo value spelled as words; the first-visit fee is described but never given.

**No SVG, no icon, no badge, no chevron, no plus-minus.**

## Verification

- `hccheck.ps1 -Sec S16 -Fields 'Questions|The questions people ask at the desk|…|Book a first appointment'` — ALL CHECKS PASS; parity 100/100. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no `<details>`; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; no claim term from the healthcare vocabulary; one placeholder per study, declared in the `placeholder-data` meta. The ask is held at `#` for S19; every booking action points at the same-variant S05 and resolves on disk.
- Rendered and read at 1440.
