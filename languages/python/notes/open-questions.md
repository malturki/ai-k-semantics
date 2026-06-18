# Python Open Questions

- Should the first milestone target all of Python 3.14 syntax with partial semantics, or a smaller executable syntax subset with full semantics?
- How should the base semantics represent implementation notes from the Language Reference?
- Which CPython diagnostics and SyntaxError messages should be normalized, and which should be left profile-specific?
- How should object identity and lifetime be modeled without adopting CPython reference counting?
- Which parts of `importlib` and filesystem behavior belong in the base language semantics?
- What host profile should be used for standard streams, command-line arguments, environment variables, filesystem paths, time, locale, and random hash seeds?
- How soon should free-threaded Python, subinterpreters, and thread-safety guarantees enter scope?
- Which PEPs need source maps before implementation starts: structural pattern matching, exception groups, type parameters, deferred annotations, template string literals, assignment expressions, and PEG grammar are early candidates.
