# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S05` — Appointment Booking · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — the eyebrow, the headline, the leads, the four questions, the three routes, the what-you-get line and the emergency refusal kept word for word; the call-back time and the usual wait left as demo values spelled as words — are kept exactly. V1's own reserved-area count per study is kept: one in 001, 003 and 004, none in 002 and 005. **There is no form anywhere**: the contract forbids one, and V1 described the route rather than imitating it.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S05-001` | Universal / Safe | 001 Linen & Sage | B | 1 — the four questions beside the desk | column rules behind the head | The four questions beside the 4:3 reception field; three ruled route rows on the lead rule; a two-part foot | 1 reserved · 2 | 168 |
| `HC-S05-002` | Premium / Editorial | 002 Porcelain & Plum | C | 2 — the four questions set large | open bracket at the head | Bracketed head split; the questions at statement size on the lead rule; three ruled route columns | none · 2 | 163 |
| `HC-S05-003` | Structured / Visual Modular | 003 Sky & Slate | B | 3 — the three routes as shared cells | bordered cell grid, 1px lines shared | Three route cells with How / What happens / When you hear as bare labelled fields; a band on the band tone with the questions and the 4:3 appointment book | 1 reserved · 2 | 223 |
| `HC-S05-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — the online route as a standing panel | measure rule under the key phrase | The online panel on the band tone down the left; head, a 21:9 waiting-room field and three ruled rows opposite | 1 reserved · 2 | 167 |
| `HC-S05-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | C | 5 — the booking written out as the conversation it is | corner frame at the head | A ruled transcript of the exchange down the left, speakers named by tracked labels; framed head and three ruled routes opposite | none · 2 | 216 |

## What changed from V1

V1's rounded booking cards and its filled call-to-action go. The headline is the display `<h2>` with `a short conversation` — the claim the section makes about booking — in the accent, and in 004 under the measure rule. The four questions are a plain ordered list, set at statement size in 002 where they are the whole composition. The three routes are ruled rows and, in 003, shared cells whose How / What happens / When you hear become bare labelled fields instead of a table. **V1's `tag` chip in 004 is dropped**: the register rules out pill tags, so ONLINE is set as the tracked uppercase label the register uses for exactly this job. **The emergency refusal is set in the graphite refusal tone** in all five. V1's 005 transcript is kept and structured as ruled exchanges with the speaker named by a tracked label and your turns in the muted tone, so the shape of the conversation is legible before the words are read.

**No SVG, no icon, no badge; no form and nothing that implies a booking is taken on the page.**

## Verification

- `hccheck.ps1 -Sec S05 -Fields 'Booking|short conversation about what is wrong|…|Answer the four questions'` — ALL CHECKS PASS; parity 95/95 on the slots common to all five. *rung back* is variant wording — V1 writes "rings you back" in 003 and 004 — and is not a shared slot. No `<h1>` (not a hero); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy outside the field ratio labels; no claim term from the healthcare vocabulary; two placeholders per study, declared in the `placeholder-data` meta; the single action held at `#`.
- Rendered and read at 1440.
