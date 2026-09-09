# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S19`
- Section Name: `Contact`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S19-001` | Universal / Safe | AUTHORED | `raw/WELL-S19-001.html` |
| `WELL-S19-002` | Premium / Editorial | AUTHORED | `raw/WELL-S19-002.html` |
| `WELL-S19-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S19-003.html` |
| `WELL-S19-004` | Conversion-led | AUTHORED | `raw/WELL-S19-004.html` |
| `WELL-S19-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S19-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's role, its governing constraint and its boundary
with `S06`, `S16` and `S20` are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint — The Section Cannot Be Made Of Its Own Details

Almost everything a contact section normally shows is data a placeholder cannot know. The `S11`
field-versus-figure test decides each one:

| Element | Treatment |
| --- | --- |
| Phone number | **Reserved field** — every studio has one |
| Email address | **Reserved field** |
| Postal address | **Reserved field**, and only where the study needs it |
| Opening hours | **Omitted** — an empty hours table asserts a weekly schedule and prints figures |
| Response time | **Omitted** — *"we reply within —"* is an invented figure and a service promise |
| A map | **Omitted** — `S16` owns the reserved map area; repeating it here blurs the boundary |
| Social handles | **Omitted** — an invented account name is an invented identity |
| Live chat | **Omitted** — mocking a chat widget invents a staffed channel |

**So the batch is built out of operating policy instead**, which is the pattern `S07`, `S12`, `S14`
and `S17` each arrived at from a different direction:

1. **What each channel is actually for** — and, in `003`, what it is bad at.
2. **A message is not a booking.** Nothing is held until somebody replies.
3. **Who answers** — whoever would be doing the treatment, not a shared inbox.
4. **What will not be answered in writing** — one line only; the long version is `S15` and `S18`.

