# Section ID

WELL-S02

# Section Name

Treatments Services

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Planned Studies

WELL-S02-001
WELL-S02-002
WELL-S02-003
WELL-S02-004
WELL-S02-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `WELL-S02-001` | Universal / Safe |
| `WELL-S02-002` | Premium / Editorial |
| `WELL-S02-003` | Structured / Visual Modular |
| `WELL-S02-004` | Conversion-led |
| `WELL-S02-005` | Art-directed / Distinctive |

These are the current authoring directions from `../../../standards/01-AUTHORING-STANDARD.md`,
read for this sector in `../WELLNESS-DESIGN-DIRECTION.md`. They are research directions, not
production enums, and the study IDs do not change with them.

# Section Role

The treatments themselves. The section names the individual treatments a guest can book, gives
each one a short description and its own visual identity, and routes onward to the treatment
detail page. The visitor leaves having chosen **a specific treatment**, not a kind of treatment.

It answers: *what do you actually do to me, and which one do I want?*

# Boundary With S03

`S03-service-categories/` owns the grouping layer above this one. Category names — `Facials`,
`Body & massage`, `Hands & feet`, `Brows & lashes` — belong there and must not become the subject
of this section. The visitor leaves S03 having chosen a **kind**; they leave S02 having chosen a
**thing**.

    "Facials" is S03. "Deep cleansing facial", with its own description and its own media, is S02.

A category name may still appear here as a small tag on a treatment, the way a card carries a
label. It may not be the item being presented.

`WELL-S01-003` already carries a four-item category group as a routing device inside the hero.
Neither S02 nor S03 should read as a larger copy of that block.

# Out Of Scope

- A global site header, primary navigation or footer
- Category-level browsing, which belongs to S03
- One treatment in full depth, which belongs to S23
- Prices, package values and membership terms, which belong to S11 and S12 — and which are
  reserved rather than invented wherever they do appear
- Practitioners, which belong to S04
- Before/after and outcome evidence, which belongs to S05 and is bound by the claims rule

# Copy Rule For This Section

This is the section where efficacy language is most likely to enter the catalog, because real spa
sites describe treatments by what they achieve. Under the claims rule in
`../WELLNESS-DESIGN-DIRECTION.md`, treatment descriptions in every `WELL-S02` study are written
**procedurally** — what happens in the room, in order — rather than by outcome.

    Not: "Restores volume and softens fine lines."
    But: "Cleansing, steam, and a slow massage through the face and neck."

Procedural description keeps the copy genuinely useful to a visitor while making no claim that
would need evidence.

# Authoring Questions

**1. What is the primary visual element of this role?**

One photograph per treatment, at a scale that shows the treatment happening — hands at work, the
material being used, the guest at rest. A treatment list without media is a price list.

**2. What must a visitor understand immediately?**

What each treatment actually involves, how the treatments differ from one another, and how to go
further into the one they want.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V2.md (design layer, current) · ./BATCH-V1.md (original authoring record)
