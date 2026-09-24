# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Beauty, Wellness & Spa` · Prefix: `WELL` · Section: `WELL-S26` — Person / Profile Detail · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, WELL translation in `../WELLNESS-DESIGN-DIRECTION.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the rule — role leads, identity reserved — the name in the portrait's own `<figcaption>` so no reflow can separate them, and the outright omission of credentials, years, counts, handles, testimonials and ratings are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Composition | Portrait | Words |
| --- | --- | --- | --- | --- | --- | ---: |
| `WELL-S26-001` | Universal / Safe | 001 Linen & Olive | 10 — portrait with offset tab, beside ruled rows | Sticky identity figure (4:5 portrait, tinted tab, reserved name, role, categories) beside HOW THEY WORK and WHAT THEY WILL SAY NO TO as ruled rows; asking for them on the foot rule | paired | 240 |
| `WELL-S26-002` | Premium / Editorial | 002 Bone & Clay | 9 — chapter pacing, no picture | 62ch column: reserved name at display scale, an accent lead, three chapters with eyebrows and serif titles, a ruled ledger, why there is no photograph | none | 311 |
| `WELL-S26-003` | Dense / Information-heavy | 003 Mist & Moss | ruled identity line + cells + ruled row | Small 1:1 portrait with tab and reserved name on a ruled line; three record cells sharing hairlines; WHAT THIS PAGE DOES NOT LIST as a ruled three-column row with reasons | paired | 289 |
| `WELL-S26-004` | Conversion-led | 004 Sand & Ochre | 10 — portrait with tab beside one action | Identity figure beside a ruled column: "Ask for them by name" in serif, one bordered action, three ruled rows, the steer-away | paired | 169 |
| `WELL-S26-005` | Sector-native / Distinctive | 005 Ivory & Plum | 9 — chapter pacing at appointment scale | Small identity in the head; five chapters (First / Then / Last) on hairlines beside a sticky column of two ruled notes | paired | 309 |

## What changed from V1

Record panels, the omissions panel and card framing are gone. Every portrait uses the register's offset-tab device — a bare 4:5 or 1:1 field with a tinted tab set behind it — and stays inside a `<figure>` with the reserved name in its `<figcaption>`. `002` is paced as chapters so the no-photograph variant has structure without a picture.

## Verification

- `wellcheck.ps1` — ALL CHECKS PASS; parity on "by name" and "Facials" 10/10. Four portraits, four paired with their name area inside one `<figure>`; no credential, year, count, rating, handle or email in visible copy; no digit beyond indices and the 4:5 label.
- Rendered and read at 1440. No correction needed.
