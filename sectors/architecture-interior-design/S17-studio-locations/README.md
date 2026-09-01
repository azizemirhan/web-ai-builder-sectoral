# Section ID

ARC-S17

# Section Name

Studio Locations

# Sector

Architecture & Interior Design

# Prefix

ARC

# Purpose

Show where the practice works from, as a set of places rather than as a directory.

# Visitor Intent

The visitor wants to know whether there is a studio near them, and what that studio is like.

# Content Responsibility

The location set: each studio named and pictured, with concise contact and context, and a route to
its full page.

# In Scope

- Studio and location imagery
- City or location name
- Concise contact and context per location
- Elegant location cards
- An optional reserved map area where it genuinely helps
- A route into the location detail page

# Out Of Scope

- A global site header, primary navigation or footer
- **Coordinate systems, location atlases and directory tables** as the default device
- One location in full depth, which belongs to S27
- Embedded third-party maps or any remote dependency
- Fabricated addresses, coordinates, phone numbers or opening hours

# Planned Studies

ARC-S17-001
ARC-S17-002
ARC-S17-003
ARC-S17-004
ARC-S17-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `ARC-S17-001` | Universal / Safe |
| `ARC-S17-002` | Premium / Editorial |
| `ARC-S17-003` | Structured / Visual Modular |
| `ARC-S17-004` | Conversion-led |
| `ARC-S17-005` | Art-directed / Distinctive |

These are authoring and research directions, not production enums, and the study IDs do not change
with them. The five studies must differ structurally. They must not become five colour schemes,
five font themes, five cosmetic variants, or five copies of one grid with the content swapped.

In this section:

- **003** organises several locations through visual cards and grouped practical information, not
  through a directory table.
- **005** is an art-directed presentation of place — studio photography, city character — not a
  coordinate atlas.

**Recorded correction.** `ARC-S17-003` is a directory table and `ARC-S17-005` a coordinate atlas;
neither carries media. Both are later reworks.

# Architecture Direction

Sector direction: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

A studio is a place, and places photograph. Location cards with studio imagery and short access
lines carry this section; coordinates and keyed plans do not.

# Section Shell

Section only. No global header, navigation or footer.

# Media Relationship

Expected. Studio or city imagery per location, plus an optional reserved map area. A map area is a
reserved slot, never an embedded service.

# Interaction Notes

Optional. A location switcher must remain a set of plain links.

# Responsive Considerations

Address and contact details must stay first-class at small widths and must not be pushed below
decorative media.

# Authoring Questions

- **Primary visual element:** studio and location photography.
- **Immediate understanding:** where the practice is, and which studio is relevant.

Full authoring question list: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

# Related Sections

S27 Studio / Location Detail (`../S27-location-branch-detail/`) is the full page behind one entry
here; S07 Studio About (`../S07-studio-about/`) covers the practice as a whole.

# Status

READY_FOR_INGESTION

# Raw Path

./raw/

# Batch

./BATCH-V1.md
