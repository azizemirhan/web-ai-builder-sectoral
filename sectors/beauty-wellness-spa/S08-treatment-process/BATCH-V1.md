# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S08`
- Section Name: `Treatment Process`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S08-001` | Universal / Safe | AUTHORED | `raw/WELL-S08-001.html` |
| `WELL-S08-002` | Premium / Editorial | AUTHORED | `raw/WELL-S08-002.html` |
| `WELL-S08-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S08-003.html` |
| `WELL-S08-004` | Conversion-led | AUTHORED | `raw/WELL-S08-004.html` |
| `WELL-S08-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S08-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's role, its governing constraint and its boundary
with `S02`, `S06` and `S07` are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint

Two rules govern this role, one carried forward and one specific to it.

**1. Steps describe the action, never the effect.** The procedural rule from `S02` applies at full
force here, because a process section is exactly where efficacy language enters on its own:
*"Step 3: extraction — clears congestion and refines pores."* Every step in this batch says what is
done. No study contains an efficacy claim, outcome description, percentage, rating, review, client,
award, certification or invented statistic.

**2. No durations, and no schedule register.** A visit has no stated length, no per-step timing and
no session count anywhere in this batch. This rules out the device the role most obviously invites:

    Allowed: "Then you lie down and the work begins."
    Not allowed: "Step 3 · 20 min · Extraction · reduces congestion".

A step table with a timing column is a **treatment protocol**, which
`../WELLNESS-DESIGN-DIRECTION.md` lists among the sector's anti-patterns. A numbered sequence is
not a schedule — it is a sequence, which is what this role genuinely is — but the moment it gains
a time column, a dosage or a course length it has become clinical paperwork. That line is the main
thing this batch had to hold, and it is why none of the five uses a tabular step layout.

**Semantic note.** All five studies mark the sequence as an `<ol>`. The order is real content here,
not styling, so it belongs in the markup rather than only in the numerals.

## The Sequence

Five steps, used consistently across the batch so the five studies read as one section. They are
written to hold for any treatment in `S02`.

| Step | What happens |
| --- | --- |
| 1 · Arriving | You come in, leave your things, and sit down. Nothing starts until you are ready. |
| 2 · A short conversation | We ask what you want from the session and what your skin has been doing. No clipboard. |
| 3 · The treatment | You lie down and the work begins. Pressure, warmth and products are adjusted as we go. |
| 4 · Coming back up | Time to sit, have something to drink, and come round before you stand. |
| 5 · Afterwards | If something would suit you at home we say so now — after, not during. |

The sequence deliberately begins at **arrival**, not at booking. Starting at "send us a request"
would make this section a second, weaker `S06`.

Step 5 is the operational other half of the `S07` commitment *nothing sold in the room*. The two
sections agree without repeating each other's framing: `S07` states the commitment, `S08` places it
in time.

## Study Records

### WELL-S08-001 — Universal / Safe

- **Structural intent / archetype:** The dependable version. One vertical spine, five steps, no
  device beyond the rail.
- **Layout model:** A continuous hairline down the left with a node per step, the steps stacked
  beside it and separated by full-width hairlines. The rail carries the sequence; the full-width
  rules keep the left-weighted text from looking truncated at wide viewports.
- **Media relationship:** None, deliberately — a photograph per step would be five pictures of the
  same room. Recorded rather than left as an omission; see *Media Slots*.
- **Responsive strategy:** The rail and its nodes narrow together at 480px rather than being
  dropped, so the sequence device survives at phone width.
- **Visual-first check:** 146 visible words.

### WELL-S08-002 — Premium / Editorial

- **Structural intent / archetype:** The visit as a descent down the page rather than a list on it.
- **Layout model:** Five full-width bands stacked down the section, alternating between two close
  ground tones. Step numbers stay small; the step names are serif at display scale. **The third
  band — the treatment — is the one that opens into two columns and carries the media**, so the
  centre of the visit is also the centre of the composition and is physically taller than the rest.
- **The device that earns the direction:** the tonal alternation makes the sequence readable
  without a rail, a numeral column or a card. It is the quietest way to say "these are in order".
