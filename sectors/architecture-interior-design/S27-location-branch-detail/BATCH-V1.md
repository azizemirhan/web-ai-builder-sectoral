# BATCH V1

## Batch Identity

- Sector: `Architecture & Interior Design`
- Prefix: `ARC`
- Section ID: `ARC-S27`
- Section Name: `Studio / Location Detail`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Default Territory | Status | Raw File |
| --- | --- | --- | --- |
| `ARC-S27-001` | Universal / Safe | AUTHORED | `raw/ARC-S27-001.html` |
| `ARC-S27-002` | Premium / Editorial | AUTHORED | `raw/ARC-S27-002.html` |
| `ARC-S27-003` | Dense / Information-heavy | AUTHORED | `raw/ARC-S27-003.html` |
| `ARC-S27-004` | Conversion-led | AUTHORED | `raw/ARC-S27-004.html` |
| `ARC-S27-005` | Sector-native / Distinctive | AUTHORED | `raw/ARC-S27-005.html` |

## Authoring Direction

**No reference images were supplied.** Authored against the section README, which names the failure
mode outright:

> *"Every address, coordinate, hour and contact route in a study must be an obvious placeholder.
> Fabricating a plausible address is the failure mode this role invites."*

> *"Address and contact details are the content most likely to be needed on a phone and must be
> first-class at small widths, not pushed below decorative media."*

> *"A map area is a reserved slot, not an embedded service."*

### Nothing here is plausible, on purpose

Every address line in the batch reads `Street address line 1`. Every hour reads `HH:MM–HH:MM`. Every
telephone and email reads `supplied by the studio`. Every coordinate reads `reserved field`. A
digit-level scan of the visible text of all five studies returns **no phone number, no email
address, no coordinate pair and no street number** — the only digits on any page are location and
person indices, address line numbers, step numbers and the section IDs quoted in the closing notes.

`003` goes one step further, because a dense sheet is where a travel time gets invented: **no
distance or duration is stated as a number anywhere**, and the distance column of the arrival table
holds reserved fields instead. `004` withholds the three claims a visit page invites — when the
studio can see you, how quickly it replies, and that a visit is available at all.

### The map, and the address-first rule

No study loads a map. Each carries a **reserved slot** with a visible label saying it is not a map
and that no third-party service is embedded; the dependency scan confirms zero external requests of
any kind across the batch.

The address-first rule is answered structurally rather than by styling. In `001`, `003`, `004` and
`005` the address, contact and hours appear **before any media in source order**, so no reflow can
push them under an image. `002` is the one study where an editorial page wants its plate first, and
the compromise is made explicit on the page: a compact address-and-telephone line sits directly under
the title, **above** the first plate, with the full register repeated at the foot.

## Study Records

### ARC-S27-001 — Universal / Safe

- **Structural intent / archetype:** The plain location page. Address, contact and hours in a
  three-column band directly under the title, then the image, then what happens here, what is
  available, getting here, a reserved map and who is based here.
- **Layout model:** Details band at three columns between rules; body at `1.4fr / 1fr` with the map
  and the people list in the aside.
- **Density:** Medium. **Media:** one `16/9` place image, one `4/3` reserved map. **Interaction:**
  none.
- **Responsive strategy:** Details band 3 → 2 → 1 columns and always stays above the image; body
  collapses at 1024px; image becomes `4/3` and the map `1/1` at 480px.
- **Composer value:** The safest binding target —
  `{name, summary, address, contact[], hours[], media, what_happens, available[], directions[], map, people[]}`.
- **Limitation / content ceiling:** Four contact routes, four hour rows, four availability rows.

### ARC-S27-002 — Premium / Editorial

- **Structural intent / archetype:** The place described as a building rather than as an address —
  the register a practice uses about its own premises.
- **Layout model:** Centred title, a compact address line between rules, a `21/9` plate, prose at a
  `34rem` measure, a plate pair, and a three-column address / contact / hours register plus a
  reserved map at the foot.
