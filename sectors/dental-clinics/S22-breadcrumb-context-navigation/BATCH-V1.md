# BATCH V1

## Batch Identity

- Sector: Dental Clinics
- Prefix: DN
- Section ID: DN-S22
- Section Name: Breadcrumb / Context Navigation
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Research / authoring date: 2026-09-14
- Sector total: 110 studies, S01-S22 authored.
- Current-page context: the same Your first visit example introduced in S21.

## Planned Studies

| Study ID | Direction | Theme | Shape | Links | Composition |
| --- | --- | --- | --- | ---: | --- |
| DN-S22-001 | Universal / Safe | Chalk | C | 2 | Wrapping breadcrumb in a quiet rounded navigation band |
| DN-S22-002 | Premium / Editorial | Linen | C | 3 | Prominent parent-return link paired with a compact breadcrumb |
| DN-S22-003 | Structured / Visual Modular | Slate | C | 5 | Breadcrumb above a row of related appointment-page links |
| DN-S22-004 | Conversion-led | Daylight | C | 2 | Focusable horizontal breadcrumb rail with a visible narrow-screen scroll cue |
| DN-S22-005 | Art-directed / Distinctive | Dusk | C | 4 | Dark breadcrumb band with paired parent and next-page routes |

## Research Metadata

Sources: the user's request and continuing modern visual direction; this section README;
../DENTAL-THEME-CONTRACT.md; ../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md; S20 and S21 study/batch records; the existing S01, S11, S15,
S17 and S19 destination studies. External references and clinical research: NONE.

The section's job is navigation. No page title, introductory paragraph, clinical claim, brand
positioning, global navigation or decorative media has been added. The current page appears only
as a breadcrumb label. Every actual link opens an existing file with the matching variant.

Document-metaphor justification: NONE. The differences are navigation hierarchy, parent-return
emphasis, related-page capacity, overflow strategy and adjacent-page movement. No technical diagram,
step number, document register or metadata table is presented to the visitor.

## Page Hierarchy and Route Mapping

Breadcrumb hierarchy in all five: Home > Appointments > Your first visit.

| Visible destination | Existing same-variant raw target | Role |
| --- | --- | --- |
| Home | S01-hero/raw/DN-S01-NNN.html | Local root-page surrogate |
| Appointments | S11-appointment-booking/raw/DN-S11-NNN.html | Parent overview |
| Your first visit | Current-page text representing the S21 example | aria-current="page", not a redundant link |
| Getting here | S17-locations/raw/DN-S17-NNN.html | Related arrival information |
| Visit questions | S15-dental-faq/raw/DN-S15-NNN.html | Related FAQ |
| Contact the team | S19-contact/raw/DN-S19-NNN.html | Related contact route |

Paths in the HTML use ../../ from the raw directory. All 16 anchor targets exist.
These are local authoring surrogates rather than production URLs or a claim that the raw studies
form a deployed site. Replace routes during integration while preserving hierarchy and semantics.
The current label is intentionally not linked to the separate S21 fragment; in an assembled page
the visitor is already on that page.

## Five Different Navigation Compositions

- 001 Chalk: the compact wrapping breadcrumb. A quiet white band gives the current location a
  restrained green pill. Small widths wrap complete list items rather than hiding ancestors.
- 002 Linen: parent-return navigation is prominent, with a separate compact breadcrumb. On phones
  the return control leads; the current breadcrumb item occupies its own complete line.
- 003 Slate: breadcrumb above three related-page links. The second named navigation landmark can
  support lateral movement without turning into global navigation. Links become full-width touch
  targets on phones. These are navigation controls, not text-only informational cards.
- 004 Daylight: one continuous, focusable horizontal rail. On narrow screens the path scrolls
  natively rather than wrapping. A visible text/arrow cue and native scrollbar make the overflow
  discoverable. Keyboard focus can reach the rail and its links; both root and current item remain
  reachable. No script or hidden-level menu is required.
- 005 Dusk: breadcrumb above paired overview-return and next-topic routes. The pair stacks on phones
  while preserving labels and arrow directions. The next topic is arrival information, not a
  clinical or appointment-completion step.

## Media, Density and Page Rhythm

All five are shape C, with zero media areas. S22's scope explicitly specifies no media: navigation
does not need a photograph to communicate hierarchy. No subject, asset or alternative text is
fabricated to satisfy a visual template.

S20 shapes: B / B / B / C / B. S21: C / B / B / C / B. S22: C / C / C / C / C.
S21 and S22 are internal-page context roles, not additional homepage sales sections.

Visible language is deliberately limited to destination labels and, for 004 on mobile, a scrolling
cue. The 40-90 word target for prose-bearing hero/CTA/breadcrumb studies is not filled with extra
explanation: that would duplicate S21's responsibility and make this navigation harder to scan.
A compact breadcrumb is allowed to be short. Authoring rationale stays in this document.

The existing composition checker assumes CONS filenames. Its dental invocation is not treated as
evidence of a successful sector-wide comparison; the scope and structural comparison are documented
above.

## Semantics and Dependencies

- Named nav landmarks; names are distinct when a study contains multiple navigation regions.
- The breadcrumb is an ordered list of three hierarchy levels.
- Exactly one aria-current="page" label per study.
- Decorative separators and arrows are aria-hidden.
- Links remain native and functional without JavaScript.
- Root marker: data-region="context-navigation".
- No h1-h6, header, footer, form, media, global navigation or page-body content.
- Framework: NONE. CDN: NONE. Remote runtime dependency: NONE. JavaScript: NONE.
- Fonts: system sans-serif. Styles are namespaced except the documented html/body host baseline.
- No tab roles or simulated tab widgets are used for ordinary links.

## QA

- ID metadata and context-navigation marker: PASS.
- Distinct named landmarks and ordered three-level breadcrumb: PASS.
- Correct non-link current-page label and silent separators: PASS.
- Local destinations: PASS, 16/16 existing matching-variant files.
- Chrome 153 at 1440 / 768 / 390 / 320 CSS pixels: PASS, 20 study/viewport combinations.
- Document horizontal overflow: NONE.
- Out-of-viewport content: NONE outside 004's deliberate internal scroll rail.
- 004 rail: both root and current item can be brought fully into view; visible narrow-screen hint
  and keyboard-focusable scroll container checked.
- Link names, keyboard focus and minimum 44px link height: PASS.
- Reduced-motion rules: present in all five.
- Desktop and 390px phone screenshots: visually inspected for every study.
- Full screen-reader, keyboard key-event scrolling and cross-browser audit: NOT_RUN.

Phone capture uses a 390px iframe to avoid Chrome on Windows' minimum outer window width.
The screenshot runner hides scrollbars; the visible narrow-screen hint still communicates overflow.
Actual browser previews retain native scrollbars. Temporary harnesses and captures are in ignored
artifacts/dn-s22/.

## Review and Handoff

Preview: ../../../review/dental-context-navigation.html.
Generator: ../../../review/build-dental-context-navigation.ps1.
Measured heights: ../../../review/dental-context-navigation-heights.json.

This five-study gallery supplements the earlier review pages and provides viewport switching,
variant filtering and full-size file links. The compact heights are measured from the actual
navigation root rather than from the browser viewport.
No Design Lab review, selection, promotion or ingestion decision is recorded.

