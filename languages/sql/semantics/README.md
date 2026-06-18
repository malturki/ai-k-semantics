# SQL Semantics

K definitions will live here once the first SQL/Foundation slice is selected.

Initial expected entry points:

```sh
kompile sql.k --main-module SQL --syntax-module SQL-SYNTAX
krun ../tests/examples/simple-select.sql
```

The base modules must target standard SQL, not a vendor dialect. Dialect-specific syntax or behavior belongs in separate profile modules.
