# Python

Planned K semantics for Python, targeting Python 3.14.6.

The main reference is the official Python documentation, especially the Python Language Reference for syntax and core semantics. CPython 3.14.6 is the primary reference implementation for differential testing and ambiguity triage.

## Current Charter

- Primary specification: Python 3.14.6 Language Reference.
- Runtime/builtins reference: Python 3.14.6 Standard Library reference.
- Feature provenance: accepted/final Python Enhancement Proposals, with current docs preferred when text differs.
- Reference implementation: CPython 3.14.6.
- Reference test suite: CPython regression suite under `Lib/test`.

## Working Rule

Model portable Python semantics from the official docs first. CPython quirks belong in a named CPython profile unless the docs make them part of the portable language behavior.
