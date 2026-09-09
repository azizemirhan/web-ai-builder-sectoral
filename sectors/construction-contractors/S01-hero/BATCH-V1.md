# BATCH V1

## Batch Identity

- Sector: `Construction & Contractors`
- Prefix: `CON`
- Section ID: `CON-S01`
- Section Name: `Hero`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `CON-S01-001` | Universal / Safe | AUTHORED | `raw/CON-S01-001.html` |
| `CON-S01-002` | Premium / Editorial | AUTHORED | `raw/CON-S01-002.html` |
| `CON-S01-003` | Structured / Visual Modular | AUTHORED | `raw/CON-S01-003.html` |
| `CON-S01-004` | Conversion-led | AUTHORED | `raw/CON-S01-004.html` |
| `CON-S01-005` | Art-directed / Distinctive | AUTHORED | `raw/CON-S01-005.html` |

**First batch in the `CON` sector.** The sector's design direction was written before authoring, in
`../CONSTRUCTION-DESIGN-DIRECTION.md`, on the same sequence used for `WELL`.

## Authoring Direction

Five reference heroes were supplied and all five were used, each placed at the direction whose
register it occupies — the *by register* mapping rather than a locked first-to-first order.

| Reference | Register | Placed at |
| --- | --- | --- |
| Blue-tinted photograph, headline, two actions, glass stat bar | Dependable evidence hero | `001` |
| Split panel: tall image, pale panel, one action, one large figure | Calm, one number | `002` |
| Oversized outlined display type, stat column, note block | Zoned grid, type-led | `003` |
| Clean white, photograph, search card overlapping its lower edge | Start-the-enquiry | `004` |
| Near-black, red block, machinery, oversized line, slide counter | Weight and plant | `005` |

## The Governing Constraint — The Counter Is The Signature, And Every Figure In It Is Reserved

**Every one of the five references is built around a number**, and every one of those numbers is
invented:

> 10K happy clients · 5K properties sold · 15+ years · 40 years of experience · 50+ projects
> completed · 100+ expert works · $3.5M · 10M+ happy customers · 12k+ properties · 8+ years of
> service · from $8 per sq. m.

That is not a coincidence: **a number is the fastest available proxy for *can you actually do
this*,** which is the first of the four questions this sector's buyer is asking. So the counter is
kept, and the `WELL-S11` field-versus-figure test decides each figure in it:

| Figure | Treatment | Reasoning |
| --- | --- | --- |
| Year founded | **Reserved field** | Every firm has one; it is on the company record either way |
| Projects completed | **Reserved field** | Countable from handover certificates |
| People employed | **Reserved field** | Countable, and the study says *directly employed*, since that and the supply chain are different numbers |
| Largest project by value | **Reserved field** | A fact, and the honest version of what a rate was signalling |
| *Happy clients*, *satisfaction*, *on-time %* | **Omitted** | An empty field asserts a survey nobody ran |
| *Properties sold* | **Omitted** | A different trade entirely |
| Safety record, incident figures | **Forbidden** | Regulated; see the sector direction |
| Awards, ratings, review scores | **Forbidden** | Invented bodies, invented judgements |
| Price, day rate, per square metre | **Omitted** | No price survives a scope nobody has walked |

**Eleven reserved fields across the batch**, every one carrying a visually hidden label naming what
belongs in it. **Zero digits in visible copy anywhere in the batch**, verified by scan.

A reserved counter still does its job: a labelled empty field at counter scale tells a reviewer
exactly what the finished hero will assert, and makes it impossible for the catalog to ship a
fabricated proof.

## What Each Study Dropped From Its Reference, And Why

This is the batch's most useful record, because in every case the dropped element is the one that
would have been invented.

| Study | Dropped | Why |
| --- | --- | --- |
| `001` | The four-figure glass bar as written | Three of the four were unearned; the bar survives with reserved fields |
| `002` | The round *watch* button | A play control implies a film that does not exist |
| `002` | The header phone number | Section shell, and the number would have been invented |
| `003` | *10K happy clients*, *5K properties sold* | A survey nobody ran, and a different trade |
| `004` | The **price range** control | A price band is either a fabricated rate or a quote for a job nobody has walked. The card says so in a line rather than silently omitting it |
| `005` | The slide counter | It asserts a carousel this scriptless study does not have — and would have put a digit on the page |
| `005` | The vertical side navigation | Site chrome |
| `005` | *From $8 per sq. m.* | Same rule as `004`'s price field |
| all | The site header | Standing section-shell rule |

