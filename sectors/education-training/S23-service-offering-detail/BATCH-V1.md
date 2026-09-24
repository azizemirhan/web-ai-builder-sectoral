# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S23
- Section Name: Student Service / Programme Support Detail
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 115 studies, S01-S23 authored.

## Studies

All five studies are AUTHORED. Each contains 166 visible words, shape C, no media.

| Study | Direction | Theme | Composition |
| --- | --- | --- | --- |
| EDU-S23-001 | Universal / Safe | Apricot | Warm service introduction beside a rounded preparation guide |
| EDU-S23-002 | Premium / Editorial | Mulberry | Editorial service overview above a three-part open detail row |
| EDU-S23-003 | Structured / Visual Modular | Cobalt | Blue service summary alongside grouped scope and delivery modules |
| EDU-S23-004 | Conversion-led | Iris | Service detail with a prominent enquiry rail |
| EDU-S23-005 | Art-directed / Distinctive | Afterhours | Oversized dark introduction above a curved lime preparation band |

## Research Metadata and Scope

Sources: user continuation request; section README; sector theme contract;
sector brief; authoring standard; existing S21/S22 studies and S19 contact route.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE. Runtime dependencies: NONE.

Admissions guidance is the single student service represented. The scope follows
the sector limitation: this is support around a programme, not a course detail or
curriculum template. Copy describes possible questions and preparation without
inventing institutional eligibility, charges, availability or outcomes.

Four reserved fields identify applicant eligibility, included support and fees,
delivery and booking, and follow-up. Replace these with verified institution facts
before publication. The contact link reaches the matching S19 raw study; this is a
local review handoff, not a working enquiry submission or automatic service selection.
The visitor is prompted to mention admissions guidance and their programme.

## Responsive and Interaction Decisions

001 uses an open introduction and scope beside a warm preparation panel. 002 moves
from a wide editorial introduction into three open content columns. 003 groups
the service summary, scope and preparation in distinct colour fields. 004 keeps
the enquiry route in a prominent purple rail beside the detailed body. 005 combines
oversized type with a curved lime preparation panel and a full-width contact row.

All columns return to normal flow below 800px, preserving introduction, scope,
preparation and enquiry order. Body measure stays controlled. Phone controls use
available width. There are no sticky panels or hidden body details.

Each study has one labelled section and H2, H3 content groups, an ordered three-step
preparation list and two semantic definition-list facts. The single link has visible
keyboard focus and at least 44px target height. CSS is scoped with explicit
border-box sizing and reduced-motion treatment. No raw scripts or external assets.

S21: B / B / C / C / B. S22: C / C / C / C / C. S23: C / C / C / C / C.
Media is optional for this role; these studies explore complete text-led service
details. No item index or decorative professional document metaphor is introduced.

## QA

- Passed 20 Chrome checks: five variants at 1440, 768, 390 and 320px.
- No document or element overflow; metadata, unique IDs and heading checked.
- Service groups, preparation steps, keyboard focus and target height checked.
- All five matching S19 contact destinations exist.
- Five desktop and five phone screenshots visually reviewed; mobile divider
  curvature corrected after review.
- All studies fit the 150-230-word detail target.
- Gallery passed filtering, five frames, mobile width, pressed states, full-size
  links and restore-all checks. Measured heights support local-file viewing.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five service details](../../../review/education-service-detail.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-service-detail.ps1

Measured heights: ../../../review/education-service-detail-heights.json.
Next: S24-project-case-study-detail.
