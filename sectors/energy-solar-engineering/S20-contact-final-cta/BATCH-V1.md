# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S20
- Section Name: Contact Final CTA
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 100 studies; S01-S20 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S20-001 | Universal / Safe | Sunlit | C | Warm closing invitation beside a rounded contact panel |
| ENG-S20-002 | Premium / Editorial | Terracotta | C | Editorial headline above horizontal contact details |
| ENG-S20-003 | Structured / Visual Modular | Tidal | C | Teal contact panel paired with a compact closing statement |
| ENG-S20-004 | Conversion-led | Daybreak | C | Wide blue contact stage beneath a split invitation |
| ENG-S20-005 | Art-directed / Distinctive | Night Current | C | Oversized dark statement above an offset lime panel |

Closed copy is 90 words; expanded copy is 113 words.

## Research Metadata and Scope

Sources: user continuation request, section README, sector brief, theme contract,
preceding S18 and S19 studies, authoring standard and media policy.
Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE. Media mode: NONE.

Contact team name, handled enquiries, email, phone and opening hours remain
explicit placeholders. No contact destinations, response times, costs or service
availability are invented. Replace these fields with verified information before
publication. Telephone and email placeholders are plain text, not fake links.

## Interaction and Responsive Decisions

Prepare your enquiry links to the existing S18 study with the same variant number.
That destination prepares a local summary and does not send a request. Native
Before you get in touch details explains what to prepare and this local behaviour.
No submission, scripts, forms, remote dependencies or global footer are introduced.

Five fixed themes retain distinct contact grouping and placement. Below 850px
the invitation precedes a single-column contact panel. Details expand in normal
flow. Each labelled section has an H2 and one labelled contact article with an H3.
Email, phone and availability use a semantic description list. Scoped CSS includes
border-box descendants, visible focus, reduced-motion treatment and controls at
least 48px tall. All five use shape C.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- No document or element overflow when closed or expanded.
- Identity metadata, unique IDs, labelled headings and disclosure checked.
- Enquiry link matches the corresponding existing S18 file; focus and target checked.
- Every disclosure opens, closes, accepts focus and meets target height.
- Five desktop and five phone screenshots visually reviewed.
- Copy meets the ordinary-content 90-170-word target.
- Gallery passed frame count, filtering, mobile width, pressed states, full-size
  links and restoration. Live sizing follows content changes where permitted;
  measured initial heights support local-file previews otherwise.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five contact layouts](../../../review/energy-contact.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-contact.ps1

Measured heights: ../../../review/energy-contact-heights.json.
Next: S21-subpage-hero.
