# Section ID

ARC-S24

# Section Name

Project Detail

# Section Role

S24 — Project / Case Study Detail

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Architecture & Interior Design

# Prefix

ARC

# Purpose

The detail page for one project, presented as the practice's own portfolio would present it.

# Role Clarification

**This is a full project detail page archetype**, and Architecture is a strongly visual sector: the
page is carried by project imagery.

Prioritise a project hero, the project title, concise metadata, large project imagery, a short
project narrative, full-width media, image-and-text relationships, project details, a controlled
gallery and related projects.

Metadata such as typology, location, discipline, year and status appears only where the data is
supplied and real.

# Visitor Intent

The visitor is assessing capability. They want to see one project in depth: what it is, how it was
approached, and what it became.

# Content Responsibility

One project in full: context, approach, what was delivered, the imagery that shows it, and the
people or services involved.

# In Scope

- A project hero and large project imagery
- Project title and concise factual metadata
- A short project narrative
- Full-width media and image-and-text relationships
- Selected project details
- A controlled gallery
- Links to the services and people involved, and to related projects

# Out Of Scope

- **A global site header, primary navigation or footer**
- An index or gallery of all work, which belongs to S02 and S14
- **Project dossiers, drawing issue sets, technical project registers, schedule-led compositions
  and drawing-sheet navigation**
- A commerce or product detail template
- Fabricated clients, outcomes, figures, budgets, areas or testimonials
- Any claim the sector's confidentiality position does not permit

# Planned Studies

ARC-S24-001
ARC-S24-002
ARC-S24-003
ARC-S24-004
ARC-S24-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `ARC-S24-001` | Universal / Safe |
| `ARC-S24-002` | Premium / Editorial |
| `ARC-S24-003` | Structured / Visual Modular |
| `ARC-S24-004` | Conversion-led |
| `ARC-S24-005` | Art-directed / Distinctive |

These are authoring and research directions, not production enums, and the study IDs do not change
with them. The five studies must differ structurally. They must not become five colour schemes,
five font themes, five cosmetic variants, or five copies of one grid with the content swapped.

In this section:

- **003** supports richer project information through modular visual blocks — grouped media,
  panelled details, disclosure — not through a dossier or a register.
- **005** is strong art-directed project storytelling: scale, crop, sequence and pacing.

**Recorded correction.** `ARC-S24-003` and `ARC-S24-005` reproduce a dossier and a drawing issue
set and were reviewed as too technical and too document-like. `ARC-S24-001`, `002` and `004` are
portfolio-shaped and are the reference for the section.

# Architecture Direction

Sector direction: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

This is the sector's flagship visual page. Large imagery, generous space, concise metadata and a
narrative that moves between images rather than around them.

# Section Shell

Page archetype: internal page content architecture is allowed. Global website chrome is not. The
region this page shares with S21 and S22 is marked `data-region="page-context"`.

# Media Relationship

Central. This role usually carries the largest documented media set in the catalogue, and the batch
document must record each slot's purpose, expected type and fallback.

# Interaction Notes

Optional. Galleries, before/after comparisons and stage navigation are all plausible, and each must
remain fully readable without script.

# Responsive Considerations

A long project narrative interleaved with media is the hardest thing here to keep coherent.
Reading order must survive every reflow, and no media set may become a horizontal scroll without a
label and a keyboard route.

# Authoring Questions

- **Primary visual element:** the project imagery, from hero to gallery.
- **Immediate understanding:** which project this is, and what it looks like.

Full authoring question list: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

# Related Sections

This is the depth page behind one entry in S02 Selected Projects (`../S02-selected-projects/`).
S13 Featured Project Case Study (`../S13-featured-project-case-study/`) is the section-scale
version; S14 Project Gallery (`../S14-project-gallery/`) is the gallery section.

# Status

READY_FOR_INGESTION

# Raw Path

./raw/

# Batch

./BATCH-V1.md
