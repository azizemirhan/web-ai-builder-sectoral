# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S06
- Section Name: Engagement Process
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 30 studies; S01-S06 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S06-001 | Universal / Safe | Ivory & Olive | A | Four open steps connected by a quiet olive line |
| FIN-S06-002 | Premium / Editorial | Rosewood | A | Narrative steps with oversized editorial numbering |
| FIN-S06-003 | Structured / Visual Modular | Lagoon | A | Four rounded process panels in a two by two composition |
| FIN-S06-004 | Conversion-led | Iris | A | Violet preparation panel beside a numbered pathway |
| FIN-S06-005 | Art-directed / Distinctive | Ink & Apricot | A | Dark stepped pairs ending in an apricot agreement panel |

All five raw files are authored. Closed visible copy is 154 words; expanded copy
is 179 words, within the structured-section budget. S05 and S06 are consecutive
A sections; the next same-variant section should use shape B or C.

## Research Metadata and Scope

Sources: user continuation request, section README, preceding finance studies and
FINANCE-THEME-CONTRACT.md. Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

Four proposed stages cover first contact, fit, proposal review and agreed next steps.
The sequence is explicitly an outline, subject to the actual engagement terms.
Contact formats, fees, eligibility checks, service scope, timing, acceptance and
onboarding requirements remain reserved fields. No free consultation, response time,
service availability, automated eligibility result or guaranteed outcome is asserted.
Preparation content reserves confirmed secure channels and accessibility arrangements.

## Media

No media slots. Typography, colour and ordered stages communicate the process.
No financial dashboards, certificates, document imitations or decorative seals.

## Interaction and Responsive Decisions

A labelled section with H2 contains an ordered list of four stages. Each list item
contains an article named by its H3; visual numbers are hidden from assistive
technology to avoid duplicate list numbering. The preparation disclosure is native
HTML details/summary, with no booking, upload, submission or invented destination.

Desktop compositions vary in alignment, column count and emphasis. Mobile restores
one sequential reading order. Scoped CSS includes wrapping, border-box descendants,
visible focus, reduced-motion handling and a summary target at least 48px tall.
The dark composition's desktop offsets are removed on tablet and phone to prevent
adjacent stages overlapping.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- Checked identity metadata, unique IDs, four ordered stages, article-heading pairing,
  absence of media and closed/expanded copy budgets.
- No document or element overflow; tablet and mobile stages do not overlap.
- Native summary focus, target height, opening and closing passed.
- Five desktop and five phone screenshots visually reviewed; checks repeated after
  correcting the dark composition's mobile stage offsets.
- Gallery frame count, filtering, mobile width, pressed states, full-size links and
  restoration passed. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five engagement layouts](../../../review/finance-process.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-process.ps1

Measured heights: ../../../review/finance-process-heights.json.
Next: S07-business-stage-solutions.
