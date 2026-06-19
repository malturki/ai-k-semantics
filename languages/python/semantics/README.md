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
- `pass`
- single-name assignment
- integer literals
- `True`, `False`, and `None`
- simple string literals as K `String` tokens
- name lookup in a single environment
- unary `+`, unary `-`, and integer/bool `+`, `-`, and `*`
- integer/bool `%`, `//`, shifts, bitwise operators, bitwise inversion, and nonnegative exponentiation
- string concatenation with `+`
- truth-value testing for integers, booleans, and `None`
- truth-value testing for strings
- short-circuiting `and` and `or`
- `not`
- binary comparisons for int-like values and equality over integers, booleans, and `None`
- string equality
- conditional expressions
- simple-name `+=`, `-=`, and `*=`
- simple-name `del`
- truthy `assert`
- module-scope `global` declarations as no-ops
- list literals in a trailing-comma value-element subset
- list truthiness, equality, membership, and positive integer indexing
- tuple literals in a trailing-comma value-element subset
- tuple truthiness, equality, membership, and positive integer indexing
- single-argument `lambda` expressions
- single-positional-argument calls to lambda closure values
- an internal `#floorDiv(E1, E2)` parser bridge form emitted by the AST adapter

The coverage ledger in `../notes/full-language-coverage.md` is the source of truth for what remains.

Current parser caveat: the K frontend treats `//` in direct K input files as a comment before it can be parsed as Python floor division. The `floorDivExp` syntax and semantics are present, and `harness/python_to_k_input.py` now translates real Python `//` nodes to the internal `#floorDiv(E1, E2)` form for adapter smoke tests.

Current container caveat: direct concrete list and tuple smoke tests use Python-valid trailing commas, such as `[1, 2,]` and `(1, 2,)`, because the first executable K container grammar avoids an ambiguity caused by un-delimited value-list productions. The AST adapter now accepts ordinary Python list and tuple displays for the supported value-expression subset and emits the trailing-comma internal form. Full displays still need expression-list evaluation, unpacking, mutation, and comprehension semantics.
