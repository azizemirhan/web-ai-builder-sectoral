# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S04`
- Section Name: `Specialists`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S04-001` | Universal / Safe | AUTHORED | `raw/WELL-S04-001.html` |
| `WELL-S04-002` | Premium / Editorial | AUTHORED | `raw/WELL-S04-002.html` |
| `WELL-S04-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S04-003.html` |
| `WELL-S04-004` | Conversion-led | AUTHORED | `raw/WELL-S04-004.html` |
| `WELL-S04-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S04-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's own role, its identity rule and its boundary with
`S26` are in `./README.md`.

## Authoring Direction

No reference images were supplied for this section. All five studies were originated.

## The Identity Problem

This is the first `WELL` section whose content is people, and it is the section where the
sector's claims rule bites hardest. `../WELLNESS-DESIGN-DIRECTION.md` forbids an invented
practitioner name, qualification, licence, registration or professional body, and
`03-MEDIA-POLICY.md` forbids inventing people at all. A specialists section populated with
realistic names and credentials would be fabrication, not placeholder content.

**The approach used across the batch — and why it also produced better compositions:**

- **Role leads, identity is reserved.** The occupational role — *Facialist*, *Massage therapist*,
  *Nail technician*, *Brow & lash specialist* — is a real, generic, non-fabricated fact about a
  post, so it carries the card as the heading. The name sits beneath as the token
  `Practitioner NN`, following the `Team member NN` convention established in `ARC-S08`.
  Composing role-first rather than name-first is what stops the placeholder reading as a broken
  card: the largest text on every card is real information.
- **Focus lines are procedural**, in line with the `S02` copy rule: what the person spends their
  time doing, never how good they are at it.
- **No credentials in any form.** No qualification, licence, registration, membership, award,
  years of experience, rating, review or social handle appears in any study — including as an
  empty labelled field, which would still assert that the studio holds one.
- **No availability or waiting times**, which would be invented facts about a real diary. This
  came up specifically in `004`, where a booking-led composition invites them.
- **Portraits are reserved media areas.** A filled portrait slot means a photograph of a real
  person who has consented to appear.

**One deliberate divergence from `ARC-S08`.** That section put a visible statement in each study
saying its roster was a placeholder. The *Visible Website Copy vs Research Notes* rule was added to
`01-AUTHORING-STANDARD.md` **after** `ARC-S08` was authored, and it places that kind of explanation
in HTML comments, `<meta>` fields and the batch record instead. No study in this batch displays a
note about its own placeholder status. The naming convention was kept; the visible disclosure was
relocated here.

**Boundary check.** Every study is a set of practitioners seen at a glance. None gives a single
person a biography, a body of work or a page-scale treatment, which is `S26`'s role — and `S26`'s
own README already states that a team index belongs to the sector core sections.

## Study Records

### WELL-S04-001 — Universal / Safe

- **Structural intent / archetype:** The dependable team grid any studio could ship.
- **Layout model:** A split header closed by a hairline, above a four-column grid of cards. Each
  card is a 4:5 reserved portrait with a caption band beneath carrying the role, the reserved name
  token, one procedural focus line, and a profile link pinned to the card foot.
- **Media relationship:** Four reserved portraits at equal, generous scale.
- **Responsive strategy:** 4 → 2 → 1 columns. The portrait steps 4:5 → 3:2 at 1024px, back to 4:5
  at 768px and to 3:2 at 480px — deliberately non-monotonic, because a two-up card is wide and a
  one-up card is wide again, while the 768px column is narrow enough to carry a portrait shape.
- **Visual-first check:** 88 visible words.

### WELL-S04-002 — Premium / Editorial

- **Structural intent / archetype:** Editorial hierarchy. One practitioner is given the space of a
  feature, the rest run as a strip beneath.
- **Layout model:** A serif header, then a two-column feature — a large 4:5 portrait beside a text
  column with the role at display scale, the name token, a longer procedural focus line and a
  profile link. A hairline opens a pull-quote-scale studio statement, and a three-up strip of 1:1
  portraits closes the section.
- **Claims note:** The pull-quote-scale line is a **studio statement, not a personal quotation**,
  and is deliberately unattributed. A quote attributed to a placeholder person would be a
  fabricated testimonial. Featuring one practitioner is a compositional device, not a seniority
  claim, and no title implying rank is used.
- **Media relationship:** One large portrait plus three small ones — the widest scale spread in the
  batch.
- **Responsive strategy:** The feature collapses to a single column at 768px with the portrait
  becoming 3:2; at 480px the three-up strip becomes a scroll-snapped rail rather than a stack, so
  the "featured plus the rest" relationship survives instead of flattening into four equal blocks.
- **Visual-first check:** 69 visible words, the lowest in the batch.

### WELL-S04-003 — Structured / Visual Modular

- **Structural intent / archetype:** The roster that answers "and what do they actually do?"
  without printing it all at once.
