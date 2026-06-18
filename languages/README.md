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

## Current Language Entries

- `python`: planned Python 3.14.6 semantics, using the official Python docs as the primary reference and CPython 3.14.6 as the reference implementation profile.
- `sql`: planned SQL:2023 research charter, currently parked while Python is the active target.
