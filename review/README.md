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
