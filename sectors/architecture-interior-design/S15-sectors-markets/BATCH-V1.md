# BATCH V1 — ARC S15 Sectors & Markets

## Batch Identity

- Sector: Architecture & Interior Design
- Prefix: ARC
- Section ID: ARC-S15
- Section Name: Sectors Markets
- Raw Path: `./raw/`
- Batch Status: READY_FOR_INGESTION

## Study Records

### ARC-S15-001 — Universal / Safe

- Structural intent / archetype: Clear six-market catalogue with a shared introduction and repeatable cards.
- Layout model: Two-part heading above a 3 × 2 equal card grid.
- Density: Medium; six markets with concise descriptions and exploration links.
- Media mode: Six completely empty landscape image slots.
- Interaction: Native market links only.
- Responsive strategy: Three columns → two columns → one-column mobile list.
- Composer value: Dependable overview for multidisciplinary studios with a balanced market portfolio.
- Limitation / content ceiling: Works best with 4–9 similarly weighted markets; large inventories need grouping or filtering.

### ARC-S15-002 — Premium / Editorial

- Structural intent / archetype: Oversized numbered typology sequence for three broad fields of practice.
- Layout model: Alternating copy and large-format empty media across full-width editorial rows.
- Density: Low; three stories with deliberate pacing.
- Media mode: Three completely empty large-format image slots.
- Interaction: Native typology links only.
- Responsive strategy: Alternating desktop spreads → linear image-and-copy mobile sequence.
- Composer value: Premium storytelling when a studio wants to frame broad themes instead of a long services list.
- Limitation / content ceiling: Best with exactly 3–4 typologies; granular markets need a second index.

### ARC-S15-003 — Dense / Information-heavy

- Structural intent / archetype: Comparative matrix connecting five markets to three architectural capabilities.
- Layout model: Table-like desktop rows that transform into labeled mobile records.
- Density: High; capability relationships are visible without imagery.
- Media mode: No media required.
- Interaction: Native row links only.
- Responsive strategy: Six-column matrix → compact record list with inline labels and retained reading order.
- Composer value: Makes overlapping disciplines legible for practices spanning architecture, interiors and reuse.
- Limitation / content ceiling: Capability terms must stay short; more than 8–10 markets would benefit from grouping.

### ARC-S15-004 — Conversion-led

- Structural intent / archetype: Project-pathway selector that moves from market recognition to a direct enquiry.
- Layout model: Introductory split above four large linked pathways and a closing contact strip.
- Density: Medium-low; four choices and one secondary conversion action.
- Media mode: No media required.
- Interaction: Native pathway and enquiry links.
- Responsive strategy: Two-column choice field → single-column mobile sequence with full-width action.
- Composer value: Useful when visitors know their project situation but not the studio’s service terminology.
- Limitation / content ceiling: Best with 3–6 high-level pathways; too many choices weaken conversion clarity.

### ARC-S15-005 — Sector-native / Distinctive

- Structural intent / archetype: Architecture-specific atlas mapping market types across scale and delivery context.
- Layout model: Three-by-three coordinate field with row and column axes.
- Density: High but diagrammatic; eight linked territories and one intentionally open cell.
- Media mode: No media required; the grid is the content.
- Interaction: Native cell links only.
- Responsive strategy: Coordinate matrix → vertically grouped context rows while preserving axis meaning in cell labels.
- Composer value: Expresses a studio’s practice as relationships rather than a conventional category list.
- Limitation / content ceiling: Requires disciplined taxonomy; unsuitable when market names cannot be mapped to two clear dimensions.

## Research Metadata

- Research inputs: Workspace authoring standards, Architecture & Interior Design sector taxonomy and the user’s existing preference for blank visual areas.
- Research date: 2026-08-31
- Structural territory rationale: The set covers catalogue, editorial, comparative, conversion and architecture-native diagram territories without repeating a single grid.
- Differentiation notes: No client, project, award, statistic, logo or factual capability claim is embedded. All visible content is neutral demonstrative copy.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: NONE

## Media Slots

| Study | Slot policy | Expected future type | Accessibility / fallback |
| --- | --- | --- | --- |
| ARC-S15-001 | Six empty landscape slots | Market or project photography | Each slot has a market-specific accessible name; full meaning remains in adjacent copy. |
| ARC-S15-002 | Three empty large-format slots | Editorial project photography | Each slot is named and paired with a complete typology story. |
| ARC-S15-003 | No media slots | — | Capability relationships are entirely textual. |
| ARC-S15-004 | No media slots | — | Pathways and actions are entirely textual. |
| ARC-S15-005 | No media slots | — | The structural atlas remains complete without imagery. |

## QA

- ID validation: PASS — five unique IDs with filename, root metadata and JSON metadata agreement.
- Standalone HTML validation: PASS — all five files load independently; HTML Tidy reports no errors or warnings.
- Accessibility baseline: PASS — semantic regions, one clear H1, named empty media, visible keyboard focus, logical source order and practical touch targets verified.
- Responsive QA: PASS — 35 in-browser checks across 1440 / 1280 / 1024 / 768-class / 430 / 390 / 320 widths with no overflow or clipped required content.
- Interaction QA: PASS — all internal targets resolve; native links remain visible, focusable and at least 40 px high at mobile width.
- Dependency validation: PASS — 0 frameworks, CDNs, remote runtime dependencies or executable JavaScript blocks.
- Media-policy validation: PASS — 0 embedded images, SVGs, video, gradients or background-image assets; all nine documented image slots are empty.

## Known Batch Boundaries

- All media areas are intentionally blank and contain no generated or embedded imagery.
- Market names, capability labels and descriptive copy are demonstrative structure, not factual studio claims.
- Links demonstrate affordances inside standalone studies and do not represent implemented destination pages.
