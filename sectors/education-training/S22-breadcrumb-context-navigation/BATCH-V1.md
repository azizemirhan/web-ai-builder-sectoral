# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S22
- Section Name: Breadcrumb / Context Navigation
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 110 studies, S01-S22 authored.

## Studies

All five studies are AUTHORED. Each uses shape C and no media. Navigation copy
is intentionally concise: 16-17 visible tokens including decorative separators;
ordinary section-body word targets are not applicable to this navigation-only role.

| Study | Direction | Theme | Composition |
| --- | --- | --- | --- |
| EDU-S22-001 | Universal / Safe | Apricot | Warm inline breadcrumb beside rounded admissions topic links |
| EDU-S22-002 | Premium / Editorial | Mulberry | Editorial breadcrumb above an open row of related topics |
| EDU-S22-003 | Structured / Visual Modular | Cobalt | Blue breadcrumb field beside a stacked admissions topic list |
| EDU-S22-004 | Conversion-led | Iris | Compact breadcrumb above a purple topic-navigation band |
| EDU-S22-005 | Art-directed / Distinctive | Afterhours | Dark two-level context strip with a lime topic rail |

## Research Metadata and Scope

Sources: user continuation request; section README and universal S22 role;
sector brief; ../EDUCATION-THEME-CONTRACT.md; preceding S20/S21 batches;
existing S01/S07/S16/S17 studies; ../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md; ../../../standards/06-BATCH-V1-TEMPLATE.md.
Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

The breadcrumb identifies Home > Admissions & enrolment, matching the S21
internal-page context. Three related topics lead to application steps, tuition
and fees, and funding options. Each raw study links to the matching theme in
S01, S07, S16 and S17 as local review destinations. Replace these raw-file routes
with verified site routes during integration. No institution-specific facts are invented.

Two named navigation landmarks provide hierarchy and related topics. The current
page is a non-link span with aria-current="page". Decorative separators and arrows
are hidden from assistive technology. No page heading or introduction is added:
those belong to S21. No primary navigation, footer, media, form or disclosure.

## Responsive and Interaction Decisions

001 balances a short trail with a rounded topic panel. 002 separates hierarchy
and topics with an editorial rule. 003 places a blue hierarchy field beside a
vertical topic list. 004 uses a purple band with pale link pills. 005 pairs a dark
two-level trail with a curved lime rail. These are five distinct compositions.

Narrow layouts stack related links at full width and wrap the breadcrumb without
removing levels. All four links remain keyboard focusable with visible focus and
at least 44px target height. Scoped CSS includes theme variables, border-box sizing
and reduced-motion treatment. No raw JavaScript or external runtime dependencies.

S20: C / B / C / C / B. S21: B / B / C / C / B. S22: C / C / C / C / C.
The no-media choice follows the navigation role. Theme continuity was manually
reviewed; the CONS-specific checker does not validate education studies.

## QA

- Passed 20 Chrome viewport checks: five studies at 1440, 768, 390 and 320px.
- No document or element overflow; current page stays visible.
- Metadata, unique IDs, two named nav landmarks and current-page semantics checked.
- All four links accept keyboard focus and meet minimum target dimensions.
- Matching S01/S07/S16/S17 local destinations exist.
- Five desktop and five phone screenshots visually reviewed.
- No headings, global shell, media, raw scripts or remote dependencies.
- Gallery passed five-frame, filtering, mobile width, pressed-state, full-size-link
  and restore-all checks. Cached measured heights support local-file previews.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five navigation studies](../../../review/education-context-navigation.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-context-navigation.ps1

Measured heights: ../../../review/education-context-navigation-heights.json.
Next: S23-service-offering-detail.
