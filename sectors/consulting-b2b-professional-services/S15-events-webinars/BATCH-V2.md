# BATCH V2 — Detailing Pass

## Batch Identity

- Sector: `Consulting & B2B Professional Services` · Prefix: `CONS` · Section: `CONS-S15` — Events & Webinars · Raw Path: `./raw/`
- Register: `../../../standards/08-VISUAL-REFERENCE-STYLE.md`, CONS translation in `../CONSULTING-THEME-CONTRACT.md` → *Detailing Pass*. Supersedes `./BATCH-V1.md` for the design layer; the V1 rules — what makes an hour worth it is who else is in the room, so each event says which kind of room it is; the cap is real and the urgency is not; no countdown, seats-remaining counter, attendee count, register-now, speaker name or headshot; event names, the cap and the share figures as placeholder demo values; the media counts per study (1, 4, 0, 1, 1) — are kept exactly.
- Batch Status: `RE-AUTHORED — V2 DETAILING — PENDING DESIGN LAB INGESTION`

## Studies

| Study ID | Direction | Theme | Register device | Pencil layer | Composition | Media / placeholders | Words |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| `CONS-S15-001` | Universal / Safe | 001 Paper & Indigo | 3 under one wide field | ghost word-numeral *Twelve* behind the head | 21:9 field of the room at the size it is run; four events as a bordered row led by marked kind chips (chair / microphone / stage / closed padlock in `--no`), serif placeholder names, who it is for and the note, the capped session on the band tone; band with V1's no-countdown line | 1 × 21:9 · 5 | 196 |
| `CONS-S15-002` | Premium / Editorial | 002 Sable & Bronze | 8 — staggered gallery | pencil ellipse round *room* | Two columns, the right dropped; each event's own room as a field whose ratio is the room's shape — 3:2 room, square desk, 21:9 hall, 3:4 door — with kind chips and serif names; band | 4 shaped fields · 5 | 221 |
| `CONS-S15-003` | Structured / Visual Modular | 003 Field & Emerald | 3 with the counter | ruled margin behind | Four modules in a bordered row led by the share of the room in the serif at counter scale — placeholder figures, the unflattering ones muted, *Not you* in `--no`; kind chips; band-tone foot cell | none · 7 | 205 |
| `CONS-S15-004` | Conversion-led | 004 White & Signal | 4 with the featured item | underline stroke under *afternoon* | The capped session as a band on the tinted paper with its 3:2 room, kind chip, serif name and the one action TAKE A PLACE; THE OTHER THREE, HONESTLY as a bordered row | 1 × 3:2 · 5 | 175 |
| `CONS-S15-005` | Art-directed / Distinctive | 005 Chalk & Violet | unequal columns narrowing with the audience | bracket grouping the head | Four ruled columns at 2.4 / 1.5 / 1.1 / 0.8 with the type stepping down, the widest carrying the room field; kind chips; foot line. The near-black ground becomes chalk | 1 × 3:2 · 5 | 193 |

## What changed from V1

The four kinds of room are one system across the batch — chair, microphone, stage, closed padlock (the last in `--no`) — as marked chips; the room is a bare field at the ratio of the room; the cap and the names keep their placeholder marking. Cards, badges and the dark 005 ground go. Copy is V1's throughout with one recorded change inside a placeholder name: "The stage-03 session" → "The stage-three session" (no-digit rule).

## Verification

- `cslcheck.ps1 -Sec S15 -Fields 'Broadcast|Closed|A conference talk|A client briefing|The counterfactual hour|countdown'` — ALL CHECKS PASS; parity 30/30; placeholders declared in every study. No `<h1>`; no header/nav/footer; no form; no script; no gradient, shadow, dashed border or radius above 2px; inline SVG only, all `aria-hidden`; no digit outside a placeholder; no seats-remaining, register-now or headshot.
- Rendered and read at 1440. Corrections: `002` field ratios and stagger reduced (height 2030 → 1752); `005` chip width moved to `min()` (checker rule).
