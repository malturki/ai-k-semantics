# K Framework Primer

Use this reference when you need to recall K concepts, toolchain shape, or implementation artifacts.

## K Specification Anatomy

K definitions are made of files, modules, and sentences.

- `requires` includes files.
- `imports` reuses modules.
- `syntax` declares sorts, productions, tokens, priorities, associativity, labels, hooks, and attributes.
- `configuration` declares the initial runtime state as nested cells.
- `rule` defines rewrite behavior.
- `context` and `context alias` define evaluation contexts.
- `claim` states reachability properties for proof.

## Cells And Configuration

Runtime state is organized in cells such as `<k>`, `<store>`, `<env>`, `<heap>`, `<stack>`, and `<threads>`.

The `<k>` cell usually stores a `K` sequence: computation items separated by `~>` and ending in `.K`. K injects program terms into `KItem`, so semantic continuation items can sit beside source-language terms.

Configuration abstraction lets rules mention only relevant cells. The compiler completes parent cells based on the declared configuration.

## Rules And Functions

Top-level rules usually mention cells and advance the whole configuration. Function rules simplify applications of productions marked `[function]`.

Use local rewrites to say what changes while preserving context:

```k
rule <k> I1:Int + I2:Int => I1 +Int I2 ...</k>
```

The ellipsis in a `K` cell preserves the rest of the computation.

## Evaluation Order

Idiomatic K evaluation order uses:

- `strict` and `seqstrict` production attributes
- `context` declarations
- `context alias` declarations
- `KResult` or `isKResult` predicates

Explicit heating/cooling rules still exist, but generated contexts are usually cleaner. Verify strictness carefully against the reference language, especially for short-circuiting, lazy constructs, assignment, control transfer, and function application.

## Builtins

Common modules:

- `DOMAINS-SYNTAX`: program-level syntax for identifiers, integers, booleans, strings.
- `DOMAINS`: common semantics modules, including `INT`, `BOOL`, `STRING`, `LIST`, `MAP`, `SET`, `K-IO`, and equality.
- `kast.md`: internal K sorts, K sequences, matching-logic syntax, variable syntax, and cells.
- Other builtins: arrays, JSON, rational numbers, FFI, substitution, unification.

Some builtin functions are partial. Undefined inputs can produce backend crashes, especially in LLVM-generated interpreters.

## Toolchain

Core tools:

```sh
kompile definition.k
kast --output kore -e 'term'
kparse file | kore-print -
krun program.ext
kompile --backend haskell definition.k
kprove spec.k
```

`kompile` writes useful artifacts into `*-kompiled`, including `parsed.txt`, `compiled.txt`, `allRules.txt`, optional JSON, KORE files, parsers, backend metadata, and backend executables.

LLVM is the main concrete execution backend for high-volume tests.

The Haskell backend is the symbolic backend. It uses unification, matching-logic constraints, and SMT solvers such as Z3. Use it for symbolic execution and `kprove`.

KORE is the intermediate representation emitted by the frontend and consumed by backends.

## Upstream Codebase Orientation

Important upstream areas:

- `k-frontend`: CLI frontends, parsing, K data structures, compile passes, proof frontend.
- `k-distribution`: scripts, tutorials, builtins, tests, packaging.
- `llvm-backend`: concrete backend wiring and LLVM compilation.
- `haskell-backend`: symbolic backend integration.
- `pyk`: Python tooling for K artifacts and workflows.

Important frontend flow:

- `org.kframework.main.Main` dispatches tools.
- `FrontEnd` centralizes CLI lifecycle.
- `KompileFrontEnd` builds `Kompile`, runs the backend pipeline, saves artifacts.
- `DefinitionParsing` handles file/module loading and bubble parsing.
- `KoreBackend.steps()` applies the main lowering pipeline.
- `KProve` builds proof definitions and invokes the backend prover.
