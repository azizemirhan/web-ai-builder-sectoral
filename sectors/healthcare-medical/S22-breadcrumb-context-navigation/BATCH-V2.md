# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Healthcare & Medical Clinics` · Prefix: `HC` · Section: `HC-S22` — Breadcrumb / Context Navigation · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, HC translation in `../HEALTHCARE-THEME-CONTRACT.md` → *Detailing Pass*.
- **This section had no V1 study.** Authored directly in the V2 register; this record carries both the authoring and the design decisions and there is no `BATCH-V1.md`.
- Batch Status: `AUTHORED IN THE V2 DETAILING PASS — PENDING DESIGN LAB INGESTION`

## The content decision

A breadcrumb cannot be written without a hierarchy, and inventing one would invent pages. So the two ancestors are **named after this sector's own sections** — `Clinic` (S01) and `Medical services` (S02) — and they link to those studies. Only the current page is reserved: `[Current page]`, bracketed and marked `data-placeholder="true"`, because the component sits on any subpage.

The parent return is the one action: **Back to all medical services**. The dense variant adds the sibling set — *Doctors and specialists · Conditions treated · Locations and departments* — which are likewise real sections, not invented pages.

The variant that carries the sector's own voice is **005**: a breadcrumb is a navigation surface, and in this sector a navigation surface says what it is not. *This trail is where the page sits. It is not the way to an emergency, and nothing above it is answered by a person.*

## Studies

| Study ID | Direction | Theme | Shape | Register device | Structure layer | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `HC-S22-001` | Universal / Safe | 001 Linen & Sage | C | 1 — the trail and the way back on one strip | column rules inside the strip | none · 1 | 34 |
| `HC-S22-002` | Premium / Editorial | 002 Porcelain & Plum | C | 2 — the trail read as an editorial index | open bracket at the head | none · 1 | 23 |
| `HC-S22-003` | Dense / Information-heavy | 003 Sky & Slate | C | 3 — the trail in a three-cell plate with the local set | bordered plate, 1px lines shared | none · 1 | 46 |
| `HC-S22-004` | Conversion-led | 004 Sand & Terracotta | C | 4 — the way back promoted above the trail | measure rule under *one step* | none · 1 | 26 |
| `HC-S22-005` | Sector-native / Distinctive | 005 Night & Mint, inverted | C | 5 — the trail framed, and the limit stated | corner frame along the head | none · 1 | 38 |

**All five are shape C**, and the contract asks a `C` to record why it carries none: *a breadcrumb has no subject to photograph, and a reserved area here would be decoration.* An all-`C` row is normally a flatness signal; here it is what the role is.

The five run **23–46 words**, under the contract's breadcrumb band of 40–90. Like S21, this is the role rather than an omission: a trail is three labels, a return is five words, and the only legitimate way to reach forty would be filler or an invented hierarchy. The dense variant, which has a real local set to name, does reach the band.

## What was designed

The trail is **tracked uppercase at 0.78rem** with muted slashes as `li + li::before`, the ancestors underlined on the hairline and the reserved current page in ink — in the accent on 005, which is the one variant that colours it. `aria-current="page"` is on the current item and the trail is a `<nav aria-label="Breadcrumb">` wrapping an `<ol>`, so the hierarchy is in the markup and not only in the look.

Each variant restates the trail rather than restyling it: 001 lays it on a strip between two hairlines with the column rules standing inside the strip; 002 breaks it, putting the ancestors on one tracked line and the reserved page beneath at display size with its leading slash suppressed; 003 puts it in the band-tone cell of a three-cell plate whose 1px lines are shared; 004 demotes it to the quiet right-hand column and promotes the return to the bordered action under its measure rule; 005 sets it on a band-tone ribbon inside the corner frame.

**This is contextual navigation, not the page chrome** — no global header, no primary menu, no footer, no search. Nothing here opens, expands or submits. No SVG, no icon, no badge, no chevron glyph beyond the shared arrow on the return and the link mark.

## Verification

- `hccheck.ps1 -Sec S22 -AllowNav -Fields 'Clinic|Medical services|Current page|Back to all medical services'` — ALL CHECKS PASS; parity 20/20. No `<h1>` (not a hero); the single `nav` landmark is the breadcrumb itself (`-AllowNav`); no header or footer; **no `<svg>`, `<script>`, `<form>`, `<iframe>`, image or remote reference**; no gradient, shadow, dashed border, pill or background-image; radius ceiling 6px; no cyan, aqua or alarm red; no digit in visible copy; one placeholder per study, declared in the `placeholder-data` meta. All links point at same-variant S01, S02, S03, S04, S14 and S18 studies and resolve on disk.
- Rendered and read at 1440. Corrections: the 001 column rules were overrunning the strip and were closed to it; the 002 leading slash was inheriting the display size and was suppressed, since the current page is on its own line; the 003 sibling rows were doubling their padding against the shared tap target and were set to none.
