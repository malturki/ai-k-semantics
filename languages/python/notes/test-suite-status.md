# Python Test Suite Status

Current status: local smoke tests pass; the full CPython suite has not been run against the K semantics.

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

## Current Blocker

This local environment has K installed, but no `python3.14` executable. The suite harness therefore exits with a clear setup error until `PYTHON_REF` points to a CPython 3.14.6 executable and `CPYTHON_SOURCE` points to a matching source checkout.

## Correctness Policy

Do not claim full Python correctness until the coverage map marks each relevant construct complete and a classified CPython suite run has no unexplained divergences.
