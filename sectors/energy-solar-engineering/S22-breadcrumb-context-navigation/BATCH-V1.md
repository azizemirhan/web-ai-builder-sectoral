# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S22
- Section Name: Breadcrumb / Context Navigation
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 110 studies; S01-S22 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S22-001 | Universal / Safe | Sunlit | C | Compact trail with related topics alongside |
| ENG-S22-002 | Premium / Editorial | Terracotta | C | Editorial breadcrumb row above related topics |
| ENG-S22-003 | Structured / Visual Modular | Tidal | C | Teal hierarchy panel paired with pale related navigation |
| ENG-S22-004 | Conversion-led | Daybreak | C | Prominent parent link within a blue navigation stage |
| ENG-S22-005 | Art-directed / Distinctive | Night Current | C | Lime hierarchy ribbon above offset related navigation |

Visible copy is 13 words. This navigation-only role intentionally uses short labels
rather than adding prose to meet an ordinary section copy target.

## Research Metadata and Scope

Sources: user continuation request, section README, sector brief, theme contract,
preceding S20 and S21 studies, authoring standard and media policy.
Research date: 2026-09-15. External research: NONE.
Document-metaphor justification: NONE. Media mode: NONE.

The example hierarchy is Home / Solutions / Solar project planning, matching the
S21 internal-page context. This demonstrates proposed page placement, not a claim
that production routes have been implemented. Related topics are technology and
engineering process; they are not labelled as siblings. No page title or hero
introduction is repeated, and no site-wide navigation is introduced.

## Interaction and Responsive Decisions

Two distinct named navigation landmarks contain the breadcrumb ordered list and
related-topic links. The current page is plain text with aria-current="page".
Four native links point to existing S01, S02, S06 and S08 studies with matching
variant numbers. Production route mapping belongs to ingestion.

The root region has an accessible name rather than a visible heading, consistent
with the navigation-only role. All hierarchy levels remain available at small
widths through wrapping. No truncation, hidden levels, scripts, remote dependencies,
forms, media or pretend controls. Scoped CSS includes border-box descendants,
visible focus, reduced-motion treatment and links at least 44px tall.
S21 was B; all S22 variants use C.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- No document or element overflow; all trail levels remain visible.
- Identity metadata, named landmarks, ordered trail and current-page marker checked.
- All four links accept focus, meet target height and retain matching variant IDs.
- Every relative destination verified on disk.
- Five desktop and five phone screenshots visually reviewed.
- Gallery passed frame count, filtering, mobile width, pressed states, full-size
  links and restoration. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five navigation layouts](../../../review/energy-navigation.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-navigation.ps1

Measured heights: ../../../review/energy-navigation-heights.json.
Next: S23-service-offering-detail.
