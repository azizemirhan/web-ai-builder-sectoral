# Project Context

WebAIBuilder has two existing repository contexts:

1. **Repo 1 — Main WebAIBuilder production application:** the production application and its runtime code.
2. **Repo 2 — WebAIBuilder Design Lab:** the environment for ingestion, capture, QA, human review, normalization, survivor selection, and promotion preparation.

This folder is the **Sector Design Authoring Workspace**. It is not a third production repository. It is a standalone local authoring workspace whose completed raw studies will eventually be ingested into Design Lab through a separate process.

The intended boundary is:

    Sector Authoring Workspace
    ↓
    completed raw batch
    ↓
    Design Lab ingestion
    ↓
    automated capture / QA
    ↓
    human review
    ↓
    normalization
    ↓
    survivor selection
    ↓
    promotion pipeline
    ↓
    main WebAIBuilder production repository

This workspace must not contain production React components, production manifests or registries, Composer or PageDocument code, runtime adapters, main application code, or Design Lab review decisions.
