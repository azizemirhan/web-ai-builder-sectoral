# BATCH V1

## Batch Identity

- Sector: Energy, Solar & Engineering
- Prefix: ENG
- Section ID: ENG-S09
- Section Name: Certifications Standards
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 45 studies; S01-S09 authored.

## Studies

| Study | Direction | Theme | Shape | Composition |
| --- | --- | --- | --- | --- |
| ENG-S09-001 | Universal / Safe | Sunlit | A | Three warm credential summaries with evidence disclosures |
| ENG-S09-002 | Premium / Editorial | Terracotta | A | Editorial rows beneath a split introduction |
| ENG-S09-003 | Structured / Visual Modular | Tidal | A | Featured certification panel beside two supporting groups |
| ENG-S09-004 | Conversion-led | Daybreak | A | Evidence-focused stack beside a concise introduction |
| ENG-S09-005 | Art-directed / Distinctive | Night Current | A | Asymmetric dark columns with a lime central emphasis |

All five studies are AUTHORED. Closed copy is 116 words, or 119 in 004.
Opening the first disclosure increases this to 128 or 131 words respectively.

## Research Metadata and Scope

Sources: user continuation request, section README, sector brief,
../ENERGY-THEME-CONTRACT.md, preceding S07 and S08 studies, authoring standard
and media policy. Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

Certification, applicable standards and professional qualifications are separate
content categories. All provider-specific descriptions and evidence details are
explicit placeholder fields. No certificate, issuer, standard number, qualification,
accreditation, validity date or compliance status is invented. Introductory copy
encourages reading scope in context without claiming credentials for a provider.
The standards disclosure explicitly distinguishes certification from a statement
of conformity. Supply verified scope and official sources before publication.

View evidence details opens the corresponding native details element. Accessible
names identify the category. No fake download buttons, verification links or
external destinations. No global header, footer, raw scripts or remote dependencies.

## Composition, Media and Responsive Decisions

The five themes remain consistent while hierarchy, introduction position, grouping
and action emphasis differ. Media slots: NONE. This is a concise credential-scope
index, not a certificate gallery. No invented seals, logos, badges or certificate
facsimiles are used. Actual documents may be linked once verified sources exist.

S07 was B; S08 and S09 are A across all variants. S10 must use B or C per variant
to avoid a third consecutive item-grid section.

Below 850px, groups stack in certification, standards and qualification order.
Expanded content remains in normal flow. A labelled H2 introduces three labelled
articles with H3 headings. Scoped CSS includes border-box descendants, visible
focus, reduced-motion treatment and controls at least 44px tall.

## QA

- Passed 20 Chrome cases: five variants at 1440, 768, 390 and 320px.
- No document or element overflow when closed, first-open or all-open.
- Metadata, unique IDs, labelled headings and three credential groups checked.
- All disclosures open, close, accept focus and meet target height.
- Five desktop and five phone screenshots visually reviewed.
- Copy meets the ordinary-content 90-170-word target.
- Gallery passed frame count, filtering, mobile width, pressed states, full-size
  links and restoration. Live sizing follows disclosures where permitted;
  measured closed heights support local-file previews otherwise.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.

## Review

[Compare five credential layouts](../../../review/energy-credentials.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-credentials.ps1

Measured heights: ../../../review/energy-credentials-heights.json.
Next: S10-sustainability-impact.
