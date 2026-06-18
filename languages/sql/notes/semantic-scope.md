# SQL Semantic Scope

## Base Target

The base semantics should model standard SQL/Foundation before any dialect profile. The first K modules should make the declarative SQL core executable over an explicit catalog and database instance.

Candidate module split:

- `SQL-SYNTAX`: lexical items and official SQL syntactic constructs.
- `SQL-COMMON`: values, NULL, truth values, identifiers, names, table/row/bag domains, diagnostics placeholders.
- `SQL-CATALOG`: schemas, tables, columns, constraints, routines where in scope, and information needed by name resolution.
- `SQL-CONFIGURATION`: current catalog, current schema, current session parameters selected for the standard profile, database contents, and result/diagnostic cells.
- `SQL-QUERY`: query expressions, table expressions, predicates, joins, grouping, aggregation, set operations, ordering, and limits where standard.
- `SQL-DML`: INSERT, UPDATE, DELETE, MERGE, and effects on database contents.
- `SQL-DDL`: schema object creation, alteration, and dropping for the selected core slice.
- `SQL-SYMBOLIC`: proof-only helpers and backend-specific constraints, isolated from executable semantics.

## Early Construct Families

- scalar values and type domains
- NULL and three-valued logic
- identifiers, delimited identifiers, qualified names, and name resolution
- row values, table values, bags/multisets, and duplicate handling
- comparison, quantified predicates, `IS NULL`, `LIKE`, `BETWEEN`, `IN`, and boolean connectives
- SELECT query expressions, FROM, WHERE, GROUP BY, HAVING, SELECT list, aliases, DISTINCT, ORDER BY
- joins, subqueries, correlation, derived tables, common table expressions
- aggregation and window-function boundary decisions
- set operations
- schema/catalog state and constraints
- core DDL and DML

## Main Semantic Risks

- SQL is declarative, but the K executable semantics still needs a deterministic representation for relation-producing computations.
- SQL tables are not simple mathematical sets; duplicate rows, NULLs, column names, ordering boundaries, and bags matter.
- Three-valued logic must be modeled directly and tested heavily.
- Name resolution is a major part of the semantics and should not be hidden behind parser shortcuts.
- Many features are optional or profile-dependent in the standard; the manifest must track supported feature sets.
- Vendor engines often diverge from the standard, so reference testing must classify dialect behavior instead of folding it into the base semantics.

## First Implementation Slice

1. Define lexical and parser smoke tests for a small SQL/Foundation fragment.
2. Define standard scalar values, NULL, truth values, and predicates.
3. Define table values as bags of rows with named columns.
4. Execute `VALUES` and simple `SELECT ... FROM ... WHERE ...` over an explicit in-memory catalog.
5. Add concrete tests with expected standard behavior before comparing to any vendor engine.
