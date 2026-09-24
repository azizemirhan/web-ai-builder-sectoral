# Section ID

WELL-S18

# Section Name

Wellness Resources

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Planned Studies

WELL-S18-001
WELL-S18-002
WELL-S18-003
WELL-S18-004
WELL-S18-005

# Expected Structural Diversity

| Variant | Direction |
| --- | --- |
| `WELL-S18-001` | Universal / Safe |
| `WELL-S18-002` | Premium / Editorial |
| `WELL-S18-003` | Structured / Visual Modular |
| `WELL-S18-004` | Conversion-led |
| `WELL-S18-005` | Art-directed / Distinctive |

These are the current authoring directions from `../../../standards/01-AUTHORING-STANDARD.md`,
read for this sector in `../WELLNESS-DESIGN-DIRECTION.md`. They are research directions, not
production enums, and the study IDs do not change with them.

# Section Role

What the studio has written down. The section indexes the aftercare notes, guides and answers the
studio publishes, so a visitor can read before or after a visit.

It answers: *what do they know, and will they tell me without me having to book?*

# The Governing Constraint — Two Problems At Once

**1. An article title is invented content.** Writing *"Five ways to strengthen your skin barrier"*
invents a publication as surely as inventing a treatment product does — and worse, that particular
title is also an efficacy claim. So:

| Element | Treatment |
| --- | --- |
| Article title | **Reserved area**, sized to the title's type scale, as `S10` reserved a quotation |
| Article summary | **Reserved area** where a study shows one |
| Topic category | **Real** — generic sector vocabulary, as in `S03` |
| Kind of resource | **Real** — an aftercare note, a guide, a question answered |
| Publication date | **Reserved field** — a published piece has a date, so the empty field asserts nothing |
| Author | **Reserved token** — `Practitioner 01`, on the `S04` rule |
| Reading time | **Omitted** — a figure a placeholder cannot compute, and the sector prints no durations |

**2. This is the section where the sector's claims rule is most likely to break.** A wellness
resources index is the natural home of *"boost"*, *"detox"*, *"reset your skin"*, *"the truth
about collagen"*. Because every title in this batch is reserved, **no study can carry such a claim
even accidentally** — which is the strongest argument for reserving titles rather than writing
plausible-sounding placeholders.

# What Is Real — Including What The Section Is Not

Three things, and the third is the most important:

1. **The topics and kinds.** Generic, and enough to show how an index sorts itself.
2. **Why the studio publishes.** *"These exist so you do not have to ring us about the same things"*
   — an operating position, and the aftercare notes are given on paper when you leave anyway.
3. **What this is not.** A wellness studio writing about skin and bodies sits next to medical
   advice, and the honest position is to say plainly that **none of this is medical advice, and
   that something changing or worrying on your skin is a doctor's question, not a spa's.**

That third line is the section's most valuable content. It is the sector's clearest liability
point, it is completely authorable because it is a statement about limits rather than a claim, and
it appears in **every study in this batch**.

**Not present in any study:** an invented article title, summary, author name, publication date,
reading time, view count, share count or category count; an efficacy, outcome or ingredient claim;
a diagnostic statement or named medical condition presented as treatable; a "trending", "most read"
or "popular" label, which asserts real traffic data.

# Boundary With S25 And S15

| Section | What it owns |
| --- | --- |
| `S15` FAQ | **Short practical answers** to booking questions |
| `S18` Wellness Resources | **The index** of what the studio has published |
| `S25` Article / Insight Detail | **One piece in full**, on its own page |

    "Will I be sold anything?" is S15. A list of what we have written is S18.
    One of those pieces, read end to end, is S25.

The same set-and-detail pattern as `S02`/`S23`, `S04`/`S26` and `S16`/`S27`.

# Out Of Scope

- A global site header, primary navigation or footer
- One article in full, which belongs to S25
- Booking questions, which belong to S15
- Any medical or diagnostic content
- Traffic figures — views, shares, "most read"

# Authoring Questions

**1. What is the primary visual element of this role?**

The title, which cannot be written. That is the whole design problem: an index is normally carried
by its headlines, and here every headline is a reserved area. So each study has to decide how much
of the composition a reserved title should occupy, and what else carries the section while it is
empty.

**2. What must a visitor understand immediately?**

That there is something worth reading here, how it is sorted, and that it is not medical advice.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer.

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V2.md (design layer, current) · ./BATCH-V1.md (original authoring record)
