# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S16`
- Section Name: `Locations`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S16-001` | Universal / Safe | AUTHORED | `raw/WELL-S16-001.html` |
| `WELL-S16-002` | Premium / Editorial | AUTHORED | `raw/WELL-S16-002.html` |
| `WELL-S16-003` | Structured / Visual Modular | AUTHORED | `raw/WELL-S16-003.html` |
| `WELL-S16-004` | Conversion-led | AUTHORED | `raw/WELL-S16-004.html` |
| `WELL-S16-005` | Art-directed / Distinctive | AUTHORED | `raw/WELL-S16-005.html` |

Direction definitions are in `standards/01-AUTHORING-STANDARD.md` and their sector reading is in
`../WELLNESS-DESIGN-DIRECTION.md`. The section's role, its governing constraint and its boundary
with `S19` and `S27` are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Governing Constraint

Almost everything a locations section normally contains is a verifiable fact about a real building.

| Element | Treatment |
| --- | --- |
| Address, postcode, city | **Reserved field** — every studio has one, so the empty field asserts nothing |
| Phone number | **Reserved field** |
| A map | **Reserved area.** An embedded map is a remote dependency, which the workspace forbids outright — so a map here is a slot, never a frame |
| Exterior photograph | **Reserved media area** |
| Opening hours | **Omitted entirely**, on the same basis as durations |
| Directions, transport, parking, access | **Reserved field where present, never written** |

**No description of the building.** This is the constraint that catches people out. Writing *"a
converted townhouse on a quiet street"* invents a property as surely as inventing an address does.
**No study in this batch describes what a site looks like, what it is near, or what kind of
building it occupies** — the compositions carry that weight instead, which is why every study
reserves generous space for a map or an entrance.

**No embedded map in any study**, verified by scan for `<iframe>`, `<embed>` and `<object>`. `005`
puts the map at full-bleed scale specifically to make the point that scale does not change the
rule; it only changes how obvious the omission is.

**Not present in any study:** an invented address, street, postcode, city, region, phone number,
email, map coordinate, travel time, distance, transport line, parking claim, access claim or
opening hour. The only digits in visible copy are the site tokens `Studio 01`–`03`, on the
`Practitioner NN` convention from `S04`.

## The Structural Fact This Batch Handles

**How many sites there are is a structural fact, not a claim — and it changes the section
completely.** A single-site studio does not need a chooser, a comparison or a set; a studio with
ten cannot use a row of cards. Rather than assume one shape and let a reviewer adapt it, the batch
demonstrates the range:

| Study | Case | Why that shape |
| --- | --- | --- |
| `002` | **One site** | One door, shown well. No chooser, no set. |
| `001` | **Two sites** | Equal cards side by side; the comparison is the layout. |
| `004` | **Three sites** | A compact list, because the panel beside it is the subject. |
| `003` | **A network** | Disclosures — one line per site closed, identical when open, so three sites and thirty are the same composition. |
| `005` | **Three sites** | Full-bleed bands, one per site, where the map is the composition. |

## The Access Line

Every study states that access needs are settled by asking rather than by reading a badge. That is
honest for a placeholder — it does not know what the building is — and `004` argues it is better
practice than the alternative even for a real studio: **a symbol cannot tell you about the step at
the door, how heavy it is, or where the nearest place to be dropped off is**, and it is wrong often
enough to be worse than nothing. **No access symbol or badge appears in any study**, which is the
specific omission `004` exists to argue for.

`003` goes one step further and reserves a per-site *"getting in"* field, because the buildings are
not the same and a single sector-wide access statement would flatten a real difference.

## Study Records

### WELL-S16-001 — Universal / Safe

- **Layout model:** Two equal cards, each with a 16:9 reserved map, the site token, reserved address
  and phone fields on hairlines, and a directions route pinned to the card foot.
- **The two-site case:** equal treatment is the content. Neither is the flagship, and the copy says
  they run the same way and cost the same, so the layout is not implying a hierarchy the studio
  does not have.
- **Responsive strategy:** cards unstack at 768px with the map becoming 3:2; the field rows go to a
  stacked label-above-value at 480px so a reserved value never gets squeezed.

### WELL-S16-002 — Premium / Editorial

- **Layout model:** One 21:9 reserved entrance plate at full width, a serif line above it, and a
  spare address block beneath split against a small reserved map.
- **The single-site case, and the copy problem it exposes:** an editorial locations section wants to
  describe the building, and that is exactly what cannot be written. **The editorial act here is
  the composition** — the plate is given the room the prose would have taken. It is the lowest word
  count in the batch by a wide margin and the largest single reserved area.
- **Responsive strategy:** the plate steps 21:9 → 16:8 → 16:10 → 4:3; the block unstacks at 768px.

### WELL-S16-003 — Structured / Visual Modular

- **Layout model:** Each site is a native `<details>` showing its token and reserved address when
  closed, opening to a reserved map and the full field set.
- **The structural argument:** this is the study that has to **scale**. `001` and `002` break down
  once a studio has more sites than fit a row; a disclosure list does not. The closed row carries a
  reserved address deliberately — a visitor scanning for the nearest site should not have to open
  all of them.
- **The per-site access field:** *"getting in"* is reserved per site rather than stated once,
  because the buildings differ. That is the honest structure, and it is recorded in the visible
  closing line.
- **Interaction:** native `<details>` / `<summary>`, first open, no JavaScript.
- **Responsive strategy:** the summary drops from three columns to two with the address peek moving
  to its own row at 768px; the detail unstacks at the same breakpoint.

### WELL-S16-004 — Conversion-led

- **Layout model:** The access commitment given a cream panel with the action, beside one reserved
  map covering all sites and a compact three-site list.
- **Conversion device:** what stops someone travelling to a spa is not which street it is on — it
  is not knowing whether they will be able to get in and around comfortably, and not wanting to
  arrive and find out. Most sites answer with a symbol. **This study makes the answer a
  conversation**, which the studio can honour, which is more useful than an icon, and which is the
  reason a visitor with a specific need picks this studio over one showing only a glyph.
- **The third promise is the one that earns trust:** *if none of them works, we will tell you that
  too rather than let you find out on the day.*
- **Responsive strategy:** the split unstacks at 1024px; the action goes full width and the site
  rows restack at 768px.

### WELL-S16-005 — Art-directed / Distinctive

- **Layout model:** Three full-bleed reserved map bands stacked, each with its site token set at up
  to 4.4rem **inside** the band over a scrim, and the reserved fields on a rule beneath.
- **The device:** everywhere else in this batch — and on most real sites — the map sits inside a
  card, which makes it decorative. Here each band runs edge to edge and the name sits in it, so the
  reserved area is unmistakably the subject. The heading says so.
- **Empty-state check:** the name is set over a bottom scrim rather than over bare tone, so it stays
  legible whether the band carries a map or the reserved fill. Confirmed in render.
- **Responsive strategy:** the band height compresses at 768px and the directions link loses its
  right-alignment, but the full-bleed band and the name-inside-it relationship hold at every width.

## Structural Diversity

| Study | Topology | Sites | Map treatment | Ground |
| --- | --- | --- | --- | --- |
| 001 | Two equal cards | 2 | 16:9 inside each card | Warm pale |
| 002 | One full-width plate + address block | 1 | Small, beside the address | Soft grey-green |
| 003 | Disclosure list, scales to any number | 3+ | Revealed on open | Pale sand |
| 004 | Commitment panel + compact list | 3 | One, covering all sites | Deep slate blue |
| 005 | Three full-bleed bands | 3 | **The composition itself** | Near-black cool |

Grounds do not repeat any used in `WELL-S01`–`S15`.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-01.
- **Visual-first check:** no study derives its distinctiveness from copy. Because the place cannot
  be described, the differentiator across the batch is entirely how many sites are shown and how
  large the reserved map is — which is the correct outcome for this role.
- **Document-metaphor justification:** `NONE`. No branch register, directory listing, address book
  or store-locator table is used.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** `003` uses native `<details>`; the rest are static. No `<script>`,
  no inline `style`, and **no `<iframe>`, `<embed>` or `<object>`** in any file.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Map ×2 | `001` — one per site card | Static map image, 16:9 | Empty tonal surface with a quiet label. **Never an embedded map frame** |
| Entrance | `002` — the single site, at full width | Still image, 21:9 stepping to 4:3 | Empty tonal surface; the address block stands alone |
| Map ×1 | `002` — small, beside the address | Static map image, 4:3 | As above |
| Map ×3 | `003` — one per site, revealed on open | Static map image, 16:9 | As above |
| Map ×1 | `004` — one covering all sites together | Static map image, 16:10 | As above |
| Map ×3 | `005` — full-bleed band per site | Static map image, band height | Name set over a scrim so it reads against fill or photograph |

Address, phone and access fields are **reserved text slots** — em dash with a visually hidden field
label. Counted by scan: 27 slots across the batch, 27 labelled.

## QA

- ID validation: **PASS.** All five IDs exist and match their filenames.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport. Nesting validated with a stack-based parser; all five parse correctly.
- Accessibility QA: **PASS.** `lang`, scoped `:focus-visible`, `aria-labelledby`,
  `prefers-reduced-motion`, 44px-plus targets. All 27 reserved slots carry a visually hidden field
  label, so no assistive technology encounters a bare em dash.
- Responsive QA: **PASS.** Breakpoints authored per study and recorded above.
- Dependency validation: **PASS, with an added check.** Scanned for `<iframe>`, `<embed>` and
  `<object>` as well as scripts, remote sources and inline styles — **zero matches**. This is the
  one section where the obvious implementation is a remote embed, so the check was made explicit.
- Section-shell check: **PASS.** Verified by scan.
- Visible-copy check: **PASS.** No study displays a note about its own placeholder status.
- Scoped-CSS check: **PASS.** Every declaration outside the host baseline is namespaced to the
  study's own `.well-s16-00N` root. A **CSS validity scan** was added for this batch and caught one
  real defect — see the render note below.
- **Address and access check: PASS.** Visible text only, comments stripped, scanned for street-type
  words, postcode patterns, phone patterns, travel times, *nearest station*, *parking*,
  *step-free*, *wheelchair*, day names, opening phrasing, currency and any digit. Every match
  resolved to a **visually hidden field label** (*Street address*, *Telephone number*, *Entrance and
  access details*), to the word *open* describing a disclosure state, or to the site tokens
  `Studio 01`–`03`. Nothing invented.
- Render check: **PASS, after one correction.** All five rendered in headless Chrome at 1440px and
  inspected. One defect was found **before** render, by a CSS-validity scan added for this batch:
  `002` carried `--slot-ink: #55605６` — a full-width digit at the end of a hex colour, which is
  invalid, would have been dropped by the parser, and would have left the slot labels at the
  inherited dark ink rather than the intended muted tone. Corrected to `#556056`. `005`'s
  full-bleed bands and inside-band names render as intended.

## Notes

- This is the sixteenth authored batch in the `WELL` sector and the fourteenth authored entirely
  without references.
- **Two reusable outcomes.** First: *how many of a thing there are* is a structural fact a batch can
  demonstrate rather than assume — it applies to locations, teams, branches, product lines and any
  other set whose size changes the composition. Second: **where the obvious implementation is a
  remote embed — a map, a video, a booking widget, a review feed — the reserved area is the answer,
  and the dependency check should name that element type explicitly.**
- The CSS-validity scan is now worth running on every batch. It caught a defect that no visual check
  would reliably have caught, because an invalid custom property fails silently into an inherited
  value that still looks plausible.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch.
  Regenerating it fails on this machine because `python3` resolves to a placeholder rather than an
  interpreter. Headless Chrome, which the generator uses for measurement, is present and working.
