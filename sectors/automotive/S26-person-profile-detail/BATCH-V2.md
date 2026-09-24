# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S26` — Technician / Sales Specialist Profile · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

The contract forbids an invented name, qualification, ticket, certification or trade body, and the brief forbids fabricated credentials and invented profile links. Every value that would identify somebody is therefore **reserved**:

> **[Approved *name*].** What the post covers, how the person works, and how to reach them. Anything that names them stays empty until they say yes.

**On the sheet** — *Name*, *Role*, **Tickets held, and who issued them**, *Which bay*. Four reserved fields, then the line that makes the emptiness a decision: *Nothing in this block is written here. Each value comes from the person, or from whoever issued it.*

What is *not* reserved is what is true of the **post** rather than the holder:

- **How a job runs with them** — one, you say what the car is doing; two, they look, and write down what they find; three, **you are told what was found and what was left, before anything is done.**
- **What they will not do** — quote a job they have not seen, start work you have not agreed to, or sell you a part that is not worn out.
- **Reaching them** — *there is no direct line and no address on this page. Every route goes through the desk.*

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S26-001` | Universal / Safe | 001 Chalk & Racing Green | B | 1 — the sheet first | the bay lines behind the head | 1 reserved · 8 | 208 |
| `AUTO-S26-002` | Premium / Editorial | 002 Paper & Oxide | C | 2 — the empty name set as the page | the plate edge at the head | none · 7 | 202 |
| `AUTO-S26-003` | Structured / Visual Modular | 003 Steel & Cobalt | B | 3 — the profile as one plate | bordered plate, 1px lines shared | 1 reserved · 8 | 227 |
| `AUTO-S26-004` | Conversion-led | 004 Bone & Aubergine | B | 4 — the reserved name, measured | the torque mark under the name | 1 reserved · 8 | 208 |
| `AUTO-S26-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | B | 5 — the profile framed | the ramp frame | 1 reserved · 8 | 208 |

All five sit inside the contract's detail band of 170–230.

**002 is the `C`**, and it records why: there is no person on this page yet, and a portrait would be the only element pretending otherwise. **004 keeps the portrait deliberately** — somebody deciding whether to hand over a key wants to see who takes it — and it is the one variant that sets it square at 1:1.

Eight placeholders per study, seven in 002. The name and the role each appear twice — once as the page's own title or label, once as a sheet row — and the `placeholder-data` meta says so rather than under-counting.

## What was designed

The sheet is the page's centre of gravity and is designed as **a sheet, not a card**: bare labelled rows on hairlines with a fixed label column, the refusal directly beneath in the graphite `--no` tone. The portrait is **the technician at work, named by role only** in its own slate label — never a studio headshot, never a badge, never a signature.

The `--no` tone carries three separate sentences on every study: what stays empty, what the person will not do, and that there is no direct line. That is more refusal than any other page in the sector, and it is right here, because a profile is where a dealership is most tempted to overstate.

003 adds one line the others do not, under the plate: *A name on this page does not mean a job with that person. The desk books whoever is free.*

## Verification

- `autocheck.ps1 -Sec S26 -Fields 'On the sheet|Tickets held|Which bay|What the post covers|How a job runs with them|What they will not do|Attached to|Reaching them'` — ALL CHECKS PASS; parity 40/40. `<h1>` present and single (detail page); no header, nav or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no `tel:` or `mailto:` link; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; **no name, qualification, ticket, certificate, trade body, award or rating**; no manufacturer, model, badge, plate, price or figure; no digit in visible copy outside the field ratio labels. All links point at same-variant S23, S24 and S19 studies.
- Rendered and read at 1440. Correction: 003 first measured 245 words, over the detail band, because it carries an extra line under the plate; the lead, the sheet refusal and the reaching-them line were each shortened, bringing all five to 202–227.
