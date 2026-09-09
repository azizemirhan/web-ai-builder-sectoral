# BATCH V1

## Batch Identity

- Sector: `Beauty, Wellness & Spa`
- Prefix: `WELL`
- Section ID: `WELL-S22`
- Section Name: `Breadcrumb / Context Navigation`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Authoring Direction | Status | Raw File |
| --- | --- | --- | --- |
| `WELL-S22-001` | Universal / Safe | AUTHORED | `raw/WELL-S22-001.html` |
| `WELL-S22-002` | Premium / Editorial | AUTHORED | `raw/WELL-S22-002.html` |
| `WELL-S22-003` | Dense / Information-heavy | AUTHORED | `raw/WELL-S22-003.html` |
| `WELL-S22-004` | Conversion-led | AUTHORED | `raw/WELL-S22-004.html` |
| `WELL-S22-005` | Sector-native / Distinctive | AUTHORED | `raw/WELL-S22-005.html` |

Second batch in the extended architecture set, using its directions rather than the `S01`–`S20` set.
The section's role, its governing constraints and its boundary with `S21` are in `./README.md`.

## Authoring Direction

No reference images were supplied. All five studies were originated.

## The Section-Shell Rule, Read For This Section

Every other `WELL` section is authored under a flat prohibition on `<header>`, `<nav>` and
`<footer>`. **`S22` is the one section where `<nav>` is required rather than forbidden**, because
the role *is* a navigation region and a breadcrumb without a landmark is decoration. `<header>`,
`<footer>`, a logo, a search field and a primary menu remain forbidden, and are scanned for.

This is worth recording as a catalog rule rather than an exception: **the section-shell prohibition
is about global site chrome, not about the elements themselves.** A section whose role is navigation
uses navigation markup.

## The Governing Constraint — Two Rules

**1. It must be navigation, not a picture of navigation.** The scaffold rules out *"decorative text
that only looks like a breadcrumb"*, and every part of that is mechanical:

| Requirement | Verified |
| --- | --- |
| `<nav>` landmark with an accessible name | Every nav in the batch has a unique `aria-label` |
| Ordered list | `<ol>` in all five |
| Real links for every level except the current | Two to five links per study |
| `aria-current="page"` on the current level | Present in all five; the current level is never also a link |
| Separators hidden from assistive technology | Every `.sep` and `.say` span carries `aria-hidden="true"` |

**2. It must not collapse into five cosmetic variants.** This is the section most at risk of that in
the whole catalog — the role is one line of text, and the obvious way to make five studies is five
separator characters. The scaffold forbids it, so **each study takes a different content
responsibility from the In Scope list:**

| Study | What it carries | What that adds |
| --- | --- | --- |
| `001` | The trail alone | Establishes the role |
| `002` | The trail as a stacked context block | Answers what happens when the last level cannot be written |
| `003` | The trail **plus siblings** | Answers *what else is at this level* |
| `004` | The trail **plus a return to the set** | Answers *how do I get back to the rest* |
| `005` | The trail **as a sentence** | Answers *what does this role sound like in this sector* |

And each takes a **different one of the three responsive strategies** the scaffold permits, so the
batch answers the narrow-width question five ways rather than once: wrap, already-vertical, scroll
with a visible edge, wrap-with-promoted-return, and reflowing prose. **No study hides or truncates
the trail**, which the scaffold rules out; verified by scanning the media queries for a
`display: none` on any trail element.

## What Is Real Here — Unusually, Almost Everything

This is the first section in the sector where almost nothing has to be reserved. A trail is made of
page names, and this sector's page names are vocabulary already established in `S02` and `S03`:
*Treatments*, *Facials*, *Body & massage*, *Hands & feet*, *Brows & lashes*, *Deep cleansing facial*.
*Home* is a universal label rather than invented content. A checker validates every crumb against
that closed list, so a stray invented category cannot enter unnoticed.

**The one exception is `002`.** It sits on an article page, where the last crumb is the article
title — invented content on the `S18` rule — so the current level is a reserved area. The trail
still works, because **every level a visitor can actually use is a level that already exists.** A
breadcrumb degrades gracefully when its final level is unwritten, in a way a headline does not.

**Not present in any study:** a primary site menu, a search field, a sign-in, a basket, a sitemap;
an item count beside a category — *"Facials (12)"* is an invented figure; a price, rating, review
count or duration; an invented page name outside the established vocabulary; a level that is not a
link; a separator announced to screen readers. Verified by scan — **no digit appears in visible copy
anywhere in the batch.**

