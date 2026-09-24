# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S14
- Section Name: Case Studies
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 70 studies; S01-S14 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S14-001 | Universal / Safe | Sunlit | B | Large project portrait beside a narrative and supporting photograph |
| ENG-S14-002 | Premium / Editorial | Terracotta | B | Panoramic photograph beneath a split introduction |
| ENG-S14-003 | Structured / Visual Modular | Tidal | B | Paired photographs beside a teal narrative panel |
| ENG-S14-004 | Conversion-led | Daybreak | B | Blue narrative beside a tall photograph above a wide detail strip |
| ENG-S14-005 | Art-directed / Distinctive | Night Current | B | Oversized heading with asymmetric photographs and an offset lime story |

All five studies are AUTHORED. Closed copy is 97 words; expanded copy is 118 words.

## Research Metadata and Scope

Sources: user continuation request, section README, sector brief,
../ENERGY-THEME-CONTRACT.md, preceding section studies, authoring standard
and media policy. Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

Each composition features one case study, framing its challenge, approach and
outcome. Project name, client context, site constraints, delivery decisions and
results remain placeholders. No project ownership, clients, locations, capacities,
savings or performance evidence are fabricated. S04 introduces project work;
S14 foregrounds the decisions and evidence behind a selected case. S24 remains
the separate full project-detail role.

Read the project context opens native details with reserved scope, dates,
measurement methods, sources and publication consent. No dead links, raw scripts,
forms, global navigation or external dependencies are introduced.

## Composition, Media and Responsive Decisions

Two photo reservations per study, ten total: an overview and a detail from the
same featured project. Supply approved real photography with licensing,
provenance and final descriptive alt text before ingestion. Visible subject
captions and accessible placeholder labels identify the reserved fields.
Solid theme backgrounds maintain the layout while approved media is unavailable.

Five fixed themes retain different image proportions and narrative placement.
All use shape B after S12 A and S13 C. Below 850px the order becomes introduction,
overview photograph, case narrative and detail photograph. Details expand in
normal flow. Each labelled section has an H2 and one labelled article with an H3.
Scoped CSS includes border-box descendants, visible focus, reduced-motion treatment
and disclosure targets at least 44px tall.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- No document or element overflow when closed or expanded.
- Identity metadata, unique IDs, labelled headings, one story and two media slots checked.
- All disclosures open, close, accept focus and meet target height.
- Five desktop and five phone screenshots visually reviewed.
- Copy meets the ordinary-content 90-170-word target.
- Gallery passed frame count, filtering, mobile width, pressed states, full-size
  links and restoration. Live sizing follows disclosures where permitted;
  measured closed heights support local-file previews otherwise.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five case-study layouts](../../../review/energy-cases.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-cases.ps1

Measured heights: ../../../review/energy-cases-heights.json.
Next: S15-technical-resources.
