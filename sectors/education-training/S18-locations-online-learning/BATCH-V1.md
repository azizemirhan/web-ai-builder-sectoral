# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S18
- Section Name: Locations Online Learning
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 90 studies, S01-S18 authored.

## Planned Studies

All five studies are AUTHORED, shape A, each with one reserved campus photograph.
Each contains 121 visible words closed and 138 with both disclosures expanded.

| Study | Direction | Theme | Composition |
| --- | --- | --- | --- |
| EDU-S18-001 | Universal / Safe | Apricot | Paired campus and online options with a broad campus photograph |
| EDU-S18-002 | Premium / Editorial | Mulberry | Editorial campus feature above an open online-learning band |
| EDU-S18-003 | Structured / Visual Modular | Cobalt | Side introduction beside connected learning-mode summaries |
| EDU-S18-004 | Conversion-led | Iris | Campus image alongside a prominent online participation panel |
| EDU-S18-005 | Art-directed / Distinctive | Afterhours | Asymmetric campus photograph and lime online-learning field |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding S16/S17 studies and batch records;
../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Two learning-mode examples demonstrate each layout: one campus and one online option.
Campus name, address, programmes, attendance, teaching period, transport, access,
visit arrangements and contact remain explicit placeholders. Online option,
programme availability, in-person requirements, format, schedule, time zone, platform,
device, connection, accessibility, recordings, assessment and support are also reserved.

No institution-specific delivery information was supplied. A visible notice identifies
locations and options as awaiting confirmation. The closing note explains that modes
vary by programme. No fabricated address, map, platform UI, visit booking, login or
course availability claim. The catalogue link reaches the matching existing S02 review
study. Confirm actual delivery options and destinations before publication.

## Responsive and Interaction Decisions

- 001: paired warm campus and online panels, with a broad image over campus information.
- 002: editorial campus image beside context, above a separate online information band.
- 003: side introduction beside connected campus and online modules; narrow screens
  put introductory context first.
- 004: campus image and context beside a purple online panel with a prominent disclosure.
- 005: asymmetric curved campus image beside an offset lime online panel.

Narrow screens stack options and remove desktop offsets. Phone campus images use
260px height; facts stack vertically. Both disclosures can remain open together.

Each study contains one section H2, two article H3s, two definition lists with four
facts total, two native details and one matching programme link. Visible keyboard
focus, 44px minimum controls and reduced-motion treatment are included.

S16: C / C / C / C / C. S17: B / B / C / C / B.
S18: A / A / A / A / A, starting a new item-comparison run.
Manual comparison used; the CONS-specific checker does not validate education studies.

## Dependency Check

- Framework, CDN and remote runtime dependencies: NONE.
- Raw JavaScript: NONE.
- Gallery JavaScript: local filters, preview widths and iframe height handling.

## Media Slots

Five total: one reserved campus learning-environment photograph per study.
Each has a visible caption and accessible reserved-image description. Supply a
photograph of the actual location with suitable permission and descriptive alt text.
No fictional campus or fabricated online platform screenshot. Without an image, the
reserved slot remains visible and campus/online information remains understandable.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with disclosures closed or both open.
- Metadata, unique IDs, section heading, two options, four facts and one media slot checked.
- Both native disclosures open and close; keyboard focus and minimum target heights checked.
- Matching S02 destinations exist.
- Five desktop and five 390px screenshots visually reviewed.
- Expanded copy remains below the 250-word limit.
- Scoped CSS and theme variables, border-box sizing and reduced-motion treatment included.
- No raw scripts, frameworks, remote dependencies or global shell.
- Gallery passed: five frames, filtering, mobile width, pressed states, full-size links
  and restoration of all previews.
- Cached heights reserve expanded content when local-file access prevents live sizing.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five location designs](../../../review/education-locations.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-locations.ps1

Measured heights: ../../../review/education-locations-heights.json.
Next: S19-contact-admissions.

