# Section ID

WELL-S12

# Section Name

Memberships Packages

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Planned Studies

WELL-S12-001
WELL-S12-002
WELL-S12-003
WELL-S12-004
WELL-S12-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `WELL-S12-001` | Universal / Safe |
| `WELL-S12-002` | Premium / Editorial |
| `WELL-S12-003` | Structured / Visual Modular |
| `WELL-S12-004` | Conversion-led |
| `WELL-S12-005` | Art-directed / Distinctive |

These are the current authoring directions from `../../../standards/01-AUTHORING-STANDARD.md`,
read for this sector in `../WELLNESS-DESIGN-DIRECTION.md`. They are research directions, not
production enums, and the study IDs do not change with them.

# Section Role

Buying more than one visit. The section sets out the ways a guest can commit to a series of
treatments rather than booking each one separately, and how those arrangements behave.

It answers: *if I am going to come back, is there a better way to do it?*

# The Governing Constraint

`S11` established the test: **reserve the field when the empty field asserts nothing; omit it when
the empty field asserts a system.** This section applies that test three times, and adds one
prohibition the test does not cover.

| Element | Test | Treatment |
| --- | --- | --- |
| Package price | A packages section exists because packages have prices | **Reserved slot** |
| Session count | A course by definition bundles a quantity | **Reserved slot** |
| Membership term | A membership by definition has a rhythm | **Reserved slot** |
| A saving or package value | — | **Forbidden outright** |

**Why a saving is forbidden rather than reserved.** A price is one figure. A saving is a
*relationship between two figures* — the bundle price against what the same treatments would cost
separately — and reserving it would reserve a claim, not a number. Worse, an empty "you save —"
field asserts that this studio discounts bundles at all, which is a commercial policy many studios
deliberately do not have. That is the same failure as `S10`'s empty star row.

**Not present in any study:** an invented price, session count, term length, currency symbol,
saving, discount, percentage, package value, "worth" figure, "was/now" pair, joining fee, minimum
term, notice period, or expiry date; a "most popular", "best value" or "recommended" badge; an
auto-renewal claim in either direction stated as a specific term.

**No comparison matrix.** The tick-grid tier table is the default device for this role on the open
web, and it is a specification matrix, which `../WELLNESS-DESIGN-DIRECTION.md` rules out for this
sector. `S11` argued that a price list is the native form of a pricing section and therefore
allowed; that argument does **not** extend here, because a comparison matrix is not the native form
of a membership — it is the native form of software pricing. No study in this batch uses one.

**What is real.** Two things:

1. **The generic commercial forms.** A course of one treatment, a mixed course, and a rolling
   membership are structural arrangements that exist across the whole sector. Naming a form is not
   inventing a product.
2. **How the arrangements behave** — whether sessions expire, whether a membership can be paused,
   whether it can be shared, what happens if you stop. These are operating commitments the studio
   controls, in the same family as `S07`, `S09`, `S10` and `S11`, and they are the only unreserved
   content in the batch. They are written **without numbers**, so no term is invented in the act of
   describing the policy.

# The Three Forms

Used consistently across the batch.

| Form | What it is |
| --- | --- |
| A course | The same treatment, booked as a series and paid for once |
| A mixed course | A set of visits to spend across the menu, decided as you go |
| A membership | One visit on a regular rhythm, running on until you stop it |

# Boundary With S11 And S17

| Section | What it owns |
| --- | --- |
| `S11` Pricing | What **one** treatment costs |
| `S12` Memberships Packages | Buying **more than one** — courses and memberships |
| `S17` Gift Cards | Buying for **someone else** |

    One facial is S11. Six of them bought together is S12.
    One bought as a present is S17.

A gift arrangement is deliberately absent from this batch; it is `S17`'s role.

# Out Of Scope

- A global site header, primary navigation or footer
- Single-treatment prices, which belong to S11
- Gift cards and gift arrangements, which belong to S17
- Treatment descriptions, which belong to S02
- A tier comparison matrix, in any form

# Authoring Questions

**1. What is the primary visual element of this role?**

Rhythm. A course, a mixed course and a membership differ in **how visits are distributed over
time** — bounded and regular, bounded and irregular, unbounded — and that difference is the one
thing a composition can show without stating a number.

**2. What must a visitor understand immediately?**

Which of the three forms fits how they actually want to come back, and what happens if their
circumstances change.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V2.md (design layer, current) · ./BATCH-V1.md (original authoring record)
