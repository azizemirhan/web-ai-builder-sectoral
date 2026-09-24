# BATCH V1

## Batch Identity

- Sector: Dental Clinics
- Prefix: DN
- Section ID: DN-S19
- Section Name: Contact
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Date: 2026-09-14
- Sector total after this batch: 95 studies across S01-S19.

## Planned Studies

| Study ID | Authoring direction | Theme | Shape | Media | Composition |
| --- | --- | --- | --- | ---: | --- |
| DN-S19-001 | Universal / Safe | Chalk | B | 1 | Balanced welcome and reception image beside a message form |
| DN-S19-002 | Premium / Editorial | Linen | B | 1 | Oversized editorial heading, wide reception image and offset terracotta contact panel |
| DN-S19-003 | Structured / Visual Modular | Slate | B | 3 | One large visit module and two compact contact modules with dedicated media |
| DN-S19-004 | Conversion-led | Daylight | B | 1 | Centered invitation above an amber topic-and-message canvas and slim reception image |
| DN-S19-005 | Art-directed / Distinctive | Dusk | B | 1 | Oversized two-line conversation typography wrapping a capsule image with open contact routes |

## Research Metadata

- Sources: the user's explicit direction (modern, visually appealing; no technical or classic styles);
  ../DENTAL-THEME-CONTRACT.md; ../../../standards/01-AUTHORING-STANDARD.md;
  ../../../standards/03-MEDIA-POLICY.md; S17 and S18 batch records and existing study source.
- Research date: 2026-09-14.
- No external visual references or factual clinical research were used.
- Visual-first check: scale, open space, image proportions, offset composition, modular grouping
  and the relationship between contact routes differentiate the studies. More copy is not the differentiator.
- Document-metaphor justification: NONE.
- All five retain the established theme ground, ink and accent. Linen uses contemporary sans-serif
  display typography; its editorial direction does not introduce classical or document styling.

## Differentiation and Page Rhythm

S17 shapes: B / A / B / B / C. S18 shapes: B / C / A / B / B.
S19 shapes: B / B / B / B / B. No new run of item grids is introduced.

- 001: balanced welcome/image area and a separate form; stacked reading order on narrow screens.
- 002: wide media with a terracotta contact panel offset over its edge; the panel becomes a contained
  overlap below the image on phones. The two direct routes are unboxed below the composition.
- 003: a large visit module next to two compact, media-bearing contact modules; tablet uses a large
  lead module above a pair, while mobile becomes one vertical sequence.
- 004: centered invitation above a topic selector and short message form; the slim arched reception
  image moves below the form on narrow screens. It prepares a general enquiry, not a booking.
- 005: oversized two-line typography and a capsule image above open call/email routes; mobile moves
  the image below the words and stacks the routes. No decorative dental symbols or technical motif.

The current check-composition-collisions.js assumes CONS filenames even when given dental-clinics.
Its empty-sector result must not be treated as evidence. Comparison with the two preceding batches
is recorded above; no claim of a successful full-sector collision scan is made.

## Content and Interaction

All variants include telephone, email, address and reception-hour fields through native disclosures.
These fields are explicitly reserved as [Clinic telephone], [Clinic email], [Clinic address],
[Town / postcode] and [Opening days and hours], with data-placeholder="true".
No real person, location, opening schedule, response-time promise or clinical outcome is invented.

001 and 004 use a small inline vanilla script for form validation, local message review and copying.
They do not send, store, log or upload any data. They never report a message as sent. Copy failure
selects the prepared text for manual copying. Input changes invalidate the prepared preview.
Labels, error handling and status feedback remain in the section. Wiring an approved clinic contact
destination is a future integration concern, not simulated as a successful submission.

002, 003 and 005 need no JavaScript.

## Dependency Check

- Framework: NONE.
- CDN: NONE.
- Remote runtime dependency: NONE.
- Fonts: system sans-serif stack.
- Icons: simple text arrows, hidden from assistive technology.
- JavaScript necessity: local message preparation in 001 and 004 only.
- Forms: no backend, network request, storage, upload or third-party embed.

## Media Slots

| Study | Slot | Purpose | Expected type | Accessibility / fallback |
| --- | --- | --- | --- | --- |
| 001 | Reception area | Anchor the invitation in the place of arrival | Approved real reception photo | Descriptive slot label; intact dimensions without media |
| 002 | Clinic reception | Wide visual anchor for contact panel | Approved real reception photo | Descriptive slot label; panel readable on its own |
| 003 | Clinic reception | Visit route | Approved real reception photo | Descriptive slot label |
| 003 | Reception team at work | Telephone route | Consented real staff photo, mid-work | No invented name or portrait; descriptive slot label |
| 003 | Consultation room | Written enquiry route | Approved real consultation-room photo | Descriptive slot label |
| 004 | Reception area | Alternate telephone route | Approved real reception photo | Descriptive slot label; narrow-screen repositioning |
| 005 | Reception team at work | Human anchor for the invitation | Consented real staff photo, mid-work | Reserved capsule, no fabricated portrait |

No image assets have been supplied or generated. Actual photography must have approved provenance
and context-appropriate alternative text before ingestion. Empty media areas are intended output.

## QA

- ID and metadata validation: PASS (5 stable IDs; consistent metadata; unique DOM IDs).
- Raw-format and dependency validation: PASS (standalone HTML, scoped CSS, no remote assets or network calls).
- Section-shell and visible-copy check: PASS (contact section only; authoring rationale stays in metadata and this record).
- Responsive rendering and overflow: PASS in Chrome 153 at 1440, 768, 390 and 320 CSS pixels: 20 study/viewport combinations, zero document overflow; expanded disclosures and message previews also checked. All five desktop and phone screenshots visually inspected.
- Accessibility and interaction checks: PASS for targeted label, focus, 44px button/summary target, native disclosure, form validation, whitespace rejection, safe text preview and edit invalidation checks. Foreground/ground token contrast verified; secondary body text exceeds 5.9:1 across themes. Reduced-motion rules present in all five. This is not a full accessibility certification.
- Full assistive-technology audit: NOT_RUN.
- Production submission: NOT_IMPLEMENTED, deliberately outside this raw batch.

## Review

The existing Python review generator only collects architecture studies. This batch has a separate,
repeatable five-study contact sheet at ../../../review/dental-contact.html, generated by
../../../review/build-dental-contact.ps1 without Python or a framework. The architecture gallery
and other authored studies are preserved.

### Browser verification notes

- Gallery: five live file previews, variant filtering, mobile width switching, pressed state and
  full-size study links verified in Chrome.
- Visual corrections: explicit border-box sizing fixes Chromium summary sizing across the details
  boundary; reception media has an explicit width on the narrow form layout.
- Phone screenshots use a 390px iframe inside the capture window. Chrome on Windows enforces a
  minimum top-level layout width, so a 390px screenshot alone does not prove a 390px layout.
- Actual screenshot artifacts and browser-check harnesses live in ignored artifacts/dn-s19/.
- Clipboard success and fallback were inspected in source; system clipboard permissions vary.
- Safari, Firefox, screen-reader testing and production contact delivery were not performed.