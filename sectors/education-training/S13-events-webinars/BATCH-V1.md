# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S13
- Section Name: Events Webinars
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 65 studies, S01-S13 authored.

## Planned Studies

All five studies are AUTHORED, shape A, with no media slots.
Each contains 145 visible words closed and 178 expanded.

| Study | Direction | Theme | Composition |
| --- | --- | --- | --- |
| EDU-S13-001 | Universal / Safe | Apricot | Three warm event cards with clear joining details |
| EDU-S13-002 | Premium / Editorial | Mulberry | Stepped editorial event rows with generous typography |
| EDU-S13-003 | Structured / Visual Modular | Cobalt | Side introduction beside compact modular event summaries |
| EDU-S13-004 | Conversion-led | Iris | Featured session with prominent joining disclosure |
| EDU-S13-005 | Art-directed / Distinctive | Afterhours | Staggered dark event cards with a lime focal point |

## Research Metadata and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; preceding S11/S12 studies and batch records;
../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md;
../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Three reserved sessions demonstrate each layout. Session titles, formats, topics,
audiences, dates, times, time zones, venues/platforms, hosts, durations, costs,
registration requirements, accessibility support and recording availability remain
bracketed placeholders with data-placeholder markers. No event facts were supplied.

A visible notice identifies the programme as a preview awaiting confirmation.
No fabricated event, date, live status, seat count, host identity or registration
link. Placeholder dates are plain text without invented machine-readable dates.
The joining disclosure reveals reserved participation information, without implying
registration has occurred. One matching S02 catalogue link is an existing review
destination. Confirm event data and supply actual registration URLs before publication.

## Responsive and Interaction Decisions

- 001: equal rounded cards below a split heading; tablet and phone stack cards.
- 002: three broad editorial rows with progressive indentation; tablet removes
  indentation, phone stacks date, session and joining details.
- 003: introduction and catalogue link beside compact event modules; narrow screens
  move context above the list and place the date field above session content on phones.
- 004: a large purple featured session beside two compact summaries; narrow screens
  show the featured session first, with its prominent joining disclosure.
- 005: staggered dark cards with a contrasting lime card; narrow screens remove
  offsets and restore a single reading sequence.

Each study contains one section H2, three article H3s, three native joining
disclosures and one programme link. Controls have visible focus treatment and
at least 44px height. Disclosures work without JavaScript. Reduced motion is supported.

S11 shapes: C / C / C / C / C. S12 and S13: A / A / A / A / A.
S14 must break this two-section A run for every variant.
Manual comparison used; the CONS-specific checker does not validate education studies.

## Dependency Check

- Framework, CDN and remote runtime dependencies: NONE.
- Raw JavaScript: NONE; native details provide interaction.
- Gallery JavaScript: local filters, viewport selection and iframe sizing.

## Media Slots

NONE. Typography, event context and colour communicate the session programme.
No event poster, portrait or institution identity was supplied or fabricated.
These layouts remain understandable without imagery.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with disclosures closed or all open.
- Metadata, unique IDs, section heading, three articles and zero media slots checked.
- Native disclosures open and close; focusability and minimum target heights checked.
- Matching S02 destinations exist.
- Five desktop and five 390px screenshots visually reviewed.
- Expanded copy remains below the 250-word limit.
- Scoped CSS and theme variables, border-box sizing and reduced-motion treatment included.
- No raw scripts, frameworks, remote dependencies or global shell.
- Gallery passed: five frames, filtering, mobile width, pressed states, full-size
  links and restoration of all previews.
- Cached heights reserve expanded content when local-file access prevents live sizing.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five event designs](../../../review/education-events.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-events.ps1

Measured heights: ../../../review/education-events-heights.json.
Next: S14-resources-downloads.

