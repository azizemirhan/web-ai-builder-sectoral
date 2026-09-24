# Section ID

WELL-S11

# Section Name

Pricing

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Planned Studies

WELL-S11-001
WELL-S11-002
WELL-S11-003
WELL-S11-004
WELL-S11-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `WELL-S11-001` | Universal / Safe |
| `WELL-S11-002` | Premium / Editorial |
| `WELL-S11-003` | Structured / Visual Modular |
| `WELL-S11-004` | Conversion-led |
| `WELL-S11-005` | Art-directed / Distinctive |

These are the current authoring directions from `../../../standards/01-AUTHORING-STANDARD.md`,
read for this sector in `../WELLNESS-DESIGN-DIRECTION.md`. They are research directions, not
production enums, and the study IDs do not change with them.

# Section Role

What things cost. The section sets out the price of individual treatments and how pricing works
here, so a visitor knows what they will pay before they arrive.

It answers: *what will this cost me, and is that the whole number?*

# The Governing Constraint — And Why It Differs From S10

`S10` established that **a figure cannot be meaningfully reserved**, and omitted star ratings on
that basis. A price is also a figure, so the rule appears to forbid this section outright. It does
not, and the difference is worth stating precisely because it is the distinction that makes the
role authorable.

| | An empty star row | An empty price |
| --- | --- | --- |
| What the empty field asserts | That this studio **runs a rating system** and holds scores in it | Nothing. Every spa charges money. |
| Is the assertion safe? | **No** — the studio may collect no ratings at all | **Yes** — the section exists because prices exist |

So: **the price is reserved, not omitted.** What is forbidden is the *figure*, not the field —
exactly as in `S10`, where the quotation was reserved and the rating was omitted. The test is
whether the empty field itself makes a claim. A price field does not; a rating field does.

**How a price is reserved.** As a **price slot**: an em dash set at the type size the real figure
will occupy, in a quiet tinted chip. That preserves the only design questions this section exists
to answer — how prominent the price is against the treatment name, and how prices compare to each
other down a list — while inventing nothing. Currency is part of what is reserved: **no currency
symbol appears anywhere**, because a symbol would invent a market.

**Not present in any study:** an invented price, figure, range, currency symbol, deposit,
consultation fee, cancellation charge, tax statement, package value, saving, discount, "was/now"
pair, or membership term; a treatment duration or session count; a "most popular" or "best value"
badge, which is a claim about real purchase data the studio has and a placeholder does not.

**Emphasis is allowed; a popularity claim is not.** A study may make one row or tier visually
prominent — that is a composition decision. It may not label it *most popular*, *best value* or
*recommended*, because those assert something about what other people bought.

**What is real here.** The studio's own pricing policy — that the price shown is the price paid,
that nothing is added at the end, that a shorter treatment costs less — is a fact about the
studio, in the same family as the `S07` commitments, the `S09` inspection offer and the `S10`
gathering policy. It is the only unreserved content in the batch.

# The Tariff Question

`../WELLNESS-DESIGN-DIRECTION.md` lists *"tariff sheets and price registers that occupy most of the
layout"* among the sector's anti-patterns. That rule forbids a tariff as a **default styling device
in sections that are not about price**. In `S11` a legible, well-set price list is the role itself,
and refusing to list prices here would be avoiding the section rather than authoring it.

What the anti-pattern still rules out, and what this batch holds to: no dense multi-column rate
matrix, no per-row duration column, no tax or terms column, and no layout in which the figures
crowd out the treatment names. A price list is a list; a rate matrix is paperwork.

# Boundary With S02 And S12

| Section | What it owns |
| --- | --- |
| `S02` Treatments | **What the treatments are** |
| `S11` Pricing | **What an individual treatment costs**, and how pricing works |
| `S12` Memberships Packages | **Bundles** — courses, memberships, gift arrangements |

    "Deep cleansing facial" is S02. What one costs is S11.
    Six of them bought together is S12.

# Out Of Scope

- A global site header, primary navigation or footer
- Packages, courses and memberships, which belong to S12
- Gift cards, which belong to S17
- Treatment descriptions, which belong to S02
- Durations, which the sector does not state anywhere — see `S08`

# Authoring Questions

**1. What is the primary visual element of this role?**

The relationship between a name and a number. Everything in a pricing section is a decision about
how loud the figure is next to what it buys, so the compositions differ mainly in that ratio —
from `002`, where the price is a quiet footnote to an editorial name, to `005`, where the price
slot is the largest element on the page.

**2. What must a visitor understand immediately?**

Roughly what a treatment costs, and that the number shown is the number they will pay.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V2.md (design layer, current) · ./BATCH-V1.md (original authoring record)
