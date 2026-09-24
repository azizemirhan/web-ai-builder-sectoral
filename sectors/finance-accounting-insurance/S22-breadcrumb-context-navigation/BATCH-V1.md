# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S22
- Section Name: Breadcrumb / Context Navigation
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15 (raw studies and review gallery); batch record closed 2026-09-16
- Sector total: 110 studies; S01-S22 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S22-001 | Universal / Safe | Ivory & Olive | C | Olive inline trail with a parent return at the opposite edge |
| FIN-S22-002 | Premium / Editorial | Rosewood | C | Rosewood editorial trail above a separate parent return |
| FIN-S22-003 | Structured / Visual Modular | Lagoon | C | Lagoon contextual trail with a compact related-information row |
| FIN-S22-004 | Conversion-led | Iris | C | Iris parent return beside a softly framed trail |
| FIN-S22-005 | Art-directed / Distinctive | Ink & Apricot | C | Dark breadcrumb ribbon with an apricot current-location marker |

All five raw files are authored. Visible copy is 8 words in 001, 002, 004 and 005 and
15 words in 003, which adds a two-link related-information row. This is a navigation
role with no copy budget; the trail, the current position and the parent return are
the whole of the content. S21 used B C B C B; no A sequence exists to extend.

## Research Metadata and Scope

Sources: user continuation request, canonical section README, FIN-S21 subpage heroes
and FINANCE-THEME-CONTRACT.md. Research date: 2026-09-15.
External research: NONE. Document-metaphor justification: NONE.

Every study carries a real navigation landmark (`nav` with an accessible name) around
an ordered list, marks the current page with `aria-current="page"` rather than by
styling alone, and offers a contextual parent return to the services index. The
current page label is a reserved field. 003 adds a second labelled `nav` for related
information, linking the resources and tools sections at the same variant. Trails link
to the same-variant hero and services studies so that assembled page N stays within
theme N. No primary navigation, page title or footer listing is included; those belong
to page chrome, S21 and the footer respectively.

## Media Slots

None. This role is navigation, not presentation.

## Interaction and Responsive Decisions

Links only, all relative and within the sector. Link targets are at least 44px tall.
Focus is a 3px accent outline with a 4px offset, contrasting with the surrounding
surface in every theme. No script, disclosure, filtering or external dependency.

At desktop the trail and the parent return share one band; 003 places the related row
in the same band and 005 sets the trail as a dark ribbon with the current location
marked in apricot. Below 850px the band releases to block flow and the return drops
beneath the trail. Below 560px insets tighten to 22px, the trail wraps at 15px and the
gap closes; the trail is never truncated or hidden. Reduced-motion disables all
animation and transition.

## QA

- Passed structural checks on all five: theme tokens and radius per contract, 1400px
  frame, reduced-motion block, namespace scoping, tag balance, no dependency, no
  claim, no figure, relative links only, focus-visible present.
- Measured heights at 1440, 768, 390 and 320px are recorded in the review folder;
  the tallest study (003 at 320px) is 406px.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five breadcrumb layouts](../../../review/finance-context-navigation.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-context-navigation.ps1

Measured heights: ../../../review/finance-context-navigation-heights.json.
Next: S23-service-offering-detail.
