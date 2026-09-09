# BATCH V1

## Batch Identity

- Sector: `Construction & Contractors`
- Prefix: `CON`
- Section ID: `CON-S27`
- Section Name: `Office / Regional Branch Detail`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `CON-S27-001` | Universal / Safe | AUTHORED | `raw/CON-S27-001.html` |
| `CON-S27-002` | Premium / Editorial | AUTHORED | `raw/CON-S27-002.html` |
| `CON-S27-003` | Structured / Visual Modular | AUTHORED | `raw/CON-S27-003.html` |
| `CON-S27-004` | Conversion-led | AUTHORED | `raw/CON-S27-004.html` |
| `CON-S27-005` | Art-directed / Distinctive | AUTHORED | `raw/CON-S27-005.html` |

Twenty-seventh and final batch in the `CON` sector. Role and boundaries in `./README.md`.

## Authoring Direction

No reference images were supplied for this section. All five studies were originated.

## The Governing Constraint — Almost Nobody Reading This Is Coming Here

A location page assumes a visitor. In this industry that assumption is wrong, and being wrong about
it decides the whole section:

    A contractor's office is not a shop. Almost nobody who reads this page is coming
    here, and the client least of all — their meetings happen on their own site.

So the page is not directions. It answers the question a client actually has — **whether this is the
office whose mornings reach their job** — and it answers the three people who genuinely do turn up.

## The Three People Who Actually Come

Named in every study, in the order of how many arrive:

| Who | What the page owes them |
| --- | --- |
| **A delivery** | The wagon comes to the yard gate rather than the office door, somebody in the yard signs, and the middle of the morning is easiest once the gangs have gone |
| **A supplier or subcontractor** | **Turning up unannounced is not how anybody gets on a list.** Send what you do, where you work and your insurances |
| **Somebody looking for work** | Early, before the gangs go out, and ask for the yard foreman. **There is no form, because a form would be slower than the walk** |

> A client is not on that list, and that is the most useful line on the page.

It is useful because it *routes*: if you have a live job the person you want is on it or driving to
it, and the number you want is your site's rather than this office's.

## A Yard Is A Place Things Leave From

The place is described by its output rather than by its appearance, which also happens to be the only
part a catalog can author honestly:

| Leaves here | And what it means |
| --- | --- |
| **Plant off our own yard**, the same day | The only reason a yard is worth what it costs to keep |
| **The fitter, in a van** | A breakdown is a drive rather than a call to a hire desk |
| **The manager, before the gangs** | What makes the morning visit on your site possible at all |

And the honest half, which a location page normally omits entirely: **past the region this office
runs, none of that travels.** Plant is hired locally, the fitter becomes a telephone call, and the
job is run from another office — named, rather than managed from the wrong end of a motorway.

## The Arrival Rule, And Access By Conversation

The one piece of real arrival information a construction office can publish without inventing
anything:

    You cannot cross the yard in what you drove in. Boots and a hi-vis, or you will be
    met in the office instead — which is fine, and is what most people should do anyway.

And access, carried unchanged from `WELL-S16` and `WELL-S27`: **a row of facility ticks would be
invented, and a tick is a promise about a place nobody has measured.** Worse here than in most
sectors, because **a yard is not a level floor** and is not the same place two months running. So the
page commits to the conversation instead: *tell us before you come and we will say honestly what the
route from the gate is like, including when the answer is that it is not passable that week.*

## Study Records

| Study | Ground | Model | Anchors |
| --- | --- | --- | --- |
| `001` | `#eef0e9` | Contact first, what leaves, who is based here, the three who come, the reserved map last | none |
| `002` | `#f9f1d8` | **The notice at the gate**, in five clauses. No map and no media at all | none |
| `003` | `#d3d9d5` | Modules ordered by who the page is for, with **the route in** as a sequence | none |
| `004` | `#16191f` | **The honest routing** — four reasons to be reading, three of them ending elsewhere | the batch's only ones |
| `005` | `#b9b2a4` | **The location page inverted**: what leaves the yard at display scale, the map a strip | none |

### `002`, the gate notice

The document at the gate of a yard: terse, imperative, addressed to whoever happens to arrive, and
written **in the order they arrive.** It is the only thing in this trade addressed to an unknown
reader standing in front of it, which is exactly what a location page is.

Distinct from the colophon of `S16-002`, the standfirst of `S21-002`, the errata of `S24-002`, the
head-note of `S25-002` and the handover note of `S26-002`.

**It carries no map and no photograph**, and says why: *a photograph of a gate is not a gate, and this
notice is for people already standing at one.*

### `003`, the route in

This variant's trap is the specification table, and a location page invites it harder than any other
section — hours, facilities, ticks, a grid of amenities. So the dense module is **a sequence rather
than a specification**: ring, then the gate, then somebody walks you over. The arrivals module's
third column is **what happens if you ignore it**, which a specification table cannot express.

### `004`, four reasons and three exits

The conversion-led study of a location page normally ends in *plan your visit*. This one opens by
saying most readers are in the wrong place and spends its largest block sending them elsewhere:
**three of its four rows end somewhere other than this office.**

> An office that collects visits it cannot use is wasting somebody's morning, and it is never its own.

### `005`, the page inverted

The largest thing on a location page is normally the map or the building. Here it is **what leaves the
yard**: *Plant. The fitter. The manager* — set at display scale, each with where it goes. The address
is small, complete and first; **the map is a strip at the foot, and the study says it is that size on
purpose.**

