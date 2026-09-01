# Section ID

ARC-S26

# Section Name

Architect / Designer Profile

# Section Role

S26 — Person / Profile Detail

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Architecture & Interior Design

# Prefix

ARC

# Purpose

The detail page for one person: who they are, what they work on, and how to reach them.

# Role Clarification

A portrait-led profile page. Favour the portrait, name, role, a concise biography, disciplines,
selected projects, related services, and credentials only where they are real.

It must not default to a curriculum sheet, a bid CV, a capability matrix or a verification form.

# Visitor Intent

The visitor is deciding whether this is the right person to work with, or has been sent to this
page by name.

# Content Responsibility

One person in full: role, focus, the work they are attached to, and a contact route.

# In Scope

- A portrait, at a scale that makes it the page's anchor
- Name, role and disciplines
- A concise biography
- Selected projects and related services
- Factual professional background the person has supplied
- A contact route appropriate to the sector

# Out Of Scope

- **A global site header, primary navigation or footer**
- A team index or grid, which belongs to S08
- **CV sheets, bid documentation, capability matrices and verification forms**
- Fabricated qualifications, registrations, memberships, awards or credentials
- Invented social handles or profile links
- Testimonials or ratings attributed to a person

# Planned Studies

ARC-S26-001
ARC-S26-002
ARC-S26-003
ARC-S26-004
ARC-S26-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `ARC-S26-001` | Universal / Safe |
| `ARC-S26-002` | Premium / Editorial |
| `ARC-S26-003` | Structured / Visual Modular |
| `ARC-S26-004` | Conversion-led |
| `ARC-S26-005` | Art-directed / Distinctive |

These are authoring and research directions, not production enums, and the study IDs do not change
with them. The five studies must differ structurally. They must not become five colour schemes,
five font themes, five cosmetic variants, or five copies of one grid with the content swapped.

In this section:

- **003** organises richer information visually — grouped panels, project modules, disclosure —
  rather than as a personnel record.
- **005** is an art-directed profile: portrait scale, crop and typographic treatment. Not a CV
  sheet.

**Recorded correction.** `ARC-S26-003` and `ARC-S26-005` are a personnel record and a CV sheet, and
the section is text-heavy throughout. The reserved-field device for unverifiable facts is correct
and stays.

# Architecture Direction

Sector direction: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

The portrait carries the page; the projects give it substance. Keep the biography short enough to
read in one pass and let the work do the rest.

# Section Shell

Page archetype: internal page content architecture is allowed. Global website chrome is not. The
region this page shares with S21 and S22 is marked `data-region="page-context"`.

# Media Relationship

One portrait slot, plus project imagery. A profile must read completely with the portrait absent,
and a filled portrait slot means an image of a real person who has consented to appear.

# Interaction Notes

Normally none.

# Responsive Considerations

Portrait and identity must stay paired at every width; a name must never end up beside or above the
wrong portrait when the layout reflows.

# Authoring Questions

- **Primary visual element:** the portrait, and the projects attached to the person.
- **Immediate understanding:** who this is, what they do, and what they have worked on.

Full authoring question list: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

# Related Sections

Nothing in this role may be invented. Credentials, registrations and memberships are verifiable
facts about real people, and a placeholder study must leave them as reserved fields rather than
fill them.

Roster section for this sector: S08 Architects & Designers (`../S08-architects-designers/`).

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
