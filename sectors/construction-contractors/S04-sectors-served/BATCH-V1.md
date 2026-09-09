# BATCH V1

## Batch Identity

- Sector: `Construction & Contractors`
- Prefix: `CON`
- Section ID: `CON-S04`
- Section Name: `Sectors Served`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `CON-S04-001` | Universal / Safe | AUTHORED | `raw/CON-S04-001.html` |
| `CON-S04-002` | Premium / Editorial | AUTHORED | `raw/CON-S04-002.html` |
| `CON-S04-003` | Structured / Visual Modular | AUTHORED | `raw/CON-S04-003.html` |
| `CON-S04-004` | Conversion-led | AUTHORED | `raw/CON-S04-004.html` |
| `CON-S04-005` | Art-directed / Distinctive | AUTHORED | `raw/CON-S04-005.html` |

Fourth batch in the `CON` sector. Governed by `../CONSTRUCTION-DESIGN-DIRECTION.md`; role and
boundaries in `./README.md`.

## Authoring Direction

No reference images were supplied for this section. All five studies were originated.

## The Governing Constraint — Naming a Sector Is Not a Claim

Every contractor in the country prints the same six words: healthcare, education, industrial,
retail, civic, residential. The list is free to write, so it persuades nobody, and the usual
attempts to make it persuade are all ruled out by the sector direction — the count of schools
built, the share of turnover by sector, the client logos, the framework names.

What survives is the only part of a sector that a contractor can be right or wrong about:

    Naming a sector is not a claim. Describing what that sector does to a programme is.

So each sector on the page carries a **constraint** — the thing about that sector which changes how
the job has to be run — and then what this firm does about it. That sentence is checkable on site,
which is precisely why competitors do not print it.

| Element | Treatment |
| --- | --- |
| Sector name | **Real** — generic vocabulary, free to write |
| The constraint | **Real, and load-bearing** — the section's whole content |
| What we do about it | **Real** — a stated operating decision, not an adjective |
| Services usually needed | **Real** — carried through from `S02` unchanged |
| Projects completed per sector, share of turnover | **Omitted** |
| Client names, logos, frameworks, authorities | **Omitted** |
| Certifications, awards, ratings, prices, durations | **Omitted** |
| Project photography | **Reserved, and deliberately secondary** — see below |

### The six constraints

| Sector | The constraint | What follows from it |
| --- | --- | --- |
| Healthcare | The building does not close while you work in it | Phasing priced first; site manager in the estates meeting |
| Education | Term starts whether you are finished or not | Programme written backwards from the first day of teaching |
| Industrial | The ground decides before anybody draws an elevation | Groundworks self-delivered rather than sublet |
| Retail | The floor is trading while the work happens | Work written in shifts; landlord and client on one programme |
| Civic | Half the permissions belong to somebody not in the room | Hoardings and closures designed at tender; late permission assumed |
| Residential | The neighbours did not choose to live next to a site | A named, reachable person on site; complaints answered, not filed |

## The Test That Separates This Section From `S03`

`S03 Projects` had to fail one test and `S04` had to pass it:

    Remove the images. Is there still an argument on the page?

In `S03` the answer had to be **no** — a project index is looked at, not read, and the picture was
the point. In `S04` the answer has to be **yes**, because a sector is an argument and not a
photograph. So this batch is carried by **colour and type instead of media**:

- **Three of the five studies carry no reserved media at all** — `001`, `003`, `005`.
- The two that do carry **one area each**, both placed as support rather than as the subject.
- A six-colour sector system does the identifying work photography would otherwise do:
  `--health`, `--edu`, `--industrial`, `--retail`, `--civic`, `--resi`, restated per study at the
  saturation its ground needs (deep on light paper in `001`–`004`, lifted on the dark ground in
  `005`).

This is the deliberate inverse of the `S02` correction, and it is not a retreat from it. `S02` was
too text-heavy **because it had abandoned photography that the section genuinely had**. `S04` has no
such asset — there is no photograph of a sector — so the visual interest is built from colour
field, scale and hierarchy instead. Every study still reads as a designed page rather than a
document.

## Study Records

| Study | Ground | Model | Media | The move |
| --- | --- | --- | --- | --- |
| `001` | `#f0efe9` | Six split cards, saturated colour half beside a light constraint half | none | The sector name sits **inside** the colour field, so the field is the label |
| `002` | `#faf8f3` | Serif proposition, four spaced passages, marginal names and coloured rules | one 21:9 plate | Four sectors given room rather than six squeezed — read as prose |
| `003` | `#e7e4e0` | Six modules with an 8px colour spine, the same three questions each | none | **Consistency makes modules comparable**, which is the only reason to show six at once |
| `004` | `#14243a` | One opened sector panel beside five tall colour columns as links | one 4:3 area | **"Which of these are you?"** — find your own constraint and act from inside it |
| `005` | `#2b2118` | Inverted hierarchy on deep brown | none | The **constraint** at display scale; the sector name reduced to a coloured dot |

