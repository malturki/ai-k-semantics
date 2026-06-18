# Specification Methodology

Use this reference when starting or reviewing a language semantics.

## Authority Order

Prefer sources in this order:

1. Official language specification maintained by the language owner.
2. Official conformance or standard test suite.
3. Official reference implementation behavior.
4. De facto implementation behavior, clearly labeled.
5. Local project decision, clearly labeled as non-standard.

When sources disagree, record the conflict and avoid silently picking one.

## Construct Fidelity

The default is direct representation:

- Every official construct gets syntax in K.
- Every construct gets semantic rules, a documented desugaring, or an explicit unsupported status.
- Do not collapse distinct source constructs just because their early behavior looks similar.
- Do not use parser normalization to erase distinctions that matter for errors, scoping, evaluation order, source locations, warnings, or later phases.

Abstractions are allowed case-by-case when they are:

- behavior-preserving for the target scope
- justified in a note
- covered by tests
- reversible or source-traceable enough for diagnostics

## Modularity

Keep modules aligned with semantic concerns:

- lexical and concrete syntax
- derived syntax/desugaring
- common semantic domains
- configuration
- core dynamic semantics
- feature-specific semantic modules
- symbolic/proof helpers
- conformance test modules and proof modules

Prefer small imports and clear extension points. Avoid one large module for an entire language unless the language is tiny.

## Source Map

Maintain a source map from language constructs to:

- spec section
- K production(s)
- semantic rule(s)
- reference tests
- conformance status
- known gaps

This map is the spine of the project. It makes missing constructs and under-tested behavior visible.

## Testing Principles

Use layered testing:

- parser smoke tests for syntax and ambiguity
- golden examples for local behavior
- standard conformance tests
- differential tests against the reference implementation
- negative tests for errors and stuck states
- proof tests for invariants and reachability properties

For each test, record the reference command, K command, normalization, expected output/error/exit code, and current status.

## Divergence Triage

Classify every mismatch:

- K semantics bug
- K parser/pretty-printer bug
- reference implementation bug
- bad upstream test
- missing upstream test
- spec ambiguity or underspecification
- unsupported feature
- intentional non-goal
- harness or normalization issue
- environment-dependent behavior

Do not normalize away semantic differences. Normalization must be explicit and reviewable.

## Undefined Or Underspecified Behavior

If behavior is undefined, implementation-defined, unspecified, or absent from the spec:

1. Identify the smallest construct or interaction involved.
2. Record all observed reference implementation behaviors.
3. Check standard tests for coverage or absence.
4. Decide whether the K semantics should reject, get stuck, model a nondeterministic choice, or choose a reference profile.
5. Document the decision and add tests.

## Review Checklist

Ask:

- Are any language constructs missing from syntax?
- Were any constructs desugared or abstracted without rationale?
- Are evaluation-order attributes faithful?
- Are values and stuck states precisely defined?
- Are binding, scope, and hygiene modeled explicitly?
- Are errors, exceptions, abrupt control, and resource effects modeled?
- Are reference tests pinned?
- Are failing tests classified?
- Are generated K artifacts available for debugging?