## The Scaffold's Responsive Rule, Made Structural

> Address and contact details are the content most likely to be needed on a phone and must be
> first-class at small widths, **not pushed below decorative media**.

Carried from `WELL-S27` and enforced: **in every study the contact block comes before any map or media
area in source order.** There is no width at which it can reflow below one, because it never comes
second. The checker compares the source position of the first reserved contact field with the first
media area and fails the study if the order is wrong.

## Compliance

- Structural validation: **PASS.** All five parse; tag nesting verified on a stack for every study.
- Metadata validation: **PASS.** Fourteen research fields plus viewport on all five; `study-id`
  matches filename; territories match the core set in order.
- Isolation: **PASS.** No `<script>`, `<iframe>`, inline `style`, event-handler attribute, remote
  reference, embedded image, inline SVG or form control anywhere in the batch. **A map is never an
  embed in this catalog, and there is nothing here for one to load.**
- **One-mechanism check: PASS.** One anchor, in `004`, routing in-page.
- **Audience check: PASS.** *Not a shop* and *almost nobody reading this is coming here* in all five,
  with the client told they are not the audience.
- **Three-arrivals check: PASS.** Delivery, supplier or subcontractor, and somebody looking for work
  in all five, each with its own honest route.
- **Arrival-rule check: PASS.** *Boots and a hi-vis* in all five; *ring first* in all five.
- **Access check: PASS.** Answered by conversation in all five, with *a yard is not a level floor* as
  the stated reason there are no facility ticks.
- **Output check: PASS.** What leaves the yard in all five, and the honest half — hired locally, run
  from another office — in all five.
- **Coverage check: PASS.** *There is no such thing as national coverage from one yard* in all five.
- **Map check: PASS.** Every map is a reserved area labelled *never an embedded service*, and every
  study prints what it would be worth: **the one fact on this page that will not help you.**
- **Hours check: PASS.** No hours anywhere, and the refusal is stated: *an empty hours table asserts a
  weekly schedule.*
- **Contact-before-media check: PASS.** In all four studies that carry media; `002` carries none and
  declares `media-mode: none`.
- **Density check: PASS.** Between eighty-six and one hundred and eighty-three visible words per
  reserved field.
- **Placeholder check: PASS.** No em-dash placeholder; every reserved value labelled; the address is
  a reserved field in all five.
- **Drawing check: PASS.** Nothing drawn at an angle.
- **No-refusal-region check: PASS.** The architecture run carries none.
- **Digit check: PASS.** No digit in visible copy in any of the five — no postcode, no telephone
  number, no hours, no travel time, no distance.
- Responsive QA: **PASS.** Verified at 1440px; each study states its ladder.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.**
- Section-shell check: **PASS.**
- Scoped-CSS check: **PASS.**
- Markdown-artefact check: **PASS.**
- Ground check: **PASS.** Five distinct grounds, none used by `S01`–`S26`.
- Render check: **PASS**, after four corrections.

## Corrections Before Render

| Study | Was | Now |
| --- | --- | --- |
| `003` | *There is no such thing from one yard* — the sector's coverage refusal, one clause short of the sentence every other study prints | Completed. A refusal that is only recognisable in context is not a refusal |
| `001`, `003` | The contact grid wrapped one field onto a second row, leaving a half-empty band | Track minimum tightened so all five and all six sit in one row. **The contact block is this section's structural promise and it should look like one thing** |
| `003` | The last pair set a tall reserved-areas module beside a short one, so half a card was empty | The two reserved areas sit side by side |
| `004` | The head ran in one column with an empty right half, and `.head p` was overriding the eyebrow's own margin | Two columns, and the lead given its own class |
| `005` | The gate band was full width with its text capped at seventy-six characters, so half of it was empty | Three columns across the band |

## Checker Note

**The checker's own ban list produced the batch's only hard failures**, and it deserves recording: a
rule banning *nearest station* fired on three studies that were **refusing** to print one — *no
directions, travel time or nearest station.* A ban that cannot tell a claim from its refusal is a
worse rule than no ban, and the digit check already makes an invented distance impossible.

The batch's own new check is the **contact-before-media check**: the source position of the first
reserved contact field must precede the first media area. It is the second check in this catalog
derived from a responsive rule rather than a content one — `S26` made *portrait and name* one element;
this makes *contact above media* an order that cannot reflow.

The second is the **reserved-area label check**: every map and media rectangle must be labelled
beginning *Reserved*, so an unlabelled grey box can never pass as a design decision.

## Notes

- Twenty-seventh authored batch in the `CON` sector. **`S01`–`S27` are complete — one hundred and
  thirty-five studies.**
- **The reusable outcome is the audience question.** Before a location page is designed, somebody
  should ask who actually arrives. In this industry the answer is a delivery, a subcontractor and
  somebody looking for work — and the page written for those three is more useful to a client than
  the page written for the client, because it tells them plainly where their answer is instead.
- The second is the inversion in `005`. **A yard is a place things leave from**, so the honest largest
  element on the page is its output rather than its appearance. That reasoning transfers to any
  location whose visitors are not customers.
- The third is the arrival rule. **Boots and a hi-vis** is the only piece of arrival information a
  contractor can publish that is real, is checkable and is not a promise about a building nobody has
  measured — and it is worth more than a row of ticks.
