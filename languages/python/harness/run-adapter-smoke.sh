#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEF="$ROOT/semantics/python.k"
WORK="$ROOT/.build"
KOMPILED="$WORK/python-kompiled"
PYTHON_REF="${PYTHON_REF:-python3}"
ADAPTER="$ROOT/harness/python_to_k_input.py"

mkdir -p "$WORK"

kompile "$DEF" \
  --main-module PYTHON \
  --syntax-module PYTHON-SYNTAX \
  --output-definition "$KOMPILED"

run_case() {
  local name="$1"
  local source="$2"
  local expected="$3"
  local adapted="$WORK/$name.kinput.py"
  local output="$WORK/$name.adapter.out"

  "$PYTHON_REF" "$source"
  "$PYTHON_REF" "$ADAPTER" "$source" > "$adapted"
  krun "$adapted" --definition "$KOMPILED" > "$output"

  if ! grep -q "^[[:space:]]*\\.K$" "$output"; then
    echo "FAIL $name: final <k> cell is not .K" >&2
    cat "$output" >&2
    exit 1
  fi

  if ! grep -q -- "$expected" "$output"; then
    echo "FAIL $name: expected result $expected" >&2
    cat "$output" >&2
    echo "Adapted input:" >&2
    cat "$adapted" >&2
    exit 1
  fi

  echo "PASS $name"
}

