# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S03
- Section Name: Industries Applications
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 15 studies; S01-S03 authored.

## Studies

All five studies are AUTHORED, with three application groups and three native
discussion disclosures each. Closed copy is 152 words, or 155 in variant 004.
Opening the first disclosure increases this to 158 or 161 words respectively.

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S03-001 | Universal / Safe | Sunlit | A | Three open application cards with prominent site photographs |
| ENG-S03-002 | Premium / Editorial | Terracotta | A | Editorial application rows pairing site imagery and practical context |
| ENG-S03-003 | Structured / Visual Modular | Tidal | A | Featured business application beside two compact site modules |
| ENG-S03-004 | Conversion-led | Daybreak | A | Horizontal application choices with focused discussion controls |
| ENG-S03-005 | Art-directed / Distinctive | Night Current | A | Dark staggered application cards with varied image proportions |

## Research Metadata and Scope

Sources: user continuation request, section README, sector brief,
../ENERGY-THEME-CONTRACT.md, preceding studies, authoring standard and media policy.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Business and workplaces, production and logistics, and land and agriculture are
exploratory application categories. Copy discusses site context and explicitly
requires service availability to be confirmed. It does not claim provider
experience, eligibility, performance or completed projects. Each disclosure holds
a labelled placeholder for verified applications, requirements or coverage.
No invented savings, capacity, certifications, permissions or guarantees.

Discussion points controls open their own native details content. Accessible
names include the corresponding application title. No dead links, invented
destinations, forms or raw JavaScript.

## Composition and Responsive Decisions

001 uses three open photo cards. 002 pairs photography and text in editorial rows.
003 places a large featured workplace card beside two compact modules. 004 uses
horizontal choices with prominent blue disclosure controls. 005 staggers three
cards, varies image proportions and highlights the first card in lime.

Below 850px, all layouts become a single column in the same content order.
Expanded content remains in normal flow. A labelled section H2 introduces three
labelled articles with H3 headings. Scoped CSS provides border-box sizing, visible
focus, reduced-motion treatment and control targets of at least 44px.

S01 shapes: B / B / B / C / B. S02 and S03: A / A / A / A / A.
This is the second consecutive A section. S04 must use B or C per variant to
avoid a third consecutive item-grid section and preserve page rhythm.

## Media and Dependencies

Three reserved application-site photographs per study, 15 slots total:
workplace setting, production setting and rural setting. Every slot is labelled
visibly and accessibly. Supply approved relevant photography before publication;
these are not fabricated project images or claims of ownership.
Framework, CDN and remote runtime dependencies: NONE.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- No document or element overflow in closed, first-open or all-open states.
- Metadata, unique IDs, labelled headings, three application groups and three
  media slots per study checked.
- All disclosures open, close, accept focus and meet the control target height.
- Desktop and phone screenshots visually reviewed.
- Closed copy meets the 90-170-word ordinary-content target.
- Gallery passed frame count, filtering, mobile width, pressed states, full-size
  links and restoration checks. Live sizing follows disclosure changes where
  permitted; measured closed heights support local-file previews otherwise.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five application layouts](../../../review/energy-applications.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-applications.ps1

Measured heights: ../../../review/energy-applications-heights.json.
Next: S04-projects.
