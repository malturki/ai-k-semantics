# Semantics

Place K definitions here.

Suggested files:

- `<language>.k` or `<language>.md` for the main definition.
- `<language>-syntax.k` or a syntax module inside the main literate file.
- `<language>-symbolic.k` for symbolic/proof-only additions when needed.

Keep build commands in this README until the language has a dedicated harness.

Example:

```sh
kompile <language>.k --main-module <LANG> --syntax-module <LANG>-SYNTAX
krun ../tests/examples/example.<ext>
```
