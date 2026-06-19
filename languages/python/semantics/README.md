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
- dictionary literals in a trailing-comma key/value subset
- dictionary truthiness, key membership, and key subscription lookup
- nonempty set literals in a trailing-comma value subset
- set truthiness and membership
- single-argument `lambda` expressions
- single-positional-argument calls to lambda closure values
- an internal `#floorDiv(E1, E2)` parser bridge form emitted by the AST adapter
- adapter-backed `if` statements with optional `else`
- adapter-backed `while` loops with `break` and `continue`, without loop `else`
- adapter-backed `for` loops over the current list/tuple value subset, including `break`, `continue`, and `return` propagation
- adapter-backed single-parameter `def` functions, `return`, fallthrough to `None`, and recursive calls in the single-environment subset

The coverage ledger in `../notes/full-language-coverage.md` is the source of truth for what remains.

Current parser caveat: the K frontend treats `//` in direct K input files as a comment before it can be parsed as Python floor division. The `floorDivExp` syntax and semantics are present, and `harness/python_to_k_input.py` now translates real Python `//` nodes to the internal `#floorDiv(E1, E2)` form for adapter smoke tests.

Current container caveat: direct concrete list, tuple, dict, and set smoke tests use Python-valid trailing commas, such as `[1, 2,]`, `(1, 2,)`, `{"x": 1,}`, and `{1, 2,}`, because the first executable K container grammar avoids ambiguities caused by un-delimited element productions. The AST adapter now accepts ordinary Python list, tuple, dict, and nonempty set displays for the supported value-expression subset and emits the trailing-comma internal form. Full displays still need expression-list evaluation, unpacking, mutation, and comprehension semantics.

Current compound-statement caveat: the K parser does not yet accept Python indentation syntax directly. The AST adapter emits internal `#if`, `#while`, `#for`, and `#def` statements with explicit blocks for the supported subset. Loop `else`, general iterator protocol, `try`, `with`, `match`, full function definitions, class definitions, and async compound statements remain unsupported.

Current function caveat: adapter-backed `#def` uses one positional parameter, no decorators, no defaults, no annotations, no keyword arguments, and an environment-restore model. Full Python function objects need real frames, cells/closures, default evaluation, globals/nonlocals, descriptors, methods, and argument binding diagnostics.
