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
| Data model | Language Reference, chapter 3 | partial | Initial kernel has minimal integers, strings, list/tuple values, booleans, and `None`. Full object identity, real bool-as-int subtype behavior, type hierarchy, attributes, descriptors, special methods, GC/lifetime notes, coroutines, and async generators remain. |
| Execution model | Language Reference, chapter 4 | partial | Initial kernel has a single environment. Full code blocks, frames, binding, scopes, exceptions, annotation scopes, and runtime components remain. |
| Import system | Language Reference, chapter 5 | not-started | Needs controlled module table and host profile. |
| Expressions | Language Reference, chapter 6 | partial | Initial kernel covers integer/string/list/tuple/bool/None atoms, names, parentheses, unary `+`/`-`/`~`, arithmetic and bitwise integer operators, string concatenation/equality, list/tuple equality/membership/indexing, truthiness for simple values, short-circuit `and`/`or`, `not`, conditional expressions, single-argument lambdas/calls, and a binary comparison subset. All other expression constructs remain. |
| Simple statements | Language Reference, chapter 7 | partial | Initial kernel covers expression statements, `pass`, truthy `assert`, module-scope `global`, simple assignment, simple-name `+=`/`-=`/`*=`, and simple-name `del`. Remaining statements are not started. |
| Compound statements | Language Reference, chapter 8 | partial | Adapter-backed `if`, `while`, and single-parameter `def` subsets exist, including `break`, `continue`, and `return` propagation. `for`, loop `else`, `try`, `with`, `match`, full functions, classes, coroutines, type parameter lists, annotations remain. |
| Top-level components | Language Reference, chapter 9 | syntax | Initial kernel parses a small file-input subset. Interactive/eval modes remain. |
| Full grammar | Language Reference, chapter 10 | syntax | A first construct-preserving CPython-AST adapter exists for the current executable subset, including ordinary `//`, list displays, and tuple displays. The full grammar must still be mirrored construct-by-construct or covered by documented parser front ends that preserve construct identity. |
| Built-ins and core library | Standard Library reference | not-started | Initial kernel only has internal integers; no real Python builtins yet. |

## Construct Families

| Family | Status | Required next evidence |
| --- | --- | --- |
| Source encodings and tokenizer behavior | not-started | CPython tokenizer cases and docs-linked K lexer/token model. |
| Indentation and block structure | not-started | Parser tests for `INDENT`/`DEDENT`, mixed tabs/spaces diagnostics, blank/comment-only lines. |
| Names, keywords, soft keywords | partial | Initial `Id` handling only; needs Python identifier Unicode rules and keyword/soft-keyword separation. |
| Literals | partial | Int, simple string, bool, and None smoke coverage; bytes, floats, imaginary numbers, full Python string prefixes/escapes, f-strings, t-strings remain. |
| Object model | partial | Minimal value model only; needs heap objects, identity, type hierarchy, attributes, descriptors. |
| Numeric operations | partial | Int/bool unary `+`/`-`/`~`, `+`, `-`, `*`, `%`, `//`, shifts, bitwise operators, and nonnegative `**`; adapter smoke now exercises real Python `//` spelling. Python numeric tower, true division, negative exponent float behavior, full coercions, and error behavior remain. |
| Truth-value testing | partial | Simple int/string/list/tuple/bool/None truthiness and short-circuit `and`/`or`; needs `__bool__`, `__len__`, full containers, and user-defined objects. |
| Name binding and scope | partial | Single environment only; needs module/function/class scopes, globals, nonlocals, comprehensions, annotation scopes. |
| Assignment | partial | Single-name assignment and simple-name `+=`/`-=`/`*=`; needs target lists, unpacking, attributes, subscriptions, annotations, and all augmented assignment operators/target forms. |
| Calls and functions | partial | Single-argument lambda values, adapter-backed single-parameter function definitions, simple returns, recursive calls, and single-positional calls; needs multi-argument call protocol, defaults, varargs, kwargs, closures/cells, decorators, annotations, methods, and real frames. |
| Containers and comprehensions | partial | Minimal list/tuple value displays, equality, membership, truthiness, and positive indexing; direct K smoke uses trailing-comma input while adapter smoke accepts ordinary Python list/tuple displays for the supported subset. Needs full expression-list evaluation, mutation, slices, dicts, sets, ranges, iterators, and comprehensions. |
| Attribute access and descriptors | not-started | Needs `object.__getattribute__`, descriptors, method binding, special method lookup. |
| Classes and metaclasses | not-started | Needs class body execution, namespace, MRO, descriptors, metaclass protocol. |
| Exceptions | not-started | Needs exception objects, raise/propagation, chaining, groups, handlers, finally. |
| Control flow | partial | Adapter-backed `if`, `while`, `break`, and `continue` subsets are covered, along with `pass`, truthy `assert`, and expression-level conditionals; needs `for`, loop `else`, `return`, `yield`, context managers. |
| Import system | not-started | Needs module cache, find/load protocol, packages, relative imports, `__main__`. |
| Pattern matching | not-started | Needs PEP 634/635/636 plus current docs mapping. |
| Coroutines and async | not-started | Needs awaitables, async functions/generators, async with/for. |
| Annotations and type syntax | not-started | Needs deferred annotations, type parameters, `type` statement, annotation scopes. |
| Standard library interactions | not-started | Needs staged builtins/core library coverage and host profile boundaries. |
| CPython profile | not-started | Needs implementation notes, diagnostics, limits, and `Lib/test` classification. |

## Completeness Rule

Do not mark a construct complete merely because CPython accepts a test. Completion requires matching the official docs, a K rule story, and an explicit decision about CPython-specific behavior.
