# Section ID

CONS-S22

# Section Name

Breadcrumb / Context Navigation

# Section Role

S22 — Breadcrumb / Context Navigation

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Consulting & B2B Professional Services

# Prefix

CONS

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

# Planned Studies

CONS-S22-001
CONS-S22-002
CONS-S22-003
CONS-S22-004
CONS-S22-005

# Expected Structural Diversity

| Variant | Direction | Theme | Shape | Composition | Media |
| --- | --- | --- | :---: | --- | ---: |
| `CONS-S22-001` | Universal / Safe | 001 Paper | C | A wrapping row of level pills, each carrying the count of what is up there | 0 |
| `CONS-S22-002` | Premium / Editorial | 002 Sable | C | The trail runs down, not across — a descending stack, each level stepped in | 0 |
| `CONS-S22-003` | Dense / Information-heavy | 003 Field | C | Four joined level modules and a fifth sibling panel on the same seam | 0 |
| `CONS-S22-004` | Conversion-led | 004 Signal | C | The trail complete but small, the way up promoted to the largest thing | 0 |
| `CONS-S22-005` | Sector-native / Distinctive | 005 Midnight | C | The count is the type and the name is the caption — `All → 6 → 3 → 1` | 0 |

All five carry no media, and that is not an authoring choice — the Media Relationship below settles
it. Third all-C batch in the sector after `S16` and `S20`, and the only one the role mandated.

# The Governing Idea

> **Nobody climbs a breadcrumb, because no level tells you what is up there.**

`Home / Services / Operating model redesign` names three levels and describes none of them, so going
up is a gamble and the trail becomes the decoration this README puts out of scope. Every level here
carries **the count of what is up there**, and every study closes on the commitment that makes the
count meaningful: **no level is a folder we invented to give the trail another rung.**

# The Trail All Five Render

`Home` → `Services` (6 pages) → `Operations` (3 pages) → `Operating model redesign` (current).
Across, not up: the other two in Operations are `Cost structure` and `Post-merger integration`.

# The Boundary With S21

`S21` cut a sibling list on the ground that a sibling set is the page's position in the site. That
debt is paid here — every study carries the sibling set as a second labelled landmark. `S21` states
the page's own limit in words; `S22` shows the position and names the rest.

These are authoring and research directions, not production enums. The five studies must
differ structurally. They must not become five colour schemes, five font themes, five
cosmetic variants, or five copies of one grid with the content swapped.

# Media Relationship

None. This role is navigation, not presentation.

# Interaction Notes

Links only. Where local navigation is present it may scroll or filter within the page, but must degrade to plain links.

# Responsive Considerations

A trail must never be silently truncated on small screens without a way to reach the hidden levels. Wrapping, scrolling with a visible affordance, or collapsing to the parent level are all acceptable; hiding the trail entirely is not.

# Related Sections

This role is semantic navigation, not decoration. Studies should use a real navigation landmark with an accessible name, mark the current page programmatically rather than by styling alone, and keep the trail keyboard reachable in a sensible order.

Sits directly above or below S21 on an internal page, and never replaces it.

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION. Design record in `./BATCH-V2.md`; original authoring record in `./BATCH-V1.md`.

# Raw Path

./raw/
