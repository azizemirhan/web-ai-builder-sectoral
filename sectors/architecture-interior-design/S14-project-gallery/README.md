# Section ID

ARC-S14

# Section Name

Project Gallery

# Sector

Architecture & Interior Design

# Prefix

ARC

# Purpose

Show the work itself. This is the sector's most purely visual section: media is the content.

# Visitor Intent

The visitor wants to look at the projects, with as little between them and the images as possible.

# Content Responsibility

A controlled set of images with light captioning, arranged with a deliberate rhythm.

# In Scope

- Project, interior and detail imagery at varied proportions
- Light captioning: project record and view
- A deliberate arrangement rhythm rather than a repeated cell
- An optional route into the project pages

# Out Of Scope

- A global site header, primary navigation or footer
- **Contact-sheet density.** A conventional grid presentation carries a maximum of **3 × 3 = 9**
  visible media slots. This is a maximum, not a requirement; editorial and carousel presentations
  may use fewer. Eighteen-frame arrangements are not this section.
- Excessive captions, numbered legends or technical image registers
- Sheet framing, drawing-set navigation or plate numbering as the gallery's structure
- Fabricated project names, addresses, dates or completion claims

# Planned Studies

ARC-S14-001
ARC-S14-002
ARC-S14-003
ARC-S14-004
ARC-S14-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `ARC-S14-001` | Universal / Safe |
| `ARC-S14-002` | Premium / Editorial |
| `ARC-S14-003` | Structured / Visual Modular |
| `ARC-S14-004` | Conversion-led |
| `ARC-S14-005` | Art-directed / Distinctive |

These are authoring and research directions, not production enums, and the study IDs do not change
with them. The five studies must differ structurally. They must not become five colour schemes,
five font themes, five cosmetic variants, or five copies of one grid with the content swapped.

In this section:

- **003** is the structured grid variant, held to the 3 × 3 maximum. Its capacity shows in the
  order and proportion of the arrangement, not in frame count or in a numbered legend.
- **005** is an art-directed gallery — crop, scale ordering, pacing — and not a drawing or photo
  register.

**Recorded correction.** `ARC-S14-003` shows eighteen frames with a numbered legend and is a later
rework; the gallery is to be capped at 3 × 3. `ARC-S14-005` uses sheet framing.

# Architecture Direction

Sector direction: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

Because every slot is empty until real media arrives, the arrangement itself has to be legible:
vary the proportions deliberately so the rhythm reads even when nothing is in it. Fewer,
better-proportioned images beat a wall of thumbnails.

# Section Shell

Section only. No global header, navigation or footer.

# Media Relationship

Central and defining. Media is the content. Slot proportions are a design decision and are
recorded in the batch document.

# Interaction Notes

Optional. A lightbox or carousel is plausible; every image and caption must remain reachable
without script, and any horizontal sequence needs a keyboard route and a visible affordance.

# Responsive Considerations

Cells must never fall below a proportion where the image stops reading. Column reductions should
remap spans deliberately rather than letting cells shrink uniformly.

# Authoring Questions

- **Primary visual element:** the images and the proportional rhythm of the arrangement.
- **Immediate understanding:** the character and quality of the work, at a glance.

Full authoring question list: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

# Related Sections

S02 Selected Projects (`../S02-selected-projects/`) indexes projects with metadata; S13 Featured
Project Case Study (`../S13-featured-project-case-study/`) features one in depth; this section
shows the work and captions it.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
