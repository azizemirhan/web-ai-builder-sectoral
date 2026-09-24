# BATCH V1

## Batch Identity

- Sector: Education & Training
- Prefix: EDU
- Section ID: EDU-S26
- Section Name: Instructor / Faculty Profile
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 130 studies, S01-S26 authored.

## Studies

All five studies are AUTHORED. 001, 002 and 005 contain 158 visible words;
003 and 004 contain 153. Every variant describes one reserved instructor profile.

| Study | Direction | Theme | Shape | Media | Composition |
| --- | --- | --- | --- | --- | --- |
| EDU-S26-001 | Universal / Safe | Apricot | B | 1 | Warm identity and portrait beside a continuous teaching biography |
| EDU-S26-002 | Premium / Editorial | Mulberry | B | 1 | Editorial identity and portrait above an open three-column profile |
| EDU-S26-003 | Structured / Visual Modular | Cobalt | C | 0 | Blue identity field with grouped background and teaching modules |
| EDU-S26-004 | Conversion-led | Iris | C | 0 | Open faculty biography with a purple contact panel |
| EDU-S26-005 | Art-directed / Distinctive | Afterhours | B | 1 | Oversized dark identity paired with a curved portrait and lime teaching panel |

## Research Metadata and Scope

Sources: user continuation request; S26 README; education theme contract;
existing S05 instructor index; preceding S24/S25 studies; authoring standard
and media policy. Research date: 2026-09-14. External research: NONE.
Document-metaphor justification: NONE.

The profile reserves name, teaching role, department, subject focus, approved
biography, qualifications, affiliations, teaching approach, current work and
professional contact arrangements. No person, credential, membership, outcome,
testimonial, contact address or social handle is invented. Text in brackets gives
the content responsibility of each field and must be replaced with supplied facts.

Browse programme catalogue reaches the matching S02 study as a local review route.
It does not assert a specific programme association; the confirmed association
belongs in the adjacent reserved field. Contact admissions reaches the matching
S19 study for course and application enquiries. This is a general routing option,
not a direct message to the instructor. The person's approved professional contact
route is separately reserved and requires verification before integration.

## Composition and Responsive Decisions

001 groups identity and portrait in one column with a continuous biography and
teaching description opposite. 002 pairs identity and portrait above three open
content columns. 003 separates identity from background and teaching in coloured
fields. 004 gives contact a prominent purple panel without inserting a form.
005 combines a large name and curved portrait with a lime teaching panel.

Below 800px, all columns return to normal flow: identity and optional portrait,
background, current teaching and contact. The portrait stays inside its identity
group, ensuring the relationship survives every reflow. On phones it is 290px
high and both links use available width. No hidden biography or sticky rail.

Each study is one labelled article with an H2 name and three H3 groups. Scoped
CSS includes explicit border-box sizing, controlled body measure, reduced-motion
treatment and visible keyboard focus. Controls are at least 44px high.
Raw scripts, frameworks, remote assets and runtime dependencies: NONE.

S24: B / B / B / B / B. S25: B / B / C / C / B. S26: B / B / C / C / B.

## Media Slots

Three total, one reserved portrait in 001, 002 and 005. Purpose: identify the
specific instructor whose name appears in the same identity group. Expected type:
approved photographic portrait of that real person with consent to appear.
Each slot has an accessible reserved-portrait label and a visible caption.
The labelled area stays allocated without an asset, while the profile remains
complete. Final imagery requires consent, provenance and licensing, plus alt text
identifying the actual person. Never substitute a fabricated person as evidence.
003 and 004 demonstrate the optional-portrait case without any media.

## QA

- Passed 20 Chrome viewport checks: five variants at 1440, 768, 390 and 320px.
- No document or element overflow; metadata, labelled article and H2 checked.
- Unique IDs, one identity group, three H3 groups and expected media counts checked.
- Both links accept keyboard focus and meet target-height requirements.
- All ten matching S02/S19 destinations exist.
- Five desktop and five phone screenshots visually reviewed, including portrait pairing.
- All variants fit the 150-230-word detail target.
- Gallery passed five frames, filtering, mobile width, pressed states, full-size
  links and restoration. Measured heights support local-file previews.
- Cross-browser and screen-reader testing not run. Design Lab ingestion not performed.

## Review

[Compare five instructor profiles](../../../review/education-profile-detail.html)

Regenerate from repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-profile-detail.ps1

Measured heights: ../../../review/education-profile-detail-heights.json.
Next: S27-location-branch-detail.