## Study Records

### CON-S01-001 — Universal / Safe

- **Layout model:** Proposition and two actions above a wide reserved project area, with the
  statistics bar overlapping its lower edge — the reference's glass bar, with every figure reserved.
- **The line that earns its place:** *"We will not price a job we have not walked."* The sector
  direction's test for any sentence is whether a competitor could print it unchanged; this one
  cannot, unless they operate that way.
- **Each reserved field carries a note on how the number is arrived at** — *counted from handover
  certificates*, *directly employed, not counting the supply chain*. A figure whose derivation is
  stated is worth more than a bigger figure that is not.

### CON-S01-002 — Premium / Editorial

- **Layout model:** A tall reserved project image holding the left, a pale panel on the right with
  the proposition, one action and **one reserved figure at counter scale**.
- **The editorial argument:** one image, one sentence, one number, one action. A contractor's hero
  does not have to prove everything above the fold; it has to be specific about one thing.
- The proposition is a continuity claim — *the people who price it are the people who build it* —
  which is checkable and is the thing mid-size contractors actually compete on.

### CON-S01-003 — Structured / Visual Modular

- **Layout model:** A twelve-column grid with four zones — a note, an oversized two-line display, a
  wide reserved project area, and a column of three reserved figures — closed by a caption naming
  what the firm builds.
- **The outlined line, and how it is made safe:** the second line is drawn with
  `-webkit-text-stroke` inside an `@supports` guard. **Without the guard, an unsupporting browser
  would render `color: transparent` and the line would vanish.** With it, the fallback is the solid
  weight. The checker verifies that any transparent-fill headline in this sector is guarded.
- **Not a specification table**, which is this direction's trap in this sector: four zones with
  different internal shapes, not rows of one matrix.

### CON-S01-004 — Conversion-led

- **Layout model:** Proposition, reserved project area, and a three-field enquiry card overlapping
  its lower edge, above three reserved figure cards.
- **What the card became.** The reference searches a property database — *Buy/Rent, Location,
  Property Type, Price Range*. A contractor has no database to search, so the same card shape starts
  **an enquiry with a real scope**: what is being built, where, and how far along it is. Three facts
  an estimator needs before they can say anything useful, every option generic sector vocabulary.
- **The refused control is the interesting one.** There is no budget field, and the card says why:
  *"a number typed into a hero is either a guess you will be held to or a rate we invented, and
  neither helps you."* Naming the refusal is the same device the `WELL` sector arrived at four
  times over.
- **Boundary:** this starts an enquiry; the full bid and RFQ flow is `S15`.
- No placeholder text in any field, and every field has a real `<label for>`.

### CON-S01-005 — Art-directed / Distinctive

- **Layout model:** A near-black field, one saturated block held to the right, a large reserved
  plant area sitting across it, and an oversized line beneath.
- **The `005` trap in this sector is becoming a car advert.** The slot names the difference:
  *machinery in use, on the job — working, not parked for a photograph.* The subject is the work.
- **The most specific proposition in the batch:** groundworks and civils, described as the thing
  everyone else's programme depends on. It is the one study that does not try to be the whole firm.
- **Correction made, recorded:** the headline's measure was set as `max-width: 22ch` on the wrapper,
  where `ch` resolves against the wrapper's 1rem rather than the display size — the headline broke
  to one word per line across six lines. Moved onto the `h1` at `17ch`, where `ch` resolves against
  the display size. **This is the third time this exact bug has appeared in the workspace
  (`WELL-S03-004`, `WELL-S21-005`, here); a `ch` measure belongs on the element whose type it is
  measuring, never on its wrapper.**

## Structural Diversity

| Study | Topology | Media | Reserved figures | Actions | Ground |
| --- | --- | --- | --- | --- | --- |
| 001 | Proposition + wide media + overlapping bar | One 21:9 | 3 | 2 | Concrete `#eef0f1` |
| 002 | Split: tall image against a pale panel | One 3:4 | 1, large | 1 + a link | Warm stone `#f4f2ea` |
| 003 | Twelve-column zoned grid | One 16:9 | 3, column | 1 | Light grey `#e8e8e6` |
| 004 | Media with an overlapping enquiry card | One 16:9 | 3, cards | Form + submit | Clean white `#f7f8f9` |
| 005 | Black field, colour block, plant plate | One 16:9 | 1 | 1 | Near-black `#131313` |

