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
- adapter-backed `float()` and `float(x)` for the current int-like/float subset
- adapter-backed `abs(x)` for the current int-like/float subset
- adapter-backed `divmod(x, y)` for the current int-like subset
- adapter-backed `pow(x, y)` for the current int-like subset, with negative exponents requiring a nonzero base and producing floats
- adapter-backed `pow(x, y, mod)` for current int-like values with nonnegative exponents and nonzero modulus
- adapter-backed true division `/` for the current int-like subset, producing float values
- `True`, `False`, `None`, adapter-backed ellipsis `...` as the `Ellipsis` singleton, and adapter-backed `__debug__` as `True` in the current non-optimized profile
- simple string literals as K `String` tokens
- name lookup in a single environment
- unary `+`, unary `-`, and integer/bool `+`, `-`, and `*`
- integer/bool `%`, `//`, `/`, shifts, bitwise operators, bitwise inversion, and exponentiation
- float and mixed int/bool/float `+`, `-`, `*`, `/`, `//`, `%`, `**`, `divmod`, `pow`, ordering comparisons, and `abs`
- string concatenation with `+`, repetition with integer/bool `*`, nonzero-step slicing, substring membership, lexicographic ordering, and positive/negative integer indexing
- truth-value testing for integers, floats, booleans, `None`, and `Ellipsis`
- truth-value testing for strings
- adapter-backed `bool()` and `bool(x)` for the current truth-value subset
- adapter-backed `all(x)` and `any(x)` for current concrete string/container/range values
- adapter-backed `sum(x)` and `sum(x, start)` for current concrete int-like container/range values
- adapter-backed one-argument `min(x)` and `max(x)` for current nonempty concrete int-like container/range values, plus multi-argument `min(a, b, ...)` and `max(a, b, ...)` for current int-like values
- short-circuiting `and` and `or`
- `not`
- binary comparisons for int-like values and equality over integers, booleans, `None`, and `Ellipsis`
- string equality
- singleton identity comparisons with `is` and `is not` for `None`, `True`, `False`, and `Ellipsis`
- adapter-backed chained comparisons over the currently supported comparison operators, with short-circuiting
- conditional expressions
- adapter-backed assignment expressions `NAME := expr` for simple-name targets in the current environment
- simple-name `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`, `<<=`, `>>=`, `&=`, `^=`, and `|=`
- multi-target simple-name assignment through the AST adapter
- simple-name `del` and adapter-backed multi-target `del` for simple names
- truthy `assert`, including adapter-backed optional assertion messages that are not evaluated on success
- module-scope single-name and multi-name `global` declarations as no-ops
- list literals in a trailing-comma value-element subset
- adapter-backed list displays with supported expression elements, starred unpacking over current ordered concrete iterables, one-generator list comprehensions over current concrete iterables with simple-name targets and zero or more filter clauses, two-generator list comprehensions over current concrete iterables with simple-name targets and zero or more filter clauses on each generator, and three-generator list comprehensions over current concrete iterables with simple-name targets and zero or more filter clauses on each generator
- list truthiness, equality, lexicographic ordering, same-type concatenation, repetition with integer/bool `*`, nonzero-step slicing, membership, and positive/negative integer indexing
- tuple literals in a trailing-comma value-element subset
- adapter-backed tuple displays with supported expression elements and starred unpacking over current ordered concrete iterables
- tuple truthiness, equality, lexicographic ordering, same-type concatenation, repetition with integer/bool `*`, nonzero-step slicing, membership, and positive/negative integer indexing
- dictionary literals in a trailing-comma key/value subset
- adapter-backed dictionary displays with supported key/value expressions, including duplicate key replacement in the supported key-equality subset
- adapter-backed one-generator dictionary comprehensions over current concrete iterables with simple-name targets and zero or more filter clauses, two-generator dictionary comprehensions over current concrete iterables with simple-name targets and zero or more filter clauses on each generator, and three-generator dictionary comprehensions over current concrete iterables with simple-name targets and zero or more filter clauses on each generator, with duplicate key replacement in the supported key-equality subset
- dictionary truthiness, equality, key membership, key subscription lookup, and key iteration in `for` loops
- nonempty set literals in a trailing-comma value subset
- adapter-backed set displays with supported expression elements and starred unpacking over current ordered concrete iterables, including duplicate element normalization, plus empty `set()`
- adapter-backed one-generator set comprehensions over current concrete iterables with simple-name targets and zero or more filter clauses, two-generator set comprehensions over current concrete iterables with simple-name targets and zero or more filter clauses on each generator, plus three-generator set comprehensions over current concrete iterables with simple-name targets and zero or more filter clauses on each generator, with duplicate element normalization
- set truthiness, equality, set-to-set ordering comparisons, membership, and length
- adapter-backed no-argument `list()`, `tuple()`, `dict()`, and `set()` constructors as explicit internal constructor expressions
- adapter-backed `list(x)` and `tuple(x)` for current ordered concrete string/list/tuple/dict/range values, with dictionaries yielding keys
- adapter-backed `dict(x)` for current concrete dictionaries and current concrete list/tuple iterables of length-two list/tuple pairs, plus `dict(key=value)`, `dict(**d)`, and `dict(x, key=value, **d)` over current simple keyword arguments and current concrete-dict keyword unpacking
- adapter-backed `set(x)` for current concrete string/list/tuple/dict/set/range values, with dictionaries yielding keys and duplicate elements normalized
- single-argument `lambda` expressions
- single-positional-argument calls to lambda closure values
- adapter-backed zero- and multi-positional-argument calls, keyword-only calls, mixed positional/keyword calls, starred positional call arguments over current ordered concrete iterables, functions, and lambdas
- adapter-backed keyword argument unpacking over current concrete dictionary values with string keys
- adapter-backed positional lambda default values, evaluated when the lambda expression is evaluated
- adapter-backed positional function default values, evaluated at function definition time
- adapter-backed function and lambda varargs parameters, including suffix defaults for fixed parameters, collecting extra positional arguments into a tuple
- adapter-backed function and lambda `**kwargs` parameters in the no-default/no-varargs/no-keyword-only subset, collecting extra keyword arguments into a dictionary keyed by strings
- adapter-backed function and lambda positional-only parameters in the no-default/no-varargs/no-keyword-only/no-kwargs subset
- adapter-backed function and lambda keyword-only parameters in the no-positional subset, including sparse defaults
- adapter-backed function and lambda mixed positional-plus-keyword-only parameters including sparse keyword-only defaults
- an internal `#floorDiv(E1, E2)` parser bridge form emitted by the AST adapter
- adapter-backed `if` statements with optional `else`
- adapter-backed `while` loops with `break`, `continue`, and loop `else`
- adapter-backed `for` loops over the current string/list/tuple/dict value subset, including `break`, `continue`, and `return` propagation
- adapter-backed flat and starred sequence unpacking targets in `for` loops
- adapter-backed `while`/`for` loop `else` clauses for the current loop subsets
- adapter-backed `range(stop)`, `range(start, stop)`, and `range(start, stop, step)` values in `for` loops
- adapter-backed range truthiness, equality, integer-like membership, indexing, nonzero-step slicing, length, and `start`/`stop`/`step` attributes
- adapter-backed `len(...)` for strings, lists, tuples, dictionaries, sets, and current range values
- adapter-backed single-parameter `def` functions, `return` with and without an expression, fallthrough to `None`, and recursive calls in the single-environment subset

