# Language Template

Copy this directory to `languages/<language-id>` when starting a new semantics.

Fill in `manifest.json` first. The manifest is the source of truth for:

- supported language version
- upstream specs
- reference implementations
- test suites
- current maturity
- known gaps

## Directories

- `semantics/`: K definitions and build notes.
- `reference/`: source/spec/reference implementation notes.
- `tests/conformance/`: concrete programs and expected behavior manifests.
- `tests/examples/`: small examples useful during development.
- `tests/proofs/`: `kprove` claims and proof helper modules.
- `harness/`: scripts or config for running this language's tests.
- `notes/`: design notes, divergence triage, and open questions.
