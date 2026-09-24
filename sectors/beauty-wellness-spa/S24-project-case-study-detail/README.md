# Section ID

WELL-S24

# Section Name

Treatment Programme Case Context Detail

# Section Role

S24 — Project / Case Study Detail

Universal Extended Site Architecture (S21–S27). The role is canonical across all
twenty sectors; the section name above is this sector's own term for it.

# Sector

Beauty, Wellness & Spa

# Prefix

WELL

# Purpose

The detail page for one body of work, presented as evidence of how the organisation actually works.

# Visitor Intent

The visitor is assessing capability. They want to see one piece of work in depth: the situation, what was done, and what it produced.

# Content Responsibility

One piece of work in full: context, approach, what was delivered, and the people or services involved.

# In Scope

- The context or brief the work responded to
- The approach taken and the decisions that shaped it
- What was delivered, and at what stages
- Supporting media presented as a documented set
- Links to the services and people involved
- Factual metadata such as scope, location or discipline

# Out Of Scope

- An index or gallery of all work, which belongs to the sector core sections
- A commerce or product detail template, which is out of S21 to S27 scope
- Fabricated clients, outcomes, figures or testimonials
- Any claim the sector's confidentiality or regulatory position does not permit

# Sector Semantic Limitation

Results imagery and outcome claims are regulated in this sector. Scoped to anonymised programme context, never to identifiable client results.

The role is retained in the scaffold rather than removed. A documented limitation is
useful research information; a deleted role is not.

# The Governing Constraint — A Case Study Is An Outcome Claim By Construction

This is the hardest section in the sector, and the difficulty is structural rather than stylistic.
**The canonical role asks for "what it produced". This sector may not say.** Results imagery and
outcome claims are regulated, `S05` already forbade before-and-after evidence, and `S10` forbade
inventing a client. Take those away from a case study and, on the face of it, nothing is left.

Something is left, and it is more interesting than the thing that was removed:

    The page cannot document a result. So it documents a method.
    Not "here is what we achieved" — "here is how a programme is agreed, run, and stopped."

That is a genuine account of capability, it is what the canonical role actually asks for under
*"the approach taken and the decisions that shaped it"*, and every word of it is authorable, because
it describes the studio's own practice rather than somebody's face.

| Element | Treatment |
| --- | --- |
| The person | **Reserved token** — `Guest 01`, on the `S10` rule |
| What they came in for | **Reserved area** — their words, not ours |
| Anything they said | **Reserved area** — the `S10` rule: the structure is authored, the quotation is reserved |
| Dates, reference | **Reserved fields** |
| The method — how it is agreed, revised, reviewed, ended | **Real**, and it is the whole page |
| A result, an improvement, a change | **Forbidden** |
| Before-and-after imagery | **Forbidden** — `S05`, and the sector limitation above |
| Number of visits | **Omitted, not reserved** — see below |
| Duration, price, satisfaction, success rate | **Omitted** |

**Why the number of visits is omitted rather than reserved.** A reserved *"visits: —"* asserts that
programmes have a fixed length. They do not; the number is decided per person and changed when it
needs changing. An empty field that asserts a system the studio does not run is the `S10` empty-star
failure and the `S17` empty-expiry failure. The batch takes the opposite position and states it:
**how many visits is decided with you, and revised.**

# The Canonical Interaction Note, Overridden

The scaffold's Interaction Notes say: *"Galleries, before/after comparisons and stage navigation are
all plausible."*

**In this sector, before/after comparison is not plausible — it is forbidden.** Recorded here rather
than silently ignored, because the conflict between a canonical role and a sector limitation is
exactly the research information this workspace exists to capture. Galleries and stage navigation
survive; the comparison does not.

# The Media Problem, And This Batch's Answer

The scaffold says media is **central** to this role — *"usually the largest documented media set in
the catalogue"*. The one media set this role would normally carry is the one the sector forbids.

The answer taken here: **the documented set is of the programme, not of the person.** The room, the
paper record, the products used, hands, the aftercare sheet. And in `005`, every reserved slot
**carries its own rule about what may and may not go in it** — which turns the sector's limitation
from a subtraction into the design of the page.

**No slot in this batch may hold an identifiable person, a face, or a comparison of two states.**

# What Is Real

1. **How a programme is agreed.** A conversation, then a plan written down that you keep.
2. **That nothing is sold up front.** You pay per visit, and stopping costs nothing.
3. **That the plan changes.** It is revised more often than it is followed to the letter.
4. **How we decide it is not working, and what happens then.** The strongest content on the page,
   because no case study prints it and every honest studio has the conversation.
5. **What is recorded, and what is not.** Notes for whoever treats you; no photographs of you unless
   you ask for them, and you can withdraw that at any point.

**Not present in any study:** an invented client name, quotation, testimonial or photograph; a
before-and-after; an outcome, improvement or efficacy claim; a success rate, satisfaction figure or
count of visits, weeks or sessions; a price or duration; a named medical condition presented as
treated; an invented practitioner name.

# Boundary With S12, S13 And S23

| Section | What it owns |
| --- | --- |
| `S12` Memberships & Packages | **The commercial shape** of buying more than one visit |
| `S13` Gallery | **The picture set**, with no narrative |
| `S23` Treatment Detail | **One treatment**, in full |
| `S24` Programme Case Context | **One programme over time** — how it was agreed, run and ended |

    S23 is one appointment. S24 is a series of them, and the decisions between.

# Media Relationship

Central. This role usually carries the largest documented media set in the catalogue, and the batch document must record each slot's purpose, expected type and fallback.

# Interaction Notes

Optional. Galleries, before/after comparisons and stage navigation are all plausible, and each must remain fully readable without script.

Before/after comparison is removed for this sector, as recorded above. `003` uses native
`<details>` only.

# Responsive Considerations

A long case narrative interleaved with media is the hardest thing here to keep coherent. Reading order must survive every reflow, and no media set may become a horizontal scroll without a label and a keyboard route.

No study in this batch uses a horizontal media scroll. Every set reflows as a grid, so reading order
survives without a scroll affordance being needed at all.

# Related Sections

This is the depth page behind one entry in the sector's work index. Product, property, vehicle and room templates are explicitly not this role.

Nearest existing section in this sector: S13 Gallery (`S13-gallery/`).

# Planned Studies

WELL-S24-001
WELL-S24-002
WELL-S24-003
WELL-S24-004
WELL-S24-005

# Expected Structural Diversity

| Variant | Territory |
| --- | --- |
| `WELL-S24-001` | Universal / Safe |
| `WELL-S24-002` | Premium / Editorial |
| `WELL-S24-003` | Dense / Information-heavy |
| `WELL-S24-004` | Conversion-led |
| `WELL-S24-005` | Sector-native / Distinctive |

These are authoring and research directions, not production enums. The five studies must
differ structurally. They must not become five colour schemes, five font themes, five
cosmetic variants, or five copies of one grid with the content swapped.

# Section Shell

Section only. No global header, logo, primary navigation, announcement bar or footer. The page title
belongs to `S21`; headings here start at `<h2>`, as in `S23`.

# Status

RE-AUTHORED — V2 DETAILING PASS — PENDING DESIGN LAB INGESTION

# Raw Path

./raw/

# Batch Document

./BATCH-V2.md (design layer, current) · ./BATCH-V1.md (original authoring record)
