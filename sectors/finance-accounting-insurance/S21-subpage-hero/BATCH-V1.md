# BATCH V1

## Batch Identity

- Sector: Finance, Accounting & Insurance
- Prefix: FIN
- Section ID: FIN-S21
- Section Name: Subpage Hero
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-15
- Sector total: 105 studies; S01-S21 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| FIN-S21-001 | Universal / Safe | Ivory & Olive | B | Internal title beside a contained landscape photograph |
| FIN-S21-002 | Premium / Editorial | Rosewood | C | Typographic title above a split context row |
| FIN-S21-003 | Structured / Visual Modular | Lagoon | B | Introduction panel beside a compact square photograph |
| FIN-S21-004 | Conversion-led | Iris | C | Text-only contextual page banner |
| FIN-S21-005 | Art-directed / Distinctive | Ink & Apricot | B | Dark internal title above a shallow panoramic image |

All five raw files are authored. Visible copy is 51 words in media variants and
42 words in text-only variants. S20 used shape C; no A sequence is extended.

## Research Metadata and Scope

Sources: user continuation request, canonical section README, preceding finance
studies and FINANCE-THEME-CONTRACT.md. Research date: 2026-09-15.
External research: NONE. Document-metaphor justification: NONE.

These are internal service-page introductions. Title, category, audience, jurisdiction
and a short page-specific scope remain reserved fields. They orient readers before
the service body; they do not restate homepage positioning or include S23 detail.
No actual service availability or jurisdiction-specific claim is invented. The
canonical dense and sector-native directions are interpreted through the established
modern Structured / Visual Modular and Art-directed / Distinctive theme contract.

## Media Slots

One reserved page-specific photograph in 001, 003 and 005; three slots total. No media
in 002 or 004. Choose a subject directly relevant to the approved service page without
implying a real client, employee or engagement. Desktop regions are 240-350px tall.

Every slot has allocated space, a visible reserved-image label, accessible description
and named caption. Obtain licensing, provenance, applicable participant consent and
final descriptive alt text before publication. Keep the labelled region as fallback
until approved imagery exists. Page context remains understandable without an image.

## Interaction and Responsive Decisions

One labelled section with H2 begins with the page title, followed by category,
introduction and contextual metadata. No navigation, CTA, disclosure, body articles,
raw scripts or external dependencies. Full contextual navigation belongs to S22.

Desktop arrangements vary through contained imagery, editorial text, a context panel,
a coloured banner and a panoramic image. Tablet and phone preserve title-first reading
order, wrap metadata and reduce media to 260/220px. Scoped CSS uses border-box sizing,
system sans and reduced-motion handling. No focus targets are needed in this static role.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- Checked identity metadata, unique IDs, title-first structure, media count, B/C
  shapes, caption pairing, no unnecessary interaction and 40-90-word hero budgets.
- No document or element overflow.
- Five desktop and five phone screenshots visually reviewed.
- Gallery frame count, filtering, mobile width, pressed states, full-size links and
  restoration passed. Measured heights support local-file previews.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five subpage hero layouts](../../../review/finance-subpage-hero.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-subpage-hero.ps1

Measured heights: ../../../review/finance-subpage-hero-heights.json.
Next: S22-breadcrumb-context-navigation.
