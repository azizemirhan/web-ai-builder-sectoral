# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S14`
- Section Name: `About Philosophy`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S14-001` | Universal / Safe | AUTHORED | `raw/WELL-S14-001.html` |
| `WELL-S14-002` | Premium / Editorial | AUTHORED | `raw/WELL-S14-002.html` |
| `WELL-S14-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S14-003.html` |
| `WELL-S14-004` | Conversion-led | AUTHORED | `raw/WELL-S14-004.html` |
| `WELL-S14-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S14-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's role, its governing constraint and its boundary
with `S07` and `S04` are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint

An about section is the classic home of invented facts: a founding year, a founder's name, a number
of years, a city, a headcount, an origin anecdote. None of it is authorable.

Applying the `S11` field-versus-figure test:

| Element | Treatment |
| --- | --- |
| Founding year | **Reserved slot** — every studio has one, so the empty field asserts nothing (`001`) |
| Founder portrait | **Reserved media slot**, on the `S04` rule (`002`) |
| A founder quotation | **Reserved quotation area**, on the `S10` rule, attributed to the token *The founder* (`002`) |
| Years of experience, headcount, guests treated | **Omitted entirely** — a figure that also carries a credential or scale claim |
| An origin story | **Omitted entirely** — not a field at all, but prose that would have to be invented outright |

**What is real, and it is the whole point of the section.** Every other `WELL` section carries one
operating-policy line as its only unreserved content — `S07` commitments, `S08` sequence, `S09`
inspection, `S10` gathering, `S11` pricing, `S12` behaviour. **`S14` is where the reasoning behind
those lines lives.** An argument is not a fact: a studio can genuinely hold a position without a
placeholder inventing anything, so the beliefs — and the trade-offs they cost — are honest content.

> `S07` says: one guest at a time.
> `S14` says: because a room with someone being shown in and out of it is not a quiet room, and we
> would rather earn less than sell that.

**Every belief in this batch is stated with what it costs the business.** That is the device the
whole section turns on: nobody writes down what a position costs them unless the position is real,
so the cost line is the part that cannot be faked by accident. It also gives the section something
`S07` does not have, which keeps the two from becoming the same list at two lengths.

**Not present in any study:** an invented founding year, founder name, personal history, origin
anecdote, city, address, headcount, years of experience, number of guests, award, qualification,
press mention or membership; a superlative or any characterisation of other studios; an efficacy
claim. A scan for **any digit in visible copy** returns nothing across all five.

## The Belief Set

| Belief | Which produces | Which costs |
| --- | --- | --- |
| Quiet is the product, not the treatment | One guest in the building at a time | Roughly half of what a day could take |
| A treatment is a conversation, not a service received | Everything decided in the room and changed as it goes | No two appointments take the same shape |
| Nobody should be sold to lying down | Product suggestions afterwards, standing up | A fraction of the retail a spa this size would take |
| Committing should not be a trap | No bundle discount, nothing auto-renewing, sessions that do not expire | Bundles are harder to sell with no saving attached |

Each conclusion is checkable against another section of this same catalog, which is what `004`
makes its argument out of.

## Study Records

### WELL-S14-001 — Universal / Safe

- **Layout model:** A split opening — position statement beside a reserved media panel, with a
  reserved founding-year field — above three belief blocks, each running belief, consequence and
  cost.
- **The reserved founding year** is the batch's demonstration of the field-versus-figure test in an
  about section: the year is reserved, while years-of-experience and headcount are omitted, because
  the second pair carry a credential and a scale claim that the first does not.
- **Responsive strategy:** three belief columns → two with the last spanning → one; the opening
  unstacks at 768px with the media becoming 16:9.
- **Visual-first check:** 188 visible words.

### WELL-S14-002 — Premium / Editorial

- **Layout model:** A 24:7 reserved plate across the top, then a single 40rem serif reading column
  — the only genuine long-form composition in the sector — with a reserved founder quotation and
  portrait set into the middle of it.
- **Reserved quotation:** the founder quote follows the `S10` rule exactly. The area is sized and
  labelled, the attribution is the token *The founder*, and the portrait beside it is a reserved
  slot on the `S04` consent rule.
- **Density, stated honestly:** at **281 visible words** this is by some way the longest study in
  the sector. That is the role rather than padding — `WELL-S13` carries 70 because a gallery has
  nothing to say, and this carries 281 because a philosophy section has nothing else. The failure
  the sector must not repeat is `ARC-S23` at 630 words in a section whose subject was not prose at
  all. Each paragraph here makes a distinct argument and names a distinct cost; none restates
  another.
- **Responsive strategy:** the plate steps 24:7 → 21:8 → 16:9 → 4:3; the column unlocks its measure
  at 768px and the quotation unstacks at 480px.

### WELL-S14-003 — Structured / Visual Modular

- **Layout model:** Four reasoning chains. Each belief is three steps at increasing indent — *we
  think*, *so*, *which costs us* — so the structure of the page is the structure of the argument.
- **How it avoids a matrix:** three parts per belief is one step from a three-column table. What
  keeps it modular is that the steps are **stepped, not aligned** — each indented further than the
  last, at a different type size and weight, with a hairline on the second step only. The eye reads
  down a derivation rather than across a row, and nothing lines up between one belief and the next.
- **Responsive strategy:** the derivation keeps its three steps at every width; only the indent
  intervals compress, from 68px/136px down to 14px/26px.
- **Visual-first check:** 226 visible words.

### WELL-S14-004 — Conversion-led

- **Layout model:** An argument panel carrying the action, beside a list of five refusals — each
  naming something the studio decided not to do and what it means for the visitor.
