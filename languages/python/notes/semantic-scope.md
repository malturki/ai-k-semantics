# Python Semantic Scope

## Base Target

The base semantics should model portable Python 3.14 language behavior from the official docs, with CPython behavior available as a separate profile.

Candidate module split:

- `PYTHON-SYNTAX`: lexical structure, indentation tokens, grammar, and concrete syntax.
- `PYTHON-COMMON`: object references, primitive values, truth values, names, exceptions, attributes, descriptors, and result categories.
- `PYTHON-CONFIGURATION`: frames, call stack, globals, locals, builtins, heap/object store, module table, import state, exception state, standard streams, and environment profile.
- `PYTHON-DATA-MODEL`: objects, types, attributes, special methods, descriptors, functions, methods, classes, metaclasses, modules, iterators, generators, coroutines, and async generators.
- `PYTHON-EXPRESSIONS`: atoms, primaries, calls, subscriptions, slicing, comprehensions, operators, comparisons, boolean operations, lambdas, conditional expressions, assignment expressions, and evaluation order.
- `PYTHON-STATEMENTS`: assignment, annotated assignment, assert, pass, del, return, yield, raise, break, continue, import, global, nonlocal, type statements, and compound statements.
- `PYTHON-IMPORT`: modules, packages, import search, loading, caching, and `__main__` behavior.
- `PYTHON-BUILTINS`: built-in functions, constants, exceptions, and built-in types required for core language execution.
- `PYTHON-CPYTHON-PROFILE`: CPython-specific implementation notes, diagnostics, limits, and test normalizers.
- `PYTHON-SYMBOLIC`: proof-only helpers and backend-specific constraints.

## Early Construct Families

- source encoding, line structure, indentation, comments, names, keywords, literals, operators, and delimiters
- expression statements and scalar literals
- object identity, type, value, truth-value testing, and built-in constants
- name binding and scope in modules, functions, classes, and comprehensions
- assignment, augmented assignment, annotated assignment, deletion, and locals/globals effects
- arithmetic, comparison, boolean, attribute, subscription, slicing, and call evaluation
- lists, tuples, dictionaries, sets, ranges, strings, bytes, and numeric types
- function definitions, calls, default arguments, closures, decorators, generators, and coroutines
- classes, descriptors, method binding, metaclasses, and special method lookup
- exceptions, chaining, `try`, `except`, `except*`, `finally`, `raise`, `assert`, and context managers
- control flow: `if`, `while`, `for`, `break`, `continue`, `return`, `yield`
- imports, modules, packages, relative imports, and `__main__`
- structural pattern matching
- annotations, type parameter lists, deferred annotation behavior, and the `type` statement

## Main Semantic Risks

- The official reference is not fully formal; prose ambiguities must be turned into explicit issues with CPython evidence where needed.
- CPython has implementation notes and observable quirks. Keep them out of the portable base unless the docs define them as language behavior.
- Python object semantics depend on attribute access, descriptors, special methods, metaclasses, and dynamic mutation; shallow object models will be wrong quickly.
- Evaluation order is specified and must be represented directly, especially for calls, comprehensions, assignment expressions, context managers, and exception handling.
- Import behavior is partly language semantics and partly host/environment behavior; it needs a controlled module store for reproducible tests.
- Standard library behavior is huge. Builtins and core data types should be prioritized before broad library semantics.
- Concurrency and free-threaded CPython behavior require separate scope decisions.

## First Implementation Slice

1. Define a parser/tokenizer slice for modules containing literals, expression statements, assignments, and simple function definitions.
2. Model objects, names, frames, heap/object store, and built-in constants.
3. Implement literal evaluation, arithmetic, truth-value testing, simple assignment, `if`, `while`, and function calls.
4. Add CPython differential tests using `python3.14` or pinned CPython 3.14.6 once available locally.
5. Expand to exceptions, containers, comprehensions, and special method dispatch before classes become feature-complete.
