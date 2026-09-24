# BATCH V1

## Batch Identity

- Sector: Dental Clinics
- Prefix: DN
- Section ID: DN-S21
- Section Name: Subpage Hero
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Research / authoring date: 2026-09-14
- Sector total: 105 studies, S01-S21 authored.
- Example internal page across every variant: Your first visit.

## Planned Studies

| Study ID | Direction | Theme | Shape | Media | Visible words | Composition |
| --- | --- | --- | --- | ---: | ---: | --- |
| DN-S21-001 | Universal / Safe | Chalk | C | 0 | 52 | Open two-column page identity with a small unboxed topic line |
| DN-S21-002 | Premium / Editorial | Linen | B | 1 | 47 | Editorial title and introduction above a contained panoramic reception strip |
| DN-S21-003 | Structured / Visual Modular | Slate | B | 1 | 54 | Centered page identity above a joined media, introduction and topic module |
| DN-S21-004 | Conversion-led | Daylight | C | 0 | 46 | Centered amber-tinted page context with one compact question route |
| DN-S21-005 | Art-directed / Distinctive | Dusk | B | 1 | 46 | Asymmetric dark page title with a low capsule image and offset introduction |

## Research Metadata

Sources: the user's request and continuing preference for modern, visually appealing designs;
this section README; ../DENTAL-THEME-CONTRACT.md; ../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md; the S19 and S20 study and batch records; S22 and S23 scope
definitions; the architecture S21 batch's distinction between page context and a homepage stage.
External references and factual clinical research: NONE.

These five alternatives describe the same internal patient-information page. They orient a reader
before the page body. They do not reintroduce the clinic, repeat a sales proposition or build a
full guide inside the hero. Each has a page-level h1 and a short introduction. Topic labels describe
scope; they are not links, fake controls or an in-page navigation system.

Document-metaphor justification: NONE. Layout, scale, visual grouping and image proportions
differentiate the variants. More text is not used as the structured variant's defining property.
The current authoring directions supersede the old Dense / Information-heavy and Sector-native
direction labels in the original scaffold.

## Section Boundaries

- Page identity rather than S01 homepage positioning.
- No global header, site navigation or footer.
- No breadcrumb trail or sibling navigation: those belong to S22.
- No guide body, treatment details, practitioner records or location details.
- Zero actions in 001, 002, 003 and 005.
- One contextual action in 004: ask about a first visit, opening the existing
  ../../S19-contact/raw/DN-S19-004.html.
- No invented dates, reading times, appointment availability, contact details or clinical claims.

The root is marked data-region="page-context" for future detail-page assembly. The h1 represents
the internal page title; consumers must not add a second competing page title when assembling it.

## Differentiation and Responsive Strategy

- 001 Chalk: open page identity split between title and introduction, followed by a small unboxed
  topic line. On narrow screens the introduction and wrapping topic labels follow the title.
  Shape C: page identity and scope are enough; no photograph is needed.
- 002 Linen: editorial title and introduction above a shallow panoramic reception strip. The
  image stays contained and never sits behind the title. On mobile the text stacks and the image
  reduces to 145px high. Typography is contemporary sans-serif, not a classical document treatment.
- 003 Slate: centered page title above one joined media / introduction / scope module. Tablet wraps
  the scope into a lower row; phone places introduction before the shallow media and wrapping scope.
  This is one cohesive context object, not a collection of text-only cards or an information table.
- 004 Daylight: centered page identity on a soft amber ground with a compact question route below.
  On mobile the contextual note and button stack. Shape C: photography is not needed to understand
  this page; the single question route is subordinate to its title.
- 005 Dusk: asymmetric title, offset introduction and a low capsule-shaped media area. Mobile keeps
  the title first, followed by the introduction and media. No cinematic full-height stage.

S19 shapes: B / B / B / B / B. S20: B / B / B / C / B. S21: C / B / B / C / B.
S21 begins the extended site-architecture catalog and is intended for an internal page rather than
as another homepage section. The comparison still checks for repeated neighbouring compositions.
The existing collision checker assumes CONS filenames; no successful full-sector automated dental
collision scan is claimed.

## Media Slots

| Study | Subject | Purpose | Accessibility / fallback |
| --- | --- | --- | --- |
| 001 | NONE | Page title and scope carry the context | No media required |
| 002 | Clinic reception | Contained panoramic context | Descriptive label, intact shallow frame |
| 003 | Clinic reception | Visual anchor in joined module | Descriptive label; reduced mobile height |
| 004 | NONE | The guide identity and question route carry the context | No media required |
| 005 | Clinic reception | Small visual counterweight | Descriptive label in contained capsule |

No photographs supplied or generated. These are reserved areas, not missing design work.
Approved real clinic photography, provenance and suitable alternative text are required before
real-media ingestion. No fictional portraits or clinical imagery are used.

## Dependencies

Framework: NONE. CDN: NONE. Remote runtime dependency: NONE. JavaScript: NONE.
Fonts: system sans-serif. Icons: text arrow hidden from assistive technology.
CSS is namespaced except the documented html/body host baseline.

## QA

- ID metadata, unique DOM IDs, named page-context sections and one h1: PASS.
- Correct internal page identity in all five: PASS.
- Standalone section shell, no runtime dependencies and no inline styles: PASS.
- At most one contextual action: PASS; its local target exists.
- Chrome 153 at 1440 / 768 / 390 / 320 CSS pixels: PASS, 20 study/viewport combinations.
- Document and element horizontal overflow: NONE in those checks.
- Title precedes media visually at every checked width: PASS.
- Action name, keyboard focus and at least 44px target height in 004: PASS.
- Reduced-motion rules: present in every study.
- Visible copy: 52 / 47 / 54 / 46 / 46 words.
- Desktop and 390px phone screenshots: visually inspected for every study.
- Full screen-reader and cross-browser audit: NOT_RUN.

Phone screenshots use a 390px iframe to avoid the minimum outer Chrome window width on Windows.
Temporary harnesses, logs and captures are in ignored artifacts/dn-s21/.

## Review and Handoff

Preview: ../../../review/dental-subpage-hero.html.
Generator: ../../../review/build-dental-subpage-hero.ps1.
Measured heights: ../../../review/dental-subpage-hero-heights.json.

The scoped gallery supplements the existing architecture, S19 and S20 review pages. It provides
five live previews, viewport switching, variant filtering and links to the standalone files.
No Design Lab selection, promotion or ingestion decision is recorded.

