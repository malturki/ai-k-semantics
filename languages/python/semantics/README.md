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
- list literals in a trailing-comma value-element subset
- list truthiness, equality, membership, and positive integer indexing
- tuple literals in a trailing-comma value-element subset
- tuple truthiness, equality, membership, and positive integer indexing
- single-argument `lambda` expressions
- single-positional-argument calls to lambda closure values

The coverage ledger in `../notes/full-language-coverage.md` is the source of truth for what remains.

Current parser caveat: the K frontend treats `//` in source files as a comment before it can be parsed as Python floor division. The `floorDivExp` syntax and semantics are present, but concrete Python-source testing for `//` needs the parser/adaptor tranche.

Current container caveat: concrete list and tuple smoke tests use Python-valid trailing commas, such as `[1, 2,]` and `(1, 2,)`, because the first executable K container grammar avoids an ambiguity caused by un-delimited value-list productions. Full displays need the parser/adaptor tranche and expression-list evaluation.
