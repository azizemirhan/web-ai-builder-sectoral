# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S11`
- Section Name: `Pricing`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S11-001` | Universal / Safe | AUTHORED | `raw/WELL-S11-001.html` |
| `WELL-S11-002` | Premium / Editorial | AUTHORED | `raw/WELL-S11-002.html` |
| `WELL-S11-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S11-003.html` |
| `WELL-S11-004` | Conversion-led | AUTHORED | `raw/WELL-S11-004.html` |
| `WELL-S11-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S11-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's role, its governing constraint, the tariff
question and its boundary with `S02` and `S12` are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint — And Why It Differs From S10

`S10` established that **a figure cannot be meaningfully reserved** and omitted star ratings on
that basis. A price is also a figure, so at first reading the rule forbids this section outright.
It does not, and the difference is the distinction that makes the role authorable:

| | An empty star row | An empty price |
| --- | --- | --- |
| What the empty field asserts | That this studio **runs a rating system** and holds scores in it | Nothing. Every spa charges money. |
| Is the assertion safe? | **No** — the studio may collect no ratings at all | **Yes** — the section exists because prices exist |

**The price is reserved, not omitted.** What is forbidden is the *figure*, not the field. The test
is whether the empty field itself makes a claim: a price field does not, a rating field does.

**How a price is reserved.** As a price slot — an em dash set at the type size the real figure will
occupy, inside a quiet chip, with a **visually hidden "Price" label** so assistive technology is
told what the field is rather than reading a bare dash. Verified by scan: 37 price slots across the
batch, 37 labelled.

**No currency symbol appears anywhere**, because a symbol would invent a market. Verified by scan
across all five files.

**Not present in any study:** an invented price, figure, range, currency symbol, deposit,
consultation fee, cancellation charge, tax statement, package value, saving, discount, "was/now"
pair or membership term; a duration or session count; a "most popular", "best value" or
"recommended" badge. A scan for **any digit at all in visible copy** returns nothing in all five
studies.

**Emphasis is allowed; a popularity claim is not.** `004` makes one treatment visually prominent —
a composition decision — and frames it as *where we would start you*, which is the studio's own
advice. It carries no popularity badge, because that would assert real purchase data a placeholder
does not have.

**What is real.** The pricing policy — the price shown is the price paid, nothing is added at the
desk, a shorter treatment costs less, moving an appointment costs nothing — is a fact about the
studio, in the same family as the `S07` commitments, the `S09` inspection offer and the `S10`
gathering policy. It is the only unreserved content in the batch.

## The Tariff Question

`../WELLNESS-DESIGN-DIRECTION.md` lists *"tariff sheets and price registers that occupy most of the
layout"* among the sector's anti-patterns. That rule forbids a tariff as a **default styling device
in sections that are not about price**. In `S11` a legible price list is the role, and refusing to
list prices here would be avoiding the section rather than authoring it.

What the anti-pattern still rules out, and what this batch holds to: **no dense multi-column rate
matrix, no per-row duration column, no tax or terms column, and no layout where the figures crowd
out the treatment names.** `003` came closest — a "what it covers" line per row could easily have
become a third column — and it stacks that tier *under* the row instead, carries no duration
column, and keeps one figure per row. A price list is a list; a rate matrix is paperwork.

## The Axis This Batch Records

Every design decision in a pricing section is the same decision: **how loud is the figure next to
what it buys.** The five studies were authored to sit at five points on that axis, so a reviewer
picks a position rather than a style.

| Study | Name scale | Price scale | Reading |
| --- | --- | --- | --- |
| `002` | Serif display, up to 2.8rem | Small chip in a footnote line | The price is present because you should know it, not because it is the point |
| `001` | List scale | Matched to the name | The conventional balance — scan the name, scan the number |
| `003` | Card scale | Matched, with an inclusion line beneath | The number plus what it buys |
| `004` | Promoted panel vs list rows | **Two scales in one study** — large in the panel, small in the list | Relative prominence used as the ranking device |
| `005` | Small uppercase label | Display scale, up to 5.4rem | The figure is the subject |

`002` and `005` are deliberate inverses and were authored as a pair.

## Study Records

### WELL-S11-001 — Universal / Safe

- **Structural intent / archetype:** The price list in its native form, done properly.
- **Layout model:** A split header carrying the policy, above four category groups laid across two
  columns as ruled rows — name left, reserved price slot right, aligned on a baseline — closed by
  a three-column policy row.
- **Media relationship:** None, deliberately: this role is a name-and-number relationship and a
  picture per row would push the figures off the line they need to align on.
- **Responsive strategy:** Two columns of groups become one at 768px; the policy row steps 3 → 2 → 1.
- **Visual-first check:** ten treatments, ten reserved slots.

### WELL-S11-002 — Premium / Editorial

- **Structural intent / archetype:** The price demoted.
- **Layout model:** Five treatments as large serif names on hairlines, with the reserved price slot
  beneath each as a small labelled line rather than beside it as a figure to scan.
- **What the study records:** that a spa can publish prices without letting them set the tone. Five
  treatments where `001` lists ten, at roughly twice the name scale.
- **Responsive strategy:** measures unlock at 768px; row padding tightens at 480px.

### WELL-S11-003 — Structured / Visual Modular

- **Structural intent / archetype:** The price plus what it covers.
- **Layout model:** Three category panels of two-tier rows — name and reserved price on the top
  line, and beneath a hairline, one line saying what happens for that price.
- **Content-capacity justification:** the capacity is the second tier, stacked under the row rather
  than added as a column. That placement is what keeps it a list rather than a rate matrix — see
  *The Tariff Question*.
- **Copy rule:** the inclusion lines describe what happens in the room, following the `S02`
  procedural rule, never what a treatment achieves.
