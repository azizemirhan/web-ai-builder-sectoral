# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Automotive` · Prefix: `AUTO` · Section: `AUTO-S22` — Breadcrumb / Context Navigation · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, AUTO translation in `../AUTOMOTIVE-THEME-CONTRACT.md`.
- **This section had no V1 study.** Content and design were authored together; there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

A breadcrumb cannot be written without a hierarchy, and inventing one would invent pages. So the two ancestors are **named after this sector's own sections** — `Dealership` (S01) and `Workshop services` (S04) — and they link to those studies. Only the current page is reserved.

The parent return is the one action: **Back to all workshop services**. The dense variant adds the sibling set — *Parts and accessories · Who does the work · Where we are* — which are likewise real sections.

**005 carries the sector's voice**, because in this pass a navigation surface says what it is not:

> **This trail is where the page sits.** Nothing on it books anything, and nothing on it is answered by a person.

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `AUTO-S22-001` | Universal / Safe | 001 Chalk & Racing Green | C | 1 — the trail and the way back on one strip | the bay lines inside the strip | none · 1 | 34 |
| `AUTO-S22-002` | Premium / Editorial | 002 Paper & Oxide | C | 2 — the trail as an editorial index | the plate edge at the head | none · 1 | 23 |
| `AUTO-S22-003` | Structured / Visual Modular | 003 Steel & Cobalt | C | 3 — the trail in a three-cell plate | bordered plate, 1px lines shared | none · 1 | 43 |
| `AUTO-S22-004` | Conversion-led | 004 Bone & Aubergine | C | 4 — the way back promoted above the trail | the torque mark under *one step* | none · 1 | 26 |
| `AUTO-S22-005` | Art-directed / Distinctive | 005 Night & Signal, inverted | C | 5 — the trail framed, and the limit stated | the ramp frame | none · 1 | 31 |

**All five are shape `C`**, and the contract asks a `C` to record why: *a breadcrumb has no subject to photograph, and a reserved area here would be decoration.* An all-`C` row is normally a flatness signal; here it is what the role is.

The five run **23–43 words**, under the contract's breadcrumb band of 40–90. Like S21, this is the role rather than an omission: a trail is three labels and a return is five words, and the only way to reach forty would be filler or an invented hierarchy. The dense variant, which has a real local set to name, does reach it.

## What was designed

The trail is **tracked uppercase at 0.78rem** with muted slashes, the ancestors underlined on the hairline and the reserved current page in ink — in the accent on 005. `aria-current="page"` is on the current item and the trail is a `<nav aria-label="Breadcrumb">` wrapping an `<ol>`, so the hierarchy is in the markup and not only in the look.

**002 is the one place in the sector where the serif display face is used on a reserved value**: the current page drops out of the tracked line and is set at `clamp(1.6rem, 3.4vw, 2.6rem)` in Georgia, with its leading slash suppressed, so a bracketed placeholder reads as the page you are on.

This is contextual navigation, not the page chrome — no global header, no primary menu, no footer, no search.

## Verification

- `autocheck.ps1 -Sec S22 -AllowNav -Fields 'Dealership|Workshop services|Current page|Back to all workshop services'` — ALL CHECKS PASS; parity 20/20. No `<h1>` (not a hero); the single `nav` landmark is the breadcrumb itself (`-AllowNav`); no header or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, `<img>`, `<table>` or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no alarm red; no manufacturer, model, badge, plate, price or figure; no digit in visible copy; one placeholder per study. All links point at same-variant S01, S04, S09, S10 and S11 studies.
- Rendered and read at 1440.
