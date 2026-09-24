# BATCH V1

## Batch Identity

- Sector: Dental Clinics
- Prefix: DN
- Section ID: DN-S27
- Section Name: Clinic Location Detail
- Raw Path: ./raw/
- Batch Status: AUTHORED - PENDING DESIGN LAB INGESTION
- Authoring date: 2026-09-14
- Sector total: 135 studies, all S01-S27 authored.

## Planned Studies

| Study | Direction | Theme | Shape | Media | Words | Composition |
| --- | --- | --- | --- | ---: | ---: | --- |
| DN-S27-001 | Universal / Safe | Chalk | B | 2 | 154 | Address-first opening, entrance diptych and open visit information |
| DN-S27-002 | Premium / Editorial | Linen | B | 1 | 150 | Editorial identity and address beside a tall entrance image |
| DN-S27-003 | Structured / Visual Modular | Slate | B | 2 | Joined identity/address band above reserved map and entrance image |
| DN-S27-004 | Conversion-led | Daylight | C | 0 | 148 | Typographic location with an amber contact panel |
| DN-S27-005 | Art-directed / Distinctive | Dusk | B | 2 | Dark identity, address/arched entrance pairing and reception chapter |

## Research and Content Boundary

Sources: user direction for five modern designs; section README;
../DENTAL-THEME-CONTRACT.md; ../../../standards/01-AUTHORING-STANDARD.md;
../../../standards/03-MEDIA-POLICY.md; S17 locations batch and preceding S25/S26
studies. External research: NONE.

Each design describes one location, not a location index. Name, address, phone,
email, hours, transport, parking, access details, services, team and referral
arrangements are explicitly reserved using data-placeholder fields.
No plausible address, phone number, coordinates, hours, route or access claim is
invented. No historical S17 example is promoted to verified branch data.
The 003 map is an unlocated empty reservation, not a drawing of invented geography.
No map embed, pin, route planner or remote map dependency is present.

The generic arrival note invites questions; it does not promise an accessible
entrance, parking, services or availability. Actual access restrictions have a
dedicated content field. Associated people/services require confirmed branch data
before adding person-specific links.

## Structure and Responsive Decisions

Every file contains one labelled article, one H1, an address element, phone/email
fields, four visit-information chapters and three native links. No global shell.

- 001 pairs identity and address, then two entrance/reception images. The visit
  columns stack below 680px. Address and clinic contact precede both images.
- 002 places identity and address beside the entrance photograph, followed by an
  editorial margin note and continuous practical information. On phones, address
  and enquiry lead; the supporting photograph follows.
- 003 joins identity and address into one object. Below it, the visit narrative
  sits beside the map/entrance pair. At 680px these become a single ordered column.
- 004 is shape C, with an amber contact grouping and open arrival chapters.
  Optional imagery is omitted to demonstrate an address/contact-led location page.
  All required fields remain. Its 148 words sit just below the 150-word target:
  no extra prose is added merely to compensate for absent media captions.
- 005 pairs address and hours with an arched entrance image; reception and care
  information follow. On phones the address, contacts and hours precede imagery.

S25 shapes: B / B / B / C / B. S26: B / B / B / C / B.
S27: B / B / B / C / B. The shape categories recur, but the location layouts are
manually compared with the article and person-profile structures: practical address,
arrival and access hierarchy governs these compositions. No technical drawing,
metadata table or location-index card grid is introduced. The CONS-specific
composition checker is not used to claim dental validation.

## Media Register

Six photo reservations plus one reserved map.

| Subject | Studies | Purpose | Expected type | Fallback |
| --- | --- | --- | --- | --- |
| Clinic entrance | 001, 002, 003, 005 | Recognise the actual entrance | Photograph of this clinic's real entrance | Labelled empty figure |
| Reception from the entrance | 001, 005 | Explain the arrival view | Real reception photograph from the arriving visitor's position | Labelled empty figure |
| Location map | 003 | Reserve orientation context | Verified location material supplied during integration | Empty map area explicitly marked location pending |

All photo reservations have visible subject captions and accessible labels.
No stock faces, patient imagery or anonymous surgery glamour shots.
Actual imagery needs provenance, permission, accurate captions and alt text.
The optional map is an explicit exception to photographic subject categories allowed
by the location-role README. It carries no invented facts and does not replace
the textual address or directions.

## Routes and Integration

Three same-variant local review links per study:
S19-contact (Ask the clinic team), S17-locations (Explore clinic locations) and
S02-dental-treatments (Browse dental treatments). All 15 targets exist.
These are overview/contact routes, not claims that every treatment is offered here.
The enquiry does not send a message or book a visit. Carry the actual location
context into the contact route during integration.

Phone/email placeholders are intentionally plain text; add working tel/mailto
links only after actual values are supplied. No fake directions action is included.
Populate verified branch facts and associated team/service routes before publishing.

## QA Record

- Headless Chrome: 20 checks at 1440, 768, 390 and 320px.
- No document overflow or out-of-viewport elements at tested widths.
- Stable metadata, unique IDs, one H1 and labelled root checked.
- Three native links per study; keyboard focus and 44px minimum height checked.
- All 15 local destinations verified on disk.
- All desktop and 390px screenshots visually reviewed.
- Mobile address/contact appears before reserved media in every variant.
- Words: 154 / 150 / 155 / 148 / 154.
- Gallery: five frames, variant filter, mobile width switch, pressed state,
  restore-all and full-size links passed.
- No raw JavaScript, remote assets or third-party embeds. Reduced-motion CSS included.
- git diff --check has no whitespace errors.
- Cross-browser, screen-reader and real-world arrival testing were not run.
- Sector authoring completion does not imply Design Lab ingestion or production readiness.

## Review

[Compare the five location studies](../../../review/dental-location-detail.html)

Regenerate from the repository root:
powershell -NoProfile -ExecutionPolicy Bypass -File review/build-dental-location-detail.ps1

Measured heights: ../../../review/dental-location-detail-heights.json.
Raw HTML remains the source of truth.

