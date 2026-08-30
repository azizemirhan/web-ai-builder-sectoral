# Section ID

AUTO-S22

# Section Name

Breadcrumb / Context Navigation

# Section Role

S22 — Breadcrumb / Context Navigation

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Automotive

# Prefix

AUTO

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

AUTO-S22-001
AUTO-S22-002
AUTO-S22-003
AUTO-S22-004
AUTO-S22-005

# Expected Structural Diversity

| Variant | Territory |
| --- | --- |
| `AUTO-S22-001` | Universal / Safe |
| `AUTO-S22-002` | Premium / Editorial |
| `AUTO-S22-003` | Dense / Information-heavy |
| `AUTO-S22-004` | Conversion-led |
| `AUTO-S22-005` | Sector-native / Distinctive |

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

NOT_STARTED

# Raw Path

./raw/
