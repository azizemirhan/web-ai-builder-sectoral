# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S27
- Section Name: Campus / Learning Location Detail
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 135 studies, S01-S27 authored. All planned sections complete.

## Studies

All five studies are AUTHORED. 001, 002 and 005 contain 155 visible words;
003 and 004 contain 150. Each represents one physical learning location.

| Study | Direction | Theme | Shape | Media | Composition |
| --- | --- | --- | --- | --- | --- |
| EDU-S27-001 | Universal / Safe | Apricot | B | 1 | Warm overview with practical details before a supporting photograph |
| EDU-S27-002 | Premium / Editorial | Mulberry | B | 1 | Editorial campus title and arrival facts above a shallow panorama |
| EDU-S27-003 | Structured / Visual Modular | Cobalt | C | 0 | Blue campus identity beside grouped visit and learning information |
| EDU-S27-004 | Conversion-led | Iris | C | 0 | Visit-first campus detail with a prominent admissions handoff |
| EDU-S27-005 | Art-directed / Distinctive | Afterhours | B | 1 | Dark identity with a curved photograph and lime arrival panel |

## Research Metadata and Scope

Sources: user continuation request; S27 README; education theme contract;
preceding S25/S26 studies; existing S19 admissions route; authoring standard and
media policy. Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

All campus-specific facts are reserved: name, description, address, telephone,
email, opening hours, time zone, seasonal exceptions, visitor appointments,
programmes, spaces, services, teams, transport, parking, reception and accessibility.
No address, coordinates, contact number, opening time or directions are fabricated.
No map, third-party embed, location rating or invented review is included.

The location-specific contact field is distinct from the general admissions link.
Contact admissions reaches the matching S19 study as a local review handoff for
course enquiries. It neither contacts a real campus nor books a visit. Replace
reserved fields and routing with verified information during integration.

## Responsive and Interaction Decisions

001 pairs practical facts and supporting media beneath the campus introduction.
002 combines identity and contact facts above a panoramic image. 003 groups
identity, practical facts, learning context and arrival guidance without media.
004 gives visiting facts and the enquiry handoff visual prominence. 005 uses
asymmetry, a curved photograph and a lime arrival panel.

Below 800px, every variant follows the DOM order: identity, address/contact/hours,
optional photo, learning context, arrival and visit planning. Practical information
stays ahead of media, including in 005 where the desktop columns are reversed.
No horizontal scrolling, hidden directions, sticky panels or location switcher.
Phone media height is 250px. The single link uses full phone width and has visible
keyboard focus with at least 44px target height.

Each study contains one labelled section, one H2, four H3 groups and a three-item
definition list. Scoped CSS includes border-box sizing, controlled text measure
and reduced-motion treatment. Raw JavaScript, frameworks and remote dependencies: NONE.

S25: B / B / C / C / B. S26: B / B / C / C / B. S27: B / B / C / C / B.

## Media Slots

Three total, one reserved campus photograph in 001, 002 and 005. Purpose: show the
actual entrance and learning environment of the named location. Expected type:
approved photograph with verified provenance and licensing, plus consent where
needed. Each slot has a visible reserved-image caption and accessible label.
Final alt text and caption must describe the actual image and confirmed entrance.
The allocated space and label remain while the asset is absent. 003 and 004 are
complete without imagery. No fabricated map or scenic substitute is used.

## QA

- Passed 20 Chrome viewport checks: five variants at 1440, 768, 390 and 320px.
- No document or element overflow; heading, section identity and metadata checked.
- Unique IDs, four H3 groups, three practical facts and media counts checked.
- Automated mobile check confirms practical contact information precedes media.
- All five matching S19 destinations exist; links accept focus and meet target height.
- Five desktop and five phone screenshots visually reviewed.
- All variants fit the 150-230-word detail target.
- Gallery passed five frames, filtering, mobile width, pressed states, full-size
  links and restoration. Measured heights support local-file viewing.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review and Sector Completion

[Compare five campus details](../../../review/education-campus-detail.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-campus-detail.ps1

Measured heights: ../../../review/education-campus-detail-heights.json.
All 27 education sections now contain five authored studies each: 135 total.
S28+ remains outside the planned catalogue. No further education section is scheduled.
