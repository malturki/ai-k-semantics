# Python Test Suite Status

Current status: local smoke tests pass; a CPython 3.14.6 reference interpreter has been built locally; the full CPython suite has not been run against the K semantics.

2026-07-02 adapter-index note: reconciled the adapter smoke manifest with 24 already-running CPython/K-green adapter files covering f-strings, string conversion builtins, `chr`, matrix-multiply TypeErrors, non-int `sum`, extended `min`/`max`, class-pattern keyword attributes, dict duplicate keyword diagnostics, and false assertions. Added shell-runner entries for the CPython/K-green bytes decode, maketrans/translate, and bytes `%` formatting cases that were already present in the manifest. Four manifest-only decode error-handler cases still hit the current `NotImplementedError` UTF-8 invalid-sequence path and remain semantic targets: `adapter-bytes-decode-error-handlers`, `adapter-bytearray-decode-error-handlers`, `adapter-bytes-decode-backslashreplace`, and `adapter-bytearray-decode-backslashreplace`.

## What Runs Now

`languages/python/harness/run-smoke.sh` compiles the current K seed and runs:

- `tests/examples/smoke-arithmetic.py`
- `tests/examples/smoke-assignment.py`

These validate the current executable slice only: integer arithmetic, semicolon-separated simple statements with trailing semicolons, single-name assignment, name lookup, and result recording.

## Full CPython Suite Preconditions

The full CPython suite requires:

- a CPython 3.14.6 executable
- a CPython source checkout at tag `v3.14.6`
- classification of `Lib/test` cases into language semantics, CPython implementation detail, standard-library behavior, platform/environment behavior, syntax/diagnostic-only behavior, unsupported behavior, and non-goals
- adapters that run each selected test or extracted test program through both CPython and the K semantics
- normalization rules for stdout, stderr, tracebacks, paths, hash seeds, resource-dependent behavior, and diagnostics

## Local Reference Interpreter

The official `Python-3.14.6.tar.xz` archive was downloaded and verified with SHA-256:

```text
143b1dddefaec3bd2e21e3b839b34a2b7fb9842272883c576420d605e9f30c63
```

It was built under `.external/Python-3.14.6`. The build-tree interpreter reports `Python 3.14.6` and successfully runs the initial reference smoke command:

```sh
./python -m test --single-process --timeout 120 test_grammar
```

Result: success, 1 test file, 75 tests.

The local build is not a fully provisioned CPython regression-test environment. Optional modules missing from the build include `_ssl`, `_hashlib`, `_sqlite3`, `_bz2`, `_lzma`, `_zstd`, `_curses`, `_tkinter`, `_uuid`, `_dbm`, `_gdbm`, and `readline`. Tests depending on these modules must be classified as environment-dependent until a fully provisioned CPython build exists.

## Current Blocker

K differential execution requires classified test adapters. The CPython suite is therefore only a reference-suite availability check until adapters exist for selected test families.

## Correctness Policy

Do not claim full Python correctness until the coverage map marks each relevant construct complete and a classified CPython suite run has no unexplained divergences.