The coverage ledger in `../notes/full-language-coverage.md` is the source of truth for what remains.

Current parser caveat: the K frontend treats `//` in direct K input files as a comment before it can be parsed as Python floor division. The `floorDivExp` syntax and semantics are present, and `harness/python_to_k_input.py` now translates real Python `//` nodes to the internal `#floorDiv(E1, E2)` form for adapter smoke tests.

Current container caveat: direct concrete list, tuple, dict, and set smoke tests use Python-valid trailing commas, such as `[1, 2,]`, `(1, 2,)`, `{"x": 1,}`, and `{1, 2,}`, because the first executable K container grammar avoids ambiguities caused by un-delimited element productions. The AST adapter now accepts ordinary Python list, tuple, dict, set displays, starred list/tuple/set display unpacking over current ordered concrete string/list/tuple/dict/range values, one-generator list comprehensions over current concrete iterables with a simple-name target and zero or more filter clauses, two-generator list comprehensions over current concrete iterables with simple-name targets and zero or more filter clauses on each generator, three-generator list comprehensions over current concrete iterables with simple-name targets and zero or more filter clauses on each generator, one-generator dict comprehensions over current concrete iterables with a simple-name target and zero or more filter clauses, two-generator dict comprehensions over current concrete iterables with simple-name targets and zero or more filter clauses on each generator, three-generator dict comprehensions over current concrete iterables with simple-name targets and zero or more filter clauses on each generator, one-generator set comprehensions over current concrete iterables with a simple-name target and zero or more filter clauses, two-generator set comprehensions over current concrete iterables with simple-name targets and zero or more filter clauses on each generator, three-generator set comprehensions over current concrete iterables with simple-name targets and zero or more filter clauses on each generator, dictionary display unpacking over current concrete dict values, no-argument `list()`, `tuple()`, `dict()`, and `set()` constructors, `list(x)`/`tuple(x)` over current ordered concrete string/list/tuple/dict/range values, `dict(x)` over current concrete dict values and current concrete list/tuple pair iterables, `dict(key=value)`, `dict(**d)`, and `dict(x, key=value, **d)` over current simple keyword arguments and current concrete-dict keyword unpacking, and `set(x)` over current concrete string/list/tuple/dict/set/range values for the supported expression subset and emits explicit internal forms. Full displays still need mutation, more-than-three/async list comprehensions, more-than-three/async dict comprehensions, more-than-three/async set comprehensions, generator comprehensions, nonempty set unpacking/order profiles, set-to-list/tuple conversion order profile, zero-step slice diagnostics, non-integer repetition diagnostics, mutable-element aliasing behavior for repeated lists, cross-type ordering/concatenation diagnostics, hashability/error behavior, and complete error behavior.

