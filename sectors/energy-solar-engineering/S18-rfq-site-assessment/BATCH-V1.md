# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S18
- Section Name: RFQ Site Assessment
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 90 studies; S01-S18 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S18-001 | Universal / Safe | Sunlit | C | Warm enquiry form beside an open introduction |
| ENG-S18-002 | Premium / Editorial | Terracotta | C | Editorial introduction above a wide two-column form |
| ENG-S18-003 | Structured / Visual Modular | Tidal | C | Teal form beside a compact invitation |
| ENG-S18-004 | Conversion-led | Daybreak | C | Wide blue form beneath a split introduction |
| ENG-S18-005 | Art-directed / Distinctive | Night Current | C | Oversized dark invitation and offset lime form |

Initial visible copy is 98 words. The QA sample summary increases it to 114 words;
user-entered content is variable and excluded from the authored copy budget.

## Research Metadata and Scope

Sources: user continuation request, section README, sector brief, theme contract,
preceding S16 and S17 studies, authoring standard and media policy.
Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE. Media mode: NONE.

The section demonstrates enquiry preparation with name, email, site location
and project brief. No assessment availability, response time, price or confirmed
booking is invented. Actual routing, assessment conditions and privacy handling
must be defined for a production submission flow. This batch has no submission
backend and never claims an enquiry was sent.

## Interaction and Responsive Decisions

Prepare enquiry uses native required-field and email validation, then presents
a local summary in a polite live region. Input is rendered as text, not HTML.
Editing any field clears the old summary. No network calls or application storage
are used. The button starts disabled and is enabled after the submit handler is
installed; a noscript message explains the local feature. Form controls have no
name attributes for accidental native serialization. Browser autofill remains
available for name and email.

Five themes use distinct desktop placement and grouping. At 850px forms become
single-column, following the introduction. Controls have explicit labels,
required attributes, minimum 48px heights, visible focus and text length limits.
Textareas resize vertically. Each labelled section has an H2 and a labelled form
with an H3. Scoped CSS includes border-box descendants and reduced-motion treatment.
S16 was A, S17 B and S18 C.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- No document or element overflow before or after summary preparation.
- Identity metadata, unique IDs, headings, four field labels and targets checked.
- Empty fields and invalid email rejected; valid sample prepares the local summary.
- HTML-like input displayed literally; edits clear stale summary content.
- Field and button focus checked; five desktop and five phone screenshots reviewed.
- Gallery passed frame count, filtering, mobile width, pressed states, full-size
  links and restoration. Live sizing follows content changes where permitted;
  measured initial heights support local-file previews otherwise.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five enquiry layouts](../../../review/energy-enquiry.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-enquiry.ps1

Measured heights: ../../../review/energy-enquiry-heights.json.
Next: S19-faq.
