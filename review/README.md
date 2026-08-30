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

If a browser refuses to load local iframes, serve the workspace over HTTP instead:

    python3 -m http.server 8000

then open `http://localhost:8000/review/index.html`.

## Regenerating

    python3 review/build-index.py

Re-run it after authoring a section. The script scans `sectors/*/S*/raw/*.html`, reads each
study's `<meta>` research fields, and falls back to the section's `BATCH-V1.md` for the
territory where a study predates the `<meta>` convention — which is currently the case for the
`ARC-S02` studies, authored in a separate pass with a different batch format.

The generator has no dependencies beyond the Python standard library.
