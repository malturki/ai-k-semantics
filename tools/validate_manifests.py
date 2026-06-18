#!/usr/bin/env python3
"""Validate language manifests without external dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ROOT / "languages"
VALID_STATUSES = {
    "planned",
    "experimental",
    "reference-testing",
    "proof-testing",
    "maintained",
}
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as err:
        raise ValueError(f"{path}: invalid JSON: {err}") from err
    if not isinstance(data, dict):
        raise ValueError(f"{path}: manifest must be a JSON object")
    return data


def require(data: dict[str, Any], path: str, manifest: Path) -> Any:
    current: Any = data
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            raise ValueError(f"{manifest}: missing required field '{path}'")
        current = current[part]
    return current


def validate_manifest(path: Path) -> list[str]:
    data = load_json(path)

    language_id = require(data, "id", path)
    if not isinstance(language_id, str) or not ID_RE.match(language_id):
        raise ValueError(f"{path}: id must match {ID_RE.pattern}")

    name = require(data, "name", path)
    if not isinstance(name, str) or not name.strip():
        raise ValueError(f"{path}: name must be a non-empty string")

    status = require(data, "status", path)
    if status not in VALID_STATUSES:
        raise ValueError(f"{path}: status must be one of {sorted(VALID_STATUSES)}")

    for field in (
        "sources.specifications",
        "sources.reference_implementations",
        "sources.test_suites",
        "semantics.backends",
        "known_gaps",
    ):
        value = require(data, field, path)
        if not isinstance(value, list):
            raise ValueError(f"{path}: {field} must be a list")

    for field in (
        "semantics.main_definition",
        "semantics.main_module",
        "semantics.syntax_module",
        "tests.conformance_manifest",
        "tests.proof_manifest",
    ):
        require(data, field, path)

    warnings: list[str] = []
    if language_id != "template" and status != "planned":
        specs = data["sources"]["specifications"]
        refs = data["sources"]["reference_implementations"]
        suites = data["sources"]["test_suites"]
        if not specs:
            warnings.append(f"{path}: non-planned language has no specifications")
        if not refs:
            warnings.append(f"{path}: non-planned language has no reference implementations")
        if not suites:
            warnings.append(f"{path}: non-planned language has no test suites")

    return warnings


def main() -> int:
    manifests = sorted(LANGUAGES.glob("*/manifest.json"))
    if not manifests:
        print("No language manifests found.", file=sys.stderr)
        return 1

    warnings: list[str] = []
    for manifest in manifests:
        warnings.extend(validate_manifest(manifest))

    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)

    print(f"Validated {len(manifests)} language manifest(s).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as err:
        print(f"error: {err}", file=sys.stderr)
        raise SystemExit(1)