- **Media relationship:** One tall reserved area, inside the third band only. Giving every step an
  image would flatten the sequence into five equal cards and lose the centre.
- **Responsive strategy:** The wide band collapses to one column at 768px with the media becoming
  16:10; the alternation is kept at every width because it is the sequence device.
- **Visual-first check:** 128 visible words.

### WELL-S08-003 — Structured / Visual Modular

- **Structural intent / archetype:** The sequence plus the thing a visitor actually wants to know —
  where they get a say.
- **Layout model:** A horizontal spine: one rail across the section with a node above each of five
  cards. Each card is two-tier — what happens, and beneath a rule, **Your say** at that point.
- **Content-capacity justification:** The capacity is the second tier, not longer sentences. The
  first tier here is *shorter* than in `001`; the study holds more because it adds an axis, which
  is the 003 test.
- **Why the second tier is the right content:** it is operational — what the visitor can ask for or
  change — never a claim about a result, and it reinforces the sector's no-pressure position
  without repeating `S07`'s framing.
- **Responsive strategy, recorded:** a horizontal spine cannot survive phone width. Rather than
  dropping the device, **the rail turns vertical below 1024px and the nodes stack along it**, so
  the sequence relationship is preserved in the axis that fits.
- **Visual-first check:** 150 visible words, which includes five second-tier lines.

### WELL-S08-004 — Conversion-led

- **Structural intent / archetype:** The rail does not stop at the last step.
- **Layout model:** A vertical sequence on a deep burgundy ground where the rail continues past
  step five into an **inverted action node** — a cream panel with its own dot on the rail, carrying
  the booking action. The steps are capped at a 52ch measure; the action panel spans much wider, so
  the terminus reads as the widest thing in the composition.
- **Conversion device:** **completion, not pressure.** Showing the whole visit and then leaving one
  obvious move is the argument. There is no urgency device — no limited availability, no countdown
  — which would be an invented diary state as well as the wrong register for this sector.
- **Semantics, held deliberately:** the five steps are the `<ol>`; the action node sits **outside**
  the list and is only visually attached to the rail. Booking is not a step of the visit — it
  happens before one — so the composition may treat it as the continuation but the markup may not
  claim it is part of the sequence.
- **Media relationship:** None. A media panel would break the run of the rail, which is the study's
  whole device.
- **Responsive strategy:** The action panel stacks its copy above a full-width button at 768px; the
  rail and both node types re-anchor together at 480px.
- **Visual-first check:** 150 visible words.

### WELL-S08-005 — Art-directed / Distinctive

- **Structural intent / archetype:** The whole visit happens in one room, so it happens in one
  image.
- **Layout model:** A full-bleed reserved media field holds the entire sequence. The five steps sit
  on it as translucent panels, each offset 7% further right than the last, so the visit reads as a
  single descent across one field rather than as five items on a page.
- **Empty-state device:** the panels are translucent, so they composite to a legible dark tone
  whether the field carries a photograph or the reserved tone. The field is set lighter than the
  section ground, so the band itself is visible as a distinct region while empty — checked in
  render, which is the state a reviewer sees.
- **Separation from `WELL-S03-005`:** that study staggers **separated** columns vertically with
  gaps between them. This staggers panels horizontally across a **shared field they all sit on**,
  which is why the field is the subject here and the panels are not.
- **Responsive strategy:** The offsets step down 7% → 5% → 3% and reach zero at 480px, but the
  panels-on-one-field relationship is kept at every width. The offsets are the rhythm; the shared
  field is the idea, and only the rhythm is negotiable.
- **Visual-first check:** 119 visible words.

## Structural Diversity

| Study | Sequence device | Media | Terminus | Ground |
| --- | --- | --- | --- | --- |
| 001 | Vertical rail with nodes | None | Last step | Pale warm grey |
| 002 | Alternating full-width band tones | One, in band three | Last band | Two-tone sand |
| 003 | Horizontal rail, vertical below 1024px | None | Last card | Light grey-green |
| 004 | Vertical rail running into an action node | None | Inverted action panel | Deep burgundy |
| 005 | Horizontal offsets across one shared field | One, full-bleed under everything | Last panel | Dark neutral |

