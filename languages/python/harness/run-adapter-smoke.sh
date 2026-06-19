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
run_case "adapter-list-normal" "$ROOT/tests/adapter/adapter-list-normal.py" "True ~> .K"
run_case "adapter-tuple-normal" "$ROOT/tests/adapter/adapter-tuple-normal.py" "True ~> .K"
run_case "adapter-lambda-normal" "$ROOT/tests/adapter/adapter-lambda-normal.py" "7 ~> .K"
run_case "adapter-if" "$ROOT/tests/adapter/adapter-if.py" "True ~> .K"
run_case "adapter-if-no-else" "$ROOT/tests/adapter/adapter-if-no-else.py" "True ~> .K"
run_case "adapter-while" "$ROOT/tests/adapter/adapter-while.py" "True ~> .K"
run_case "adapter-nested-if-while" "$ROOT/tests/adapter/adapter-nested-if-while.py" "True ~> .K"
