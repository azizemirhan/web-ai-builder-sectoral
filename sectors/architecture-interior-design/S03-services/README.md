# Section ID

ARC-S03

# Section Name

Services

# Sector

Architecture & Interior Design

# Prefix

ARC

# Purpose

State what the studio offers: the set of services a client can engage, each described briefly
enough to choose between them.

# Visitor Intent

The visitor is working out whether the practice does the kind of work they need, and which
offering that would be.

# Content Responsibility

The service set: each service named, described concisely, given a visual identity, and linked
onward where a detail page exists.

# In Scope

- Named services with concise descriptions
- A media or visual treatment attached to each service
- Optional grouping of related services
- An onward route to the service detail page

# Out Of Scope

- A global site header, primary navigation or footer
- **The design process**, which belongs to S06 — services state *what is offered*, not *how a
  project is run*
- One service in full depth, which belongs to S23
- Specification-style field lists, inclusion tables or scope schedules as the primary device
- Fabricated fees, durations, guarantees or availability

# Planned Studies

ARC-S03-001
ARC-S03-002
ARC-S03-003
ARC-S03-004
ARC-S03-005
ARC-S03-006 (extension variant)
ARC-S03-007 (extension variant)

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `ARC-S03-001` | Universal / Safe |
| `ARC-S03-002` | Premium / Editorial |
| `ARC-S03-003` | Structured / Visual Modular |
| `ARC-S03-004` | Conversion-led |
| `ARC-S03-005` | Art-directed / Distinctive |

These are authoring and research directions, not production enums, and the study IDs do not change
with them. The five studies must differ structurally. They must not become five colour schemes,
five font themes, five cosmetic variants, or five copies of one grid with the content swapped.
Extension variants beyond 005 carry their own recorded rationale in the batch document.

In this section:

- **003** organises a larger service set through visual modularity — cards, panels, grouped media,
  disclosure — rather than by adding a specification field list to each card.
- **005** is an art-directed services composition: imagery, scale and typographic contrast, not a
  service sheet or scope schedule.

# Architecture Direction

Sector direction: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

Prefer service cards and visual modules, concise service descriptions, and a real
image-to-service relationship. Interaction is welcome where it helps a visitor compare offerings.
A service becomes legible through the work it produces; pair it with imagery rather than with a
longer definition.

# Section Shell

Section only. No global header, navigation or footer.

# Media Relationship

Expected. Each service should be able to carry its own media area; the section should not present
services as text blocks alone.

# Interaction Notes

Optional. Tabs, disclosure or hover states are justified where the service set is large, and all
content must remain reachable without script.

# Responsive Considerations

Service cards must reflow to full-width blocks that keep image, name and description together. A
card grid must not leave narrow media slivers at small widths.

# Authoring Questions

- **Primary visual element:** the image or visual treatment attached to each service.
- **Immediate understanding:** what the studio can be engaged to do.

Full authoring question list: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

# Related Sections

S06 Design Process (`../S06-design-process/`) explains how a project runs; S10 Capabilities
(`../S10-capabilities/`) states what the practice can take on; S23 Architecture / Interior Service
Detail (`../S23-service-offering-detail/`) is the full page behind one entry here.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
