# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S03
- Section Name: Course Categories
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 15 studies, S01-S03 authored.

## Planned Studies

All five studies are AUTHORED; each raw filename matches its study ID.

| Study | Direction | Theme | Shape | Media | Words closed / expanded | Composition |
| --- | --- | --- | --- | ---: | --- | --- |
| EDU-S03-001 | Universal / Safe | Apricot | C | 0 | 75 / 154 | Large subject pills beside a concise introduction |
| EDU-S03-002 | Premium / Editorial | Mulberry | B | 2 | 81 / 160 | Open editorial category list with staggered photographs |
| EDU-S03-003 | Structured / Visual Modular | Cobalt | A | 6 | 93 / 172 | Six media-led subject cards in a category mosaic |
| EDU-S03-004 | Conversion-led | Iris | C | 0 | 80 / 159 | Purple catalogue callout beside open category rows |
| EDU-S03-005 | Art-directed / Distinctive | Afterhours | B | 2 | 81 / 160 | Dark composition with curved photographs and two subject columns |

## Research and Scope

Sources: user continuation request; section README; sector brief;
../EDUCATION-THEME-CONTRACT.md; ../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md; preceding S01 and S02 studies.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Six example subject categories demonstrate the index. Bracketed category labels,
a visible example notice and reserved associated-programme fields distinguish
illustrative structure from actual offerings. No institution catalogue was supplied.
The short descriptions explain subject scope without claiming course availability.
No invented programme counts, credentials, dates or outcomes.

The visual differences come from layout, scale, colour, grouping and media placement.
Closed copy is intentionally concise; expanded copy stays below 250 words.

## Responsive and Interaction Decisions

- 001: split introduction and rounded subject controls; phones use one category column.
- 002: two staggered image areas accompany an open list; categories precede images on phones.
- 003: three columns become two on tablets and one on narrow phones.
- 004: the purple catalogue callout leads the subject list on phones.
- 005: two open subject columns accompany curved media; phones show one subject column followed by images.

Six independent native details/summary controls reveal scope and associated-programme
placeholders. All can stay open together. Plus indicators rotate when expanded.
The single catalogue link in each study reaches the matching existing S02 raw study.
These are review routes. Category-specific filtered destinations require real mappings.

S01 shapes: B / B / B / C / B. S02: A / A / A / A / A.
S03: C / B / A / C / B. Variant 003 now has two consecutive A sections;
S04-003 should use another shape. Manual comparison was used; the CONS-specific
composition checker does not validate education studies.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- Raw JavaScript: NONE; native disclosures provide the required interaction.
- Gallery JavaScript: local preview selection, viewport sizing and frame height measurement.

## Media Register

| Study | Reserved slots | Purpose and expected type | Accessibility / fallback |
| --- | --- | --- | --- |
| 001 | None | Typography and subject controls carry the composition | No decorative media required |
| 002 | Shared learning space; Practical learning studio | Verified contextual learning photographs | Labelled empty figures with accessible reserved-photo labels |
| 003 | Creative learning studio; Collaborative learning space; Practical learning studio; Group learning space; Independent study space; Specialist learning studio | Verified photographs relevant to the eventual subjects | One labelled reserved figure per category |
| 004 | None | The coloured catalogue callout and category list carry the composition | No decorative media required |
| 005 | Practical learning studio; Shared study space | Verified contextual learning photographs | Labelled reserved figures preserve the curved composition |

Ten reserved media areas total. Empty slots are intentional. Actual imagery requires
accurate alt text and verified provenance; no remote images or generated faces included.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow with all six disclosures closed or open.
- Stable study IDs, unique DOM IDs, one section H2, no H1 or global shell.
- Native controls open and close; focusability and 44px minimum control height checked.
- Five catalogue destinations exist and match their variants.
- All five desktop and 390px screenshots visually reviewed.
- Expanded copy: 154-172 words; no raw runtime dependencies.
- Reduced-motion CSS present.
- Gallery checks passed: five frames, variant filtering, 390px mode, pressed state,
  full-size links and restoration of all variants.
- Cached gallery heights allow all categories to remain open if local-file permissions
  prevent live measurement; live frame measurement handles height changes when available.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five category layouts](../../../review/education-categories.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-categories.ps1

Measured heights: ../../../review/education-categories-heights.json.
Next: S04-learning-outcomes.
