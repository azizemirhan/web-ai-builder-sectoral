# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S21
- Section Name: Subpage Hero
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 105 studies; S01-S21 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S21-001 | Universal / Safe | Sunlit | B | Compact introduction beside a rounded site photograph |
| ENG-S21-002 | Premium / Editorial | Terracotta | B | Editorial title above a shallow panoramic photograph |
| ENG-S21-003 | Structured / Visual Modular | Tidal | B | Teal title panel beside a site photograph |
| ENG-S21-004 | Conversion-led | Daybreak | B | Split introduction above a blue-framed photograph |
| ENG-S21-005 | Art-directed / Distinctive | Night Current | B | Large dark title beside an asymmetrical site photograph |

Visible copy is 59 words in every variant.

## Research Metadata and Scope

Sources: user continuation request, section README, sector brief, theme contract,
preceding S19 and S20 studies, authoring standard and media policy.
Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

The example internal page is Solar project planning. The title, category and short
introduction identify the page and its intended scope. This is not the S01 brand
hero or a complete planning article. No project facts, service guarantees, dates,
reading times or qualifications are fabricated. The label and topic line are
contextual text, not breadcrumb navigation; S22 owns that separate role.

## Composition and Media

One site-context photograph is reserved per variant, five total. Supply an approved
image suitable for the planning page, with licensing and provenance recorded and
final descriptive alt text before ingestion. Captions and accessible labels make
the reservation explicit; solid theme fields retain the composition without media.

Five themes retain different title placement, image proportions and colour
treatment. All use shape B after S19 and S20 C. Below 850px title and introduction
precede a reduced photograph; at phone widths media height is 230px. The teal title
panel becomes an open introduction on phones to preserve text width. No links,
forms, scripts or interactive controls are needed. Scoped CSS includes border-box
descendants, reduced-motion treatment and a labelled section H2. Final page-level
heading integration is part of ingestion, not this standalone section study.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- No document or element overflow.
- Identity metadata, unique IDs, labelled heading and one media slot checked.
- Copy meets the 40-90-word hero target.
- Five desktop and five phone screenshots visually reviewed.
- Gallery passed frame count, filtering, mobile width, pressed states, full-size
  links and restoration. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five subpage heroes](../../../review/energy-subpage-hero.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-subpage-hero.ps1

Measured heights: ../../../review/energy-subpage-hero-heights.json.
Next: S22-breadcrumb-context-navigation.
