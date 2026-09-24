# BATCH V1

## Batch Identity

- Sector: Dental Clinics
- Prefix: DN
- Section ID: DN-S23
- Section Name: Dental Treatment Detail
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Research / authoring date: 2026-09-14
- Sector total: 115 studies, S01-S23 authored.
- Example offering: a first dental consultation.

## Planned Studies

| Study | Direction | Theme | Shape | Media | Visible words | Composition |
| --- | --- | --- | --- | ---: | ---: | --- |
| DN-S23-001 | Universal / Safe | Chalk | B | 1 | 186 | Wide image between an open introduction and three content columns |
| DN-S23-002 | Premium / Editorial | Linen | B | 1 | 192 | Offset portrait-format room reservation beside a continuous service narrative |
| DN-S23-003 | Structured / Visual Modular | Slate | B | 2 | 185 | Joined media-led chapters with preparation and enquiry below |
| DN-S23-004 | Conversion-led | Daylight | C | 0 | 209 | Question-led introduction, amber enquiry panel and native disclosures |
| DN-S23-005 | Art-directed / Distinctive | Dusk | B | 1 | Arched media anchor, staggered open copy and a separate lower process sequence |

## Research Metadata

Sources: user direction for five modern, visually appealing studies; section README;
../DENTAL-THEME-CONTRACT.md; ../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md; S02 offering context; preceding S21 and S22
raw/batch records; existing S19 contact destinations. No external references or
clinical research are claimed.

The selected service extends the first-visit context of S21/S22. These are complete
standalone detail studies, not five snippets of one page. The content covers one
consultation: its purpose, discussion scope, suitability, stages, preparation and
specific enquiry route. It does not list every treatment or prescribe a treatment.
Copy is illustrative authoring content, not a verified clinic protocol.

Document-metaphor justification: NONE. Hierarchy uses space, type, colour and media.
No charts, clinical diagrams, technical registers, invented prices, credentials,
outcomes or availability. Content is 185-209 visible words with disclosures open.

## Structural Differentiation and Responsive Behaviour

- 001: a panoramic media anchor separates the introduction from an open three-part
  service story. Three columns become two below 980px and one below 680px.
- 002: an offset tall supporting image sits beside the entire narrative. At 680px
  and below, service information and enquiry lead; the image becomes a short
  supporting closing element. No sticky rail competes with the reading column.
- 003: two joined chapters each carry media: scope/suitability and process. Their
  shared seam makes one composition. Below 560px chapters stack with preparation
  and the enquiry link following. This is an anchored pair (B), not a five-item grid.
- 004: an amber enquiry panel accompanies a large question-led heading. Two native
  details elements start open, exposing the complete service description without
  script. They remain toggleable by keyboard. Below 860px the panel joins normal
  flow; the lower process sequence also stacks. Shape C is intentional: the decision
  and enquiry need emphasis, and a photograph would not explain either.
- 005: staggered paragraphs balance an arched media area on a dark ground; the
  process spans the lower composition. At 680px the offsets release and the image
  sits between the enquiry route and process. Sea-green controls use dark text.

S21 shapes: C / B / B / C / B. S22 shapes: C / C / C / C / C.
S23 shapes: B / B / B / C / B. Manual comparison distinguishes these detail bodies
from S21 introductions and S22 navigation bands. The repository composition checker
assumes CONS filenames; its invocation is not counted as dental validation.

## Media Register

Five reserved areas total: one consultation-room area in 001, 002 and 005;
consultation-room and dentist-in-conversation areas in 003. No media in 004.
All reservations are labelled and the full offering remains understandable empty.
No photographs, generated assets, remote requests, mouth imagery or invented faces.
Future photographs should depict the clinic's actual consultation space or staff;
portrait media stays reserved until suitable real material is supplied.

## Routes and Page Assembly

Every primary link opens the existing same-variant S19-contact study. The secondary
link opens the same-variant S02-dental-treatments overview. All ten local targets
exist; these are review destinations, not deployed URLs. The enquiry link does not
submit a request or claim an appointment is booked. Production integration must
carry the consultation context into the contact destination.

Each standalone study has one internal H1 and a named service-offering-detail section.
When assembling with S21, use one page heading and avoid duplicating the introductory
context. S22 remains separate local navigation. There is no global header or footer.

## QA Record

- Headless Chrome: 20 viewport checks, five studies at 1440, 768, 390 and 320px.
- No document overflow or out-of-viewport elements at the tested sizes.
- Stable metadata, unique IDs, one H1 and labelled root checked.
- All links and summary controls meet the 44px height check and receive keyboard focus.
- Both 004 disclosures start open and toggle closed/open successfully.
- Two local links per study; destination existence verified on disk.
- All five desktop and 390px screenshots reviewed for layout and readable order.
- Gallery: five previews, variant filter, mobile width switch, pressed state,
  restore-all and full-size links checked.
- Raw studies have no JavaScript, external stylesheets, fonts or frameworks.
- Reduced-motion CSS included. Contrast uses the sector's fixed theme colours.
- Cross-browser, screen-reader and live clinic workflow validation have not been run.
- No Design Lab ingestion or selection decision is claimed.

## Review

Open ../../../review/dental-treatment-detail.html.
Regenerate with powershell -NoProfile -ExecutionPolicy Bypass -File review/build-dental-treatment-detail.ps1
from the repository root. Gallery heights are recorded in
../../../review/dental-treatment-detail-heights.json.

