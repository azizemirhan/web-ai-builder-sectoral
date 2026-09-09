# BATCH V1

## Batch Identity

- Sector: `Consulting & B2B Professional Services`
- Prefix: `CONS`
- Section ID: `CONS-S22`
- Section Name: `Breadcrumb / Context Navigation`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

Second of the extended architecture roles, twenty-second batch overall. Themes unchanged from `S01`.
The sector stands at **110 studies**.

## Planned Studies

| Study ID | Direction | Theme | Shape | Composition | Media | Words |
| --- | --- | --- | :---: | --- | ---: | ---: |
| `CONS-S22-001` | Universal / Safe | 001 Paper | **C** | A wrapping row of level pills, each carrying the count of what is up there | **0** | 53 |
| `CONS-S22-002` | Premium / Editorial | 002 Sable | **C** | **The trail runs down, not across** — a descending stack, each level stepped in from the last | **0** | 53 |
| `CONS-S22-003` | Dense / Information-heavy | 003 Field | **C** | Four joined level modules and a fifth sibling panel on the same seam — **up and across in one object** | **0** | 52 |
| `CONS-S22-004` | Conversion-led | 004 Signal | **C** | The trail complete but small, then **the way up promoted to the largest thing** | **0** | 48 |
| `CONS-S22-005` | Sector-native / Distinctive | 005 Midnight | **C** | **The count is the type and the name is the caption** — `All → 6 → 3 → 1` | **0** | 53 |

**All five are shape C with zero media, and that is not an authoring choice.** The section README
settles it: *Media Relationship — None. This role is navigation, not presentation.* Third all-C batch
in the sector after `S16` and `S20`, and the only one where the role mandated it.

## The Section Role

Show where the current page sits in the site hierarchy, and give the visitor a way back up or across.

## The Trap

**A breadcrumb that shows the URL instead of the site.** `Home / Services / Operating model redesign`
names three levels and describes none of them. Going up is therefore a gamble — the visitor cannot
tell whether *Services* holds four things or forty — so they use the back button, and the trail sits
on the page as an ornament shaped like navigation, which the README names directly as out of scope:
*decorative text that only looks like a breadcrumb.*

## The Governing Idea

> **Nobody climbs a breadcrumb, because no level tells you what is up there.**

So every level in every study **carries the count of what is up there**, and one legend line says so.
A trail that can be used is worth the row it occupies; one that cannot is a graphic of a hierarchy.

### Why this is the sector's answer and not a generic one

Consulting sites carry the deepest invented taxonomies on the web — *Insights / Research / Points of
view / 2024* — and the whole commercial function of that depth is to make a small number of offers
look like a large number of capabilities. **Printing the count per level cannot do that**: six
services, three of them operations, one of them this page. It is a claim the firm has to be able to
meet, which is why every study closes on the same commitment: **no level here is a folder we invented
to give the trail another rung.** It is `S10`'s move — a firm that shows the count instead of the
impression has given up the impression — applied to navigation.

## The Trail All Five Render

| Level | Count | Rendered as |
| --- | --- | --- |
| `Home` | — | Link |
| `Services` | `6` pages | Link |
| `Operations` | `3` pages | Link |
| `Operating model redesign` | this page | `<span aria-current="page">`, never a link |

Across, not up: the other two in `Operations` are `Cost structure` and `Post-merger integration`.

## The Boundary With S21

`CONS-S21`'s batch document recorded a sibling list drafted for `005` and cut, on the ground that a
sibling set is the page's **position in the site** and therefore belongs here. **That debt is paid in
this batch:** every study carries the sibling set as a second labelled landmark. `S21` states the
page's own limit in words and names one alternative; `S22` shows the position and names the rest.

## Semantics — the one section whose subject is not composition

The README is explicit: *this role is semantic navigation, not decoration.* Every study therefore:

- uses a real **`nav` landmark whose accessible name comes from the visible heading**, and a second
  labelled landmark for the sibling set, so *up* and *across* are distinguishable without sight;
- uses an **ordered list**, because the order is the meaning;
- marks the current page with **`aria-current="page"` on a `span`, never a link** — a scan confirms
  zero `<a aria-current>` and exactly one `aria-current` per study;
- **marks every state at least twice.** The current level is filled *and* weighted *and*
  `aria-current` in `001` and `003`; enlarged *and* darkened *and* `aria-current` in `002`; lit in
  accent *and* `aria-current` in `005`. A position communicated by fill alone locates nothing for a
  visitor who cannot see it;
