# Review Contact Sheet

A local viewing aid for the Sector Design Authoring Workspace.

`index.html` shows every authored raw study on one page, grouped by section, in two columns,
with a live preview of each study rendered from the real file.

## Scope boundary

This directory is **not** part of the study batch and **not** the Design Lab gallery.

- It contains no studies, and nothing here is intended for ingestion.
- It records no review, normalisation, survivor-selection, or promotion decision. Those belong
  to Design Lab, per `standards/07-DESIGN-LAB-INGESTION-HANDOFF.md`.
- It exists so authored work can be looked at side by side while authoring continues.

## Usage

Open `review/index.html` in a browser.

- The **Desktop 1440 / Tablet 768 / Phone 390** control re-renders every preview at that
  viewport width, so responsive behaviour can be compared across studies at a glance.
- **Open study** loads the raw file itself in a new tab, at full size.
- Previews are the actual study files in iframes, scaled down — not screenshots. Anything that
  renders here is what the file really does, including the two studies that use JavaScript.

### PDF export

**PDF üret** opens a picker. Sections can be selected in bulk or opened up to tick individual
studies; **Tümünü seç** / **Temizle** select or clear everything at once. Two options sit above the
list: paper (**A3 landscape**, default, or A4 landscape) and which device widths to include.

**Sayfaları hazırla** builds one landscape page per selected study — desktop 1440, tablet 768 and
phone 390 side by side, each scaled so the *whole* study fits the page height — then opens the
browser's print dialog, where **Save as PDF** produces the file. The preview stays on screen, so
**Yazdır / PDF olarak kaydet** can be pressed again without rebuilding, and **← Listeye dön**
returns to the contact sheet.

Two things worth knowing:

- The pages are live iframes, not screenshots, so they are rendered at print time and are as
  sharp as the printer allows. Preparing many pages at once is slow; the picker warns past 40.
- Scale-to-fit needs each study's real height at each width. Every authored study is measured at
  build time and its height is written into the page, so the fit is right from the first paint;
  where the browser can also read into the iframe (served over HTTP, see above) it re-measures and
  refines. A study that has never been measured falls back to a generous default, which may print
  with space at the bottom — no ARC study is currently in that state.

If a browser refuses to load local iframes, serve the workspace over HTTP instead:

    python3 -m http.server 8000

then open `http://localhost:8000/review/index.html`.

## Regenerating

    python3 review/build-index.py               # measure changed studies, then build
    python3 review/build-index.py --no-measure  # build with cached or default heights
    python3 review/build-index.py --pdf         # also print the whole sector to
                                                # review/architecture-contact-sheet.pdf

**Workspace convention: a section is not finished until this page has been regenerated.** Run the
generator as part of section close-out and stage `review/index.html` in the same commit as the
studies, alongside the section `BATCH-V1.md`, the section README, and the sector README row. The
page is generated rather than hand-written, so it goes stale silently — and a stale contact sheet
is worse than none, because it looks complete while missing exactly the work being reviewed. The script scans `sectors/*/S*/raw/*.html`, reads each
study's `<meta>` research fields, and falls back to the section's `BATCH-V1.md` for the
territory where a study predates the `<meta>` convention — which is currently the case for the
`ARC-S02` studies, authored in a separate pass with a different batch format.

Before writing the page, the generator measures each study's rendered height at 1440, 768 and 390
pixels wide by loading it in headless Chrome, and caches the numbers in `review/.heights.json`
keyed by a hash of the file and by a measuring-method version. Only new, changed, or
differently-measured studies are re-measured.

How the measurement works, and why it is shaped this way:

- A run loads twelve studies at once, each in a static iframe, and reads their heights on the
  page's `load` event. The frames are in the markup rather than created from script because a
  document's load event waits for its frames; building them from script needs a virtual clock,
  which turned a two-second run into a stall.
- The frames are as tall as a real screen — 900px at 1440, 1024px at 768, 844px at 390 — so a study
  sized in `vh` resolves against a plausible viewport instead of an arbitrary probe height. Below
  the frame height the body's own box is measured rather than `scrollHeight`, which can never
  report less than the viewport; that is what stops a breadcrumb from claiming 300px.
- **`--dump-dom` writes the DOM as soon as the page has loaded, but the browser does not reliably
  exit afterwards** — Chrome's updater keeps the process alive — so waiting for the process to end
  waits forever. The run watches the dump for its end marker instead and stops the browser it
  started. Only the process this script launched is ever stopped; a browser you have open is not
  touched.
