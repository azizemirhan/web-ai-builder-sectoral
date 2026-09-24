# BATCH V1

## Batch Identity

- Sector: `Healthcare & Medical Clinics`
- Prefix: `HC`
- Section ID: `HC-S11`
- Section Name: `Accreditations Certifications`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Direction | Theme | Shape | Composition | Areas | Words |
| --- | --- | --- | :---: | --- | ---: | ---: |
| `HC-S11-001` | Universal / Safe | 001 Linen & Sage | B | Three cards — the people, the building, the equipment — with *look it up* and a reserved pill each; **a wide frame of the desk with the register open** and the not-shown line beside it | 1 | 204 |
| `HC-S11-002` | Premium / Editorial | 002 Porcelain & Plum | B | **A tall frame of the registration on the wall by the door**, the three checks as a ruled serif column beside it | 1 | 201 |
| `HC-S11-003` | Structured / Visual Modular | 003 Sky & Slate | B | Head beside **the nurse checking the equipment log**; **a ledger of three rows with the same fields — *checked by*, *look it up*, *reserved*** | 1 | 212 |
| `HC-S11-004` | Conversion-led | 004 Sand & Terracotta | **C** | **A terracotta panel — *ask to see it; nobody will ask why*** — beside the three checks with *look it up* in bold | 0 | 228 |
| `HC-S11-005` | Art-directed / Distinctive | 005 Night & Mint | **C** | Dark ground; **three display-size mint words — *Registered. Inspected. Serviced.*** — each heading a column with the check and a reserved pill | 0 | 189 |

Row `B B B C C`. Pages four and five each carried `B B B` across `S08`–`S10` and take their
`C` here; pages one to three, after `C`, `B` and `C` at `S10`, return to `B`.

## The Governing Idea

> **A register you can look up, not a wall of badges.**

The sector's accreditation section is a strip of seals and logos, none of which a visitor can
check from the page; in this sector an invented body, registration or award is prohibited. This
batch says what is actually checkable and how:

- **The people** — every clinician is on a public register, by number; *look it up: the register
  and the number are on the letter you take home, and at the desk.*
- **The building** — inspected by the regulator, on its schedule; *look it up: the report is at
  the desk, and on the regulator's own site.*
- **The equipment** — serviced on a schedule, and the log is kept; *look it up: ask to see the log
  for the machine used on you.*

**Not shown here:** logos of bodies we are not members of; awards; any seal we could not explain
at the desk. `004` turns the section into permission — *ask to see it; nobody will ask why.*

## Reserved Fields

No register, body, number or date is named. Each check carries a **reserved field** marked
`data-placeholder="true"` — *register name and number*, *date of last inspection*, *service
schedule* — visibly empty, which is the honest form of a badge. Clear or fill before real use.

## Density

All five are declared **structured, 170–230**: three checks, each carrying what is checked, who
checks it, how you look it up and a reserved field, is a list-shaped role. 189–228; no trimming
was needed and no field was dropped.

## Media

Three reserved areas: the desk with the register open (`001`), the framed registration on the
wall by the door — the one badge a clinic is required to show, where it is required to show it
(`002`), and the nurse checking the equipment log (`003`). `004` and `005` are type by intent.

## Verification Record

- Word band structured `170–230`: **204 / 201 / 212 / 228 / 189.**
- Content parity: **17 shared fields across five studies, 85/85 slots present.**
- Reserved areas: **1 / 1 / 1 / 0 / 0.** Reserved fields: 3 per study.
- Claims scan clean; no named body, register, board, licence, award or seal; no clinician name,
  outcome, figure, price, telephone, hour or digit.
- Dependencies none; tag balance, namespace, frame, reduced-motion, `<h2>` labelling, no
  solid-border-plus-max-width: all pass. The one link per study is `#` (contact, `S19` not yet
  authored).
- Rendered and read at 1440 and 390; no layout corrections required.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.
