# Section ID

WELL-S09

# Section Name

Technology Products

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Planned Studies

WELL-S09-001
WELL-S09-002
WELL-S09-003
WELL-S09-004
WELL-S09-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `WELL-S09-001` | Universal / Safe |
| `WELL-S09-002` | Premium / Editorial |
| `WELL-S09-003` | Structured / Visual Modular |
| `WELL-S09-004` | Conversion-led |
| `WELL-S09-005` | Art-directed / Distinctive |

These are the current authoring directions from `../../../standards/01-AUTHORING-STANDARD.md`,
read for this sector in `../WELLNESS-DESIGN-DIRECTION.md`. They are research directions, not
production enums, and the study IDs do not change with them.

# Section Role

What the work is done with. The section covers the equipment in the room and the products used on
the skin — what they are, how they are chosen, and how they are looked after.

It answers: *what is going to touch me, and where did it come from?*

# The Governing Constraint — And The Distinction That Resolves It

This role is about named things, and named things in this sector are **brands**. A real
implementation of this section carries device names, product ranges and partner marks. A
placeholder carries none of them: `03-MEDIA-POLICY.md` forbids inventing products, logos and
brands outright, and `../WELLNESS-DESIGN-DIRECTION.md` forbids the device-specification blocks and
ingredient tables this role most naturally reaches for.

The distinction that makes it authorable, which is the same move as `S04`:

| Layer | Example | Status |
| --- | --- | --- |
| **Brand** | A device name, a product range, a manufacturer, a partner mark | **Reserved**, never invented. Marks are reserved media areas, exactly like the portrait slots in `S04`. |
| **Function** | "A steamer", "hand tools", "warm stones", "cleansers", "oils" | **Allowed.** Generic room objects and product categories, not brands. |
| **Policy** | "Cleaned between every guest", "chosen in the room", "any label can be read on request" | **Allowed, and it is the real content.** How a studio looks after its tools and chooses its products is a fact about the studio. |

**Function and policy lead; brand is reserved.** This is the same resolution as `S04`, where the
role led and the name was reserved — and as there, it produces the better section: a visitor
learns more from *cleaned between every guest* than from a logo they do not recognise.

**Not present in any study:** an invented device name, product name, range, manufacturer,
ingredient, patent or partner mark; a certification, approval or compliance mark; the phrase
*medical grade*, *clinically tested*, *professional only* or an equivalent; an efficacy claim about
any device or product; a specification block, ingredient table or device datasheet; a price; a
percentage; an award.

**Marks are reserved, not omitted.** Where a real page would carry a row of partner marks, the
studies reserve that row as empty media slots. The structure is demonstrated; the brands are not
invented.

# Boundary With S02, S08 And S11

| Section | What it owns |
| --- | --- |
| `S02` Treatments | **What is done** — the treatments on offer |
| `S08` Treatment Process | **The order** it happens in |
| `S09` Technology Products | **What it is done with**, and how those things are chosen and kept |
| `S11` Pricing | Anything with a figure attached |

    "Deep cleansing facial" is S02. "Then the treatment begins" is S08.
    "A steamer, and hand tools cleaned between every guest" is S09.

# The Equipment And Product Set

Used consistently across the batch so the five studies read as one section.

| Equipment | Stated as |
| --- | --- |
| The couch | Heated, and adjusted to you before anything starts |
| The steamer | Used before cleansing, at a temperature you agree to |
| Hand tools | Cleaned and sterilised between every guest, without exception |
| Warm stones | Heated in water and tested on our own wrist first |

| Product category | Stated as |
| --- | --- |
| Cleansers · Oils · Masks · Exfoliants | Chosen in the room for the skin in front of us, and every label can be read on request |

# Out Of Scope

- A global site header, primary navigation or footer
- Treatments, which belong to S02
- The order of a visit, which belongs to S08
- Retail prices and product sales, which belong to S11
- Practitioners, which belong to S04

# Authoring Questions

**1. What is the primary visual element of this role?**

Objects. This is the one section in the sector whose subject is things rather than people or
spaces, so the compositions reserve object-scale media — a trolley, a set of tools, a shelf — and
a row of partner marks where a real page would carry them.

**2. What must a visitor understand immediately?**

That the equipment is looked after, that the products are chosen for them rather than sold to
them, and that they can ask to see any of it.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V2.md (design layer, current) · ./BATCH-V1.md (original authoring record)
