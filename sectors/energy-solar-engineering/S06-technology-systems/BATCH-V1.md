# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S06
- Section Name: Technology Systems
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 30 studies; S01-S06 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S06-001 | Universal / Safe | Sunlit | A | Three open technology stories with broad equipment photographs |
| ENG-S06-002 | Premium / Editorial | Terracotta | A | Alternating editorial rows with generous image crops |
| ENG-S06-003 | Structured / Visual Modular | Tidal | A | Featured solar module beside compact storage and conversion modules |
| ENG-S06-004 | Conversion-led | Daybreak | A | Image-led comparison cards with prominent exploration controls |
| ENG-S06-005 | Art-directed / Distinctive | Night Current | A | Staggered technology gallery with a tall central image |

All five studies are AUTHORED. Each has three technology groups and three native
disclosures. Closed copy is 139 words, or 142 in 004. Opening the first disclosure
increases this to 147 or 150 words respectively.

## Research Metadata and Scope

Sources: user continuation request, section README, sector brief,
../ENERGY-THEME-CONTRACT.md, preceding S04 and S05 studies, authoring standard and
media policy. Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Solar generation, energy storage and power conversion are exploratory technology
categories. The introduction asks visitors to confirm available technologies and
combinations. Descriptions frame discussion of site constraints, intended use and
compatibility without providing specifications or claiming provider capabilities.
Disclosures reserve verified equipment, criteria, limits and integration scope.
No invented brands, products, warranties, capacity, efficiency, savings or guarantees.
Supply approved facts before publication.

Explore system opens the corresponding native details element. Accessible names
include the technology title. No dead links, fake submissions, global navigation,
raw scripts or remote runtime dependencies.

## Composition and Responsive Decisions

The same content is arranged as open columns, alternating editorial rows, a
featured module beside two compact modules, action-focused comparison cards and
a staggered gallery. Typographic hierarchy, media proportions and content placement
differentiate the five layouts. There are no blueprint grids, gauges or dashboards.

Below 850px, all studies stack in solar, storage and conversion order. Photographs
retain 260px reservations, followed by headings, descriptions and disclosures.
Expanded content remains in normal flow. Each group is a labelled article with
an H3 under the section H2. Scoped CSS includes border-box descendants, visible
focus, reduced-motion treatment and controls at least 44px tall.

S04 was B across all variants; S05 and S06 are A. S07 must use B or C per variant
to avoid three consecutive item-grid sections.

## Media

Three reserved photographs per study, 15 total: a solar installation, storage
equipment and conversion equipment. Each slot has a visible subject caption and
an accessible reserved-image label. Use approved relevant equipment photography;
these slots do not imply owned installations or verified product availability.
Licensing, provenance and final descriptive alt text are required before ingestion.
Solid theme-colour fields preserve hierarchy when imagery is unavailable.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- No document or element overflow when closed, first-open or all-open.
- Metadata, unique IDs, labelled headings, three technology articles and three
  media reservations per variant checked.
- All disclosures open, close, accept focus and meet the control target height.
- Five desktop and five phone screenshots visually reviewed.
- Copy meets the ordinary-content 90-170-word target.
- Gallery passed frame count, filtering, mobile width, pressed states, full-size
  links and restoration. Live sizing follows disclosures where permitted;
  measured closed heights support local-file previews otherwise.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five technology layouts](../../../review/energy-technology.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-technology.ps1

Measured heights: ../../../review/energy-technology-heights.json.
Next: S07-infrastructure-equipment.
