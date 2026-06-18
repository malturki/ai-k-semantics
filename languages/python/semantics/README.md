# Python Semantics

K definitions live here.

Current entry points:

```sh
kompile python.k --main-module PYTHON --syntax-module PYTHON-SYNTAX
krun ../tests/examples/simple.py
```

The base modules should model portable Python semantics from the official docs. CPython-specific behavior belongs in a profile module.

## Current Slice

`python.k` is an executable seed, not a full semantics. It currently covers:

- semicolon-separated simple statements with a trailing semicolon
- expression statements
- single-name assignment
- integer literals
- name lookup in a single environment
- integer `+`, `-`, and `*`

The coverage ledger in `../notes/full-language-coverage.md` is the source of truth for what remains.
