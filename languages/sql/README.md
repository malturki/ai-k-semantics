# SQL

Planned K semantics for standard SQL, targeting SQL:2023 / ISO/IEC 9075:2023.

The global reference definition for SQL is the ISO/IEC 9075 series, maintained under ISO/IEC JTC 1/SC 32. For this repository, the first semantic target is SQL/Foundation, not a vendor dialect.

## Current Charter

- Primary specification: ISO/IEC 9075-2:2023 SQL/Foundation.
- Framework and terminology: ISO/IEC 9075-1:2023 SQL/Framework.
- Catalog/schema model: ISO/IEC 9075-11:2023 SQL/Schemata.
- Initial status: planned.
- Reference implementation: none globally accepted.
- Conformance suite: no current globally accepted public SQL:2023 suite identified yet.

## Working Rule

Treat every SQL construct as standard syntax plus semantics unless the construct is explicitly deferred. Vendor behavior belongs in named profiles, not in the base SQL semantics.
