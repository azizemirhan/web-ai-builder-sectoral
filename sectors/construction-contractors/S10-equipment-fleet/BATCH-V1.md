# BATCH V1

## Batch Identity

- Sector: `Construction & Contractors`
- Prefix: `CON`
- Section ID: `CON-S10`
- Section Name: `Equipment Fleet`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `CON-S10-001` | Universal / Safe | AUTHORED | `raw/CON-S10-001.html` |
| `CON-S10-002` | Premium / Editorial | AUTHORED | `raw/CON-S10-002.html` |
| `CON-S10-003` | Structured / Visual Modular | AUTHORED | `raw/CON-S10-003.html` |
| `CON-S10-004` | Conversion-led | AUTHORED | `raw/CON-S10-004.html` |
| `CON-S10-005` | Art-directed / Distinctive | AUTHORED | `raw/CON-S10-005.html` |

Tenth batch in the `CON` sector, and the section `S05` fenced in advance. Role and boundaries in
`./README.md`.

## Authoring Direction

No reference images were supplied for this section. All five studies were originated.

## The Governing Constraint — The Specification You Need Is The Site's

The sector direction names this section's trap while describing a different variant: *becoming a car
advert; the subject is the work, not the plant.* On an equipment page that warning governs all five
studies, because a fleet list **is** a car advert by default — machines photographed clean, with
their weights printed underneath.

    A fleet list is a car advert with the prices removed. A specification tells you what a
    machine can do somewhere. It does not tell you whether it can get onto your site.

So no study is organised by machine. Every one is organised by **the site condition each machine
answers**, and the check tests that on the content rather than on a class name — access, ground and
standing, hours and noise, the route across the highway, the thing next door that must not move, and
height without a crane.

The machine name is demoted everywhere in the batch. In `005` it is a chip beside a headline; in
`003` it is the label on a card under a tier; in `002` it appears inside continuous prose. **Nowhere
is it the largest thing on the page.**

## The Media Rule, Stricter Here Than Anywhere Else In The Sector

The sector media direction allows *plant media — machinery in use*. On this page that stops being a
preference:

    No reserved area may be captioned for a machine at rest.

A photograph of clean plant on a forecourt is an advertisement; the same machine with an operator in
it, working, in mud, is evidence. `CON-S05-002` carried one at-rest yard area as a single supporting
image and that was defensible; here plant is the whole subject, so at-rest is forbidden and **every
caption in this batch names the work, the operator or the site.** The checker reads the captions and
tests both halves — nothing at rest, and everything naming the work.

## The Four Access Tiers

The organising fact a client needs first and no fleet list gives them: **what can physically get in.**

| Tier | Means |
| --- | --- |
| Through a domestic gate | A back garden, a side return, an occupied terrace |
| Through a site gate | Ordinary access, a hardstanding, a compound |
| Delivered on a low-loader | It does not drive itself in, and the standing is the harder half |
| **Needs a road closure or a crane** | **Not us.** A specialist, a permit and a programme of its own |

`003` is built entirely on this ladder and **draws the gate rather than dimensioning it** — two posts
and the gap between them, widening tier by tier, built from elements. The fourth tier's posts are
drawn broken, because there is no gate: that job goes elsewhere.

Drawing the opening rather than measuring it is also how the study states the access fact without
asserting a measurement, which the section's own rule forbids.

## Study Records

| Study | Ground | Model | Media | The move |
| --- | --- | --- | --- | --- |
| `001` | `#efeeea` | Six site conditions as cards, condition first | 2 bands | The condition before the machine, in the order the question arrives |
| `002` | `#faf7f1` | A broadsheet — genuine two-column text | 1 plate | **Real columns**, which cannot be read as a grid of objects |
| `003` | `#e3e6e3` | Four access tiers, each headed by a drawn gate | 1 band | **The gate, drawn rather than dimensioned** |
| `004` | `#0f1b1a` | Three photographs to send, and what each answers | 1 band | **Send us a photograph of your gate** |
| `005` | `#211d18` | Photo-essay register, sides alternating | 4 areas | **The largest words are the site's problem** |

### `002`, where the form does the refusing

Every editorial study in this sector so far has been a single measure, a margin against a body, or
two independent tracks. This one is **one text flowing through two columns** — the setting a reader
associates with an argument rather than a catalogue.

That is not decoration. A fleet page wants to become a grid of objects, and continuous columned prose
**cannot be read as a grid of objects**, so the form refuses the section's trap before any of the
copy has to.

