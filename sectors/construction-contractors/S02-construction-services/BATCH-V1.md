# BATCH V1

## Batch Identity

- Sector: `Construction & Contractors`
- Prefix: `CON`
- Section ID: `CON-S02`
- Section Name: `Construction Services`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `CON-S02-001` | Universal / Safe | AUTHORED | `raw/CON-S02-001.html` |
| `CON-S02-002` | Premium / Editorial | AUTHORED | `raw/CON-S02-002.html` |
| `CON-S02-003` | Structured / Visual Modular | AUTHORED | `raw/CON-S02-003.html` |
| `CON-S02-004` | Conversion-led | AUTHORED | `raw/CON-S02-004.html` |
| `CON-S02-005` | Art-directed / Distinctive | AUTHORED | `raw/CON-S02-005.html` |

Second batch in the `CON` sector. Governed by `../CONSTRUCTION-DESIGN-DIRECTION.md`; the section's
role and boundaries are in `./README.md`.

## Revision — V1 rev 2, After Review

The first pass of this batch was reviewed and rejected on design grounds, correctly. The content
rules were right and the layouts were not: **three of the five studies carried no media at all**,
every service was explained in three-line paragraphs, and the section read as documentation rather
than as design. The sector direction says *project photography is this sector's only genuine asset*
— and the first pass then removed it.

All five studies were rewritten image-first. What changed and what did not:

| Kept | Rewritten |
| --- | --- |
| The delivery marker on every service | From a paragraph to a chip on the image |
| The turn-down / steer-away position | From four paragraphs to one line, or four one-line conditions |
| Every content rule — no figures, prices, lead times, certifications, client names | — |
| The five structural approaches | Their visual form, entirely |

| Study | Was | Now |
| --- | --- | --- |
| 001 | Six white text cards with small images | A full-width featured service plus a five-card grid, every card led by a large reserved image with the label and chip on it |
| 002 | A single column of prose | Alternating image-and-text bands, sides swapping down the page, one sentence per service |
| 003 | Three white panels of lists — a specification sheet | **A twelve-column image mosaic** at four tile sizes, labels and chips riding on the images, closed by a marker legend bar |
| 004 | Two columns of paragraphs | A wide reserved image with a **white decision card floating over its lower half**, bullets cut to one line |
| 005 | Six equal text blocks on a dark ground | A **cinematic image stage** with the line set over it and the sequence as a slim stage rail beneath |

**Reserved media went from two areas across the batch to nineteen**, and every one is large. The
reserved fills are drawn as gradients rather than as flat grey, so they read as photographic
placeholders at the scale the finished section will use, and each dark tile carries a veil so the
label stays legible whatever photograph replaces it.

**Two corrections during the rewrite, both recorded:**

- `003`'s first mosaic mixed aspect ratios across a twelve-column grid, so row one did not
  tessellate and the layout opened a hole under the wide tile. Rebuilt on **explicit row spans**
  with a fixed `grid-auto-rows` height — an image mosaic tessellates on row spans, not on aspect
  ratios.
- `004`'s headline carried `max-width: 26ch` on its **wrapper**, where `ch` resolves against 1rem
  rather than against the display size; the headline broke to five lines. Moved onto the `h2`.
  **This is the fourth appearance of that bug in this workspace** (`WELL-S03-004`, `WELL-S21-005`,
  `CON-S01-005`, here). It belongs in the authoring standard, not in four batch documents.

The checker needed one adaptation as well: the marker class names changed in the rewrite, so the
delivery-marker scan matched nothing while the markers were plainly present. Widened to match any
marker class shape rather than one literal — **a check written against a class name is a check
against a decision that has not been made yet.**

## Authoring Direction

No reference images were supplied for this section; the set the user provided covered `S01` only.
All five studies were originated.

## The Governing Constraint — Every Service Says Who Actually Does It

A services list is the easiest section in this sector to write and the least useful. *Design and
build · groundworks · frame · fit-out · civils · refurbishment* is on every competitor's site and
distinguishes nobody.

**What does distinguish a contractor, and what almost none of them print, is which of those they do
with their own people and which they buy in.**

    Self-delivered · Managed, with a specialist · Joint

That marker is **real** (every firm knows the answer for its own list), **checkable** (a client can
ask on site), **uncopyable** (a firm that subcontracts everything cannot print it without saying
so), and it answers the question actually being asked — *can you do this one* means *whose hands,
and who carries it when it goes wrong.*

**Every study carries it**, and the checker verifies it — with one deliberate exception recorded
below.

## What Is Omitted, And Why

