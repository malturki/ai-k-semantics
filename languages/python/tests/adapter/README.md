# Python Adapter Smoke Tests

These files are real Python source programs parsed by CPython's `ast` module and
translated by `harness/python_to_k_input.py` into the current K input subset.

The adapter is not a semantics shortcut. It is a temporary parser bridge for
constructs whose syntax is already represented in K but whose concrete Python
spelling is not yet accepted directly by the K frontend.
