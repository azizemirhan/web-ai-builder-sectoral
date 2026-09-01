# Section ID

ARC-S21

# Section Name

Subpage Hero

# Section Role

S21 — Subpage Hero

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Architecture & Interior Design

# Prefix

ARC

# Purpose

Top-of-page contextual hero for an internal page. It states where the visitor has landed and what
the page is for, then hands off to the page body.

# Role Clarification

**This is a conventional website internal-page hero, adapted for Architecture & Interior Design.**

It is the hero at the top of a Services page, a Projects page, an About page, a Contact page, a
Journal page, or an individual content page where that is appropriate.

It may be:

- a background-image hero
- a contained-image hero
- a split text and image hero
- a typography-only hero
- a subtle colour or background treatment

It should usually contain a page title, an optional short description, an optional small
contextual label, and an optional call to action where one is genuinely appropriate.

It must **not** become a dossier cover, a project register, a metadata database, a folio, a drawing
sheet, a specification header or a contents index. Keep it recognisably a normal website subpage
hero.

# Visitor Intent

The visitor has already arrived from somewhere specific. They are checking that this is the page they wanted and orienting themselves before reading.

# Content Responsibility

Page identity: title, a short contextual introduction, optional contextual metadata, optional media, and at most one contextual action.

# In Scope

- Page title and, where useful, a parent or category label
- A short introduction that frames the page rather than the sector
- A small amount of contextual metadata such as category, date, reading time or discipline
- An optional single contextual action tied to this page
- An optional media area sized for an internal page rather than a landing stage

# Out Of Scope

- A restatement of the homepage hero from S01
- Primary sector positioning or brand manifesto copy
- **A global site header, primary navigation or footer** — navigation context belongs to S22
- Body content that belongs to S23 to S27
- **Metadata registers, dossier covers, drawing sheets, folios and contents indexes**
- Multiple competing calls to action

# Planned Studies

ARC-S21-001
ARC-S21-002
ARC-S21-003
ARC-S21-004
ARC-S21-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `ARC-S21-001` | Universal / Safe |
| `ARC-S21-002` | Premium / Editorial |
| `ARC-S21-003` | Structured / Visual Modular |
| `ARC-S21-004` | Conversion-led |
| `ARC-S21-005` | Art-directed / Distinctive |

These are authoring and research directions, not production enums, and the study IDs do not change
with them. The five studies must differ structurally. They must not become five colour schemes,
five font themes, five cosmetic variants, or five copies of one grid with the content swapped.

In this section:

- **001** is the simple, classic internal-page hero.
- **002** is a premium image-led hero.
- **003** is a structured visual hero: a split or modular arrangement of title, context and media.
  It is not a hero carrying a metadata table.
- **004** is context- and CTA-aware.
- **005** is an art-directed Architecture banner — and still a subpage hero.

**Recorded correction.** The section as authored read the role as a document header rather than a
website internal-page hero; four of five studies are later reworks or rebuilds.

# Architecture Direction

Sector direction: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

Architecture character here comes from the image, the crop and the typographic treatment of the
page title — not from reference notation or metadata apparatus.

# Section Shell

Section only. No global header, primary navigation or footer, even though this role sits at the top
of a page where those would exist in production.

# Media Relationship

Optional. An internal page hero often carries no image at all, and the study set should include at least one variant that works without one. Where media is present it is usually smaller and more contained than the S01 stage.

# Interaction Notes

Normally none. Any interaction should be limited to a single contextual action.

# Responsive Considerations

The title must remain the first thing read at every width. Contextual metadata should wrap rather than truncate, and any media area should be allowed to reduce or disappear before the title does.

# Authoring Questions

- **Primary visual element:** the page title, and the media treatment framing it.
- **Immediate understanding:** which page this is and what it is for.

Full authoring question list: `../ARCHITECTURE-DESIGN-DIRECTION.md`.

# Related Sections

S01 is the homepage or primary sector hero. S21 is the internal page contextual hero. A study that would work unchanged as S01 has not answered this role.

Homepage hero for this sector: S01 Hero (`../S01-hero/`).

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
