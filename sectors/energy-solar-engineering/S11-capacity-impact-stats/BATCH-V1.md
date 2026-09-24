# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S11
- Section Name: Capacity Impact Stats
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 55 studies; S01-S11 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S11-001 | Universal / Safe | Sunlit | A | Open columns with oversized values and contextual labels |
| ENG-S11-002 | Premium / Editorial | Terracotta | A | Editorial rows pairing a large value with its scope |
| ENG-S11-003 | Structured / Visual Modular | Tidal | A | Featured capacity figure beside two supporting impact metrics |
| ENG-S11-004 | Conversion-led | Daybreak | A | Source-focused metric stack beside an interpretation guide |
| ENG-S11-005 | Art-directed / Distinctive | Night Current | A | Descending dark composition ending in a lime impact figure |

All five studies are AUTHORED. Each has three metric groups and three native
source disclosures. Copy is 125 words closed and 135 with the first disclosure open.

## Research Metadata and Scope

Sources: user continuation request, section README, sector brief,
../ENERGY-THEME-CONTRACT.md, preceding S09 and S10 studies, authoring standard
and media policy. Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

Installed capacity, energy generated and emissions impact are candidate metric
categories. All values are explicit [Value] placeholders. Their descriptions
reserve units, boundaries, dates, periods and measurement status. Disclosures
reserve sources and methodology. No capacities, energy totals, emissions results,
growth rates, comparative claims or project ownership are invented. Supply verified
values and sources before publication. The emissions field requires a baseline
and distinguishes measured, calculated and projected results.

View source & scope opens the corresponding native details content. Accessible
names identify the metric. There are no fake source links, animated counters,
charts implying data, global headers or footers, raw scripts or remote dependencies.

## Composition, Media and Responsive Decisions

Large values anchor each layout. The five established themes remain consistent
while grouping, narrative position and metric emphasis vary. No gauges, dashboards
or technical document metaphors are used. Media slots: NONE; the section's role is
to present figures and context, and S10 supplies preceding photographic content.

S09 was A and S10 was B; S11 begins a new A sequence. Below 850px all metrics stack
in capacity, generation and emissions order. Descending offsets reset; expanded
details remain in normal flow. A labelled H2 introduces three labelled articles
with H3 headings. Scoped CSS includes border-box descendants, visible focus,
reduced-motion treatment and controls at least 44px tall.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- No document or element overflow when closed, first-open or all-open.
- Metadata, unique IDs, labelled headings and three metric groups checked.
- All disclosures open, close, accept focus and meet target height.
- Five desktop and five phone screenshots visually reviewed.
- Copy meets the ordinary-content 90-170-word target.
- Gallery passed frame count, filtering, mobile width, pressed states, full-size
  links and restoration. Live sizing follows disclosures where permitted;
  measured closed heights support local-file previews otherwise.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five metric layouts](../../../review/energy-stats.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-stats.ps1

Measured heights: ../../../review/energy-stats-heights.json.
Next: S12-products-systems.
