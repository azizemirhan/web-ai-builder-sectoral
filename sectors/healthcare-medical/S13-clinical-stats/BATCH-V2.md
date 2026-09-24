# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S13` — Clinical Stats · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the eyebrow, the headline, the lead, the five counts with their labels and why-it-matters lines, the where-you-check-it lines in 003, the usual-wait panel in 004 and the not-counted-in-public refusal kept word for word — are kept exactly. **Every count is about the building and the diary, never about a patient**, and all five are demo values marked `data-placeholder="true"` and spelled as words. V1's own reserved-area count per study is kept: one in 001–004, none in 005.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S13-001` | Universal / Safe | 001 Linen & Sage | B | 1 — five counts set as word-numerals | column rules behind the head | Five count columns on the lead rule; a closing band with the 4:3 corridor, the refusal and the action | 1 reserved · 5 | 148 |
| `HC-S13-002` | Premium / Editorial | 002 Porcelain & Plum | B | 2 — the diary beside the counts | open bracket at the head | A 3:4 appointment-book field beside five ruled count rows on the lead rule | 1 reserved · 5 | 149 |
| `HC-S13-003` | Structured / Visual Modular | 003 Sky & Slate | B | 3 — every count with the place you verify it | bordered cell grid, 1px lines shared | Head with a 4:3 handover field; five rows of word-numeral, label, Why it matters and Where you check it on the band tone | 1 reserved · 5 | 207 |
| `HC-S13-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — the wait raised out of the list | measure rule under the key phrase | The usual-wait panel on the band tone with that count at display size and a 4:3 diary field, beside the other four as ruled rows | 1 reserved · 5 | 160 |
| `HC-S13-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | C | 5 — the five counts read as an index | corner frame at the head | Five word-numeral count rows on the lead rule, offset inward | none · 5 | 145 |

## What changed from V1

This is the other section the sector's anti-pattern list names — *statistics panels with percentages, success rates or patient counts* — and the headline answers it directly. The re-authoring keeps the answer visible: **there is no chart, no percentage, no counter, no stat tile and no digit anywhere.** Each value is a word — *Six*, *Eleven*, *A week*, *Half an hour*, *A few days* — set large in the accent, which is how this register carries an index numeral. V1's rounded stat tiles go; the counts are columns and ruled rows separated by hairlines, and in 003 a shared-line ledger whose *Where you check it* column sits on the band tone, because the verifiability is the point.

**V1's `tag` chip in 004** becomes the register's tracked uppercase label, and the not-counted-in-public refusal — outcomes, satisfaction scores, how many people have been seen — is set in the graphite refusal tone throughout.

**No SVG, no icon, no badge, no chart.**

## Verification

- `hccheck.ps1 -Sec S13 -Fields 'In numbers|Numbers about the building and the diary|…|Book a first appointment'` — ALL CHECKS PASS; parity 65/65. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; **no digit anywhere in visible copy** outside the field ratio labels — every count is a word; no claim term from the healthcare vocabulary; five placeholders per study, declared in the `placeholder-data` meta. Every booking action points at the same-variant S05 and resolves on disk.
- Rendered and read at 1440.
