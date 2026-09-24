# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S13
- Section Name: ROI Financing
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 65 studies; S01-S13 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S13-001 | Universal / Safe | Sunlit | C | Open introduction beside a warm evaluation panel |
| ENG-S13-002 | Premium / Editorial | Terracotta | C | Editorial overview above a two-column evaluation narrative |
| ENG-S13-003 | Structured / Visual Modular | Tidal | C | Teal context panel paired with an introductory column |
| ENG-S13-004 | Conversion-led | Daybreak | C | Wide blue evaluation invitation beneath the introduction |
| ENG-S13-005 | Art-directed / Distinctive | Night Current | C | Oversized dark statement above an offset lime panel |

All five studies are AUTHORED. Closed copy is 90 words; expanded copy is 109 words.

## Research Metadata and Scope

Sources: user continuation request, section README, sector brief,
../ENERGY-THEME-CONTRACT.md, preceding S11 and S12 studies, authoring standard
and media policy. Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

Investment scope, quoted costs, operating assumptions, savings estimates and
financing terms remain explicit placeholders. No rates, payback periods, savings,
funding providers, approved offers or guarantees are invented. Approved project
information and calculation sources are required to replace these reservations.
This batch provides presentation layouts, not a calculator or financial advice.

View evaluation details opens a native disclosure with fields for the estimate
source, date, assumptions, sensitivity and exclusions. No dead links, forms,
global navigation, raw scripts or external dependencies are introduced.

## Composition, Media and Responsive Decisions

All five use shape C with typography and colour; media mode is NONE.
S11 and S12 were A; this batch breaks that consecutive item-grid sequence.
Five established themes carry distinct desktop compositions without technical
or classical document styling. Below 850px each introduction precedes its
evaluation panel, with disclosures expanding in normal flow.

Each labelled section has an H2 and one labelled article with an H3. Scoped CSS
provides border-box descendants, visible focus, reduced-motion treatment and
disclosure targets at least 44px tall.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- No document or element overflow when closed or expanded.
- Metadata, unique IDs, labelled headings, one article and zero media slots checked.
- All disclosures open, close, accept focus and meet target height.
- Five desktop and five phone screenshots visually reviewed.
- Copy meets the ordinary-content 90-170-word target.
- Gallery passed frame count, filtering, mobile width, pressed states, full-size
  links and restoration. Live sizing follows disclosures where permitted;
  measured closed heights support local-file previews otherwise.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five financing layouts](../../../review/energy-financing.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-financing.ps1

Measured heights: ../../../review/energy-financing-heights.json.
Next: S14-case-studies.