- **Responsive strategy:** 3 → 2 panels with the third spanning full width, then one per row.

### WELL-S11-004 — Conversion-led

- **Structural intent / archetype:** An entry point, not a recommendation about what others bought.
- **Layout model:** One treatment promoted to a cream panel with a large reserved price slot and
  the action, beside a compact list of everything else at list scale.
- **Conversion device:** a visitor who does not know the sector cannot choose from a list, so the
  study answers "where do I start?" rather than "which is best". The framing is *where we would
  start you* — the studio's own advice, which it can stand behind — and there is deliberately **no
  popularity or value badge**.
- **The scale difference is the argument:** the promoted slot is roughly three times the list slots.
  Relative price prominence is exactly what this direction is deciding, so the study carries two
  price scales at once.
- **Responsive strategy:** the split unstacks at 1024px; the action goes full width at 768px.

### WELL-S11-005 — Art-directed / Distinctive

- **Structural intent / archetype:** The figure made the subject.
- **Layout model:** Six reserved price slots at up to 5.4rem in a staggered two-column rhythm, with
  the treatment name reduced to a small uppercase label above each — the inverse of `002`.
- **Why the reservation does the most work here:** at this scale the slot's width is what tells a
  reviewer whether a three-figure number will fit the composition. That is a question a fabricated
  price would answer falsely and an honest reservation answers correctly.
- **Responsive strategy:** the stagger goes at 768px and the display scale is reduced twice, but
  the price-as-subject hierarchy is kept at every width — the rhythm is negotiable, the hierarchy
  is the study.

## Structural Diversity

| Study | Topology | Treatments | Price slots | Ground |
| --- | --- | --- | --- | --- |
| 001 | Two-column grouped ruled list | 10 | 10, matched scale | Pale butter |
| 002 | Serif list, price demoted beneath | 5 | 5, small | Warm mid-grey |
| 003 | Three panels of two-tier rows | 8 | 8, matched scale | Pale cool mint |
| 004 | Promoted panel beside a compact list | 8 | 8, at two scales | Deep indigo |
| 005 | Staggered display-scale figures | 6 | 6, display scale | Warm black |

Grounds do not repeat any used in `WELL-S01`–`S10`.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-01.
- **Structural direction rationale:** recorded per study above.
- **Differentiation notes:** recorded in *The Axis This Batch Records* and *Structural Diversity*.
- **Visual-first check:** no study derives its distinctiveness from copy; the differentiator across
  the batch is type scale and the name-to-figure ratio.
- **Document-metaphor justification:** `NONE`. No rate matrix, tariff sheet, invoice, quotation
  document or terms schedule is used — see *The Tariff Question*.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** All five studies are fully static. No `<script>` element and no
  inline `style` attribute appears in any file in this batch.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Price slot ×37 | All five studies — one per treatment, at the study's chosen scale | **Text**, replaced by the real figure and its currency | Em dash in a quiet chip, with a visually hidden "Price" label so the field is announced. The chip's size is the design information: it shows how much room the real figure gets |

This batch carries **no media at all**. That is deliberate and consistent across the five: the role
is a relationship between a name and a number, and every study spends its composition on that ratio
rather than on imagery. `S02` is where these treatments are shown; `S11` is where they are priced.

## QA

- ID validation: **PASS.** All five planned IDs exist; every `study-id` meta matches its filename.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport in every study. Nesting validated with a stack-based parser over comment-stripped
  markup; all five parse correctly.
- Accessibility QA: **PASS.** Every study sets `lang`, scopes a `:focus-visible` ring, labels its
  section with `aria-labelledby`, honours `prefers-reduced-motion`, and gives every interactive
  element a 44px-or-greater target. **Every one of the 37 price slots carries a visually hidden
  "Price" label**, so no assistive technology encounters a bare em dash — verified by scan.
- Responsive QA: **PASS.** Four authored breakpoints per study, recorded per study above.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image, script or
  inline style.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status.
- Scoped-CSS check: **PASS.** Every declaration outside the `html` / `body` host baseline is
  namespaced to that study's own `.well-s11-00N` root, verified by scan.
- **Figure and currency check: PASS.** This batch's defining check, and the strictest scan run in
  the sector: visible text only, comments stripped, scanned for **any digit whatsoever**, for every
  currency symbol, and for *was/now*, *save*, *discount*, *deposit*, *fee*, *VAT*, *tax*,
  *most popular*, *best value*, *recommended*, per-session or per-month phrasing, and durations.
  **Zero digits in visible copy across all five studies. Zero currency symbols.** One match for
  *offer* was reviewed and is the verb — "everything we offer, with what it costs beside it" — not
  a promotional offer.
- Render check: **PASS, no corrections.** All five rendered in headless Chrome at 1440px and
  inspected. `004`'s two price scales read correctly against each other, and `005`'s display-scale
  slots hold their staggered rhythm. Fourth batch in five to need no render correction.

## Notes

- This is the eleventh authored batch in the `WELL` sector and the ninth authored entirely without
  references.
- **The field-versus-figure test is the reusable outcome.** `S10` and `S11` look like the same
  problem and are not: reserve the field when the empty field asserts nothing, omit it when the
  empty field asserts a system. That test settles ratings, prices, review counts, capacity figures,
  years-in-business and every other number a placeholder is tempted to invent — and it applies to
  every sector in the catalog, not just this one.
- Four sections in this sector now carry an operating-policy line as their only unreserved content:
  `S07` commitments, `S09` inspection, `S10` gathering, `S11` pricing. Together they are the
  studio's voice, and they are the part of a placeholder catalog that is actually true.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a placeholder rather than an
  interpreter. Headless Chrome, which the generator uses for measurement, is present and working.
