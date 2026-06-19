#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEF="$ROOT/semantics/python.k"
WORK="$ROOT/.build"
KOMPILED="$WORK/python-kompiled"

mkdir -p "$WORK"

kompile "$DEF" \
  --main-module PYTHON \
  --syntax-module PYTHON-SYNTAX \
  --output-definition "$KOMPILED"

run_case() {
  local name="$1"
  local source="$2"
  local expected="$3"
  local output="$WORK/$name.out"

  krun "$source" --definition "$KOMPILED" > "$output"

  if ! grep -q "^[[:space:]]*\\.K$" "$output"; then
    echo "FAIL $name: final <k> cell is not .K" >&2
    cat "$output" >&2
    exit 1
  fi

  if ! grep -q -- "$expected" "$output"; then
    echo "FAIL $name: expected result $expected" >&2
    cat "$output" >&2
    exit 1
  fi

  echo "PASS $name"
}

run_case "smoke-arithmetic" "$ROOT/tests/examples/smoke-arithmetic.py" "7 ~> .K"
run_case "smoke-assignment" "$ROOT/tests/examples/smoke-assignment.py" "10 ~> .K"
run_case "smoke-bool-constants" "$ROOT/tests/examples/smoke-bool-constants.py" "None ~> .K"
run_case "smoke-bool-ops" "$ROOT/tests/examples/smoke-bool-ops.py" "True ~> .K"
run_case "smoke-comparisons" "$ROOT/tests/examples/smoke-comparisons.py" "True ~> .K"
run_case "smoke-pass" "$ROOT/tests/examples/smoke-pass.py" "4 ~> .K"
run_case "smoke-strings" "$ROOT/tests/examples/smoke-strings.py" "True ~> .K"
run_case "smoke-conditional-expression" "$ROOT/tests/examples/smoke-conditional-expression.py" "2 ~> .K"
run_case "smoke-augmented-assignment" "$ROOT/tests/examples/smoke-augmented-assignment.py" "8 ~> .K"
run_case "smoke-augmented-true-div" "$ROOT/tests/examples/smoke-augmented-true-div.py" "True ~> .K"
run_case "smoke-del-name" "$ROOT/tests/examples/smoke-del-name.py" "2 ~> .K"
run_case "smoke-int-operators" "$ROOT/tests/examples/smoke-int-operators.py" "8 ~> .K"
run_case "smoke-lists" "$ROOT/tests/examples/smoke-lists.py" "1 ~> .K"
run_case "smoke-tuples" "$ROOT/tests/examples/smoke-tuples.py" "2 ~> .K"
run_case "smoke-lambda-call" "$ROOT/tests/examples/smoke-lambda-call.py" "6 ~> .K"
run_case "smoke-assert-global" "$ROOT/tests/examples/smoke-assert-global.py" "2 ~> .K"
