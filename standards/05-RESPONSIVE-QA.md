# Responsive QA

Apply this checklist to every raw study before handoff:

- Content remains usable at narrow, medium, and wide viewport widths.
- No required content or controls are clipped, overlapped, or unreachable.
- Reading and focus order remain coherent across layout changes.
- Media slots preserve their documented behavior without forcing overflow.
- Touch targets remain practical on small screens.
- Text resizing does not cause loss of content or functionality.
- Any intentional breakpoint-specific behavior is documented in the batch file.

## Responsive Behavior Is Part of the Archetype

A study is not a desktop composition that is later squeezed. The narrow-width composition is part
of what makes the study a distinct structural territory, and it is authored deliberately.

A distinctive design must have an intentional transformation, not a fallback. Where a device is
wide-width only — a spine, a rail, a horizontal sequence, a keyed diagram — the study must say
what replaces it, and the replacement must carry the same information.

## Failure Patterns to Avoid

- Fixed collapsed slivers: elements given a small fixed width at every breakpoint, which render as
  blank columns when their media slots are empty.
- Desktop overlaps preserved on mobile.
- Side rails that stay in place until they are too narrow to read.
- Decorative elements consuming mobile width that content needs.
- Horizontal structures with no narrow-width strategy at all.
- Visual emptiness caused by a media slot collapsing incorrectly rather than reflowing.

A composition that only reads once real media is present has not passed this checklist: reserved
media areas are normally empty, and the study must be legible in that state at every width.
