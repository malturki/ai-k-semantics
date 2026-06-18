# Python Conformance Tests

Conformance tests for the base semantics must cite the Python Language Reference, Standard Library reference, or a current accepted/final PEP.

The CPython regression suite is the primary reference suite for the CPython profile. Imported tests should be classified before use so implementation-specific and platform-dependent behavior does not accidentally define the portable base semantics.

`cpython-classification.json` is the seed classification ledger for upstream `Lib/test` files. A test is not ready for K differential execution until it has a construct reference, a review status, and an adapter/extraction plan.