### `004`, the conversion a plant page can honestly make

The access question is the only thing here that can be answered truthfully before anybody visits, and
it is the question that stops jobs before they start. So: **send three photographs** — the way in,
where a machine would have to stand, and the route out — each with what it answers.

Two things keep it honest. The answer that comes back is **a tier rather than a measurement**, for
the same reason the gates are drawn rather than dimensioned. And the panel states what a photograph
cannot settle: *"What is under the ground. No picture settles that, and we will not pretend one
did."*

It is deliberately not `S06-004`, which converts on the site walk and costs a morning. This costs the
walk to the gate.

### `005`, the register the direction asked for

The sector direction names this variant as the plant register and names its trap in the same line.
The study takes the imagery and inverts the typography: **the site condition at the size a machine
name usually gets, and the machine at the size a caption usually gets.** A page can be image-led and
still refuse to be a catalogue, and that is the whole demonstration.

## Compliance

- Structural validation: **PASS.** All five parse; tag nesting verified on a stack for every study.
- Metadata validation: **PASS.** Fourteen research fields plus viewport on all five; `study-id`
  matches filename; territories match the core set in order.
- Isolation: **PASS.** No `<script>`, `<iframe>`, inline `style`, remote reference, embedded image,
  inline SVG or form control anywhere in the batch.
- Responsive QA: **PASS.** Verified at 1440px; each study states its ladder. `002`'s columns collapse
  to one before the measure gets uncomfortable.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.** No malformed hex, no accidental 8-digit hex, no `clamp()` arity
  error, no viewport-height unit.
- Section-shell check: **PASS.** No header, nav or footer; no `<h1>`; every study labelled by its own
  `h2` through `aria-labelledby`.
- Scoped-CSS check: **PASS.**
- **Media check: PASS.** Nine reserved plant areas across the batch; none captioned for a machine at
  rest; every one naming the work, the operator or the site.
- **Organisation check: PASS.** Every study addresses at least three site conditions; four of the
  five address five or six.
- **Manufacturer check: PASS.** No make or model named in any study.
- **Reserved-count check: PASS.** Machines, units, ticketed operators and fitters reserved in all
  five; every field labelled for a screen reader.
- **Steer-away check: PASS.** The road-closure tier kept in all five.
- **Specification check: PASS**, on the page with its declared refusal removed. No tonnage, weight,
  reach, capacity, hours run, fleet value, utilisation or emissions rating outside the block that
  names them in order to refuse them.
- **Markdown-artefact check: PASS.** Carried forward from `S09`.
- Ground check: **PASS.** Five distinct grounds, none used by `S01`–`S09`.
- Render check: **PASS, no corrections.**

## Corrections Before Render

Two, both caught by the checker rather than by eye:

| Study | Was | Now |
| --- | --- | --- |
| `005` | **The steer-away was missing entirely.** Four register entries and no mention anywhere of the work that goes to a specialist — the only study in ten batches to drop the sector's standing admission | The road-closure line restored to the foot |
| — | The organisation rule counted class names, so it failed `002` (continuous prose) and `004` (built around three photographs), both of which are organised by site condition throughout | Re-keyed to the content: six site conditions, matched in the visible copy |

The second is the third recurrence of one lesson, first recorded in `CON-S02`:

    A check written against a class name is a check against a decision that has not been
    made yet.

It fails specifically on the studies that differ most from the first one written, which is exactly
the set a diversity catalog most needs to let through.

## Notes

- Tenth authored batch in the `CON` sector. `S01`–`S10` are complete.
- **The reusable outcome is that a product page becomes useful when it is indexed by the buyer's
  constraint rather than the object's attributes.** Plant here, but the same inversion is available
  anywhere a page defaults to a catalogue — vehicles, machinery, software tiers, materials, venues.
  The attributes stay on the page; they stop being the index.
- The second outcome is `002`'s: **the form can carry the refusal.** Where a section has a strong
  default shape it is worth asking which layout is structurally incapable of that shape, and using
  it. Continuous multi-column prose cannot be a product grid, so choosing it settled the argument
  before the copy arrived.
- The third is the caption rule. `S10` is the first section where **a media caption became a
  checkable content decision** rather than a label: *at rest* versus *in use* is the entire
  difference between an advertisement and evidence, and it costs nothing to enforce.
- `S11 Leadership Team` is next, and the sector direction has already ruled on it: anti-pattern
  thirteen forbids the wall of stock portraits, and `S11` follows the `WELL-S04` rule — **role
  leads, identity reserved.**
