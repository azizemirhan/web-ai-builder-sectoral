# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S23`
- Section Name: `Treatment / Wellness Service Detail`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S23-001` | Universal / Safe | AUTHORED | `raw/WELL-S23-001.html` |
| `WELL-S23-002` | Premium / Editorial | AUTHORED | `raw/WELL-S23-002.html` |
| `WELL-S23-003` | Dense / Information-heavy | AUTHORED | `raw/WELL-S23-003.html` |
| `WELL-S23-004` | Conversion-led | AUTHORED | `raw/WELL-S23-004.html` |
| `WELL-S23-005` | Sector-native / Distinctive | AUTHORED | `raw/WELL-S23-005.html` |

Third batch in the extended architecture set. The section's role, its governing constraint and its
boundary with `S02` and `S08` are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint — Describe The Room, Not The Result

**This is the page in the whole sector where an efficacy claim is most likely to appear.** A
treatment detail page is the natural home of *"reduces fine lines"*, *"boosts circulation"*,
*"detoxifies"*, *"stimulates collagen"*. The rule for the batch, stated so it can be applied to any
sentence:

    Describe what happens in the room, and who it suits.
    Never describe what it will do to the person.

| Sentence | Verdict |
| --- | --- |
| *"Cleansed twice. Once to take the day off, once properly."* | **Real** — a description of events |
| *"The steam is warm rather than hot and you can say if it is too much."* | **Real** — the experience |
| *"For a first facial, or coming back after a long gap."* | **Real** — suitability |
| *"Reduces the appearance of fine lines."* | **Forbidden** |
| *"Detoxifies and rebalances."* | **Forbidden** — claim and pseudo-mechanism |

**The discovery is that the honest version is not the thinner one.** A description of what happens
to you, in order, is more persuasive than a promise about your skin — and it is entirely authorable,
because it is a statement about the studio's own practice rather than about a body it has not seen.
`005` takes this furthest and then names its own limit: *"That is where the description stops."*

Verified by scan across the batch: no *reduce*, *boost*, *detox*, *brighten*, *rejuvenate*,
*resurface*, *stimulate*, *collagen*, *toxins*, *firming*, *lifting*, *anti-ageing*, *wrinkle*,
*fine lines*, *pores*, *glow*, *radiance*, *clinically*, *proven*, *guarantee*, *dermatologist*,
*cure*, *heal*, *transform*, *renew*, *restore*, *before and after*, and no named condition —
*acne*, *rosacea*, *eczema*, *psoriasis*, *pigmentation* — anywhere in visible copy.

## The Money And Duration Fields — A Refinement Of The S11 Test

| Element | Treatment | Reasoning |
| --- | --- | --- |
| Price | **Reserved field**, in all five | Every treatment has one, so the empty field asserts nothing |
| How long it takes | **Reserved field**, in `001`, `003`, `004` | Same test — one overall duration is a property of the offering |
| Per-step timings | **Omitted** | The `S08` rule holds: a sequence is content, a schedule is a claim |
| Availability, turnaround | **Omitted** | The scaffold rules them out; an empty *"available from —"* asserts a booking system |
| Guarantee | **Omitted entirely** | A guarantee about a body is a claim no studio should print |

`S08` omitted durations because it was timing **each stage**. One overall duration on a detail page
is a field like the price. Recorded so the two sections do not look inconsistent.

## Heading Levels — A Small Decision With Consequences

Unlike every core section, **no study here carries an `<h1>`.** On a real page `S21` holds the page
title, `S22` the trail, and `S23` is the body beneath them — so this section's headings start at
`<h2>`, and the section is labelled by one. The checker enforces it. It is the first section in the
catalog where the *absence* of an `h1` is the correct answer, and it is a consequence of `S21` and
`S22` having been authored first.

## Study Records

### WELL-S23-001 — Universal / Safe

- **Layout model:** The described sequence and an includes/excludes pair in the main measure, with a
  supporting rail carrying reserved price and duration, one action, and a reserved media area.
- **The dependable shape**, and the one that shows the sequence as a labelled list — each step named
  in bold, described in plain words, no timings.
- **Responsive strategy:** the rail releases **below** the body at 900px rather than sitting beside
  a narrowed measure, which is what the scaffold asks of a supporting rail.

### WELL-S23-002 — Premium / Editorial

- **Layout model:** Long-form prose at a controlled measure — an opening paragraph at reading scale,
  three body paragraphs, one line pulled to display size, a wide reserved plate, the reserved price
  and one text action at the foot.
- **The counter-proposal to `001`: no lists anywhere.** The includes and excludes are said in
  sentences — *"There is no peel in it and no acid. Nothing is sold to you at the end"* — which is
  harder to write and much closer to how somebody actually decides.
- **The pulled line is the studio's own voice, not a quotation.** A testimonial here would be an
  invented person, and belongs to `S10` in any case.
- **Duration is not shown at all**, which is a legitimate editorial choice rather than an omission;
  three of the five studies carry it.

### WELL-S23-003 — Dense / Information-heavy

- **Layout model:** A four-item facts strip, then the sequence, includes against excludes, suits
  against ask-us-instead, and the conditions as native disclosures.
- **No media at all** — the density variant is the right place to prove the scaffold's requirement
  that the page is complete without any.
- **Why disclosures here:** the conditions are the part most visitors do not need and a few visitors
  badly need. Open by default they bury the description; behind script they are unreachable. Native
  `<details>` is the only option honest to both readers, and it satisfies the scaffold's rule that
  full content stays reachable without script.
- **The dense variant is where a claim would normally slip in as a bullet** — *"brightens"*,
  *"decongests"*. Every line in every list here is an event, a piece of practice, or a suitability
  statement instead.

### WELL-S23-004 — Conversion-led

- **Layout model:** A two-column decision panel — *book it if* against *ask us instead if* — above
  the reserved fields, one action, and the treatments this one can be booked alongside.
- **The steer away is the conversion device.** Half of deciding is finding out this is the wrong
  one, so the *ask us instead* column gets equal weight and names the cases where the studio would
  rather sell nothing.
- **"Can be booked alongside", not "often booked with".** The second is a frequency claim about real
  bookings; the first is a statement of what the studio permits. The named treatments come only from
  the established `S02` set.
- **What it avoids:** no urgency, scarcity, availability line, discount, course, plan,
  before-and-after, rating or testimonial — a treatment page is where all of them normally appear.

### WELL-S23-005 — Sector-native / Distinctive

- **Layout model:** The treatment written as **what happens to you**, second person, as a calm
  walkthrough beside one tall reserved media column.
- **Why this is sector-native:** in most sectors a detail page is a specification. Here, what
  somebody is deciding is whether they want to be in that room — and no list of inclusions answers
  that. So the study drops the specification and walks the visitor through the appointment.
- **The sharpest test of the batch rule, and the batch's best line.** The second person invites
  *"you will leave glowing"*. Instead the study stops at the door and says so: *"That is where the
  description stops. What your skin does afterwards is between you and your skin — we can tell you
  what we did and what usually helps, and we will not promise you a result."* **Naming the limit is
  the most persuasive sentence in the batch**, and it is the same move `S20` made with urgency.
- **Unnumbered on purpose:** numbering would turn an experience into a protocol, which the sector
  direction rules out.
- **Correction made, recorded:** the walkthrough's `54ch` measure inside a `1.5fr` column left about
  four hundred pixels of dead space before the media column — air in the wrong place reads as a
  mistake, not as calm. Rebuilt with `grid-template-columns: min(100%, 60ch) minmax(0, 1fr)` and a
  capped column width, so the pair sits together and the slack falls at the right margin where it
  reads as a margin. **A measure cap inside a fractional column produces a hole, not a margin.**

## Structural Diversity

| Study | Shape | Sequence shown as | Media | Reserved fields | Ground |
| --- | --- | --- | --- | --- | --- |
| 001 | Body + supporting rail | Labelled list | One 4:3 area | Price, duration | Pale sage `#f0f2ef` |
| 002 | Single prose measure | Prose | One 21:9 plate | Price | Warm ivory `#faf6f0` |
| 003 | Facts strip + four panels | Compact list | **None** | Price, duration | Cool grey-blue `#eaeef0` |
| 004 | Decision panel + adjacency | Not shown — suitability instead | One 16:9 area | Price, duration | Deep pine `#1a2b26` |
| 005 | Walkthrough + tall column | Second-person walkthrough | One 3:4 column | Price | Warm sand `#d9d2c8` |