- A run that fails takes its whole group with it, so failed groups are retried four at a time and
  then one at a time. Anything still unmeasured is listed by name at the end and keeps the default
  height until a later build picks it up.

`--no-measure` skips the step entirely, and if no Chrome-family browser is installed the generator
says so and uses defaults. None of this affects the contact sheet itself; it only affects how
tightly the PDF export can fit a study to its page.

`--pdf` prints the whole sector without the browser dialog: it lays the same pages out from the
same measured heights into a standalone print view, one A3-landscape page per study with the three
widths side by side, and renders it with headless Chrome to
`review/architecture-contact-sheet.pdf`. The file is a build artifact and is not tracked in git —
regenerate it when the studies change. The picker in the page remains the interactive route and
the way to print a subset.

The generator has no dependencies beyond the Python standard library. Headless Chrome is optional
and used only for measurement.

## Dental S19 Contact

Open [dental-contact.html](dental-contact.html) to compare DN-S19-001 through DN-S19-005.
It offers 1440 / 768 / 390 preview widths, variant filtering and links to the actual standalone files.

Regenerate from the workspace root on Windows:

    powershell -NoProfile -ExecutionPolicy Bypass -File review/build-dental-contact.ps1

ExecutionPolicy Bypass applies only to this command. No system policy is changed.
The generator reads the five raw files and their metadata; dental-contact-heights.json holds the
measured closed-state heights. Serve the workspace over HTTP for automatic resizing after opening
contact details or preparing a message. Full-size study links work independently of preview sizing.

This scoped contact sheet supplements the existing architecture gallery; build-index.py still owns
that gallery. It records no Design Lab review or ingestion decision.
## Dental S20 Final Appointment CTA

Open [dental-appointment-cta.html](dental-appointment-cta.html) to compare DN-S20-001 through DN-S20-005
at desktop, tablet and phone widths. Primary links lead to matching S11 appointment-option studies;
secondary links lead to matching S19 contact studies. No appointment is submitted or confirmed.

Regenerate from the workspace root:

    powershell -NoProfile -ExecutionPolicy Bypass -File review/build-dental-appointment-cta.ps1

The generator reads the five raw files and their metadata. Closed-state heights are recorded in
dental-appointment-cta-heights.json. This supplements the architecture and S19 review pages.
## Dental S21 Subpage Hero

Open [dental-subpage-hero.html](dental-subpage-hero.html) to compare DN-S21-001 through DN-S21-005.
All five introduce the same internal page, Your first visit. Two omit media; only 004 has a
contextual action, leading to S19 contact. These are page-context blocks, not homepage heroes.

Regenerate from the workspace root:

    powershell -NoProfile -ExecutionPolicy Bypass -File review/build-dental-subpage-hero.ps1

The generator reads the five raw files and their metadata. Measured heights are in
dental-subpage-hero-heights.json. The page offers viewport switching, variant filtering and
full-size file links, alongside the existing review galleries.
## Dental S22 Breadcrumb / Context Navigation

Open [dental-context-navigation.html](dental-context-navigation.html) to compare DN-S22-001 through
DN-S22-005. Each is a compact navigation-only study for the S21 first-visit page context.
004 deliberately scrolls its path on narrow screens; the other variants wrap.

Regenerate from the workspace root:

    powershell -NoProfile -ExecutionPolicy Bypass -File review/build-dental-context-navigation.ps1

The generator reads the raw files and their metadata. Actual navigation-root heights are in
dental-context-navigation-heights.json. The gallery offers viewport switching, variant filtering
and full-size file links alongside the earlier review pages.
## Dental S23 Dental Treatment Detail

[dental-treatment-detail.html](dental-treatment-detail.html) presents five modern consultation detail studies with variant selection and desktop, tablet and mobile previews.

Regenerate from the repository root: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-dental-treatment-detail.ps1

Measured preview heights: dental-treatment-detail-heights.json. Raw files remain the source of truth.

## Dental S24 Treatment Case Context Detail

[dental-case-detail.html](dental-case-detail.html) contains five anonymised case-detail designs with reserved case content and media, variant selection and desktop/tablet/mobile previews.

Regenerate from the repository root: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-dental-case-detail.ps1

Measured preview heights: dental-case-detail-heights.json.

## Dental S25 Patient Guide Detail

