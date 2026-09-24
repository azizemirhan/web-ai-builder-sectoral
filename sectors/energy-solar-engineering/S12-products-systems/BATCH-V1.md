# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S12
- Section Name: Products Systems
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 60 studies; S01-S12 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S12-001 | Universal / Safe | Sunlit | A | Three warm product cards with contained image stages |
| ENG-S12-002 | Premium / Editorial | Terracotta | A | Open editorial product columns with an offset central item |
| ENG-S12-003 | Structured / Visual Modular | Tidal | A | Horizontal product modules pairing image and specification context |
| ENG-S12-004 | Conversion-led | Daybreak | A | Featured blue product beside two compact supporting cards |
| ENG-S12-005 | Art-directed / Distinctive | Night Current | A | Dark product collection with a lime central card |

All five studies are AUTHORED. Closed copy is 134 words, or 137 in 004.
Opening the first disclosure increases this to 146 or 149 words respectively.

## Research Metadata and Scope

Sources: user continuation request, section README, sector brief,
../ENERGY-THEME-CONTRACT.md, preceding S10 and S11 studies, authoring standard
and media policy. Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE.

Solar module, storage system and inverter entries reserve actual product names,
manufacturer descriptions and verified details. No models, specifications, prices,
availability, compatibility or warranty terms are invented. The introduction asks
visitors to confirm available models and configurations. Supply approved product
information and official sources before publication. S06 introduces technology
categories; S12 demonstrates individual product entries and their detail fields.

View product details opens native details content for its product. Accessible names
identify the product placeholder. No fake shopping actions, downloads, external
destinations, global headers or footers, raw scripts or remote dependencies.

## Composition, Media and Responsive Decisions

The five themes remain consistent while image proportions, grouping, product
emphasis and reading direction differ. No technical document metaphor is used.
S10 was B; S11 and S12 are A. S13 must use B or C per variant to avoid a third
consecutive item-grid section.

Three product-image reservations per study, 15 total: solar module, storage system
and inverter. Use approved product photography or manufacturer renders that
accurately represent the selected model, with licensing and provenance documented
before ingestion. Provide final descriptive alt text. Visible captions and
accessible placeholder labels identify the slots; solid theme-colour fields
retain the composition when images are unavailable. No fabricated product imagery.

Below 850px products stack in solar, storage and inverter order. Image reservations
remain 260px tall, and details expand in normal flow. A labelled section H2
introduces three labelled articles with H3 headings. Scoped CSS includes border-box
descendants, visible focus, reduced-motion treatment and targets at least 44px tall.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- No document or element overflow when closed, first-open or all-open.
- Metadata, unique IDs, labelled headings, three products and three media slots checked.
- All disclosures open, close, accept focus and meet target height.
- Five desktop and five phone screenshots visually reviewed.
- Copy meets the ordinary-content 90-170-word target.
- Gallery passed frame count, filtering, mobile width, pressed states, full-size
  links and restoration. Live sizing follows disclosures where permitted;
  measured closed heights support local-file previews otherwise.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five product layouts](../../../review/energy-products.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-products.ps1

Measured heights: ../../../review/energy-products-heights.json.
Next: S13-roi-financing.
