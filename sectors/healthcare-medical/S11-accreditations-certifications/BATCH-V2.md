# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S11` — Accreditations & Certifications · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the eyebrow, the headline, the lead, the three checks with their look-it-up lines, the ledger labels in 003, the ask-to-see-it panel in 004 and the not-shown-here refusal kept word for word — are kept exactly. **No register, body, number, date, regulator or seal is named**: the register name and number, the date of the last inspection and the service schedule are reserved values marked `data-placeholder="true"`. V1's own reserved-area count per study is kept: one in 001, 002 and 003, none in 004 and 005.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S11-001` | Universal / Safe | 001 Linen & Sage | B | 1 — three checks, each with the way to check it | column rules behind the head | Three ruled check rows on the lead rule; a closing band with the 4:3 open register, the refusal and the ask | 1 reserved · 3 | 194 |
| `HC-S11-002` | Premium / Editorial | 002 Porcelain & Plum | B | 2 — the registration beside the three checks | open bracket at the head | A 4:5 field of the framed registration beside three ruled check rows on the lead rule | 1 reserved · 3 | 193 |
| `HC-S11-003` | Structured / Visual Modular | 003 Sky & Slate | B | 3 — the checks as a four-column ledger | bordered cell grid, 1px lines shared | Head with a 4:3 equipment log; three rows of what is checked, Checked by, Look it up on the band tone, and the reserved value | 1 reserved · 3 | 204 |
| `HC-S11-004` | Conversion-led | 004 Sand & Terracotta | C | 4 — the ask standing beside the three checks | measure rule under the key phrase | The ask panel on the band tone and the refusal in a side column beside three ruled check rows | none · 3 | 228 |
| `HC-S11-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | C | 5 — three words, each answered | corner frame at the head | Registered. Inspected. Serviced. at statement size in the accent, offset inward, each with its label, statement, look-it-up line and reserved value | none · 3 | 189 |

## What changed from V1

This is the section the sector's anti-pattern list names twice — *accreditation walls, badge rows and seal strips as the main device* — and the headline already says so. The re-authoring makes the refusal structural: **there is no badge, no seal, no logo and no SVG of any kind on any of the five studies.** What a wall of badges would have been is instead three checks, each with the way a visitor verifies it themselves, and three reserved values.

Each reserved value is a **bordered edge in the graphite refusal token** — a 1px rule and 2px corners, never a filled chip or a pill — reading `RESERVED — REGISTER NAME AND NUMBER`. V1's look-it-up line is marked by the accent, so the checkable half of each claim is the coloured one. The headline is the display `<h2>` with `you can look up` in the accent, and in 004 under the measure rule. In 003 the four columns become a shared-line ledger with the look-it-up column on the band tone; in 005 V1's three words carry the composition at statement size. **V1's `tag` chip in 004** becomes the register's tracked uppercase label, and the not-shown-here refusal is set in the refusal tone throughout.

## Verification

- `hccheck.ps1 -Sec S11 -AllowClaims 'award' -Fields 'Registered and inspected|A register you can look up|…|Ask at the desk'` — ALL CHECKS PASS; parity 85/85 on the slots common to all five. **The allowance is V1's own refusal**: *Awards* appears only in the sentence listing what the page will not show. The phrase *public register, by number* is variant wording — 003 writes "Every clinician here, by number" — so the shared slot is *public register*. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; three placeholders per study, declared in the `placeholder-data` meta. The one action is held at `#` for S19, as V1 left it.
- Rendered and read at 1440.
