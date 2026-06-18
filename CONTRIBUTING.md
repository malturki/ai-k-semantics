# Contributing

This repository is meant to grow language-by-language. Keep each contribution scoped to one language, one shared tool, or one workflow document unless there is a strong reason to cross boundaries.

For a new language:

1. Copy `languages/_template` to `languages/<language-id>`.
2. Fill in `manifest.json` before writing much K code.
3. Record the exact upstream spec, reference implementation, and test-suite versions.
4. Keep generated artifacts out of git unless a workflow document explicitly says otherwise.
5. Add known divergences as notes instead of burying them in tests.

Every behavior claim should be backed by one of:

- An official specification citation.
- A reference implementation result.
- A reference test-suite case.
- A deliberate local design note marked as non-standard.