- **Layout model:** An asymmetric 0.4fr / 1.6fr split — a standing intro column beside a stack of
  four horizontal person rows. Each row is a three-column grid: a small square portrait, a body
  carrying role, name token, focus line and an inline disclosure, and a profile link at the row
  end.
- **Content-capacity justification:** The capacity is held in **progressive disclosure**, not in
  visible copy. Closed, each row is a role and one line; opened, it reveals three treatment names
  on hairlines. This is the clearest 003 in the sector so far against the standard's test — the
  study is information-capable, and removing the disclosures would remove the reason it differs,
  while adding nothing to the closed state.
- **Interaction:** Native `<details>` / `<summary>`, one per practitioner, **no JavaScript**.
  Summary elements are natively focusable and announce their expanded state. The first row is open
  on arrival so the pattern is discoverable.
- **Markup constraint, recorded:** the row is deliberately **not** wrapped in a link. An anchor may
  not contain a `summary`, so the profile link sits as a separate control at the row end rather
  than the whole row being clickable.
- **Media relationship:** Four small square reserved portraits — the smallest in the batch, because
  the row has to stay a row.
- **Responsive strategy:** The intro column moves above the rows at 1024px; the profile link moves
  under the body at 768px; at 480px the row becomes a single column and the portrait widens to 3:2
  so it does not become a tiny square beside a full-width body.
- **Visual-first check:** 127 visible words, the highest in the batch — and the count includes the
  twelve treatment names that are hidden behind closed disclosures on arrival.

### WELL-S04-004 — Conversion-led

- **Structural intent / archetype:** Booking with a named person, with "no preference" treated as a
  real choice rather than a failure to choose.
- **Layout model:** A row of five equal columns. Four are practitioner cards — reserved portrait,
  role, name token, short focus line, and a filled booking action pinned to the card foot. The
  fifth is an outlined tile with **no portrait**, carrying the no-preference route.
- **Conversion behaviour, and how it stays sector-appropriate:** Nothing is collected; each action
  opens a booking route. The trap named for `004` in `../WELLNESS-DESIGN-DIRECTION.md` is the
  section collapsing into a form, and it does not. The sector-specific insight is the fifth column:
  in a spa many visitors genuinely have no preference, so the alternative is given the same width
  and the same weight as a person, and its different anatomy — no portrait, outlined rather than
  filled — is what marks it as not-a-person.
- **Separation from `WELL-S03-004`:** the other nearby conversion study places its fallback as a
  full-width band beneath the targets. Here the alternative sits inside the row as a peer.
- **Media relationship:** Four reserved portraits in five columns.
- **Responsive strategy:** 5 → 3 → 2 → 1 columns. The portrait steps 4:5 → 1:1 → 3:2, and the
  no-preference tile switches from bottom-aligned to top-aligned at 1200px so it does not float in
  a tall empty column once the row wraps.
- **Visual-first check:** 103 visible words.

### WELL-S04-005 — Art-directed / Distinctive

- **Structural intent / archetype:** The team as one continuous image rather than four cards.
- **Layout model:** A full-bleed band of four columns at **unequal widths**
  (`1.28fr 0.84fr 1.08fr 0.8fr`) running edge to edge at equal height with no gaps. Above it, a
  ruled header row whose cells use the same column template so the reserved name tokens sit exactly
  over their portraits. Each column carries its role over a scrim at its foot.
- **Distinctiveness, and why it is not paperwork:** The differentiation is proportion and adjacency
  — a wall of people. It reaches for none of the clinical or administrative devices in the sector
  anti-pattern list.
- **Empty-state device, recorded:** a gapless band of four identically toned panels would read as
  one solid block before any photography arrives. Two devices keep it legible empty — the columns
  alternate between two close tones, and each carries its role over a scrim. Once real portraits
  are placed the photographs do that work and the alternation becomes invisible.
- **Separation from `WELL-S03-005`:** that study uses separated columns at staggered vertical
  offsets. This one is the opposite — flush, gapless, equal-height, with the rhythm coming from
  differing widths rather than positions.
- **Responsive strategy:** The band stays gapless at every width; the column count halves to two at
  1024px and to one at 480px, the ruled header row is dropped at 768px rather than being squeezed,
  and the tonal alternation is re-keyed at 480px so vertically stacked columns still alternate.
- **Visual-first check:** 48 visible words, the lowest in the sector so far.

## Structural Diversity

| Study | Topology | Portrait scale | Identity treatment | Conversion behaviour |
| --- | --- | --- | --- | --- |
| 001 | Four-column card grid | 4:5, equal | Role heading, name token beneath | Profile link per card |
| 002 | Feature + statement + three-up strip | One large, three small | Same, at two scales | One profile link |
| 003 | Standing intro beside four horizontal rows | Small square | Same, in a row body | Profile link plus per-person disclosure |
| 004 | Five equal columns, four people plus an alternative | 4:5, equal | Same, plus a portrait-less fifth tile | Booking action per person, plus first-available |
| 005 | Gapless full-bleed band, unequal widths | Full column height | Name tokens in an aligned ruled row above | Link per column |

