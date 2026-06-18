# Language Onboarding Workflow

Use this checklist when adding a new language under `languages/<language-id>`.

## 1. Charter

Create or update `manifest.json` with:

- language name and short identifier
- intended semantic scope
- status
- owner or maintainer
- official specifications
- reference implementations
- reference test suites
- known non-goals

Do this before writing significant K code.

## 2. Source Corpus

Record exact source versions:

- spec version, edition, or commit
- reference implementation release and commit
- test-suite release and commit
- relevant standards documents
- known errata

Store notes under `reference/` and `notes/`. Do not vendor large upstream test suites by default; prefer scripts or manifests that can fetch pinned versions.

## 3. Semantic Slices

Build in small slices:

1. lexical tokens and parser smoke tests
2. values and core expressions
3. evaluation order and control contexts
4. state model
5. declarations, binding, and scope
6. functions/calls/modules
7. errors and stuck states
8. I/O and host interaction
9. concurrency or nondeterminism, if present
10. proofs and symbolic tests

Each slice should have concrete reference cases.

## 4. K Structure

Recommended K module split:

- `<LANG>-SYNTAX`
- `<LANG>-COMMON`
- `<LANG>-CONFIGURATION`
- `<LANG>-SEMANTICS`
- `<LANG>-PARSING` if extra parser entry modules are needed
- `<LANG>-SYMBOLIC` for Haskell/backend-specific symbolic additions
- `<LANG>-PROOFS` or separate proof modules under `tests/proofs`

This split is a guideline. Follow the language's real shape over rigid naming.

## 5. Reference Testing

Every reference test should record:

- input program
- input stdin/environment, if any
- reference command
- reference version
- expected stdout/stderr/exit code
- K command
- normalization rules
- current result
- known divergence issue, if any

## 6. Review Gate

Before moving a language beyond `experimental`, require:

- parser round-trip or parse-tree sanity cases
- positive and negative concrete tests
- reference-suite differential run
- known divergence report
- artifact preservation strategy
- at least one proof or symbolic sanity case where useful
