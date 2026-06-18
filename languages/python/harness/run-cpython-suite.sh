#!/usr/bin/env bash
set -euo pipefail

PYTHON_REF="${PYTHON_REF:-python3.14}"
CPYTHON_SOURCE="${CPYTHON_SOURCE:-}"

if ! command -v "$PYTHON_REF" >/dev/null 2>&1; then
  echo "Missing CPython reference executable: $PYTHON_REF" >&2
  echo "Set PYTHON_REF to a CPython 3.14.6 executable before running the suite." >&2
  exit 2
fi

if [ -z "$CPYTHON_SOURCE" ] || [ ! -d "$CPYTHON_SOURCE/Lib/test" ]; then
  echo "Missing CPython source checkout with Lib/test." >&2
  echo "Set CPYTHON_SOURCE to a checkout of https://github.com/python/cpython at tag v3.14.6." >&2
  exit 2
fi

echo "Reference implementation:"
"$PYTHON_REF" --version

echo "Running CPython reference suite only. K differential execution requires classified test adapters."
cd "$CPYTHON_SOURCE"
"$PYTHON_REF" -m test
