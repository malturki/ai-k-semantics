---
name: k-formal-semantics
description: Build, review, or maintain formal semantics in the K Framework for programming languages. Use when Codex is asked to define K specifications, translate official language specs into K modules, design modular syntax/configuration/rewrite rules, validate semantics against reference implementations and standard test suites, triage spec/test gaps, or work in repositories for AI-maintained K language semantics.
---

# K Formal Semantics

## Core Posture

Treat every language semantics as an executable formalization of the language maintainer's specification, checked against the language's reference implementation and standard conformance tests.

Default to fidelity over convenience:

- Specify every language construct as a syntactic structure plus semantic rules.
- Avoid abstracting away constructs unless a case-specific rationale is written down.
- Prefer clean, modular K modules that let constructs evolve independently.
- Record provenance for every behavior claim: spec section, reference result, test case, or explicit local design decision.
- Classify underspecification, bad tests, missing tests, and reference implementation quirks instead of hiding them.

## Before Acting

If the task references current language specs, repositories, test suites, K versions, or reference implementation versions, verify them from primary sources or local pinned sources. Specifications and test suites change.

Read the relevant project files before editing. In an `ai-k-semantics`-style repo, start with:

- `README.md`
- `docs/k-framework/*.md`
- `docs/workflows/*.md`
- `languages/<language>/manifest.json`
- `languages/<language>/reference/`
- `languages/<language>/semantics/`
- `languages/<language>/tests/`

For deeper K details, read only the needed references:

- `references/k-framework-primer.md` for K concepts and toolchain.
- `references/specification-methodology.md` for language-semantic methodology.
- `references/repo-workflow.md` for repository layout and validation workflow.

## Workflow

1. Establish the language charter.
   Identify the language version, semantic scope, non-goals, authoritative specification, reference implementation, and standard test suites. Put this in the manifest before extensive implementation.

2. Build a source map.
   Link each construct to spec sections and test coverage. Track ambiguous or missing specification text as first-class notes.

3. Design modules.
   Separate syntax, common domains, configuration, dynamic semantics, symbolic/proof additions, and test/proof modules when the language shape supports it. Keep imports intentional.

4. Specify syntax construct-by-construct.
   Represent each official construct directly in syntax unless there is a documented reason to desugar or abstract it. Prefer explicit K productions over parser shortcuts that erase semantic distinctions.

5. Specify semantics in small slices.
   Start with values and core expressions, then evaluation order, state, binding/scope, functions/modules/classes/control/errors/I/O/concurrency as relevant. Add concrete reference tests for each slice.

6. Validate continuously.
   Use `kompile`, `kast`/`kparse`, and `krun` for parser and concrete execution tests. Use the Haskell backend and `kprove` for symbolic/proof obligations where useful.

7. Differential-test against the reference implementation.
   Compare normalized stdout, stderr, exit status, final state, and errors. Preserve K artifacts on mismatch: parsed/compiled text, rule maps, KORE, proof residuals, and command logs.

8. Triage divergences.
   Classify mismatches as K bug, reference bug, spec ambiguity, unsupported feature, bad test, missing test, normalization issue, or intentional non-goal.

9. Document every compromise.
   If a construct is desugared, abstracted, approximated, unsupported, or intentionally reference-specific, write the reason and the validation implications.

## K Design Rules

- Use `DOMAINS-SYNTAX` for syntax modules and `DOMAINS` or narrower builtin modules for semantics when appropriate.
- Put runtime state in cells; mention only the cells a rule needs and rely on configuration abstraction.
- Define evaluation order with `strict`, `seqstrict`, `context`, and `context alias` where idiomatic, but verify the generated behavior against the language spec.
- Use `KResult` or `isKResult` consistently to define values.
- Keep functions mathematical: use `[function]` rules for semantic functions and top-level cell rules for state transitions.
- Keep generated semantic items such as continuations, frames, environments, and internal markers distinct from user syntax.
- Prefer K's builtin collections only when their algebra and partiality match the language behavior.
- Avoid backend-specific behavior in general semantics; isolate symbolic/proof-only helpers or LLVM/Haskell constraints.

## Output Expectations

When planning, produce a concrete next slice with sources, K modules, tests, and validation commands.

When implementing, edit the repo directly, add or update tests, run available validation, and summarize what is proven, tested, or still unknown.

When reviewing, lead with semantic fidelity risks, missing constructs, underspecified behavior, bad abstractions, missing tests, and modularity problems.
