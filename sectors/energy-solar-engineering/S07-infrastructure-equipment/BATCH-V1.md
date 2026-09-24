# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S07
- Section Name: Infrastructure Equipment
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 35 studies; S01-S07 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S07-001 | Universal / Safe | Sunlit | B | Tall infrastructure view beside a readiness story and detail crop |
| ENG-S07-002 | Premium / Editorial | Terracotta | B | Panoramic photograph above an editorial narrative and equipment crop |
| ENG-S07-003 | Structured / Visual Modular | Tidal | B | Asymmetric image pair above a full-width readiness panel |
| ENG-S07-004 | Conversion-led | Daybreak | B | Blue readiness panel beside two offset photographs |
| ENG-S07-005 | Art-directed / Distinctive | Night Current | B | Wide sculpted image above an offset lime story |

All five studies are AUTHORED. Each contains two media reservations and a single
native equipment-readiness disclosure. Copy is 103 words closed and 116 expanded.

## Research Metadata and Scope

Sources: user continuation request, section README, sector brief,
../ENERGY-THEME-CONTRACT.md, preceding S05 and S06 studies, authoring standard
and media policy. Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Copy frames site space, access, positioning and maintenance as discussion topics.
It asks visitors to confirm available equipment and infrastructure. No facilities,
fleet, equipment ownership, specifications, capacity or performance are invented.
The disclosure reserves verified infrastructure, availability, requirements and
responsibilities. Supply approved site-specific facts before publication.

Explore equipment readiness opens a native details element. There are no dead
links, fake submissions, global headers or footers, raw scripts or remote runtime
dependencies. This section introduces physical infrastructure context, rather than
repeating the technology-category index from S06.

## Composition and Responsive Decisions

The five themes remain consistent while media scale, narrative placement and
disclosure emphasis vary. All five studies use two anchored media areas, shape B,
breaking the A sequence from S05 and S06. No technical document metaphor is used.

Below 850px, the main photograph, narrative and equipment detail stack in DOM
order. At phone widths the main photograph is 300px tall and the detail is 250px.
Expanded content remains in normal flow. A labelled H2 introduces a labelled
article with an H3. Scoped CSS provides border-box descendants, visible focus,
reduced-motion treatment and controls at least 44px tall.

## Media

Two slots per study, ten total. Site infrastructure should show an approved
physical installation setting; equipment context should show relevant equipment
positioned within its working environment. Neither slot implies provider ownership.
Both have visible subject captions and accessible reserved-image labels. Licensing,
provenance and final descriptive alt text are required before ingestion. Solid
theme-colour fields preserve the intended layout without fabricated evidence.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- No document or element overflow with the disclosure closed or open.
- Metadata, unique IDs, labelled headings, one article and two media slots checked.
- Disclosure opens, closes, accepts focus and meets the minimum target height.
- Five desktop and five phone screenshots visually reviewed.
- Copy meets the ordinary-content 90-170-word target.
- Gallery passed frame count, filtering, mobile width, pressed states, full-size
  links and restoration. Live sizing follows disclosures where permitted;
  measured closed heights support local-file previews otherwise.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five infrastructure layouts](../../../review/energy-infrastructure.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-infrastructure.ps1

Measured heights: ../../../review/energy-infrastructure-heights.json.
Next: S08-engineering-process.