Current compound-statement caveat: the K parser does not yet accept Python indentation syntax directly. The AST adapter emits internal `#if`, `#while`, `#whileElse`, `#for`, `#forElse`, unpacking-`for`, and `#def` statements with explicit blocks for the supported subset. `for` iteration is defined only for current concrete string/list/tuple/dict/range values, with dictionaries iterating over keys. General iterator protocol, `try`, `with`, `match`, full function definitions, class definitions, and async compound statements remain unsupported.

Current range caveat: adapter-backed `range` support is an internal `rangeVal` subset used by `for` loops, `len`, equality, truthiness, integer-like containment, indexing, nonzero-step slicing, and `start`/`stop`/`step` attribute access, including positive and negative integer steps. Zero-step `ValueError`, non-integer containment fallback, out-of-range `IndexError`, broader range object behavior, and the general iterator protocol remain unsupported.

Current builtin caveat: `len` is defined only for the current concrete string/container/range values, `bool` is defined only through the current truth-value subset, `all` and `any` are defined only for current concrete string/container/range values after the argument value is materialized, `sum` is defined only for current concrete int-like container/range values with optional int-like `start`, one-argument `min` and `max` are defined only for current nonempty concrete int-like container/range values, multi-argument `min` and `max` are defined only for current int-like argument values, `int` is defined only for no argument and current int-like values, `float` is defined only for no argument and current int-like/float values, `abs` is defined over current int-like and float values, `divmod` is defined over current int-like/float values, two-argument `pow` is defined over current int-like values and the finite positive-base real float subset, and three-argument modular `pow` is defined only for current int-like values with nonnegative exponents and nonzero modulus, with negative two-argument integer `pow` exponents requiring a nonzero base, `__debug__` is defined as `True` for the current non-optimized profile, and the current container type constructors cover no-argument `list()`, `tuple()`, `dict()`, and `set()`, one-argument `list(x)`/`tuple(x)` over current ordered concrete iterables, `dict(x)` over current dict values and list/tuple pair iterables, `dict(key=value)`/`dict(**d)`/`dict(x, key=value, **d)` over current simple keyword arguments and current concrete-dict keyword unpacking, and one-argument `set(x)` over current concrete iterables. General builtins namespace lookup, optimization profile behavior for `-O`, broader constructor arguments, mapping protocol, dictionary-constructor duplicate-keyword diagnostics, set iteration order profiles, string/base numeric conversion, full float string/object coercion and error behavior, negative-base complex power results, zero-base negative-exponent diagnostics, modular inverse for negative-exponent `pow`, lazy iterator side effects, non-int sum starts/items, empty/default/key `min`/`max`, `__bool__`/`__len__`/`__iter__`/`__next__`/`__int__`/`__float__`/`__abs__`/`__divmod__`/`__pow__` dispatch, overflow/error behavior, and user-defined objects remain unsupported.

