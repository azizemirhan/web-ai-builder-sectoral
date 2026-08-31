# BATCH V1 — ARC S16 Press & News

## Batch Identity

- Sector: Architecture & Interior Design
- Prefix: ARC
- Section ID: ARC-S16
- Section Name: Press News
- Raw Path: `./raw/`
- Batch Status: READY_FOR_INGESTION

## Study Records

### ARC-S16-001 — Universal / Safe

- Structural intent / archetype: Familiar featured-story plus recent-news list.
- Layout model: Large lead article paired with four compact chronological links.
- Density: Medium; one feature and four updates.
- Media mode: One completely empty featured image slot.
- Interaction: Native story and archive links only.
- Responsive strategy: Two-column desktop split → single-column feature followed by news list.
- Composer value: Reliable default for studios publishing occasional news and journal entries.
- Limitation / content ceiling: The side list is best kept to 3–6 items; longer archives need pagination or a dedicated index.

### ARC-S16-002 — Premium / Editorial

- Structural intent / archetype: Magazine-like practice journal with a masthead, lead essay and three secondary notes.
- Layout model: Full-width issue masthead, split lead spread and three-column story footer.
- Density: Medium-low with generous editorial pacing.
- Media mode: Four completely empty editorial image slots.
- Interaction: Native article links only.
- Responsive strategy: Magazine spread → stacked lead and two-column stories → single-column mobile issue.
- Composer value: Supports a studio journal with a distinct editorial voice and strong hierarchy.
- Limitation / content ceiling: Best for curated issues; frequent short announcements should use an archive structure.

### ARC-S16-003 — Dense / Information-heavy

- Structural intent / archetype: Chronological press and news archive with visible category affordances.
- Layout model: Filter-style navigation above a five-column desktop index.
- Density: High; six entries expose date, type, title and topic.
- Media mode: No media required.
- Interaction: Native category and entry links; filters are structural affordances, not scripted behavior.
- Responsive strategy: Table-like archive → labeled compact records → narrow two-column records.
- Composer value: Useful for mature studios with mixed news, press and journal inventories.
- Limitation / content ceiling: Functional filtering and pagination would be required during product integration for large archives.

### ARC-S16-004 — Conversion-led

- Structural intent / archetype: Press room that pairs a current story with studio profile, media kit and enquiry paths.
- Layout model: Large feature area with a stacked action panel.
- Density: Medium; one feature and three press-resource modules.
- Media mode: One completely empty featured image slot.
- Interaction: Native story, resource and contact links.
- Responsive strategy: Split press desk → feature followed by full-width resource stack.
- Composer value: Gives editors a short route from context to approved material or contact.
- Limitation / content ceiling: Requires real resource destinations at ingestion; no downloadable files are embedded in the study.

### ARC-S16-005 — Sector-native / Distinctive

- Structural intent / archetype: Architectural pin-up board presenting current stories as numbered working sheets.
- Layout model: Oversized heading above an asymmetric lead, two notes and one wide press file.
- Density: Medium-high visual field with four editorial records.
- Media mode: Four completely empty mixed-ratio image slots.
- Interaction: Native story and press-file links only.
- Responsive strategy: Asymmetric three-column board → two-column board → single-column mobile file.
- Composer value: Gives an architecture practice a recognizably studio-native alternative to a generic news grid.
- Limitation / content ceiling: Best as a current selection of 4–6 items; a complete archive should sit elsewhere.

## Research Metadata

- Research inputs: Workspace authoring standards, Architecture & Interior Design sector taxonomy and the user’s existing preference for blank visual areas.
- Research date: 2026-08-31
- Structural territory rationale: The set covers familiar newsroom, editorial journal, dense archive, press conversion and architecture-native working-board territories.
- Differentiation notes: No publication logo, award, quote, client, ranking, download or factual press claim is embedded. Dates, titles and topics are demonstrative content.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: NONE

## Media Slots

| Study | Slot policy | Expected future type | Accessibility / fallback |
| --- | --- | --- | --- |
| ARC-S16-001 | One empty feature slot | News or project photography | The slot is named; title, category and summary remain complete without media. |
| ARC-S16-002 | Four empty editorial slots | Journal or process photography | Each slot has a story-specific accessible name and adjacent text fallback. |
| ARC-S16-003 | No media slots | — | Archive entries are entirely textual. |
| ARC-S16-004 | One empty feature slot | Current press-story photography | The slot is named and the press actions remain usable without it. |
| ARC-S16-005 | Four empty mixed-ratio slots | Press, process or project photography | Each slot is named; numbered records preserve context without imagery. |

## QA

- ID validation: PASS — five unique IDs with filename, root metadata and JSON metadata agreement.
- Standalone HTML validation: PASS — all five files load independently; HTML Tidy reports no errors or warnings.
- Accessibility baseline: PASS — semantic regions, one clear H1, named empty media, visible keyboard focus, logical source order and practical touch targets verified.
- Responsive QA: PASS — 35 in-browser checks across 1440 / 1280 / 1024 / 768-class / 430 / 390 / 320 widths with no overflow or clipped required content.
- Interaction QA: PASS — all internal targets resolve; native links remain visible, focusable and at least 40 px high at mobile width.
- Dependency validation: PASS — 0 frameworks, CDNs, remote runtime dependencies or executable JavaScript blocks.
- Media-policy validation: PASS — 0 embedded images, SVGs, video, gradients or background-image assets; all ten documented image slots are empty.

## Known Batch Boundaries

- All media areas are intentionally blank and contain no generated or embedded imagery.
- Dates, titles, topic labels and descriptions are illustrative placeholders, not factual studio news.
- Category controls and links demonstrate affordances; filtering, pagination, downloads and destinations are not implemented.
