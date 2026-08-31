# BATCH V1 — ARC S19 Project Inquiry

## Batch Identity

- Sector: Architecture & Interior Design
- Prefix: ARC
- Section ID: ARC-S19
- Section Name: Project Inquiry
- Raw Path: `./raw/`
- Batch Status: READY_FOR_INGESTION

## Study Records

### ARC-S19-001 — Universal / Safe

- Structural intent / archetype: Complete two-part project inquiry covering contact and core brief information.
- Layout model: Sticky introduction beside a structured form with grouped fields.
- Density: Medium; seven inputs, consent and one submit action.
- Media mode: No media required.
- Interaction: Native form controls and browser validation only.
- Responsive strategy: Two-column desktop → stacked introduction and form → single-column field flow.
- Composer value: Dependable default for practices needing enough context before the first reply.
- Limitation / content ceiling: File uploads, privacy handling and live delivery must be connected during product integration.

### ARC-S19-002 — Premium / Editorial

- Structural intent / archetype: Minimal inquiry beginning with one open-ended project question.
- Layout model: Large editorial statement paired with a three-field note form.
- Density: Low; idea, email and location only.
- Media mode: No media required.
- Interaction: Native form controls and browser validation only.
- Responsive strategy: Split editorial sheet → stacked statement and form.
- Composer value: Reduces friction for high-touch studios that prefer an initial narrative over a detailed questionnaire.
- Limitation / content ceiling: Collects too little information for qualification or technical scoping.

### ARC-S19-003 — Dense / Information-heavy

- Structural intent / archetype: Detailed operational brief covering contact, type, place, scale, timing, stage and priorities.
- Layout model: Section-labeled desktop form rows with two-column field groups.
- Density: High; structured fields and a radio group.
- Media mode: No media required.
- Interaction: Native inputs, selects, radio controls and browser validation.
- Responsive strategy: Label-and-fields matrix → stacked fieldsets → single-column mobile form.
- Composer value: Useful when a studio needs consistent qualification data before assigning an enquiry.
- Limitation / content ceiling: Longer forms increase abandonment; conditional logic would be needed during integration for complex briefs.

### ARC-S19-004 — Conversion-led

- Structural intent / archetype: Guided inquiry that first reassures users through three common starting situations.
- Layout model: Explanatory pathway panel beside a compact four-field form.
- Density: Medium-low and action-oriented.
- Media mode: No media required.
- Interaction: Native select, textarea, email field and browser validation.
- Responsive strategy: Split pathway/form panel → sequential reassurance followed by form.
- Composer value: Helps visitors begin even when they do not know architecture-service terminology.
- Limitation / content ceiling: The pathways are explanatory only; dynamic branching would require product logic.

### ARC-S19-005 — Sector-native / Distinctive

- Structural intent / archetype: Architecture-specific project sheet framing place, scale, use and priority as coordinates.
- Layout model: Drawing-style header, scale axis and gridded form field.
- Density: Medium-high but diagrammatic.
- Media mode: No media required; the sheet is native HTML/CSS.
- Interaction: Native inputs, radio controls, textarea and browser validation.
- Responsive strategy: Wide brief sheet → vertical-axis single-column mobile form.
- Composer value: Gives an architecture practice a recognizable alternative to a generic contact form.
- Limitation / content ceiling: Works best as an initial outline; technical schedules and documents belong in a later workflow.

## Research Metadata

- Research inputs: Workspace authoring standards, Architecture & Interior Design sector taxonomy and the established requirement to avoid generated visuals.
- Research date: 2026-08-31
- Structural territory rationale: The set covers comprehensive, editorial-minimal, information-dense, conversion-guided and architecture-native brief territories.
- Differentiation notes: No live endpoint, file upload, client data, project claim or external service is embedded.

## Dependency Check

- Framework: NONE
- CDN: NONE
- Remote runtime dependency: NONE
- JavaScript necessity: NONE

## Media Slots

| Study | Slot policy | Expected future type | Accessibility / fallback |
| --- | --- | --- | --- |
| ARC-S19-001 | No media slots | — | Form meaning is entirely semantic and textual. |
| ARC-S19-002 | No media slots | — | Editorial hierarchy uses native type and structure. |
| ARC-S19-003 | No media slots | — | The detailed brief is entirely form-based. |
| ARC-S19-004 | No media slots | — | Guidance and form remain entirely textual. |
| ARC-S19-005 | No media slots | — | Drawing marks are structural CSS and not required for form meaning. |

## QA

- ID validation: PASS — five unique IDs with filename, root metadata and JSON metadata agreement.
- Standalone HTML validation: PASS — all five files load independently; HTML Tidy reports no errors or warnings.
- Accessibility baseline: PASS — semantic form groups, explicit labels, native required states, logical focus order, visible focus and practical touch targets verified.
- Responsive QA: PASS — 35 in-browser checks across 1440 / 1280 / 1024 / 768-class / 430 / 390 / 320 widths with no overflow or clipped required content.
- Interaction QA: PASS — all five forms block empty submission, focus the first invalid field, accept valid sample data and submit only to their own local fragment.
- Dependency validation: PASS — 0 frameworks, CDNs, remote runtime dependencies or executable JavaScript blocks.
- Media-policy validation: PASS — 0 media slots, embedded images, SVGs, video, gradients or background-image assets.

## Known Batch Boundaries

- Forms submit only to their own local fragment and do not transmit or store data.
- Privacy copy, spam protection, upload handling, success/error states and backend delivery remain integration responsibilities.
- All field labels and options are demonstrative placeholders and require project-specific legal/content review.
