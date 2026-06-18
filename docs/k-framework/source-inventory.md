# K Framework Source Inventory

Captured on 2026-06-18.

## Official Web Sources

- K homepage: https://kframework.org/
- User manual: https://kframework.org/docs/user_manual/
- K tutorial: https://kframework.org/k-distribution/k-tutorial/
- Tool reference: https://kframework.org/docs/ktools/
- Builtins/prelude: https://kframework.org/k-distribution/include/kframework/
- PL tutorial and reference language definitions: https://kframework.org/k-distribution/pl-tutorial/
- pyk docs: https://kframework.org/pyk/

## Local Upstream Clones

These clones are research inputs, not vendored dependencies of this repo.

```text
/home/openclaw/workarea/repos/k-framework-upstream
  remote: https://github.com/runtimeverification/k.git
  commit: 4a46d12 Set Version: 7.1.337

/home/openclaw/workarea/repos/k-pl-tutorial-upstream
  remote: https://github.com/runtimeverification/pl-tutorial.git
  commit: 83761c9 Update dependency: deps/k_release (#42)
```

## What Was Reviewed

From `runtimeverification/k`:

- `README.md` for build, packaging, and developer orientation.
- `docs/user_manual.md`, `docs/ktools.md`, and `docs/cheat_sheet.md`.
- `k-distribution/k-tutorial` lessons for syntax, rewriting, configurations, evaluation order, symbolic execution, and proofs.
- `k-distribution/include/kframework/builtin` for `domains.md`, `kast.md`, `prelude.md`, and related standard library modules.
- `k-distribution/tests/smoke/imp.k` as a compact executable semantics example.
- Frontend and backend entry points:
  - `org.kframework.main.Main`
  - `org.kframework.main.FrontEnd`
  - `org.kframework.kompile.KompileFrontEnd`
  - `org.kframework.kompile.Kompile`
  - `org.kframework.kompile.DefinitionParsing`
  - `org.kframework.backend.kore.KoreBackend`
  - `org.kframework.backend.llvm.LLVMBackend`
  - `org.kframework.kprove.KProve`
- `pyk/README.md` for the Python scripting interface.

From `runtimeverification/pl-tutorial`:

- Top-level README and language progression.
- LAMBDA, IMP, IMP++, and type-system examples at a high level.
- SIMPLE, KOOL, FUN, and LOGIK language definitions and bundled tests as larger reference patterns.

## Graphify Orientation

Graphify was used for repository detection. The full `runtimeverification/k` clone detected 890 supported files and roughly 681,072 words, mostly implementation code. A full semantic graph pass was not run because this Codex environment only allows subagent spawning when explicitly requested, while graphify's semantic extraction path prefers subagents. The source review therefore combined graphify detection with direct code and documentation inspection.

## Source Reliability Notes

- The official user manual says it is still under construction, so manual notes here should be treated as practical guidance, not as a complete language-lawyer spec.
- The official site notes that parts of the PL tutorial may be out of date relative to modern K. Use it as a pattern library and compare against current K behavior before copying idioms.
- For future language semantics, each source entry should capture an exact version, commit, release tag, or archival URL.
