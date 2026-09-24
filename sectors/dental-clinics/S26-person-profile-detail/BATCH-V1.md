# BATCH V1

## Batch Identity

- Sector: Dental Clinics
- Prefix: DN
- Section ID: DN-S26
- Section Name: Dentist / Specialist Profile
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 130 studies, S01-S26 authored.

## Planned Studies

| Study | Direction | Theme | Shape | Portraits | Words | Composition |
| --- | --- | --- | --- | ---: | ---: | --- |
| DN-S26-001 | Universal / Safe | Chalk | B | 1 | 154 | Large portrait and identity split with three open background columns |
| DN-S26-002 | Premium / Editorial | Linen | B | 1 | Centred identity above a portrait flanked by editorial profile text |
| DN-S26-003 | Structured / Visual Modular | Slate | B | 1 | Joined portrait/identity object above open two-by-two biography chapters |
| DN-S26-004 | Conversion-led | Daylight | C | 0 | Large typographic identity and an amber enquiry column |
| DN-S26-005 | Art-directed / Distinctive | Dusk | B | 1 | Arched portrait, oversized identity and staggered biography |

## Research and Data Boundary

Sources: user request for five modern designs; section README;
../DENTAL-THEME-CONTRACT.md; ../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md; S04 team batch and preceding S24/S25 studies.
External research: NONE.

The section demonstrates one person's full profile. No actual clinician information
has been supplied. Name, role, introduction, scope, approach, associated work,
qualifications, awarding institutions and registration remain bracketed reserved
fields with data-placeholder markers. Historical S04 examples are not treated as
verified biographies. No specialist title, qualification, registration, membership,
award, patient quotation, availability, social handle or contact address is invented.

Associated treatments and casework have an explicit reserved field. Person-specific
links require confirmed relationships and therefore are not replaced by arbitrary
cases. The generic clinic overview links do not assert that this person provides
every listed treatment.

Document metaphor: NONE. No CV tables, technical registers, credential badges or
text-only informational cards. The identity object in 003 includes its own portrait;
004's amber field groups actual contact/navigation controls.

## Structure and Responsive Decisions

Each file contains one labelled article and one H1, four profile chapters, an enquiry
route and named clinic navigation. There is no global header or footer.

- 001 pairs a tall portrait with identity, introduction and enquiry; supporting
  background columns stack below 680px. Portrait stays adjacent to its identity.
- 002 keeps the name over one central portrait, with text at either side on desktop.
  At tablet widths the portrait occupies the right column; below 680px it follows
  identity, before the biography.
- 003 joins one portrait and identity into a single rounded object. Open biography
  chapters follow in two columns, stacking below 560px.
- 004 uses no portrait, as explicitly permitted by the section scope. Shape C
  demonstrates a complete profile without imagery; type and amber contact emphasis
  establish hierarchy. The enquiry column follows the biography below 680px.
- 005 uses an arched single portrait alongside identity and enquiry. Below 680px
  it follows identity within the same introduction, and biography offsets release.
- All portrait variants contain exactly one figure. No team grid or ambiguous
  portrait/name pairing is introduced.

S24 shapes: B / B / A / B / B. S25: B / B / B / C / B.
S26: B / B / B / C / B. Manual comparison distinguishes person identity from
case narrative and article reading layouts. The CONS-specific composition checker
is not counted as dental validation.

## Media Register

One reserved portrait in 001, 002, 003 and 005; zero in 004.
Purpose: show the actual person named by the profile, in conversation.
Expected type: a consented photograph of that clinician, without patient identity,
mouth imagery or instruments near a face. No generated portrait or stock face.
Fallback: labelled empty figure, retaining its intended proportions.
Each figure has a visible subject caption and accessible reserved-portrait label.
All biography and contact information remains understandable without photography.
Actual images require provenance, consent, confirmed identity and accurate alt text.

## Routes and Integration

Each study links to the same-variant S19-contact, S04-dentists-specialists and
S02-dental-treatments files. All 15 targets exist. They are local review destinations.
The enquiry goes through the clinic; it does not send a message, book an appointment
or invent a direct personal address. Carry the actual clinician identity into the
contact flow during integration. Add verified associated service/case links when
real profile material is supplied. Replace reserved fields before publication.

## QA Record

- Headless Chrome: 20 viewport checks at 1440, 768, 390 and 320px.
- No document overflow or out-of-viewport elements at those widths.
- Stable metadata, unique IDs, one H1 and labelled root checked.
- Three native links per study; keyboard focus and minimum 44px height checked.
- All 15 local link destinations verified on disk.
- All five desktop and 390px screenshots visually reviewed.
- Visible words: 154 / 154 / 154 / 151 / 154.
- Gallery: five frames, variant filter, mobile width switch, pressed state,
  restore-all and full-size links passed.
- No raw JavaScript, frameworks, external fonts or remote assets.
- Reduced-motion CSS included; git diff --check has no whitespace errors.
- Cross-browser and screen-reader testing were not run.
- No credential verification, production publication or Design Lab ingestion claimed.

## Review

[Compare the five profiles](../../../review/dental-profile-detail.html)

Regenerate from the repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-dental-profile-detail.ps1

Measured heights: ../../../review/dental-profile-detail-heights.json.
Raw HTML remains the source of truth.

