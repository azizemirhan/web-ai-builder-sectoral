# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S06`
- Section Name: `Consultation Booking`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S06-001` | Universal / Safe | AUTHORED | `raw/WELL-S06-001.html` |
| `WELL-S06-002` | Premium / Editorial | AUTHORED | `raw/WELL-S06-002.html` |
| `WELL-S06-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S06-003.html` |
| `WELL-S06-004` | Conversion-led | AUTHORED | `raw/WELL-S06-004.html` |
| `WELL-S06-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S06-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's role, its boundary with `S19` and `S20`, and its
governing constraint are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Direction Problem, And How This Batch Solves It

Every study in this section carries a booking route, so `004` cannot be distinguished by having
one — which is the opposite of the situation in every other section so far, where the trap was a
section *becoming* a booking widget.

The distinguishing axis chosen for this batch is **friction: how much is asked, and how**.

| Study | What it asks for | Why |
| --- | --- | --- |
| `001` | Six fields — treatment, time of day, day, name, contact, notes | The full request a studio would normally need up front |
| `002` | Three fields, and **no date at all** | The editorial reading is an invitation to talk; timing is settled in the conversation |
| `003` | Five fields, shown as three visible stages | The structure of the request is the content |
| `004` | **One field** | Minimum friction; everything else deferred to the call |
| `005` | Four controls, written as one sentence | The form is the typography |

That axis also produced five different compositions rather than five skins on a form.

## The Governing Constraint

The claims rule in `../WELLNESS-DESIGN-DIRECTION.md` applies, with three additions specific to a
booking role. **Not present in any study in this batch:**

- **Invented availability.** No named slot, no "next available", no waiting time, no opening hours,
  no diary state. A placeholder cannot know a real studio's calendar. Where timing is needed the
  studies offer **preference bands** — morning, afternoon, evening, no preference — which are the
  visitor's input rather than the studio's claim, and a native `type="date"` field, which the
  visitor fills.
- **Invented prices or durations.** No treatment length, no consultation fee, no deposit.
- **A promise about the outcome of booking.** No response-time guarantee, no "confirmed instantly".
  This was the live risk in `004`, where *"we will call you within an hour"* is the natural
  conversion line and exactly the promise a placeholder may not make. Its copy says what will be
  asked, not when it will happen.

**The forms are structure, not collection.** Every form is native controls with real labels and
**no `action`, no endpoint and no script**. Nothing is sent anywhere and nothing is stored. This
was verified by scan across all five files.

Three studies close with the same factual reassurance — *nothing is booked and nothing is charged
by sending this* — which is true of the structure itself rather than a claim about the business.

## Study Records

### WELL-S06-001 — Universal / Safe

- **Structural intent / archetype:** The dependable booking section. Everything a studio would
  normally ask, in one card, with the reassurance beside it rather than under it.
- **Layout model:** An asymmetric 0.86fr / 1.14fr split. Left: header, one lead, and a
  hairline-separated "what happens next" list. Right: a white card holding a two-column field grid
  — treatment and time of day paired, day and name paired, contact and notes full width — closed
  by a filled action and a secondary text route.
- **Media relationship:** **None, deliberately.** The subject of this section is an interface, and
  a decorative image beside a form adds nothing the role needs. Media-carrying compositions in this
  batch are `002` and `005`; this is recorded rather than left as an omission.
- **Responsive strategy:** The split becomes one column at 1024px, and the field grid becomes one
  column at 480px so no field is ever half-width on a phone.
- **Visual-first check:** 105 visible words, the highest in the batch — six field labels, three
  "what happens next" items and a hint. Copy in a form role is interface text, not prose.

### WELL-S06-002 — Premium / Editorial

- **Structural intent / archetype:** Booking as an invitation rather than a task.
- **Layout model:** A wide serif invitation across the top, then a lower half splitting a tall
  reserved media panel against a three-field request. The fields are set as quiet underlined lines
  with serif labels, not as a boxed card — the form is inside the composition rather than inside a
  container.
- **The deliberate omission:** this study asks for **no date**. A consultation in this register is
  a conversation, and pinning a day on the page contradicts that. It is the only study in the batch
  that does not ask when.