Grounds: cool stone, soft blush, warm taupe, deep teal-slate, deep oxblood. None repeats a ground
used in `WELL-S01`–`S03`.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-01.
- **Structural direction rationale:** recorded per study above.
- **Differentiation notes:** recorded in *Structural Diversity* above.
- **Visual-first check:** 48–127 visible words per study. `003`'s figure includes twelve treatment
  names sitting behind closed disclosures on arrival, so its on-screen count is lower than the
  number suggests.
- **Document-metaphor justification:** `NONE`. The ruled header row in `005` is a typographic
  alignment device that pairs a name with the portrait beneath it, not a register, ledger or
  directory table.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** `003` uses native `<details>` / `<summary>`; the other four are
  fully static. No `<script>` element appears in any file in this batch.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Portrait ×4 | `001` — one per card, above the caption band | Still image, 4:5 stepping to 3:2 | Empty tonal surface with a quiet label; role, name token and focus line stand alone |
| Portrait ×1 | `002` — the featured practitioner | Still image, 4:5 stepping to 3:2 | Empty tonal surface; the feature column carries the study without it |
| Portrait ×3 | `002` — the closing strip | Still image, 1:1 | Empty tonal surfaces; the strip reads as a deliberate row when empty |
| Portrait ×4 | `003` — small square beside each row body | Still image, 1:1 widening to 3:2 at 480px | Empty tonal surface; the row is a complete record without it |
| Portrait ×4 | `004` — one per practitioner column | Still image, 4:5 stepping to 3:2 | Empty tonal surface; the fifth column has none by design, and that difference is the point |
| Portrait ×4 | `005` — each fills a full band column, under a scrim | Still image, filling a column of fixed height | Empty tonal surface with a quiet label; tonal alternation keeps the four columns distinguishable while empty |

Empty reserved media areas are intended output, not defects. A filled portrait slot in this section
means a photograph of a real person who has consented to appear.

**Media-density note.** Every study carries four portraits — one per practitioner — except `002`,
which carries the same four at two different scales. None approaches a contact sheet.

## QA

- ID validation: **PASS.** All five planned IDs exist; every `study-id` meta matches its filename.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport in every study. Nesting was validated with a stack-based parser rather than tag counting
  — see the note below — and all five parse with correctly balanced, correctly ordered elements.
- Accessibility QA: **PASS.** Every study sets `lang`, scopes a `:focus-visible` ring, labels its
  section with `aria-labelledby`, honours `prefers-reduced-motion`, gives every interactive element
  a 44px-or-greater target, and marks decorative arrows `aria-hidden`. `003`'s disclosures are
  native `summary` elements, which are focusable and announce their state without any ARIA.
- Responsive QA: **PASS.** Four authored breakpoints per study, recorded per study above —
  including `002`'s decision to keep its strip as a rail at 480px and `005`'s decision to drop the
  ruled header row rather than squeeze it.
- Dependency validation: **PASS.** No framework, CDN, remote asset, embedded image or script.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status, per the
  divergence from `ARC-S08` recorded above.
- Scoped-CSS check: **PASS.** Every declaration outside the `html` / `body` host baseline is
  namespaced to that study's own `.well-s04-00N` root, verified by scan.
- Identity and credential check: **PASS.** Visible copy scanned, with comments stripped, for
  qualification, licence, registration, accreditation, award, membership, diploma, years of
  experience, rating and review vocabulary, and for currency and percentages. Clean in all five.
  One draft line in `004` read "everyone here is trained across the treatments they are listed
  under"; *trained* is a credential claim, and it was changed to *works across* before this scan.
- Render check: **PASS, after one correction.** All five studies were rendered in headless Chrome
  at 1440px and inspected. `003`'s disclosure was confirmed to work — the open row shows its list,
  the other three are collapsed. One concept-breaking bug was found and fixed: `005`'s columns were
  given `aspect-ratio: 3 / 4`, so columns of deliberately unequal **width** rendered at unequal
  **height** and the "continuous band" became a ragged staircase. The columns were changed to a
  shared fixed height at each breakpoint, which is what makes the band continuous.

**Tooling note.** The first tag-balance scan of this batch reported failures that were all
artefacts of the checker, not the files: `<details>` and `<summary>` counted from the prose inside
an HTML comment, "rating" matched inside "Hydrating facial", and `<a[^>]*>` matched `<article>` and
so reported a nested-anchor violation that did not exist. The checks were redone with a stack-based
parser over comment-stripped markup, and a visible-text-only claims scan. The results above are
from the corrected checks.

## Notes

- This is the fourth authored batch in the `WELL` sector and the second authored entirely without
  references.
- The identity rule established here — role leads, name reserved, no credentials in any form —
  should carry forward to `S26` when that section is authored, and to the equivalent people
  sections in every other sector.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO`
  batch. Regenerating it fails on this machine because `python3` resolves to a placeholder rather
  than an interpreter. Headless Chrome, which the generator uses for measurement, is present and
  working — it was used for the render check above.