- **Density:** Low. **Media:** three plate areas plus a reserved map. **Interaction:** none.
- **Responsive strategy:** Measure narrows then releases at 768px, where the compact line also
  left-aligns; register 3 → 2 → 1 columns; plates `21/9` → `16/9` → `4/3`.
- **Composer value:** The editorial register, and the only study that describes the premises in
  prose. Its content model is the smallest in the section.
- **Limitation / content ceiling:** Two prose sections and three plates. It holds no tables; a
  location with real operational detail belongs in `003`.

### ARC-S27-003 — Dense / Information-heavy

- **Structural intent / archetype:** The location details sheet — every operational fact a visitor
  or a courier could need, in tables, open on the page.
- **Layout model:** Identification band, then three tables (contact routes, hours by day, access and
  arrival), a services-and-people pair, and a reserved map area.
- **Density:** High — the densest in the section. **Media:** reserved map only; a details sheet needs
  no photography. **Interaction:** none, and nothing is hidden behind a control.
- **Responsive strategy:** Identification collapses at 1024px, the two-up bodies at the same
  breakpoint; every table scrolls inside its own `overflow-x` container with a `min-width`, so the
  page body never scrolls sideways.
- **Composer value:** The highest-capacity option, and the only one modelling **hours as rows** and
  **arrival as a route table** — `{route, distance, note}` with distance reserved.
- **Limitation / content ceiling:** Seven day rows, six arrival routes, four contact routes.

### ARC-S27-004 — Conversion-led

- **Structural intent / archetype:** The page ordered around arranging a visit, with the address
  carried inside the decision header rather than below the fold.
- **Layout model:** Decision header at `1.2fr / 1fr` — title, summary and address on the left, a
  bordered action box with contact and hours on the right — then a self-selection pair, three
  arrangement steps, a "before you come" pair holding the reserved map, and a filled closing band.
- **Density:** Medium. **Media:** reserved map only. **Interaction:** none; no form.
- **Responsive strategy:** Header collapses at 1024px with the address still above everything else;
  fit pair, steps and the two-column block go single at 768px; buttons full width at 480px.
- **Composer value:** The conversion register for a location. Adds
  `{visit_reasons[], visit_alternatives[], steps[], bring[]}`.
- **Limitation / content ceiling:** Four reasons against three, three steps, four things to bring.

### ARC-S27-005 — Sector-native / Distinctive

- **Structural intent / archetype:** The **keyed approach**. An architect describes a building by
  how it is arrived at — street, threshold, stair, floor — and keys each move to a letter on a plan.
- **Layout model:** Head carrying title and address above a heavy rule; then the approach at
  `1fr / 0.86fr` — five lettered steps beside a reserved plan area — a floor register continuing the
  same lettering in three columns, and a three-column foot of contact, hours and reserved map.
- **Density:** Medium. **Media:** one reserved plan area, one reserved map. **Interaction:** none.
- **Responsive strategy:** The plan area drops **below** the sequence at 768px rather than shrinking,
  because the lettered steps are the information and the plan is the illustration; floor register
  3 → 2 → 1; the key discs shrink but never fall below a legible size.
- **Composer value:** The identity option and a **seventeenth sector-native register** for the
  sector. Content model `{approach[{key, name, note}], floor_key[{key, room}]}` — arrival described
  as a sequence, which no generic location component carries.
- **Limitation / content ceiling:** Five approach steps and six floor keys is the tested shape.

## Research Metadata

- **Sources:** None. Authored against the section README.
- **Research date:** 2026-08-31
- **Structural territory rationale:** Territories were mapped onto the five things a location page
  can be — a set of details, a description of a building, an operational sheet, an invitation to
  visit, and a set of directions.
- **Differentiation notes:** Five distinct geometries: details band over a two-column body; centred
  editorial measure; tabular sheet; decision header; lettered approach against a plan. Grounds
  differ — near-white, warm paper, cool grey, warm off-white, paper. Media differs — 2, 4, 1, 1 and
  2 areas, of which the map or plan is always reserved. **No study uses JavaScript.**
- **Sector-interpretation note:** `S17 Studio Locations` is the index of every location; this is the
  depth page behind one of its entries, and no study here lists more than one location.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE
