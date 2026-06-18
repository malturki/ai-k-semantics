# SQL Reference Materials

Retrieved: 2026-06-18.

## Authoritative Reference

The globally accepted reference definition of SQL is the ISO/IEC 9075 standard series, "Information technology - Database languages SQL". The current edition found in the ISO catalog is SQL:2023 / ISO/IEC 9075:2023, published in 2023-06.

ISO/IEC 9075-1:2023, SQL/Framework, is the entry point for the standard series. The ISO catalog describes it as the conceptual framework used by the other parts to specify SQL grammar and statement-processing results, and as the source of common terms and notation.

The technical committee is ISO/IEC JTC 1/SC 32, Data management and interchange. Its structure includes WG 3, Database language.

## Core Parts For This Semantics

- ISO/IEC 9075-1:2023, SQL/Framework: https://www.iso.org/standard/76583.html
- ISO/IEC 9075-2:2023, SQL/Foundation: https://www.iso.org/standard/76584.html
- ISO/IEC 9075-11:2023, SQL/Schemata: https://www.iso.org/standard/76586.html

SQL/Foundation is the first implementation target because it contains the core language constructs. SQL/Schemata becomes relevant when the semantics models catalog state, information schema behavior, and standard schema-visible effects.

## Other Published SQL:2023 Parts

These parts are part of the current ISO/IEC 9075:2023 series, but are out of initial scope unless separately chartered:

- ISO/IEC 9075-3:2023, SQL/CLI: https://www.iso.org/standard/84803.html
- ISO/IEC 9075-4:2023, SQL/PSM: https://www.iso.org/standard/76585.html
- ISO/IEC 9075-9:2023, SQL/MED: https://www.iso.org/standard/84804.html
- ISO/IEC 9075-10:2023, SQL/OLB: https://www.iso.org/standard/84805.html
- ISO/IEC 9075-13:2023, SQL/JRT: https://www.iso.org/standard/84806.html
- ISO/IEC 9075-14:2023, SQL/XML: https://www.iso.org/standard/76587.html
- ISO/IEC 9075-15:2023, SQL/MDA: https://www.iso.org/standard/84807.html
- ISO/IEC 9075-16:2023, SQL/PGQ: https://www.iso.org/standard/79473.html

## Copyright And Access

Do not vendor ISO standard text into this repository. The public ISO catalog pages are useful for citation metadata, but the standards themselves are copyrighted and most parts are paid documents. K rules must cite section identifiers and summarize local design decisions without reproducing protected standard text.

## Reference Implementation Status

SQL does not have a single globally accepted reference implementation. PostgreSQL, SQLite, MySQL, DuckDB, commercial DBMSs, and cloud SQL dialects are implementations/dialects. They may be useful for differential profiles, but none is the normative source for standard SQL.

## Test Suite Status

No current globally accepted public conformance suite for SQL:2023 has been identified yet. Historical NIST/FIPS SQL conformance work and modern vendor/research suites should be investigated, but they must not be treated as authoritative until their scope, status, license, and relation to the current standard are confirmed.
