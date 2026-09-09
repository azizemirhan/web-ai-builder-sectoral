# BATCH V1

## Batch Identity

- Sector: `Construction & Contractors`
- Prefix: `CON`
- Section ID: `CON-S14`
- Section Name: `Service Areas`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `CON-S14-001` | Universal / Safe | AUTHORED | `raw/CON-S14-001.html` |
| `CON-S14-002` | Premium / Editorial | AUTHORED | `raw/CON-S14-002.html` |
| `CON-S14-003` | Structured / Visual Modular | AUTHORED | `raw/CON-S14-003.html` |
| `CON-S14-004` | Conversion-led | AUTHORED | `raw/CON-S14-004.html` |
| `CON-S14-005` | Art-directed / Distinctive | AUTHORED | `raw/CON-S14-005.html` |

Fourteenth batch in the `CON` sector. Role and boundaries in `./README.md`.

## Authoring Direction

No reference images were supplied for this section. All five studies were originated.

## The Rule Was Set In Advance

Anti-pattern eleven: **the map of pins across a country, asserting coverage nobody verified.** The
direction sends this section to *named real regions or a reserved area*.

A pin map is forbidden for the same reason a logo wall is: **it asserts at a glance something
nothing on the page supports.** Twelve pins say *we work here*; they do not say whether anybody from
the firm has been to eleven of those places this year.

## The Governing Constraint — A Service Area Is Not A Circle

    A service area is the distance a site manager can cover and still be on your site
    every morning. It is not a radius, and it is not a county.

So an area is described by **what you lose the further out you are** — and the four bands run:

| Band | What changes |
| --- | --- |
| Around the yard | Every morning, our plant, our fitter the same day. Travel not priced — it is where we work |
| The next ring out | Still every morning. Plant hired locally beyond a point, and **the fitter is a drive rather than a visit** |
| Further than that | **Most mornings, not every morning.** A hire desk rather than our fitter |
| Beyond that | **We do not bid**, and we name a firm nearer you |

## The Constraint Produced The Better Answer

A distance is a figure and a drive time is a duration, and this sector omits both — the `S06` rule
and the counter rule between them. That looked like a problem and was not:

    The figure this section cannot print is the one that would have told you least.

**Miles never described a service area.** Fifty on a motorway and fifty across a city are different
jobs, and neither says whether somebody will be standing on a site at seven in the morning.
Attendance does. The catalog's own restriction pushed the section onto the honest measure.

## The Admission

> **We will travel further than this for the right job, and we are worse at it.**

A firm claiming to cover a whole country is either very large or not telling the truth, and the ones
in the middle simply cost a client more in travel and less in attendance. Present in all five, and
in `003` and `005` the outermost band is the loudest thing on the page.

## Study Records

| Study | Ground | Model | Map | The move |
| --- | --- | --- | --- | --- |
| `001` | `#f0eeeb` | Four bands as cards, ordered outward | reserved | Each band states what you lose |
| `002` | `#f8f5ee` | The reserved map beside the argument against it | reserved, large | **The artefact and the argument, side by side** |
| `003` | `#dde0dd` | A degradation ladder, stepped outward | reserved, smallest thing on the page | **The loss block grows** |
| `004` | `#151d1a` | One ask, three possible answers | reserved | **Do not ask whether we cover you** |
| `005` | `#f2efe7` | Four bands darkening outward | **none at all** | **The page darkens as the attendance falls** |

### `002`, arguing with the artefact

The map is reserved at the size a finished page would give it, and the column beside it explains why
it will tell a reader less than the paragraph they are reading. Putting the two in the same eyeline
is the whole study, and it is the only editorial study in this catalog where **the reserved area is
the subject of the argument** rather than support for it.

### `003`, the loss block grows

Band one's *what you lose* is a thin line saying nothing; band four's fills the row. Each band is
also indented one step further and carries fewer modules than the last, because there is less to
promise. A reader who takes nothing else takes the shape, which is the argument: **a service area
does not end at a line, it degrades.**

Its map is present, reserved, and deliberately the smallest thing on the page.

### `004`, and a fourth arrival

> **Do not ask whether we cover you.** Ask which band you are in and what it costs you.

*Do you cover us* is a yes-or-no question with only one answer a contractor ever gives. Replacing it
with a band and a consequence makes the enquiry capable of coming back negative — and the third
answer is *a firm nearer you would serve you better, and here is one.*

That is **the fourth section in this sector to convert by handing over the less flattering result**,
after `S09`, `S12` and `S13`, and the only one where the outcome is losing the enquiry outright.

