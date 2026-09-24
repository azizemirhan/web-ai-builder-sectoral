# Section ID

WELL-S03

# Section Name

Service Categories

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Planned Studies

WELL-S03-001
WELL-S03-002
WELL-S03-003
WELL-S03-004
WELL-S03-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `WELL-S03-001` | Universal / Safe |
| `WELL-S03-002` | Premium / Editorial |
| `WELL-S03-003` | Structured / Visual Modular |
| `WELL-S03-004` | Conversion-led |
| `WELL-S03-005` | Art-directed / Distinctive |

These are the current authoring directions from `../../../standards/01-AUTHORING-STANDARD.md`,
read for this sector in `../WELLNESS-DESIGN-DIRECTION.md`. They are research directions, not
production enums, and the study IDs do not change with them.

# Section Role

The grouping layer. The section presents the small set of categories the studio's work divides
into, gives each one a visual identity and a single line saying what it covers, and routes onward
into that group. The visitor leaves having chosen **a kind of treatment**, not a specific one.

It answers: *which part of what you do is the part I want?*

# Boundary With S02

`S02-treatments-services/` owns the individual treatments. A named treatment with its own
description and its own media belongs there and must not become the subject of this section.

    "Facials" is S03. "Deep cleansing facial", with its own description and its own media, is S02.

A category panel in this section may **preview** what a category contains — a short list of the
treatment names inside it, as plain routing text. That is the category answering "what is in
here?", which is category-level navigation and belongs to this role. It stops being S03 the moment
a treatment gets its own description, its own media or its own action.

`WELL-S01-003` already carries a four-item category group as a routing device inside the hero.
This section is the full expression of that role, not a larger copy of that block: the hero group
is a compact list of names, while this section gives each category media, a line and a route.

# Category Set

The sector's four categories, used consistently across `S01`, `S02` and `S03` so the catalog reads
as one site:

| Category | What it covers |
| --- | --- |
| Facials | Cleansing, steam and hands-on work for the face and neck |
| Body & massage | Full-body work, from slow massage to scrubs and wraps |
| Hands & feet | Soaking, shaping and massage for hands and feet |
| Brows & lashes | Shaping, tinting and detail work around the eyes |

# Out Of Scope

- A global site header, primary navigation or footer
- Individual treatments presented as the subject, which belongs to S02
- One category in full depth, which belongs to S23
- Prices, package values and membership terms, which belong to S11 and S12
- Practitioners, which belong to S04
- Before/after and outcome evidence, which belongs to S05 and is bound by the claims rule

# Copy Rule For This Section

The claims rule in `../WELLNESS-DESIGN-DIRECTION.md` applies unchanged, and the procedural
description rule established for `S02` applies here at category scale: a category line says what
the category **covers**, never what it achieves.

    Not: "Skin that looks visibly younger."
    But: "Cleansing, steam and hands-on work for the face and neck."

# Authoring Questions

**1. What is the primary visual element of this role?**

One image per category, chosen so the four read as clearly different kinds of work at a glance —
a face, a back, hands, eyes. In a categories section the images do the sorting; the words only
confirm it.

**2. What must a visitor understand immediately?**

That the work divides into a small number of kinds, which kind theirs is, and how to go into it.
Four categories should be legible without reading a single line.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V2.md (design layer, current) · ./BATCH-V1.md (original authoring record)
