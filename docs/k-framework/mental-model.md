# K Mental Model

K is a rewrite-based executable semantic framework. A K definition describes a language or system with syntax, state, and behavior. The toolchain compiles that definition and derives useful tools such as parsers, interpreters, symbolic executors, model-checking/search workflows, and proof workflows.

## Specification Anatomy

A K specification is built from files, modules, and sentences.

- Files use `requires` to include other files.
- Modules use `imports` to reuse other modules.
- The file and module dependency graphs are expected to be acyclic.
- `syntax` declarations define sorts, tokens, productions, lexical syntax, syntactic lists, priorities, associativity, labels, hooks, and attributes.
- `configuration` declarations define the initial state as nested cells.
- `rule`, `context`, `context alias`, and `claim` declarations define behavior, evaluation contexts, and proof obligations.

The three recurring design questions for a language semantics are:

1. What terms can programs contain?
2. What state exists at runtime?
3. Which rewrites are valid transitions?

## Configurations And Cells

Runtime state is organized into labeled cells, written with XML-like syntax such as `<k> ... </k>` or `<store> ... </store>`. Cells can be nested. K's configuration abstraction lets a rule mention only the cells it needs; the compiler completes missing parent cells from the declared configuration.

Common patterns:

- `<k>` contains the current computation.
- `<store>`, `<env>`, `<state>`, `<heap>`, `<stack>`, and `<threads>` encode language-specific state.
- `$PGM` is the conventional configuration variable for the initial program.
- Other `$NAME` configuration variables can parameterize execution via `krun -cNAME=...`.

## K Sequences

The `<k>` cell usually holds a term of sort `K`, which acts like a sequence of computational tasks joined by `~>` and ending in `.K`. K injects ordinary program terms into `KItem`, so computations can mix program fragments with semantic continuation items such as frames, saved environments, or control markers.

This is one of K's core strengths: control-intensive features like exceptions, return, call/cc, threads, and abrupt termination can be represented by rewriting and rearranging computation items.

## Rewriting

Top-level semantic rules usually mention one or more cells. A rule rewrites the current configuration by matching the left side, applying the substitution, and producing the right side.

K supports local rewrites inside larger terms:

```k
rule <k> I1:Int + I2:Int => I1 +Int I2 ...</k>
```

The ellipsis in a `K` cell says that the suffix of the computation is not relevant and should be preserved.

Function rules are different from top-level rules. A production with `[function]` is a mathematical function, and its rules simplify function applications rather than advance the whole configuration.

## Evaluation Order

K can encode evaluation order explicitly with heating and cooling rules, but idiomatic modern definitions use:

- `strict` and `seqstrict` production attributes.
- `context` declarations.
- `context alias` declarations.
- `KResult` or `isKResult` predicates to identify values that should no longer be heated.

For a new language, evaluation-order policy should be documented near the syntax module. This avoids accidental mismatches with a reference interpreter.

## Builtins

The builtins/prelude provide practical sorts and operations for definitions:

- `DOMAINS-SYNTAX` for program-level syntax of identifiers, integers, booleans, and strings.
- `DOMAINS` for common semantic domains such as `INT`, `BOOL`, `STRING`, `LIST`, `MAP`, `SET`, `K-IO`, and equality.
- `kast.md` for K's internal sorts, `K`, `KItem`, `KConfigVar`, K sequences, matching-logic syntax, and variable syntax.
- Specialized modules for arrays, JSON, rational numbers, FFI, substitution, and unification.

Use builtin collection operations carefully. Some operations are partial; the docs warn that undefined inputs can make generated LLVM interpreters crash.

## Backends

The LLVM backend is the normal concrete execution backend. It is fast and suited to running reference suites.

The Haskell backend is the symbolic backend. It uses unification rather than simple pattern matching, tracks matching-logic constraints, and delegates satisfiability questions to SMT solvers such as Z3. It is the natural backend for symbolic execution and `kprove`.

KORE is the intermediate representation produced from K specifications and consumed by backends. The frontend compiles K into KORE, and then backend-specific machinery builds interpreters or proof/search engines from it.

## Proofs

`claim` sentences describe reachability properties. `kprove` builds a proof definition from a compiled semantics plus a proof/spec module, then asks the backend rewriter to prove the claims. Successful proofs print `#Top`; failed proofs usually include a residual matching-logic condition and final configuration showing where implication failed.

For this repository, proofs should supplement concrete conformance tests. They are especially useful for language-independent invariants, desugaring equivalences, type-safety sketches, and small semantic kernels.
