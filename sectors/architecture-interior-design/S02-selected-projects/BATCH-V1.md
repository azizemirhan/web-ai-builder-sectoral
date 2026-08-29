# BATCH V1 — ARC S02 Selected Projects

## Batch Identity

- Sector: Architecture & Interior Design
- Prefix: ARC
- Section ID: ARC-S02
- Section Name: Selected Projects
- Raw Path: `./raw/`
- Batch Status: READY_FOR_INGESTION

## Study Records

### ARC-S02-001 — Universal / Safe

- Structural intent / archetype: Introductory text column paired with a four-project image mosaic, following the supplied featured-projects reference structure.
- Layout model: Narrow editorial introduction + large lead slot + two compact slots + one tall slot.
- Density: Medium; four projects with restrained metadata and detail affordances.
- Media mode: Four completely empty image slots; no generated visual treatment.
- Interaction: Link hover and focus treatment only.
- Responsive strategy: Intro/mosaic desktop split → introduction above a two-column mosaic → single-column mobile project stack.
- Composer value: Reliable default for architecture, interiors, residential, commercial and multidisciplinary studios.
- Limitation / content ceiling: Best with 3–6 projects; hierarchy weakens if the lead project is removed or more than 8 projects are shown.

### ARC-S02-002 — Premium / Editorial

- Structural intent / archetype: Premium paired-project presentation following the supplied selected-residences reference structure.
- Layout model: Large uppercase heading and short introduction above two equal-width, large-format project studies.
- Density: Low; two projects with title, discipline/context, concise description and project affordance.
- Media mode: Two completely empty landscape image slots.
- Interaction: Link hover and focus treatment only.
- Responsive strategy: Paired desktop studies → single-column mobile sequence with metadata moving below each empty slot.
- Composer value: Premium portfolio storytelling for studios with a tightly curated body of work.
- Limitation / content ceiling: Intentionally limited to two featured projects; additional works should continue in another section or index.

### ARC-S02-003 — Dense / Information-heavy

- Structural intent / archetype: Numbered three-project sequence following the supplied horizontal showcase reference structure.
- Layout model: Split heading/introduction above three equal project columns with large numbers and compact metadata.
- Density: Medium; three projects with title, typology, summary and link.
- Media mode: Three completely empty landscape image slots.
- Interaction: Native links only.
- Responsive strategy: Three-column desktop sequence → lead-wide two-column tablet layout → single-column numbered mobile sequence.
- Composer value: Strong comparative rhythm for a small, curated project group.
- Limitation / content ceiling: Best with exactly 3–4 works; additional projects dilute the numbered sequence.

### ARC-S02-004 — Conversion-led

- Structural intent / archetype: Editorial image collage with an integrated studio conversation action, following the supplied collage reference structure.
- Layout model: Six differently sized empty slots arranged around a compact project heading and CTA.
- Density: Medium-high visual field; one named lead work and five supporting image positions.
- Media mode: Six completely empty mixed-ratio image slots.
- Interaction: One native project-inquiry link.
- Responsive strategy: Three-column desktop collage → two-column tablet/mobile collage with the copy moving first.
- Composer value: Supports image-rich portfolio storytelling while preserving a secondary conversion path.
- Limitation / content ceiling: Requires a disciplined six-image set; weak or repetitive imagery would reduce the collage hierarchy.

### ARC-S02-005 — Sector-native / Distinctive

- Structural intent / archetype: Direct six-project catalogue grid following the supplied 3×2 project-gallery reference structure, adapted away from property-sales semantics.
- Layout model: Centered section heading and typology labels above a three-column, two-row project grid.
- Density: Medium-high; six projects with title, typology and project link.
- Media mode: Six completely empty equal-ratio image slots.
- Interaction: Native project links only.
- Responsive strategy: 3×2 desktop catalogue → two-column tablet grid → single-column mobile list.
- Composer value: Fast scanning and broad portfolio coverage with predictable media requirements.
- Limitation / content ceiling: Uniform slots reduce hierarchy; best when all six projects have equally strong imagery.

## Research Metadata

- Research inputs: `selected-projects-sections-1.png` through `selected-projects-sections-5.png`, supplied as structural references only.
- Research date: 2026-08-29
- Structural territory rationale: The reference set suggested grid, editorial collage, structured index, portfolio-plus-action and presentation-sheet territories. Each was reinterpreted for architecture-studio portfolio semantics.
- Differentiation notes: No brand, project name, logo, price, claim, statistic or image from the references was copied or embedded.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: NONE

## Media Slots

| Study | Slot policy | Expected future type | Accessibility / fallback |
| --- | --- | --- | --- |
| ARC-S02-001 | Four empty mixed-size slots | Project photography | Each empty slot has a project-specific accessible name; captions preserve meaning. |
| ARC-S02-002 | Two empty large-format slots | Featured project photography | Each slot is named and paired with complete project text outside the image area. |
| ARC-S02-003 | Three empty equal-format slots | Project photography | Each slot is named; number, title and project metadata remain visible without imagery. |
| ARC-S02-004 | Six empty collage slots | Project photography and details | Each slot has a specific accessible name; the visual field remains intentionally blank. |
| ARC-S02-005 | Six empty equal-ratio slots | Project photography | Each slot is named and paired with architecture-portfolio metadata. |

## QA

- ID validation: PASS — five unique IDs and filename/metadata/root-ID agreement.
- Standalone HTML validation: PASS — all files load independently; HTML Tidy reports no errors or warnings.
- Accessibility baseline: PASS — semantic regions, heading order, named empty media slots, real links, visible focus, practical targets, reduced-motion handling and normal-text contrast checked.
- Responsive QA (1440 / 1280 / 1024 / 768 / 430 / 390 / 320): PASS — 35 in-browser layout checks completed with no horizontal overflow.
- Interaction QA: PASS — native links only; no custom interaction required.
- Dependency validation: PASS — 0 external runtime dependencies.
- Media-policy validation: PASS — every visual slot is empty; 0 embedded images, gradients, SVGs, reference assets, remote media, client marks or evidentiary claims.
- Reference-alignment review: PASS — studies follow the supplied mosaic, paired-project, numbered-sequence, collage and 3×2 catalogue structures without reproducing source brands or content.

## Known Batch Boundaries

- All visible image areas are intentionally blank and contain no generated or embedded imagery.
- Project names and metadata are neutral demonstrative content, not factual portfolio claims.
- Project links demonstrate affordance within standalone studies and do not represent implemented detail pages.
