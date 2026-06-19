# Python Harness

The harness will eventually run:

- K parser and execution tests.
- Standard conformance tests with docs/PEP provenance.
- Differential tests against CPython 3.14.6.
- Selected CPython `Lib/test` cases after classification.

Every differential run must record the CPython executable, version, platform, environment variables, hash seed, command-line flags, stdin/stdout/stderr normalization, and expected exception/diagnostic handling.

## Current Commands

```sh
languages/python/harness/run-smoke.sh
```

Compiles `semantics/python.k` and runs the local smoke cases.

```sh
PYTHON_REF=/path/to/python3.14 languages/python/harness/run-adapter-smoke.sh
```

Compiles `semantics/python.k`, checks each adapter smoke program with CPython,
translates it through `python_to_k_input.py`, and runs the adapted K input. This
is the first construct-preserving bridge from ordinary Python source to the
current semicolon-terminated K subset.

```sh
PYTHON_REF=/path/to/python3.14 CPYTHON_SOURCE=/path/to/cpython languages/python/harness/run-cpython-suite.sh
```

Checks the CPython reference suite entry point against a small classified smoke subset. By default it runs:

```sh
python -m test --single-process --timeout 120 test_grammar
```

Set `CPYTHON_TEST_ARGS` to select another classified subset or to intentionally launch the full suite. K differential adapters still need to be built per classified test family.
