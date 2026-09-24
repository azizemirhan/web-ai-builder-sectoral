# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S27
- Section Name: Office / Service Location Detail
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 135 studies; S01-S27 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S27-001 | Universal / Safe | Sunlit | B | Contact rail beside a photograph with paired information below |
| ENG-S27-002 | Premium / Editorial | Terracotta | B | Contact row, panoramic photograph and narrow narrative |
| ENG-S27-003 | Structured / Visual Modular | Tidal | B | Teal contacts and supporting photograph beside visit information |
| ENG-S27-004 | Conversion-led | Daybreak | B | Blue contact panel above narrative and a tall location photograph |
| ENG-S27-005 | Art-directed / Distinctive | Night Current | B | Dark identity, lime contact ribbon and offset location narrative |

Visible copy: 156 words per study. All location information is always visible.

## Research Metadata and Scope

Sources: user continuation request, section README, existing theme contract and
repository media policy. Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

Each study covers exactly one physical location: address, local contact details,
opening context, available services, local team, arrival and visit arrangements.
Names, addresses, phone numbers, email addresses, hours and all location-specific
claims are explicit placeholders. No coordinates, directions, accessibility claims,
reviews or staff presence are invented. Verified local relationships are required
before linking actual people or services. No fabricated maps or embedded providers.

## Media

One approved location photograph per study; five reserved slots total. Expected
type: a real photograph of this location and its entrance. Purpose: recognition on
arrival. The visible caption and accessible label describe the reserved subject.
Before ingestion, supply licensing, provenance and final descriptive alternative
text. Fallback: retain the labelled allocated region; all contact and arrival
information remains understandable without imagery. No map slot is necessary for
these compositions; verified written arrival information has a dedicated section.

## Interaction and Responsive Decisions

One labelled section has an H2 and a named article with four H3 information groups.
A named contact group uses a definition list with an address element. Reserved
phone and email fields are plain text rather than nonfunctional call or mail links.
No raw scripts, external dependencies, hidden content or pretend controls.
Production phone, email and directions routes require supplied location details.

Contacts precede the photograph in DOM order and appear above it at tablet and
phone widths. Desktop layouts vary contact emphasis, photo proportions and the
arrangement of the narrative. Scoped CSS provides readable measures, border-box
descendants, responsive wrapping and reduced-motion treatment. S25-S27 use shape B.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- Identity metadata, heading structure, unique IDs, media count and word budget
  checked. Four contact fields and the address element verified.
- No document or element overflow. Contact-before-media order passed at small widths.
- No fabricated interactive controls; all location content remains visible.
- Five desktop and five phone screenshots visually reviewed.
- Gallery frame count, filtering, mobile width, pressed states, full-size links and
  restoration passed. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five location layouts](../../../review/energy-location-detail.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-location-detail.ps1

Measured heights: ../../../review/energy-location-detail-heights.json.
All 27 planned energy sections are authored. No additional energy section is scheduled.