## Study Records

### WELL-S22-001 — Universal / Safe

- **Layout model:** Four levels on one line above a hairline, current page marked and not a link.
- **The variant that establishes the role** before the others add to it: no siblings, no return, no
  context line.
- **Responsive strategy:** wraps to a second line. Never truncated, never hidden.

### WELL-S22-002 — Premium / Editorial

- **Layout model:** The trail set vertically as a stepped context block against a left rule — the
  credit block of a printed programme rather than a chain.
- **The batch's sharpest content point:** on an article page the last crumb cannot be written, so it
  is a reserved area. Recorded because it shows the difference between a trail and a headline —
  a trail with an unwritten final level is still fully usable.
- **A second-order benefit of the vertical set:** the step-in is drawn with padding rather than with
  characters, so **there is no separator to hide from a screen reader at all.** The most accessible
  breadcrumb in the batch is the one that stopped using punctuation.
- **Responsive strategy:** already vertical; nothing to do.

### WELL-S22-003 — Dense / Information-heavy

- **Layout model:** The trail on the first line, the sibling category set on the second, as two
  separately named navigation landmarks.
- **Why siblings are the right density for this role:** they answer *what else is at this level*,
  which a trail alone cannot. Adding more crumbs would have made the study longer, not denser.
- **The current sibling is marked `aria-current="page"` and rendered as text, not a link** — the set
  says where you already are rather than offering to take you there.
- **Responsive strategy:** the trail **scrolls horizontally with a visible edge rule** rather than
  wrapping, because a wrapping trail above a wrapping sibling row produces four ragged lines. Second
  of the three permitted strategies.
- **No count beside any category.** A sibling set is exactly where *"Facials (12)"* would normally
  appear, and that is an invented figure.

### WELL-S22-004 — Conversion-led

- **Layout model:** A promoted return to the parent set as a real control on the left, the full
  trail small beside it, and one line saying why it is there.
- **What conversion means for a breadcrumb:** not urgency — there is nothing here to hurry. The
  commercially useful thing this role does is **give the way back to the set** to somebody who
  landed deep from a search engine and has never seen the category page. For them the trail is not
  orientation, it is the only route to the rest of the catalogue.
- **The full trail is kept beside the promoted control**, because promoting one level is not a
  reason to hide the others.
- **The honest line is an observation, not a claim:** *"Most people reach a page like this from a
  search rather than from our menu."* It is about how sites are used, so it needs no figure behind
  it and carries none.

### WELL-S22-005 — Sector-native / Distinctive

- **Layout model:** The trail written as a sentence on a soft sage band.
- **Why this is sector-native:** a chevron chain is interface grammar borrowed from software, and in
  a register built on calm it reads as machinery. Saying where somebody is in the words a
  receptionist would use is the version of this role that belongs to **this** sector.
- **The device, and the interesting part:** the markup is still an ordered list of levels, root
  first. The connective words — *Under*, *inside*, *you are looking at the* — are separate spans
  marked `aria-hidden`, **so a screen reader hears a clean three-level trail while a sighted reader
  gets a sentence. Neither audience is served the other one's version.** A paragraph with links in
  it would have looked identical and lost the list semantics entirely.
- **Correction made, recorded:** with `li { display: inline }`, the newline between list items
  renders as a space, so punctuation placed at the *start* of each item produced *"Treatments ,
  inside"*. Moving each comma to the **end** of the preceding item puts the stray space where a
  space belongs. **Any inline list assembled into prose has this bug; the fix is punctuation-last.**
- **Responsive strategy:** it is prose, so it reflows.

## Structural Diversity

| Study | Shape | Levels | Extra content | Responsive strategy | Ground |
| --- | --- | --- | --- | --- | --- |
| 001 | One horizontal line | 4 | — | Wraps | Warm pale grey `#f1f0ec` |
| 002 | Vertical stepped block | 4, last reserved | — | Already vertical | Pale lilac `#f4f1f6` |
| 003 | Line + sibling row | 3 | 4 siblings | Scrolls with a visible edge | Cool pale grey `#e7eaed` |
| 004 | Promoted return + small trail | 4 | Return control, one line | Wraps, return full width | Deep pine `#233028` |
| 005 | A sentence | 3 | — | Reflows | Soft sage `#c6cdc4` |

