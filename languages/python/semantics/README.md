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
- adapter-backed flat sequence unpacking assignment to simple names
- adapter-backed starred sequence unpacking assignment to simple names over current list/tuple RHS values
- integer literals
- adapter-backed `int()` and `int(x)` for the current int-like subset
- adapter-backed `abs(x)` for the current int-like subset
- adapter-backed `divmod(x, y)` for the current int-like subset
- adapter-backed two-argument `pow(x, y)` for the current nonnegative-exponent int-like subset
- `True`, `False`, and `None`
- simple string literals as K `String` tokens
- name lookup in a single environment
- unary `+`, unary `-`, and integer/bool `+`, `-`, and `*`
- integer/bool `%`, `//`, shifts, bitwise operators, bitwise inversion, and nonnegative exponentiation
- string concatenation with `+`, repetition with integer/bool `*`, nonzero-step slicing, substring membership, lexicographic ordering, and positive/negative integer indexing
- truth-value testing for integers, booleans, and `None`
- truth-value testing for strings
- adapter-backed `bool()` and `bool(x)` for the current truth-value subset
- adapter-backed `all(x)` and `any(x)` for current concrete string/container/range values
- adapter-backed `sum(x)` and `sum(x, start)` for current concrete int-like container/range values
- adapter-backed one-argument `min(x)` and `max(x)` for current nonempty concrete int-like container/range values
- short-circuiting `and` and `or`
- `not`
- binary comparisons for int-like values and equality over integers, booleans, and `None`
- string equality
- singleton identity comparisons with `is` and `is not` for `None`, `True`, and `False`
- adapter-backed chained comparisons over the currently supported comparison operators, with short-circuiting
- conditional expressions
- adapter-backed assignment expressions `NAME := expr` for simple-name targets in the current environment
- simple-name `+=`, `-=`, `*=`, `%=`, `**=`, `//=`, `<<=`, `>>=`, `&=`, `^=`, and `|=`
- multi-target simple-name assignment through the AST adapter
- simple-name `del`
- truthy `assert`
- module-scope `global` declarations as no-ops
- list literals in a trailing-comma value-element subset
- adapter-backed list displays with supported expression elements
- list truthiness, equality, lexicographic ordering, same-type concatenation, repetition with integer/bool `*`, nonzero-step slicing, membership, and positive/negative integer indexing
- tuple literals in a trailing-comma value-element subset
- adapter-backed tuple displays with supported expression elements
- tuple truthiness, equality, lexicographic ordering, same-type concatenation, repetition with integer/bool `*`, nonzero-step slicing, membership, and positive/negative integer indexing
- dictionary literals in a trailing-comma key/value subset
- adapter-backed dictionary displays with supported key/value expressions, including duplicate key replacement in the supported key-equality subset
- dictionary truthiness, equality, key membership, key subscription lookup, and key iteration in `for` loops
- nonempty set literals in a trailing-comma value subset
- adapter-backed set displays with supported expression elements, including duplicate element normalization, plus empty `set()`
- set truthiness, equality, set-to-set ordering comparisons, membership, and length
- adapter-backed no-argument `list()`, `tuple()`, `dict()`, and `set()` constructors as explicit internal constructor expressions
- adapter-backed `list(x)` and `tuple(x)` for current ordered concrete string/list/tuple/dict/range values, with dictionaries yielding keys
- single-argument `lambda` expressions
- single-positional-argument calls to lambda closure values
- adapter-backed zero- and multi-positional-argument calls, keyword-only calls, mixed positional/keyword calls, functions, and lambdas
- adapter-backed positional lambda default values, evaluated when the lambda expression is evaluated
- adapter-backed positional function default values, evaluated at function definition time
- an internal `#floorDiv(E1, E2)` parser bridge form emitted by the AST adapter
- adapter-backed `if` statements with optional `else`
- adapter-backed `while` loops with `break`, `continue`, and loop `else`
- adapter-backed `for` loops over the current string/list/tuple/dict value subset, including `break`, `continue`, and `return` propagation
- adapter-backed flat sequence unpacking targets in `for` loops
- adapter-backed `while`/`for` loop `else` clauses for the current loop subsets
- adapter-backed `range(stop)`, `range(start, stop)`, and `range(start, stop, step)` values in `for` loops
- adapter-backed range truthiness, equality, integer-like membership, indexing, nonzero-step slicing, and length
- adapter-backed `len(...)` for strings, lists, tuples, dictionaries, sets, and current range values
- adapter-backed single-parameter `def` functions, `return`, fallthrough to `None`, and recursive calls in the single-environment subset