run_case "adapter-floor-div" "$ROOT/tests/adapter/adapter-floor-div.py" "True ~> .K"
run_case "adapter-string-repeat" "$ROOT/tests/adapter/adapter-string-repeat.py" "True ~> .K"
run_case "adapter-string-slice" "$ROOT/tests/adapter/adapter-string-slice.py" "True ~> .K"
run_case "adapter-string-slice-step" "$ROOT/tests/adapter/adapter-string-slice-step.py" "True ~> .K"
run_case "adapter-string-slice-negative-step" "$ROOT/tests/adapter/adapter-string-slice-negative-step.py" "True ~> .K"
run_case "adapter-list-normal" "$ROOT/tests/adapter/adapter-list-normal.py" "True ~> .K"
run_case "adapter-list-expressions" "$ROOT/tests/adapter/adapter-list-expressions.py" "True ~> .K"
run_case "adapter-list-negative-index" "$ROOT/tests/adapter/adapter-list-negative-index.py" "True ~> .K"
run_case "adapter-list-ordering" "$ROOT/tests/adapter/adapter-list-ordering.py" "True ~> .K"
run_case "adapter-list-concat" "$ROOT/tests/adapter/adapter-list-concat.py" "True ~> .K"
run_case "adapter-list-repeat" "$ROOT/tests/adapter/adapter-list-repeat.py" "True ~> .K"
run_case "adapter-list-slice" "$ROOT/tests/adapter/adapter-list-slice.py" "True ~> .K"
run_case "adapter-list-slice-step" "$ROOT/tests/adapter/adapter-list-slice-step.py" "True ~> .K"
run_case "adapter-list-slice-negative-step" "$ROOT/tests/adapter/adapter-list-slice-negative-step.py" "True ~> .K"
run_case "adapter-tuple-normal" "$ROOT/tests/adapter/adapter-tuple-normal.py" "True ~> .K"
run_case "adapter-tuple-expressions" "$ROOT/tests/adapter/adapter-tuple-expressions.py" "True ~> .K"
run_case "adapter-tuple-negative-index" "$ROOT/tests/adapter/adapter-tuple-negative-index.py" "True ~> .K"
run_case "adapter-tuple-ordering" "$ROOT/tests/adapter/adapter-tuple-ordering.py" "True ~> .K"
run_case "adapter-tuple-concat" "$ROOT/tests/adapter/adapter-tuple-concat.py" "True ~> .K"
run_case "adapter-tuple-repeat" "$ROOT/tests/adapter/adapter-tuple-repeat.py" "True ~> .K"
run_case "adapter-tuple-slice" "$ROOT/tests/adapter/adapter-tuple-slice.py" "True ~> .K"
run_case "adapter-tuple-slice-step" "$ROOT/tests/adapter/adapter-tuple-slice-step.py" "True ~> .K"
run_case "adapter-tuple-slice-negative-step" "$ROOT/tests/adapter/adapter-tuple-slice-negative-step.py" "True ~> .K"
run_case "adapter-lambda-normal" "$ROOT/tests/adapter/adapter-lambda-normal.py" "7 ~> .K"
run_case "adapter-if" "$ROOT/tests/adapter/adapter-if.py" "True ~> .K"
run_case "adapter-if-no-else" "$ROOT/tests/adapter/adapter-if-no-else.py" "True ~> .K"
run_case "adapter-is-none" "$ROOT/tests/adapter/adapter-is-none.py" "True ~> .K"
run_case "adapter-is-bool" "$ROOT/tests/adapter/adapter-is-bool.py" "True ~> .K"
run_case "adapter-chained-comparison" "$ROOT/tests/adapter/adapter-chained-comparison.py" "True ~> .K"
run_case "adapter-chained-comparison-short-circuit" "$ROOT/tests/adapter/adapter-chained-comparison-short-circuit.py" "False ~> .K"
run_case "adapter-chained-identity" "$ROOT/tests/adapter/adapter-chained-identity.py" "True ~> .K"
run_case "adapter-while" "$ROOT/tests/adapter/adapter-while.py" "True ~> .K"
run_case "adapter-while-else-normal" "$ROOT/tests/adapter/adapter-while-else-normal.py" "True ~> .K"
run_case "adapter-while-else-break" "$ROOT/tests/adapter/adapter-while-else-break.py" "True ~> .K"
run_case "adapter-nested-if-while" "$ROOT/tests/adapter/adapter-nested-if-while.py" "True ~> .K"
run_case "adapter-break" "$ROOT/tests/adapter/adapter-break.py" "True ~> .K"
run_case "adapter-continue" "$ROOT/tests/adapter/adapter-continue.py" "True ~> .K"
run_case "adapter-function-return" "$ROOT/tests/adapter/adapter-function-return.py" "True ~> .K"
run_case "adapter-function-local" "$ROOT/tests/adapter/adapter-function-local.py" "True ~> .K"
run_case "adapter-function-fallthrough" "$ROOT/tests/adapter/adapter-function-fallthrough.py" "True ~> .K"
run_case "adapter-function-recursion" "$ROOT/tests/adapter/adapter-function-recursion.py" "True ~> .K"
run_case "adapter-function-zero-arg" "$ROOT/tests/adapter/adapter-function-zero-arg.py" "True ~> .K"
run_case "adapter-function-multi-arg" "$ROOT/tests/adapter/adapter-function-multi-arg.py" "True ~> .K"
run_case "adapter-function-arg-expressions" "$ROOT/tests/adapter/adapter-function-arg-expressions.py" "True ~> .K"
run_case "adapter-lambda-multi-arg" "$ROOT/tests/adapter/adapter-lambda-multi-arg.py" "True ~> .K"
run_case "adapter-for-list" "$ROOT/tests/adapter/adapter-for-list.py" "True ~> .K"
run_case "adapter-for-tuple" "$ROOT/tests/adapter/adapter-for-tuple.py" "True ~> .K"
run_case "adapter-for-break-continue" "$ROOT/tests/adapter/adapter-for-break-continue.py" "True ~> .K"
run_case "adapter-for-return" "$ROOT/tests/adapter/adapter-for-return.py" "True ~> .K"
run_case "adapter-for-unpack" "$ROOT/tests/adapter/adapter-for-unpack.py" "True ~> .K"
run_case "adapter-for-unpack-list-target" "$ROOT/tests/adapter/adapter-for-unpack-list-target.py" "True ~> .K"
run_case "adapter-for-unpack-break-continue" "$ROOT/tests/adapter/adapter-for-unpack-break-continue.py" "True ~> .K"
run_case "adapter-for-unpack-else" "$ROOT/tests/adapter/adapter-for-unpack-else.py" "True ~> .K"
run_case "adapter-for-else-normal" "$ROOT/tests/adapter/adapter-for-else-normal.py" "True ~> .K"
run_case "adapter-for-else-break" "$ROOT/tests/adapter/adapter-for-else-break.py" "True ~> .K"
run_case "adapter-for-else-continue" "$ROOT/tests/adapter/adapter-for-else-continue.py" "True ~> .K"
run_case "adapter-range-for" "$ROOT/tests/adapter/adapter-range-for.py" "True ~> .K"
run_case "adapter-range-start-stop" "$ROOT/tests/adapter/adapter-range-start-stop.py" "True ~> .K"
run_case "adapter-range-break-continue" "$ROOT/tests/adapter/adapter-range-break-continue.py" "True ~> .K"
run_case "adapter-range-step" "$ROOT/tests/adapter/adapter-range-step.py" "True ~> .K"
run_case "adapter-range-negative-step" "$ROOT/tests/adapter/adapter-range-negative-step.py" "True ~> .K"
run_case "adapter-range-step-else" "$ROOT/tests/adapter/adapter-range-step-else.py" "True ~> .K"
run_case "adapter-len-containers" "$ROOT/tests/adapter/adapter-len-containers.py" "True ~> .K"
run_case "adapter-len-string-range" "$ROOT/tests/adapter/adapter-len-string-range.py" "True ~> .K"
run_case "adapter-len-range-step" "$ROOT/tests/adapter/adapter-len-range-step.py" "True ~> .K"
run_case "adapter-dict" "$ROOT/tests/adapter/adapter-dict.py" "True ~> .K"
run_case "adapter-dict-truthy" "$ROOT/tests/adapter/adapter-dict-truthy.py" "True ~> .K"
run_case "adapter-dict-expressions" "$ROOT/tests/adapter/adapter-dict-expressions.py" "True ~> .K"
run_case "adapter-dict-duplicate-keys" "$ROOT/tests/adapter/adapter-dict-duplicate-keys.py" "True ~> .K"
run_case "adapter-dict-equality" "$ROOT/tests/adapter/adapter-dict-equality.py" "True ~> .K"
run_case "adapter-set" "$ROOT/tests/adapter/adapter-set.py" "True ~> .K"
run_case "adapter-set-expressions" "$ROOT/tests/adapter/adapter-set-expressions.py" "True ~> .K"
run_case "adapter-set-equality" "$ROOT/tests/adapter/adapter-set-equality.py" "True ~> .K"
run_case "adapter-set-ordering" "$ROOT/tests/adapter/adapter-set-ordering.py" "True ~> .K"
run_case "adapter-assign-many" "$ROOT/tests/adapter/adapter-assign-many.py" "True ~> .K"
run_case "adapter-unpack-tuple" "$ROOT/tests/adapter/adapter-unpack-tuple.py" "True ~> .K"
run_case "adapter-unpack-list" "$ROOT/tests/adapter/adapter-unpack-list.py" "True ~> .K"
run_case "adapter-unpack-expression-rhs" "$ROOT/tests/adapter/adapter-unpack-expression-rhs.py" "True ~> .K"
run_case "adapter-augmented-more" "$ROOT/tests/adapter/adapter-augmented-more.py" "True ~> .K"