- External assets: NONE — no `<link>`, `<img>`, `@import`, `url()`, webfont, inline SVG or inline
  `style` attribute in any of the five files.
- **Map services: NONE.** No `<iframe>`, no embed, no tile request, no geocoding call. Every map is a
  bordered reserved slot with a visible label.
- Network calls: NONE. Browser storage: NONE. JavaScript necessity: NONE.

## Media Slots

| Slot | Study | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- | --- |
| `place`, `map` | `ARC-S27-001` | Image of the studio; reserved map | Photograph `16/9`; map `4/3` | Both may be empty. Address, contact and hours sit above the image in source order and never move below it. |
| `plate-1…3`, `map` | `ARC-S27-002` | Lead plate, interior pair; reserved map | Photograph `21/9` and `4/3` | The compact address line stays above the lead plate at every width. |
| `map` | `ARC-S27-003` | Reserved map | — | The only slot on the sheet. Every operational fact is text. |
| `map` | `ARC-S27-004` | Reserved map inside "before you come" | — | Directions are confirmed in writing by the studio, not drawn here. |
| `plan`, `map` | `ARC-S27-005` | Reserved plan keyed A–E; reserved map | — | The lettered sequence is real text and reads on its own with the plan empty. |

No slot in this batch loads or implies a third-party map, and none carries a review, rating, badge or
logo.

## QA

- **ID validation: PASS.** Five IDs with matching `<meta name="study-id">`, `data-study-id`, scoped
  root class and filename; every element `id` namespaced and unique.
- **Raw-format validation: PASS.** Tag balance, nesting and unique-id checks pass; unscoped-CSS and
  inline-`style` scans return zero.
- **Location-policy QA: PASS — the key check for this section.** A pattern scan of the visible text
  of all five studies for email addresses, telephone-shaped digit runs and coordinate pairs returns
  **zero matches**. Every address line, hour, coordinate, distance and duration is a token or a
  reserved field. No review, rating or claim is attributed to any location.
- **Address-first QA: PASS.** In `001`, `003`, `004` and `005` the address and contact block precedes
  every media element in source order. `002` places a compact address-and-telephone line above its
  lead plate and repeats the full register at the foot; the deviation and its reason are stated on
  the page itself.
- **Accessibility QA: PASS.** One `<h1>` per study, no heading jumps, every `aria-labelledby`
  resolving, every `<a>` with an `href`, `<address>` used for postal addresses and labelled by its
  own heading, `:focus-visible` in all five with a light focus colour inside dark panels,
  `prefers-reduced-motion` in all five. The arrival keys in `005` are text characters, not marks.
- **Contrast QA: PASS.** 30 pairs measured across this section: all text ≥ 4.5:1, all component
  boundaries ≥ 3:1 — including the reserved map and plan slot labels, which sit on the palest fills
  in the batch. No failures.
- **Responsive QA: PASS by static review at 1440, 1280, 1024, 768, 430, 390 and 320px.** All five
  define the 1280 / 1024 / 768 / 480 / 360 ladder; every grid track uses `minmax(0, …)`; all three
  tables in `003` scroll inside their own containers.
- **Role-compliance validation: PASS.** No study carries a list of all locations, which belongs to
  `S17`.
- **Not run here:** rendered-screenshot capture, real-browser and assistive-technology testing.

## Notes

- The reserved map slot should survive normalisation as a **first-class slot type**. A location
  component that treats "map" as an embed has no honest empty state; this batch treats it as a media
  area that happens to be a map, which does.
- `ARC-S27-005` adds a seventeenth sector-native register — the keyed approach. It was checked
  against the key plan of `ARC-S22-005`: that register locates a *page within a set* and its cells
  are links, so it is navigation; this one locates a *visitor within a building* and its letters key
  to physical moves, so it is arrival information.
- Every study marks its top region `data-region="page-context"`.
- `planning/PROGRESS.md` and `planning/SECTOR-STATUS.md` roll-up counters are unchanged; they need a
  separate workspace-level pass.
- No review, normalisation, survivor-selection, or promotion decision is recorded in this document.
