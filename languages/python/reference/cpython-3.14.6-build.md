# CPython 3.14.6 Reference Build

Recorded: 2026-06-18.

This project uses CPython 3.14.6 as the primary reference implementation for differential testing and ambiguity triage. Portable Python semantics still come from the official Python documentation first; CPython-only behavior belongs in the CPython profile.

## Source Archive

- Release page: https://www.python.org/downloads/release/python-3146/
- Source archive: https://www.python.org/ftp/python/3.14.6/Python-3.14.6.tar.xz
- SHA-256: `143b1dddefaec3bd2e21e3b839b34a2b7fb9842272883c576420d605e9f30c63`

The local archive was downloaded to `.external/Python-3.14.6.tar.xz` and verified with `sha256sum`.

## Local Build

The source was extracted to `.external/Python-3.14.6` and configured with:

```sh
./configure --prefix=/home/openclaw/workarea/repos/ai-k-semantics/.external/cpython-3.14.6-install
make -j2
```

The resulting build-tree interpreter reports:

```text
Python 3.14.6
3.14.6 (main, Jun 18 2026, 19:56:37) [GCC 13.3.0]
```

## Optional Module Gaps

This local container build is good enough for reference smoke checks, but it is not a fully provisioned CPython regression-test environment. Configure/build reported these missing or disabled optional modules:

- Disabled: `_sqlite3`
- Missing: `_bz2`, `_curses`, `_curses_panel`, `_dbm`, `_gdbm`, `_hashlib`, `_lzma`, `_ssl`, `_tkinter`, `_uuid`, `_zstd`, `readline`

Do not interpret failures or skips in tests depending on these modules as language-semantics evidence.

## Harness Use

From the repository root:

```sh
PYTHON_REF=/home/openclaw/workarea/repos/ai-k-semantics/.external/Python-3.14.6/python \
CPYTHON_SOURCE=/home/openclaw/workarea/repos/ai-k-semantics/.external/Python-3.14.6 \
languages/python/harness/run-cpython-suite.sh
```

The harness defaults to the small reference smoke subset:

```sh
python -m test --single-process --timeout 120 test_grammar
```

Set `CPYTHON_TEST_ARGS` to run a different classified subset. Running the full suite intentionally requires an explicit argument such as:

```sh
CPYTHON_TEST_ARGS="-m test" ...
```
