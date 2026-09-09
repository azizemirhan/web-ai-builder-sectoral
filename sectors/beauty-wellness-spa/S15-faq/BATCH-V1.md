# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S15`
- Section Name: `FAQ`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S15-001` | Universal / Safe | AUTHORED | `raw/WELL-S15-001.html` |
| `WELL-S15-002` | Premium / Editorial | AUTHORED | `raw/WELL-S15-002.html` |
| `WELL-S15-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S15-003.html` |
| `WELL-S15-004` | Conversion-led | AUTHORED | `raw/WELL-S15-004.html` |
| `WELL-S15-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S15-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's role, its governing constraint and its boundary
with `S06`, `S14` and `S19` are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint — And The Move That Resolves It

An FAQ has to answer what people actually ask, and in this sector several of those questions ask
for exactly what the catalog may not invent: **how long does it take, how much is it, when are you
free.** The easy failure is to leave them out, producing an FAQ that answers only what was
convenient.

> **The FAQ names the questions it will not answer in writing, and says why.**

    "How long will it take?"
    "We do not print a length, on purpose. It depends on what we find once we start, so we agree it
    with you in the room rather than giving you a number you would then be held to."

That is not a dodge — it is the studio's actual position, and it is the same position `S08` and
`../WELLNESS-DESIGN-DIRECTION.md` already took when they ruled durations out of the whole sector.
`S15` is where a visitor finds out the omission was deliberate. **An FAQ that explains its own
silences is more trustworthy than one that fills them.**

**Every answer is grounded in a commitment established elsewhere in the catalog.**

| Question | Answered from |
| --- | --- |
| Do I need to know what I want? | `S06`, `S08` |
| How long will it take? | **The deliberate silence** — explained, not answered |
| What does it cost? | `S11` |
| Will I be sold anything? | `S07` |
| Can I ask for a particular person? | `S04` |
| What if I need to move it? | `S07` |
| Is it awkward to say stop? | `S08` |
| Can I look round first? | `S13` |

Nothing was invented for the FAQ. That also makes the section **self-checking**: an answer that
contradicted its source section would be a defect visible from inside the catalog, without
reference to anything outside it.

**Not present in any study:** an invented duration, price, figure, currency symbol, opening hour,
day name, availability, waiting time or response time; an efficacy, diagnostic or condition claim;
a fabricated policy no other section supports. A scan for **any digit in visible copy** returns
nothing across all five.

**Not a knowledge base.** No ticket numbers, article counts, category icons, search field or
"was this helpful?" control appears anywhere. `003` came closest, and is addressed in its record.

## The Axis This Batch Records

An FAQ's only real design decision is **what is visible before a click**. The five studies spread
across that axis deliberately, and `002` argues one end of it as a position rather than a style.

| Study | Disclosures | Visible on arrival |
| --- | --- | --- |
| `001` | 8 native `<details>` | One answer |
| `003` | 8 native `<details>`, grouped | Three answers, one per panel |
| `004` | none | All eight, one promoted |
| `002` | **none, deliberately** | All eight |
| `005` | none | Four, at display scale |

## Study Records

### WELL-S15-001 — Universal / Safe

- **Layout model:** A single column of eight native disclosures on hairlines, first open.
- **Interaction:** Native `<details>` / `<summary>` — focusable and state-announcing without any
  ARIA, and without a line of JavaScript.
- **Responsive strategy:** the header unstacks at 768px; the answer measure unlocks with it.
- **Visual-first check:** 256 visible words across eight answers.

### WELL-S15-002 — Premium / Editorial

- **Layout model:** Eight question-and-answer pairs set **open** in two reading columns, serif
  questions above sans answers, with no disclosure control anywhere.
- **The argument:** this is the only study in the batch a visitor can read without touching
  anything, and that is the point. A sector built on not hiding things — no selling in the room, no
  added charges at the desk, no hidden durations — has a weak case for folding eight short answers
  behind eight clicks. The visible copy says so.
- **Responsive strategy:** two columns become one at 768px; nothing collapses at any width.
- **Visual-first check:** 273 visible words, the highest in the batch, all of it visible at once.

### WELL-S15-003 — Structured / Visual Modular

- **Layout model:** The same eight questions sorted into three labelled panels — *before you book*,
  *on the day*, *money and changes* — each a set of native disclosures with its first question open.
- **How it avoids the knowledge-base register:** the groups are named for **when a question occurs
  to someone**, which is a visitor's sequence rather than an internal taxonomy, and the study
  carries no ticket numbers, article counts, category icons, search field or feedback control.
  Three collapsible panels is one step from a support desk; the naming is what keeps it a spa page.
- **Responsive strategy:** 3 → 2 panels with the third spanning full width, then one per row; every
  panel keeps its own first-open question so the pattern survives.
- **Visual-first check:** 265 visible words.

### WELL-S15-004 — Conversion-led

- **Layout model:** The blocking question promoted to a cream panel with the action beside it, over
  the remaining seven answers open in a compact two-column list.