- **Media relationship:** One tall reserved panel, present here and absent from `001` because the
  editorial register needs the room to feel like a place.
- **Responsive strategy:** The lower half goes to one column at 768px with the panel becoming
  16:10, then 4:3 at 480px.
- **Visual-first check:** 71 visible words.

### WELL-S06-003 — Structured / Visual Modular

- **Structural intent / archetype:** The shape of the request made visible. Three stages, so the
  visitor can see how short it is before starting.
- **Layout model:** Three numbered stage modules in a row — *what you want*, *when suits you*, *how
  to reach you* — inside **one** form, closed by a full-width bar carrying the reassurance and a
  single action.
- **Content-capacity justification:** The capacity is the staging, not the copy. Five fields are
  grouped into three legible steps rather than listed as five; the study holds more perceived
  structure at the same field count.
- **Interaction:** Native controls only, **no JavaScript**. The three modules are stages of a
  single form, not three forms — everything submits together, so nothing depends on a script to
  carry state between steps. That is a deliberate choice: a scripted multi-step wizard would be the
  obvious answer and would fail the dependency rule.
- **Numbering note:** the 01 / 02 / 03 marks are stage indicators for a sequence the visitor moves
  through. They are not the editorial sequence device used in `WELL-S02-002`, and not a register,
  schedule or document numbering scheme.
- **Media relationship:** None, deliberately, as in `001`.
- **Responsive strategy:** 3 → 2 columns at 1024px with the third stage spanning full width, then
  one column at 480px; the closing bar stacks its text above a full-width action at 768px.
- **Visual-first check:** 97 visible words.

### WELL-S06-004 — Conversion-led

- **Structural intent / archetype:** The shortest possible path. One field, one action, and an
  honest statement of what is being deferred.
- **Layout model:** A single centred column on a saturated terracotta ground. A large invitation, a
  one-line lead, one labelled field paired with the action in a single row, then two short closing
  lines — one saying the rest is handled on the call, one offering the longer form instead.
- **Conversion behaviour:** the escape hatch points *back* to the fuller request rather than away
  from the section, so a visitor who wants to write everything out is not stranded by the short
  path.
- **Risk handled:** see *The Governing Constraint* — no response-time promise.
- **Media relationship:** None, deliberately: any media here would sit between the visitor and the
  one field.
- **Responsive strategy:** The field row stacks to full-width input above full-width action at
  480px.
- **Visual-first check:** 58 visible words, the lowest in the batch, which is the point.

### WELL-S06-005 — Art-directed / Distinctive

- **Structural intent / archetype:** The form as typography. The request is one display-scale
  sentence and the controls sit inside it, so the fields *are* the composition.
- **Layout model:** A deep charcoal-violet ground, a small eyebrow, then a sentence at up to
  3.1rem: *"I would like [treatment], ideally [time]. My name is [name] and you can reach me on
  [contact]."* Every control is underlined and set in warm gold against the cream sentence, so the
  interactive parts read out of the type.
- **Accessibility, and why this pattern is acceptable here:** every control has a real `<label>`
  bound by `for`, held visually hidden because the sentence supplies the visible context; the
  reading order of the sentence and the tab order of the controls are the same. This is the
  art-directed answer **only** — `001` and `003` carry conventional labelled-field forms, so the
  section covers both, and a reviewer choosing between them is not forced to take the inline
  pattern to get this role.
- **Media relationship:** None, deliberately: the type is the image, and a panel beside it would
  compete with the one device the study has.
- **Responsive strategy:** The sentence stays a sentence and only reduces — three type steps, with
  the inline field widths narrowing in `ch` at each so the line breaks stay reasonable.
- **Visual-first check:** 81 visible words, of which the sentence itself is roughly 30.

## Structural Diversity

| Study | Topology | Fields | Form presentation | Media |
| --- | --- | --- | --- | --- |
| 001 | Intro column beside a form card | 6 | Boxed card, two-column grid | None |
| 002 | Wide invitation over media + request | 3 | Underlined lines, serif labels | One tall panel |
| 003 | Three numbered stage modules | 5 | Three cards, one form | None |
| 004 | Centred single column, saturated ground | 1 | One pill field beside the action | None |
| 005 | Display-scale sentence | 4 | Inline within the type | None |

