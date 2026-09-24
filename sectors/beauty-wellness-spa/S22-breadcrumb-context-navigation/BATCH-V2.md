# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Beauty, Wellness & Spa` · Prefix: `WELL` · Section: `WELL-S22` — Breadcrumb / Context Navigation · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, WELL translation in `../WELLNESS-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the navigation rules are kept exactly — a named `<nav>` landmark, an ordered list, real links for every level but the current, `aria-current="page"` on the current, separators hidden from assistive technology, no truncation — and each study still carries a different content responsibility.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Composition | Height at 1440 |
| --- | --- | --- | --- | --- | ---: |
| `WELL-S22-001` | Universal / Safe | 001 Linen & Olive | tracked label line on a hairline | Four levels in tracked uppercase, accent slashes, current in ink | 114 |
| `WELL-S22-002` | Premium / Editorial | 002 Bone & Clay | stepped column against a left rule | The trail as a serif staircase, the article-title level a reserved area; a ruled note beside | 301 |
| `WELL-S22-003` | Dense / Information-heavy | 003 Mist & Moss | label line + cells sharing hairlines | The trail, then the sibling categories as four cells with accent indices, current marked | 202 |
| `WELL-S22-004` | Conversion-led | 004 Sand & Ochre | bordered action on a ruled line | "← All facials" as a bordered action beside the trail, the observation right-aligned | 158 |
| `WELL-S22-005` | Sector-native / Distinctive | 005 Ivory & Plum | one serif sentence between rules | The trail as a sentence in serif, levels underlined, current in accent italic, connectives hidden | 165 |

## What changed from V1

The sage band, the chevron chain and the visually hidden `h1` are gone: a breadcrumb names the nav landmark with `aria-label` and leaves the page's `h1` to the hero. Separators are the register's thin accent slash; the sibling set is a hairlined cell row; the promoted return is the register's bordered rectangle. Word counts sit below the hero band by nature of the role.

## Verification

- `wellcheck.ps1 -AllowNav` (the only section where `<nav>` is required) — ALL CHECKS PASS. Twelve `aria-current="page"` markers across the five files (one per landmark); no `<header>`, `<footer>`, search field or menu; no digit in visible copy beyond the sibling indices.
- Rendered and read at 1440. No correction needed.
