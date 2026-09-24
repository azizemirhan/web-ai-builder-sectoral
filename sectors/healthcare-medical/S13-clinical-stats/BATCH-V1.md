# BATCH V1

## Batch Identity

- Sector: `Healthcare & Medical Clinics`
- Prefix: `HC`
- Section ID: `HC-S13`
- Section Name: `Clinical Stats`
- Raw Path: `./raw/`
- Batch Status: `AUTHORED — PENDING DESIGN LAB INGESTION`

## Planned Studies

| Study ID | Direction | Theme | Shape | Composition | Areas | Words |
| --- | --- | --- | :---: | --- | ---: | ---: |
| `HC-S13-001` | Universal / Safe | 001 Linen & Sage | B | Five counted things as cards — **the value as a word, large**, the thing counted, why it matters; **a wide frame of the corridor with the room doors** beside the not-counted line | 1 | 154 |
| `HC-S13-002` | Premium / Editorial | 002 Porcelain & Plum | B | **A tall frame of the appointment book open on the desk**, the five counts as a ruled serif column with the word in plum | 1 | 159 |
| `HC-S13-003` | Structured / Visual Modular | 003 Sky & Slate | B | Head beside **the team at the morning handover**; **a ledger of five rows with a third field — *where you check it*** | 1 | 215 |
| `HC-S13-004` | Conversion-led | 004 Sand & Terracotta | B | **A terracotta panel carrying the one number that decides a booking — the usual wait — as a word, with the action**, over a frame of the desk with the diary; the other four as a ruled list | 1 | 169 |
| `HC-S13-005` | Art-directed / Distinctive | 005 Night & Mint | **C** | Dark ground; **the five values as words at billboard size in mint**, stacked as ruled lines | 0 | 145 |

Row `B B B B C`. Page three, after `C C C` across `S10`–`S12`, returns to a frame. Page five,
after `C C B`, takes its `C`. No page has two consecutive `A`.

## The Governing Idea

> **Numbers about the building and the diary, not about you.**

The sector's stats section is four big figures — patients seen, years, a satisfaction percentage,
a success rate — that describe other people and prove nothing about the visitor's visit. In this
sector an outcome statistic is prohibited and the contract composes a stats role *without
figures*. What may be counted in public is what the clinic owns and the visitor can check, as
**demo values spelled as words**:

| Value | Counted | Why it matters |
| --- | --- | --- |
| *Six* | consulting rooms | a first appointment does not wait for a room |
| *Eleven* | people on the team | you are told which one you will see |
| *A week* | usual wait for a first appointment | told to you when you book, not promised |
| *Half an hour* | usual length of a first visit | long enough to be examined and to ask |
| *A few days* | usual wait for results | you are told which day to expect them |

**Not counted in public:** outcomes, satisfaction scores, how many people we have seen — none of
them tells you anything about your visit. `003` adds *where you check it* to every row; `004`
gives the wait, the one number that decides a booking, the panel and the action.

## Placeholder Data

All five values in every study are demo values marked `data-placeholder="true"`, spelled as
words, and there is **no digit anywhere in the batch**. Clear before real use.

## Density

Standard band throughout except `003`, declared structured for its third field. 145–169
elsewhere; the role is short once outcome text is removed and nothing was padded.

## Media

Four reserved areas, each the thing being counted: the corridor with the room doors (`001`); the
appointment book — where three of the five numbers live (`002`); the team at the morning
handover, by role (`003`); the desk with the diary open (`004`). `005` is type: a word at
billboard size cannot pretend to be a percentage.

## Verification Record

- Word bands: **154 / 159 / 215 / 169 / 145** (standard except `003` structured).
- Content parity: **15 shared fields across five studies, 75/75 slots present.**
- Reserved areas: **1 / 1 / 1 / 1 / 0.** Demo values: 5 per study, all words.
- Claims scan clean; no digit, outcome, success, satisfaction or patient-count figure; no
  clinician name, price, telephone or hour.
- Dependencies none; tag balance, namespace, frame, reduced-motion, `<h2>` labelling, no
  solid-border-plus-max-width, relative hrefs only: all pass.
- Rendered and read at 1440 and 390; no layout corrections required.
- Cross-browser and screen-reader tests not run. Design Lab ingestion not performed.
