# WebAIBuilder Sector Design Authoring Workspace

This standalone local workspace is the authoring source for a planned catalog of sector-specific raw design studies. It is not the main WebAIBuilder production application and it is not the WebAIBuilder Design Lab.

## Scope

- 20 sectors
- 20 section roles per sector
- 5 planned studies per section
- 2,000 planned studies in total
- 0 authored studies at initial setup

The current repository contains structure and documentation only. It contains no HTML studies, application code, production manifests, registry code, runtime adapters, or Design Lab review decisions.

## Workspace Map

- `standards/`: authoring, naming, QA, media, and future handoff standards.
- `planning/`: the master plan and initial progress/status records.
- `sectors/`: sector briefs, sector indexes, section READMEs, and tracked `raw/` study directories.
- `review/`: a generated local contact sheet of the authored studies. Not part of the batch and
  not the Design Lab gallery. Regenerate it with `python3 review/build-index.py` and stage it in
  the same commit whenever studies are added or changed.

Each future completed raw batch is intended to be validated and ingested into Design Lab without a conversion or rewrite step. No ingestion pipeline is implemented here.
