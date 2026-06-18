# Python Reference Materials

Retrieved: 2026-06-18.

## Authoritative Reference

Python is not specified by an ISO-style standard. For this project, the authoritative source for the language is the official Python documentation maintained by the Python project.

The current stable documentation on docs.python.org is Python 3.14.6. The documentation page lists Python 3.14 as stable, Python 3.15 as pre-release, and Python 3.16 as in development.

## Primary Sources

- Python 3.14.6 documentation: https://docs.python.org/3/
- Python Language Reference: https://docs.python.org/3/reference/
- Language Reference introduction: https://docs.python.org/3/reference/introduction.html
- Full grammar specification: https://docs.python.org/3/reference/grammar.html
- Python Standard Library: https://docs.python.org/3/library/
- Built-in functions: https://docs.python.org/3/library/functions.html
- Built-in types: https://docs.python.org/3/library/stdtypes.html
- Built-in exceptions: https://docs.python.org/3/library/exceptions.html
- Import system: https://docs.python.org/3/reference/import.html
- PEP index: https://peps.python.org/
- Python version status: https://devguide.python.org/versions/
- Python 3.14.6 release page: https://www.python.org/downloads/release/python-3146/
- CPython repository: https://github.com/python/cpython

## How To Use These Sources

Use the Language Reference as the main semantic source. It covers:

- lexical analysis
- data model
- execution model
- import system
- expressions
- simple statements
- compound statements
- top-level components
- full grammar

Use the Standard Library reference when language semantics depends on built-ins, built-in types, exceptions, importlib, `ast`, `tokenize`, `token`, `keyword`, or other standard modules.

Use accepted and final PEPs for design rationale and feature provenance. PEPs are especially important for newer constructs such as structural pattern matching, exception groups, type parameter lists, deferred annotations, and template string literals. If a PEP and the current docs disagree, prefer the current docs and record the discrepancy.

## Specification Caveat

The Language Reference explicitly says it uses English for most semantics and formal notation mainly for syntax and lexical analysis. It also says CPython implementation notes appear where CPython limitations or behavior are worth mentioning. This is important for K work: the repository should track prose ambiguities and distinguish portable language semantics from CPython-profile behavior.

## Reference Implementation

Use CPython 3.14.6 as the primary reference implementation:

- Release page: https://www.python.org/downloads/release/python-3146/
- Source repository: https://github.com/python/cpython
- Expected tag: `v3.14.6`
- Release date: 2026-06-10

CPython is the original and most-maintained Python implementation. New language features generally appear there first, but CPython internals and implementation notes are not automatically portable language semantics.

## Test Suite

Use the CPython regression suite as the primary reference test suite for the CPython profile:

- Test runner guidance: https://devguide.python.org/testing/run-write-tests/
- Test package documentation: https://docs.python.org/3/library/test.html
- Suite location: `Lib/test` in the CPython source tree.

Every imported CPython test should be classified before use:

- portable language semantics
- CPython implementation detail
- standard library behavior
- platform/environment behavior
- syntax/diagnostic-only behavior
- unsupported or non-goal
