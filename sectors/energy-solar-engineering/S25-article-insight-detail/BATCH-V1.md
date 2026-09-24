# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S25
- Section Name: Technical Insight / Article Detail
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 125 studies; S01-S25 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S25-001 | Universal / Safe | Sunlit | B | Centered reading column beneath a wide photograph |
| ENG-S25-002 | Premium / Editorial | Terracotta | B | Split editorial opening followed by a narrow reading column |
| ENG-S25-003 | Structured / Visual Modular | Tidal | B | Teal attribution rail beside an article with an inline photograph |
| ENG-S25-004 | Conversion-led | Daybreak | B | Blue editorial opening with a reading column and resource pathway |
| ENG-S25-005 | Art-directed / Distinctive | Night Current | B | Dark photo-led opening, offset article and lime closing thought |

Visible copy: 171 words closed; 187 words with publication notes expanded.

## Research Metadata and Editorial Scope

Sources: user continuation request, section README, theme contract, preceding
studies and repository media policy. Research date: 2026-09-15. External research:
NONE. Document-metaphor justification: NONE.

Original sample article: A clearer brief for your solar project. Three short
sections discuss defining a question, identifying available site information and
keeping unknowns visible. The complete body remains readable without interaction.
This is general editorial sample copy, without engineering calculations, investment
claims, performance forecasts or marketing promises. No external article is copied.
Author and publication date remain explicit placeholders; no author, date, citation
or publication history is fabricated. Publication notes identify outstanding
editorial approval, attribution, references and licensing.

## Media

One reserved editorial site photograph per study; five slots total. Its purpose is
to establish context, without claiming that the pictured site is an owned project
or evidence of an outcome. Expected type: approved site photograph. The visible
caption and accessible label identify the reserved subject. Before ingestion,
supply licensing, provenance and final descriptive alternative text. Fallback:
retain the labelled allocated region; all article content remains understandable.
Variant 003 places the photograph inside the reading column without widening it.

## Interaction and Responsive Decisions

A labelled section has one H2; the named article contains three H3 body sections.
Attribution uses a definition list. Native details exposes publication notes;
it does not gate the article. One native resource link opens the corresponding
S15 variant, with production routing deferred to ingestion. No fake related article,
share control, reading timer or progress indicator is introduced.

Reading columns have a 720px maximum and paragraph measure of 65ch. Mobile retains
all content in normal flow. Scoped CSS provides border-box descendants, visible
focus, 44px targets and reduced-motion treatment. No raw scripts, external fonts,
frameworks or remote dependencies. Both preceding sections and S25 use shape B.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- Identity, heading structure, unique IDs, media count and word budgets checked.
- No document or element overflow, including expanded notes.
- Native disclosure opening, closing, focus and target height passed.
- Resource links retain matching variant numbers; all destinations verified on disk.
- Five desktop and five phone layouts visually reviewed; attribution alignment and
  mobile paragraph alignment refined during review.
- Gallery frame count, filtering, mobile width, pressed states, full-size links and
  restoration passed. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five article layouts](../../../review/energy-article-detail.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-article-detail.ps1

Measured heights: ../../../review/energy-article-detail-heights.json.
Next: S26-person-profile-detail.