- **Conversion device:** an about section normally converts by claiming things. This one converts
  by **naming what it gave up**. Each refusal costs the business something, so nobody writes them
  unless they are true — and each is **checkable against another section of this catalog**: no
  selling in the room against `S07`, no bundle discount against `S12`, no stated durations against
  `S08`, no rating scores against `S10`. The panel says so explicitly: *if you find us doing any of
  it, we have got something wrong.* That cross-checkability is the argument.
- **What it avoids:** the refusals describe this studio's own choices and never characterise anyone
  else's, so nothing becomes a comparative claim about other spas.
- **Visual-first check:** 243 visible words.

### WELL-S14-005 — Art-directed / Distinctive

- **Layout model:** One sentence at up to 5rem filling most of the section, with three short cost
  lines at the foot and a reserved media area bled off the right edge behind the type at a close
  tone.
- **The pairing with `002`:** these two were authored as deliberate opposites. `002` is a 281-word
  reading column; this is the same argument compressed to one sentence. Between them they mark the
  two ends of the only real decision this section has — **how much prose is on screen at once** — so
  a reviewer picks a point on that axis rather than a style.
- **What keeps it from being a slogan:** the three foot lines name what the position means, what it
  costs and how firmly it is held. A display-scale sentence alone would be a claim shape.
- **Responsive strategy:** the bled ground becomes a normal-flow band below the sentence at 768px
  rather than being dropped, so the composition keeps its second element at phone width.
- **Visual-first check:** 65 visible words, the fewest in the batch by a wide margin.

## Structural Diversity

| Study | Topology | Prose on screen | Media | Ground |
| --- | --- | --- | --- | --- |
| 001 | Split opening above three belief blocks | 188 words | One panel + founding field | Pale cool grey |
| 002 | Wide plate above a serif reading column | 281 words | Plate, portrait, quotation area | Warm paper |
| 003 | Four stepped reasoning chains | 226 words | None | Muted teal-grey |
| 004 | Argument panel beside five refusals | 243 words | None | Deep charcoal-plum |
| 005 | One display-scale sentence over a bled ground | 65 words | One bled area | Light terracotta-clay |

Grounds do not repeat any used in `WELL-S01`–`S13`.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-01.
- **Visual-first check:** 65–281 visible words — the widest spread in the sector, and deliberately
  so. This is the one section whose subject is prose, so the batch composes on quantity of prose
  rather than on imagery. `005` proves the argument survives compression; `002` proves it rewards
  length.
- **Document-metaphor justification:** `NONE`. No manifesto plate, charter, mission statement panel
  or values register is used. `003`'s stepped derivation is a reading device, not a document form.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** No `<script>` element and no inline `style` attribute in any file.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| The studio | `001`, `002` | Still image, 4:3 and 24:7 | Empty tonal surface with a quiet label |
| Founder portrait | `002` | Still image, 1:1 | **A filled slot means a real person who has consented to appear** |
| Founder quotation | `002` | **Text**, replaced by a `<blockquote>` | Sized, labelled region; attribution is the token *The founder* |
| Founding year | `001` | **Text** | Em dash with a visually hidden "Year the studio opened" label |
| The room | `005` | Still image, bled off the right edge | Empty tonal surface set close to the paper so it reads as ground rather than illustration |

`003` and `004` carry no media at all, deliberately: a chain of reasoning and a list of refusals are
text arguments, and a photograph beside either is decoration.

## QA

- ID validation: **PASS.** All five IDs exist and match their filenames.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport. Nesting validated with a stack-based parser; all five parse correctly.
- Accessibility QA: **PASS.** `lang`, scoped `:focus-visible`, `aria-labelledby`,
  `prefers-reduced-motion`, and 44px-plus targets throughout. The reserved founding-year and
  quotation areas carry visually hidden field labels; `005`'s bled ground is `aria-hidden`.
- Responsive QA: **PASS.** Breakpoints authored per study and recorded above — including `003`'s
  decision to keep all three indent steps at phone width and `005`'s decision to reflow its bled
  ground rather than drop it.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image, script or
  inline style.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status.
- Scoped-CSS check: **PASS.** Every declaration outside the host baseline is namespaced to the
  study's own `.well-s14-00N` root.
- **About-page fabrication check: PASS.** This batch's defining check. Visible text only, comments
  stripped, scanned for *founded in*, *since <year>*, any four-digit year, *N years*, headcounts,
  *award*, *certified*, *qualified*, *accredited*, *member of*, *featured in*, *as seen*, *best*,
  *leading*, *finest*, *number one*, *unlike other*, *most spas*, currency, percentages, and **any
  digit at all**. Zero matches in all five.
- Boundary check: **PASS.** No study restates `S07`'s commitments as a list. Where a commitment
  appears it is the conclusion of an argument or an item in a list of refusals, both of which carry
  content `S07` does not.
- Render check: **PASS, no corrections.** All five rendered in headless Chrome at 1440px and
  inspected. `005`'s bled ground reads as ground rather than illustration, and its sentence holds
  the composition; `003`'s indents read as a derivation. Seventh batch in eight to need no render
  correction.

## Notes

- This is the fourteenth authored batch in the `WELL` sector and the twelfth authored entirely
  without references.
- **The cost line is the reusable outcome.** Every sector has an about or philosophy section, and
  every one is a fabrication magnet. Stating what a position costs the business is authorable
  without inventing anything, differentiates without a superlative, and is self-policing — a
  fabricated cost reads as false immediately, which is why writing them keeps the section honest.
- `S14` completes the group it belongs to: `S07` states the commitments, `S08` gives the order,
  `S14` gives the reasoning, and `S04` gives the people.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a placeholder rather than an
  interpreter. Headless Chrome, which the generator uses for measurement, is present and working.