- **draws separators in CSS**, so no chevron or arrow enters an accessible name or a copied selection;
- **hides nothing to fit.** `001` and `004` wrap, `002` is already one level per line at every width,
  `003` re-flows to two columns then one, `005` wraps and reduces the numeral. No study truncates,
  ellipsises or drops a level — a scan confirms zero `text-overflow: ellipsis` and zero
  `display: none` in the batch.

## The Five Compositions

- **`001`** — the trail as pills, the count as a chip inside each, the current one filled. The safest
  binding target in the section: an ordered `{label, href, count}` collection with the last flagged.
- **`002`** — a horizontal trail compresses four levels into one line and makes them look equivalent.
  **Set as a descending stack it draws the shape it describes** — the reader travels down into the
  page and the indent at the bottom is how far in they are. It also solves the responsive problem by
  construction: a vertical trail is already what the horizontal ones collapse *into* on a phone.
- **`003`** — every other treatment puts the trail on one row and the siblings on another, asking the
  reader to understand two components. Here they are one joined object with a `2px` seam, **because a
  sibling is not a separate kind of destination — it is the level above, entered one door along.**
- **`004`** — **converting by sending them up.** There is nothing to sell in a breadcrumb; what it can
  convert is a visitor about to leave into a visitor one level up. So the parent is the largest thing
  on the section and it says what is up there, with both siblings named inside it. The trade is that
  the section spends its whole surface on the one link leading away from the current page. **A page
  that cannot survive naming its own alternatives was not going to hold that reader anyway.**
- **`005`** — **the count is the type and the name is the caption.** The row reads *All to six to
  three to one* before a single name is taken in, so the shape of the trail is the shape of the
  narrowing, drawn rather than described.

## Placeholder Data

The level counts and the two sibling page names are demo values marked `data-placeholder="true"`. No
client name, logo, testimonial, percentage, currency figure, award or ranking appears anywhere.

## What This Section Will Not Do

- **No primary site navigation.** That is page chrome.
- **No footer navigation or sitemap listing.**
- **No page title or introduction.** That is `S21`, and no study repeats it.
- **No decorative text shaped like a breadcrumb** — every level here is a real destination with a real
  count behind it.
- **No JavaScript.** Links only.
- **No global header or footer.** The section-shell rule.

## Verification Record

- Word band `40–90` (breadcrumb): **53 / 53 / 52 / 48 / 53.** All five in band, headers synced.
- Tag balance: **0 unbalanced elements** in all five. No `<script>`, `<iframe>`, `<img>`, `<svg>`,
  `<form>`, `<table>` or monospace face anywhere.
- Semantics scan: **clean on every rule above** — two named landmarks per study, ordered trail, one
  `aria-current="page"` per study and never on a link, no dangling `aria-labelledby`, no truncation.
- Theme conformance: **110/110 studies in the sector** conform to the contract grounds and accents.
- Composition collisions: **no exact match.** `S22` contributes none of the 17 open near matches.
  `001`, `002` and `005` share the coarse block sequence `HERE > LEGEND > ACROSS > REAL`; they are
  different variants, so they never meet on an assembled page, and the composition that differs is the
  trail itself — a pill row, a descending stack and a display-numeral row are not the same object.
- Structure check: the same **3 intentional FAILs** as before this batch. `S22` adds none.

### Found before rendering

- `003` was written with its sibling `nav` outside the joined block, which contradicted its own
  *up and across in one object* claim and left `.cell h2 / ul / a` as dead CSS. Rebuilt as a fifth
  panel on the same seam, still outside the trail's `<ol>` so the trail's semantics stay clean.
- `002`'s header claimed it carried *the fewest words in the batch*; the count made that false once
  the studies were measured. Corrected rather than left standing.

### Found only by rendering

- `005` — the level names were set in `--ink-dim` (#4a505c on #0b0d12, roughly **2.6:1**), below AA.
  In the one section whose subject is accessibility semantics, those names are content, not ornament.
  Moved to `--ink-soft`; only the arrows, which are CSS and reach nobody, stay that faint.
- `001` — the chevrons were drawn in `--line` and effectively invisible, which left the pills reading
  as an unrelated row rather than a trail. Moved to `--ink-soft` at half opacity: visible as a
  sequence, still decorative.
