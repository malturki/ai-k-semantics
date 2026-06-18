# Languages

Each subdirectory represents one language semantics effort.

Start by copying `_template`:

```sh
cp -R languages/_template languages/<language-id>
```

Then edit `languages/<language-id>/manifest.json` and replace the template values.

Expected maturity values:

- `planned`: sources identified, no executable semantics yet
- `experimental`: partial semantics, local tests only
- `reference-testing`: differential/reference-suite testing in progress
- `proof-testing`: proof-oriented tests in progress
- `maintained`: CI-backed semantics with documented coverage and known gaps

Do not use `_template` as a real language entry.
