# Section ID

WELL-S22

# Section Name

Breadcrumb / Context Navigation

# Section Role

S22 — Breadcrumb / Context Navigation

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Purpose

Show where the current page sits in the site hierarchy, and give the visitor a way back up or across it.

# Visitor Intent

The visitor wants to know what this page is part of, and to move up a level or sideways without returning to the homepage.

# Content Responsibility

Hierarchy and local context: a breadcrumb trail, the current position within it, and optionally a local navigation set for sibling pages.

# In Scope

- A breadcrumb trail from a root to the current page
- A clear indication of the current page within that trail
- Optional contextual back navigation to the parent
- Optional local navigation across sibling pages or in-page anchors
- Optional short context line, such as the collection this page belongs to

# Out Of Scope

- Primary site navigation, which belongs to the page chrome
- Decorative text that only looks like a breadcrumb
- Page title and introduction, which belong to S21
- Footer navigation or sitemap listings

# The Section-Shell Rule, Read For This Section

Every other `WELL` section is authored under a flat prohibition: **no `<header>`, no `<nav>`, no
`<footer>`.** That rule exists to keep global site chrome out of section studies.

**`S22` is the one section where `<nav>` is required rather than forbidden**, because the role *is*
a navigation region. The prohibition is read as it was meant:

| Element | In `S22` |
| --- | --- |
| `<nav>` with an accessible name | **Required** — a breadcrumb without a landmark is decoration |
| `<header>`, `<footer>` | Still forbidden |
| Primary site navigation | Still forbidden — a trail is not a menu |
| A logo, an announcement bar, a search field | Still forbidden |

# The Governing Constraint — Two Rules

**1. It must be navigation, not a picture of navigation.** The scaffold rules out *"decorative text
that only looks like a breadcrumb"*, and the difference is mechanical:

| Requirement | Why |
| --- | --- |
| A `<nav>` landmark with an accessible name | So it can be found and skipped |
| An ordered list | A trail has an order, and the markup should say so |
| Real links for every level except the current one | A trail you cannot use is an illustration |
| `aria-current="page"` on the current level | The scaffold: *mark the current page programmatically rather than by styling alone* |
| Separators marked `aria-hidden` | A slash is not a word |

**2. It must not collapse into five cosmetic variants.** This is the section most at risk of it in
the whole catalog: the role is one line of text, and the obvious way to produce five studies is five
separator characters and five type scales. The scaffold forbids exactly that, so **each study takes
a different content responsibility from the In Scope list**:

| Study | What it carries |
| --- | --- |
| `001` | The trail alone |
| `002` | The trail as a stacked context block, on a page whose last level cannot be written |
| `003` | The trail **plus sibling navigation** |
| `004` | The trail **plus a return to the set** |
| `005` | The trail **as a sentence** |

# What Is Real Here — Unusually, Almost Everything

This is the first section in the sector where almost nothing has to be reserved. A trail is made of
page names, and this sector's page names are generic vocabulary already established in `S02` and
`S03`: *Treatments*, *Facials*, *Body & massage*, *Hands & feet*, *Brows & lashes*, *Deep cleansing
facial*. *Home* is a universal label rather than invented content.

**The one exception is the article page**, where the last crumb is the article's title — and an
article title is invented content on the `S18` rule. `002` is authored on that page deliberately,
so the batch records what a trail does when its final level cannot be written: **the crumb becomes
a reserved area, and the trail still works**, because every level a visitor can actually use is a
level that already exists.

**Not present in any study:** a primary site menu; a search field; an item count beside a category;
a price, rating or duration; an invented page name outside the vocabulary above; a trail whose
levels are not links; a separator that is announced to screen readers.

# Boundary With S21

| Section | What it owns |
| --- | --- |
| `S21` Subpage Hero | The **page identity** — its title and what it holds |
| `S22` Breadcrumb / Context Navigation | The **path to it**, and the way back up or across |

    S21 names the page. S22 shows the path to it.

`S21` was authored first and kept every trail-shaped element out on purpose, so this section
inherits a clean role. `S22` returns the favour: **no study here restates the page title as a
heading.** The current page appears once, as the last crumb.

# Media Relationship

None. This role is navigation, not presentation.

# Interaction Notes

Links only. Where local navigation is present it may scroll or filter within the page, but must degrade to plain links.

No study uses JavaScript. `003`'s sibling set is a plain link list.

# Responsive Considerations

A trail must never be silently truncated on small screens without a way to reach the hidden levels. Wrapping, scrolling with a visible affordance, or collapsing to the parent level are all acceptable; hiding the trail entirely is not.

**Each study takes a different one of those three strategies**, so the batch answers the
responsive question five ways rather than once:

| Study | Narrow-width strategy |
| --- | --- |
| `001` | Wraps to a second line |
| `002` | Already vertical; nothing to do |
| `003` | Scrolls horizontally with a visible edge affordance |
| `004` | Trail wraps; the parent return goes full width |
| `005` | It is prose, so it reflows |

# Related Sections

This role is semantic navigation, not decoration. Studies should use a real navigation landmark with an accessible name, mark the current page programmatically rather than by styling alone, and keep the trail keyboard reachable in a sensible order.

Sits directly above or below S21 on an internal page, and never replaces it.

# Planned Studies

WELL-S22-001
WELL-S22-002
WELL-S22-003
WELL-S22-004
WELL-S22-005

# Expected Structural Diversity

| Variant | Territory |
| --- | --- |
| `WELL-S22-001` | Universal / Safe |
| `WELL-S22-002` | Premium / Editorial |
| `WELL-S22-003` | Dense / Information-heavy |
| `WELL-S22-004` | Conversion-led |
| `WELL-S22-005` | Sector-native / Distinctive |

These are authoring and research directions, not production enums. The five studies must
differ structurally. They must not become five colour schemes, five font themes, five
cosmetic variants, or five copies of one grid with the content swapped.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