## Research Metadata

- **Sources:** five reference heroes supplied by the user; all five used, each placed by register.
- **Research date:** 2026-09-03.
- **Visual-first check:** no study derives its distinctiveness from copy. The differentiator is how
  the counter is carried — an overlapping bar, one large figure, a column, three cards, or a single
  figure beside the action.
- **Document-metaphor justification:** `NONE`.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** `004` uses native form controls only — no validation script, no
  success state. No `<script>`, `<iframe>` or inline `style` in any file.

## Media Slots

| Slot | Study | Expected Type | Rule attached to the slot |
| --- | --- | --- | --- |
| Project media | `001` | Still image, 21:9 | Completed work; no stock handshake, no posed group in clean PPE |
| Project media | `002` | Still image, 3:4 | One finished building; a real project, not a render |
| Project media | `003` | Still image, 16:9 | Completed work, wide; a real project, not a render |
| Project media | `004` | Still image, 16:9 | Completed work, wide; a real project, not a render |
| Plant media | `005` | Still image, 16:9 | Machinery in use, on the job — working, not parked |
| Counter figures ×11 | all five | **Text**, replaced by the real figure | Em dash with a visually hidden field label |

**Every media slot states what it may not contain**, which is the `WELL-S24-005` device applied from
the first batch of a new sector rather than discovered late in it.

## QA

- ID validation: **PASS.** All five IDs exist and match their filenames; `sector-prefix` is `CON` in
  all five.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport. Nesting validated with a stack-based parser.
- Territory validation: **PASS.** All five match the core `S01`–`S20` direction set.
- Accessibility QA: **PASS.** Exactly one `<h1>` per study, `aria-labelledby`,
  `prefers-reduced-motion`, 50px-plus targets, every reserved field with a visually hidden label.
  `004`'s three fields each have a real `<label for>` and no `placeholder` attribute.
- Responsive QA: **PASS.** Verified at 1440px; each study states its ladder, and in `001` and `004`
  the overlapping bar and card reduce their overlap before they would collide with the media label.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.** No malformed hex, no accidental 8-digit hex, no `clamp()` arity error.
- **Text-stroke guard check: PASS.** `003`'s transparent-fill headline is inside an `@supports`
  guard, so it degrades to solid rather than disappearing. New check, added for this sector.
- Section-shell check: **PASS.** No header, nav or footer in any study, although all five references
  show one.
- Scoped-CSS check: **PASS.** Every declaration outside the host baseline is namespaced.
- **Reserved-counter check: PASS — this batch's defining check.** Eleven reserved fields, eleven
  labelled, and **no digit in visible copy anywhere in the batch.**
- **Fabricated-proof check: PASS.** Thirty-one patterns covering currency, percentages, per-square
  rates, *happy clients*, *satisfaction*, on-time and on-budget **claim forms**, zero-accident and
  incident figures, certifications and ISO, *accredited*, *approved contractor*, awards, star
  ratings, reviews, testimonials, guarantees, *market leader*, *leading*, *best in*, *world-class*,
  and urgency devices. **Zero matches.**
- **Soft check, ten occurrences, all verified in context:** every *price*, *priced*, *budget*,
  *estimator*, *estimate* and *claim* sits inside a refusal or a description of who does the work.
- Render check: **PASS, after one correction.** All five rendered in headless Chrome at 1440px and
  inspected; `005`'s headline measure was moved from the wrapper to the `h1`, as recorded above.

## Notes

- **First authored batch in the `CON` sector**, and the first in this workspace to be authored
  against a full set of supplied references rather than one or none.
- **The reusable outcome is the treatment of the counter.** Construction sells the removal of risk,
  and a number is the fastest proxy for capability — which is exactly why every reference invents
  one. Keeping the counter and reserving every figure in it preserves the sector's signature device
  while making a fabricated proof structurally impossible. **Every sector whose heroes lean on
  numbers — logistics, manufacturing, finance, IT services — can take this unchanged.**
- The second outcome is smaller and immediately reusable: **what a study drops from its reference is
  worth recording as carefully as what it keeps.** Four of the five dropped elements here were the
  invented ones, and the record of why is the most transferable part of the batch.
- The `ch`-on-the-wrapper bug has now appeared three times in this workspace. It belongs in the
  authoring standard rather than in three separate batch documents.
- `S02 Construction Services` is next in this sector. `WELL-S27` remains part-authored — four of
  five studies, no batch document — and its README says so.
