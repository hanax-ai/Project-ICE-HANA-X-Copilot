# ADR-013: Use Crawl4AI for governed web acquisition

**Status:** Proposed
**Date:** 2026-07-16
**Owner:** HANA-X AI Architecture
**Derived from:** ICE-SRC-008 and ICE-ARCH-001

## Context

Some workflows require external web content that must be acquired and normalized for analysis or governed retention.

## Decision

Use Crawl4AI behind a controlled acquisition service with domain policy, SSRF and private-address blocking, secret isolation, provenance, licensing/robots review, page hashes, retention, refresh, and user approval before permanent ingestion.

## Consequences

- Web content can enter the same normalized ingestion pipeline.
- The crawler must not be described or configured as a bot-detection bypass.
- External content is untrusted and cannot override system policy.

## Validation and follow-up

- Implement network and URL security controls.
- Define retention, freshness, rights, and citation rules.

## References

- `05_Architecture/02_Component_Architecture/ICE-ARCH-001_HANA-X-Copilot-Solution-Architecture/References/ICE-ARCH-001_References.md`
