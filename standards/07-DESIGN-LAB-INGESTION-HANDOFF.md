# Design Lab Ingestion Handoff

This document records the intended future handoff only. The pipeline is not implemented in this workspace.

    completed section batch
    ↓
    validate IDs
    ↓
    validate raw format
    ↓
    validate dependencies
    ↓
    copy/import immutable studies
    ↓
    Design Lab registration
    ↓
    gallery
    ↓
    capture
    ↓
    QA
    ↓
    human review

## Authoring Workspace Responsibility

- Complete the section batch.
- Preserve stable study IDs.
- Satisfy the standalone raw format and dependency policy.
- Complete batch metadata and pre-handoff QA records.

## Design Lab Responsibility

- Import immutable study inputs.
- Register studies and make them available to the gallery and capture flow.
- Run Design Lab QA and human review.
- Keep review decisions, normalization, selection, and promotion work outside this workspace.

The required operation is **validate → ingest**, not **convert → rewrite → ingest**.
