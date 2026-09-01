# Section ID

ARC-S20

# Section Name

Consultation CTA

# Sector

Architecture & Interior Design

# Prefix

ARC

# Purpose

A high-impact conversion section: invite the visitor into a consultation and give them one clear
way to take it.

# Visitor Intent

The visitor is close to making contact and needs a single, obvious next step.

# Content Responsibility

The invitation: a concise headline, one supporting sentence, the primary action, and at most a few
short supporting points.

# In Scope

- A concise headline
- One supporting sentence
- A primary call to action
- Optional media
- Optional short supporting points

# Out Of Scope

- A global site header, primary navigation or footer
- **Agenda sheets, meeting documents and appointment-form framing**
- The enquiry form itself, which belongs to S19
- Fabricated availability, response times, fees or guarantees
- Multiple competing calls to action

# Planned Studies

ARC-S20-001
ARC-S20-002
ARC-S20-003
ARC-S20-004
ARC-S20-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `ARC-S20-001` | Universal / Safe |
| `ARC-S20-002` | Premium / Editorial |
| `ARC-S20-003` | Structured / Visual Modular |
| `ARC-S20-004` | Conversion-led |
| `ARC-S20-005` | Art-directed / Distinctive |

These are authoring and research directions, not production enums, and the study IDs do not change
with them. The five studies must differ structurally. They must not become five colour schemes,
five font themes, five cosmetic variants, or five copies of one grid with the content swapped.

In this section:

- **003** may carry a few supporting points as visual modules; it must stay an invitation rather
  than becoming an information panel.
- **005** is an art-directed invitation — imagery, scale, typographic confidence. Not an agenda
  document.

**Recorded correction.** `ARC-S20-005` is an agenda document and is a later rebuild.

# Architecture Direction

Sector direction: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

Compactness is the point. A single strong image field or an expanse of quiet space, a short line,
and one action.

# Section Shell

Section only. No global header, navigation or footer.

# Media Relationship

Optional. Where present, one deliberate image field rather than several small ones.

# Interaction Notes

A real link or button, keyboard operable, with a visible focus state.

# Responsive Considerations

The action must remain visible and tappable without scrolling past decorative media, and the
headline must not clip at 320px.

# Authoring Questions

- **Primary visual element:** the single media field or the whitespace framing the invitation.
- **Immediate understanding:** what is being offered and how to take it.

Full authoring question list: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

# Related Sections

S19 Project Inquiry (`../S19-project-inquiry/`) is where this invitation leads.

# Status

READY_FOR_INGESTION

# Raw Path

./raw/

# Batch

./BATCH-V1.md