No study repeats another's sequence device, and none uses a tabular or timed layout. Grounds do not
repeat any used in `WELL-S01`–`S07`.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-01.
- **Structural direction rationale:** recorded per study above.
- **Differentiation notes:** recorded in *Structural Diversity* above.
- **Visual-first check:** 119–150 visible words. The band is narrow because every study carries the
  same five steps at one line each; what differs is the device, not the copy. `003` sits at the top
  of the band because it adds a second tier, and `002` at the bottom because its serif display
  scale does more of the work.
- **Document-metaphor justification:** `NONE`. No protocol table, treatment schedule, course plan
  or clinical record device is used, and no study carries a timing column — see *The Governing
  Constraint*.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** All five studies are fully static; the rails, nodes and offsets
  are CSS pseudo-elements and margins. No `<script>` element appears in any file in this batch.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Treatment in progress | `002` — inside the third band, beside the step that is the centre of the visit | Still image, 4:3 stepping to 16:10 | Empty tonal surface with a quiet label; the band's copy stands alone and the band stays the tallest either way |
| Treatment room | `005` — a full-bleed field carrying the entire sequence on top of it | Still image, full-bleed behind five translucent panels | Reserved tone set lighter than the section ground so the field reads as a distinct region while empty; panel contrast was checked against that empty tone |

**Why three of five studies carry no media, recorded rather than left as an omission.** The subject
of this role is a sequence, and the honest image for "a short conversation" is the same room as the
image for "arriving". One photograph per step would be five near-identical pictures filling space
the media policy reserves for something the role needs. `002` and `005` carry media because theirs
is structural — a single image marking the centre of the visit, and a single field the whole
sequence sits on.

## QA

- ID validation: **PASS.** All five planned IDs exist; every `study-id` meta matches its filename.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport in every study. Nesting validated with a stack-based parser over comment-stripped
  markup; all five parse correctly. Every study marks its sequence as an `<ol>`, verified by scan.
- Accessibility QA: **PASS.** Every study sets `lang`, scopes a `:focus-visible` ring, labels its
  section with `aria-labelledby`, honours `prefers-reduced-motion`, and gives every interactive
  element a 44px-or-greater target. The rails, nodes and dots are CSS pseudo-elements carrying no
  content, so nothing decorative reaches the accessibility tree.
- Responsive QA: **PASS.** Four authored breakpoints per study, recorded per study above —
  including `003`'s horizontal-to-vertical rail transformation and `005`'s decision about which
  half of its device is negotiable.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image or script.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status.
- Scoped-CSS check: **PASS.** Every declaration outside the `html` / `body` host baseline is
  namespaced to that study's own `.well-s08-00N` root, verified by scan.
- **Duration and protocol check: PASS.** This batch's defining check. Visible text only, comments
  stripped, scanned for minutes, hours, session counts, week counts and the word *duration*, and
  for outcome vocabulary, superlatives, awards, certifications, percentages, currency, ratings,
  reviews and urgency words. Clean in all five, and no study uses a tabular step layout.
- Render check: **PASS, no corrections.** All five rendered in headless Chrome at 1440px and
  inspected, with `004` re-rendered at 1750px tall to confirm the action node below the fold. The
  vertical rails and their nodes align in `001` and `004`; `003`'s horizontal rail aligns to the
  card left edges; `004`'s rail runs correctly into the inverted action node and stops at it;
  `005`'s descent reads across the field. This is the second consecutive batch to need no render
  correction.

## Notes

- This is the eighth authored batch in the `WELL` sector and the sixth authored entirely without
  references.
- The no-timing rule is the reusable outcome here. Every sector has a process section, and in
  healthcare, dental and medical-aesthetic sectors the pull toward a timed protocol table is
  stronger than it is here. The distinction to carry forward: **a sequence is content, a schedule
  is a claim.**
- `S08` now closes the group that `S06` and `S07` opened: `S06` is the request, `S07` is what holds
  on every visit, `S08` is the order it happens in. The three read together without overlapping.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a placeholder rather than an
  interpreter. Headless Chrome, which the generator uses for measurement, is present and working.
