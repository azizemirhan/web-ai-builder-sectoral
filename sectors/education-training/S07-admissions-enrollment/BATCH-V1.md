# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S07
- Section Name: Admissions Enrollment
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 35 studies, S01-S07 authored.

## Planned Studies

All five studies are AUTHORED. Each raw filename matches its study ID.

| Study | Direction | Theme | Shape | Media | Words closed / expanded | Composition |
| --- | --- | --- | --- | ---: | --- | --- |
| EDU-S07-001 | Universal / Safe | Apricot | C | 0 | 109 / 126 | Three open steps above a warm preparation panel |
| EDU-S07-002 | Premium / Editorial | Mulberry | B | 1 | 112 / 129 | Editorial introduction and image beside admission information |
| EDU-S07-003 | Structured / Visual Modular | Cobalt | C | 0 | 109 / 126 | Large numbered steps beside a compact preparation panel |
| EDU-S07-004 | Conversion-led | Iris | C | 0 | 109 / 126 | Purple programme-selection callout beside preparation steps |
| EDU-S07-005 | Art-directed / Distinctive | Afterhours | B | 1 | 112 / 129 | Dark sequence beside an offset curved learning-space image |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding S05 and S06 raw/batch records;
../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Three steps introduce programme choice, requirements and the application route.
Two disclosures reserve dates/availability and fees/practical details. Actual
entry requirements, documents, application channel, review process, enrolment steps,
intake dates, availability, fees, payment terms and support contact remain explicit
bracketed placeholders with data-placeholder markers. The guide is labelled illustrative.
No application process or institution data was supplied.

There is no invented deadline, acceptance promise, seat count, payment action or
application confirmation. The only navigation is a truthful programme-selection
link to the matching existing S02 raw study. No form collects personal information.
Production application and admissions-support routes require confirmed destinations.

The designs differ through sequence orientation, grouping, image placement and
prominence of the selection route. They use concise copy and modern web layouts,
without technical paperwork or classical academic decoration.

## Responsive and Interaction Decisions

- 001: three open steps lead a wide preparation panel; phones stack steps and the panel CTA.
- 002: the introduction and image accompany a second information column; phones
  show introductory content, image, steps and preparation in that order.
- 003: large numbered steps sit beside a white information panel; phones stack
  the two areas while retaining padding inside the panel.
- 004: a purple programme-selection callout leads a separate step and preparation column.
  On phones, the callout is followed by the complete sequence.
- 005: a dark sequence accompanies a curved image; phones place the image last.

Native details/summary disclosures open independently and can stay open together.
Plus indicators rotate on expansion. Three steps use an ordered list and H3 headings.
Controls include visible focus treatment and at least 44px target height.

S05 shapes: A / A / A / A / A. S06: C / B / C / C / B.
S07: C / B / C / C / B. No consecutive A run exists. The media-free designs
use open typographic sequences rather than repeated media cards.
Manual comparison used; the CONS-specific checker does not validate education.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- Raw JavaScript: NONE; native disclosures provide interaction.
- Gallery JavaScript: local variant selection, preview widths and frame height handling.

## Media Slots

| Study | Slot | Purpose / expected type | Accessibility / fallback |
| --- | --- | --- | --- |
| 001 | None | Open steps and preparation panel carry the design | No media required |
| 002 | Welcoming learning space | Verified photograph of the actual learning environment | Labelled reserved figure with accessible description |
| 003 | None | Numbered steps and preparation panel carry the design | No media required |
| 004 | None | Coloured selection callout and preparation content carry the design | No media required |
| 005 | Welcoming learning space | Verified photograph of the actual learning environment | Labelled reserved figure with accessible description |

Two reserved photo areas total. Empty slots are intentional. Actual media requires
provenance, permission and accurate alternative text. No generated faces or remote assets.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with both disclosures closed or open.
- Metadata, unique IDs, section region, H2 and three ordered steps checked.
- Native disclosures open and close; focusability and minimum control height checked.
- Matching S02 catalogue destinations exist.
- All five desktop and 390px screenshots visually reviewed.
- Expanded copy: 126-129 words.
- Scoped CSS, border-box sizing and reduced-motion treatment included.
- No raw scripts, frameworks, remote dependencies, forms or global shell.
- Gallery passed: five frames, variant filtering, mobile width, pressed states,
  full-size links and restoration of all previews.
- Cached heights reserve expanded content when local-file access prevents live sizing.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five admissions designs](../../../review/education-admissions.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-admissions.ps1

Measured heights: ../../../review/education-admissions-heights.json.
Next: S08-school-stats.
