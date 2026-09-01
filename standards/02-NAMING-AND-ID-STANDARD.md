# Naming and ID Standard

## Stable Study ID

Every planned or authored study uses:

    <SECTOR-PREFIX>-S<SECTION-NUMBER>-<VARIANT>

Example:

    HC-S01-001

- HC is the stable sector prefix.
- S01 is the stable section role number.
- 001 is the variant number.

Default variants are 001 through 005. Section numbers are zero-padded and contiguous from S01
through S27 in every sector.

## Section Number Ranges

| Range | Model | Numbering |
| --- | --- | --- |
| S01–S20 | Sector Core | Section roles specific to the sector |
| S21–S27 | Universal Extended Site Architecture | The same seven roles, at the same numbers, in every sector |
| S28+ | Reserved / provisional | Sector-native extensions beyond the shared model. Outside the planned catalog count; used only where a sector documents a genuinely additional role. |

Section numbers above S20 are explicitly supported and follow the same rules as S01–S20: two
digits, zero-padded, contiguous, and stable. A section number is never reused or renumbered once
allocated.

For S21–S27 the number and the universal role are canonical across the catalog, so `S24` means
the same structural role in every sector. The sector-facing section name may adapt to the
sector's own terminology — `LAW-S24` is a representative matter and `ARC-S24` is a project —
without changing the number, the role, or the ID.

Filenames must not be the only source of semantic meaning. IDs remain stable if section display names evolve. Prefixes are unique across the sector catalog.
