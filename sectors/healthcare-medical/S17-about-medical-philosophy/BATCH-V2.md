# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S17` — About / Medical Philosophy · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*.
- **This section had no V1 study.** It is authored directly in the V2 register, so this record carries both the authoring and the design decisions and there is no `BATCH-V1.md`. The five rules are shared across all five studies.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

The contract's copy direction bans the entire vocabulary this role is normally written in — *compassionate, dedicated, state-of-the-art, holistic, patient-centred*. A philosophy section written without those words has to say what the clinic actually does. So each of the five rules is paired with **what keeping it costs the clinic**, because a rule with no cost is a slogan:

| | The rule | What it costs us |
| --- | --- | --- |
| One | You are told who, before you book | We cannot quietly move you to whoever is free |
| Two | Nothing happens without your yes | Some visits end without the thing we expected to do |
| Three | A test only if it changes what we do | We are sometimes asked why we did not scan |
| Four | What was found goes to you in writing | Every visit takes longer than it would without it |
| Five | If this is not the place, you are told | We turn work away most weeks |

The section then **names the four words it refuses**, which is why they appear on the page at all.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S17-001` | Universal / Safe | 001 Linen & Sage | B | 1 — five rules, each with its price | column rules behind the head | 1 reserved · 0 | 227 |
| `HC-S17-002` | Premium / Editorial | 002 Porcelain & Plum | C | 2 — the five rules set at statement size | open bracket at the head | none · 0 | 224 |
| `HC-S17-003` | Structured / Visual Modular | 003 Sky & Slate | B | 3 — the rule against its price | bordered cell grid, 1px lines shared | 1 reserved · 0 | 235 |
| `HC-S17-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — hold us to it | measure rule under the key phrase | 1 reserved · 0 | 250 |
| `HC-S17-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | C | 5 — the rules read as a list you could test | corner frame at the head | none · 0 | 229 |

Shapes read B · C · B · B · C.

## What was designed

Each rule is a ruled row: the rule in ink, what it means on the day in ink or the muted tone, and **what it costs in the graphite refusal token**. In 003 the cost becomes its own column on the band tone, so the page reads as two facing claims rather than one. In 002 and 005 the rule rises to statement size. The refusal that names the four banned words is set in the refusal tone in all five and closes every study.

**No SVG, no icon, no badge, no team photograph of people laughing in a corridor** — the sector picture this role reaches for, and the first thing the contract's media rule rules out.

## Verification

- `hccheck.ps1 -Sec S17 -AllowClaims 'compassionate|patient-centred|holistic|state-of-the-art' -Fields 'How we work|A philosophy is a list of things you can be held to|…|Who you will see'` — ALL CHECKS PASS; parity 55/55. **The allowance is the section's own refusal**: those four words appear only in the sentence that declines them, which is the point of the section. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; no placeholder in this section. Every booking action points at the same-variant S05 and resolves on disk; *Who you will see* is held at `#` because S03 is a section rather than a page.
- Rendered and read at 1440. Correction: the 004 panel ran the study to 261 words, over the contract's 250 ceiling, so the panel's copy was cut to one sentence, bringing it to 250.