[dental-article-detail.html](dental-article-detail.html) contains five modern article layouts with variant selection and desktop/tablet/mobile previews.

Regenerate from the repository root: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-dental-article-detail.ps1

Measured preview heights: dental-article-detail-heights.json.

## Dental S26 Dentist Profile Detail

[dental-profile-detail.html](dental-profile-detail.html) contains five modern single-person profiles with variant selection and desktop/tablet/mobile previews.

Regenerate from the repository root: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-dental-profile-detail.ps1

Measured preview heights: dental-profile-detail-heights.json.

## Dental S27 Clinic Location Detail

[dental-location-detail.html](dental-location-detail.html) contains five modern location studies with variant selection and desktop/tablet/mobile previews.

Regenerate from the repository root: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-dental-location-detail.ps1

Measured preview heights: dental-location-detail-heights.json.

## Education S01 Hero

[education-hero.html](education-hero.html) shows five education hero designs with variant selection and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-hero.ps1

Measured heights: education-hero-heights.json, including room for expanded catalogue status.

## Education S02 Programs Courses

[education-programmes.html](education-programmes.html) shows five programme catalogue layouts with expandable information and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-programmes.ps1

Measured heights: education-programmes-heights.json.

## Education S03 Course Categories

[education-categories.html](education-categories.html) shows five category layouts with expandable subject scope, catalogue links and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-categories.ps1

Measured heights: education-categories-heights.json.

## Education S04 Learning Outcomes

[education-outcomes.html](education-outcomes.html) shows five outcome layouts with assessment disclosures, catalogue links and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-outcomes.ps1

Measured heights: education-outcomes-heights.json.

## Education S05 Instructors Faculty

[education-faculty.html](education-faculty.html) shows five faculty layouts with portrait slots, expandable backgrounds and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-faculty.ps1

Measured heights: education-faculty-heights.json.

## Education S06 Curriculum Learning Path

[education-curriculum.html](education-curriculum.html) shows five learning-path layouts with expandable stage content and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-curriculum.ps1

Measured heights: education-curriculum-heights.json.

## Education S07 Admissions Enrollment

[education-admissions.html](education-admissions.html) shows five admissions layouts with preparation steps, expandable information and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-admissions.ps1

Measured heights: education-admissions-heights.json.

## Education S08 School Stats

[education-stats.html](education-stats.html) shows five statistics layouts with reserved figures, source disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-stats.ps1

Measured heights: education-stats-heights.json.

## Education S09 Student Testimonials

[education-testimonials.html](education-testimonials.html) shows five student-story layouts with reserved quotations, portrait areas and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-testimonials.ps1

Measured heights: education-testimonials-heights.json.

## Education S10 Student Projects

[education-projects.html](education-projects.html) shows five student-project galleries with image slots, expandable process information and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-projects.ps1

Measured heights: education-projects-heights.json.

## Education S11 Accreditations

[education-accreditations.html](education-accreditations.html) shows five accreditation layouts with scope fields, verification disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-accreditations.ps1

Measured heights: education-accreditations-heights.json.

## Education S12 Campus Facilities

[education-campus.html](education-campus.html) shows five campus layouts with reserved facility photographs, access disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-campus.ps1

Measured heights: education-campus-heights.json.

## Education S13 Events Webinars

[education-events.html](education-events.html) shows five event layouts with reserved session information, joining disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-events.ps1

Measured heights: education-events-heights.json.

## Education S14 Resources Downloads

[education-resources.html](education-resources.html) shows five resource layouts with file context, availability notices, native details and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-resources.ps1

Measured heights: education-resources-heights.json.

## Education S15 FAQ

[education-faq.html](education-faq.html) shows five FAQ layouts with six native disclosures, two topics and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-faq.ps1

Measured heights: education-faq-heights.json.

## Education S16 Tuition Pricing

[education-tuition.html](education-tuition.html) shows five tuition layouts with fee context, payment/cancellation disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-tuition.ps1

Measured heights: education-tuition-heights.json.

## Education S17 Scholarships Funding

[education-funding.html](education-funding.html) shows five funding layouts with eligibility context, application disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-funding.ps1

Measured heights: education-funding-heights.json.

## Education S18 Locations Online Learning

[education-locations.html](education-locations.html) shows five campus and online-learning comparisons with access disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-locations.ps1

Measured heights: education-locations-heights.json.

## Education S19 Contact Admissions

[education-contact.html](education-contact.html) shows five admissions contact layouts with enquiry guidance and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-contact.ps1

