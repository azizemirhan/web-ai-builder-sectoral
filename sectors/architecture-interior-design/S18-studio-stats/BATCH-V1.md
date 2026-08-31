# BATCH V1 — ARC S18 Studio Stats

## Batch Identity

- Sector: Architecture & Interior Design
- Prefix: ARC
- Section ID: ARC-S18
- Section Name: Studio Stats
- Raw Path: `./raw/`
- Batch Status: READY_FOR_INGESTION

## Study Records

### ARC-S18-001 — Universal / Safe

- Structural intent / archetype: Clear four-metric studio overview with context attached to each figure.
- Layout model: Split heading above four equal statistic panels.
- Density: Medium; four primary figures and short explanations.
- Media mode: No media required.
- Interaction: None.
- Responsive strategy: Four columns → two-by-two grid → single-column mobile stack.
- Composer value: Reliable default when a practice needs a concise, easily scanned facts section.
- Limitation / content ceiling: Best with 3–8 high-confidence figures; too many values weaken hierarchy.

### ARC-S18-002 — Premium / Editorial

- Structural intent / archetype: One oversized unifying figure followed by three supporting measures.
- Layout model: Editorial lead spread above a three-column statistics footer.
- Density: Low with one dominant message.
- Media mode: No media required.
- Interaction: None.
- Responsive strategy: Split lead and three columns → stacked lead and two-column support → single-column mobile issue.
- Composer value: Turns an abstract “one practice” idea into a strong editorial statement.
- Limitation / content ceiling: Depends on one defensible lead figure or ratio; unsuitable for a long fact inventory.

### ARC-S18-003 — Dense / Information-heavy

- Structural intent / archetype: Practice data index pairing every figure with operational context.
- Layout model: Four-column desktop table transforming into labeled mobile records.
- Density: High; six measures cover team, work, network and cadence.
- Media mode: No media required.
- Interaction: None.
- Responsive strategy: Table-like index → compact records with values held as a distinct right column.
- Composer value: Supports mature practices that need to explain several dimensions without decorative imagery.
- Limitation / content ceiling: More than 8–10 measures should be grouped into themes or moved to a report.

### ARC-S18-004 — Conversion-led

- Structural intent / archetype: Three capacity measures leading directly to a project conversation.
- Layout model: Intro, three equal statistics and a full-width closing CTA.
- Density: Medium-low; only figures relevant to engagement are retained.
- Media mode: No media required.
- Interaction: One native project-conversation link.
- Responsive strategy: Three columns and horizontal CTA → single-column measures and action.
- Composer value: Connects team scale and market breadth to a clear next step for prospective clients.
- Limitation / content ceiling: Figures must be genuinely relevant to collaboration; vanity metrics weaken the conversion story.

### ARC-S18-005 — Sector-native / Distinctive

- Structural intent / archetype: Architectural measurement sheet treating practice figures as coordinated dimensions.
- Layout model: Four-column drawing field with scale header, vertical axis and dimension lines.
- Density: Medium-high and diagrammatic.
- Media mode: No media required; native CSS drawing marks carry the visual structure.
- Interaction: None.
- Responsive strategy: Four-column sheet → two-by-two measure field → vertically stacked mobile drawing.
- Composer value: Provides a recognizably architecture-native alternative to a generic counter grid.
- Limitation / content ceiling: Best with exactly four related measures; it communicates composition more than comparison.

## Research Metadata

- Research inputs: Workspace authoring standards, Architecture & Interior Design sector taxonomy and the requirement to avoid generated visuals.
- Research date: 2026-08-31
- Structural territory rationale: The set covers safe grid, editorial statement, data index, conversion and architectural drawing territories.
- Differentiation notes: Every figure is explicitly labeled as illustrative. No factual team size, project count, tenure, ranking, award or market claim is asserted.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: NONE

## Media Slots

| Study | Slot policy | Expected future type | Accessibility / fallback |
| --- | --- | --- | --- |
| ARC-S18-001 | No media slots | — | Figures and context are entirely textual. |
| ARC-S18-002 | No media slots | — | Editorial hierarchy uses native typography and structure. |
| ARC-S18-003 | No media slots | — | The index is entirely textual. |
| ARC-S18-004 | No media slots | — | Capacity and CTA remain entirely textual. |
| ARC-S18-005 | No media slots | — | Measurement marks are native CSS and non-essential to the figure labels. |

## QA

- ID validation: PASS — five unique IDs with filename, root metadata and JSON metadata agreement.
- Standalone HTML validation: PASS — all five files load independently; HTML Tidy reports no errors or warnings.
- Accessibility baseline: PASS — semantic regions, one clear H1, machine-readable data values, explicit context and coherent source order verified.
- Responsive QA: PASS — 35 in-browser checks across 1440 / 1280 / 1024 / 768-class / 430 / 390 / 320 widths with no overflow or clipped required content.
- Interaction QA: PASS — the single CTA target resolves, remains at least 40 px high and shows visible keyboard focus; four studies intentionally contain no controls.
- Dependency validation: PASS — 0 frameworks, CDNs, remote runtime dependencies or executable JavaScript blocks.
- Media-policy validation: PASS — 0 media slots, embedded images, SVGs, video, gradients or background-image assets.

## Known Batch Boundaries

- All values are demonstrative placeholders and must be replaced with verified studio data before ingestion.
- No count-up animation is used; figures remain available without motion or JavaScript.
- The studies contain no imagery, generated visual, client mark or unsupported evidentiary claim.
