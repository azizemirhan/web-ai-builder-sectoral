# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S04
- Section Name: Projects
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 20 studies; S01-S04 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S04-001 | Universal / Safe | Sunlit | B | Wide photograph above a split project story and detail image |
| ENG-S04-002 | Premium / Editorial | Terracotta | B | Portrait photograph beside a narrow story and inset detail |
| ENG-S04-003 | Structured / Visual Modular | Tidal | B | Teal narrative panel beside a stacked overview and detail diptych |
| ENG-S04-004 | Conversion-led | Daybreak | B | Wide project view beside a blue panel with a prominent exploration control |
| ENG-S04-005 | Art-directed / Distinctive | Night Current | B | Tall curved photograph, offset lime story and smaller detail image |

All five studies are AUTHORED. Each presents one featured project, two related
photographs and one native disclosure. This is an edited project spotlight, not
an exhaustive portfolio or a project detail page.

## Research Metadata and Scope

Sources: user continuation request, section README, sector brief,
../ENERGY-THEME-CONTRACT.md, preceding S02 and S03 studies, authoring standard
and media policy. Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

No project evidence was supplied. Project name, location, type, introduction and
expanded narrative are explicit placeholder fields. No project ownership,
clients, capacity, savings, completion status or environmental results are invented.
Replace these fields with approved facts before publication. Generic introductory
copy frames the visitor's exploration without claiming provider performance.

The Explore project context control opens native details content locally. There
are no dead links, fake destinations, forms, global navigation or raw scripts.

## Composition and Responsive Decisions

Each variant retains the established colour theme while changing the photograph
scale, narrative placement, heading arrangement and disclosure emphasis.
Two anchored images of the same project make every variant shape B. S02 and S03
were A across all variants; S04 breaks that consecutive item-grid sequence.

Below 850px the overview, story and detail photograph stack in DOM order. All
content remains in normal flow when expanded. At phone widths the principal
photograph is 310px tall, with a 250px detail reservation. Section headings use
H2; the project article uses a labelled H3. Scoped CSS includes descendant
border-box sizing, visible keyboard focus, reduced-motion treatment and controls
at least 44px tall. No remote runtime dependencies.

Copy is 78 words closed and 97 expanded. This deliberately falls below the sector's
ordinary-content 90-word target: the section is a media-led project spotlight,
and adding unsupported narrative or padding would conflict with the authoring
standard's proportional-copy and no-fabrication requirements.

## Media

Two reserved photographs per study, ten slots total. The overview shows the
verified project in its site context; the detail shows an installation detail
from that same project. Both need approved provenance, licensing and final
descriptive alt text before ingestion. Visible captions and accessible reserved
image labels identify the current placeholders. Solid theme-colour fields retain
space and hierarchy when photographs are unavailable; no fabricated imagery.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- No document or element overflow with the disclosure closed or open.
- Metadata, unique IDs, labelled headings, one project article and two media
  reservations per variant checked.
- Disclosure opens, closes, accepts focus and meets the minimum target height.
- Five desktop and five phone screenshots visually reviewed.
- Gallery frame count, filtering, mobile width, pressed states, full-size links
  and restoration checked. Live sizing follows disclosure changes where allowed;
  measured closed heights support local-file previews otherwise.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five project layouts](../../../review/energy-projects.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-projects.ps1

Measured heights: ../../../review/energy-projects-heights.json.
Next: S05-capabilities.