**The same treatment, described five structurally different ways** — a list, a piece of prose, a
compact specification, a decision, and a walkthrough. Grounds do not repeat any used in
`WELL-S01`–`S22`; verified across all 115 studies.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-02.
- **Visual-first check:** no study derives its distinctiveness from copy. The differentiator is what
  form the description takes and where the decision sits.
- **Document-metaphor justification:** `NONE`.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** `003` uses native `<details>`/`<summary>`; every disclosure's
  content is present in the document with the disclosure closed. No `<script>`, `<iframe>`, form
  element or inline `style`.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| The treatment room | `001` — in the supporting rail | Still image, 4:3 | Empty tonal surface with a quiet label |
| The room, mid-treatment | `002` — after the prose | Still image, 21:9 | As above |
| The treatment room | `004` — beside the decision panel | Still image, 16:9 | As above |
| Hands, warm towel | `005` — tall column beside the walkthrough | Still image, 3:4 | As above |

**No study carries more than one media area, and `003` carries none.** Every page reads complete
with every slot empty, which is what the scaffold requires of supporting media.

## QA

- ID validation: **PASS.** All five IDs exist and match their filenames.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport. Nesting validated with a stack-based parser.
- Territory validation: **PASS.** All five match the extended-architecture set.
- **Heading-level check: PASS.** No `<h1>` in any study; each is labelled by an `<h2>`.
- Accessibility QA: **PASS.** `aria-labelledby`, `prefers-reduced-motion`, 46px-plus targets, every
  reserved field carrying a visually hidden label, native disclosures keyboard-operable by default.
