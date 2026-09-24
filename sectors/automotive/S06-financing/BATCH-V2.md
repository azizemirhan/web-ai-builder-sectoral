# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S06` — Financing · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

Finance is the role where the contract's figure ban bites hardest: no rate, no monthly payment, no deposit, no total, no term. That is not a gap — it is the truth about a rate:

> **A rate quoted before a check is a *guess*.** What finance costs depends on you, on the car, and on the day. Two of those we have not met yet.

The page is therefore built as **two opposed lists**, which is the honest shape of the subject:

- **What we can tell you now** — one, which kinds of agreement the showroom can arrange for you; two, what each one leaves you owning at the end of it; three, what happens if you want out of it early. All three are true before anyone is met.
- **What only a check can tell you** — *the rate*, *each month*, *up front*, *altogether*. Four bare labelled fields, all four reserved.

Then the limit:

> **No rate, payment, deposit or total is printed on this page.** A figure shown before anybody has looked at your circumstances is a number chosen to make you carry on reading.

**There is no calculator**, and no element on the page computes anything.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S06-001` | Universal / Safe | 001 Chalk & Racing Green | C | 1 — the two lists opposed on the lead rule | the bay lines behind the head | none · 4 | 144 |
| `AUTO-S06-002` | Premium / Editorial | 002 Paper & Oxide | B | 2 — the blank total as the lead image | the plate edge at the head | 1 reserved · 4 | 150 |
| `AUTO-S06-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the two lists as one itemised sheet | bordered plate, 1px lines shared | 2 reserved · 4 | 154 |
| `AUTO-S06-004` | Conversion-led | 004 Bone & Aubergine | B | 4 — *guess*, measured | the torque mark under *guess* | 1 reserved · 4 | 148 |
| `AUTO-S06-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | C | 5 — the lists framed and offset | the ramp frame | none · 4 | 144 |

All five sit inside the contract's standard band of 90–170.

**Two studies are `C`, and each records why.** 001: every figure on the page is reserved, and a photograph beside four empty values would be the only thing on it that looked settled. 005: the distinctive reading takes the refusal literally — if no figure is settled, nothing is allowed to look settled.

## What was designed

The reserved media, where it exists, is chosen to be the honest picture of a price: **the itemised sheet on the desk with the total line left blank**, at 21:9 in 002 and 16:9 in 003. It is the one image on this site that shows a number without printing one. 003 pairs it with the service reception, 004 with the handover desk — where the figure is finally said out loud.

The three things that *can* be said are numbered in words in the bordered chip; the four that cannot are a bare labelled register with a fixed `11rem` label column. Setting them in the same weight and the same rhythm is the point: the reader sees that the empty half is the same size as the full one.

## Verification

- `autocheck.ps1 -Sec S06 -AllowClaims 'deposit' -Fields 'Paying for it|A rate quoted before a check|What we can tell you now|What only a check can tell you|The rate|Each month|Up front|Altogether|Talk it through'` — ALL CHECKS PASS; parity 45/45.
- **Checker allowance, read before it was granted:** `deposit` is on the automotive claims list. It appears twice per study — once as the reserved field's value *[Approved deposit, after a check]*, once inside the refusal that says no deposit is printed. Both are refusals of the claim, not the claim.
- No `<h1>` (not a hero); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<input>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; **no rate, payment, deposit, total, term, percentage or any other figure**; no manufacturer, model, badge or plate; no rating, award or urgency device; no digit in visible copy outside the field ratio labels; four placeholders per study, declared in the `placeholder-data` meta. Both links point at same-variant S07 and S19 studies.
- Rendered and read at 1440.
