# Sum Verification Experiment

This directory contains a first proof experiment for a tiny Python program:

```python
total = 0
i = 1

while i <= n:
    total = total + i
    i = i + 1

total
```

## Intended Property

For any integer input `n >= 0`, the program terminates with:

```text
total == n * (n + 1) // 2
i == n + 1
result == total
```

## Loop Invariant

At the head of the loop:

```text
1 <= i <= n + 1
total == (i - 1) * i // 2
```

This says that before each iteration, `total` is the sum of all integers from
`1` through `i - 1`. When the loop exits, `i > n`; combined with
`i <= n + 1`, this gives `i == n + 1`, so `total == n * (n + 1) // 2`.

## Files

- `sum.py`: source program being specified.
- `sum-verification.k`: proof helper module layered on the Python semantics.
- `sum-spec.k`: reachability-claim scaffold for the full Python semantics, with
  precondition, postcondition, and loop-invariant preservation/exit obligations.
- `sum-loop-verification.k`: compact K model of just the `sum.py` loop state.
- `sum-loop-spec.k`: proof obligations for the compact loop model.

## Validation Command

From `languages/python/tests/proofs/sum`:

```sh
kompile sum-loop-verification.k \
  --main-module SUM-LOOP-VERIFICATION \
  --backend haskell \
  --output-definition ../../../.build/sum-loop-haskell-kompiled

kprove sum-loop-spec.k \
  --definition ../../../.build/sum-loop-haskell-kompiled \
  --spec-module SUM-LOOP-SPEC
```

## Current Results

The compact loop model currently proves:

- `sum-init-establishes-invariant`
- `sum-loop-exit-implies-postcondition`

The preservation claim, `sum-loop-preserves-invariant`, is still pending. It
requires a solver-friendly form of the arithmetic fact that extending the
partial sum by `i` advances the invariant from `sumTo(i - 1)` to `sumTo(i)`.

The full Python-semantics scaffold is present in `sum-verification.k` and
`sum-spec.k`, but the current Haskell backend proof attempt runs out of memory
when importing the full Python semantics. The compact loop model is intended to
isolate and discharge the core invariant argument first.
