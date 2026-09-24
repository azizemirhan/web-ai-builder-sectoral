# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S26` — Doctor / Specialist Profile Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*.
- **This section had no V1 study.** Authored directly in the V2 register; this record carries both the authoring and the design decisions and there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

The sector forbids inventing a clinician's name, qualification, registration, licence, board or professional body, and the brief forbids fabricated credentials, invented handles, and testimonials attributed to a person. Every value that would identify somebody is therefore a **bracketed placeholder**: the name (in the `<h1>` and again in the register), the role, the registration, the department, the description of the post and the portrait caption.

What is left is not nothing — it is **the post rather than the biography**, and that is the whole idea of the page:

- **On the register** — Name, Role, Registration, Where they work, all reserved, followed by the line that makes the emptiness a decision: *Nothing in this block is written here. Each value comes from the register that holds it, and a value that is not in the register stays empty.*
- **What the post covers** — reserved, with one honest sentence after it: *The rest of this page is the same for everybody who holds it.*
- **How the appointment runs** — three steps, true of any clinician in this clinic: you say what changed and when · they look, and ask · you are told what it is not, and what happens next, in writing.
- **What they will not do** — give a diagnosis through a link, take an emergency, answer a message that is not an appointment.
- **Attached to** — the area in full and the pathway. **Reaching them** — *there is no direct line and no address on this page. Every route goes through the desk.*

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S26-001` | Universal / Safe | 001 Linen & Sage | B | 1 — the register first | column rules behind the head | 1 reserved · 8 | 207 |
| `HC-S26-002` | Premium / Editorial | 002 Porcelain & Plum | C | 2 — the empty name set as the page | open bracket at the head | none · 7 | 201 |
| `HC-S26-003` | Structured / Visual Modular | 003 Sky & Slate | B | 3 — the profile as one plate | bordered plate, 1px lines shared | 1 reserved · 8 | 227 |
| `HC-S26-004` | Conversion-led | 004 Sand & Terracotta | B | 4 — the reserved name, measured | measure rule under the name's second half | 1 reserved · 8 | 207 |
| `HC-S26-005` | Art-directed / Distinctive | 005 Night & Mint, inverted | B | 5 — the profile framed | corner frame at the head | 1 reserved · 8 | 207 |

All five sit inside the contract's detail band of 170–230.

**002 is the `C`**, and it records why: there is no person on this page yet, and a portrait would be the only element on it pretending otherwise. **004 keeps the portrait deliberately** — it is the conversion-led reading, and a visitor deciding whether to book wants to see who they will be in the room with; it is the one variant that sets it square at 1:1.

Eight placeholders per study, seven in 002. The name and the role each appear twice — once as the page's own title or label, once as a register row — and the `placeholder-data` meta says so rather than under-counting.

## What was designed

The register block is the page's centre of gravity, and it is designed as a **register, not a card**: bare labelled rows on hairlines with a fixed `9.5rem` label column so the reserved values share one left edge, and the refusal paragraph directly beneath in the graphite `--no` tone. It sits on the lead rule in 001 and 002, in its own band-tone cell in 003, beside the portrait in 004, and on a band-tone panel in 005.

The portrait, where it exists, is **the doctor at work, named by role only** — never a studio headshot, never a badge, never a signature. The `--no` tone carries three separate sentences on every study: what stays empty, what the person will not do, and that there is no direct line. That is more refusal than any other page in the sector, and it is correct here, because a profile page is where a clinic is most tempted to overstate.

003 adds one line the others do not, under the plate on the lead rule: *A name on this page does not mean an appointment with that person. The desk books whoever is free first.*

No SVG, no icon, no badge, no social row, no credential list, no rating, no global header or footer.

## Verification

- `hccheck.ps1 -Sec S26 -Fields 'On the register|What the post covers|How the appointment runs|What they will not do|Attached to|Reaching them'` — ALL CHECKS PASS; parity 30/30. `<h1>` present and single (detail page); no header/nav/footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no claim term; no digit in visible copy outside the field ratio labels. All links point at same-variant S18, S23, S24 and S05 studies and resolve on disk.
- Rendered and read at 1440. Corrections: the register rows were sizing their label column per row, so the reserved values stepped a few pixels apart, and the column was fixed; 005's post description was two lines against a 3:4 portrait and left a 300-pixel void, so the appointment block was moved into the same column.
