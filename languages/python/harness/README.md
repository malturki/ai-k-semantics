# Python Harness

The harness will eventually run:

- K parser and execution tests.
- Standard conformance tests with docs/PEP provenance.
- Differential tests against CPython 3.14.6.
- Selected CPython `Lib/test` cases after classification.

Every differential run must record the CPython executable, version, platform, environment variables, hash seed, command-line flags, stdin/stdout/stderr normalization, and expected exception/diagnostic handling.