- **Conversion device:** the question that actually stops a booking here is *how long will it take?*
  — and it is the one question the catalog may not answer with a number. Rather than burying it
  seventh in a list, this study promotes it and answers **the worry behind it**: that an unstated
  length means an open-ended bill or a rushed hour. Both are addressed with commitments that
  already exist — a shorter treatment costs less (`S11`), nothing is booked so tightly that a
  treatment is cut short (`S07`). **Turning the awkward question into the headline is the device.**
- **No collapsing:** the remaining seven are open, because a conversion study should not put a
  click between a visitor and the reassurance they came for.
- **Visual-first check:** 270 visible words.

### WELL-S15-005 — Art-directed / Distinctive

- **Layout model:** The hierarchy inverted. Four questions reduced to small uppercase labels, with
  the **answers** set at up to 2.6rem beneath them on alternating alignment.
- **The device, and why it matters:** every conventional FAQ makes the question loud and the answer
  quiet, which means the page is visually a list of things that might be wrong. Reversing it means
  a visitor scanning without reading sees **four reassurances rather than four anxieties**.
  Confirmed in render — the page reads as answers.
- **Why four and not eight:** at display scale eight answers would be a wall. The low count is what
  the device costs, and it is why the other four studies carry the full set.
- **Responsive strategy:** the inversion holds at every width; only the alternating alignment goes
  at 768px, because right-aligned display text at phone width is harder to read than it looks.
- **Visual-first check:** 95 visible words.

## Structural Diversity

| Study | Topology | Questions | Interaction | Ground |
| --- | --- | --- | --- | --- |
| 001 | Single column of disclosures | 8 | Native `<details>` | Pale warm grey |
| 002 | Two open reading columns | 8 | **None** | Warm bone |
| 003 | Three grouped disclosure panels | 8 | Native `<details>` | Pale blue-grey |
| 004 | Promoted question + open two-column list | 8 | None | Deep olive |
| 005 | Inverted hierarchy, alternating alignment | 4 | None | Clay |

Grounds do not repeat any used in `WELL-S01`–`S14`.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-01.
- **Visual-first check:** 95–273 visible words. The four full studies sit close together because
  they carry the same eight answers; what differs is disclosure, grouping and rank rather than
  copy. A Q&A section is text by nature — the comparison the sector must not repeat remains
  `ARC-S23` at 630 words in a section whose subject was not prose.
- **Document-metaphor justification:** `NONE`. No knowledge base, support desk, ticket system or
  help-centre article device is used — see the note in `003`'s record.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** `001` and `003` use native `<details>` / `<summary>`; the other
  three are fully static. No `<script>` element and no inline `style` attribute in any file.

## Media Slots

**None.** This batch carries no media at all, deliberately and consistently: an FAQ is a reading
interface, and a photograph beside a short answer is decoration. `S13` is where this sector's
imagery lives.

## QA

- ID validation: **PASS.** All five IDs exist and match their filenames.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport. Nesting validated with a stack-based parser; all five parse correctly.
- Accessibility QA: **PASS.** `lang`, scoped `:focus-visible`, `aria-labelledby`,
  `prefers-reduced-motion`, and 44px-plus targets throughout. The disclosures in `001` and `003`
  are native `summary` elements, which are focusable and announce their expanded state without any
  ARIA; both honour `prefers-reduced-motion` by dropping the chevron rotation.
- Responsive QA: **PASS.** Breakpoints authored per study and recorded above — including `005`'s
  decision to drop its alternating alignment but keep its inversion.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image, script or
  inline style.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status.
- Scoped-CSS check: **PASS.** Every declaration outside the host baseline is namespaced to the
  study's own `.well-s15-00N` root.
- **Unanswerable-question check: PASS.** This batch's defining check. Visible text only, comments
  stripped, scanned for **any digit**, every currency symbol, minutes and hours, clock times, day
  names, *open <n>*, *within <n>*, percentages, *was this helpful*, *ticket*, *article*, and for
  efficacy, guarantee and diagnostic vocabulary including named skin conditions. **Zero matches in
  all five.**
- Source-consistency check: **PASS.** Every answer traces to a commitment in `S04`, `S06`, `S07`,
  `S08`, `S11` or `S13`, or is the explained silence. No answer contradicts its source section.
- Render check: **PASS, no corrections.** All five rendered in headless Chrome at 1440px and
  inspected. `005`'s inversion reads as intended — the page scans as answers rather than questions.
  Eighth batch in nine to need no render correction.

## Notes

- This is the fifteenth authored batch in the `WELL` sector and the thirteenth authored entirely
  without references.
- **The explained silence is the reusable outcome.** Every sector has an FAQ, and every sector's
  FAQ will be asked something the catalog cannot invent — a price, a lead time, a success rate, an
  availability. Naming the question and explaining why it is not answered in writing is authorable,
  is more honest than omission, and turns a constraint into a statement of how the business works.
- `S15` is the first section that is **downstream of the whole catalog**: it has no content of its
  own and every answer is borrowed from a section that came before it. That makes it the natural
  place to notice inconsistency, and none was found.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a placeholder rather than an
  interpreter. Headless Chrome, which the generator uses for measurement, is present and working.
