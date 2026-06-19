# Python Full-Language Coverage Map

This file is the completeness ledger for Python 3.14.6. A construct is not considered complete until it has:

- direct syntax in K or a documented reason for a faithful desugaring
- semantic rules linked to the official docs
- local positive and negative tests
- CPython differential coverage, unless classified as intentionally non-CPython
- known ambiguity/divergence notes where relevant

Status values:

- `not-started`: no K syntax or semantics yet
- `syntax`: syntax exists, semantics incomplete
- `partial`: executable semantics exists for a documented subset
- `profile`: only covered in an implementation/profile module
- `complete`: docs-linked semantics and tests are in place

## Source Chapters

| Source area | Reference | Status | Notes |
| --- | --- | --- | --- |
| Lexical analysis | Language Reference, chapter 2 | partial | Initial kernel uses semicolon-separated simple statements with trailing semicolons and parses integers, simple K strings, `True`, `False`, and `None`; an AST adapter now bridges a small ordinary-Python source subset into that form. Full source encoding, physical/logical lines, indentation, comments, token classes, f/t-string details, bytes, and numeric literal edge cases remain. |
| Data model | Language Reference, chapter 3 | partial | Initial kernel has minimal integers, strings, list/tuple/dict/set values, booleans, and `None`. Full object identity, real bool-as-int subtype behavior, type hierarchy, attributes, descriptors, special methods, GC/lifetime notes, coroutines, and async generators remain. |
| Execution model | Language Reference, chapter 4 | partial | Initial kernel has a single environment. Full code blocks, frames, binding, scopes, exceptions, annotation scopes, and runtime components remain. |
| Import system | Language Reference, chapter 5 | not-started | Needs controlled module table and host profile. |
| Expressions | Language Reference, chapter 6 | partial | Initial kernel covers integer/string/list/tuple/dict/set/bool/None atoms, names, parentheses, expression-backed list/tuple/dict/set displays through the adapter, unary `+`/`-`/`~`, arithmetic and bitwise integer operators, string concatenation/equality/order, string/list/tuple sequence repetition with integer-like counts, string/list/tuple nonzero-step slicing, string substring membership and indexing, list/tuple same-type concatenation, list/tuple/dict/set equality, list/tuple lexicographic ordering, set-to-set ordering comparisons, list/tuple membership/indexing, dict key membership/lookup, set membership, range equality/membership/indexing/nonzero-step slicing, singleton identity comparisons, chained comparisons over supported operators, truthiness for simple values, short-circuit `and`/`or`, `not`, conditional expressions, simple-name assignment expressions, positional-argument lambdas/calls including suffix defaults, and a binary comparison subset. All other expression constructs remain. |
| Simple statements | Language Reference, chapter 7 | partial | Initial kernel covers expression statements, `pass`, truthy `assert`, module-scope `global`, simple assignment, flat and starred sequence unpacking assignment over current list/tuple RHS values, simple-name `+=`/`-=`/`*=`, and simple-name `del`. Remaining statements are not started. |
| Compound statements | Language Reference, chapter 8 | partial | Adapter-backed `if`, `while`, string/list/tuple/dict/range `for`, flat unpacking `for` targets, and positional-parameter `def` subsets exist, including `break`, `continue`, `return` propagation, and loop `else` for the current while/for subsets. General iteration, `try`, `with`, `match`, full functions, classes, coroutines, type parameter lists, annotations remain. |
| Top-level components | Language Reference, chapter 9 | syntax | Initial kernel parses a small file-input subset. Interactive/eval modes remain. |
| Full grammar | Language Reference, chapter 10 | syntax | A first construct-preserving CPython-AST adapter exists for the current executable subset, including ordinary `//`, list displays, and tuple displays. The full grammar must still be mirrored construct-by-construct or covered by documented parser front ends that preserve construct identity. |
| Built-ins and core library | Standard Library reference | partial | Internal `range`, `len`, `bool`, `all`, `any`, int-like `sum`, nonempty int-like one-argument `min`/`max`, `int`, `abs`, `divmod`, and two-argument `pow` subsets exist, plus no-argument `list()`, `tuple()`, `dict()`, and `set()` constructors and ordered-iterable `list(x)`/`tuple(x)` for current concrete values; no full builtins namespace or general object protocol yet. |

## Construct Families

