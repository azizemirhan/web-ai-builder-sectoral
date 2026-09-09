# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S12`
- Section Name: `Memberships Packages`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S12-001` | Universal / Safe | AUTHORED | `raw/WELL-S12-001.html` |
| `WELL-S12-002` | Premium / Editorial | AUTHORED | `raw/WELL-S12-002.html` |
| `WELL-S12-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S12-003.html` |
| `WELL-S12-004` | Conversion-led | AUTHORED | `raw/WELL-S12-004.html` |
| `WELL-S12-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S12-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's role, its governing constraint and its boundary
with `S11` and `S17` are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint

`S11` established the test: **reserve the field when the empty field asserts nothing; omit it when
the empty field asserts a system.** This section applies it three times and adds one prohibition
the test does not cover.

| Element | Test | Treatment |
| --- | --- | --- |
| Package price | A packages section exists because packages have prices | **Reserved slot** |
| Session count | A course by definition bundles a quantity | **Reserved slot** |
| Membership rhythm | A membership by definition has a rhythm | **Reserved slot** |
| A saving or package value | — | **Forbidden outright** |

**Why a saving is forbidden rather than reserved.** A price is one figure; a saving is a
*relationship between two figures* — the bundle price against the same treatments bought
separately — so reserving it would reserve a claim rather than a number. Worse, an empty
"you save —" field asserts that this studio discounts bundles at all, which is a commercial policy
many studios deliberately do not have. That is the same failure as `S10`'s empty star row.

The batch turns that prohibition into a position rather than an absence. All five studies close on
the same line:

> *None of the three is cheaper for being bought together. They exist so you can stop thinking
> about booking, not so you can chase a deal.*

**No comparison matrix.** The tick-grid tier table is the default device for this role on the open
web, and it is a specification matrix, which the sector direction rules out. `S11` argued that a
price list is the native form of a pricing section and therefore allowed; **that argument does not
extend here**, because a comparison matrix is not the native form of a membership — it is the
native form of software pricing. Verified by scan: no `<table>` element in any study.

**Not present in any study:** an invented price, session count, term length, currency symbol,
saving, discount, percentage, package value, "worth" figure, RRP, "was/now" pair, joining fee,
minimum term, notice period or expiry date; a "most popular", "best value" or "recommended" badge;
a per-month or per-session rate; an auto-renewal term. A scan for **any digit at all in visible
copy** returns nothing across all five studies.

**What is real.** Two things: the **generic commercial forms** — naming a form is not inventing a
product — and **how the arrangements behave**, written deliberately without numbers so no term is
invented in the act of stating the policy.

## The Three Forms

| Form | What it is |
| --- | --- |
| A course | The same treatment, booked as a series and paid for once |
| A mixed course | A set of visits to spend across the menu, decided as you go |
| A membership | One visit on a regular rhythm, running on until you stop it |

**They differ in distribution over time, not in value** — bounded and regular, bounded and
irregular, unbounded. That is the axis this batch composes on, and it is the one thing a layout can
show without stating a number.

## Study Records

### WELL-S12-001 — Universal / Safe

- **Structural intent / archetype:** The three forms as three cards, plainly set.
- **Layout model:** A split header, three cards each naming the form, describing it in a line,
  carrying its own reserved fields, listing three behaviours on hairlines, and ending in an action.
- **The one decision that matters:** each card reserves **different fields** — a course has a visit
  count, a membership has a rhythm. A uniform field set across the three would have produced a
  comparison matrix by accident, which is exactly what this section may not do.
- **Responsive strategy:** 3 → 2 cards with the third spanning full width, then one column with the
  action going full width.

### WELL-S12-002 — Premium / Editorial

- **Structural intent / archetype:** A membership section is a **proposition, not a product**.
- **Layout model:** One arrangement — the membership — given a serif proposition with its reserved
  fields inline on a hairline and its behaviour spelled out across three columns, with the other
  two forms following as a quiet pair beneath.
- **Why featuring one is not a badge:** the study argues for a form in the studio's own voice and
  says so. It carries no *recommended* label, which would assert what other people chose.
- **Responsive strategy:** the behaviour row steps 3 → 2 → 1; the pair unstacks at 768px.

### WELL-S12-003 — Structured / Visual Modular

- **Structural intent / archetype:** Three panels shaped like what they are.
- **Layout model:** Each panel has a **different internal anatomy** matched to its form — a repeat
  block for the course (the same treatment name listed down, closing on an open marker), a chooser
  block for the mixed course (category pills), and a recurrence block for the membership (what
  happens if you pause, miss one, stop).
- **How it avoids the anti-pattern:** this is the `WELL-S09-003` move applied to a role whose
  default device is explicitly forbidden. Nothing aligns across the three panels because nothing
  compares across them, and the header says so in the visible copy.
- **Responsive strategy:** 3 → 2 panels with the third spanning full width, then one per row.

### WELL-S12-004 — Conversion-led

- **Structural intent / archetype:** The exit as the headline.
- **Layout model:** A cream panel answering what happens if you pause, miss one, stop, or have paid
  ahead — carrying the action and a secondary route to a single treatment — beside the three
  arrangements listed compactly on the dark ground.
- **Conversion device:** the barrier to committing to a series is not price, it is **being locked
  in**. So the panel that carries the action answers what happens when circumstances change: four
  operating commitments the studio controls and can keep. There is no saving, no limited-time offer
  and no urgency — a discount would be a claim about two figures, and urgency would be an invented
  diary state.
- **The secondary route is the honest one:** *book a single treatment and decide later.* A section
  selling commitment that does not offer the uncommitted option is not being straight.