Measured heights: education-contact-heights.json.

## Education S20 Final Apply Enroll CTA

[education-final-cta.html](education-final-cta.html) shows five final CTA layouts with admissions and programme links, plus desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-final-cta.ps1

Measured heights: education-final-cta-heights.json.

## Education S21 Subpage Hero

[education-subpage-hero.html](education-subpage-hero.html) shows five admissions internal-page heroes with a single contextual link and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-subpage-hero.ps1

Measured heights: education-subpage-hero-heights.json.

## Education S22 Breadcrumb Context Navigation

[education-context-navigation.html](education-context-navigation.html) shows five breadcrumb and admissions topic-navigation layouts with desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-context-navigation.ps1

Measured heights: education-context-navigation-heights.json.

## Education S23 Student Service Detail

[education-service-detail.html](education-service-detail.html) compares five admissions guidance service layouts with desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-service-detail.ps1

Measured heights: education-service-detail-heights.json.

## Education S24 Cohort Case Detail

[education-case-detail.html](education-case-detail.html) compares five cohort case layouts with three reserved evidence images per study and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-case-detail.ps1

Measured heights: education-case-detail-heights.json.

## Education S25 Article Research Detail

[education-article-detail.html](education-article-detail.html) compares five article layouts with complete short editorial copy and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-article-detail.ps1

Measured heights: education-article-detail-heights.json.

## Education S26 Instructor Faculty Profile

[education-profile-detail.html](education-profile-detail.html) compares five instructor profile layouts with desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-profile-detail.ps1

Measured heights: education-profile-detail-heights.json.

## Education S27 Campus Learning Location Detail

[education-campus-detail.html](education-campus-detail.html) compares five campus detail layouts with desktop/tablet/mobile previews. Education S01-S27 now contains 135 authored studies.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-education-campus-detail.ps1

Measured heights: education-campus-detail-heights.json.

## Energy S01 Hero

[energy-hero.html](energy-hero.html) compares five energy and solar hero layouts with native project-preparation guidance and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-hero.ps1

Measured heights: energy-hero-heights.json.

## Energy S02 Solutions Services

[energy-solutions.html](energy-solutions.html) compares five service layouts with native scope disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-solutions.ps1

Measured heights: energy-solutions-heights.json.

## Energy S03 Industries Applications

[energy-applications.html](energy-applications.html) compares five application layouts with native discussion disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-applications.ps1

Measured heights: energy-applications-heights.json.

## Energy S04 Projects

[energy-projects.html](energy-projects.html) compares five project spotlights with native context disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-projects.ps1

Measured heights: energy-projects-heights.json.

## Energy S05 Capabilities

[energy-capabilities.html](energy-capabilities.html) compares five capability layouts with native disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-capabilities.ps1

Measured heights: energy-capabilities-heights.json.

## Energy S06 Technology Systems

[energy-technology.html](energy-technology.html) compares five technology layouts with reserved imagery, native disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-technology.ps1

Measured heights: energy-technology-heights.json.

## Energy S07 Infrastructure Equipment

[energy-infrastructure.html](energy-infrastructure.html) compares five infrastructure layouts with reserved imagery, native readiness disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-infrastructure.ps1

Measured heights: energy-infrastructure-heights.json.

## Energy S08 Engineering Process

[energy-process.html](energy-process.html) compares five ordered process layouts with native disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-process.ps1

Measured heights: energy-process-heights.json.

## Energy S09 Certifications Standards

[energy-credentials.html](energy-credentials.html) compares five credential layouts with native evidence disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-credentials.ps1

Measured heights: energy-credentials-heights.json.

## Energy S10 Sustainability Impact

[energy-impact.html](energy-impact.html) compares five sustainability layouts with reserved imagery, native evidence disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-impact.ps1

Measured heights: energy-impact-heights.json.

## Energy S11 Capacity Impact Stats

[energy-stats.html](energy-stats.html) compares five metric layouts with native source disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-stats.ps1

Measured heights: energy-stats-heights.json.

## Energy S12 Products Systems

[energy-products.html](energy-products.html) compares five product layouts with reserved images, native details and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-products.ps1

Measured heights: energy-products-heights.json.

## Energy S13 ROI Financing

[energy-financing.html](energy-financing.html) compares five financial-context layouts with native evaluation disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-financing.ps1

Measured heights: energy-financing-heights.json.