- Responsive QA: **PASS.** Every supporting rail or column releases into normal flow before it
  competes with the body, as the scaffold requires; measures are controlled at wide widths.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.** No malformed hex, no accidental 8-digit hex, no `clamp()` with the
  wrong arity, no viewport-height unit.
- Section-shell check: **PASS.** No header, nav or footer — `S22`'s `<nav>` exemption does not
  extend to this section.
- Scoped-CSS check: **PASS.**
- **Claims check: PASS — this batch's defining check.** Thirty-five patterns covering efficacy,
  outcome, mechanism, ingredient action, regulated claims and named conditions. **Zero matches in
  all five.**
- **Figure check: PASS.** No digit in visible copy; no price, duration, availability, turnaround,
  rating, review, discount or offer.
- **Soft check, ten occurrences, all verified as refusals:** *sold a course*, *sold to you at the
  end*, *a course, or a plan to come back*, *we will not promise you a result*. The word *results*
  was moved from the hard list to the soft list for exactly this reason — **a study must be allowed
  to name the thing it is refusing to do.** Same lesson as `S20`'s urgency scan and `S22`'s chrome
  scan; this is the third batch to need it, so it is now a standing rule of the checker design.
- Render check: **PASS, after one correction.** All five rendered in headless Chrome at 1440px and
  inspected; `005`'s composition was rebuilt as recorded above.

## Notes

- Twenty-third authored batch in the `WELL` sector, twenty-first without references, third of the
  seven extended architecture roles.
- **The reusable outcome is the substitution rule: replace the claim with the description of
  events.** Every sector with a regulated or unprovable outcome — clinics, therapists, trainers,
  consultants, anyone selling a process rather than an object — can write a detail page this way,
  and it is *better* copy, not merely safer copy. What a visitor actually wants to know is what will
  happen to them, and that is knowable.
- The second outcome is `005`'s closing move: **naming the limit converts.** *"That is where the
  description stops"* is more convincing than any promise that could have gone in its place, and it
  is the same device as `S20`'s *"you will not find a countdown on this page"* and `S18`'s medical
  limits line. Three sections have now independently arrived at it, which makes it a sector pattern
  rather than a one-off.
- `S24` is next: Treatment Programme / Case Context Detail — and it will need the hardest version of
  this batch's rule, because a case study is a claim about an outcome by construction.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch,
  because `python3` on this machine resolves to a Windows Store placeholder rather than an
  interpreter.
