# Section ID

ARC-S19

# Section Name

Project Inquiry

# Sector

Architecture & Interior Design

# Prefix

ARC

# Purpose

Collect an initial project enquiry: enough to start a conversation, and no more.

# Visitor Intent

The visitor has decided to make contact and wants to do it quickly, without being interrogated.

# Content Responsibility

The enquiry itself: a short set of questions with real labels, a clear submit action, and enough
context to make sending it feel reasonable.

# In Scope

- A clear, modern form composition
- Concise questions with real labels and visible focus states
- Strong whitespace around the form
- A contextual image where it supports the enquiry
- A progressive or multi-step structure where it genuinely reduces friction

# Out Of Scope

- A global site header, primary navigation or footer
- **Working sheets, project issue sheets and briefing-document framing**
- Long qualification questionnaires
- Fabricated response times, fees or availability
- The general consultation invitation, which belongs to S20

# Planned Studies

ARC-S19-001
ARC-S19-002
ARC-S19-003
ARC-S19-004
ARC-S19-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `ARC-S19-001` | Universal / Safe |
| `ARC-S19-002` | Premium / Editorial |
| `ARC-S19-003` | Structured / Visual Modular |
| `ARC-S19-004` | Conversion-led |
| `ARC-S19-005` | Art-directed / Distinctive |

These are authoring and research directions, not production enums, and the study IDs do not change
with them. The five studies must differ structurally. They must not become five colour schemes,
five font themes, five cosmetic variants, or five copies of one grid with the content swapped.

In this section:

- **003** may ask more, but through grouped steps and disclosure rather than as one long field
  wall.
- **005** is an art-directed enquiry composition — imagery, scale, typographic framing around a
  clean form. Not a project issue sheet.

**Recorded correction.** `ARC-S19-005` is a working project sheet and is a later rebuild.

# Architecture Direction

Sector direction: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

Form clarity comes first here; the Architecture register comes from the space around the form and
from a single contextual image, not from documentary framing.

# Section Shell

Section only. No global header, navigation or footer.

# Media Relationship

Optional. One contextual image at most; this section legitimately carries little media.

# Interaction Notes

Real form controls with real labels, keyboard operable, visible focus. Multi-step structures must
keep every field reachable and must not depend on script to be understood.

# Responsive Considerations

Fields must be full width and comfortably tappable on a phone, labels must stay attached to their
inputs, and a two-column form must collapse in a sensible order.

# Authoring Questions

- **Primary visual element:** the form composition and the space around it, with an optional
  contextual image.
- **Immediate understanding:** what is being asked, and that it is short.

Full authoring question list: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

# Related Sections

S20 Consultation CTA (`../S20-consultation-cta/`) is the invitation; this section is the enquiry
itself.

# Status

READY_FOR_INGESTION

# Raw Path

./raw/

# Batch

./BATCH-V1.md
