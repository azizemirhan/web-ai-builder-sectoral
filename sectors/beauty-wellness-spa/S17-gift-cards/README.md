# Section ID

WELL-S17

# Section Name

Gift Cards

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Planned Studies

WELL-S17-001
WELL-S17-002
WELL-S17-003
WELL-S17-004
WELL-S17-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `WELL-S17-001` | Universal / Safe |
| `WELL-S17-002` | Premium / Editorial |
| `WELL-S17-003` | Structured / Visual Modular |
| `WELL-S17-004` | Conversion-led |
| `WELL-S17-005` | Art-directed / Distinctive |

These are the current authoring directions from `../../../standards/01-AUTHORING-STANDARD.md`,
read for this sector in `../WELLNESS-DESIGN-DIRECTION.md`. They are research directions, not
production enums, and the study IDs do not change with them.

# Section Role

Buying for someone else. The section sets out how a gift is bought here, what form it takes, and
how it behaves once the other person has it.

It answers: *can I give this to someone without it being awkward?*

# The Governing Constraint

The `S11` field-versus-figure test applies unchanged, and this section adds one term the test does
not cover.

| Element | Treatment |
| --- | --- |
| Gift amount | **Reserved field** — a gift card has an amount by definition, so the empty field asserts nothing |
| Card artwork | **Reserved media area** |
| Recipient name, message | **Reserved form fields**, collected from the buyer |
| Denomination tiers | **Omitted** — a set of fixed amounts is a set of invented figures |
| An expiry period | **Omitted entirely** — see below |
| Delivery time | **Omitted entirely** — a placeholder cannot know how fast anything arrives |

**Why an expiry period is omitted rather than reserved.** A reserved *"valid for —"* field asserts
that the card expires at all, which is a commercial policy many studios deliberately do not have —
the same failure as `S10`'s empty star row and `S12`'s empty saving. The batch takes the opposite
position and states it: **the card does not expire**, which is an operating commitment the studio
controls, in the same family as `S12`'s *sessions do not expire*.

**Not present in any study:** an invented amount, denomination, currency symbol, figure, expiry
date or period, delivery time, postage cost, booking fee, discount or bonus-credit offer; a
"most popular" or "best value" tier.

# What Is Real — The Awkward Bits

A gift card section normally sells warmth. What a buyer is actually anxious about is narrower and
more practical, and all of it is answerable with operating commitments rather than claims:

| The worry | The commitment |
| --- | --- |
| They will see what I spent | **The amount is not printed on the card** |
| It will run out and they will have to top it up awkwardly | Whatever is left stays on it |
| It will expire before they get round to it | It does not expire |
| They will feel obliged to have the thing I chose | It can be spent on anything, or put toward something dearer |
| It will arrive as a bare code with no thought in it | The message is written by the buyer and reproduced as written |

**The first one is the section's strongest content and the one most sites get wrong.** Printing the
value on a gift card turns a present into a receipt. Saying plainly that it is not printed is
differentiating, costs the studio nothing, and is exactly the kind of thing a placeholder can state
honestly.

# The Forms

Three structural choices, all generic commercial forms rather than invented products:

| Choice | Options |
| --- | --- |
| How it arrives | A printed card, handed over — or a digital one, sent by email |
| What it is for | An amount to spend on anything — or a named treatment from `S02` |
| What comes with it | A message written by the buyer |

# Boundary With S11 And S12

| Section | What it owns |
| --- | --- |
| `S11` Pricing | What **one treatment** costs, for yourself |
| `S12` Memberships Packages | Buying **more than one**, for yourself |
| `S17` Gift Cards | Buying **for someone else** |

    One facial is S11. Six of them for yourself is S12. One for your sister is S17.

# Out Of Scope

- A global site header, primary navigation or footer
- Prices and packages for the buyer's own use, which belong to S11 and S12
- The booking form, which belongs to S06
- Denomination tiers, in any study
- Delivery timing, in any study

# Authoring Questions

**1. What is the primary visual element of this role?**

The card as an object. This is the only section in the sector whose subject is a physical thing the
visitor will hold or send, so the compositions reserve it at object scale and treat it as a
designed artefact rather than as a product thumbnail.

**2. What must a visitor understand immediately?**

That giving one will not be embarrassing — for them or for the person receiving it.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

AUTHORED — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V1.md
