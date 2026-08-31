# BATCH V1 — ARC S24 Project Detail

## Batch Identity

- Sector: Architecture & Interior Design
- Prefix: ARC
- Section ID: ARC-S24
- Section Name: Project Detail
- Raw Path: `./raw/`
- Batch Status: READY_FOR_INGESTION

## Page Scope

Every study is a complete standalone project case-study page rather than an isolated section. Each page includes project navigation, opening title and metadata, a full context/approach/delivery narrative, a documented media sequence, credits or project facts, and a next-project transition.

## Study Records

### ARC-S24-001 — Universal / Safe

- Structural intent / archetype: Complete, broadly reusable case study from project masthead through next-project navigation.
- Layout model: Project title and facts, lead media, three narrative chapters, decision cards, delivery ledger and next project.
- Density: Medium; clear balance between story, facts and five empty media slots.
- Media mode: Lead view, existing/context pair, wide shared-space view and vertical detail view.
- Interaction: Native project, chapter-related and next-project links.
- Responsive strategy: Two-column masthead and chapter rail → single-column narrative preserving exact source order.
- Composer value: Reliable default project-detail architecture for residential, workplace, hospitality and interior work.
- Limitation / content ceiling: Best for 3–5 narrative chapters; larger drawing or specification sets need a dossier variant.

### ARC-S24-002 — Premium / Editorial

- Structural intent / archetype: Long-form editorial case study organized as three chapters: inherit, open and resolve.
- Layout model: Oversized folio masthead, cover image, chapter navigation, alternating long-form stories, statement, image sets and project ledger.
- Density: Medium-low with generous editorial pacing and seven empty media slots.
- Media mode: Cover, vertical project views, two-image detail spread, panorama and final resolved detail.
- Interaction: Native chapter navigation and next-case-study link.
- Responsive strategy: Editorial spreads and alternating columns → linear reading sequence with media adjacent to its chapter.
- Composer value: Premium storytelling for practices that explain design intent through a carefully authored narrative.
- Limitation / content ceiling: Requires strong writing and a disciplined media edit; frequent factual updates are harder than in the dossier model.

### ARC-S24-003 — Dense / Information-heavy

- Structural intent / archetype: Complete technical project dossier with persistent index, strategy matrix, drawing set and credit ledger.
- Layout model: Sticky desktop sidebar beside a structured content file with four indexed sections.
- Density: High; brief, four workstreams, five empty media/drawing slots, delivery summary and eight credit fields.
- Media mode: Lead project view, plan, section, detail and completed-room record.
- Interaction: Native dossier table of contents and next-dossier link.
- Responsive strategy: Sticky two-column dossier → top project header with two-column mobile/tablet index → compact labeled records.
- Composer value: Strong evidence format for complex civic, workplace, reuse or multidisciplinary projects.
- Limitation / content ceiling: Detailed tables require concise field values; very large drawing registers need a dedicated document viewer.

### ARC-S24-004 — Conversion-led

- Structural intent / archetype: Full case study connecting project evidence to related expertise and a similar-project enquiry.
- Layout model: Project masthead, summary proof strip, context story, image sequence, delivered-scope panel, related services and CTA.
- Density: Medium; five empty media slots and a clear conversion path after the evidence.
- Media mode: Lead, vertical threshold, paired workspace sequence and delivered detail.
- Interaction: Native service, related-project CTA and next-project links.
- Responsive strategy: Two-column evidence layouts → single-column narrative; CTA becomes a full-width mobile action.
- Composer value: Useful when project pages are a principal route into new-business conversations.
- Limitation / content ceiling: The CTA must remain secondary to the project evidence; real service and enquiry destinations are required at integration.

### ARC-S24-005 — Sector-native / Distinctive

- Structural intent / archetype: Complete architecture case study presented as a drawing issue set.
- Layout model: Title block, five-part sheet index, cover sheet, project brief, four-sheet drawing set, design notes, delivery schedule, credits and next set.
- Density: High and architectural; five empty project/drawing slots plus structured technical records.
- Media mode: Cover, ground plan, long section, arrival sequence and interior/landscape record.
- Interaction: Native sheet index and next-drawing-set link.
- Responsive strategy: Wide title block, sheet register and paired drawings → vertical indexed issue set with compact tables.
- Composer value: Distinctive project evidence for architecture practices accustomed to plans, sections, drawing codes and issue registers.
- Limitation / content ceiling: This is an interpretive web structure, not a substitute for downloadable construction documentation or a CAD viewer.

## Research Metadata

- Research inputs: S24 workspace role definition, workspace authoring/accessibility/responsive/media standards, and the user’s explicit request for complete project detail pages.
- Research date: 2026-08-31
- Structural territory rationale: The batch covers universal narrative, editorial long-form, technical dossier, conversion-led evidence and architecture-native drawing-set territories.
- Differentiation notes: No project, client, location, consultant, completion status, outcome, statistic, quote or award is presented as factual. All visible project data is neutral demonstrative content.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: NONE

## Media Slots

| Study | Slot policy | Expected future type | Accessibility / fallback |
| --- | --- | --- | --- |
| ARC-S24-001 | Five empty mixed-ratio slots | Project photography, context and detail views | Every slot has a project-specific accessible name; the full context/approach/delivery narrative remains outside media. |
| ARC-S24-002 | Seven empty editorial slots | Cover, spatial sequence and material detail photography | Each slot is chapter-specific; all design reasoning remains readable when media is absent. |
| ARC-S24-003 | Five empty project/drawing slots | Lead photography, plan, section, detail and record view | Drawing captions and dossier text retain purpose and sequence without assets. |
| ARC-S24-004 | Five empty mixed-ratio slots | Lead, threshold, workspace and delivered-detail photography | Each slot is named; situation, response, delivery and CTA remain complete without imagery. |
| ARC-S24-005 | Five empty issue-sheet slots | Cover photography, plan, section and spatial records | Sheet titles, codes and captions identify every missing asset and preserve the drawing-set logic. |

## QA

- ID validation: PASS — five unique IDs with filename, root metadata and JSON metadata agreement.
- Standalone HTML validation: PASS — all five complete pages load independently; HTML Tidy reports no errors or warnings.
- Accessibility baseline: PASS — one H1 per page, semantic project/chapter structure, named empty media, labeled data tables, coherent source order, visible focus and practical touch targets verified.
- Responsive QA: PASS — 35 in-browser full-page checks across 1440 / 1280 / 1024 / 768-class / 430 / 390 / 320 widths with no overflow or clipped required content.
- Interaction QA: PASS — all project, chapter, dossier, service, CTA and next-project targets resolve; representative navigation links place their target in the visible viewport.
- Dependency validation: PASS — 0 frameworks, CDNs, remote runtime dependencies or executable JavaScript blocks.
- Media-policy validation: PASS — all 27 media slots are empty and accessibly named; 0 embedded images, SVGs, video, gradients or background-image assets.

## Known Batch Boundaries

- All project names, locations, dates, disciplines, stages, teams, consultants and narratives are illustrative placeholders.
- All 27 media areas are intentionally blank and contain no generated or embedded imagery.
- Links demonstrate project, chapter, service, enquiry and next-project affordances but do not represent implemented destination pages.
- Real project pages require verified facts, licensed media, final accessibility text, approved credits and evidence review before ingestion.