The coverage ledger in `../notes/full-language-coverage.md` is the source of truth for what remains.

Current parser caveat: the K frontend treats `//` in direct K input files as a comment before it can be parsed as Python floor division. The `floorDivExp` syntax and semantics are present, and `harness/python_to_k_input.py` now translates real Python `//` nodes to the internal `#floorDiv(E1, E2)` form for adapter smoke tests.

Current container caveat: direct concrete list, tuple, dict, and set smoke tests use Python-valid trailing commas, such as `[1, 2,]`, `(1, 2,)`, `{"x": 1,}`, and `{1, 2,}`, because the first executable K container grammar avoids ambiguities caused by un-delimited element productions. The AST adapter now accepts ordinary Python list, tuple, dict, set displays, no-argument `list()`, `tuple()`, `dict()`, and `set()` constructors, and `list(x)`/`tuple(x)` over current ordered concrete string/list/tuple/dict/range values for the supported expression subset and emits explicit internal forms. Full displays still need unpacking, mutation, comprehensions, dictionary unpacking, set-to-list/tuple conversion order, zero-step slice diagnostics, non-integer repetition diagnostics, mutable-element aliasing behavior for repeated lists, cross-type ordering/concatenation diagnostics, hashability/error behavior, and complete error behavior.

Current compound-statement caveat: the K parser does not yet accept Python indentation syntax directly. The AST adapter emits internal `#if`, `#while`, `#whileElse`, `#for`, `#forElse`, and `#def` statements with explicit blocks for the supported subset. `for` iteration is defined only for current concrete string/list/tuple/dict/range values, with dictionaries iterating over keys. General iterator protocol, `try`, `with`, `match`, full function definitions, class definitions, and async compound statements remain unsupported.

Current range caveat: adapter-backed `range` support is an internal `rangeVal` subset used by `for` loops, `len`, equality, truthiness, integer-like containment, indexing, and nonzero-step slicing, including positive and negative integer steps. Zero-step `ValueError`, range object attributes, non-integer containment fallback, out-of-range `IndexError`, and the general iterator protocol remain unsupported.

Current builtin caveat: `len` is defined only for the current concrete string/container/range values, `bool` is defined only through the current truth-value subset, `all` and `any` are defined only for current concrete string/container/range values after the argument value is materialized, `sum` is defined only for current concrete int-like container/range values with optional int-like `start`, one-argument `min` and `max` are defined only for current nonempty concrete int-like container/range values, `int` is defined only for no argument and current int-like values, `abs`, `divmod`, and two-argument `pow` are defined only for current int-like values, with `pow` limited to nonnegative exponents, and the current container type constructors cover only no-argument `list()`, `tuple()`, `dict()`, and `set()`. General builtins namespace lookup, constructor arguments, string/base numeric conversion, three-argument modular `pow`, lazy iterator side effects, non-int sum starts/items, empty/default/key/multi-argument `min`/`max`, `__bool__`/`__len__`/`__iter__`/`__next__`/`__int__`/`__abs__`/`__divmod__`/`__pow__` dispatch, overflow/error behavior, and user-defined objects remain unsupported.

Current assignment-expression caveat: adapter-backed `NAME := expr` evaluates `expr`, binds the resulting value to `NAME` in the current single environment, and yields that value. Full named-expression support still needs concrete parser integration, grammar-position restrictions and diagnostics, comprehension scope behavior, and interaction with real module/function/class scopes.

Current unpacking-assignment caveat: flat and starred assignment targets are adapter-backed for simple names and current concrete list/tuple RHS values. A starred target receives a list of remaining values, possibly empty, and prefix/star/suffix name binding follows left-to-right target order. General iterable unpacking, nested targets, starred targets in `for`, unpacking diagnostics, and attribute/subscript targets remain unsupported.

Current function caveat: adapter-backed `#def`, `#defArgs`, and `#defDefaults` cover zero or more positional parameters, optional suffix defaults evaluated at function definition time, keyword-only calls without positional arguments, mixed positional/keyword calls without starred argument unpacking or `**kwargs`, no decorators, no annotations, no positional-only or keyword-only parameters, no varargs/kwargs, and an environment-restore model. Full Python function objects need real frames, cells/closures, globals/nonlocals, descriptors, methods, and argument binding diagnostics.

Current augmented-assignment caveat: true-division `/=` and matrix-multiplication `@=` remain unsupported because the current value model has no float/numeric tower or matrix protocol.

Current identity caveat: `is` and `is not` are defined only for the language singletons `None`, `True`, and `False` compared with singleton or non-singleton values. General object identity requires a heap/object model and remains unsupported.