Grounds do not repeat any used in `WELL-S01`–`S21`; verified by scan across all 110 studies.

## Research Metadata

- **Sources:** none supplied; all five studies originated.
- **Research date:** 2026-09-02.
- **Visual-first check:** no study derives its distinctiveness from copy or from a separator
  character. The differentiator is what each one is *responsible for* — the trail, the trail with an
  unwritable end, the trail plus siblings, the trail plus a return, the trail as language.
- **Document-metaphor justification:** `NONE`.

## Dependency Check

- Framework: NONE · CDN: NONE · Remote runtime dependency: NONE
- JavaScript necessity: **NONE.** `003`'s sibling set is a plain link list, which is what the
  scaffold requires any local navigation to degrade to. No `<script>`, `<iframe>`, form element or
  inline `style`.

## Media Slots

| Slot | Purpose | Expected Type | Accessibility / Fallback |
| --- | --- | --- | --- |
| Article title | `002` — the current level on an article page | **Text** | Reserved area carrying the field name |

One reserved element in the whole batch, and no media anywhere: the scaffold is explicit that this
role is navigation, not presentation.

## QA

- ID validation: **PASS.** All five IDs exist and match their filenames.
- Raw-format validation: **PASS.** Standalone HTML, `lang` set, 14 research `<meta>` fields plus
  viewport. Nesting validated with a stack-based parser.
- Territory validation: **PASS.** All five match the extended-architecture set.
- **Navigation-semantics check: PASS — this batch's defining check.** Every study: a `<nav>` with a
  unique accessible name, an `<ol>`, real links, `aria-current="page"` on a current level that is
  never itself a link, and every separator or connective `aria-hidden`.
- **Section-shell check, read for S22: PASS.** No `<header>` or `<footer>`; `<nav>` present and
  named in all five; no logo, search field or primary menu.
- Accessibility QA: **PASS.** Exactly one `<h1>` per study, visually hidden, naming the region —
  and **not carrying the `hidden` attribute**, which would remove it from the accessibility tree and
  break the `aria-labelledby` that points at it. That check exists because the first build of `001`
  did exactly that.
- Responsive QA: **PASS.** Three different permitted strategies across five studies; verified that
  no media query hides a trail element.
- Dependency validation: **PASS.**
- CSS-validity scan: **PASS.** No malformed hex, no accidental 8-digit hex, no `clamp()` with the
  wrong arity, no viewport-height unit.
- Scoped-CSS check: **PASS.**
- **Vocabulary check: PASS.** Every crumb in every study validates against the closed list of names
  established in `S02` and `S03`, plus *Home* and the reserved *Article title*.
- **Figure and chrome check: PASS.** No digit in visible copy; no price, rating, review, duration,
  sign-in, basket or sitemap. Two soft occurrences of *search* and *menu* were printed with their
  surrounding sentence and confirmed to be `004`'s prose about how visitors arrive.
- Render check: **PASS, after one correction.** All five rendered in headless Chrome and inspected;
  `005`'s inline-list spacing was fixed as recorded above.

## Notes

- Twenty-second authored batch in the `WELL` sector, twentieth without references, second of the
  seven extended architecture roles.
- **The reusable outcome is how to make five studies of a one-line component.** Do not vary the
  styling; vary the *responsibility*. The scaffold's In Scope list for this role has five entries —
  trail, current position, back navigation, sibling navigation, context line — and taking a
  different combination in each study produced five structurally different sections from a component
  that is fundamentally one line of text. Any sector, and any small component, can use that method.
- The second outcome is `002`'s: **a breadcrumb whose last level cannot be written still works.**
  That is worth knowing for every sector whose detail pages carry unwritable titles — the trail is
  usable even when the page it names is not yet named.
- Two checker bugs were found and fixed while writing this batch, both of the same family as earlier
  ones: `[0-9.]+vh` matched the `.vh` utility class name, and a hard ban on *search* and *menu*
  punished a study for describing how visitors arrive. **Both were the checker being wrong about
  the studies, not the studies being wrong** — the second tier of the `S20` scan is what made the
  difference.
- `S23` is next: Treatment / Wellness Service Detail — the body of the page these last two batches
  have been opening.
- The review contact sheet at `review/index.html` still does not include any `WELL` or `AUTO` batch,
  because `python3` on this machine resolves to a Windows Store placeholder rather than an
  interpreter.
