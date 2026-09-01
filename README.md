# WebAIBuilder Sector Design Authoring Workspace

This standalone local workspace is the authoring source for a planned catalog of sector-specific raw design studies. It is not the main WebAIBuilder production application and it is not the WebAIBuilder Design Lab.

## Scope

- 20 sectors
- 27 section roles per sector
- 5 planned studies per section
- 2,700 planned studies in total

The catalog is in two parts:

| Range | Model | Sections | Planned studies |
| --- | --- | ---: | ---: |
| S01–S20 | Sector Core — the sector's own page and section roles | 20 per sector | 2,000 |
| S21–S27 | Universal Extended Site Architecture — detail-page and page-context roles shared by every sector | 7 per sector | 700 |
| **Total** |  | **27 per sector** | **2,700** |

The original core catalog was 2,000 studies across S01–S20. S21–S27 extend it; they do not
replace it. S28 and above are reserved for provisional sector-native extensions; they are not
scaffolded and are outside the planned catalog count.

The repository contains structure, documentation, and authored raw studies only. It contains no application code, production manifests, registry code, runtime adapters, or Design Lab review decisions.

## Workspace Map

- `standards/`: authoring, naming, QA, media, and future handoff standards.
- `planning/`: the master plan and initial progress/status records.
- `sectors/`: sector briefs, sector indexes, section READMEs, and tracked `raw/` study directories.
- `review/`: a generated local contact sheet of the authored studies. Not part of the batch and
  not the Design Lab gallery. Regenerate it with `python3 review/build-index.py` and stage it in
  the same commit whenever studies are added or changed.

Each future completed raw batch is intended to be validated and ingested into Design Lab without a conversion or rewrite step. No ingestion pipeline is implemented here.
