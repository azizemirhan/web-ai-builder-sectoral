# Section ID

ARC-S22

# Section Name

Breadcrumb / Context Navigation

# Section Role

S22 — Breadcrumb / Context Navigation

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Architecture & Interior Design

# Prefix

ARC

# Purpose

Show where the current page sits in the site hierarchy, and give the visitor a way back up it.

# Role Clarification

**This section means a conventional website breadcrumb.**

The core semantic model is:

    Home / Projects / Residential / Project Name

or its equivalent for another branch of the site.

The five variants may differ through typography, spacing, container treatment, background,
separators, a subtle contextual label or minimal supporting context. **The function must remain
breadcrumb navigation.**

S22 must not turn into sibling navigation, a project pager, a page table of contents, a key plan, a
technical locator, a section index or a mini sitemap.

# Visitor Intent

The visitor wants to know what this page is part of, and to move up a level without returning to
the homepage.

# Content Responsibility

Hierarchy and position: a breadcrumb trail from a root to the current page, and a clear indication
of where the current page sits in it.

# In Scope

- A breadcrumb trail from a root to the current page
- A clear indication of the current page within that trail
- Optional contextual back navigation to the parent
- An optional short context line, such as the collection this page belongs to

# Out Of Scope

- Primary site navigation, which belongs to the page chrome
- **Sibling navigation, project pagers, page contents, key plans, drawing-set locators, section
  indexes and mini sitemaps**
- Decorative text that only looks like a breadcrumb
- Page title and introduction, which belong to S21
- Footer navigation or sitemap listings

# Planned Studies

ARC-S22-001
ARC-S22-002
ARC-S22-003
ARC-S22-004
ARC-S22-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `ARC-S22-001` | Universal / Safe |
| `ARC-S22-002` | Premium / Editorial |
| `ARC-S22-003` | Structured / Visual Modular |
| `ARC-S22-004` | Conversion-led |
| `ARC-S22-005` | Art-directed / Distinctive |

These are authoring and research directions, not production enums, and the study IDs do not change
with them. The five studies must differ structurally — but within one component role.

In this section:

- **003** may add a container, a background band or a minimal contextual label alongside the trail.
  It does not gain content capacity by becoming a navigation system.
- **005** can be visually distinctive — typography, separators, spacing, treatment — without
  changing the component's role.

**Recorded correction.** Three of five studies broadened breadcrumbs into sibling navigation,
project paging or a drawing-set locator and are later rebuilds. `ARC-S22-001` is the reference.

# Architecture Direction

Sector direction: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

This is the one Architecture role where restraint is the whole design. The sector register shows in
type and spacing, nothing more.

# Section Shell

Component only. Not the site's primary navigation, and never a substitute for it.

# Media Relationship

None. This role is navigation, not presentation.

# Interaction Notes

Links only.

# Accessibility

Use a real navigation landmark with an accessible name, mark the current page programmatically —
`aria-current` — rather than by styling alone, and keep the trail keyboard reachable in order.

# Responsive Considerations

A trail must never be silently truncated on small screens without a way to reach the hidden levels. Wrapping, scrolling with a visible affordance, or collapsing to the parent level are all acceptable; hiding the trail entirely is not.

# Authoring Questions

- **Primary visual element:** the trail itself — type, spacing and separator treatment.
- **Immediate understanding:** where this page sits, and how to go up.

Full authoring question list: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

# Related Sections

Sits directly above or below S21 (`../S21-subpage-hero/`) on an internal page, and never replaces
it.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
