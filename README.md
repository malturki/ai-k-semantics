# AI K Semantics

Public workspace for AI-generated and AI-maintained K Framework semantics for programming languages.

The repository is organized around one principle: every semantics must be traceable to a specification, a reference implementation, and a repeatable test or proof story. K gives us executable definitions, parsers, interpreters, symbolic execution, and proof tooling from one specification; this repo adds project structure, provenance, reference-suite discipline, and review notes around that capability.

## Current Status

This is the initial scaffold. It contains:

- K Framework research notes from the official docs, tutorials, builtins, PL tutorial, and upstream source tree.
- A language workspace template under `languages/_template`.
- An initial Python charter under `languages/python`, targeting Python 3.14.6.
- An initial SQL charter under `languages/sql`, targeting SQL:2023 / ISO/IEC 9075:2023.
- Manifest schemas and a lightweight validator for future language entries.
- Workflow docs for language onboarding and reference-implementation validation.

No production language semantics have been added yet.

## Layout

```text
docs/
  k-framework/       Notes on K concepts, toolchain, codebase, and sources.
  workflows/         How to add and validate a new language semantics.
  adr/               Architecture decisions for this repo.
languages/
  _template/         Copy this structure for each language.
schemas/
  language-manifest.schema.json
skills/
  k-formal-semantics/ Reusable Codex skill for K semantics work.
tools/
  validate_manifests.py
```

## Codex Skill

This repo versions a reusable Codex skill at `skills/k-formal-semantics`. Install or copy it into `${CODEX_HOME:-~/.codex}/skills/k-formal-semantics` to make Codex auto-discover the project methodology for K semantics work.

## Intended Workflow

1. Create `languages/<language>/manifest.json` from the template.
2. Pin source materials: language specs, reference implementation versions, test suites, and known conformance profiles.
3. Build the K syntax and dynamic semantics incrementally.
4. Run concrete tests with `kompile` and `krun`.
5. Run symbolic/proof tests with the Haskell backend and `kprove` where useful.
6. Compare behavior against the reference implementation and record every known gap.

## Validate

```sh
make validate
```

The current validator checks manifest shape and required provenance fields. It does not replace K compilation or reference-suite testing.

## Primary K Sources

- [K homepage](https://kframework.org/)
- [K User Manual](https://kframework.org/docs/user_manual/)
- [K Tutorial](https://kframework.org/k-distribution/k-tutorial/)
- [K Tool Reference](https://kframework.org/docs/ktools/)
- [K Builtins](https://kframework.org/k-distribution/include/kframework/)
- [K PL Tutorial](https://kframework.org/k-distribution/pl-tutorial/)
- [runtimeverification/k](https://github.com/runtimeverification/k)
- [pyk documentation](https://kframework.org/pyk/)

See `docs/k-framework/source-inventory.md` for the captured source snapshot.
