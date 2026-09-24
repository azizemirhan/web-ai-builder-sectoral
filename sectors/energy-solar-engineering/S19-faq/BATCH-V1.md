# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S19
- Section Name: FAQ
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 95 studies; S01-S19 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S19-001 | Universal / Safe | Sunlit | C | Open introduction beside a warm accordion panel |
| ENG-S19-002 | Premium / Editorial | Terracotta | C | Editorial introduction above two columns of divided questions |
| ENG-S19-003 | Structured / Visual Modular | Tidal | C | Teal FAQ panel with pale question surfaces |
| ENG-S19-004 | Conversion-led | Daybreak | C | Wide blue FAQ stage with a side heading |
| ENG-S19-005 | Art-directed / Distinctive | Night Current | C | Oversized dark statement and offset lime question rows |

Closed copy is 104 words; opening the first answer increases it to 125 words.
All six answers together remain within the 250-word ceiling.

## Research Metadata and Scope

Sources: user continuation request, section README, sector brief, theme contract,
preceding S17 and S18 studies, authoring standard and media policy.
Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE. Media mode: NONE.

Six questions cover enquiry preparation, site suitability, service coverage,
quotation scope, scheduling and post-handover support. The first answer gives
general enquiry preparation guidance. The remaining answers reserve approved
business-specific information. No locations, prices, timelines, warranty terms,
assessment availability or support commitments are invented. Replace reserved
answers with verified business information before publication.

## Interaction and Responsive Decisions

Six native details/summary controls work independently; multiple answers may
remain open. No scripts, dead links, remote dependencies, forms or global
navigation are introduced. Each section has an H2 and one labelled FAQ article
with an H3. Questions provide the disclosure names without redundant ARIA state.
The decorative plus is hidden from assistive technology.

Five fixed themes use different question grouping and emphasis. At 850px all
layouts become one column and preserve document order. Answers expand in normal
flow. Scoped CSS includes border-box descendants, visible focus, reduced-motion
treatment and controls at least 64px tall. S17 was B; S18 and S19 use C.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- No document or element overflow when closed, first-open or all-open.
- Identity metadata, unique IDs, labelled headings and six disclosures checked.
- Every disclosure opens, closes, accepts focus and meets target height.
- Five desktop and five phone screenshots visually reviewed.
- Initial copy meets the ordinary-content target; all-open copy is below 250 words.
- Gallery passed frame count, filtering, mobile width, pressed states, full-size
  links and restoration. Live sizing follows content changes where permitted;
  measured initial heights support local-file previews otherwise.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five FAQ layouts](../../../review/energy-faq.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-faq.ps1

Measured heights: ../../../review/energy-faq-heights.json.
Next: S20-contact-final-cta.
