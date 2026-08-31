# BATCH V1 — ARC S17 Studio Locations

## Batch Identity

- Sector: Architecture & Interior Design
- Prefix: ARC
- Section ID: ARC-S17
- Section Name: Studio Locations
- Raw Path: `./raw/`
- Batch Status: READY_FOR_INGESTION

## Study Records

### ARC-S17-001 — Universal / Safe

- Structural intent / archetype: Clear three-location card catalogue with address and detail affordances.
- Layout model: Split heading above three equal location cards.
- Density: Medium; three studios with district, address and link.
- Media mode: Three completely empty landscape image slots.
- Interaction: Native studio links only.
- Responsive strategy: Three columns → lead-wide two-column composition → one-column mobile list.
- Composer value: Dependable default for practices with a small, equally weighted studio network.
- Limitation / content ceiling: Best with 2–6 locations; larger networks need regional grouping or search.

### ARC-S17-002 — Premium / Editorial

- Structural intent / archetype: Featured studio portrait followed by two secondary locations.
- Layout model: Large split editorial feature above paired compact studio records.
- Density: Low; one dominant and two supporting locations.
- Media mode: Three completely empty editorial image slots.
- Interaction: Native studio links only.
- Responsive strategy: Feature spread and paired footer → stacked lead and locations → single-column mobile flow.
- Composer value: Gives a principal studio strong narrative presence while keeping the full network visible.
- Limitation / content ceiling: The hierarchy assumes one primary location and works best with exactly 2–4 studios.

### ARC-S17-003 — Dense / Information-heavy

- Structural intent / archetype: Studio directory exposing address, access and local-time information.
- Layout model: Six-column desktop directory transforming into labeled mobile records.
- Density: High; operational detail is visible without media.
- Media mode: No media required.
- Interaction: Native row-detail links only.
- Responsive strategy: Table-like index → compact records retaining logical reading and focus order.
- Composer value: Appropriate when practical visit and access information matters as much as studio identity.
- Limitation / content ceiling: Long addresses and complex transport directions should move to location detail pages.

### ARC-S17-004 — Conversion-led

- Structural intent / archetype: Featured visit path paired with other in-person and remote contact options.
- Layout model: Large visit module beside a stacked connection panel.
- Density: Medium; one principal visit action and three supporting routes.
- Media mode: One completely empty featured studio image slot.
- Interaction: Native visit, directions, studio and conversation links.
- Responsive strategy: Split conversion panel → feature followed by a full-width option stack.
- Composer value: Helps prospective clients move directly from location context to a meeting action.
- Limitation / content ceiling: Real booking, maps and contact destinations must be connected during product integration.

### ARC-S17-005 — Sector-native / Distinctive

- Structural intent / archetype: Architecture-specific coordinate atlas treating studios as points in one shared practice.
- Layout model: Three-column diagram with axis, coordinate codes and circular location marks.
- Density: Medium-high and diagrammatic.
- Media mode: No media required; the network diagram is the content.
- Interaction: Native coordinate links only.
- Responsive strategy: Horizontal atlas → vertically grouped coordinate records with retained codes.
- Composer value: Offers a studio-native alternative to generic maps or address cards.
- Limitation / content ceiling: Best with 2–5 locations; it is conceptual navigation, not a geographic map.

## Research Metadata

- Research inputs: Workspace authoring standards, Architecture & Interior Design sector taxonomy and the established requirement for blank visual areas.
- Research date: 2026-08-31
- Structural territory rationale: The set covers catalogue, editorial, operational directory, conversion and architecture-native atlas territories.
- Differentiation notes: No real address, map, opening hour, phone number, client or geographic claim is embedded. Location data is visibly demonstrative.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: NONE

## Media Slots

| Study | Slot policy | Expected future type | Accessibility / fallback |
| --- | --- | --- | --- |
| ARC-S17-001 | Three empty landscape slots | Studio exterior or interior photography | Each slot is named; address and studio data remain complete outside the slot. |
| ARC-S17-002 | Three empty editorial slots | Studio portrait photography | Each slot is named and paired with a complete studio record. |
| ARC-S17-003 | No media slots | — | Directory information is entirely textual. |
| ARC-S17-004 | One empty feature slot | Principal studio or arrival photography | The slot is named; all visit and contact actions remain usable without media. |
| ARC-S17-005 | No media slots | — | Coordinate relationships are expressed through native HTML/CSS structure. |

## QA

- ID validation: PASS — five unique IDs with filename, root metadata and JSON metadata agreement.
- Standalone HTML validation: PASS — all five files load independently; HTML Tidy reports no errors or warnings.
- Accessibility baseline: PASS — semantic regions, one clear H1, named empty media, structured addresses, visible keyboard focus and practical touch targets verified.
- Responsive QA: PASS — 35 in-browser checks across 1440 / 1280 / 1024 / 768-class / 430 / 390 / 320 widths with no overflow or clipped required content.
- Interaction QA: PASS — all internal targets resolve; native links remain visible, focusable and at least 40 px high at mobile width.
- Dependency validation: PASS — 0 frameworks, CDNs, remote runtime dependencies or executable JavaScript blocks.
- Media-policy validation: PASS — 0 embedded images, SVGs, video, gradients or background-image assets; all seven documented image slots are empty.

## Known Batch Boundaries

- All media areas are intentionally blank and contain no generated or embedded imagery.
- Studio names, addresses, time zones and access notes are illustrative placeholders, not factual location information.
- Links demonstrate affordances; maps, bookings, email delivery and destination pages are not implemented.
