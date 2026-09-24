# Section ID

WELL-S23

# Section Name

Treatment / Wellness Service Detail

# Section Role

S23 — Service / Offering Detail

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Purpose

The detail page for one single offering, presented in enough depth that a visitor can decide whether it is the right one for them.

# Visitor Intent

The visitor has chosen one offering from an index and now wants specifics: what it covers, how it runs, what it involves and what happens next.

# Content Responsibility

One offering in full: what it is, what is included, how it is delivered, who it suits, and the route to enquire about it.

# In Scope

- A description of the single offering the page is about
- What the offering includes and, where useful, what it excludes
- How it is delivered, staged or sequenced
- Who it is for, and the conditions under which it applies
- Related or adjacent offerings
- A route to enquire about this specific offering

# Out Of Scope

- An index or grid of every offering, which belongs to the sector core sections
- Homepage positioning copy
- Fabricated pricing, guarantees, turnaround times or availability
- Any regulated claim the sector does not permit

# The Governing Constraint — Describe The Room, Not The Result

**This is the page in the whole sector where an efficacy claim is most likely to appear.** A
treatment detail page is the natural home of *"reduces fine lines"*, *"boosts circulation"*,
*"detoxifies"*, *"resurfaces"*, *"stimulates collagen"*. Every one of those is an outcome claim, and
`WELLNESS-DESIGN-DIRECTION.md` rules the whole family out.

The rule for this section, stated so it can be applied to any sentence on the page:

    Describe what happens in the room, and who it suits.
    Never describe what it will do to the person.

| Sentence | Verdict |
| --- | --- |
| *"Your face is cleansed twice, then steamed."* | **Real** — it is a description of events |
| *"Warm oil, and pressure firm enough that you will feel it the next day."* | **Real** — a description of the experience |
| *"For anyone who wants a thorough clean rather than something aimed at one concern."* | **Real** — it describes suitability |
| *"Reduces the appearance of fine lines."* | **Forbidden** — an outcome claim |
| *"Detoxifies and rebalances."* | **Forbidden** — an outcome claim and a pseudo-mechanism |
| *"Clinically proven to…"* | **Forbidden** — a regulated claim |

**The useful discovery is that the honest version is not thinner than the claim.** A description of
what happens to you, minute by minute, is more persuasive than a promise about your skin — and it is
completely authorable, because it is a statement about the studio's own practice.

# The Money And Duration Fields — A Refinement Of The S11 Test

| Element | Treatment | Reasoning |
| --- | --- | --- |
| Price | **Reserved field** | The `S11` test: every treatment has a price, so an empty labelled field asserts nothing |
| How long it takes | **Reserved field** | Same test — a single overall duration is a property of the offering, like its price |
| Per-step timings | **Still omitted** | The `S08` rule stands: *a sequence is content, a schedule is a claim*. A timed sequence asserts a protocol the studio may not run |
| Availability, turnaround | **Omitted** | The scaffold rules them out, and an empty *"available from —"* asserts a booking system |
| Guarantee | **Omitted entirely** | A guarantee about a body is a claim no studio should print |

This is a deliberate refinement rather than a reversal: `S08` omitted durations because it was
timing **each stage**. One overall duration on a detail page is a field like any other. Recorded
here so the two sections do not look inconsistent.

# Boundary With S02 And S08

| Section | What it owns |
| --- | --- |
| `S02` Treatments Services | **The set** — every treatment, a name and a line each |
| `S08` Treatment Process | **The studio's process for any visit** — arriving, consultation, aftercare |
| `S23` Treatment Detail | **One treatment in full** — what happens in *this* one |

    S02 is the menu. S08 is how any visit runs. S23 is what this one is.

The sequence in `S23` is the sequence of **this treatment**, not of a visit to the studio. If a
study's steps would read identically on every other treatment page, it has written `S08` by mistake.

# What Is Real On This Page

1. **The description of events.** What is done, in what order, with what.
2. **What is included, and what is not.** *"No extractions unless you ask for them"* is a real,
   checkable statement about practice, and the exclusions reassure more than the inclusions.
3. **Who it suits, and who it does not.** Including the steer away: *"if you want something aimed at
   one particular thing, this is not it — ask us about the others."*
4. **The limits.** A short version of the `S18` line where the page touches skin that is changing or
   sore: that is a doctor's question, not a spa's.
5. **The route to ask about this one.** Tied to this treatment, not to the business.

**Not present in any study:** an efficacy, outcome, ingredient-action or mechanism claim; a named
medical condition presented as treatable; a *clinically proven*, *dermatologist approved* or
*results* statement; a before-and-after; a price, duration or availability figure; a guarantee; a
star rating, review count or testimonial; an invented practitioner name; a per-step timing.

# Media Relationship

Optional and supporting. Media should illustrate the offering rather than carry it, and the page must remain complete when a media slot is empty.

Every media area in this batch is a reserved area, and **no study depends on one**: `003` carries no
media at all, and the four that do would still read with every slot empty.

# Interaction Notes

Usually none. Where an offering has stages or options, disclosure or tab patterns may be justified, but the full content must remain reachable without script.

`003` uses native `<details>`/`<summary>` for the conditions, which needs no script at all.

# Responsive Considerations

Long-form body copy needs a controlled measure at wide widths and must not collapse into a single dense column on small screens. Any supporting rail or sticky element should release to normal flow before it starts competing with the body.

No study uses a sticky rail. Where a rail carries the reserved fields and the action, it releases
into normal flow above or below the body before it starts competing with it.

# Related Sections

This is the depth page behind one entry in the sector's offering index. The index lives in the sector core sections; this page is what one of its entries opens into.

Nearest existing section in this sector: S02 Treatments Services (`S02-treatments-services/`).

# Planned Studies

WELL-S23-001
WELL-S23-002
WELL-S23-003
WELL-S23-004
WELL-S23-005

# Expected Structural Diversity

| Variant | Territory |
| --- | --- |
| `WELL-S23-001` | Universal / Safe |
| `WELL-S23-002` | Premium / Editorial |
| `WELL-S23-003` | Dense / Information-heavy |
| `WELL-S23-004` | Conversion-led |
| `WELL-S23-005` | Sector-native / Distinctive |

These are authoring and research directions, not production enums. The five studies must
differ structurally. They must not become five colour schemes, five font themes, five
cosmetic variants, or five copies of one grid with the content swapped.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer. The page title
belongs to `S21` and the trail to `S22`; this section is the body beneath them.

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V2.md (design layer, current) · ./BATCH-V1.md (original authoring record)
