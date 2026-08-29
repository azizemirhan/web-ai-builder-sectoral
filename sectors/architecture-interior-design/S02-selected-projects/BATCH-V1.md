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

- Structural intent / archetype: Broadly reusable portfolio overview with a clear introduction, one lead project and four supporting projects.
- Layout model: Twelve-column grid; lead project spans two-thirds at wide widths, supporting projects form a regular portfolio matrix.
- Density: Medium; five projects with title, typology/context metadata and project affordance.
- Media mode: Five reserved image slots with a landscape-dominant lead slot.
- Interaction: Link hover and focus treatment only.
- Responsive strategy: 8/4 desktop composition → two-column tablet portfolio → single-column mobile stack with consistent media ratios.
- Composer value: Reliable default for architecture, interiors, residential, commercial and multidisciplinary studios.
- Limitation / content ceiling: Best with 3–6 projects; hierarchy weakens if the lead project is removed or more than 8 projects are shown.

### ARC-S02-002 — Premium / Editorial

- Structural intent / archetype: Art-directed selected-works spread modeled on an architecture monograph rather than a card catalogue.
- Layout model: Asymmetric eleven-column editorial field with a vertical folio, oversized title and four irregular project plates.
- Density: Low; four deliberately spaced projects.
- Media mode: Mixed landscape, portrait, detail and panoramic reserved plates.
- Interaction: Link hover and focus treatment only.
- Responsive strategy: Asymmetric desktop spread → reduced-column editorial field → ordered mobile alternation with controlled insets.
- Composer value: Premium portfolio storytelling for studios with a tightly curated body of work.
- Limitation / content ceiling: Best with 3–5 projects and mixed media orientations; editorial asymmetry simplifies below tablet and loses rhythm above 6 items.

### ARC-S02-003 — Dense / Information-heavy

- Structural intent / archetype: Architecture project register that exposes typology, context, discipline, scope and neutral status without becoming a dashboard.
- Layout model: Structured project table paired with a sticky selectable preview plate.
- Density: High; eight project entries and six metadata dimensions.
- Media mode: One reserved preview slot updated by project selection.
- Interaction: Native buttons update the preview; keyboard activation, pressed state and polite live-region feedback are included.
- Responsive strategy: Full register + sticky preview → reduced metadata columns → preview-first mobile list with project, typology and index retained.
- Composer value: Efficient archive overview for practices whose selection must communicate breadth and discipline.
- Limitation / content ceiling: Requires short project labels and controlled taxonomy; more than 12 entries should move to a dedicated archive page.

### ARC-S02-004 — Conversion-led

- Structural intent / archetype: Portfolio evidence flows into a contextual architecture inquiry without allowing the call to action to dominate.
- Layout model: One large lead case plus two supporting works, followed by a bounded project-conversation module.
- Density: Medium-low; three projects and one secondary inquiry module.
- Media mode: Three reserved project slots with one capability-defining lead image.
- Interaction: Project and inquiry links with visible hover and focus states.
- Responsive strategy: Lead/support split → two-column supporting works → single-column projects with a full-width inquiry action.
- Composer value: Connects selected work to a commission pathway for studios that use portfolio evidence as the primary conversion mechanism.
- Limitation / content ceiling: Best with exactly 3–4 projects; repeated CTAs or extra service modules would overpower the portfolio.

### ARC-S02-005 — Sector-native / Distinctive

- Structural intent / archetype: Drawing-sheet portfolio system pairing overview, detail and diagram slots with architectural annotations.
- Layout model: Bordered presentation board with title block, vertical project numbers, mixed media cells, notes and a sheet schedule.
- Density: Medium-high; three projects with three reading modes each.
- Media mode: Reserved primary image, detail/context and abstract diagram slots.
- Interaction: Project-sheet links only.
- Responsive strategy: Paired desktop sheets → single-column sheets → simplified mobile sheet with stacked main media and compact secondary slots.
- Composer value: Architecture-native storytelling that can carry plans, sections, details and photography in a coherent composition.
- Limitation / content ceiling: Requires disciplined image roles and concise annotations; the technical sheet language is less suitable for purely decorative portfolios.

## Research Metadata

- Research inputs: `selected-projects-sections-1.png` through `selected-projects-sections-5.png`, supplied as structural references only.
- Research date: 2026-08-29
- Structural territory rationale: The reference set suggested grid, editorial collage, structured index, portfolio-plus-action and presentation-sheet territories. Each was reinterpreted for architecture-studio portfolio semantics.
- Differentiation notes: No brand, project name, logo, price, claim, statistic or image from the references was copied or embedded.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: ARC-S02-003 uses small inline vanilla JavaScript for accessible project-preview selection; all other studies require no JavaScript.

## Media Slots

| Study | Slot policy | Expected future type | Accessibility / fallback |
| --- | --- | --- | --- |
| ARC-S02-001 | Lead + four supporting slots | Project photography | Each reserved treatment has a project-specific accessible name; structure remains readable without media. |
| ARC-S02-002 | Four mixed-orientation plates | Editorial project photography/details | Plate purpose and project are named; captions carry the project semantics. |
| ARC-S02-003 | One selectable preview | Project photography | Accessible name updates with selection; full project metadata remains in the register. |
| ARC-S02-004 | Lead + two supporting slots | Capability-oriented project photography | Each slot is named; portfolio and inquiry path remain understandable without imagery. |
| ARC-S02-005 | Primary + detail/context + diagram per project | Photography, detail, plan/section | Every slot has a distinct accessible role; abstract diagrams are explicitly reserved and non-evidentiary. |

## QA

- ID validation: PASS — five unique IDs and filename/metadata/root-ID agreement.
- Standalone HTML validation: PASS — all files load independently; HTML Tidy reports no errors or warnings.
- Accessibility baseline: PASS — semantic regions and heading order, named media slots, real controls, visible focus, keyboard activation, reduced-motion handling and normal-text contrast checked.
- Responsive QA (1440 / 1280 / 1024 / 768 / 430 / 390 / 320): PASS — deliberate transformations checked in-browser with no horizontal overflow at any target width.
- Interaction QA: PASS — ARC-S02-003 preview selection verified by pointer, Enter and visible keyboard focus; other studies use native links only.
- Dependency validation: PASS — 0 external runtime dependencies.
- Media-policy validation: PASS — 0 embedded reference images, remote images, client marks or evidentiary claims.
- Structural diversity review: PASS — grid overview, editorial spread, project register, portfolio-to-inquiry sequence and project-sheet board provide different Composer value; no pair is a cosmetic restyle of the same layout.

## Known Batch Boundaries

- The studies use quiet reserved media treatments, not production imagery.
- Project names and metadata are neutral demonstrative content, not factual portfolio claims.
- Project links demonstrate affordance within standalone studies and do not represent implemented detail pages.