**Not present in any study:** an invented telephone number, email address, street address,
postcode, set of opening hours, response time, staff name, social handle or account; a map, embed,
live chat widget or availability indicator; a response-rate or satisfaction figure; an urgency
device; a newsletter capture. Verified by scan — **no digit appears in visible copy anywhere in the
batch**, and neither does an `@`, a weekday, an *am*/*pm*, or the words *map*, *directions*,
*within*, *live chat*, *follow us*.

## The Line That Matters

> A message is not a booking. Nothing is held until somebody has replied and you have said yes.

It appears in all five studies, phrased for each one — a heading in `001`, a closing note in `002`,
a *not for* line in `003`, the whole aside in `004`, and a clause under the email field in `005`.
It costs the studio nothing, it prevents the commonest misunderstanding in the sector, and a
placeholder can state it honestly. Same shape as `S17`'s *the amount is not printed on the card*:
**the strongest content in a transactional section is the awkward bit nobody prints.**

## Study Records

### WELL-S19-001 — Universal / Safe

- **Layout model:** Three channel cards — ring us, write to us, come in — each with its reserved
  field and one line on what that channel is good for, above two closing commitments.
- **Why three cards and not a details block:** a list of details answers *what are they*; a card per
  channel answers *which one do I use*, which is the only question this section is asked.
- **Responsive strategy:** 3 → 2 cards with the third spanning full width, then one per row; the
  commitments go 2 → 1.

### WELL-S19-002 — Premium / Editorial

- **Layout model:** A short serif proposition holding the left half, the reserved details set on the
  right as a colophon — small caps labels, hairline rules, nothing else.
- **The editorial reading:** the details are treated as **the endmatter of a printed programme**,
  which is also the honest hierarchy — the sentence is real and the details are not written yet.
  Lowest word count in the batch.
- **No address here, deliberately:** an editorial colophon listing one street would read as a
  headquarters, and the set of locations belongs to `S16`.
- **Responsive strategy:** the split unstacks at 860px.

### WELL-S19-003 — Structured / Visual Modular

- **Layout model:** Three channel modules above a full-width module on a dark ground setting out
  what happens after you get in touch.
- **The device — every module carries a "not for" line.** Listing channels tells a visitor nothing
  they could not guess; saying what each channel is *bad* at is the part that actually routes them,
  and it is authorable because it describes the studio's working habits rather than a promise. The
  email module's *not for* is where this batch's central line lands most naturally: **holding a
  time.**
- **Named, not numbered:** the three stages are *first*, *then*, *after that*. A numbered sequence
  in this sector starts to read as a protocol, which the sector direction rules out.
- **Responsive strategy:** 3 → 2 → 1 modules; the closing module goes 4 → 2 → 1 columns.

### WELL-S19-004 — Conversion-led

- **Layout model:** A three-field message form holding the left of the composition, with an aside
  saying what the form does not do and offering the telephone instead.
- **It is a message form, not a booking form.** Who you are, how to reach you, what you want to ask.
  **No treatment picker, no date, no time** — the moment it acquires those it has become `S06` in
  the wrong place, and it would be promising to hold something it cannot hold. Verified by scan: no
  `<select>` and no date or time input in any study.
- **Conversion device:** the honest limit again. A conversion-led contact section normally implies
  that sending the form starts something; this one says it **holds nothing**, then sends anyone who
  wants a time to the telephone. **Routing people away from the form is the conversion decision**,
  because the wrong channel produces a worse outcome for both sides.
- **No placeholder text in any field.** A placeholder that reads like real data is invented data,
  and it also disappears the moment someone types. Labels and hints carry it instead.
- **Correction made, recorded:** the reserved telephone field was first filled with the same tone as
  the form inputs beside it and read as a fourth, empty input. Its fill was removed so the dashed
  edge alone marks it as a reserved value rather than something to type into.

### WELL-S19-005 — Art-directed / Distinctive

- **Layout model:** One oversized line on a saturated clay ground, under it a single reserved plate
  given the full width and the height of an object, with the two quieter ways in held small beneath.
- **The device — the reserved field is promoted to the subject.** Everywhere else in this sector a
  reserved slot has been a quiet stand-in. Here the study argues that the fastest route to an answer
  is a person on the telephone, and makes that argument by giving the number the page. It still
  works while empty: a labelled plate at that scale reads as *the number goes here and it is the
  point*, which is what the finished section will say.
- **Deliberately not a plaque:** no engraved sign, no door plate, no certificate frame — that would
  drift into the certification register the sector direction rules out. It is a plain field at
  object scale.
- **Correction made, recorded:** the plate first sat at 1.26:1 against its ground and depended
  entirely on its dashed edge to read. Deepened to `#6b2f1f` for 1.50:1, on the same reasoning as
  the `S10-005` watermark fix.

## Structural Diversity

| Study | Topology | Reserved fields | Interaction | Ground |
| --- | --- | --- | --- | --- |
| 001 | Three channel cards + two commitments | 3 | None | Pale sage `#eef0ea` |
| 002 | Proposition beside a colophon | 2 | None | Warm parchment `#f3efe6` |
| 003 | Three channel modules + an after module | 3 | None | Pale slate `#e8eaee` |
| 004 | Message form beside a limits aside | 1 | Native form controls | Deep petrol `#1c2f3a` |
| 005 | One oversized line + one plate at object scale | 3 | None | Saturated clay `#8f4530` |

Grounds do not repeat any used in `WELL-S01`–`S18`; verified by scan across all 95 studies.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-02.
- **Visual-first check:** no study derives its distinctiveness from copy. The differentiator is what
  carries a contact section once the map and the photograph of the building are gone — a card per
  channel, a single sentence, a routing argument, a form, or the number itself at object scale.
- **Document-metaphor justification:** `NONE`. No card, coupon, certificate, plaque or letterhead
  device is used.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** `004` uses native form controls only — no validation script, no
  success state, no submit handler. No `<script>`, no `<iframe>`, no inline `style` attribute in any
  file.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Telephone ×5 | One per study | **Text**, replaced by the real number | Em dash with a visually hidden "Telephone number" label; in `005` a labelled plate at object scale |
| Email ×4 | `001`–`003`, `005` | **Text** | Em dash with a visually hidden "Email address" label |
| Address ×3 | `001`, `003`, `005` | **Text** | Em dash with a visually hidden "Street address" label |
| Message form | `004` — three native fields | **User input**, submitted to the studio | Labelled fields, no placeholder text, 48px targets |

Verified by scan: 11 reserved slots plus `005`'s plate; all 11 slots carry a visually hidden field
label, and every form field has a matching `<label for>`.

## QA

- ID validation: **PASS.** All five IDs exist and match their filenames.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport. Nesting validated with a stack-based parser; all five parse correctly.
- Accessibility QA: **PASS.** `lang`, scoped `:focus-visible`, `aria-labelledby`,
  `prefers-reduced-motion`, 44px-plus targets, every reserved slot labelled. `004`'s three fields
  each have a real `<label for>` and a hint that is part of the label, not a placeholder.
- Responsive QA: **PASS.** Breakpoints authored per study and recorded above; verified at 1440px and
  720px with no horizontal overflow in any study.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image, script, iframe
  or inline style.
- CSS-validity scan: **PASS.** No malformed hex, no accidental 8-digit hex, no `clamp()` with the
  wrong arity.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status.
- Scoped-CSS check: **PASS.** Every declaration outside the host baseline is namespaced to the
  study's own `.well-s19-00N` root.
- **Contact-data check: PASS — this batch's defining check.** Visible text only, comments and hidden
  field labels stripped, scanned for **any digit**, `@`, `www.`, `.com`, every weekday, *am*, *pm*,
  *opening hours*, *reply within*, *response time*, *within a*, *same day*, *round the clock*,
  *live chat*, *whatsapp*, *instagram*, *facebook*, *follow us*, *map*, *directions*, *subscribe*,
  *guaranteed*, *certified*, *accredited*, percentages. **Zero matches in all five.**
- **Booking-form check: PASS.** No `<select>`, no date, time, datetime, month or week input, and no
  `placeholder` attribute in any study.
- **Message-is-not-a-booking check: PASS.** All five studies state it.
- Render check: **PASS, after two corrections.** All five rendered in headless Chrome at 1440px and
  inspected: `004`'s reserved field was un-filled so it stops reading as an input, and `005`'s plate
  was deepened for contrast. Both recorded above.

## Notes

- This is the nineteenth authored batch in the `WELL` sector and the seventeenth authored entirely
  without references.
- **The reusable outcome is that a contact section is a routing problem, not a details block.** Every
  detail in it is reserved, so what is left to design is the decision a visitor is actually making:
  which way in suits the question they have, and what happens once they use it. `003`'s *not for*
  line and `004`'s decision to send people away from its own form are the two clearest expressions
  of that, and both are transferable to any sector whose contact details cannot be invented.
- `S19` closes the group that begins at `S06`: `S06` books a time, `S16` says where the building is,
  `S19` is for everyone who is not ready to do either yet, and `S20` will make the closing ask.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a Windows Store placeholder
  rather than an interpreter. Headless Chrome, which the generator uses for measurement, is present
  and working, so a Node port of `review/build-index.py` would restore it.