### `005`, the inversion

Every sectors page in this industry sets the sector name large and the explanation small. `005`
does the opposite, and the reason is the governing constraint stated as a layout decision: the
sector name is the part every competitor also prints, and the constraint is the part they cannot.
Setting *"The building does not close while you work in it."* at display scale and *Healthcare* at
caption scale makes the argument entirely through type hierarchy, with no copy required to explain
it.

### `004`, and the control that is not a control

The five unopened sectors are **links, not a toggle**. A control that appears to switch panels and
does not is the `CON-S01-005` slide-counter failure, and this batch does not repeat it. The opened
panel carries the constraint, the action and the steer-away together, because the conversion device
here is *recognition* — a visitor who finds their own sector should be able to act without
scrolling back to a form.

## The Steer-Away Is Kept

`001`, `004` and `005` each name the sector this firm is **wrong** for — anything with a live
process running through it: clean areas, data halls, food production. A sectors page that lists only
sectors served is a claim of universal competence, which nobody in this industry believes. Naming
the exclusion is what makes the other six sentences credible, and it costs nothing that was ever
going to convert.

`003` makes the same move against the missing counter instead: *"How many schools we have built
tells you how busy we have been, not whether we understood the gate on yours — and the second
question is the one you are actually asking."*

## Compliance

- Structural validation: **PASS.** All five parse; tag nesting verified on a stack for every study.
- Metadata validation: **PASS.** Fourteen research fields plus viewport on all five; `study-id`
  matches filename; territories match the core set in order.
- Isolation: **PASS.** No `<script>`, `<iframe>`, inline `style`, remote reference or embedded
  image anywhere in the batch.
- Responsive QA: **PASS.** Verified at 1440px; each study states its ladder.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.** No malformed hex, no accidental 8-digit hex, no `clamp()` arity
  error, no viewport-height unit.
- Section-shell check: **PASS.** No header, nav or footer; no `<h1>`; every study labelled by its
  own `h2` through `aria-labelledby`.
- Scoped-CSS check: **PASS.**
- **Fabricated-proof check: PASS.** No digit in visible copy anywhere in the batch; no per-sector
  count or percentage, no client name, logo, framework or authority, no certification, award,
  rating, review, price, duration or urgency device.
- **Constraint check: PASS.** Every named sector states a constraint; six sector entries per study
  except `002`, which carries four by editorial decision.
- **Media-secondary check: PASS.** Two reserved areas in the batch, in two different studies;
  three studies carry none.
- **Soft check, twenty-three occurrences, all verified in context:** every *programme*,
  *permissions*, *specialists* and *wrong firm* sits inside a constraint statement or a steer-away,
  never a competence claim.
- Render check: **PASS, two corrections.**

## Corrections at Render

| Study | Was | Now |
| --- | --- | --- |
| `002` | Shell at `1240px` against a `56ch` measure, leaving a dead right third across the whole page | Shell pulled to `1080px`, sector name up to `clamp(1.24rem, 1.75vw, 1.6rem)`, rule thickened to `7px` |
| `005` | Standfirst `h2` on a `20ch` measure, breaking to four lines | `30ch` |

Both are the same failure the batch documents keep recording in a different form: **a measure set
without reference to the container it sits in.** `002` is the container-too-wide case and `005` the
measure-too-narrow one.

## Notes

- Fourth authored batch in the `CON` sector. `S01`–`S04` are complete.
- **The reusable outcome is that a category list becomes content when each category names its own
  constraint.** Any sector whose "who we serve" section is a list of free-to-write words — legal,
  accountancy, logistics, insurance, industrial supply — can convert that list into an argument by
  the same move, and the argument survives with no photography at all.
- The second outcome is the pairing with `S03`. Two adjacent sections, one carried entirely by
  images with its text reserved and one carried entirely by text with its images secondary, is a
  better rhythm than two image grids — and it fell out of asking what each section can actually
  claim rather than what it usually looks like.
- Checker lesson, and the second time in two sections: the rule counted `<h3>` and so counted `001`
  and `005`'s steer-away heading as a sector, and counted `004`'s five routed sectors as none.
  Keying the count off the **sector colour marker** rather than the heading tag fixed both.
  *A structural check should key off the thing the design actually varies, not the tag that happens
  to carry it in the first study written.*
- `S05 Capabilities` is next in this sector.
