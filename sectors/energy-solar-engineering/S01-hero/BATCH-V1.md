# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S01
- Section Name: Hero
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 5 studies; S01 authored.

## Planned Studies

All five studies are AUTHORED. Visible copy: 54 words in 001/002/003/005 and 49 in
004. Expanded preparation guidance brings these to 77 and 72 respectively.

| Study | Direction | Theme | Shape | Media | Composition |
| --- | --- | --- | --- | --- | --- |
| ENG-S01-001 | Universal / Safe | Sunlit | B | 1 | Split hero with a tall rounded solar photograph |
| ENG-S01-002 | Premium / Editorial | Terracotta | B | 1 | Editorial statement above a panoramic installation image |
| ENG-S01-003 | Structured / Visual Modular | Tidal | B | 1 | Teal content field beside solar media and a scope strip |
| ENG-S01-004 | Conversion-led | Daybreak | C | 0 | Centred blue typographic hero with a project-preparation action |
| ENG-S01-005 | Art-directed / Distinctive | Night Current | B | 1 | Oversized dark statement with an asymmetrical solar photograph |

## Research Metadata

Sources: user sector-start instruction and modern-style preference; section README;
sector brief; ../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md; ../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

This opening establishes solar and engineering context through aspirational copy,
site-related questions and supporting media. No fabricated provider, installed
capacity, savings, ROI, emissions reduction, credential or performance promise.
Three short topic labels identify areas to explore rather than certified services.
The new ../ENERGY-THEME-CONTRACT.md fixes the five palettes for later sections.

Prepare your project brief opens a native details disclosure explaining what to
bring to an initial discussion: site location, usage and priorities. It submits
nothing and collects no data. Later enquiry/solution sections are still unauthored,
so the interaction is complete locally without invented or dead destination links.

## Visual and Responsive Decisions

001 is a balanced split with warm rounded media. 002 places the statement and
action above a broad image. 003 uses separate colour fields for message, image and
scope. 004 makes the preparation action central in a blue type-only composition.
005 combines oversized type with a narrower curved image and deliberate offset.
No technical dashboard or classical design language is used.

All phone layouts place the message and preparation disclosure before media,
then the topic list. Media reduces to 280px; the disclosure control uses available
width. Expanded text stays in normal flow. The gallery observes live height changes
where permitted and uses cached closed-state measurements otherwise.

One labelled section and H2, one native details/summary, three topic list items.
No global shell, heading clutter, forms, fake navigation or raw JavaScript.
Visible focus, 50px control target, scoped CSS, border-box sizing and reduced-motion
treatment included. This is the first section; no previous page-rhythm comparison.

## Media Slots and Dependencies

Four slots: one actual solar-installation photograph in 001, 002, 003 and 005.
Purpose: establish energy and site context. Expected type: an approved photograph
with verified licensing/provenance; do not imply project ownership without evidence.
Each slot carries a visible reserved-image caption and an accessible description.
It retains allocated space without an asset. Replace labels with verified scene
descriptions and final alt text before publication. No AI-generated project evidence.
004 intentionally explores a complete type-and-colour hero without media.

Framework, CDN, remote runtime dependencies and raw JavaScript: NONE.
Gallery JavaScript: preview sizing, filtering and width selection only.

## QA

- Passed 20 Chrome checks: five studies at 1440, 768, 390 and 320px.
- Closed and expanded states have no document or element overflow.
- Identity, metadata, labelled H2, unique IDs, media and scope-item counts checked.
- Native disclosure opens/closes, accepts focus and meets target height.
- All variants meet the 40-90-word hero target, including expanded copy.
- Five desktop and five phone screenshots visually reviewed.
- Gallery passed five frames, filtering, mobile width, pressed states, full-size
  links and restoration. Measured heights support local-file previews.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five energy heroes](../../../review/energy-hero.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-hero.ps1

Measured heights: ../../../review/energy-hero-heights.json.
Next: S02-solutions-services.
