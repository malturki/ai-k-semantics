#!/usr/bin/env python3
"""Validate Python-specific source and CPython test ledgers."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE_MAP = ROOT / "languages/python/reference/source-map.json"
TEST_CLASSIFICATION = ROOT / "languages/python/tests/conformance/cpython-classification.json"
ADAPTER_SMOKE = ROOT / "languages/python/tests/conformance/adapter-smoke.json"
DIAGNOSTICS_PROFILE = ROOT / "languages/python/tests/conformance/cpython-diagnostics-profile.json"

ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")

SOURCE_STATUSES = {
    "not-started",
    "syntax",
    "partial",
    "profile",
    "complete",
}

TEST_CLASSES = {
    "candidate-language-semantics",
    "candidate-lexical",
    "candidate-parser-ast",
    "candidate-builtins",
    "candidate-object-model",
    "candidate-execution-model",
    "candidate-import-system",
    "stdlib-behavior",
    "cpython-implementation-detail",
    "platform-environment",
    "diagnostic-only",
    "environment-dependent",
    "non-goal",
    "unclassified",
}

REVIEW_STATUSES = {
    "seed",
    "reference-smoke-passed",
    "needs-split",
    "blocked",
    "excluded",
}

TRANSLATION_STATUSES = {
    "not-started",
    "needs-extraction",
    "adapter-needed",
    "ready",
    "excluded",
}

DIAGNOSTIC_NORMALIZATION_STATUSES = {
    "current",
    "future",
}


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as err:
        raise ValueError(f"{path}: invalid JSON: {err}") from err
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return data


def require_obj(data: dict[str, Any], key: str, path: Path) -> dict[str, Any]:
    value = data.get(key)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: '{key}' must be an object")
    return value


def require_list(data: dict[str, Any], key: str, path: Path) -> list[Any]:
    value = data.get(key)
    if not isinstance(value, list):
        raise ValueError(f"{path}: '{key}' must be a list")
    return value


def require_str(data: dict[str, Any], key: str, path: Path) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{path}: '{key}' must be a non-empty string")
    return value


def validate_id(value: Any, what: str, path: Path) -> str:
    if not isinstance(value, str) or not ID_RE.match(value):
        raise ValueError(f"{path}: {what} must match {ID_RE.pattern}")
    return value


def validate_source_map(path: Path) -> set[str]:
    data = load_json(path)
    language = require_obj(data, "language", path)
    if language.get("id") != "python":
        raise ValueError(f"{path}: language.id must be 'python'")
    require_str(language, "version", path)

    construct_ids: set[str] = set()
    family_ids: set[str] = set()
    families = require_list(data, "construct_families", path)
    if not families:
        raise ValueError(f"{path}: construct_families cannot be empty")

    for family in families:
        if not isinstance(family, dict):
            raise ValueError(f"{path}: construct_families entries must be objects")
        family_id = validate_id(family.get("id"), "family id", path)
        if family_id in family_ids:
            raise ValueError(f"{path}: duplicate family id '{family_id}'")
        family_ids.add(family_id)
        require_str(family, "title", path)
        status = require_str(family, "status", path)
        if status not in SOURCE_STATUSES:
            raise ValueError(f"{path}: family '{family_id}' has invalid status '{status}'")
        references = require_list(family, "references", path)
        if not references:
            raise ValueError(f"{path}: family '{family_id}' must have references")
        constructs = require_list(family, "constructs", path)
        if not constructs:
            raise ValueError(f"{path}: family '{family_id}' must list constructs")

        for construct in constructs:
            if not isinstance(construct, dict):
                raise ValueError(f"{path}: constructs in '{family_id}' must be objects")
            construct_id = validate_id(construct.get("id"), "construct id", path)
            if construct_id in construct_ids:
                raise ValueError(f"{path}: duplicate construct id '{construct_id}'")
            construct_ids.add(construct_id)
            require_str(construct, "title", path)
            status = require_str(construct, "status", path)
            if status not in SOURCE_STATUSES:
                raise ValueError(f"{path}: construct '{construct_id}' has invalid status '{status}'")
            require_list(construct, "references", path)
            require_list(construct, "k_coverage", path)
            require_list(construct, "test_coverage", path)
            require_list(construct, "gaps", path)

    return construct_ids


def validate_test_classification(path: Path, construct_ids: set[str]) -> None:
    data = load_json(path)
    suite = require_obj(data, "reference_suite", path)
    if suite.get("implementation") != "CPython":
        raise ValueError(f"{path}: reference_suite.implementation must be 'CPython'")
    require_str(suite, "version", path)

    tests = require_list(data, "tests", path)
    if not tests:
        raise ValueError(f"{path}: tests cannot be empty")

    seen: set[str] = set()
    for test in tests:
        if not isinstance(test, dict):
            raise ValueError(f"{path}: tests entries must be objects")
        test_id = validate_id(test.get("id"), "test id", path)
        if test_id in seen:
            raise ValueError(f"{path}: duplicate test id '{test_id}'")
        seen.add(test_id)
        source_path = require_str(test, "source_path", path)
        if not source_path.startswith("Lib/test/"):
            raise ValueError(f"{path}: {test_id}.source_path must be under Lib/test")
        test_class = require_str(test, "classification", path)
        if test_class not in TEST_CLASSES:
            raise ValueError(f"{path}: {test_id} has invalid classification '{test_class}'")
        review_status = require_str(test, "review_status", path)
        if review_status not in REVIEW_STATUSES:
            raise ValueError(f"{path}: {test_id} has invalid review_status '{review_status}'")
        translation_status = require_str(test, "translation_status", path)
        if translation_status not in TRANSLATION_STATUSES:
            raise ValueError(f"{path}: {test_id} has invalid translation_status '{translation_status}'")
        refs = require_list(test, "construct_refs", path)
        for ref in refs:
            if ref not in construct_ids:
                raise ValueError(f"{path}: {test_id} references unknown construct '{ref}'")
        require_list(test, "notes", path)
        require_list(test, "blockers", path)


def validate_adapter_smoke(path: Path) -> set[str]:
    data = load_json(path)
    if data.get("suite") != "python-adapter-smoke":
        raise ValueError(f"{path}: suite must be 'python-adapter-smoke'")
    cases = require_list(data, "cases", path)
    if not cases:
        raise ValueError(f"{path}: cases cannot be empty")

    seen: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            raise ValueError(f"{path}: cases entries must be objects")
        case_id = validate_id(case.get("id"), "adapter case id", path)
        if case_id in seen:
            raise ValueError(f"{path}: duplicate adapter case id '{case_id}'")
        seen.add(case_id)
        source = require_str(case, "source", path)
        source_path = path.parent / source
        if not source_path.resolve().is_file():
            raise ValueError(f"{path}: {case_id}.source does not exist: {source}")
        require_str(case, "reference", path)
        require_str(case, "expected_result", path)
        require_list(case, "coverage", path)

    return seen


def validate_diagnostics_profile(path: Path, adapter_case_ids: set[str]) -> None:
    data = load_json(path)
    profile = require_obj(data, "profile", path)
    if profile.get("id") != "cpython-diagnostics":
        raise ValueError(f"{path}: profile.id must be 'cpython-diagnostics'")
    require_str(profile, "language_version", path)
    require_str(profile, "source_tag", path)
    require_list(profile, "reference_sources", path)

    levels = require_list(data, "normalization_levels", path)
    if not levels:
        raise ValueError(f"{path}: normalization_levels cannot be empty")
    level_ids: set[str] = set()
    current_levels = 0
    for level in levels:
        if not isinstance(level, dict):
            raise ValueError(f"{path}: normalization_levels entries must be objects")
        level_id = validate_id(level.get("id"), "normalization level id", path)
        if level_id in level_ids:
            raise ValueError(f"{path}: duplicate normalization level id '{level_id}'")
        level_ids.add(level_id)
        status = require_str(level, "status", path)
        if status not in DIAGNOSTIC_NORMALIZATION_STATUSES:
            raise ValueError(f"{path}: normalization level '{level_id}' has invalid status '{status}'")
        if status == "current":
            current_levels += 1
        require_str(level, "description", path)
    if current_levels == 0:
        raise ValueError(f"{path}: at least one normalization level must be current")

    cases = require_list(data, "adapter_diagnostic_cases", path)
    if not cases:
        raise ValueError(f"{path}: adapter_diagnostic_cases cannot be empty")
    seen: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            raise ValueError(f"{path}: adapter_diagnostic_cases entries must be objects")
        case_id = validate_id(case.get("id"), "diagnostic adapter case id", path)
        if case_id in seen:
            raise ValueError(f"{path}: duplicate diagnostic adapter case id '{case_id}'")
        if case_id not in adapter_case_ids:
            raise ValueError(f"{path}: diagnostic adapter case '{case_id}' is not in adapter-smoke.json")
        seen.add(case_id)
        normalization = validate_id(case.get("normalization"), f"{case_id}.normalization", path)
        if normalization not in level_ids:
            raise ValueError(f"{path}: {case_id} references unknown normalization level '{normalization}'")
        exception_classes = require_list(case, "exception_classes", path)
        if not exception_classes:
            raise ValueError(f"{path}: {case_id}.exception_classes cannot be empty")
        for exc in exception_classes:
            if not isinstance(exc, str) or not exc.endswith("Error"):
                raise ValueError(f"{path}: {case_id}.exception_classes entries must be *Error class names")
        require_str(case, "notes", path)
    require_list(data, "known_gaps", path)


def main() -> int:
    construct_ids = validate_source_map(SOURCE_MAP)
    validate_test_classification(TEST_CLASSIFICATION, construct_ids)
    adapter_case_ids = validate_adapter_smoke(ADAPTER_SMOKE)
    validate_diagnostics_profile(DIAGNOSTICS_PROFILE, adapter_case_ids)
    print(
        "Validated Python source map, CPython test classification, adapter smoke manifest, "
        f"and diagnostics profile ({len(construct_ids)} construct ids, "
        f"{len(adapter_case_ids)} adapter cases)."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as err:
        print(f"error: {err}", file=sys.stderr)
        raise SystemExit(1)
