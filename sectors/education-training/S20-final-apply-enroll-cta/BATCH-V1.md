# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S20
- Section Name: Final Apply Enroll CTA
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 100 studies, S01-S20 authored; core catalogue complete.

## Planned Studies

All five studies are AUTHORED. Variants 001, 003 and 004 contain 54 visible words;
002 and 005 contain 56, including their media captions.

| Study | Direction | Theme | Shape | Media | Composition |
| --- | --- | --- | --- | --- | --- |
| EDU-S20-001 | Universal / Safe | Apricot | C | 0 | Warm rounded closing banner with actions beside the message |
| EDU-S20-002 | Premium / Editorial | Mulberry | B | 1 | Editorial application invitation beside a learning-space photograph |
| EDU-S20-003 | Structured / Visual Modular | Cobalt | C | 0 | Open invitation above a blue action band |
| EDU-S20-004 | Conversion-led | Iris | C | 0 | Centred purple application invitation with a prominent next step |
| EDU-S20-005 | Art-directed / Distinctive | Afterhours | B | 1 | Oversized dark invitation beside a curved learning-space image |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding S18/S19 batch records; existing S07 admissions
and S02 programme studies; ../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

A short final invitation directs visitors to review application preparation or find
a programme. The primary Review application steps link reaches the matching existing
S07 admissions guide; Find a programme reaches the matching S02 catalogue.
These are local review routes. No actual application endpoint was supplied, and
neither link claims to submit an application or reserve a place.

The note reminds visitors that programme requirements, fees and dates vary. No invented
deadline, scarcity claim, award guarantee, enrolment confirmation, form or payment action.
Replace review routes with verified production destinations when integrating the studies.

## Responsive and Interaction Decisions

- 001: a warm rounded horizontal banner with actions beside the message; phones stack it.
- 002: editorial text and actions beside a broad learning-space photograph; phones place
  the photograph after the actions.
- 003: open introduction above a blue action band; phones stack links inside the band.
- 004: centred purple invitation with a pale primary control and secondary programme route.
- 005: oversized dark typography and lime primary control beside a curved photograph;
  phones put the image below the invitation.

Each study has one section H2 and two real local links. No extra article, heading,
disclosure or global footer. Focus treatment and minimum 44px target heights included.
No raw JavaScript is required.

S18: A / A / A / A / A. S19: B / B / C / C / B.
S20: C / B / C / C / B. Short closing compositions avoid another item grid.
Manual comparison used; the CONS-specific checker does not validate education studies.

## Dependency Check

- Framework, CDN and remote runtime dependencies: NONE.
- Raw JavaScript: NONE.
- Gallery JavaScript: local filters, preview widths and iframe height handling.

## Media Slots

Two total: one reserved learning-environment photograph in 002 and 005. Each has a
visible caption and accessible reserved-image description. Supply a photograph of an
actual learning environment with suitable permission and descriptive alt text before
publication. No fabricated students, graduation outcome or institution identity.
The labelled slot remains reserved without media and both actions remain usable.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow.
- Metadata, unique IDs, accessible H2, two routes and media counts checked.
- Both links accept keyboard focus and have minimum 44px target height.
- Matching S07 and S02 destinations exist.
- Five desktop and five 390px screenshots visually reviewed.
- Every study fits the 40-90-word CTA budget.
- Scoped CSS and theme variables, border-box sizing and reduced-motion treatment included.
- No raw scripts, frameworks, remote dependencies or global shell.
- Gallery passed: five frames, filtering, mobile width, pressed states, full-size links
  and restoration of all previews.
- Measured heights support local-file previews when live sizing is unavailable.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five final CTA designs](../../../review/education-final-cta.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-final-cta.ps1

Measured heights: ../../../review/education-final-cta-heights.json.
Next: S21-subpage-hero.

