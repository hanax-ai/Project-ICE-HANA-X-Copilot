# ADR-012: Use Docling for governed document normalization

**Status:** Proposed
**Date:** 2026-07-16
**Owner:** HANA-X AI Architecture
**Derived from:** ICE-SRC-008 and ICE-ARCH-001

## Context

Uploaded SAP and business documents include complex layouts and tables that must be normalized locally while preserving structure and provenance.

## Decision

Use Docling as the baseline document conversion component for supported files. Preserve originals, normalize to structured Markdown/JSON, capture provenance, and quality-check tables and extracted fields before indexing.

## Consequences

- The ingestion pipeline uses a common normalized representation.
- Successful parsing does not imply semantic accuracy.
- Original binaries remain immutable evidence.

## Validation and follow-up

- Create document/table extraction evaluation sets.
- Define malware scanning, size limits, supported formats, and failure handling.

## References

- `05_Architecture/02_Component_Architecture/ICE-ARCH-001_HANA-X-Copilot-Solution-Architecture/References/ICE-ARCH-001_References.md`