Grounds: pale lavender-grey, dusty rose-brown, mid blue-grey, saturated terracotta, deep
charcoal-violet. None repeats a ground used in `WELL-S01`–`S05`.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-01.
- **Structural direction rationale:** recorded per study above.
- **Differentiation notes:** recorded in *The Direction Problem* and *Structural Diversity*.
- **Visual-first check:** 58–105 visible words. The counts sit higher than `S05` because a form
  role's copy is interface text — field labels, hints and the closing reassurance — rather than
  prose. No study derives its distinctiveness from copy volume.
- **Document-metaphor justification:** `NONE`. No intake form, consent form, medical questionnaire
  or clinical record device is used. `003`'s stage numbering is addressed in its study record.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** All five studies are fully static native forms. No `<script>`
  element appears in any file in this batch, and no form carries an `action`.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Consultation room | `002` — the one media area in the batch, held tall beside the request | Still image, 4:5 stepping to 4:3 | Empty tonal surface with a quiet label; the invitation and the three fields carry the study without it |

**Why four of five studies carry no media, recorded rather than left as an omission.** This is the
one section in the sector whose subject is an interface. `../WELLNESS-DESIGN-DIRECTION.md` warns
that a visually oriented section must not quietly become text-only — but a booking form is not a
visually oriented section, and a decorative image placed beside a field set would be filler rather
than reserved space for something the role needs. `002` carries media because its editorial reading
genuinely needs the room to feel like a place. The other four would not be improved by it.

## QA

- ID validation: **PASS.** All five planned IDs exist; every `study-id` meta matches its filename.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport in every study. Nesting validated with a stack-based parser over comment-stripped
  markup; all five parse correctly.
- Accessibility QA: **PASS.** Every study sets `lang`, scopes a `:focus-visible` ring, labels its
  section with `aria-labelledby`, honours `prefers-reduced-motion`, and gives every interactive
  element a 44px-or-greater target. **Every form control in the batch has a real `<label>` bound by
  `for`** — verified by scan, which cross-checked every `input`, `select` and `textarea` id against
  every `label for`. Zero unlabelled controls across all five studies. `005`'s labels are visually
  hidden because the sentence supplies visible context; every other study labels visibly.
- Responsive QA: **PASS.** Four authored breakpoints per study, recorded per study above.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image or script.
- **Form-collection check: PASS.** No `<form>` in this batch carries an `action`, and no file
  contains a `<script>`. Nothing is submitted, sent or stored anywhere.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status.
- Scoped-CSS check: **PASS.** Every declaration outside the `html` / `body` host baseline is
  namespaced to that study's own `.well-s06-00N` root, verified by scan.
- Availability and claims check: **PASS.** Visible text only, comments stripped, scanned for
  response-time phrasing (*within N*, *instantly*, *immediately*), clock times, durations in
  minutes or hours, *next available*, opening hours, currency, *deposit*, *fee*, *guarantee* and
  percentages. Clean in all five.
- Render check: **PASS, after two corrections.** All five rendered in headless Chrome at 1440px and
  inspected. `003`'s three-stage form and `005`'s inline sentence both render and read as intended.
  Two defects were found and fixed:
  - `005`'s treatment `<select>` sized itself to its longest option, *"to talk it through first"*,
    leaving a long empty underline between the chosen value and the native arrow. Native selects
    cannot be sized to the selected option without script, so the longest option was shortened to
    *"to talk first"*, which tightens the control without adding a dependency.
  - `004` carried a dropped word — *"Would rather write it out?"* — corrected to *"Would you rather
    write it out?"*.

## Notes

- This is the sixth authored batch in the `WELL` sector and the fourth authored entirely without
  references.
- The `S06` / `S19` / `S20` boundary written into `./README.md` matters more than most, because all
  three sections read as "get in touch" and would otherwise converge: `S06` is the interaction,
  `S19` is the contact facts, `S20` is the closing invitation.
- The friction axis used to separate the five directions here is reusable for any sector whose
  section role is already a conversion moment.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a placeholder rather than an
  interpreter. Headless Chrome, which the generator uses for measurement, is present and working.