Current assignment-expression caveat: adapter-backed `NAME := expr` evaluates `expr`, binds the resulting value to `NAME` in the current single environment, and yields that value. Full named-expression support still needs concrete parser integration, grammar-position restrictions and diagnostics, comprehension scope behavior, and interaction with real module/function/class scopes.

Current unpacking caveat: flat and starred assignment targets are adapter-backed for simple names and current concrete list/tuple RHS values, and flat/starred `for` targets are adapter-backed over current concrete list/tuple item values. A starred target receives a list of remaining values, possibly empty, and prefix/star/suffix name binding follows left-to-right target order. General iterable unpacking, nested targets, unpacking diagnostics, and attribute/subscript targets remain unsupported.

Current function caveat: adapter-backed `#def`, `#defArgs`, `#defDefaults`, `#defVarArgs`, `#defVarArgsDefaults`, `#defKwArgs`, `#defPosOnly`, `#defKwOnly`, `#defKwDefaults`, `#defPosKwOnly`, `#defPosKwDefaults`, `#lambdaArgs`, `#lambdaDefaults`, `#lambdaVarArgs`, `#lambdaVarArgsDefaults`, `#lambdaKwArgs`, `#lambdaPosOnly`, `#lambdaKwOnly`, `#lambdaKwDefaults`, `#lambdaPosKwOnly`, and `#lambdaPosKwDefaults` cover zero or more positional parameters, optional suffix defaults evaluated at function/lambda definition time, varargs parameters including suffix defaults and keyword binding for fixed parameters, `**kwargs` parameters without defaults, varargs, or keyword-only parameters, positional-only parameters without defaults, varargs, keyword-only parameters, or kwargs, keyword-only parameters without positional parameters including sparse defaults, mixed positional-plus-keyword-only parameters including sparse keyword-only defaults, keyword-only calls without positional arguments, mixed positional/keyword calls, starred positional call unpacking over current ordered concrete string/list/tuple/dict/range values, keyword argument unpacking over current concrete dictionary values with string keys, bare and value-return statements, no decorators, no annotations, no positional-only defaults or combinations, and an environment-restore model. Full Python function objects need real frames, cells/closures, globals/nonlocals, descriptors, methods, and argument binding diagnostics.

Current augmented-assignment caveat: matrix-multiplication `@=` remains unsupported because there is no matrix protocol, and augmented assignment is otherwise limited to simple-name targets in the current value/operator subsets rather than full in-place/special-method dispatch.

Current identity caveat: `is` and `is not` are defined only for the language singletons `None`, `True`, `False`, and `Ellipsis` compared with singleton or non-singleton values. The adapter maps the ordinary Python `...` atom to the internal `Ellipsis` singleton; the assignable builtins name `Ellipsis` is not modeled because the current subset has no builtins namespace. General object identity requires a heap/object model and remains unsupported.
