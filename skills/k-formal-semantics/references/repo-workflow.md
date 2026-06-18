# Repository Workflow

Use this reference in repositories organized for AI-maintained K semantics, especially `ai-k-semantics`.

## Expected Layout

```text
docs/
  k-framework/
  workflows/
  adr/
languages/
  <language>/
    manifest.json
    semantics/
    reference/
    tests/
      conformance/
      examples/
      proofs/
    harness/
    notes/
schemas/
tools/
```

## Language Manifest

Fill the manifest before implementation grows:

- `id`, `name`, `status`
- K framework versions
- language version and scope
- non-goals
- official specifications
- reference implementations
- test suites
- main K definition/module/syntax module
- backends
- conformance/proof manifests
- known gaps

Status values commonly include:

- `planned`
- `experimental`
- `reference-testing`
- `proof-testing`
- `maintained`

## New Language Procedure

1. Copy the template directory.
2. Fill `manifest.json`.
3. Add source inventory under `reference/`.
4. Add source-map notes under `notes/`.
5. Build the first syntax module and parser tests.
6. Add a minimal configuration and one semantic slice.
7. Add reference and K commands for the slice.
8. Run validation and commit focused changes.

## K Commands To Prefer

For concrete execution:

```sh
kompile semantics/<lang>.k --main-module <LANG> --syntax-module <LANG>-SYNTAX
krun tests/examples/example.<ext>
```

For parsing:

```sh
kast --definition <lang>-kompiled --output kore tests/examples/example.<ext>
kparse tests/examples/example.<ext> | kore-print -
```

For proofs:

```sh
kompile semantics/<lang>.k --backend haskell
kprove tests/proofs/<property>-spec.k
```

Adapt commands to the repo's harness once one exists.

## Artifact Handling

Keep generated artifacts out of git by default:

- `*-kompiled/`
- `.kompile-*/`
- temporary reference-suite downloads
- raw mismatch logs unless deliberately curated

For CI failures, upload artifacts or write a compact triage report.

## Commit Discipline

Prefer commits that separate:

- source/provenance updates
- syntax additions
- semantic rule additions
- test additions
- harness changes
- documentation and triage notes

Never silently update pinned reference versions in a semantics change.