### `005`, the gradient

Distance from the yard is drawn as descent and as light: band one is nearly the paper colour, band
four nearly black, and the loss sentence grows through the four until it is the largest type on the
page. **It is the only study in the batch that reserves no map at all** — at that scale even an
empty map would become the subject, and the subject is attendance rather than territory.

## Compliance

- Structural validation: **PASS.** All five parse; tag nesting verified on a stack for every study.
- Metadata validation: **PASS.** Fourteen research fields plus viewport on all five; `study-id`
  matches filename; territories match the core set in order.
- Isolation: **PASS.** No `<script>`, `<iframe>`, inline `style`, remote reference, embedded image,
  inline SVG or form control anywhere in the batch.
- Responsive QA: **PASS.** Verified at 1440px; each study states its ladder. `003`'s step unwinds
  first, being decoration rather than structure.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS**, after two corrections — see below. No malformed hex, no non-ASCII
  character in any stylesheet, no accidental 8-digit hex, no `clamp()` arity error, no
  viewport-height unit.
- Section-shell check: **PASS.** No header, nav or footer; no `<h1>`; every study labelled by its own
  `h2` through `aria-labelledby`.
- Scoped-CSS check: **PASS.**
- **Band check: PASS.** All four bands present in all five studies.
- **Loss check: PASS.** Seven distinct losses stated in every study.
- **Measure check: PASS.** Attendance is the measure in all five — *every morning* and *most
  mornings, not every morning* both present.
- **Refusal check: PASS.** The outermost band declines and redirects in all five; the
  *we are worse at it* admission present in all five.
- **Map check: PASS.** No drawn map, pin or marker element anywhere. Where a map appears it is a
  reserved area whose caption says so; `005` carries none.
- **Reserved-region check: PASS.** Region names and the yard location reserved; every field labelled
  for a screen reader.
- **Coverage-claim check: PASS**, on the page with its declared refusal removed. No *nationwide*, no
  radius, no mileage, no drive time, no depot or office count outside the blocks that name them in
  order to refuse them.
- **Markdown-artefact check: PASS.**
- Ground check: **PASS.** Five distinct grounds, none used by `S01`–`S13`.
- Render check: **PASS, no corrections.**

## Corrections Before Render

| Study | Was | Now |
| --- | --- | --- |
| `003` | **Two corrupted values in the palette** — one hex containing a non-ASCII digit, another containing a space. Both would have silently dropped the declaration and left the ink colour to inherit | Repaired, and the checker tightened |

That one is worth the note. The existing hex rule matched `#[^\s;,)}]+`, which **cannot see a hex
with a space in it** — the space terminated the match — and treated a non-ASCII digit as an ordinary
character. Two new checks now run on every stylesheet in this section: a stricter hex scan, and
**no non-ASCII character anywhere in the CSS at all.**

A colour that silently fails is the worst class of defect in this catalog: it does not throw, it
does not look broken in a thumbnail, and it changes what the page says by changing what a reader can
read.

## Checker Note

The loss rule failed `002` and `004` on the first run because it looked for the label *what you
lose*, which `002` states in prose and `004` in an element of its own. Re-keyed to the seven losses
themselves.

**Seventh occurrence.** A rule keyed to a label or a class has now failed the most-differentiated
study in seven of fourteen sections in this sector, and never once caught a real defect while doing
so. It should be treated as the default failure mode when writing these checks, not as a surprise.

## Notes

- Fourteenth authored batch in the `CON` sector. `S01`–`S14` are complete.
- **The reusable outcome is that coverage should be described by what degrades, not by where a line
  is.** Every sector with a service-area page draws a shape and implies uniformity inside it. Naming
  the bands and what is lost at each is more useful to a reader, harder to fake, and produces a page
  that can say *not us* — which a map structurally cannot.
- The second outcome is the one this section stumbled into: **the figure the catalog could not print
  was the one that told the reader least.** Miles and drive times were unavailable, and the honest
  measure — attendance — was better. That is now the third or fourth time a restriction in this
  sector has produced a stronger page rather than a compromised one.
- The third is `005`'s: **a gradient is an honest picture where an outline is not.** It shows
  degradation rather than a boundary, which is what a service area actually is.
- `S15 Bid RFQ` is next, and several sections have already fenced it: it owns the formal
  submission and money, `S05-004` holds this sector's only form, and `S06`'s gates decide what is
  fixed at the point a bid is accepted.
