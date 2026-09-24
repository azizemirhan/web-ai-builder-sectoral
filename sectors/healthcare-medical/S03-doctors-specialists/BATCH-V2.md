# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S03` — Doctors & Specialists · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the eyebrow, the headline, the leads, the five role names and every line under them, the booking note and the refusal to list qualifications kept word for word; **everyone named by role only**, with no clinician name, qualification, registration, licence, board or professional body anywhere — are kept exactly. V1's own reserved-area count per study is kept: five in 001 and 005, one in 002 and 004, two in 003.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S03-001` | Universal / Safe | 001 Linen & Sage | A | 1 — the five people in a row | column rules behind the head | Head split; five portrait cells at 4:5 on the lead rule; the booking note and the refusal as a two-part foot | 5 reserved · 0 | 201 |
| `HC-S03-002` | Premium / Editorial | 002 Porcelain & Plum | B | 2 — the roles as an editorial list | open bracket at the head | The 4:5 handover field beside five ruled role rows on the lead rule | 1 reserved · 0 | 160 |
| `HC-S03-003` | Structured / Visual Modular | 003 Sky & Slate | A | 3 — the five roles as shared cells | bordered cell grid, 1px lines shared | The doctor's field tall down the first column, five role modules as bare labelled Sees / First visit / In the room fields, the nurse's field closing the last row | 2 reserved · 0 | 222 |
| `HC-S03-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — the booking note raised to the top | measure rule under the key phrase | A booking band on the band tone; the 4:5 doctor field beside five ruled role rows with the refusal beneath | 1 reserved · 0 | 169 |
| `HC-S03-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | A | 5 — the five people carried along a rail | corner frame at the head | Framed head; five portrait cells at 4:5 along a labelled, keyboard-reachable rail on the lead rule, offset inward | 5 reserved · 0 | 203 |

## What changed from V1

V1's rounded staff cards and its plain stacked roles go. The headline is the display `<h2>` with `in the room.` — the thing the section argues you are actually choosing — in the accent, and in 004 under the measure rule. Each role is a bare flat portrait field at 4:5 with its slate label inside the bottom-left corner (`THE NURSE · 4:5`), followed by who they see in ink and what they are like in the muted tone on a hairline. In 003 the three facts become bare labelled fields — SEES / FIRST VISIT / IN THE ROOM — rather than a table. **V1's refusal to list qualifications is set in the graphite refusal tone**, so the sentence that declines to publish a CV reads as the position it is rather than as a footnote.

V1's `005` rail is kept as a rail and made properly reachable: it carries V1's `aria-label` and is focusable, so the five roles can be scrolled with the keyboard, which the contract requires of any horizontal set.

**No SVG, no icon, no badge** — a sector whose anti-pattern list names the accreditation wall gets no badges of any kind.

## Verification

- `hccheck.ps1 -Sec S03 -Fields 'Who you will see|You are not choosing a CV|…|Registrations and accreditations'` — ALL CHECKS PASS; parity 85/85 on the slots common to all five. The lead is variant-specific and checked separately: 001, 002 and 005 carry V1's *Five people, by role…* line, 003 carries V1's own longer variant and 004 carries none, matching V1 exactly. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; no claim term from the healthcare vocabulary; no placeholder in this section; both links held at `#`, as V1 left them, because S05 and S11 are not yet authored.
- Rendered and read at 1440.