| Element | Treatment | Reasoning |
| --- | --- | --- |
| Project count or value per service | **Omitted** | An invented figure repeated six times over |
| Duration, programme, lead time | **Omitted** | The `WELL-S08` rule: a sequence is content, a schedule is a claim |
| Price, rate, *from £X* | **Omitted** | No price survives a scope nobody has walked |
| Certification or scheme per service | **Forbidden** | Sector direction |
| Client or project names | **Forbidden** | Sector direction |

**No digit appears in visible copy anywhere in the batch**, verified by scan, along with
thirty-seven patterns covering currency, percentages, per-square rates, lead times, *fast track*,
satisfaction, on-time and on-budget claim forms, zero-accident figures, certifications, ISO,
*approved contractor*, awards, ratings, reviews, testimonials, guarantees, *trusted by*, *leading*,
*market leader* and urgency devices. **Zero matches.**

## Study Records

### CON-S02-001 — Universal / Safe

- **Layout model:** One featured service across the full width, then a five-card grid. Every card is
  led by a large reserved project image with the service name, the delivery chip and one line of
  copy sitting beneath it.
- **Six large reserved media areas.** Project photography is this sector's only genuine asset, and a
  service without a picture of itself is a line in a list.
- **The chip does the work the paragraph used to do.** Name, chip, one sentence — the delivery fact
  is the second thing read on every card rather than the fifth.
- Closed by a single dark strip carrying the turn-down position in one line.

### CON-S02-002 — Premium / Editorial

- **Layout model:** Alternating bands — a tall reserved image on one side, the service on the other,
  the sides swapping down the page, with hairline separations and no card chrome.
- **The deliberate counter-proposal to `001`.** Same content, no cards, no chips: **the delivery
  fact is a small-caps line under the service name**, typographic rather than a badge, which is the
  editorial register's way of carrying it. *"Managed — a specialist erects, we carry it."*
- **The checker was made direction-aware for this.** `002` scores zero delivery chips, which is
  correct behaviour rather than a defect, so it is checked on the delivery **vocabulary** in prose
  instead of on the markup. **A rule a study may legitimately satisfy in a different medium needs a
  check that knows that** — the same lesson as the soft-tier scans in `WELL`, in a new form.
- One sentence per service, and the serif display voice carries the section rather than the copy
  volume.

### CON-S02-003 — Structured / Visual Modular

- **Layout model:** A twelve-column image mosaic at four tile sizes — one hero tile spanning two
  rows, one tall, four square, one wide — with the group label, service name and delivery chip
  riding on each image over a gradient veil, closed by a legend bar.
- **The structure is the tile size, not a table.** The sector direction names this direction's trap
  exactly — *a table of trades is not a design* — and a mosaic carries the same grouping through
  scale and position, so the hierarchy arrives before a word is read.
- **The legend still defines all three markers**, including the one nobody prints: *joint*, where
  the firm's labour works alongside a specialist and the line of responsibility is written down
  before anybody starts.
- **Correction made, recorded:** the first mosaic mixed aspect ratios across the grid, so row one
  did not tessellate and a hole opened under the wide tile. Rebuilt on explicit row spans with a
  fixed `grid-auto-rows` height. **An image mosaic tessellates on row spans, not on aspect ratios.**

### CON-S02-004 — Conversion-led

- **Layout model:** A wide reserved project image with a white decision card floating over its lower
  half — *we are right for this* against *ask somebody else* — above a row of service chips and one
  action.
- **The steer-away column keeps equal weight**, which is the study's whole argument: a visitor who
  leaves because the right-hand column described their job has been served better than one who
  enquires about work the firm would decline.
- **Eight one-line conditions instead of eight paragraphs.** Each is checkable against the reader's
  own project — *more than one trade*, *a building somebody is still using*, *a price before anybody
  has walked the job* — and none of them is an adjective.
- **Correction made, recorded:** the headline carried its measure on the wrapper, where `ch`
  resolves against 1rem rather than the display size, and broke to five lines. Moved onto the `h2`.

### CON-S02-005 — Art-directed / Distinctive

- **Layout model:** A large reserved project area with the line set over it under a gradient veil,
  above a six-cell stage rail carrying each stage's name, delivery chip and known failure.
- **The argument the layout makes without a sentence:** every other study presents the services as a
  menu, which is how a client thinks about them before they have built anything. This one presents
  them as **stages of one job** — you do not pick groundworks *or* frame, and the handover between
  them is where the money goes.
- **Not a schedule.** No durations, no weeks, no cell widths implying a programme. The cells are
  equal and the closing line says why: *"drawing them at different lengths here would be inventing a
  programme for a project nobody has seen."* The `WELL-S08` rule, with its reasoning visible.
- **Each cell carries the failure that stage is known for**, cut to a phrase — *the gap between two
  subcontractors*, *everybody in the same room at once*. The most useful thing a contractor can tell
  somebody who has not built before, and authorable because it describes the work rather than the
  firm's record.

