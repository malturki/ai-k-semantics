# Toolchain And Codebase Notes

## User-Facing Tools

- `kompile`: compile a K definition into a `*-kompiled` directory and backend artifacts.
- `kparse`: parse a term or file according to a compiled definition.
- `kast`: parse expressions/files and emit KAST/KORE-style representations.
- `krun`: execute concrete or symbolic configurations.
- `kprove`: prove K claims against a compiled definition.
- `kore-print`: inspect KORE.

Useful cheat-sheet patterns:

```sh
kompile definition.k
krun program.ext
krun -cPGM='program text'
kast --output kore -e 'term'
kompile --backend haskell --enable-search definition.k
krun --search-all program.ext
kprove spec.k
```

## Compilation Artifacts To Preserve

`kompile` writes important files into the `*-kompiled` directory. Future harnesses should be able to archive or inspect:

- `parsed.txt`
- `compiled.txt`
- `allRules.txt`
- `parsed.json` and `compiled.json` when `--emit-json` is used
- `definition.kore` or generated KORE files
- `syntaxDefinition.kore`
- `macros.kore`
- generated parsers such as `parser_PGM`
- `backend.txt`
- backend-specific executables or decision trees

These artifacts are valuable for triage when a generated semantics disagrees with a reference implementation.

## Main Java Architecture

The upstream source is Maven-based and split into modules:

- `k-frontend`: command-line tools, parsing, definition data structures, compilation passes, unparsing, and proof frontend logic.
- `k-distribution`: scripts, packaging, tutorials, builtins, and smoke/regression tests.
- `llvm-backend`: concrete backend wiring that emits KORE, decision trees, and LLVM executables.
- `haskell-backend`: symbolic backend integration.
- `pyk`: Python scripting interface for K artifacts and workflows.

## Entry Flow

`org.kframework.main.Main` dispatches the first CLI argument to frontend modules:

- `-kompile`
- `-kast`
- `-kdep`
- `-kprove`
- `-kserver`
- `-klsp`

It uses Java `ServiceLoader` and Guice modules so backend modules can contribute tool-specific bindings.

Each frontend extends `FrontEnd`, which centralizes help/version handling, timeouts, shutdown behavior, temp directory cleanup, and error reporting.

## Kompile Flow

`KompileFrontEnd` checks the definition file, builds a `Kompile` instance, gets the selected backend, and runs:

1. Parse the definition.
2. Run pre-compilation structural checks.
3. Apply the backend compilation pipeline.
4. Run post-compilation checks.
5. Save compiled artifacts.
6. Let the backend produce backend-specific artifacts.

`Kompile` stores parsed and compiled definitions, optional JSON, a rule source map, parser artifacts, and the serialized `compiled.bin` used by later tools.

## Parsing Flow

`DefinitionParsing` handles outer parsing, module loading, `requires`, bubble parsing for rules/configurations/contexts, parse caches, regex checks, config bubble resolution, and non-config bubble resolution.

Practical implication: syntax definitions and semantic sentences interact through generated grammars. Ambiguity, attributes, and module imports can change how rules parse, so parser-focused tests matter.

## KORE Backend Pipeline

`KoreBackend.steps()` defines the default frontend-to-KORE transformation pipeline. Major passes include:

- resolving commutative simplification rules
- resolving I/O streams
- resolving `#fun`
- resolving functions with configuration context
- resolving `strict` and `seqstrict`
- resolving anonymous variables
- resolving contexts and heat/cool attributes
- semantic casts
- guard-or patterns
- fresh constants
- sort predicates and sort projections
- macro expansion
- implicit computation cells
- simplification rule checks
- cell concretization
- coverage
- language parsing module generation
- configuration variable handling
- sentence numbering

For language semantics work, this means source K is intentionally higher-level than what the backend sees. When debugging, inspect both parsed and compiled artifacts.

## LLVM Backend

`LLVMBackend` extends `KoreBackend`. It writes `definition.kore`, runs matching compilation to produce a decision tree, then invokes `llvm-kompile` to build an interpreter, library, search executable, Python target, or C target depending on options.

This is the primary path for high-volume concrete conformance tests.

## Haskell Backend And Proofs

`KProve` builds a proof definition, creates a backend rewriter, calls `rewriter.prove`, and pretty-prints the resulting claim state. The Haskell backend supports symbolic execution with matching-logic constraints and SMT assistance.

This is the primary path for reachability claims, simplification lemmas, and symbolic tests.

## pyk

`pyk` is distributed as the `kframework` Python package. It is the likely place to automate future workflows around KAST/KORE parsing, subprocess orchestration, proof result triage, and generated test harnesses.
