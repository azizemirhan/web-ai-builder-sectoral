# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S13
- Section Name: Resources Guides
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 65 studies; S01-S13 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S13-001 | Universal / Safe | Ivory & Olive | B | Learning photograph beside an open guide introduction |
| FIN-S13-002 | Premium / Editorial | Rosewood | B | Wide photographic opening above an editorial guide |
| FIN-S13-003 | Structured / Visual Modular | Lagoon | B | Stacked introduction and guide alongside a tall photograph |
| FIN-S13-004 | Conversion-led | Iris | B | Featured guide and landscape photograph on a violet stage |
| FIN-S13-005 | Art-directed / Distinctive | Ink & Apricot | B | Apricot guide introduction above a panoramic photograph |

All five raw files are authored. Closed visible copy is 97 words; expanded copy
is 127 words. S11 and S12 used shape A; this media-anchored B section resets the sequence.

## Research Metadata and Scope

Sources: user continuation request, section README, preceding finance studies and
FINANCE-THEME-CONTRACT.md. Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

Each variant presents one featured educational resource with an expandable topic
outline. Guide title, introduction, intended reader, publication format, author or
reviewer, relevant jurisdiction and review date remain explicitly reserved. Source
references, learning objectives and related reading belong in the outline. No actual
guide, author, financial advice or downloadable document is invented. Reading and
download routes must be verified before links are introduced.

## Media Slots

One reserved learning-context photograph per study; five slots total. Intended
subject: a quiet reading or learning setting that supports the educational mood.
The image is contextual and must not imply an actual client or employee relationship.

Each slot has allocated space, a visible reserved-image label, an accessible image
description and a named caption. Before publication obtain licensing, provenance,
applicable participant consent and final descriptive alt text. Keep the labelled
reserved region as the fallback until an approved image is available. The resource
introduction and contents remain understandable without imagery.

## Interaction and Responsive Decisions

One labelled section with H2 contains one featured resource article named by its H3.
A native Inside this guide disclosure reveals the reserved outline. No scripts,
forms, dead routes or external dependencies are included in raw studies.

Desktop compositions vary through image proportions, sequence, grid and colour.
Tablet and phone reflow into introduction, image, caption and guide. Iris retains
its contrast and visible focus on the mobile guide panel. Scoped CSS includes
wrapping, border-box sizing, reduced-motion handling and a 48px summary target.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- Checked identity metadata, unique IDs, heading structure, reserved guide and
  publication fields, media-caption pairing and closed/expanded copy budgets.
- No document or element overflow with the disclosure closed or open.
- Summary accepts focus, meets target height and opens/closes correctly.
- Five desktop and five phone screenshots visually reviewed.
- Gallery frame count, filtering, mobile width, pressed states, full-size links and
  restoration passed. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five resource layouts](../../../review/finance-resources.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-resources.ps1

Measured heights: ../../../review/finance-resources-heights.json.
Next: S14-compliance-calendar.