| Family | Status | Required next evidence |
| --- | --- | --- |
| Source encodings and tokenizer behavior | not-started | CPython tokenizer cases and docs-linked K lexer/token model. |
| Indentation and block structure | not-started | Parser tests for `INDENT`/`DEDENT`, mixed tabs/spaces diagnostics, blank/comment-only lines. |
| Names, keywords, soft keywords | partial | Initial `Id` handling only; needs Python identifier Unicode rules and keyword/soft-keyword separation. |
| Literals | partial | Int, simple string, bool, and None smoke coverage; bytes, floats, imaginary numbers, full Python string prefixes/escapes, f-strings, t-strings remain. |
| Object model | partial | Minimal value model with singleton identity only; needs heap objects, general identity, type hierarchy, attributes, descriptors. |
| Numeric operations | partial | Int/bool unary `+`/`-`/`~`, `+`, `-`, `*`, `%`, `//`, shifts, bitwise operators, nonnegative `**`, adapter-backed `int()`/`int(x)`, `abs(x)`, `divmod(x, y)`, two-argument `pow(x, y)`, concrete-iterable `sum(x)`/`sum(x, start)`, and one-argument `min(x)`/`max(x)` for current int-like values with nonnegative exponents for `pow`; adapter smoke now exercises real Python `//` spelling. Python numeric tower, true division, negative exponent float behavior, string/base int conversion, full coercions, non-int sum starts/items, key/default/multi-argument min/max, and error behavior remain. |
| Truth-value testing | partial | Simple int/string/list/tuple/dict/set/range/bool/None truthiness, adapter-backed `bool()`/`bool(x)`, concrete-iterable `all(x)`/`any(x)` for those values, and short-circuit `and`/`or`; needs `__bool__`, `__len__`, `__iter__`, full containers, lazy iterator side effects, and user-defined objects. |
| Name binding and scope | partial | Single environment only, including simple-name assignment expressions in that current environment; needs module/function/class scopes, globals, nonlocals, comprehensions, annotation scopes. |
| Assignment | partial | Single-name assignment, adapter-backed simple-name assignment expressions, adapter-backed multi-target simple-name assignment, flat sequence unpacking assignment to simple names, starred sequence unpacking assignment to simple names over current list/tuple RHS values, and simple-name augmented assignment for current integer-like operators; needs nested unpacking, general iterable unpacking, attributes, subscriptions, annotations, `/=`, `@=`, unpacking diagnostics, and full target evaluation order. |
| Calls and functions | partial | Positional-argument lambda values and function definitions, positional lambda/function defaults evaluated at lambda/function definition time, simple returns, recursive calls, zero/multi-positional calls, and keyword-only calls without positional arguments; needs mixed positional/keyword calls, `**kwargs`, varargs, keyword-only and positional-only parameters, closures/cells, decorators, annotations, methods, argument-binding diagnostics, and real frames. |
| Containers and comprehensions | partial | Minimal string/list/tuple/dict/set value displays, adapter-backed expression evaluation for list/tuple/dict/set displays, no-argument `list()`, `tuple()`, `dict()`, and `set()` constructors, `list(x)`/`tuple(x)` over current ordered string/list/tuple/dict/range values, duplicate dictionary key replacement in the supported key-equality subset, duplicate set element normalization through the adapter, string/list/tuple repetition with integer-like counts, string/list/tuple nonzero-step slicing, string substring membership, string iteration, lexicographic ordering, and positive/negative indexing, list/tuple same-type concatenation, list/tuple/dict/set equality, list/tuple lexicographic ordering, set-to-set ordering comparisons, membership, truthiness, positive/negative indexing, dict key membership, dict key lookup, dict key iteration, and adapter-backed `range(stop)`/`range(start, stop)`/`range(start, stop, step)` values for `for` loops, equality, integer-like membership, positive/negative indexing, nonzero-step slicing, and `len`; direct K smoke uses trailing-comma input while adapter smoke accepts ordinary Python displays for the supported subset. Needs broader constructor arguments/iterable conversion, set-to-list/tuple conversion order profile, unpacking, mutation, zero-step slice diagnostics, slice objects, non-integer repetition diagnostics, repeated-list mutable-element aliasing behavior, cross-type concatenation diagnostics, out-of-range IndexError behavior, dictionary views/iterator mutation behavior, dictionary unpacking, full range object behavior, iterators, and comprehensions. |
| Attribute access and descriptors | not-started | Needs `object.__getattribute__`, descriptors, method binding, special method lookup. |
| Classes and metaclasses | not-started | Needs class body execution, namespace, MRO, descriptors, metaclass protocol. |
| Exceptions | not-started | Needs exception objects, raise/propagation, chaining, groups, handlers, finally. |
| Control flow | partial | Adapter-backed `if`, `while`, string/list/tuple/dict/range `for`, flat unpacking `for` targets, loop `else`, `break`, `continue`, and function `return` subsets are covered, along with `pass`, truthy `assert`, and expression-level conditionals; needs general iteration, nested/starred loop targets, `yield`, context managers. |
| Import system | not-started | Needs module cache, find/load protocol, packages, relative imports, `__main__`. |
| Pattern matching | not-started | Needs PEP 634/635/636 plus current docs mapping. |
| Coroutines and async | not-started | Needs awaitables, async functions/generators, async with/for. |
| Annotations and type syntax | not-started | Needs deferred annotations, type parameters, `type` statement, annotation scopes. |
| Standard library interactions | partial | Internal `range(stop)`/`range(start, stop)`/`range(start, stop, step)` loop, equality, integer-like membership, indexing, nonzero-step slicing, truthiness, and length support exist; `len`, `bool`, concrete-iterable `all`/`any`, int-like `sum`, nonempty int-like one-argument `min`/`max`, int-like `int`, `abs`, `divmod`, and two-argument `pow` work for current concrete values, with `pow` limited to nonnegative exponents; no-argument `list()`, `tuple()`, `dict()`, and `set()` constructors build current empty concrete values, and `list(x)`/`tuple(x)` convert current ordered concrete string/list/tuple/dict/range values. Needs staged builtins/core library coverage, broader constructor arguments/iterable conversion, set-to-list/tuple conversion order profile, string/base int conversion, full range object behavior, zero-step diagnostics, general `__bool__`/`__len__`/`__iter__`/`__next__`/`__int__`/`__abs__`/`__divmod__`/`__pow__`, non-int sum starts/items, key/default/multi-argument min/max, and host profile boundaries. |
| CPython profile | not-started | Needs implementation notes, diagnostics, limits, and `Lib/test` classification. |

## Completeness Rule

Do not mark a construct complete merely because CPython accepts a test. Completion requires matching the official docs, a K rule story, and an explicit decision about CPython-specific behavior.