## Energy S14 Case Studies

[energy-cases.html](energy-cases.html) compares five case-study layouts with reserved project photography, native context disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-cases.ps1

Measured heights: energy-cases-heights.json.

## Energy S15 Technical Resources

[energy-resources.html](energy-resources.html) compares five resource layouts with reserved covers, native information disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-resources.ps1

Measured heights: energy-resources-heights.json.

## Energy S16 Service Areas

[energy-areas.html](energy-areas.html) compares five service-area layouts with reserved photography, native coverage disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-areas.ps1

Measured heights: energy-areas-heights.json.

## Energy S17 Engineers Team

[energy-team.html](energy-team.html) compares five team layouts with reserved photography, native expertise disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-team.ps1

Measured heights: energy-team-heights.json.

## Energy S18 RFQ Site Assessment

[energy-enquiry.html](energy-enquiry.html) compares five enquiry forms with local summary preparation, native validation and desktop/tablet/mobile previews. No enquiry is transmitted.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-enquiry.ps1

Measured heights: energy-enquiry-heights.json.

## Energy S19 FAQ

[energy-faq.html](energy-faq.html) compares five FAQ layouts with six native disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-faq.ps1

Measured heights: energy-faq-heights.json.

## Energy S20 Contact Final CTA

[energy-contact.html](energy-contact.html) compares five closing contact layouts with links to matching S18 enquiry studies, native guidance and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-contact.ps1

Measured heights: energy-contact-heights.json.

## Energy S21 Subpage Hero

[energy-subpage-hero.html](energy-subpage-hero.html) compares five internal-page heroes with reserved site photographs and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-subpage-hero.ps1

Measured heights: energy-subpage-hero-heights.json.

## Energy S22 Breadcrumb / Context Navigation

[energy-navigation.html](energy-navigation.html) compares five navigation layouts with matching-variant links and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-navigation.ps1

Measured heights: energy-navigation-heights.json.

## Energy S23 Engineering / Energy Solution Detail

[energy-service-detail.html](energy-service-detail.html) compares five service detail layouts with native conditions disclosures, matching enquiry links and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-service-detail.ps1

Measured heights: energy-service-detail-heights.json.

## Energy S24 Project Detail

[energy-project-detail.html](energy-project-detail.html) compares five project narratives with three reserved photographs, native evidence notes and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-project-detail.ps1

Measured heights: energy-project-detail-heights.json.

## Energy S25 Technical Insight / Article Detail

[energy-article-detail.html](energy-article-detail.html) compares five article layouts with attribution, reserved editorial imagery, publication notes and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-article-detail.ps1

Measured heights: energy-article-detail-heights.json.

## Energy S26 Engineer / Expert Profile

[energy-profile-detail.html](energy-profile-detail.html) compares five expert profiles with reserved portraits, complete biographies, team contact links and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-profile-detail.ps1

Measured heights: energy-profile-detail-heights.json.

## Energy S27 Office / Service Location Detail

[energy-location-detail.html](energy-location-detail.html) compares five location layouts with prominent contact fields, arrival information and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-energy-location-detail.ps1

Measured heights: energy-location-detail-heights.json.

Energy S01-S27 authoring is complete: 27 sections and 135 studies, pending Design Lab ingestion.

## Finance S01 Hero

[finance-hero.html](finance-hero.html) compares five modern finance hero layouts with native conversation preparation disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-hero.ps1

Measured heights: finance-hero-heights.json.

## Finance S02 Services Solutions

[finance-services.html](finance-services.html) compares five service category layouts with independent scope disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-services.ps1

Measured heights: finance-services-heights.json.

## Finance S03 Client Segments

[finance-segments.html](finance-segments.html) compares five audience layouts with reserved contextual photographs, eligibility disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-segments.ps1

Measured heights: finance-segments-heights.json.

## Finance S04 Advisors Experts

[finance-advisors.html](finance-advisors.html) compares five adviser team layouts with reserved portraits, native professional background disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-advisors.ps1

Measured heights: finance-advisors-heights.json.

## Finance S05 Regulatory Trust

[finance-trust.html](finance-trust.html) compares five trust layouts with entity, scope and complaints information, native verification disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-trust.ps1

Measured heights: finance-trust-heights.json.

## Finance S06 Engagement Process

[finance-process.html](finance-process.html) compares five four-stage engagement layouts with native preparation disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-process.ps1

Measured heights: finance-process-heights.json.

