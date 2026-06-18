# Reference Implementation Validation

The goal is not just to make a K semantics execute. The goal is to make it agree with the language's reference implementation or documented specification, and to know exactly where it does not.

## Test Tiers

- Smoke tests: small local examples that compile and run quickly.
- Golden tests: pinned programs with expected outputs.
- Reference-suite tests: official or de facto conformance suites.
- Differential tests: same generated or curated program run under both K and the reference implementation.
- Negative tests: parse errors, runtime errors, type errors, and undefined behavior boundaries.
- Proof tests: `claim`-based reachability properties, invariants, or semantic equivalences.

## Differential Loop

For each test case:

1. Run the reference implementation.
2. Normalize output, errors, and exit code using documented rules.
3. Run the K semantics through `kompile` plus `krun`, or a precompiled interpreter.
4. Normalize K output.
5. Compare results.
6. Store logs and generated K artifacts on mismatch.
7. Classify the mismatch.

Mismatch classes:

- K bug
- reference implementation bug
- spec ambiguity
- unsupported feature
- intentional non-goal
- harness normalization issue
- nondeterministic or environment-dependent behavior

## Normalization

Normalization must be explicit and language-specific. Examples:

- whitespace-only output differences
- path prefixes
- nondeterministic object addresses
- timestamp or random data
- implementation-defined error wording
- exit-code conventions

Never normalize away semantic content without a note.

## Undefined And Implementation-Defined Behavior

If the language has undefined or implementation-defined behavior, tests should classify it before comparison. Do not force K to match accidental reference behavior unless the project explicitly chooses that profile.

## Artifact Policy

For failed cases, preserve enough to reproduce:

- input program
- command lines
- environment variables
- reference output
- K output
- `parsed.txt`
- `compiled.txt`
- `allRules.txt`
- KORE artifacts when useful
- proof residuals for `kprove`

Generated artifacts should normally stay out of git, but CI can upload them as run artifacts.
