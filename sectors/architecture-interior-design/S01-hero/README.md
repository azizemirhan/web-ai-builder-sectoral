# Section ID

ARC-S01

# Section Name

Hero

# Section Role

S01 — Hero

Sector Core (S01–S20). This is a **section** study: it describes the opening section of the
homepage, not a whole page.

# Sector

Architecture & Interior Design

# Prefix

ARC

# Purpose

The primary homepage hero for the practice. It establishes what kind of studio this is and the
quality of its work in one screen, then hands off to the page below.

# Visitor Intent

The visitor has just arrived, usually knowing little or nothing about the practice. They are
forming a first judgement about the work before they read anything.

# Content Responsibility

Practice identity and first visual impression: a short positioning statement, the primary media
field, and at most one action.

# In Scope

- A short positioning line or practice statement
- A primary media field carrying project, interior or spatial photography
- An optional single call to action
- An optional small contextual label such as a discipline or location line

# Out Of Scope

- **A global site header, logo bar, primary navigation, footer or announcement bar**
- A drawing title block, sheet reference or issue stamp used as hero framing
- A project index or grid, which belongs to S02
- Extended positioning copy, which belongs to S05 and S07
- Multiple competing calls to action

# Planned Studies

ARC-S01-001
ARC-S01-002
ARC-S01-003
ARC-S01-004
ARC-S01-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `ARC-S01-001` | Universal / Safe |
| `ARC-S01-002` | Premium / Editorial |
| `ARC-S01-003` | Structured / Visual Modular |
| `ARC-S01-004` | Conversion-led |
| `ARC-S01-005` | Art-directed / Distinctive |

These are authoring and research directions, not production enums, and the study IDs do not change
with them. The five studies must differ structurally. They must not become five colour schemes,
five font themes, five cosmetic variants, or five copies of one grid with the content swapped.

In this section:

- **001** is a balanced image-and-copy hero.
- **002** is a premium editorial or full-bleed hero.
- **003** is a structured visual hero: modular media and content blocks composing one opening
  statement, not a hero carrying a field list.
- **004** is a project-enquiry-aware hero where the onward route is part of the composition.
- **005** is a strongly art-directed hero — unusual but elegant composition, crop, scale or
  typographic treatment — and not a drawing sheet.

# Architecture Direction

Sector direction: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

This is the most image-led section in the sector. Impact comes from the media field, the crop, the
scale relationship and the typographic treatment. Copy is short by definition. Sheet framing,
title blocks and reference notation are not the way this section becomes architectural.

# Section Shell

Hero only. No logo, no navigation, no header shell, no footer.

# Media Relationship

Central. At least one large media field, and studies should differ in how that field is scaled and
cropped rather than repeating one full-bleed answer.

# Interaction Notes

Minimal. Any interaction — a scroll cue, a slow media transition — must respect reduced motion and
must not be required to understand the section.

# Responsive Considerations

The positioning line must be readable first at every width. A media field should reduce or
re-crop rather than disappearing, and a hero must never leave a fixed empty band on a phone.

# Authoring Questions

- **Primary visual element:** the main project or interior image field and its crop.
- **Immediate understanding:** what kind of practice this is, and that the work is worth scrolling
  for.

Full authoring question list: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

# Related Sections

S21 Subpage Hero (`../S21-subpage-hero/`) is the internal-page hero. A study that would work
unchanged as S21 has not answered this role. The project index that follows is S02 Selected
Projects (`../S02-selected-projects/`).

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