## Finance S07 Business Stage Solutions

[finance-stages.html](finance-stages.html) compares five business stage layouts with reserved planning photographs, native scope disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-stages.ps1

Measured heights: finance-stages-heights.json.

## Finance S08 Pricing Packages

[finance-pricing.html](finance-pricing.html) compares five package layouts with reserved fees, scope and billing information, native terms disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-pricing.ps1

Measured heights: finance-pricing-heights.json.

## Finance S09 Financial Tools

[finance-tools.html](finance-tools.html) compares five tool discovery layouts with independent purpose and limits disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-tools.ps1

Measured heights: finance-tools-heights.json.

## Finance S10 Client Testimonials

[finance-testimonials.html](finance-testimonials.html) compares five testimonial layouts with reserved client portraits and quotations, native context disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-testimonials.ps1

Measured heights: finance-testimonials-heights.json.

## Finance S11 Case Studies

[finance-cases.html](finance-cases.html) compares five case layouts with reserved context photographs, anonymised engagement narratives, independent disclosures and desktop/tablet/mobile previews.

Regenerate: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-cases.ps1

Measured heights: finance-cases-heights.json.

## Finance S12 Firm Stats

[Compare five firm fact layouts](finance-stats.html): modern layouts for firm history, people and office presence, with reserved values and native definition/source disclosures. Desktop, tablet and phone previews are available.

Regenerate from repository root: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-stats.ps1

Measured heights: finance-stats-heights.json.

## Finance S13 Resources Guides

[Compare five resource layouts](finance-resources.html): featured educational guides with reserved publication details, contextual imagery and native topic outlines. Desktop, tablet and phone previews are available.

Regenerate from repository root: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-resources.ps1

Measured heights: finance-resources-heights.json.

## Finance S14 Compliance Calendar

[Compare five calendar layouts](finance-calendar.html): modern agenda layouts with reserved dates, obligation scopes and official-source notes. A native disclosure holds shared calendar context. Desktop, tablet and phone previews are available.

Regenerate from repository root: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-calendar.ps1

Measured heights: finance-calendar-heights.json.

## Finance S15 Technology Integrations

[Compare five integration layouts](finance-integrations.html): modern layouts for accounting, document exchange and reporting connections, with reserved platform details and a native availability disclosure. Desktop, tablet and phone previews are available.

Regenerate from repository root: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-integrations.ps1

Measured heights: finance-integrations-heights.json.

## Finance S16 Security Privacy

[Compare five privacy layouts](finance-privacy.html): modern information-handling introductions with reserved practice details, contextual imagery and native privacy information disclosures. Desktop, tablet and phone previews are available.

Regenerate from repository root: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-privacy.ps1

Measured heights: finance-privacy-heights.json.

## Finance S17 FAQ

[Compare five FAQ layouts](finance-faq.html): five independently expandable questions about service fit, preparation, fees, existing tools and changing needs. Answers remain reserved for approved information. Desktop, tablet and phone previews are available.

Regenerate from repository root: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-faq.ps1

Measured heights: finance-faq-heights.json.

## Finance S18 Locations Offices

[Compare five office layouts](finance-offices.html): featured office introductions with reserved address, visiting, contact and arrival information alongside office photography slots. Desktop, tablet and phone previews are available.

Regenerate from repository root: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-offices.ps1

Measured heights: finance-offices-heights.json.

## Finance S19 Contact

[Compare five contact layouts](finance-contact.html): email, telephone and meeting introductions with reserved contact details and native preparation disclosures. Desktop, tablet and phone previews are available.

Regenerate from repository root: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-contact.ps1

Measured heights: finance-contact-heights.json.

## Finance S20 Consultation Quote CTA

[Compare five consultation layouts](finance-consultation.html): closing invitations with links to the matching S19 contact studies and native quote-preparation disclosures. Availability and terms remain reserved. Desktop, tablet and phone previews are available.

Regenerate from repository root: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-consultation.ps1

Measured heights: finance-consultation-heights.json.

## Finance S21 Subpage Hero

[Compare five subpage hero layouts](finance-subpage-hero.html): title-first internal service-page introductions, with three contained media layouts and two text-only variants. Page content remains reserved. Desktop, tablet and phone previews are available.

Regenerate from repository root: powershell -NoProfile -ExecutionPolicy Bypass -File review/build-finance-subpage-hero.ps1

Measured heights: finance-subpage-hero-heights.json.
