# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S14
- Section Name: Compliance Calendar
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 70 studies; S01-S14 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S14-001 | Universal / Safe | Ivory & Olive | A | Rounded date markers beside open event rows |
| FIN-S14-002 | Premium / Editorial | Rosewood | A | Introduction beside an editorial calendar sequence |
| FIN-S14-003 | Structured / Visual Modular | Lagoon | A | Three generous calendar cards with a highlighted centre |
| FIN-S14-004 | Conversion-led | Iris | A | Featured date above two complementary agenda entries |
| FIN-S14-005 | Art-directed / Distinctive | Ink & Apricot | A | Apricot date capsules beside spacious event narratives |

All five raw files are authored. Closed visible copy is 141 words; expanded copy
is 169 words. S13 used shape B, so this A section begins a new sequence.

## Research Metadata and Scope

Sources: user continuation request, section README, preceding finance studies and
FINANCE-THEME-CONTRACT.md. Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

Three reserved agenda entries cover filing, payment and review or renewal contexts.
Dates, obligation titles, applicable entities, periods, jurisdiction, required action
and official source references remain placeholders. No legal deadline, tax rule,
payment amount or applicable obligation is asserted. Before publication, verify the
calendar year, timezone, official deadlines, holiday adjustments and entity-specific
exceptions for the intended audience. Populate and sort entries chronologically.
Replace reserved dates with machine-readable time elements once actual dates exist.

## Media Slots

None. Typography, colour and agenda spacing carry the section. No faux documents,
dashboard controls, charts, seals or decorative calendar widgets are included.

## Interaction and Responsive Decisions

One labelled section with H2 contains three articles, each named by its H3. Each
entry pairs a reserved date with its obligation, scope and verification source.
A native Calendar scope and source notes disclosure provides shared context.
There are no reminder subscriptions, calendar exports, fabricated routes or scripts.

Desktop layouts use open rows, a split introduction, equal cards, a featured entry
and date capsules. Tablet and phone preserve the date, title, scope and source order.
Scoped CSS includes wrapping, border-box sizing, visible focus, reduced-motion
handling and a summary target of at least 48px.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- Checked identity metadata, unique IDs, article-heading pairs, three reserved dates,
  source notes and closed/expanded copy budgets.
- No document or element overflow with the disclosure closed or open.
- Summary accepts focus, meets target height and opens/closes correctly.
- Five desktop and five phone screenshots visually reviewed.
- Gallery frame count, filtering, mobile width, pressed states, full-size links and
  restoration passed. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five calendar layouts](../../../review/finance-calendar.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-calendar.ps1

Measured heights: ../../../review/finance-calendar-heights.json.
Next: S15-technology-integrations.
