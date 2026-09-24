# BATCH V1

## Batch Identity

- Sector: Dental Clinics
- Prefix: DN
- Section ID: DN-S20
- Section Name: Final Appointment CTA
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Research / authoring date: 2026-09-14
- Sector total: 100 studies, S01-S20 authored.

## Planned Studies

| Study ID | Direction | Theme | Shape | Media | Visible words | Composition |
| --- | --- | --- | --- | ---: | ---: | --- |
| DN-S20-001 | Universal / Safe | Chalk | B | 1 | 59 | Forest invitation banner with an inset reception window |
| DN-S20-002 | Premium / Editorial | Linen | B | 1 | 42 | Tall reception image beside open editorial typography and an understated action |
| DN-S20-003 | Structured / Visual Modular | Slate | B | 1 | 63 | Centered introduction above a joined image, reassurance and action strip |
| DN-S20-004 | Conversion-led | Daylight | C | 0 | 46 | Oversized invitation beside a circular amber appointment action |
| DN-S20-005 | Art-directed / Distinctive | Dusk | B | 1 | 43 | Panoramic reception reservation with a floating centered dark invitation |

## Research Metadata

Sources: the user's current request and continuing direction (modern, visually appealing; no technical
or classic styles), ../DENTAL-THEME-CONTRACT.md, ../../../standards/01-AUTHORING-STANDARD.md,
../../../standards/03-MEDIA-POLICY.md, S11 appointment-booking, S18 resources and S19 contact sources
and batch records. No external references or factual clinical research were used.

The final section closes a page with one primary step and one softer alternative. It does not reopen
the full enquiry workflow. Scale, space, media proportion and action geometry differentiate these
studies; additional prose is not the differentiator. Document-metaphor justification: NONE.

## Differentiation and Responsive Strategy

- 001: green invitation banner and inset arched reception window. On phones the action precedes
  the image; no S19 form column is repeated.
- 002: portrait reception image beside open editorial typography. Mobile changes the image to a
  shallow horizontal frame. No S19 offset contact panel; the font stays contemporary sans-serif.
- 003: centered invitation above one joined image / reassurance / action strip. Tablet places the
  blue action below the first pair; mobile creates a single vertical sequence. No independent card grid.
- 004: type and colour only; a circular amber action becomes a wide pill on phones. The action itself
  supplies the visual anchor. A photograph adds no information needed for this final decision.
- 005: panorama reservation around an inset dark invitation, floating past its lower edge. On phones
  inset margins shrink. This differs from S19's full-width headline and capsule composition.

S18 shapes: B / C / A / B / B. S19: B / B / B / B / B. S20: B / B / B / C / B.
No third consecutive item grid is introduced. The C variant deliberately gives the final decision
breathing space after S19's form and reception image.

The existing composition-collision checker assumes CONS filenames. Its dental invocation is not
used as evidence. The preceding batches were compared directly; no full-sector automated collision
scan is claimed.

## Actions and Dependencies

Exactly two native anchors in every file:
- Primary: ../../S11-appointment-booking/raw/DN-S11-NNN.html.
- Secondary: ../../S19-contact/raw/DN-S19-NNN.html.

All ten targets exist and match the variant. These links navigate existing raw studies, not a
scheduling backend. No invented time slots, prices, contact details, clinical guarantees, urgency
devices or booking confirmations are added. Approved application routes can replace them at ingestion.

Framework: NONE. CDN: NONE. Remote runtime dependency: NONE. JavaScript: NONE.
Fonts: system sans-serif. Icons: text arrows with aria-hidden. CSS is namespaced, apart from the
documented html/body host baseline. No global header, navigation or footer.

## Media Slots

| Study | Reserved subject | Purpose | Accessibility / fallback |
| --- | --- | --- | --- |
| 001 | Clinic reception | Place of arrival | Descriptive label in arched frame; intact empty dimensions |
| 002 | Clinic reception | Editorial counterweight | Descriptive label; portrait-to-landscape transformation |
| 003 | Reception team at work | Human anchor | Reserved only; no fabricated person, face or name |
| 004 | NONE | Action and typography carry the composition | No decorative media needed |
| 005 | Clinic reception | Panoramic surround | Descriptive label remains above the invitation panel |

No photos supplied or generated. Empty slots are intended output. Approved real clinic photography,
provenance and contextual alternative text are required before real-media ingestion.

## QA

- Stable IDs, metadata, unique DOM IDs and named sections: PASS.
- Standalone format and no runtime dependencies: PASS.
- Native link targets: PASS, all 10 resolve to existing matching-variant files.
- Chrome 153 at 1440 / 768 / 390 / 320 CSS pixels: PASS, 20 study/viewport combinations.
- Document and element horizontal overflow: NONE in those checks.
- Anchor names, keyboard focus and minimum 44px target height: PASS.
- Reduced-motion blocks: present in all five.
- Visible copy: 59 / 42 / 63 / 46 / 43 words; within the 40-90 CTA band.
- Desktop and 390px phone screenshots: visually inspected for every study.
- Full screen-reader and cross-browser audit: NOT_RUN.
- Real appointment submission: NOT_IMPLEMENTED; outside this raw batch.

Phone screenshots use an explicitly 390px-wide iframe to avoid Chrome on Windows' minimum outer
window width. Temporary browser harnesses, logs and captures are in ignored artifacts/dn-s20/.
The Daylight word emphasis was reduced to a low highlight stripe so it does not cover the line above.

## Review

Compare: ../../../review/dental-appointment-cta.html.
Regenerate: ../../../review/build-dental-appointment-cta.ps1.
Measured heights: ../../../review/dental-appointment-cta-heights.json.

The scoped gallery supplements the existing architecture and S19 galleries. It provides five live
previews, viewport switching, variant filtering and links to the actual standalone files.
No Design Lab review, selection or ingestion decision is recorded.

