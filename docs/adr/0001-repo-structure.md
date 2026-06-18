# ADR 0001: Repository Structure

Status: accepted

Date: 2026-06-18

## Context

This repo will contain AI-generated and AI-maintained K semantics for multiple programming languages. Each language will have different upstream specifications, reference implementations, test suites, and semantic maturity.

## Decision

Use a language-centered layout under `languages/<language-id>` with shared workflow docs, schemas, and tools at the repository root.

Each language gets:

- `manifest.json` for provenance and status
- `semantics/` for K definitions
- `reference/` for source and reference implementation notes
- `tests/` for conformance examples, proofs, and future harness data
- `harness/` for language-specific runners or manifests
- `notes/` for design decisions, gaps, and triage

## Consequences

This keeps unrelated languages isolated while allowing common validation and CI to operate over manifests. The cost is some boilerplate per language, but the explicit provenance is essential for correctness.
