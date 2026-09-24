# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S12
- Section Name: Firm Stats
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 60 studies; S01-S12 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S12-001 | Universal / Safe | Ivory & Olive | A | Three open firm figures separated by quiet olive rules |
| FIN-S12-002 | Premium / Editorial | Rosewood | A | Editorial figures aligned with their definitions |
| FIN-S12-003 | Structured / Visual Modular | Lagoon | A | Asymmetric two by two composition with a featured fact |
| FIN-S12-004 | Conversion-led | Iris | A | Violet introduction beside a vertical fact sequence |
| FIN-S12-005 | Art-directed / Distinctive | Ink & Apricot | A | Dark typographic figures with an apricot central fact |

All five raw files are authored. Closed visible copy is 127 words; expanded copy
is 156 words. S11 and S12 use shape A, so S13 must use shape B or C.

## Research Metadata and Scope

Sources: user continuation request, section README, preceding finance studies and
FINANCE-THEME-CONTRACT.md. Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

Firm history, team count and office presence remain explicit reserved fields.
Each value needs an approved definition, source and reference date. Legal entity,
included personnel and staffed-location scope must be stated before publication.
No establishment date, headcount, location count, performance or quality claim is
invented. Shared source notes provide room for methodology, exclusions and review
dates without implying financial performance.

## Media Slots

None. These typographic fact layouts require no photography or decorative charts.

## Interaction and Responsive Decisions

One labelled section with H2 contains three articles, each named by its H3. A native
Definitions and source notes disclosure provides supporting context. No animated
counters, scripts, forms, fabricated routes or external dependencies are included.

Desktop layouts vary between open columns, editorial rows, a featured composition,
a split introduction and staggered cards. Tablet and phone use one reading order.
Mobile value-to-heading spacing was refined following visual review. Scoped CSS
includes wrapping, visible focus, reduced-motion handling and a 48px summary target.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- Checked metadata, unique IDs, article-heading pairs, reserved values, source notes
  and closed/expanded copy budgets.
- No document or element overflow with the disclosure closed or open.
- Summary accepts focus, meets target height and opens/closes correctly.
- Five desktop and five phone screenshots visually reviewed; automated checks
  repeated after the mobile spacing refinement.
- Gallery frame count, filtering, mobile width, pressed states, full-size links and
  restoration passed. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five firm fact layouts](../../../review/finance-stats.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-stats.ps1

Measured heights: ../../../review/finance-stats-heights.json.
Next: S13-resources-guides.