- **Responsive strategy:** the split unstacks at 1024px; the action goes full width at 768px.

### WELL-S12-005 — Art-directed / Distinctive

- **Structural intent / archetype:** Show the difference instead of stating it.
- **Layout model:** Three wide strips, one per arrangement, each carrying a different repeating
  rhythm — even and end-capped, irregular and end-capped, and even but **masked to fade off the
  right edge**.
- **Why the device is honest, and why it is not dots:** drawing the distribution as a row of
  discrete marks would state a count — six dots is six visits — which this batch may not invent. A
  **repeating gradient has no count**: its marks are a function of the strip's width, so it reads as
  *regular*, *irregular* or *ongoing* without asserting a number. The fade is what says "runs on"
  rather than "ends here", and the end cap on the other two is what says "ends".
- **Fallback:** if a browser does not support `mask-image`, the membership strip simply does not
  fade — it is still the only strip without an end cap, so the distinction survives.
- **Responsive strategy:** the gradient periods tighten at 768px, but all three rhythms and the
  capped/uncapped distinction are kept at every width.

## Structural Diversity

| Study | Topology | Reserved slots | What differentiates the forms |
| --- | --- | --- | --- |
| 001 | Three cards with per-form fields | 6 | Different field sets per card |
| 002 | Featured proposition above a quiet pair | 6 | Rank — one argued, two stated |
| 003 | Three panels, three internal anatomies | 6 | The panel's internal shape |
| 004 | Exit panel beside a compact list | 6 | The exit, not the offer |
| 005 | Three rhythm strips | 6 | The rhythm itself, drawn |

Grounds: pale rose-grey, warm mid-taupe, pale periwinkle, deep bronze-brown, deep charcoal-blue.
None repeats a ground used in `WELL-S01`–`S11`.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-01.
- **Structural direction rationale:** recorded per study above.
- **Differentiation notes:** recorded in *Structural Diversity* above.
- **Visual-first check:** no study derives its distinctiveness from copy. `005` in particular
  carries the least text in the batch and the most information, because the rhythm strips do work
  the words would otherwise have to do.
- **Document-metaphor justification:** `NONE`. No tier comparison matrix, rate table, contract
  schedule or terms document is used — see *The Governing Constraint*.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** All five studies are fully static. No `<script>` element and no
  inline `style` attribute appears in any file. `005`'s rhythms are CSS repeating gradients and a
  CSS mask — no images, no canvas, no script.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Price slot ×15 | All five — one per arrangement | **Text**, replaced by the real figure and its currency | Em dash in a quiet chip with a visually hidden "Price" label |
| Visit-count slot ×10 | The course and mixed course in each study | **Text** | Em dash with a visually hidden "Number of visits" label |
| Rhythm slot ×5 | The membership in each study | **Text** | Em dash with a visually hidden "Visit rhythm" label |

Thirty reserved slots across the batch, six per study, all labelled — verified by scan. This batch
carries **no media at all**: the subject is a commercial arrangement, and a photograph says nothing
about how visits are distributed over time.

## QA

- ID validation: **PASS.** All five planned IDs exist; every `study-id` meta matches its filename.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport in every study. Nesting validated with a stack-based parser over comment-stripped
  markup; all five parse correctly.
- Accessibility QA: **PASS.** Every study sets `lang`, scopes a `:focus-visible` ring, labels its
  section with `aria-labelledby`, honours `prefers-reduced-motion`, and gives every interactive
  element a 44px-or-greater target. All 30 reserved slots carry a visually hidden field label, so
  no assistive technology encounters a bare em dash. `005`'s rhythm strips are `aria-hidden`
  decorative elements; the same information is in each strip's sentence.
- Responsive QA: **PASS.** Breakpoints authored per study and recorded above.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image, script or
  inline style.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status.
- Scoped-CSS check: **PASS.** Every declaration outside the `html` / `body` host baseline is
  namespaced to that study's own `.well-s12-00N` root, verified by scan.
- **Saving, term and matrix check: PASS.** This batch's defining check. Visible text only, comments
  stripped, scanned for every currency symbol, for *save*, *saving*, *worth*, *discount*, *RRP*,
  *joining fee*, *minimum term*, *notice period*, *most popular*, *best value*, *recommended*,
  per-month/week/year/session rates, *auto-renew*, percentages, and **any digit whatsoever**. Zero
  matches in all five. A separate scan for `<table>` returns nothing, confirming no comparison
  matrix. The only expiry-related matches are the phrase *do not expire* — a policy commitment that
  sessions have no expiry, not an invented expiry date.
- Render check: **PASS, no corrections.** All five rendered in headless Chrome at 1440px and
  inspected. `005`'s three rhythms are immediately distinguishable in render — even and capped,
  irregular and capped, even and fading off the right edge — which is the whole argument of the
  study, and the mask renders correctly. Fifth batch in six to need no render correction.

## Notes

- This is the twelfth authored batch in the `WELL` sector and the tenth authored entirely without
  references.
- **The rhythm device is the reusable outcome.** Any section whose subject is a quantity a
  placeholder may not invent — visits, sessions, capacity, frequency, headcount — can express the
  *shape* of that quantity with a repeating gradient rather than discrete marks, because a gradient
  has no count. That is a general answer to a general problem, and `S12-005` is where it was found.
- Five sections in this sector now carry an operating-policy line as their only unreserved content:
  `S07` commitments, `S09` inspection, `S10` gathering, `S11` pricing, `S12` behaviour. Together
  they are the studio's voice and the part of a placeholder catalog that is actually true.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a placeholder rather than an
  interpreter. Headless Chrome, which the generator uses for measurement, is present and working.
