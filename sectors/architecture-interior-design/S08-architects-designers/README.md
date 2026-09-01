# Section ID

ARC-S08

# Section Name

Architects & Designers

# Sector

Architecture & Interior Design

# Prefix

ARC

# Purpose

Present the people behind the practice: who they are, what they do, and what they work on.

# Visitor Intent

The visitor wants to see who they would actually be dealing with, and to find the right person for
their project.

# Content Responsibility

The roster: portrait, name, role, discipline, a concise line or two, and the route to a full
profile.

# In Scope

- Portraits as the primary content
- Name, role and discipline
- A concise bio line per person
- The projects or services a person is attached to
- A route into the individual profile page

# Out Of Scope

- A global site header, primary navigation or footer
- One person in full depth, which belongs to S26
- **CV sheets, personnel registers, bid-team schedules or capability matrices**
- Fabricated qualifications, registrations, memberships, awards or contact details

# Planned Studies

ARC-S08-001
ARC-S08-002
ARC-S08-003
ARC-S08-004
ARC-S08-005
ARC-S08-006 (extension variant)
ARC-S08-007 (extension variant)
ARC-S08-008 (extension variant)
ARC-S08-009 (extension variant)

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `ARC-S08-001` | Universal / Safe |
| `ARC-S08-002` | Premium / Editorial |
| `ARC-S08-003` | Structured / Visual Modular |
| `ARC-S08-004` | Conversion-led |
| `ARC-S08-005` | Art-directed / Distinctive |

These are authoring and research directions, not production enums, and the study IDs do not change
with them. The five studies must differ structurally. They must not become five colour schemes,
five font themes, five cosmetic variants, or five copies of one grid with the content swapped.
Extension variants beyond 005 carry their own recorded rationale in the batch document.

In this section:

- **003** holds a larger roster through portrait-led modular arrangement and disclosure — not by
  becoming a personnel list.
- **005** is an art-directed roster composition: portrait scale, crop and rhythm. Not a register.

**Recorded corrections.** `ARC-S08-003` was reviewed as too technical and too text-heavy.
`ARC-S08-007` does not render usably at any width and is a later rebuild; the concept is not
carried forward by this README.

# Architecture Direction

Sector direction: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

Portraits carry this section. Prioritise portrait presence, scale and consistency, then names,
roles and disciplines, then concise bios and project relationships. CV-sheet and bid-document
aesthetics are not the way this section becomes professional.

# Section Shell

Section only. No global header, navigation or footer.

# Media Relationship

Central. A portrait slot per person, reserved and quiet where no real portrait exists. A filled
portrait means a real person who has consented to appear.

# Interaction Notes

Optional. Hover states, disclosure of a longer bio, or a filmstrip are all plausible; every
person's information must remain reachable without script and at every width.

# Responsive Considerations

Portrait and identity must stay paired at every width — a name must never end up beside the wrong
portrait. Filmstrip and rail patterns need a real narrow-width form, not a fixed sliver.

# Authoring Questions

- **Primary visual element:** the portraits and the rhythm of the roster.
- **Immediate understanding:** who the people are and what each of them does.

Full authoring question list: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

# Related Sections

S26 Architect / Designer Profile (`../S26-person-profile-detail/`) is the full page behind one
person here. S07 Studio About (`../S07-studio-about/`) is the practice as a whole.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