## Structural Diversity

| Study | Topology | Reserved media | Delivery marker as | Ground |
| --- | --- | --- | --- | --- |
| 001 | Featured service + five-card image grid | 6, large | A chip beside the name | Soft grey `#f2f2f0` |
| 002 | Alternating image-and-text bands | 4, tall | **A small-caps line under the name** | Warm ivory `#f7f4ee` |
| 003 | Twelve-column image mosaic, four tile sizes | 7, varied | A chip on the image | Cool grey `#eceeef` |
| 004 | Image with a floating decision card | 1, wide | A chip in the closing row | Near-white `#fbfbfa` |
| 005 | Cinematic image stage + stage rail | 1, large | An outlined chip per stage | Near-black `#101215` |

## Research Metadata

- **Sources:** none supplied for this section; all five originated.
- **Research date:** 2026-09-03.
- **Visual-first check:** no study derives its distinctiveness from copy. The differentiator is what
  organises the list — cards, prose, position on the job, a decision, or the order of the build.
- **Document-metaphor justification:** `NONE`.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** No `<script>`, `<iframe>`, form control or inline `style` in any
  file.

## Media Slots

| Slot | Study | Expected Type | Rule attached to the slot |
| --- | --- | --- | --- |
| Service media x6 | 001 | Still image, one per service | The work itself; no stock handshake, no posed group in clean PPE |
| Service media x4 | 002 | Still image, 5:4, tall | One completed job each; a real project, not a render |
| Mosaic tiles x7 | 003 | Still image, four sizes | Labels ride on the image, so each needs a quiet upper area |
| Project media x1 | 004 | Still image, 21:9 | Completed work, wide; the card covers its lower half |
| Project media x1 | 005 | Still image, large | Work in progress; a veil carries the type over it |

Nineteen reserved areas across the batch, against two in the first pass. Every fill is a gradient
rather than flat grey so it reads as a photographic placeholder, and every dark tile carries a veil
so its label stays legible whatever photograph replaces it.

## QA

- ID validation: **PASS.** All five IDs match their filenames; `sector-prefix` is `CON` throughout.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport. Nesting validated with a stack-based parser.
- Territory validation: **PASS.** All five match the core `S01`–`S20` direction set.
- **Heading-level check: PASS.** No `<h1>` in any study — on a real page `S01` carries it and `S02`
  is a body section beneath. Each study is labelled by an `<h2>`. This is the `CON` sector's first
  body section, so the rule is set here for everything after it.
- Accessibility QA: **PASS.** `aria-labelledby`, `prefers-reduced-motion`, 52px targets on the two
  actions in the batch.
- Responsive QA: **PASS.** Verified at 1440px; each study states its ladder. `005`'s band folds
  6 → 3 → 2 → 1 with the build order preserved, which is the only thing that must survive.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.** No malformed hex, no accidental 8-digit hex, no `clamp()` arity
  error, no viewport-height unit.
- Section-shell check: **PASS.** No header, nav or footer.
- Scoped-CSS check: **PASS.**
- **Delivery-marker check: PASS — this batch's defining check.** Six markers in `001`, eleven in
  `003`, six in `004`, six in `005`, and ten prose statements in `002`. The *joint* marker is used
  and defined.
- **Fabricated-proof check: PASS.** Thirty-seven patterns, zero matches, no digit in visible copy.
- **Soft check, thirteen occurrences, all verified in context:** every *price*, *priced*,
  *estimator*, *programme* and *weeks* sits inside a refusal, a description of who does the work, or
  `005`'s explanation of why no programme is drawn.
- Render check: **PASS, after two corrections in the rewrite.** All five rendered in headless Chrome
  at 1440px and inspected; 003's mosaic tessellation and 004's headline measure were fixed, as
  recorded in the revision note above.

## Notes

- Second authored batch in the `CON` sector; `S01` and `S02` are now complete.
- **The reusable outcome is the delivery marker.** Any sector where the buyer's real question is
  *whose hands actually do this* — construction, agencies, managed IT, logistics, healthcare
  groups — has the same problem: an undifferentiated service list that every competitor also
  publishes. The fix is not better adjectives, it is **one honest attribute per line that a firm
  cannot print unless it is true.**
- The second outcome is a checker principle: **a rule that a study may satisfy in a different medium
  needs a check that knows that.** `002` states the delivery fact in prose rather than as a badge,
  which is a legitimate editorial choice and a zero score on the naive check. Making the check
  direction-aware, rather than forcing `002` to carry badges it deliberately rejects, kept both the
  rule and the study intact.
- `S03 Projects` is next in this sector — where the reserved-media discipline set in `S01` and the
  no-client-names rule will meet a portfolio.
- `WELL-S27` remains part-authored: four of five studies, no batch document, and its README says so.
