#!/usr/bin/env python3
"""Translate a supported Python AST subset to concrete K parser input.

This is a construct-preserving bridge for early differential tests. It parses
real Python source with the reference interpreter's ``ast`` module and emits the
small semicolon-terminated syntax currently accepted by ``semantics/python.k``.
Unsupported nodes are rejected instead of being desugared silently.
"""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path
from typing import TypeGuard


class UnsupportedPythonSubset(ValueError):
    """Raised when the current K semantics has no faithful target construct."""


ELLIPSIS_NAME_ID = "kEllipsisName"
DUNDER_INIT_NAME_ID = "kDunderInitName"
DUNDER_NAME_NAME_ID = "kDunderNameName"
DUNDER_DOC_NAME_ID = "kDunderDocName"
DUNDER_MODULE_NAME_ID = "kDunderModuleName"
DUNDER_QUALNAME_NAME_ID = "kDunderQualnameName"
DUNDER_ALL_NAME_ID = "kDunderAllName"
DUNDER_VALUE_NAME_ID = "kDunderValueName"
DUNDER_TYPE_PARAMS_NAME_ID = "kDunderTypeParamsName"
DUNDER_PARAMETERS_NAME_ID = "kDunderParametersName"
NO_RELATIVE_MODULE_ID = "kNoRelativeModuleName"
JSON_SURROGATE_PAIR_RE = re.compile(r"\\u(d[89ab][0-9a-f]{2})\\u(d[cdef][0-9a-f]{2})")
SUPPORTED_ZERO_ARG_CLASS_PATTERNS = {
    "bytearray",
    "bool",
    "bytes",
    "complex",
    "dict",
    "float",
    "frozenset",
    "int",
    "list",
    "range",
    "set",
    "slice",
    "str",
    "tuple",
}
SUPPORTED_SINGLE_ARG_CLASS_PATTERNS = {
    "bytearray",
    "bool",
    "bytes",
    "dict",
    "float",
    "frozenset",
    "int",
    "list",
    "set",
    "str",
    "tuple",
}
CLASS_PATTERN_ID_ALIASES = {
    "frozenset": "kFrozenSetClassName",
    "set": "kSetClassName",
}
SUPPORTED_GETATTR_NAMES = {
    "__doc__",
    "__module__",
    "__name__",
    "__parameters__",
    "__qualname__",
    "__type_params__",
    "__value__",
    "denominator",
    "imag",
    "missing",
    "numerator",
    "real",
    "start",
    "step",
    "stop",
}
SUPPORTED_BUILTIN_CLASS_NAMES = {
    "bytearray",
    "bool",
    "bytes",
    "complex",
    "dict",
    "float",
    "frozenset",
    "int",
    "list",
    "memoryview",
    "range",
    "set",
    "slice",
    "str",
    "tuple",
}
SUPPORTED_IMPORT_MODULES = {
    "builtins",
    "importlib",
    "keyword",
    "math",
}
SET_MUTATING_METHOD_NAMES = {
    "add",
    "clear",
    "discard",
    "difference_update",
    "intersection_update",
    "pop",
    "remove",
    "symmetric_difference_update",
    "update",
}
METHOD_CALL0_NAMES = {
    "capitalize",
    "clear",
    "copy",
    "decode",
    "expandtabs",
    "hex",
    "isalnum",
    "isalpha",
    "isascii",
    "isdigit",
    "islower",
    "isspace",
    "istitle",
    "isupper",
    "lower",
    "lstrip",
    "pop",
    "popitem",
    "reverse",
    "rsplit",
    "rstrip",
    "sort",
    "split",
    "splitlines",
    "strip",
    "swapcase",
    "title",
    "update",
    "upper",
} | SET_MUTATING_METHOD_NAMES
METHOD_CALL1_NAMES = {
    "append",
    "center",
    "count",
    "decode",
    "endswith",
    "expandtabs",
    "extend",
    "find",
    "get",
    "hex",
    "index",
    "join",
    "ljust",
    "lstrip",
    "partition",
    "pop",
    "remove",
    "removeprefix",
    "removesuffix",
    "rfind",
    "rindex",
    "rjust",
    "rpartition",
    "rsplit",
    "rstrip",
    "setdefault",
    "sort",
    "split",
    "splitlines",
    "startswith",
    "strip",
    "translate",
    "update",
    "zfill",
} | SET_MUTATING_METHOD_NAMES
METHOD_CALL2_NAMES = {
    "center",
    "count",
    "decode",
    "endswith",
    "find",
    "get",
    "hex",
    "index",
    "insert",
    "ljust",
    "pop",
    "replace",
    "rfind",
    "rindex",
    "rjust",
    "rsplit",
    "setdefault",
    "split",
    "startswith",
    "translate",
} | SET_MUTATING_METHOD_NAMES
METHOD_CALL3_NAMES = {
    "count",
    "endswith",
    "find",
    "index",
    "replace",
    "rfind",
    "rindex",
    "startswith",
} | SET_MUTATING_METHOD_NAMES
SUPPORTED_FORMAT_SPECS = {
    "",
    "b",
    "c",
    "d",
    "o",
    "x",
    "X",
    "#b",
    "#d",
    "#o",
    "#x",
    "#X",
    "+b",
    "+c",
    "+d",
    "+o",
    "+x",
    "+X",
    " b",
    " c",
    " d",
    " o",
    " x",
    " X",
    "-b",
    "-c",
    "-d",
    "-o",
    "-x",
    "-X",
    "+#b",
    "+#d",
    "+#o",
    "+#x",
    "+#X",
    " #b",
    " #d",
    " #o",
    " #x",
    " #X",
    "-#b",
    "-#d",
    "-#o",
    "-#x",
    "-#X",
}
FORMAT_ALIGN_CHARS = "<>=^"
FORMAT_SIGN_CHARS = "+- "
FORMAT_INT_TYPE_CHARS = "bcdoxX"
FORMAT_STRING_TYPE_CHARS = "s"
FORMAT_NUMERIC_TYPE_CHARS = "bcdoxXeEfFgGn%"
FORMAT_FLOAT_SPECIAL_TYPE_CHARS = "eEfFgGn%"


def format_align_index(spec: str) -> int:
    if len(spec) >= 2 and spec[1] in FORMAT_ALIGN_CHARS:
        return 1
    if len(spec) >= 1 and spec[0] in FORMAT_ALIGN_CHARS:
        return 0
    return -1


def parse_supported_format_spec(spec: str, type_chars: str) -> tuple[int, bool, bool, str, str] | None:
    if any(ord(ch) >= 128 for ch in spec):
        return None
    align_index = format_align_index(spec)
    index = align_index + 1 if align_index >= 0 else 0
    has_sign = index < len(spec) and spec[index] in FORMAT_SIGN_CHARS
    if has_sign:
        index += 1
    has_alt = index < len(spec) and spec[index] == "#"
    if has_alt:
        index += 1
    if index < len(spec) and spec[index] == "0":
        index += 1
    end = len(spec)
    if index < len(spec) and spec[-1] in type_chars:
        end -= 1
    grouping = ""
    if end > index and spec[end - 1] in ",_":
        grouping = spec[end - 1]
        end -= 1
    if end < index:
        return None
    width = spec[index:end]
    if width and not width.isdecimal():
        return None
    return align_index, has_sign, has_alt, grouping, width


def parse_supported_int_precision_format_spec(spec: str) -> tuple[bool, str, str] | None:
    if any(ord(ch) >= 128 for ch in spec):
        return None
    align_index = format_align_index(spec)
    index = align_index + 1 if align_index >= 0 else 0
    if index < len(spec) and spec[index] in FORMAT_SIGN_CHARS:
        index += 1
    if index < len(spec) and spec[index] == "#":
        index += 1
    if index < len(spec) and spec[index] == "0":
        index += 1
    end = len(spec)
    if index < len(spec) and spec[-1] in FORMAT_INT_TYPE_CHARS:
        end -= 1
    grouping = ""
    if end > index and spec[end - 1] in ",_":
        grouping = spec[end - 1]
        end -= 1
    body = spec[index:end]
    if "." not in body:
        return None
    width, precision = body.split(".", 1)
    precision_missing = precision == ""
    if precision_missing and grouping:
        return None
    if width and not width.isdecimal():
        return None
    if precision and not precision.isdecimal():
        return None
    return precision_missing, grouping, width


def parse_supported_z_format_spec(
    spec: str, type_chars: str, *, allow_precision: bool
) -> tuple[int, bool, bool, str] | None:
    if any(ord(ch) >= 128 for ch in spec):
        return None
    align_index = format_align_index(spec)
    index = align_index + 1 if align_index >= 0 else 0
    if index < len(spec) and spec[index] in FORMAT_SIGN_CHARS:
        index += 1
    if index >= len(spec) or spec[index] != "z":
        return None
    index += 1
    has_alt = index < len(spec) and spec[index] == "#"
    if has_alt:
        index += 1
    if index < len(spec) and spec[index] == "0":
        index += 1
    end = len(spec)
    if index < len(spec) and spec[-1] in type_chars:
        end -= 1
    grouping = ""
    if end > index and spec[end - 1] in ",_":
        grouping = spec[end - 1]
        end -= 1
    body = spec[index:end]
    if "." in body:
        if not allow_precision:
            return None
        width, precision = body.split(".", 1)
        if precision == "" or not precision.isdecimal():
            return None
    else:
        width = body
    if width and not width.isdecimal():
        return None
    return align_index, has_alt, grouping != "", width


def parse_supported_typed_format_spec(
    spec: str, type_chars: str, *, allow_grouping: bool
) -> tuple[int, bool, bool, bool, bool, bool, bool] | None:
    if any(ord(ch) >= 128 for ch in spec):
        return None
    align_index = format_align_index(spec)
    index = align_index + 1 if align_index >= 0 else 0
    has_sign = index < len(spec) and spec[index] in FORMAT_SIGN_CHARS
    if has_sign:
        index += 1
    has_z = index < len(spec) and spec[index] == "z"
    if has_z:
        index += 1
    has_alt = index < len(spec) and spec[index] == "#"
    if has_alt:
        index += 1
    if index < len(spec) and spec[index] == "0":
        index += 1
    if index >= len(spec) or spec[-1] not in type_chars:
        return None
    end = len(spec) - 1
    has_grouping = end > index and spec[end - 1] in ",_"
    if has_grouping:
        if not allow_grouping:
            return None
        end -= 1
    body = spec[index:end]
    has_precision = "." in body
    precision_missing = False
    if has_precision:
        width, precision = body.split(".", 1)
        precision_missing = precision == ""
        if precision and not precision.isdecimal():
            return None
    else:
        width = body
    if width and not width.isdecimal():
        return None
    return align_index, has_sign, has_z, has_alt, has_grouping, has_precision, precision_missing


def parse_supported_float_special_format_spec(spec: str) -> tuple[str, bool, bool] | None:
    if any(ord(ch) >= 128 for ch in spec):
        return None
    align_index = format_align_index(spec)
    index = align_index + 1 if align_index >= 0 else 0
    if index < len(spec) and spec[index] in FORMAT_SIGN_CHARS:
        index += 1
    if index < len(spec) and spec[index] == "z":
        index += 1
    if index < len(spec) and spec[index] == "#":
        index += 1
    if index < len(spec) and spec[index] == "0":
        index += 1
    end = len(spec)
    type_char = ""
    if index < len(spec) and spec[-1] in FORMAT_NUMERIC_TYPE_CHARS:
        if spec[-1] not in FORMAT_FLOAT_SPECIAL_TYPE_CHARS:
            return None
        type_char = spec[-1]
        end -= 1
    body = spec[index:end]
    has_width_grouping = False
    has_precision_grouping = False
    precision_missing = False
    if "." in body:
        width, precision = body.split(".", 1)
        has_width_grouping = bool(width) and width[-1] in ",_"
        if has_width_grouping:
            width = width[:-1]
        has_precision_grouping = bool(precision) and precision[-1] in ",_"
        if has_precision_grouping:
            precision = precision[:-1]
        precision_missing = precision == "" and not has_precision_grouping
        if width and not width.isdecimal():
            return None
        if precision and not precision.isdecimal():
            return None
    else:
        width = body
        has_width_grouping = bool(width) and width[-1] in ",_"
        if has_width_grouping:
            width = width[:-1]
    if width and not width.isdecimal():
        return None
    return type_char, has_width_grouping or has_precision_grouping, precision_missing


def parse_supported_string_format_spec(spec: str) -> tuple[int, bool, bool, bool, str] | None:
    if any(ord(ch) >= 128 for ch in spec):
        return None
    align_index = format_align_index(spec)
    index = align_index + 1 if align_index >= 0 else 0
    has_sign = index < len(spec) and spec[index] in FORMAT_SIGN_CHARS
    if has_sign:
        index += 1
    has_alt = index < len(spec) and spec[index] == "#"
    if has_alt:
        index += 1
    if index < len(spec) and spec[index] == "0":
        index += 1
    end = len(spec)
    if index < len(spec) and spec[-1] in FORMAT_STRING_TYPE_CHARS:
        end -= 1
    body = spec[index:end]
    if "," in body or "_" in body:
        return None
    precision_missing = False
    if "." in body:
        width, precision = body.split(".", 1)
        precision_missing = precision == ""
        if precision and not precision.isdecimal():
            return None
    else:
        width = body
    if width and not width.isdecimal():
        return None
    return align_index, has_sign, has_alt, precision_missing, width


def format_int_spec_supported(spec: str) -> bool:
    if spec in SUPPORTED_FORMAT_SPECS:
        return True
    if not spec:
        return False
    return parse_supported_format_spec(spec, FORMAT_INT_TYPE_CHARS) is not None


def format_int_precision_spec_supported(spec: str) -> bool:
    return parse_supported_int_precision_format_spec(spec) is not None


def format_int_z_spec_supported(spec: str) -> bool:
    parsed = parse_supported_z_format_spec(spec, FORMAT_INT_TYPE_CHARS, allow_precision=False)
    if parsed is None:
        return False
    _align_index, _has_alt, has_grouping, _width = parsed
    if not has_grouping:
        return True
    return spec.endswith(",d") or (
        "_" in spec and not spec.endswith("_c")
    )


def format_int_string_type_spec_supported(spec: str) -> bool:
    parsed = parse_supported_typed_format_spec(
        spec, FORMAT_STRING_TYPE_CHARS, allow_grouping=False
    )
    if parsed is None:
        return False
    *_rest, _has_precision, precision_missing = parsed
    return not precision_missing


def format_int_n_diagnostic_spec_supported(spec: str) -> bool:
    parsed = parse_supported_typed_format_spec(spec, "n", allow_grouping=True)
    if parsed is None:
        return False
    (
        _align_index,
        _has_sign,
        has_z,
        _has_alt,
        has_grouping,
        has_precision,
        _precision_missing,
    ) = parsed
    return has_z or has_grouping or has_precision


def format_string_spec_supported(spec: str) -> bool:
    if spec == "":
        return True
    parsed = parse_supported_string_format_spec(spec)
    if parsed is None:
        return False
    align_index, has_sign, has_alt, precision_missing, _width = parsed
    if has_sign or has_alt or precision_missing:
        return False
    return align_index < 0 or spec[align_index] != "="


def format_string_precision_missing_supported(spec: str) -> bool:
    parsed = parse_supported_string_format_spec(spec)
    if parsed is None:
        return False
    align_index, has_sign, has_alt, precision_missing, _width = parsed
    if has_sign or has_alt or not precision_missing:
        return False
    return align_index < 0 or spec[align_index] != "="


def format_string_diagnostic_spec_supported(spec: str) -> bool:
    parsed = parse_supported_string_format_spec(spec)
    if parsed is None:
        return False
    align_index, has_sign, has_alt, precision_missing, _width = parsed
    if precision_missing:
        return False
    has_equal_align = align_index >= 0 and spec[align_index] == "="
    return has_sign or has_alt or has_equal_align


def format_string_z_spec_supported(spec: str) -> bool:
    parsed = parse_supported_z_format_spec(spec, FORMAT_STRING_TYPE_CHARS, allow_precision=True)
    if parsed is None:
        return False
    align_index, has_alt, has_grouping, _width = parsed
    if has_alt or has_grouping:
        return False
    return align_index < 0 or spec[align_index] != "="


def format_string_numeric_type_spec_supported(spec: str) -> bool:
    parsed = parse_supported_typed_format_spec(
        spec, FORMAT_NUMERIC_TYPE_CHARS, allow_grouping=True
    )
    if parsed is None:
        return False
    align_index, has_sign, has_z, has_alt, _has_grouping, _has_precision, precision_missing = parsed
    if has_sign or has_z or has_alt or precision_missing:
        return False
    return align_index < 0 or spec[align_index] != "="


def format_float_special_spec_supported(spec: str) -> bool:
    if spec == "":
        return False
    parsed = parse_supported_float_special_format_spec(spec)
    if parsed is None:
        return False
    type_char, has_grouping, precision_missing = parsed
    return not precision_missing and not (has_grouping and type_char == "n")


def format_float_n_grouping_diagnostic_spec_supported(spec: str) -> bool:
    parsed = parse_supported_float_special_format_spec(spec)
    if parsed is None:
        return False
    type_char, has_grouping, precision_missing = parsed
    return not precision_missing and has_grouping and type_char == "n"


def format_float_precision_missing_spec_supported(spec: str) -> bool:
    parsed = parse_supported_float_special_format_spec(spec)
    if parsed is None:
        return False
    _type_char, _has_grouping, precision_missing = parsed
    return precision_missing


def format_spec_supported(spec: str) -> bool:
    return (
        format_int_spec_supported(spec)
        or format_int_precision_spec_supported(spec)
        or format_int_z_spec_supported(spec)
        or format_int_string_type_spec_supported(spec)
        or format_int_n_diagnostic_spec_supported(spec)
        or format_string_spec_supported(spec)
        or format_string_diagnostic_spec_supported(spec)
        or format_string_z_spec_supported(spec)
        or format_string_numeric_type_spec_supported(spec)
        or format_float_special_spec_supported(spec)
        or format_float_n_grouping_diagnostic_spec_supported(spec)
        or format_float_precision_missing_spec_supported(spec)
        or format_string_precision_missing_supported(spec)
    )


def emit_id(name: str) -> str:
    if name == "Ellipsis":
        return ELLIPSIS_NAME_ID
    if name == "__init__":
        return DUNDER_INIT_NAME_ID
    if name == "__name__":
        return DUNDER_NAME_NAME_ID
    if name == "__doc__":
        return DUNDER_DOC_NAME_ID
    if name == "__module__":
        return DUNDER_MODULE_NAME_ID
    if name == "__qualname__":
        return DUNDER_QUALNAME_NAME_ID
    if name == "__all__":
        return DUNDER_ALL_NAME_ID
    if name == "__value__":
        return DUNDER_VALUE_NAME_ID
    if name == "__type_params__":
        return DUNDER_TYPE_PARAMS_NAME_ID
    if name == "__parameters__":
        return DUNDER_PARAMETERS_NAME_ID
    return name


def unsupported(node: ast.AST, message: str) -> UnsupportedPythonSubset:
    location = ""
    lineno = getattr(node, "lineno", None)
    col = getattr(node, "col_offset", None)
    if lineno is not None and col is not None:
        location = f" at line {lineno}, column {col}"
    return UnsupportedPythonSubset(f"{message}{location}: {node.__class__.__name__}")


def emit_min_max_keyword_call(
    node: ast.AST, builtin_name: str, args: list[ast.expr], keywords: list[ast.keyword]
) -> str:
    if len(keywords) == 2:
        first, second = keywords
        if first.arg == "default" and second.arg == "key":
            if len(args) == 1:
                return (
                    f"#{builtin_name}DefaultKey("
                    f"{emit_exp(args[0])}, {emit_exp(first.value)}, {emit_exp(second.value)})"
                )
            return (
                f"#{builtin_name}ArgsDefaultKey("
                f"{emit_arg_exps(args)}, {emit_exp(first.value)}, {emit_exp(second.value)})"
            )
        if first.arg == "key" and second.arg == "default":
            if len(args) == 1:
                return (
                    f"#{builtin_name}KeyDefault("
                    f"{emit_exp(args[0])}, {emit_exp(first.value)}, {emit_exp(second.value)})"
                )
            return (
                f"#{builtin_name}ArgsKeyDefault("
                f"{emit_arg_exps(args)}, {emit_exp(first.value)}, {emit_exp(second.value)})"
            )
        raise unsupported(
            node,
            f"{builtin_name} currently supports combined default= and key= keywords only",
        )
    if len(keywords) != 1:
        raise unsupported(
            node,
            f"{builtin_name} currently supports at most default= and key= keyword pairs",
        )
    keyword = keywords[0]
    if keyword.arg == "default":
        if len(args) == 1:
            return f"#{builtin_name}Default({emit_exp(args[0])}, {emit_exp(keyword.value)})"
        return f"#{builtin_name}ArgsDefault({emit_arg_exps(args)}, {emit_exp(keyword.value)})"
    if keyword.arg == "key":
        if len(args) == 1:
            return f"#{builtin_name}Key({emit_exp(args[0])}, {emit_exp(keyword.value)})"
        return f"#{builtin_name}ArgsKey({emit_arg_exps(args)}, {emit_exp(keyword.value)})"
    raise unsupported(
        node,
        f"{builtin_name} currently supports only default= or key=, not **kwargs or other keywords",
    )


def emit_sorted_keyword_call(node: ast.AST, arg: ast.expr, keywords: list[ast.keyword]) -> str:
    if len(keywords) == 2:
        first, second = keywords
        if first.arg == "key" and second.arg == "reverse":
            return (
                f"#sortedKeyReverse("
                f"{emit_exp(arg)}, {emit_exp(first.value)}, {emit_exp(second.value)})"
            )
        if first.arg == "reverse" and second.arg == "key":
            return (
                f"#sortedReverseKey("
                f"{emit_exp(arg)}, {emit_exp(first.value)}, {emit_exp(second.value)})"
            )
        raise unsupported(node, "sorted currently supports combined key= and reverse= keywords only")
    if len(keywords) != 1:
        raise unsupported(node, "sorted currently supports at most key= and reverse= keyword pairs")
    keyword = keywords[0]
    if keyword.arg == "key":
        return f"#sortedKey({emit_exp(arg)}, {emit_exp(keyword.value)})"
    if keyword.arg == "reverse":
        return f"#sortedReverse({emit_exp(arg)}, {emit_exp(keyword.value)})"
    raise unsupported(node, "sorted currently supports only key= or reverse=, not **kwargs or other keywords")


def emit_list_sort_keyword_call(node: ast.AST, name: str, keywords: list[ast.keyword]) -> str:
    emitted_name = emit_id(name)
    if len(keywords) == 2:
        first, second = keywords
        if first.arg == "key" and second.arg == "reverse":
            return (
                f"#listSortKeyReverse("
                f"{emitted_name}, {emit_exp(first.value)}, {emit_exp(second.value)})"
            )
        if first.arg == "reverse" and second.arg == "key":
            return (
                f"#listSortReverseKey("
                f"{emitted_name}, {emit_exp(first.value)}, {emit_exp(second.value)})"
            )
        raise unsupported(node, "list.sort currently supports combined key= and reverse= keywords only")
    if len(keywords) != 1:
        raise unsupported(node, "list.sort currently supports at most key= and reverse= keyword pairs")
    keyword = keywords[0]
    if keyword.arg == "key":
        return f"#listSortKey({emitted_name}, {emit_exp(keyword.value)})"
    if keyword.arg == "reverse":
        return f"#listSortReverse({emitted_name}, {emit_exp(keyword.value)})"
    raise unsupported(node, "list.sort currently supports only key= or reverse=, not **kwargs or other keywords")


def emit_module(module: ast.Module) -> str:
    return emit_stmt_list(module.body) + "\n"


def emit_interactive_input(module: ast.Interactive) -> str:
    return emit_stmt_list(module.body) + "\n"


def emit_stmt_list(stmts: list[ast.stmt]) -> str:
    return "\n".join(f"{emit_stmt(stmt)};" for stmt in stmts)


def emit_block(stmts: list[ast.stmt]) -> str:
    if not stmts:
        return "{}"
    return "{\n" + emit_stmt_list(stmts) + "\n}"


def emit_stmt_block(stmt: str) -> str:
    return "{\n" + stmt + ";\n}"


def emit_exception_expr(exp: ast.expr) -> str:
    match exp:
        case ast.Name(id=name):
            return f"#exception({emit_id(name)})"
        case ast.Call(func=ast.Name(id=name), args=args, keywords=[]):
            return f"#exceptionCall({emit_id(name)}, {emit_arg_exps(args)})"
        case ast.Call(func=ast.Name(), keywords=keywords) if keywords:
            raise unsupported(exp, "exception constructor calls with keyword arguments are not supported")
    raise unsupported(exp, "only named exception classes and named exception constructor calls are supported")


def emit_import_stmt(stmt: ast.Import, names: list[ast.alias]) -> str:
    emitted: list[str] = []
    for alias in names:
        if "." in alias.name:
            path = emit_string(alias.name)
            if alias.asname is None:
                emitted.append(f"#importDotted({path})")
            else:
                emitted.append(f"#importDottedAs({path}, {emit_id(alias.asname)})")
            continue
        if alias.name not in SUPPORTED_IMPORT_MODULES:
            raise unsupported(stmt, "only supported builtin-module imports are accepted")
        module = emit_id(alias.name)
        if alias.asname is None:
            emitted.append(f"#import({module})")
        else:
            emitted.append(f"#importAs({module}, {emit_id(alias.asname)})")
    return ";\n".join(emitted)


def emit_import_from_stmt(stmt: ast.ImportFrom, module: str | None, names: list[ast.alias], level: int) -> str:
    if level != 0:
        dotted_module = module is not None and "." in module
        module_name = emit_string(module) if dotted_module and module is not None else (
            NO_RELATIVE_MODULE_ID if module is None else emit_id(module)
        )
        emitted: list[str] = []
        for alias in names:
            if alias.name == "*":
                if dotted_module:
                    emitted.append(f"#fromRelativeDottedImportStar({level}, {module_name})")
                else:
                    emitted.append(f"#fromRelativeImportStar({level}, {module_name})")
                continue
            imported = emit_id(alias.name)
            if dotted_module and alias.asname is None:
                emitted.append(f"#fromRelativeDottedImport({level}, {module_name}, {imported})")
            elif dotted_module:
                emitted.append(
                    f"#fromRelativeDottedImportAs({level}, {module_name}, {imported}, {emit_id(alias.asname)})"
                )
            elif alias.asname is None:
                emitted.append(f"#fromRelativeImport({level}, {module_name}, {imported})")
            else:
                emitted.append(f"#fromRelativeImportAs({level}, {module_name}, {imported}, {emit_id(alias.asname)})")
        return ";\n".join(emitted)
    if module is None:
        raise unsupported(stmt, "absolute from-import statements require a module name")
    if "." in module:
        module_path = emit_string(module)
        if len(names) == 1 and names[0].name == "*":
            return f"#fromDottedImportStar({module_path})"
        emitted: list[str] = []
        for alias in names:
            if alias.name == "*":
                raise unsupported(stmt, "from-import star cannot be combined with named imports")
            imported = emit_id(alias.name)
            if alias.asname is None:
                emitted.append(f"#fromDottedImport({module_path}, {imported})")
            else:
                emitted.append(f"#fromDottedImportAs({module_path}, {imported}, {emit_id(alias.asname)})")
        return ";\n".join(emitted)
    if module not in SUPPORTED_IMPORT_MODULES:
        raise unsupported(stmt, "only supported builtin-module from-import statements are accepted")
    module_id = emit_id(module)
    if len(names) == 1 and names[0].name == "*":
        return f"#fromImportStar({module_id})"
    emitted: list[str] = []
    for alias in names:
        if alias.name == "*":
            raise unsupported(stmt, "from-import star cannot be combined with named imports")
        imported = emit_id(alias.name)
        if alias.asname is None:
            emitted.append(f"#fromImport({module_id}, {imported})")
        else:
            emitted.append(f"#fromImportAs({module_id}, {imported}, {emit_id(alias.asname)})")
    return ";\n".join(emitted)


def emit_stmt(stmt: ast.stmt) -> str:
    match stmt:
        case ast.Expr(value=value):
            return emit_exp(value)
        case ast.Pass():
            return "pass"
        case ast.Break():
            return "break"
        case ast.Continue():
            return "continue"
        case ast.Assert(test=test, msg=None):
            return f"assert {emit_exp(test)}"
        case ast.Assert(test=test, msg=msg):
            return f"#assertMsg({emit_exp(test)}, {emit_exp(msg)})"
        case ast.Global(names=[name]):
            return f"global {emit_id(name)}"
        case ast.Global(names=names):
            return f"#globalMany({emit_id_items(names)})"
        case ast.Delete(targets=[ast.Name(id=name)]):
            return f"del {emit_id(name)}"
        case ast.Delete(targets=targets):
            return emit_delete(stmt, targets)
        case ast.Assign(targets=targets, value=value):
            return emit_assign(stmt, targets, value)
        case ast.AnnAssign(target=target, value=value):
            return emit_ann_assign(stmt, target, value)
        case ast.TypeAlias(name=name, type_params=type_params, value=value):
            return emit_type_alias(stmt, name, type_params, value)
        case ast.AugAssign(target=ast.Name(id=name), op=op, value=value):
            if isinstance(op, ast.FloorDiv):
                return f"#floorDivAssign({emit_id(name)}, {emit_exp(value)})"
            return f"{emit_id(name)} {emit_aug_op(op)}= {emit_exp(value)}"
        case ast.AugAssign(
            target=ast.Subscript(value=ast.Name(id=name), slice=slice_, ctx=ast.Store()),
            op=op,
            value=value,
        ) if not isinstance(slice_, ast.Slice):
            return (
                f"#subscriptAug({emit_id(name)}, {emit_exp(slice_)}, "
                f"{emit_aug_op_tag(op)}, {emit_exp(value)})"
            )
        case ast.AugAssign():
            raise unsupported(stmt, "only simple-name and simple-name subscript augmented assignment targets are supported")
        case ast.Return(value=None):
            return "return"
        case ast.Return(value=value):
            return f"return {emit_exp(value)}"
        case ast.Raise(exc=None, cause=None):
            return "raise"
        case ast.Raise(exc=exc, cause=ast.Constant(value=None)) if exc is not None:
            return f"#raiseFromNone({emit_exception_expr(exc)})"
        case ast.Raise(exc=exc, cause=cause) if exc is not None and cause is not None:
            return f"#raiseFrom({emit_exception_expr(exc)}, {emit_exception_expr(cause)})"
        case ast.Raise(exc=exc, cause=None) if exc is not None:
            return f"raise {emit_exception_expr(exc)}"
        case ast.Raise():
            raise unsupported(stmt, "only bare re-raise or raising a named exception class/call, optionally from None or another named class/call, is supported")
        case ast.Import(names=names):
            return emit_import_stmt(stmt, names)
        case ast.ImportFrom(module=module, names=names, level=level):
            return emit_import_from_stmt(stmt, module, names, level)
        case ast.FunctionDef(
            name=name,
            args=args,
            body=body,
            decorator_list=decorators,
            returns=returns,
            type_comment=type_comment,
        ):
            return emit_function_def(stmt, name, args, body, decorators, returns, type_comment)
        case ast.AsyncFunctionDef(
            name=name,
            args=args,
            body=body,
            decorator_list=decorators,
            returns=returns,
            type_comment=type_comment,
        ):
            return emit_async_function_def(stmt, name, args, body, decorators, returns, type_comment)
        case ast.ClassDef(
            name=name,
            bases=bases,
            keywords=keywords,
            body=body,
            decorator_list=decorators,
        ):
            return emit_simple_class_def(stmt, name, bases, keywords, body, decorators)
        case ast.If(test=test, body=body, orelse=orelse):
            return f"#if({emit_exp(test)}, {emit_block(body)}, {emit_block(orelse)})"
        case ast.While(test=test, body=body, orelse=[]):
            return f"#while({emit_exp(test)}, {emit_block(body)})"
        case ast.While(test=test, body=body, orelse=orelse):
            return f"#whileElse({emit_exp(test)}, {emit_block(body)}, {emit_block(orelse)})"
        case ast.For(target=target, iter=iter_, body=body, orelse=orelse):
            return emit_for_stmt(stmt, target, iter_, body, orelse)
        case ast.With(items=items, body=body, type_comment=None):
            return emit_with_stmt(stmt, items, body)
        case ast.Match(subject=subject, cases=cases):
            return f"#match({emit_exp(subject)}, {emit_match_cases(stmt, cases)})"
        case ast.Try(body=body, handlers=handlers, orelse=orelse, finalbody=finalbody) if handlers and finalbody:
            return f"#tryFinally({emit_stmt_block(emit_try_except(stmt, body, handlers, orelse))}, {emit_block(finalbody)})"
        case ast.Try(body=body, handlers=handlers, orelse=orelse, finalbody=[]) if handlers:
            return emit_try_except(stmt, body, handlers, orelse)
        case ast.Try(body=body, handlers=[], orelse=[], finalbody=finalbody):
            return f"#tryFinally({emit_block(body)}, {emit_block(finalbody)})"
        case ast.Try():
            raise unsupported(
                stmt,
                "only supported try/except/finally sentinel subsets are accepted",
            )
        case _:
            raise unsupported(stmt, "statement is not supported by the current K subset")


def emit_exp(exp: ast.expr) -> str:
    match exp:
        case ast.Constant(value=value):
            return emit_constant(exp, value)
        case ast.JoinedStr(values=values):
            return f"#fstring({emit_fstring_parts(exp, values)})"
        case ast.Name(id="__debug__"):
            return "#debug"
        case ast.Name(id="Ellipsis"):
            return f"#name({ELLIPSIS_NAME_ID})"
        case ast.Name(id=name):
            return emit_id(name)
        case ast.NamedExpr(target=ast.Name(id=name), value=value):
            return f"#namedExpr({emit_id(name)}, {emit_exp(value)})"
        case ast.NamedExpr():
            raise unsupported(exp, "only simple-name assignment expression targets are supported yet")
        case ast.BinOp(left=left, op=op, right=right):
            return emit_bin_op(left, op, right)
        case ast.UnaryOp(op=op, operand=operand):
            return emit_unary_op(op, operand)
        case ast.BoolOp(op=op, values=values):
            return emit_bool_op(exp, op, values)
        case ast.Compare(left=left, ops=[op], comparators=[right]):
            return f"({emit_exp(left)} {emit_cmp_op(op)} {emit_exp(right)})"
        case ast.Compare(left=left, ops=ops, comparators=comparators):
            return f"#compareChain({emit_exp(left)}, {emit_cmp_chain(ops, comparators)})"
        case ast.IfExp(test=test, body=body, orelse=orelse):
            return f"({emit_exp(body)} if {emit_exp(test)} else {emit_exp(orelse)})"
        case ast.Lambda(args=args, body=body):
            return emit_lambda(exp, args, body)
        case ast.Call(func=ast.Name(id="range"), args=[stop], keywords=[]):
            return f"#range({emit_exp(stop)})"
        case ast.Call(func=ast.Name(id="range"), args=[start, stop], keywords=[]):
            return f"#range({emit_exp(start)}, {emit_exp(stop)})"
        case ast.Call(func=ast.Name(id="range"), args=[start, stop, step], keywords=[]):
            return f"#range({emit_exp(start)}, {emit_exp(stop)}, {emit_exp(step)})"
        case ast.Call(func=ast.Name(id="enumerate"), args=[arg], keywords=[]):
            return f"#enumerate({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="enumerate"), args=[arg, start], keywords=[]):
            return f"#enumerate({emit_exp(arg)}, {emit_exp(start)})"
        case ast.Call(func=ast.Name(id="enumerate"), args=[arg], keywords=[ast.keyword(arg="start", value=start)]):
            return f"#enumerate({emit_exp(arg)}, {emit_exp(start)})"
        case ast.Call(func=ast.Name(id="zip"), args=args, keywords=[]):
            return f"#zip({emit_arg_exps(args)})"
        case ast.Call(func=ast.Name(id="zip"), args=args, keywords=[ast.keyword(arg="strict", value=strict)]):
            return f"#zipStrict({emit_arg_exps(args)}, {emit_exp(strict)})"
        case ast.Call(func=ast.Name(id="reversed"), args=[arg], keywords=[]):
            return f"#reversed({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="map"), args=args, keywords=[]):
            return f"#map({emit_arg_exps(args)})"
        case ast.Call(func=ast.Name(id="map"), args=args, keywords=[ast.keyword(arg="strict", value=strict)]):
            return f"#mapStrict({emit_arg_exps(args)}, {emit_exp(strict)})"
        case ast.Call(func=ast.Name(id="map"), keywords=keywords) if keywords:
            raise unsupported(exp, "map currently supports only the strict= keyword")
        case ast.Call(func=ast.Name(id="filter"), args=args, keywords=[]):
            return f"#filter({emit_arg_exps(args)})"
        case ast.Call(func=ast.Name(id="filter"), keywords=keywords) if keywords:
            raise unsupported(exp, "filter is positional-only in the current builtin profile")
        case ast.Call(func=ast.Name(id="iter"), args=args, keywords=[]):
            return f"#iter({emit_arg_exps(args)})"
        case ast.Call(func=ast.Name(id="iter"), keywords=keywords) if keywords:
            raise unsupported(exp, "iter is positional-only in the current builtin profile")
        case ast.Call(func=ast.Name(id="next"), args=args, keywords=[]):
            return f"#next({emit_arg_exps(args)})"
        case ast.Call(func=ast.Name(id="next"), keywords=keywords) if keywords:
            raise unsupported(exp, "next is positional-only in the current builtin profile")
        case ast.Call(func=ast.Name(id="slice"), args=[stop], keywords=[]):
            return f"#sliceCtor({emit_exp(stop)})"
        case ast.Call(func=ast.Name(id="slice"), args=[start, stop], keywords=[]):
            return f"#sliceCtor({emit_exp(start)}, {emit_exp(stop)})"
        case ast.Call(func=ast.Name(id="slice"), args=[start, stop, step], keywords=[]):
            return f"#sliceCtor({emit_exp(start)}, {emit_exp(stop)}, {emit_exp(step)})"
        case ast.Call(func=ast.Name(id="len"), args=[arg], keywords=[]):
            return f"#len({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="list"), args=[], keywords=[]):
            return "#listCtor()"
        case ast.Call(func=ast.Name(id="list"), args=[arg], keywords=[]):
            return f"#listCtor({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="tuple"), args=[], keywords=[]):
            return "#tupleCtor()"
        case ast.Call(func=ast.Name(id="tuple"), args=[arg], keywords=[]):
            return f"#tupleCtor({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="sorted"), args=[arg], keywords=[]):
            return f"#sorted({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="sorted"), args=[arg], keywords=keywords) if keywords:
            return emit_sorted_keyword_call(exp, arg, keywords)
        case ast.Call(func=ast.Name(id="dict"), args=[], keywords=[]):
            return "#dictCtor()"
        case ast.Call(func=ast.Name(id="dict"), args=[arg], keywords=[]):
            return f"#dictCtor({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="dict"), args=[], keywords=keywords) if keywords:
            return emit_dict_ctor_keywords(exp, None, keywords)
        case ast.Call(func=ast.Name(id="dict"), args=[arg], keywords=keywords) if keywords:
            return emit_dict_ctor_keywords(exp, arg, keywords)
        case ast.Call(func=ast.Name(id="dict"), keywords=keywords) if keywords:
            raise unsupported(exp, "dict constructor supports at most one positional argument")
        case ast.Call(func=ast.Name(id="set"), args=[], keywords=[]):
            return "#setCtor()"
        case ast.Call(func=ast.Name(id="set"), args=[arg], keywords=[]):
            return f"#setCtor({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="frozenset"), args=[], keywords=[]):
            return "#frozensetCtor()"
        case ast.Call(func=ast.Name(id="frozenset"), args=[arg], keywords=[]):
            return f"#frozensetCtor({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="bytes"), args=[], keywords=[]):
            return "#bytesCtor()"
        case ast.Call(func=ast.Name(id="bytes"), args=[arg], keywords=[]):
            return f"#bytesCtor({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="bytes"), args=[source, encoding], keywords=[]):
            return f"#bytesCtor({emit_exp(source)}, {emit_exp(encoding)})"
        case ast.Call(func=ast.Name(id="bytes"), args=[source, encoding, errors], keywords=[]):
            return f"#bytesCtor({emit_exp(source)}, {emit_exp(encoding)}, {emit_exp(errors)})"
        case ast.Call(
            func=ast.Attribute(value=ast.Name(id="bytes"), attr="fromhex", ctx=ast.Load()),
            args=[arg],
            keywords=[],
        ):
            return f"#bytesFromHex({emit_exp(arg)})"
        case ast.Call(
            func=ast.Attribute(value=ast.Name(id="bytes"), attr="maketrans", ctx=ast.Load()),
            args=[from_arg, to_arg],
            keywords=[],
        ):
            return f"#bytesMakeTrans({emit_exp(from_arg)}, {emit_exp(to_arg)})"
        case ast.Call(func=ast.Name(id="bytearray"), args=[], keywords=[]):
            return "#bytearrayCtor()"
        case ast.Call(func=ast.Name(id="bytearray"), args=[arg], keywords=[]):
            return f"#bytearrayCtor({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="bytearray"), args=[source, encoding], keywords=[]):
            return f"#bytearrayCtor({emit_exp(source)}, {emit_exp(encoding)})"
        case ast.Call(func=ast.Name(id="bytearray"), args=[source, encoding, errors], keywords=[]):
            return f"#bytearrayCtor({emit_exp(source)}, {emit_exp(encoding)}, {emit_exp(errors)})"
        case ast.Call(
            func=ast.Attribute(value=ast.Name(id="bytearray"), attr="fromhex", ctx=ast.Load()),
            args=[arg],
            keywords=[],
        ):
            return f"#bytearrayFromHex({emit_exp(arg)})"
        case ast.Call(
            func=ast.Attribute(value=ast.Name(id="bytearray"), attr="maketrans", ctx=ast.Load()),
            args=[from_arg, to_arg],
            keywords=[],
        ):
            return f"#bytearrayMakeTrans({emit_exp(from_arg)}, {emit_exp(to_arg)})"
        case ast.Call(func=ast.Name(id="memoryview"), args=[arg], keywords=[]):
            return f"#memoryview({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="bool"), args=[], keywords=[]):
            return "#boolCtor()"
        case ast.Call(func=ast.Name(id="bool"), args=[arg], keywords=[]):
            return f"#boolCtor({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="str"), args=[], keywords=[]):
            return "#strCtor()"
        case ast.Call(func=ast.Name(id="str"), args=[arg], keywords=[]):
            return f"#strCtor({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="repr"), args=[arg], keywords=[]):
            return f"#repr({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="ascii"), args=[arg], keywords=[]):
            return f"#ascii({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="format"), args=[value], keywords=[]):
            return f"#format({emit_exp(value)})"
        case ast.Call(func=ast.Name(id="format"), args=[value, spec], keywords=[]):
            emitted_spec = emit_format_spec(exp, spec)
            if emitted_spec is not None:
                return f"#format({emit_exp(value)}, {emitted_spec})"
            return f"#format({emit_exp(value)}, {emit_exp(spec)})"
        case ast.Call(func=ast.Name(id="chr"), args=[arg], keywords=[]):
            return f"#chr({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="ord"), args=[arg], keywords=[]):
            return f"#ord({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="bin"), args=[arg], keywords=[]):
            return f"#bin({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="oct"), args=[arg], keywords=[]):
            return f"#oct({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="hex"), args=[arg], keywords=[]):
            return f"#hex({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="hash"), args=[arg], keywords=[]):
            return f"#hash({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="callable"), args=[arg], keywords=[]):
            return f"#callable({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="isinstance"), args=[obj, classinfo], keywords=[]):
            if isinstance(classinfo, ast.Name) and classinfo.id not in SUPPORTED_BUILTIN_CLASS_NAMES:
                return f"#isinstanceDynamic({emit_exp(obj)}, {emit_exp(classinfo)})"
            emitted_classinfo, is_tuple = emit_builtin_classinfo(exp, classinfo)
            if is_tuple:
                return f"#isinstanceAny({emit_exp(obj)}, {emitted_classinfo})"
            return f"#isinstance({emit_exp(obj)}, {emitted_classinfo})"
        case ast.Call(func=ast.Name(id="issubclass"), args=[cls, classinfo], keywords=[]):
            if (
                isinstance(cls, ast.Name)
                and isinstance(classinfo, ast.Name)
                and cls.id not in SUPPORTED_BUILTIN_CLASS_NAMES
                and classinfo.id not in SUPPORTED_BUILTIN_CLASS_NAMES
            ):
                return f"#issubclassDynamic({emit_exp(cls)}, {emit_exp(classinfo)})"
            emitted_class = emit_builtin_class_name(exp, cls, "issubclass first argument")
            emitted_classinfo, is_tuple = emit_builtin_classinfo(exp, classinfo)
            if is_tuple:
                return f"#issubclassAny({emitted_class}, {emitted_classinfo})"
            return f"#issubclass({emitted_class}, {emitted_classinfo})"
        case ast.Call(func=ast.Name(id="getattr"), args=[obj, name], keywords=[]):
            emitted_name = emit_getattr_name(name)
            if emitted_name is not None:
                return f"#getattr({emit_exp(obj)}, {emitted_name})"
            return f"#getattrDyn({emit_exp(obj)}, {emit_exp(name)})"
        case ast.Call(func=ast.Name(id="getattr"), args=[obj, name, default], keywords=[]):
            emitted_name = emit_getattr_name(name)
            if emitted_name is not None:
                return (
                    f"#getattrDefault({emit_exp(obj)}, "
                    f"{emitted_name}, {emit_exp(default)})"
                )
            return f"#getattrDefaultDyn({emit_exp(obj)}, {emit_exp(name)}, {emit_exp(default)})"
        case ast.Call(func=ast.Name(id="hasattr"), args=[obj, name], keywords=[]):
            emitted_name = emit_getattr_name(name)
            if emitted_name is not None:
                return f"#hasattr({emit_exp(obj)}, {emitted_name})"
            return f"#hasattrDyn({emit_exp(obj)}, {emit_exp(name)})"
        case ast.Call(func=ast.Name(id="setattr"), args=[obj, name, value], keywords=[]):
            return f"#setattr({emit_exp(obj)}, {emit_exp(name)}, {emit_exp(value)})"
        case ast.Call(func=ast.Name(id="delattr"), args=[obj, name], keywords=[]):
            return f"#delattr({emit_exp(obj)}, {emit_exp(name)})"
        case ast.Call(
            func=ast.Attribute(value=ast.Name(id="object"), attr="__setattr__", ctx=ast.Load()),
            args=[obj, name, value],
            keywords=[],
        ):
            return f"#objectSetattr({emit_exp(obj)}, {emit_exp(name)}, {emit_exp(value)})"
        case ast.Call(
            func=ast.Attribute(value=ast.Name(id="object"), attr="__getattribute__", ctx=ast.Load()),
            args=[obj, name],
            keywords=[],
        ):
            return f"#objectGetattribute({emit_exp(obj)}, {emit_exp(name)})"
        case ast.Call(
            func=ast.Attribute(value=ast.Name(id="object"), attr="__delattr__", ctx=ast.Load()),
            args=[obj, name],
            keywords=[],
        ):
            return f"#objectDelattr({emit_exp(obj)}, {emit_exp(name)})"
        case ast.Call(func=ast.Name(id="all"), args=[arg], keywords=[]):
            return f"#all({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="any"), args=[arg], keywords=[]):
            return f"#any({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="sum"), args=[arg], keywords=[]):
            return f"#sum({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="sum"), args=[arg, start], keywords=[]):
            return f"#sum({emit_exp(arg)}, {emit_exp(start)})"
        case ast.Call(func=ast.Name(id="min"), args=[arg], keywords=[]):
            return f"#min({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="min"), args=[arg], keywords=keywords) if keywords:
            return emit_min_max_keyword_call(exp, "min", [arg], keywords)
        case ast.Call(func=ast.Name(id="min"), args=args, keywords=[]) if len(args) >= 2:
            return f"#minArgs({emit_arg_exps(args)})"
        case ast.Call(func=ast.Name(id="min"), args=args, keywords=keywords) if len(args) >= 2 and keywords:
            return emit_min_max_keyword_call(exp, "min", args, keywords)
        case ast.Call(func=ast.Name(id="max"), args=[arg], keywords=[]):
            return f"#max({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="max"), args=[arg], keywords=keywords) if keywords:
            return emit_min_max_keyword_call(exp, "max", [arg], keywords)
        case ast.Call(func=ast.Name(id="max"), args=args, keywords=[]) if len(args) >= 2:
            return f"#maxArgs({emit_arg_exps(args)})"
        case ast.Call(func=ast.Name(id="max"), args=args, keywords=keywords) if len(args) >= 2 and keywords:
            return emit_min_max_keyword_call(exp, "max", args, keywords)
        case ast.Call(func=ast.Name(id="int"), args=[], keywords=[]):
            return "#intCtor()"
        case ast.Call(func=ast.Name(id="int"), args=[arg], keywords=[]):
            return f"#intCtor({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="int"), args=[arg, base], keywords=[]):
            return f"#intCtor({emit_exp(arg)}, {emit_exp(base)})"
        case ast.Call(func=ast.Name(id="float"), args=[], keywords=[]):
            return "#floatCtor()"
        case ast.Call(func=ast.Name(id="float"), args=[arg], keywords=[]):
            return f"#floatCtor({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="complex"), args=[], keywords=[]):
            return "#complexCtor()"
        case ast.Call(func=ast.Name(id="complex"), args=[arg], keywords=[]):
            return f"#complexCtor({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="complex"), args=[real, imag], keywords=[]):
            return f"#complexCtor({emit_exp(real)}, {emit_exp(imag)})"
        case ast.Call(func=ast.Name(id="complex"), args=[], keywords=keywords) if keywords:
            return emit_complex_ctor_keywords(exp, None, keywords)
        case ast.Call(func=ast.Name(id="complex"), args=[arg], keywords=keywords) if keywords:
            return emit_complex_ctor_keywords(exp, arg, keywords)
        case ast.Call(func=ast.Name(id="complex"), keywords=keywords) if keywords:
            raise unsupported(exp, "complex constructor supports at most one positional argument with keywords")
        case ast.Call(
            func=ast.Attribute(value=ast.Name(id="dict"), attr="fromkeys", ctx=ast.Load()),
            args=[iterable],
            keywords=[],
        ):
            return f"#dictFromKeys({emit_exp(iterable)})"
        case ast.Call(
            func=ast.Attribute(value=ast.Name(id="dict"), attr="fromkeys", ctx=ast.Load()),
            args=[iterable, value],
            keywords=[],
        ):
            return f"#dictFromKeys({emit_exp(iterable)}, {emit_exp(value)})"
        case ast.Call(func=ast.Attribute(value=value, attr="conjugate", ctx=ast.Load()), args=[], keywords=[]):
            return f"#conjugate({emit_exp(value)})"
        case ast.Call(
            func=ast.Attribute(value=ast.Name(id=name), attr="sort", ctx=ast.Load()),
            args=[],
            keywords=keywords,
        ) if keywords:
            return emit_list_sort_keyword_call(exp, name, keywords)
        case ast.Call(
            func=ast.Attribute(value=ast.Name(id=name), attr=attr, ctx=ast.Load()),
            args=[],
            keywords=[],
        ) if attr in METHOD_CALL0_NAMES:
            return f"#methodCall0({emit_id(name)}, {emit_id(attr)})"
        case ast.Call(
            func=ast.Attribute(value=ast.Name(id=name), attr=attr, ctx=ast.Load()),
            args=[arg],
            keywords=[],
        ) if attr in METHOD_CALL1_NAMES:
            return f"#methodCall({emit_id(name)}, {emit_id(attr)}, {emit_exp(arg)})"
        case ast.Call(
            func=ast.Attribute(value=ast.Name(id=name), attr=attr, ctx=ast.Load()),
            args=[arg1, arg2],
            keywords=[],
        ) if attr in METHOD_CALL2_NAMES:
            return f"#methodCall2({emit_id(name)}, {emit_id(attr)}, {emit_exp(arg1)}, {emit_exp(arg2)})"
        case ast.Call(
            func=ast.Attribute(value=ast.Name(id=name), attr="translate", ctx=ast.Load()),
            args=[table],
            keywords=[ast.keyword(arg="delete", value=delete)],
        ):
            return f"#methodCall2({emit_id(name)}, {emit_id('translate')}, {emit_exp(table)}, {emit_exp(delete)})"
        case ast.Call(
            func=ast.Attribute(value=ast.Name(id=name), attr=attr, ctx=ast.Load()),
            args=[arg1, arg2, arg3],
            keywords=[],
        ) if attr in METHOD_CALL3_NAMES:
            return f"#methodCall3({emit_id(name)}, {emit_id(attr)}, {emit_exp(arg1)}, {emit_exp(arg2)}, {emit_exp(arg3)})"
        case ast.Call(func=ast.Name(id="abs"), args=[arg], keywords=[]):
            return f"#abs({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="divmod"), args=[left, right], keywords=[]):
            return f"#divmod({emit_exp(left)}, {emit_exp(right)})"
        case ast.Call(func=ast.Name(id="pow"), args=[base, exponent], keywords=[]):
            return f"#pow({emit_exp(base)}, {emit_exp(exponent)})"
        case ast.Call(func=ast.Name(id="pow"), args=[base, exponent, modulus], keywords=[]):
            return f"#pow({emit_exp(base)}, {emit_exp(exponent)}, {emit_exp(modulus)})"
        case ast.Call(func=ast.Name(id="round"), args=[number], keywords=[]):
            return f"#round({emit_exp(number)})"
        case ast.Call(func=ast.Name(id="round"), args=[number, ndigits], keywords=[]):
            return f"#round({emit_exp(number)}, {emit_exp(ndigits)})"
        case ast.Call(func=func, args=[], keywords=keywords) if keywords:
            return f"#callKw({emit_exp(func)}, {emit_kw_arg_exps(exp, keywords)})"
        case ast.Call(func=func, args=args, keywords=keywords) if args and keywords:
            return f"#callMixed({emit_exp(func)}, {emit_arg_exps(args)}, {emit_kw_arg_exps(exp, keywords)})"
        case ast.Call(keywords=keywords) if keywords:
            raise unsupported(exp, "unsupported keyword call shape")
        case ast.Call(func=func, args=[arg], keywords=[]):
            return f"({emit_exp(func)}({emit_exp(arg)}))"
        case ast.Call(func=func, args=args, keywords=[]):
            return f"#call({emit_exp(func)}, {emit_arg_exps(args)})"
        case ast.Attribute(value=value, attr=attr, ctx=ast.Load()):
            return f"#attr({emit_exp(value)}, {emit_id(attr)})"
        case ast.ListComp(elt=elt, generators=[generator]):
            return emit_list_comprehension(exp, elt, generator)
        case ast.ListComp(elt=elt, generators=[outer, inner]):
            return emit_list_comprehension_two_generators(exp, elt, outer, inner)
        case ast.ListComp(elt=elt, generators=[outer, middle, inner]):
            return emit_list_comprehension_three_generators(exp, elt, outer, middle, inner)
        case ast.ListComp(elt=elt, generators=generators):
            return emit_list_comprehension_many(exp, elt, generators)
        case ast.DictComp(key=key, value=value, generators=[generator]):
            return emit_dict_comprehension(exp, key, value, generator)
        case ast.DictComp(key=key, value=value, generators=[outer, inner]):
            return emit_dict_comprehension_two_generators(exp, key, value, outer, inner)
        case ast.DictComp(key=key, value=value, generators=[outer, middle, inner]):
            return emit_dict_comprehension_three_generators(exp, key, value, outer, middle, inner)
        case ast.DictComp(key=key, value=value, generators=generators):
            return emit_dict_comprehension_many(exp, key, value, generators)
        case ast.SetComp(elt=elt, generators=[generator]):
            return emit_set_comprehension(exp, elt, generator)
        case ast.SetComp(elt=elt, generators=[outer, inner]):
            return emit_set_comprehension_two_generators(exp, elt, outer, inner)
        case ast.SetComp(elt=elt, generators=[outer, middle, inner]):
            return emit_set_comprehension_three_generators(exp, elt, outer, middle, inner)
        case ast.SetComp(elt=elt, generators=generators):
            return emit_set_comprehension_many(exp, elt, generators)
        case ast.GeneratorExp(elt=elt, generators=generators):
            return emit_generator_expression(exp, elt, generators)
        case ast.List(elts=elts, ctx=ast.Load()):
            return emit_list(elts)
        case ast.Tuple(elts=elts, ctx=ast.Load()):
            return emit_tuple(elts)
        case ast.Dict(keys=keys, values=values):
            return emit_dict(exp, keys, values)
        case ast.Set(elts=elts):
            return emit_set(elts)
        case ast.Subscript(value=value, slice=ast.Slice(lower=lower, upper=upper, step=None), ctx=ast.Load()):
            return f"#slice({emit_exp(value)}, {emit_slice_bound(lower)}, {emit_slice_bound(upper)})"
        case ast.Subscript(value=value, slice=ast.Slice(lower=lower, upper=upper, step=step), ctx=ast.Load()):
            return f"#sliceStep({emit_exp(value)}, {emit_slice_bound(lower)}, {emit_slice_bound(upper)}, {emit_exp(step)})"
        case ast.Subscript(value=value, slice=slice_, ctx=ast.Load()):
            return f"({emit_exp(value)}[{emit_exp(slice_)}])"
        case _:
            raise unsupported(exp, "expression is not supported by the current K subset")


def emit_constant(node: ast.AST, value: object) -> str:
    if value is True:
        return "True"
    if value is False:
        return "False"
    if value is None:
        return "None"
    if value is Ellipsis:
        return "Ellipsis"
    if isinstance(value, complex):
        return emit_complex(value)
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return repr(value)
    if isinstance(value, str):
        return emit_string(value)
    if isinstance(value, bytes):
        return emit_bytes(value)
    raise unsupported(node, f"constant {value!r} is not supported")


def emit_string(value: str) -> str:
    return JSON_SURROGATE_PAIR_RE.sub(emit_surrogate_pair, json.dumps(value))


def emit_surrogate_pair(match: re.Match[str]) -> str:
    high = int(match.group(1), 16)
    low = int(match.group(2), 16)
    code_point = 0x10000 + ((high - 0xD800) << 10) + (low - 0xDC00)
    return f"\\U{code_point:08x}"


def emit_fstring_parts(node: ast.AST, values: list[ast.expr]) -> str:
    if not values:
        return "#fstrEnd"
    value = values[0]
    rest = emit_fstring_parts(node, values[1:])
    match value:
        case ast.Constant(value=text) if isinstance(text, str):
            return f"#fstrText({emit_string(text)}, {rest})"
        case ast.FormattedValue(value=formatted, conversion=-1, format_spec=None):
            return f"#fstrExp({emit_exp(formatted)}, {rest})"
        case ast.FormattedValue(value=formatted, conversion=conversion, format_spec=None):
            emitted_conversion = emit_fstring_conversion(value, conversion)
            return f"#fstrExpConv({emit_exp(formatted)}, {emitted_conversion}, {rest})"
        case ast.FormattedValue(value=formatted, conversion=-1, format_spec=format_spec) if is_empty_fstring_format_spec(format_spec):
            return f"#fstrExpFormatEmpty({emit_exp(formatted)}, {rest})"
        case ast.FormattedValue(value=formatted, conversion=conversion, format_spec=format_spec) if is_empty_fstring_format_spec(format_spec):
            emitted_conversion = emit_fstring_conversion(value, conversion)
            return f"#fstrExpConvFormatEmpty({emit_exp(formatted)}, {emitted_conversion}, {rest})"
        case ast.FormattedValue(value=formatted, conversion=-1, format_spec=format_spec) if fstring_literal_format_spec_supported(format_spec):
            emitted_spec = emit_string(fstring_literal_format_spec_value(format_spec))
            return f"#fstrExpFormat({emit_exp(formatted)}, {emitted_spec}, {rest})"
        case ast.FormattedValue(value=formatted, conversion=conversion, format_spec=format_spec) if fstring_literal_format_spec_supported(format_spec):
            emitted_conversion = emit_fstring_conversion(value, conversion)
            emitted_spec = emit_string(fstring_literal_format_spec_value(format_spec))
            return f"#fstrExpConvFormat({emit_exp(formatted)}, {emitted_conversion}, {emitted_spec}, {rest})"
        case ast.FormattedValue(value=formatted, conversion=-1, format_spec=format_spec) if fstring_dynamic_format_spec(format_spec):
            emitted_spec_parts = emit_fstring_parts(format_spec, format_spec.values)
            return f"#fstrExpFormatParts({emit_exp(formatted)}, {emitted_spec_parts}, {rest})"
        case ast.FormattedValue(value=formatted, conversion=conversion, format_spec=format_spec) if fstring_dynamic_format_spec(format_spec):
            emitted_conversion = emit_fstring_conversion(value, conversion)
            emitted_spec_parts = emit_fstring_parts(format_spec, format_spec.values)
            return f"#fstrExpConvFormatParts({emit_exp(formatted)}, {emitted_conversion}, {emitted_spec_parts}, {rest})"
        case ast.FormattedValue(format_spec=format_spec) if format_spec is not None:
            raise unsupported(value, "f-string format specifications are not supported yet")
        case ast.FormattedValue():
            raise unsupported(value, "unsupported f-string formatted value shape")
    raise unsupported(node, "only literal text and formatted expressions are supported in f-strings")


def is_empty_fstring_format_spec(format_spec: ast.expr | None) -> bool:
    return isinstance(format_spec, ast.JoinedStr) and not format_spec.values


def fstring_literal_format_spec_value(format_spec: ast.expr | None) -> str:
    if not isinstance(format_spec, ast.JoinedStr):
        raise AssertionError("expected JoinedStr format_spec")
    parts: list[str] = []
    for value in format_spec.values:
        if not isinstance(value, ast.Constant) or not isinstance(value.value, str):
            raise AssertionError("expected literal string format_spec part")
        parts.append(value.value)
    return "".join(parts)


def fstring_literal_format_spec_supported(format_spec: ast.expr | None) -> bool:
    if not isinstance(format_spec, ast.JoinedStr) or not format_spec.values:
        return False
    for value in format_spec.values:
        if not isinstance(value, ast.Constant) or not isinstance(value.value, str):
            return False
    return format_spec_supported(fstring_literal_format_spec_value(format_spec))


def fstring_dynamic_format_spec(format_spec: ast.expr | None) -> TypeGuard[ast.JoinedStr]:
    if not isinstance(format_spec, ast.JoinedStr):
        return False
    return any(
        not isinstance(value, ast.Constant) or not isinstance(value.value, str)
        for value in format_spec.values
    )


def emit_fstring_conversion(node: ast.AST, conversion: int) -> str:
    if conversion == ord("s"):
        return "#fstrConvStr"
    if conversion == ord("r"):
        return "#fstrConvRepr"
    if conversion == ord("a"):
        return "#fstrConvAscii"
    raise unsupported(node, "f-strings currently support only !s, !r, and !a conversions")


def emit_complex(value: complex) -> str:
    return f"#complex({repr(value.real)}, {repr(value.imag)})"


def emit_bytes(value: bytes) -> str:
    if not value:
        return "#bytes()"
    return "#bytes(" + ", ".join(str(byte) for byte in value) + ",)"


def emit_bin_op(left: ast.expr, op: ast.operator, right: ast.expr) -> str:
    left_text = emit_exp(left)
    right_text = emit_exp(right)
    if isinstance(op, ast.FloorDiv):
        return f"#floorDiv({left_text}, {right_text})"
    if isinstance(op, ast.Div):
        return f"#trueDiv({left_text}, {right_text})"
    return f"({left_text} {emit_binary_op(op)} {right_text})"


def emit_unary_op(op: ast.unaryop, operand: ast.expr) -> str:
    if isinstance(op, ast.UAdd):
        return f"(+ {emit_exp(operand)})"
    if isinstance(op, ast.USub):
        return f"(- {emit_exp(operand)})"
    if isinstance(op, ast.Invert):
        return f"(~ {emit_exp(operand)})"
    if isinstance(op, ast.Not):
        return f"(not {emit_exp(operand)})"
    raise unsupported(op, "unary operator is not supported")


def emit_bool_op(node: ast.AST, op: ast.boolop, values: list[ast.expr]) -> str:
    if len(values) < 2:
        raise unsupported(node, "boolean operation needs at least two values")
    symbol = "and" if isinstance(op, ast.And) else "or" if isinstance(op, ast.Or) else None
    if symbol is None:
        raise unsupported(op, "boolean operator is not supported")
    result = emit_exp(values[0])
    for value in values[1:]:
        result = f"({result} {symbol} {emit_exp(value)})"
    return result


def emit_comp_filters(filters: list[ast.expr]) -> str:
    if not filters:
        raise ValueError("comprehension filter list must be nonempty")
    if len(filters) == 1:
        return f"#filter({emit_exp(filters[0])})"
    return f"#filters({emit_exp(filters[0])}, {emit_comp_filters(filters[1:])})"


def emit_maybe_comp_filters(filters: list[ast.expr]) -> str:
    if not filters:
        return "#noFilters"
    return emit_comp_filters(filters)


def emit_try_except(
    node: ast.AST,
    body: list[ast.stmt],
    handlers: list[ast.ExceptHandler],
    orelse: list[ast.stmt],
) -> str:
    if len(handlers) == 1 and handlers[0].name is None and isinstance(handlers[0].type, ast.Name):
        handler = handlers[0]
        emitted_body = emit_block(body)
        emitted_exception = emit_id(handler.type.id)
        emitted_handler = emit_block(handler.body)
        if orelse:
            return f"#tryExceptElse({emitted_body}, {emitted_exception}, {emitted_handler}, {emit_block(orelse)})"
        return f"#tryExcept({emitted_body}, {emitted_exception}, {emitted_handler})"

    emitted_body = emit_block(body)
    emitted_handlers = emit_except_handlers(node, handlers)
    if orelse:
        return f"#tryExceptCasesElse({emitted_body}, {emitted_handlers}, {emit_block(orelse)})"
    return f"#tryExceptCases({emitted_body}, {emitted_handlers})"


def emit_match_cases(node: ast.AST, cases: list[ast.match_case]) -> str:
    if not cases:
        raise unsupported(node, "match statements require at least one case")
    case = cases[0]
    emitted_pattern = emit_match_pattern(node, case.pattern)
    emitted_guard = emit_exp(case.guard) if case.guard is not None else None
    emitted_body = emit_block(case.body)
    if len(cases) == 1:
        if emitted_guard is not None:
            return f"#matchCaseGuard({emitted_pattern}, {emitted_guard}, {emitted_body})"
        return f"#matchCase({emitted_pattern}, {emitted_body})"
    if emitted_guard is not None:
        return f"#matchCasesGuard({emitted_pattern}, {emitted_guard}, {emitted_body}, {emit_match_cases(node, cases[1:])})"
    return f"#matchCases({emitted_pattern}, {emitted_body}, {emit_match_cases(node, cases[1:])})"


def emit_match_pattern(node: ast.AST, pattern: ast.pattern) -> str:
    match pattern:
        case ast.MatchAs(pattern=None, name=None):
            return "#matchWildcard"
        case ast.MatchAs(pattern=None, name=name) if name is not None:
            return f"#matchCapture({emit_id(name)})"
        case ast.MatchAs(pattern=as_pattern, name=name) if name is not None:
            return f"#matchAs({emit_match_binding_pattern(node, as_pattern)}, {emit_id(name)})"
        case ast.MatchSingleton(value=True):
            return "#matchSingleton(True)"
        case ast.MatchSingleton(value=False):
            return "#matchSingleton(False)"
        case ast.MatchSingleton(value=None):
            return "#matchSingleton(None)"
        case ast.MatchValue(value=value):
            return f"#matchValue({emit_exp(value)})"
        case ast.MatchOr(patterns=patterns):
            return emit_match_or_patterns(node, patterns, allow_capture=True)
        case ast.MatchSequence(patterns=patterns):
            return emit_match_sequence_pattern(node, patterns, allow_star_capture=True, allow_element_capture=True)
        case ast.MatchMapping(keys=keys, patterns=patterns, rest=rest):
            return emit_match_mapping_pattern(
                node, keys, patterns, rest, allow_rest_capture=True, allow_value_capture=True
            )
        case ast.MatchClass(cls=cls, patterns=[], kwd_attrs=kwd_attrs, kwd_patterns=kwd_patterns) if kwd_attrs:
            return emit_match_class_kw_pattern(node, cls, kwd_attrs, kwd_patterns, allow_capture=True)
        case ast.MatchClass(cls=cls, patterns=[subpattern], kwd_attrs=kwd_attrs, kwd_patterns=kwd_patterns) if kwd_attrs:
            return emit_single_arg_match_class_kw_pattern(
                node, cls, subpattern, kwd_attrs, kwd_patterns, allow_capture=True
            )
        case ast.MatchClass(cls=cls, patterns=[], kwd_attrs=[], kwd_patterns=[]):
            return emit_zero_arg_match_class(node, cls)
        case ast.MatchClass(cls=cls, patterns=[subpattern], kwd_attrs=[], kwd_patterns=[]):
            return emit_single_arg_match_class(node, cls, subpattern, allow_capture=True)
        case _:
            raise unsupported(node, "only value, singleton, wildcard, capture, non-binding OR, non-binding AS, non-binding sequence, non-binding mapping, zero-argument builtin class, and non-binding single-positional builtin class match patterns are supported")


def emit_match_or_patterns(node: ast.AST, patterns: list[ast.pattern], allow_capture: bool) -> str:
    if len(patterns) < 2:
        raise unsupported(node, "OR match patterns require at least two alternatives")
    left = emit_match_or_alternative_pattern(node, patterns[0], allow_capture=allow_capture)
    if len(patterns) == 2:
        right = emit_match_or_alternative_pattern(node, patterns[1], allow_capture=allow_capture)
    else:
        right = emit_match_or_patterns(node, patterns[1:], allow_capture=allow_capture)
    return f"#matchOr({left}, {right})"


def emit_match_or_alternative_pattern(node: ast.AST, pattern: ast.pattern, allow_capture: bool) -> str:
    if allow_capture:
        return emit_match_binding_pattern(node, pattern)
    return emit_match_nonbinding_pattern(node, pattern)


def emit_match_binding_pattern(node: ast.AST, pattern: ast.pattern) -> str:
    match pattern:
        case ast.MatchAs(pattern=None, name=None):
            return "#matchWildcard"
        case ast.MatchAs(pattern=None, name=name) if name is not None:
            return f"#matchCapture({emit_id(name)})"
        case ast.MatchAs(pattern=as_pattern, name=name) if name is not None:
            return f"#matchAs({emit_match_binding_pattern(node, as_pattern)}, {emit_id(name)})"
        case ast.MatchSingleton(value=True):
            return "#matchSingleton(True)"
        case ast.MatchSingleton(value=False):
            return "#matchSingleton(False)"
        case ast.MatchSingleton(value=None):
            return "#matchSingleton(None)"
        case ast.MatchValue(value=value) if isinstance(value, ast.Constant):
            return f"#matchValue({emit_exp(value)})"
        case ast.MatchOr(patterns=patterns):
            return emit_match_or_patterns(node, patterns, allow_capture=True)
        case ast.MatchSequence(patterns=patterns):
            return emit_match_sequence_pattern(
                node, patterns, allow_star_capture=True, allow_element_capture=True
            )
        case ast.MatchMapping(keys=keys, patterns=patterns, rest=rest):
            return emit_match_mapping_pattern(
                node, keys, patterns, rest, allow_rest_capture=True, allow_value_capture=True
            )
        case ast.MatchClass(cls=cls, patterns=[], kwd_attrs=kwd_attrs, kwd_patterns=kwd_patterns) if kwd_attrs:
            return emit_match_class_kw_pattern(node, cls, kwd_attrs, kwd_patterns, allow_capture=True)
        case ast.MatchClass(cls=cls, patterns=[subpattern], kwd_attrs=kwd_attrs, kwd_patterns=kwd_patterns) if kwd_attrs:
            return emit_single_arg_match_class_kw_pattern(
                node, cls, subpattern, kwd_attrs, kwd_patterns, allow_capture=True
            )
        case ast.MatchClass(cls=cls, patterns=[], kwd_attrs=[], kwd_patterns=[]):
            return emit_zero_arg_match_class(node, cls)
        case ast.MatchClass(cls=cls, patterns=[subpattern], kwd_attrs=[], kwd_patterns=[]):
            return emit_single_arg_match_class(node, cls, subpattern, allow_capture=True)
        case _:
            raise unsupported(node, "only supported binding match subpatterns may capture names")


def emit_match_nonbinding_pattern(node: ast.AST, pattern: ast.pattern) -> str:
    match pattern:
        case ast.MatchAs(pattern=None, name=None):
            return "#matchWildcard"
        case ast.MatchSingleton(value=True):
            return "#matchSingleton(True)"
        case ast.MatchSingleton(value=False):
            return "#matchSingleton(False)"
        case ast.MatchSingleton(value=None):
            return "#matchSingleton(None)"
        case ast.MatchValue(value=value) if isinstance(value, ast.Constant):
            return f"#matchValue({emit_exp(value)})"
        case ast.MatchOr(patterns=patterns):
            return emit_match_or_patterns(node, patterns, allow_capture=False)
        case ast.MatchSequence(patterns=patterns):
            return emit_match_sequence_pattern(node, patterns, allow_star_capture=False, allow_element_capture=False)
        case ast.MatchMapping(keys=keys, patterns=patterns, rest=rest):
            return emit_match_mapping_pattern(
                node, keys, patterns, rest, allow_rest_capture=False, allow_value_capture=False
            )
        case ast.MatchClass(cls=cls, patterns=[], kwd_attrs=kwd_attrs, kwd_patterns=kwd_patterns) if kwd_attrs:
            return emit_match_class_kw_pattern(node, cls, kwd_attrs, kwd_patterns, allow_capture=False)
        case ast.MatchClass(cls=cls, patterns=[subpattern], kwd_attrs=kwd_attrs, kwd_patterns=kwd_patterns) if kwd_attrs:
            return emit_single_arg_match_class_kw_pattern(
                node, cls, subpattern, kwd_attrs, kwd_patterns, allow_capture=False
            )
        case ast.MatchClass(cls=cls, patterns=[], kwd_attrs=[], kwd_patterns=[]):
            return emit_zero_arg_match_class(node, cls)
        case ast.MatchClass(cls=cls, patterns=[subpattern], kwd_attrs=[], kwd_patterns=[]):
            return emit_single_arg_match_class(node, cls, subpattern, allow_capture=False)
        case _:
            raise unsupported(node, "only non-binding wildcard, literal, singleton, OR, sequence, mapping, zero-argument builtin class, and single-positional builtin class pattern alternatives are supported")


def emit_zero_arg_match_class(node: ast.AST, cls: ast.expr) -> str:
    if not isinstance(cls, ast.Name):
        raise unsupported(node, "only simple-name zero-argument class match patterns are supported")
    if cls.id not in SUPPORTED_ZERO_ARG_CLASS_PATTERNS:
        raise unsupported(node, "only zero-argument class match patterns for current builtin value types are supported")
    return f"#matchClass({emit_id(CLASS_PATTERN_ID_ALIASES.get(cls.id, cls.id))})"


def emit_single_arg_match_class(
    node: ast.AST,
    cls: ast.expr,
    subpattern: ast.pattern,
    allow_capture: bool,
) -> str:
    if not isinstance(cls, ast.Name):
        raise unsupported(node, "only simple-name single-positional class match patterns are supported")
    if cls.id not in SUPPORTED_SINGLE_ARG_CLASS_PATTERNS:
        raise unsupported(node, "only single-positional class match patterns for builtin whole-object matching types are supported")
    emitted_class = emit_id(CLASS_PATTERN_ID_ALIASES.get(cls.id, cls.id))
    emitted_pattern = emit_match_class_arg_pattern(node, subpattern, allow_capture=allow_capture)
    return f"#matchClassArg({emitted_class}, {emitted_pattern})"


def emit_match_class_kw_pattern(
    node: ast.AST,
    cls: ast.expr,
    kwd_attrs: list[str],
    kwd_patterns: list[ast.pattern],
    allow_capture: bool,
) -> str:
    if not isinstance(cls, ast.Name):
        raise unsupported(node, "only simple-name keyword class match patterns are supported")
    if cls.id not in SUPPORTED_ZERO_ARG_CLASS_PATTERNS:
        raise unsupported(node, "only keyword class match patterns for current builtin value types are supported")
    emitted_class = emit_id(CLASS_PATTERN_ID_ALIASES.get(cls.id, cls.id))
    emitted_attrs = emit_match_class_attr_patterns(
        node, kwd_attrs, kwd_patterns, allow_capture=allow_capture
    )
    return f"#matchClassKw({emitted_class}, {emitted_attrs})"


def emit_single_arg_match_class_kw_pattern(
    node: ast.AST,
    cls: ast.expr,
    subpattern: ast.pattern,
    kwd_attrs: list[str],
    kwd_patterns: list[ast.pattern],
    allow_capture: bool,
) -> str:
    if not isinstance(cls, ast.Name):
        raise unsupported(node, "only simple-name positional-plus-keyword class match patterns are supported")
    if cls.id not in SUPPORTED_SINGLE_ARG_CLASS_PATTERNS:
        raise unsupported(node, "only positional-plus-keyword class match patterns for builtin whole-object matching types are supported")
    emitted_class = emit_id(CLASS_PATTERN_ID_ALIASES.get(cls.id, cls.id))
    emitted_pattern = emit_match_class_arg_pattern(node, subpattern, allow_capture=allow_capture)
    emitted_attrs = emit_match_class_attr_patterns(node, kwd_attrs, kwd_patterns, allow_capture=allow_capture)
    return f"#matchClassArgKw({emitted_class}, {emitted_pattern}, {emitted_attrs})"


def emit_match_class_attr_patterns(
    node: ast.AST,
    kwd_attrs: list[str],
    kwd_patterns: list[ast.pattern],
    allow_capture: bool,
) -> str:
    if len(kwd_attrs) != len(kwd_patterns):
        raise unsupported(node, "keyword class match pattern attribute/value arity mismatch")
    if not kwd_attrs:
        return "#matchNoAttrPatterns"
    if allow_capture:
        pattern = emit_match_binding_pattern(node, kwd_patterns[0])
    else:
        pattern = emit_match_nonbinding_pattern(node, kwd_patterns[0])
    rest = emit_match_class_attr_patterns(node, kwd_attrs[1:], kwd_patterns[1:], allow_capture=allow_capture)
    return f"#matchAttrPattern({emit_id(kwd_attrs[0])}, {pattern}, {rest})"


def emit_match_class_arg_pattern(node: ast.AST, pattern: ast.pattern, allow_capture: bool) -> str:
    if allow_capture:
        return emit_match_binding_pattern(node, pattern)
    return emit_match_nonbinding_pattern(node, pattern)


def emit_match_sequence_patterns(node: ast.AST, patterns: list[ast.pattern], allow_capture: bool) -> str:
    if not patterns:
        return "#matchNoPatterns"
    head = emit_match_sequence_element_pattern(node, patterns[0], allow_capture=allow_capture)
    return f"#matchPattern({head}, {emit_match_sequence_patterns(node, patterns[1:], allow_capture=allow_capture)})"


def emit_match_sequence_element_pattern(node: ast.AST, pattern: ast.pattern, allow_capture: bool) -> str:
    if allow_capture:
        return emit_match_binding_pattern(node, pattern)
    return emit_match_nonbinding_pattern(node, pattern)


def emit_match_sequence_pattern(
    node: ast.AST,
    patterns: list[ast.pattern],
    allow_star_capture: bool,
    allow_element_capture: bool,
) -> str:
    star_indices = [index for index, pattern in enumerate(patterns) if isinstance(pattern, ast.MatchStar)]
    if not star_indices:
        return f"#matchSequence({emit_match_sequence_patterns(node, patterns, allow_capture=allow_element_capture)})"
    if len(star_indices) != 1:
        raise unsupported(node, "sequence match patterns support at most one star pattern")
    star_index = star_indices[0]
    star_pattern = patterns[star_index]
    prefix = emit_match_sequence_patterns(node, patterns[:star_index], allow_capture=allow_element_capture)
    suffix = emit_match_sequence_patterns(node, patterns[star_index + 1 :], allow_capture=allow_element_capture)
    if not isinstance(star_pattern, ast.MatchStar):
        raise unsupported(node, "sequence star pattern shape is unsupported")
    if star_pattern.name is not None:
        if not allow_star_capture:
            raise unsupported(node, "capture-bearing starred sequence patterns require binding rollback in this position")
        return f"#matchSequenceStarCapture({prefix}, {emit_id(star_pattern.name)}, {suffix})"
    return f"#matchSequenceStar({prefix}, {suffix})"


def emit_match_mapping_pattern(
    node: ast.AST,
    keys: list[ast.expr],
    patterns: list[ast.pattern],
    rest: str | None,
    allow_rest_capture: bool,
    allow_value_capture: bool,
) -> str:
    if rest is not None:
        if not allow_rest_capture:
            raise unsupported(node, "capture-bearing mapping **rest patterns require binding rollback in this position")
        return f"#matchMappingRest({emit_match_mapping_patterns(node, keys, patterns, allow_capture=allow_value_capture)}, {emit_id(rest)})"
    if len(keys) != len(patterns):
        raise unsupported(node, "mapping match pattern key/value arity mismatch")
    return f"#matchMapping({emit_match_mapping_patterns(node, keys, patterns, allow_capture=allow_value_capture)})"


def emit_match_mapping_patterns(
    node: ast.AST,
    keys: list[ast.expr],
    patterns: list[ast.pattern],
    allow_capture: bool,
) -> str:
    if not keys:
        return "#matchNoMapPatterns"
    key = keys[0]
    if not isinstance(key, ast.Constant):
        raise unsupported(node, "only constant mapping match pattern keys are supported")
    value_pattern = emit_match_mapping_value_pattern(node, patterns[0], allow_capture=allow_capture)
    rest = emit_match_mapping_patterns(node, keys[1:], patterns[1:], allow_capture=allow_capture)
    return f"#matchMapPattern({emit_exp(key)}, {value_pattern}, {rest})"


def emit_match_mapping_value_pattern(node: ast.AST, pattern: ast.pattern, allow_capture: bool) -> str:
    if allow_capture:
        return emit_match_binding_pattern(node, pattern)
    return emit_match_nonbinding_pattern(node, pattern)


def emit_except_handlers(node: ast.AST, handlers: list[ast.ExceptHandler]) -> str:
    handler = handlers[0]
    if handler.type is None:
        if handler.name is not None:
            raise unsupported(node, "bare except handlers cannot bind a target")
        if len(handlers) != 1:
            raise unsupported(node, "bare except handlers must be last")
        return f"#exceptAny({emit_block(handler.body)})"
    emitted_exception, is_tuple = emit_except_type(node, handler.type)
    emitted_alias = emit_id(handler.name) if handler.name is not None else None
    emitted_handler = emit_block(handler.body)
    if len(handlers) == 1:
        if is_tuple and emitted_alias is not None:
            return f"#exceptTupleAs({emitted_exception}, {emitted_alias}, {emitted_handler})"
        if is_tuple:
            return f"#exceptTuple({emitted_exception}, {emitted_handler})"
        if emitted_alias is not None:
            return f"#exceptAs({emitted_exception}, {emitted_alias}, {emitted_handler})"
        return f"#except({emitted_exception}, {emitted_handler})"
    emitted_rest = emit_except_handlers(node, handlers[1:])
    if is_tuple and emitted_alias is not None:
        return f"#exceptsTupleAs({emitted_exception}, {emitted_alias}, {emitted_handler}, {emitted_rest})"
    if is_tuple:
        return f"#exceptsTuple({emitted_exception}, {emitted_handler}, {emitted_rest})"
    if emitted_alias is not None:
        return f"#exceptsAs({emitted_exception}, {emitted_alias}, {emitted_handler}, {emitted_rest})"
    return f"#excepts({emitted_exception}, {emitted_handler}, {emitted_rest})"


def emit_except_type(node: ast.AST, type_expr: ast.expr) -> tuple[str, bool]:
    if isinstance(type_expr, ast.Name):
        return emit_id(type_expr.id), False
    if isinstance(type_expr, ast.Tuple) and type_expr.elts:
        names = []
        for elt in type_expr.elts:
            if not isinstance(elt, ast.Name):
                raise unsupported(node, "only named exception types in except tuples are supported")
            names.append(elt.id)
        return emit_id_items(names), True
    raise unsupported(node, "only named except handlers and named exception tuples are supported")


def emit_builtin_classinfo(node: ast.AST, classinfo: ast.expr) -> tuple[str, bool]:
    if isinstance(classinfo, ast.Name):
        return emit_builtin_class_name(node, classinfo, "classinfo"), False
    if isinstance(classinfo, ast.Tuple):
        names = []
        for elt in classinfo.elts:
            names.append(emit_builtin_class_name(node, elt, "classinfo tuple entry"))
        return emit_id_items(names), True
    raise unsupported(
        node,
        "classinfo currently supports known built-in class names and tuples of them",
    )


def emit_builtin_class_name(node: ast.AST, class_expr: ast.expr, role: str) -> str:
    if isinstance(class_expr, ast.Name) and class_expr.id in SUPPORTED_BUILTIN_CLASS_NAMES:
        return emit_id(CLASS_PATTERN_ID_ALIASES.get(class_expr.id, class_expr.id))
    raise unsupported(node, f"{role} currently supports known built-in class names")


def emit_getattr_name(name_expr: ast.expr) -> str | None:
    if isinstance(name_expr, ast.Constant) and isinstance(name_expr.value, str):
        if name_expr.value in SUPPORTED_GETATTR_NAMES:
            return emit_id(name_expr.value)
    return None


def emit_format_spec(node: ast.AST, spec_expr: ast.expr) -> str | None:
    if isinstance(spec_expr, ast.Constant) and isinstance(spec_expr.value, str):
        if format_spec_supported(spec_expr.value):
            return emit_exp(spec_expr)
        raise unsupported(node, "format currently supports only the current string/integer/special-float format_spec subset")
    return None


def ensure_non_async_comprehension(
    node: ast.AST, kind: str, generators: list[ast.comprehension]
) -> None:
    if any(generator.is_async for generator in generators):
        raise unsupported(node, f"async {kind} comprehensions are not supported yet")


def emit_comp_clause(generator: ast.comprehension) -> str:
    return (
        f"#compClause({emit_exp(generator.iter)}, {emit_target(generator.target)}, "
        f"{emit_maybe_comp_filters(generator.ifs)})"
    )


def emit_comp_clauses(generators: list[ast.comprehension]) -> str:
    if not generators:
        raise ValueError("comprehension clause list must be nonempty")
    if len(generators) == 1:
        return emit_comp_clause(generators[0])
    generator = generators[0]
    return (
        f"#compClauses({emit_exp(generator.iter)}, {emit_target(generator.target)}, "
        f"{emit_maybe_comp_filters(generator.ifs)}, {emit_comp_clauses(generators[1:])})"
    )


def emit_maybe_comp_clauses(generators: list[ast.comprehension]) -> str:
    if not generators:
        return "#noCompClauses"
    return f"#compRest({emit_comp_clauses(generators)})"


def emit_list_comprehension_many(
    node: ast.AST, elt: ast.expr, generators: list[ast.comprehension]
) -> str:
    if len(generators) < 4:
        raise unsupported(node, "list comprehension generator shape is not supported")
    ensure_non_async_comprehension(node, "list", generators)
    outer = generators[0]
    return (
        f"#listCompMany({emit_exp(outer.iter)}, {emit_target(outer.target)}, "
        f"{emit_maybe_comp_filters(outer.ifs)}, "
        f"{emit_maybe_comp_clauses(generators[1:])}, {emit_exp(elt)})"
    )


def emit_generator_expression(
    node: ast.AST, elt: ast.expr, generators: list[ast.comprehension]
) -> str:
    ensure_non_async_comprehension(node, "generator expression", generators)
    if len(generators) == 1:
        materialized = emit_list_comprehension(node, elt, generators[0])
    elif len(generators) == 2:
        materialized = emit_list_comprehension_two_generators(
            node, elt, generators[0], generators[1]
        )
    elif len(generators) == 3:
        materialized = emit_list_comprehension_three_generators(
            node, elt, generators[0], generators[1], generators[2]
        )
    else:
        materialized = emit_list_comprehension_many(node, elt, generators)
    return f"#genExp({materialized})"


def simple_generator_yields(body: list[ast.stmt]) -> list[ast.Yield] | None:
    yields: list[ast.Yield] = []
    for stmt in body:
        if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Yield):
            yields.append(stmt.value)
            continue
        return None
    return yields or None


def emit_yield_value(value: ast.expr | None) -> str:
    if value is None:
        return "None"
    return emit_exp(value)


def emit_yield_exps(yields: list[ast.Yield]) -> str:
    if len(yields) == 1:
        return f"#yield({emit_yield_value(yields[0].value)})"
    return f"#yields({emit_yield_value(yields[0].value)}, {emit_yield_exps(yields[1:])})"


def emit_simple_generator_function_def(
    name: str,
    args: ast.arguments,
    body: list[ast.stmt],
    decorators: list[ast.expr],
    returns: ast.expr | None,
) -> str | None:
    if decorators or returns is not None:
        return None
    if (
        args.posonlyargs
        or args.defaults
        or args.vararg is not None
        or args.kwonlyargs
        or any(default is not None for default in args.kw_defaults)
        or args.kwarg is not None
    ):
        return None
    yields = simple_generator_yields(body)
    if yields is None:
        return None
    names = [arg.arg for arg in args.args]
    return f"#genDef({emit_id(name)}, {emit_id_items(names)}, {emit_yield_exps(yields)})"


def split_body_docstring(body: list[ast.stmt]) -> tuple[str, list[ast.stmt]]:
    if (
        body
        and isinstance(body[0], ast.Expr)
        and isinstance(body[0].value, ast.Constant)
        and isinstance(body[0].value.value, str)
    ):
        return emit_string(body[0].value.value), body[1:]
    return "None", body


def collect_current_block_global_names(body: list[ast.stmt]) -> list[str]:
    names: list[str] = []

    def add(name: str) -> None:
        if name not in names:
            names.append(name)

    def visit(node: ast.AST) -> None:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            return
        if isinstance(node, ast.Global):
            for item in node.names:
                add(item)
            return
        for child in ast.iter_child_nodes(node):
            visit(child)

    for stmt in body:
        visit(stmt)
    return names


def current_block_contains_yield(body: list[ast.stmt]) -> bool:
    found = False

    def visit(node: ast.AST) -> None:
        nonlocal found
        if found:
            return
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            return
        if isinstance(node, (ast.Yield, ast.YieldFrom)):
            found = True
            return
        for child in ast.iter_child_nodes(node):
            visit(child)

    for stmt in body:
        visit(stmt)
    return found


def supported_global_function_signature(args: ast.arguments, decorators: list[ast.expr]) -> bool:
    return (
        not decorators
        and not args.posonlyargs
        and args.vararg is None
        and not args.kwonlyargs
        and args.kwarg is None
    )


def emit_simple_class_def(
    node: ast.AST,
    name: str,
    bases: list[ast.expr],
    keywords: list[ast.keyword],
    body: list[ast.stmt],
    decorators: list[ast.expr],
) -> str:
    if keywords:
        raise unsupported(node, "class metaclass keywords are not supported yet")
    if len(bases) > 1:
        raise unsupported(node, "multiple class bases are not supported yet")
    base_name: str | None = None
    if bases:
        if not isinstance(bases[0], ast.Name):
            raise unsupported(node, "only simple name class bases are supported in the current class profile")
        if bases[0].id in SUPPORTED_BUILTIN_CLASS_NAMES:
            raise unsupported(node, "builtin class bases are not supported yet")
        base_name = bases[0].id
    if getattr(node, "type_params", []):
        raise unsupported(node, "class type parameters are not supported yet")
    doc_value, body_items = split_body_docstring(body)
    members: list[tuple[str, str, str, str, str]] = [
        ("attr", emit_id("__module__"), emit_string("__main__"), "", ""),
        ("attr", emit_id("__qualname__"), emit_string(name), "", ""),
        ("attr", emit_id("__doc__"), doc_value, "", ""),
    ]
    for stmt in body_items:
        match stmt:
            case ast.Pass():
                continue
            case ast.Assign(targets=[ast.Name(id=attr, ctx=ast.Store())], value=value, type_comment=None):
                members.append(("attr", emit_id(attr), emit_exp(value), "", ""))
            case ast.Assign(type_comment=type_comment) if type_comment is not None:
                raise unsupported(stmt, "class-body type comments are not supported yet")
            case ast.FunctionDef(
                name=method_name,
                args=args,
                body=method_body,
                decorator_list=method_decorators,
                returns=method_returns,
                type_comment=method_type_comment,
            ):
                member = emit_simple_class_method(
                    stmt,
                    method_name,
                    args,
                    method_body,
                    method_decorators,
                    method_returns,
                    method_type_comment,
                )
                if member[0] in {"propertygetter", "propertysetter", "propertydeleter"}:
                    previous_kind = next((kind for kind, attr_name, _payload, _defaults, _body in reversed(members) if attr_name == member[1]), None)
                    if previous_kind not in {"property", "propertygetter", "propertysetter", "propertydeleter"}:
                        raise unsupported(stmt, "property getters, setters, and deleters currently require a prior @property for the same class-body name")
                members.append(member)
            case _:
                raise unsupported(
                    stmt,
                    "only pass, simple name assignments, and simple method definitions are supported in the current class body profile",
                )
    if decorators:
        decorator_exps = emit_arg_exps(decorators)
        if base_name is not None:
            return f"#classBaseDecorated({emit_id(name)}, {emit_id(base_name)}, {decorator_exps}, {emit_class_attr_exps(members)})"
        return f"#classDecorated({emit_id(name)}, {decorator_exps}, {emit_class_attr_exps(members)})"
    if base_name is not None:
        return f"#classBase({emit_id(name)}, {emit_id(base_name)}, {emit_class_attr_exps(members)})"
    return f"#classAttrs({emit_id(name)}, {emit_class_attr_exps(members)})"


def emit_simple_class_method(
    node: ast.AST,
    name: str,
    args: ast.arguments,
    body: list[ast.stmt],
    decorators: list[ast.expr],
    returns: ast.expr | None,
    type_comment: str | None,
) -> tuple[str, str, str, str, str]:
    # Python 3.14 annotations are lazy metadata. The current method values do
    # not expose metadata/introspection, so annotations are erased in this subset.
    _ = returns
    method_kind = "method"
    if decorators:
        if len(decorators) != 1:
            raise unsupported(node, "only @staticmethod, @classmethod, @property, simple @name.getter, simple @name.setter, and simple @name.deleter are supported in the current method profile")
        decorator = decorators[0]
        if isinstance(decorator, ast.Name) and decorator.id == "staticmethod":
            method_kind = "staticmethod"
        elif isinstance(decorator, ast.Name) and decorator.id == "classmethod":
            method_kind = "classmethod"
        elif isinstance(decorator, ast.Name) and decorator.id == "property":
            method_kind = "property"
        elif (
            isinstance(decorator, ast.Attribute)
            and decorator.attr == "getter"
            and isinstance(decorator.value, ast.Name)
            and decorator.value.id == name
        ):
            method_kind = "propertygetter"
        elif (
            isinstance(decorator, ast.Attribute)
            and decorator.attr == "setter"
            and isinstance(decorator.value, ast.Name)
            and decorator.value.id == name
        ):
            method_kind = "propertysetter"
        elif (
            isinstance(decorator, ast.Attribute)
            and decorator.attr == "deleter"
            and isinstance(decorator.value, ast.Name)
            and decorator.value.id == name
        ):
            method_kind = "propertydeleter"
        else:
            raise unsupported(node, "only @staticmethod, @classmethod, @property, simple @name.getter, simple @name.setter, and simple @name.deleter are supported in the current method profile")
    if type_comment is not None:
        raise unsupported(node, "method type comments are not supported yet")
    if getattr(node, "type_params", []):
        raise unsupported(node, "method type parameters are not supported yet")
    pos_names = [arg.arg for arg in args.posonlyargs]
    names = [arg.arg for arg in args.args]
    if not (pos_names or names) and method_kind != "staticmethod":
        raise unsupported(node, "class methods currently require at least an explicit self parameter")
    if (
        args.posonlyargs
        or args.defaults
        or args.vararg is not None
        or args.kwarg is not None
        or args.kwonlyargs
        or any(default is not None for default in args.kw_defaults)
    ) and method_kind in {"property", "propertygetter", "propertysetter", "propertydeleter"}:
        raise unsupported(node, "property accessors currently do not support positional-only parameters, default parameter values, keyword-only parameters, *args, or **kwargs")
    if method_kind in {"property", "propertygetter"} and len(names) != 1:
        raise unsupported(node, "properties currently support only a getter with an explicit self parameter")
    if method_kind == "propertysetter" and len(names) != 2:
        raise unsupported(node, "property setters currently support only an explicit self parameter and one value parameter")
    if method_kind == "propertydeleter" and len(names) != 1:
        raise unsupported(node, "property deleters currently support only an explicit self parameter")
    if args.kwonlyargs:
        if args.kwarg is not None:
            kw_names = [arg.arg for arg in args.kwonlyargs]
            kw_defaults = emit_kw_defaults(args.kw_defaults)
            if args.posonlyargs:
                payload = f"{emit_id_items(pos_names)}, {emit_id_items(names)}"
                if args.vararg is not None:
                    if args.defaults or kw_defaults is not None:
                        pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                        kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                        return (
                            f"{method_kind}posonlyvarargskwdefaultskwargs",
                            emit_id(name),
                            payload,
                            f"{pos_defaults}, {emit_id(args.vararg.arg)}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {emit_id(args.kwarg.arg)}",
                            emit_block(body),
                        )
                    return (
                        f"{method_kind}posonlyvarargskwonlykwargs",
                        emit_id(name),
                        payload,
                        f"{emit_id(args.vararg.arg)}, {emit_id_items(kw_names)}, {emit_id(args.kwarg.arg)}",
                        emit_block(body),
                    )
                if args.defaults or kw_defaults is not None:
                    pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                    kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                    return (
                        f"{method_kind}posonlykwdefaultskwargs",
                        emit_id(name),
                        payload,
                        f"{pos_defaults}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {emit_id(args.kwarg.arg)}",
                        emit_block(body),
                    )
                return (
                    f"{method_kind}posonlykwonlykwargs",
                    emit_id(name),
                    payload,
                    f"{emit_id_items(kw_names)}, {emit_id(args.kwarg.arg)}",
                    emit_block(body),
                )
            if args.vararg is not None:
                if args.defaults or kw_defaults is not None:
                    pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                    kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                    return (
                        f"{method_kind}varargskwdefaultskwargs",
                        emit_id(name),
                        emit_id_items(names),
                        f"{pos_defaults}, {emit_id(args.vararg.arg)}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {emit_id(args.kwarg.arg)}",
                        emit_block(body),
                    )
                return (
                    f"{method_kind}varargskwonlykwargs",
                    emit_id(name),
                    emit_id_items(names),
                    f"{emit_id(args.vararg.arg)}, {emit_id_items(kw_names)}, {emit_id(args.kwarg.arg)}",
                    emit_block(body),
                )
            if args.defaults or kw_defaults is not None:
                pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                return (
                    f"{method_kind}kwdefaultskwargs",
                    emit_id(name),
                    emit_id_items(names),
                    f"{pos_defaults}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {emit_id(args.kwarg.arg)}",
                    emit_block(body),
                )
            return (
                f"{method_kind}kwonlykwargs",
                emit_id(name),
                emit_id_items(names),
                f"{emit_id_items(kw_names)}, {emit_id(args.kwarg.arg)}",
                emit_block(body),
            )
        kw_names = [arg.arg for arg in args.kwonlyargs]
        kw_defaults = emit_kw_defaults(args.kw_defaults)
        if args.posonlyargs and args.vararg is not None:
            payload = f"{emit_id_items(pos_names)}, {emit_id_items(names)}"
            if args.defaults or kw_defaults is not None:
                pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                return (
                    f"{method_kind}posonlyvarargskwdefaults",
                    emit_id(name),
                    payload,
                    f"{pos_defaults}, {emit_id(args.vararg.arg)}, {emit_id_items(kw_names)}, {kw_defaults_exp}",
                    emit_block(body),
                )
            return (
                f"{method_kind}posonlyvarargskwonly",
                emit_id(name),
                payload,
                f"{emit_id(args.vararg.arg)}, {emit_id_items(kw_names)}",
                emit_block(body),
            )
        if args.vararg is not None:
            if args.defaults or kw_defaults is not None:
                pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                return (
                    f"{method_kind}varargskwdefaults",
                    emit_id(name),
                    emit_id_items(names),
                    f"{pos_defaults}, {emit_id(args.vararg.arg)}, {emit_id_items(kw_names)}, {kw_defaults_exp}",
                    emit_block(body),
                )
            return (
                f"{method_kind}varargskwonly",
                emit_id(name),
                emit_id_items(names),
                f"{emit_id(args.vararg.arg)}, {emit_id_items(kw_names)}",
                emit_block(body),
            )
        if args.posonlyargs:
            payload = f"{emit_id_items(pos_names)}, {emit_id_items(names)}"
            if args.defaults or kw_defaults is not None:
                pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                return (
                    f"{method_kind}posonlykwdefaults",
                    emit_id(name),
                    payload,
                    f"{pos_defaults}, {emit_id_items(kw_names)}, {kw_defaults_exp}",
                    emit_block(body),
                )
            return (f"{method_kind}posonlykwonly", emit_id(name), payload, emit_id_items(kw_names), emit_block(body))
        if args.defaults or kw_defaults is not None:
            pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
            kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
            return (
                f"{method_kind}kwdefaults",
                emit_id(name),
                emit_id_items(names),
                f"{pos_defaults}, {emit_id_items(kw_names)}, {kw_defaults_exp}",
                emit_block(body),
            )
        return (f"{method_kind}kwonly", emit_id(name), emit_id_items(names), emit_id_items(kw_names), emit_block(body))
    if args.posonlyargs:
        payload = f"{emit_id_items(pos_names)}, {emit_id_items(names)}"
        if args.kwarg is not None:
            if args.vararg is not None:
                extra = f"{emit_id(args.vararg.arg)}, {emit_id(args.kwarg.arg)}"
                if args.defaults:
                    return (f"{method_kind}posonlyvarkwargsdefaults", emit_id(name), payload, f"{emit_arg_exps(args.defaults)}, {extra}", emit_block(body))
                return (f"{method_kind}posonlyvarkwargs", emit_id(name), payload, extra, emit_block(body))
            if args.defaults:
                return (f"{method_kind}posonlykwargsdefaults", emit_id(name), payload, f"{emit_arg_exps(args.defaults)}, {emit_id(args.kwarg.arg)}", emit_block(body))
            return (f"{method_kind}posonlykwargs", emit_id(name), payload, emit_id(args.kwarg.arg), emit_block(body))
        if args.vararg is not None:
            if args.defaults:
                return (f"{method_kind}posonlyvarargsdefaults", emit_id(name), payload, f"{emit_arg_exps(args.defaults)}, {emit_id(args.vararg.arg)}", emit_block(body))
            return (f"{method_kind}posonlyvarargs", emit_id(name), payload, emit_id(args.vararg.arg), emit_block(body))
        if args.defaults:
            return (f"{method_kind}posonlydefaults", emit_id(name), payload, emit_arg_exps(args.defaults), emit_block(body))
        return (f"{method_kind}posonly", emit_id(name), payload, "", emit_block(body))
    if args.vararg is not None and args.kwarg is not None:
        payload = f"{emit_id(args.vararg.arg)}, {emit_id(args.kwarg.arg)}"
        if args.defaults:
            return (f"{method_kind}varkwargsdefaults", emit_id(name), emit_id_items(names), f"{emit_arg_exps(args.defaults)}, {payload}", emit_block(body))
        return (f"{method_kind}varkwargs", emit_id(name), emit_id_items(names), payload, emit_block(body))
    if args.kwarg is not None:
        if args.defaults:
            return (f"{method_kind}kwargsdefaults", emit_id(name), emit_id_items(names), f"{emit_arg_exps(args.defaults)}, {emit_id(args.kwarg.arg)}", emit_block(body))
        return (f"{method_kind}kwargs", emit_id(name), emit_id_items(names), emit_id(args.kwarg.arg), emit_block(body))
    if args.vararg is not None:
        if args.defaults:
            return (f"{method_kind}varargsdefaults", emit_id(name), emit_id_items(names), f"{emit_arg_exps(args.defaults)}, {emit_id(args.vararg.arg)}", emit_block(body))
        return (f"{method_kind}varargs", emit_id(name), emit_id_items(names), emit_id(args.vararg.arg), emit_block(body))
    if args.defaults:
        return (f"{method_kind}defaults", emit_id(name), emit_id_items(names), emit_arg_exps(args.defaults), emit_block(body))
    return (method_kind, emit_id(name), emit_id_items(names), "", emit_block(body))


def emit_class_attr_exps(members: list[tuple[str, str, str, str, str]]) -> str:
    if not members:
        return "#noClassAttrs"
    kind, name, payload, defaults, body = members[0]
    rest = emit_class_attr_exps(members[1:])
    if kind == "attr":
        return f"#classAttr({name}, {payload}, {rest})"
    pos_only_extended_method_ctors = {
        "methodposonlyvarargs": "#classMethodPosOnlyVarArgs",
        "methodposonlyvarargsdefaults": "#classMethodPosOnlyVarArgsDefaults",
        "methodposonlykwargs": "#classMethodPosOnlyKwArgs",
        "methodposonlykwargsdefaults": "#classMethodPosOnlyKwArgsDefaults",
        "methodposonlyvarkwargs": "#classMethodPosOnlyVarKwArgs",
        "methodposonlyvarkwargsdefaults": "#classMethodPosOnlyVarKwArgsDefaults",
        "methodposonlyvarargskwonly": "#classMethodPosOnlyVarArgsKwOnly",
        "methodposonlyvarargskwdefaults": "#classMethodPosOnlyVarArgsKwDefaults",
        "methodposonlyvarargskwonlykwargs": "#classMethodPosOnlyVarArgsKwOnlyKwArgs",
        "methodposonlyvarargskwdefaultskwargs": "#classMethodPosOnlyVarArgsKwDefaultsKwArgs",
        "methodposonlykwonlykwargs": "#classMethodPosOnlyKwOnlyKwArgs",
        "methodposonlykwdefaultskwargs": "#classMethodPosOnlyKwDefaultsKwArgs",
        "staticmethodposonlyvarargs": "#classStaticMethodPosOnlyVarArgs",
        "staticmethodposonlyvarargsdefaults": "#classStaticMethodPosOnlyVarArgsDefaults",
        "staticmethodposonlykwargs": "#classStaticMethodPosOnlyKwArgs",
        "staticmethodposonlykwargsdefaults": "#classStaticMethodPosOnlyKwArgsDefaults",
        "staticmethodposonlyvarkwargs": "#classStaticMethodPosOnlyVarKwArgs",
        "staticmethodposonlyvarkwargsdefaults": "#classStaticMethodPosOnlyVarKwArgsDefaults",
        "staticmethodposonlyvarargskwonly": "#classStaticMethodPosOnlyVarArgsKwOnly",
        "staticmethodposonlyvarargskwdefaults": "#classStaticMethodPosOnlyVarArgsKwDefaults",
        "staticmethodposonlyvarargskwonlykwargs": "#classStaticMethodPosOnlyVarArgsKwOnlyKwArgs",
        "staticmethodposonlyvarargskwdefaultskwargs": "#classStaticMethodPosOnlyVarArgsKwDefaultsKwArgs",
        "staticmethodposonlykwonlykwargs": "#classStaticMethodPosOnlyKwOnlyKwArgs",
        "staticmethodposonlykwdefaultskwargs": "#classStaticMethodPosOnlyKwDefaultsKwArgs",
        "classmethodposonlyvarargs": "#classClassMethodPosOnlyVarArgs",
        "classmethodposonlyvarargsdefaults": "#classClassMethodPosOnlyVarArgsDefaults",
        "classmethodposonlykwargs": "#classClassMethodPosOnlyKwArgs",
        "classmethodposonlykwargsdefaults": "#classClassMethodPosOnlyKwArgsDefaults",
        "classmethodposonlyvarkwargs": "#classClassMethodPosOnlyVarKwArgs",
        "classmethodposonlyvarkwargsdefaults": "#classClassMethodPosOnlyVarKwArgsDefaults",
        "classmethodposonlyvarargskwonly": "#classClassMethodPosOnlyVarArgsKwOnly",
        "classmethodposonlyvarargskwdefaults": "#classClassMethodPosOnlyVarArgsKwDefaults",
        "classmethodposonlyvarargskwonlykwargs": "#classClassMethodPosOnlyVarArgsKwOnlyKwArgs",
        "classmethodposonlyvarargskwdefaultskwargs": "#classClassMethodPosOnlyVarArgsKwDefaultsKwArgs",
        "classmethodposonlykwonlykwargs": "#classClassMethodPosOnlyKwOnlyKwArgs",
        "classmethodposonlykwdefaultskwargs": "#classClassMethodPosOnlyKwDefaultsKwArgs",
    }
    if kind in pos_only_extended_method_ctors:
        return f"{pos_only_extended_method_ctors[kind]}({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "method":
        return f"#classMethod({name}, {payload}, {body}, {rest})"
    if kind == "methoddefaults":
        return f"#classMethodDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodvarargs":
        return f"#classMethodVarArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodvarargsdefaults":
        return f"#classMethodVarArgsDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodvarargskwonly":
        return f"#classMethodVarArgsKwOnly({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodvarargskwdefaults":
        return f"#classMethodVarArgsKwDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodvarargskwonlykwargs":
        return f"#classMethodVarArgsKwOnlyKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodvarargskwdefaultskwargs":
        return f"#classMethodVarArgsKwDefaultsKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodvarkwargs":
        return f"#classMethodVarKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodvarkwargsdefaults":
        return f"#classMethodVarKwArgsDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodkwargs":
        return f"#classMethodKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodkwargsdefaults":
        return f"#classMethodKwArgsDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodkwonly":
        return f"#classMethodKwOnly({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodkwdefaults":
        return f"#classMethodKwDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodkwonlykwargs":
        return f"#classMethodKwOnlyKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodkwdefaultskwargs":
        return f"#classMethodKwDefaultsKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodposonly":
        return f"#classMethodPosOnly({name}, {payload}, {body}, {rest})"
    if kind == "methodposonlydefaults":
        return f"#classMethodPosOnlyDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodposonlykwonly":
        return f"#classMethodPosOnlyKwOnly({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "methodposonlykwdefaults":
        return f"#classMethodPosOnlyKwOnlyDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethod":
        return f"#classStaticMethod({name}, {payload}, {body}, {rest})"
    if kind == "staticmethoddefaults":
        return f"#classStaticMethodDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodvarargs":
        return f"#classStaticMethodVarArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodvarargsdefaults":
        return f"#classStaticMethodVarArgsDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodvarargskwonly":
        return f"#classStaticMethodVarArgsKwOnly({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodvarargskwdefaults":
        return f"#classStaticMethodVarArgsKwDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodvarargskwonlykwargs":
        return f"#classStaticMethodVarArgsKwOnlyKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodvarargskwdefaultskwargs":
        return f"#classStaticMethodVarArgsKwDefaultsKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodvarkwargs":
        return f"#classStaticMethodVarKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodvarkwargsdefaults":
        return f"#classStaticMethodVarKwArgsDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodkwargs":
        return f"#classStaticMethodKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodkwargsdefaults":
        return f"#classStaticMethodKwArgsDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodkwonly":
        return f"#classStaticMethodKwOnly({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodkwdefaults":
        return f"#classStaticMethodKwDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodkwonlykwargs":
        return f"#classStaticMethodKwOnlyKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodkwdefaultskwargs":
        return f"#classStaticMethodKwDefaultsKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodposonly":
        return f"#classStaticMethodPosOnly({name}, {payload}, {body}, {rest})"
    if kind == "staticmethodposonlydefaults":
        return f"#classStaticMethodPosOnlyDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodposonlykwonly":
        return f"#classStaticMethodPosOnlyKwOnly({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "staticmethodposonlykwdefaults":
        return f"#classStaticMethodPosOnlyKwOnlyDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethod":
        return f"#classClassMethod({name}, {payload}, {body}, {rest})"
    if kind == "classmethoddefaults":
        return f"#classClassMethodDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodvarargs":
        return f"#classClassMethodVarArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodvarargsdefaults":
        return f"#classClassMethodVarArgsDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodvarargskwonly":
        return f"#classClassMethodVarArgsKwOnly({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodvarargskwdefaults":
        return f"#classClassMethodVarArgsKwDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodvarargskwonlykwargs":
        return f"#classClassMethodVarArgsKwOnlyKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodvarargskwdefaultskwargs":
        return f"#classClassMethodVarArgsKwDefaultsKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodvarkwargs":
        return f"#classClassMethodVarKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodvarkwargsdefaults":
        return f"#classClassMethodVarKwArgsDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodkwargs":
        return f"#classClassMethodKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodkwargsdefaults":
        return f"#classClassMethodKwArgsDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodkwonly":
        return f"#classClassMethodKwOnly({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodkwdefaults":
        return f"#classClassMethodKwDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodkwonlykwargs":
        return f"#classClassMethodKwOnlyKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodkwdefaultskwargs":
        return f"#classClassMethodKwDefaultsKwArgs({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodposonly":
        return f"#classClassMethodPosOnly({name}, {payload}, {body}, {rest})"
    if kind == "classmethodposonlydefaults":
        return f"#classClassMethodPosOnlyDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodposonlykwonly":
        return f"#classClassMethodPosOnlyKwOnly({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "classmethodposonlykwdefaults":
        return f"#classClassMethodPosOnlyKwOnlyDefaults({name}, {payload}, {defaults}, {body}, {rest})"
    if kind == "property":
        return f"#classProperty({name}, {payload}, {body}, {rest})"
    if kind == "propertygetter":
        return f"#classPropertyGetter({name}, {payload}, {body}, {rest})"
    if kind == "propertysetter":
        return f"#classPropertySetter({name}, {payload}, {body}, {rest})"
    if kind == "propertydeleter":
        return f"#classPropertyDeleter({name}, {payload}, {body}, {rest})"
    raise AssertionError(f"unknown class member kind: {kind}")


def emit_list_comprehension(
    node: ast.AST, elt: ast.expr, generator: ast.comprehension
) -> str:
    if generator.is_async:
        raise unsupported(node, "async list comprehensions are not supported yet")
    if not isinstance(generator.target, ast.Name):
        if generator.ifs:
            return (
                f"#listCompTargetIfs({emit_exp(generator.iter)}, {emit_target(generator.target)}, "
                f"{emit_comp_filters(generator.ifs)}, {emit_exp(elt)})"
            )
        return (
            f"#listCompTarget({emit_exp(generator.iter)}, {emit_target(generator.target)}, "
            f"{emit_exp(elt)})"
        )
    if len(generator.ifs) > 1:
        return (
            f"#listCompIfs({emit_exp(generator.iter)}, {generator.target.id}, "
            f"{emit_comp_filters(generator.ifs)}, {emit_exp(elt)})"
        )
    if generator.ifs:
        return (
            f"#listCompIf({emit_exp(generator.iter)}, {generator.target.id}, "
            f"{emit_exp(generator.ifs[0])}, {emit_exp(elt)})"
        )
    return f"#listComp({emit_exp(generator.iter)}, {generator.target.id}, {emit_exp(elt)})"


def emit_list_comprehension_two_generators(
    node: ast.AST, elt: ast.expr, outer: ast.comprehension, inner: ast.comprehension
) -> str:
    if outer.is_async or inner.is_async:
        raise unsupported(node, "async list comprehensions are not supported yet")
    if not isinstance(outer.target, ast.Name) or not isinstance(inner.target, ast.Name):
        if outer.ifs or inner.ifs:
            return (
                f"#listCompTargetForIfs({emit_exp(outer.iter)}, {emit_target(outer.target)}, "
                f"{emit_maybe_comp_filters(outer.ifs)}, {emit_exp(inner.iter)}, "
                f"{emit_target(inner.target)}, {emit_maybe_comp_filters(inner.ifs)}, {emit_exp(elt)})"
            )
        return (
            f"#listCompTargetFor({emit_exp(outer.iter)}, {emit_target(outer.target)}, "
            f"{emit_exp(inner.iter)}, {emit_target(inner.target)}, {emit_exp(elt)})"
        )
    if outer.ifs or inner.ifs:
        return (
            f"#listCompForIfs({emit_exp(outer.iter)}, {outer.target.id}, "
            f"{emit_maybe_comp_filters(outer.ifs)}, {emit_exp(inner.iter)}, "
            f"{inner.target.id}, {emit_maybe_comp_filters(inner.ifs)}, {emit_exp(elt)})"
        )
    return (
        f"#listCompFor({emit_exp(outer.iter)}, {outer.target.id}, "
        f"{emit_exp(inner.iter)}, {inner.target.id}, {emit_exp(elt)})"
    )


def emit_list_comprehension_three_generators(
    node: ast.AST,
    elt: ast.expr,
    outer: ast.comprehension,
    middle: ast.comprehension,
    inner: ast.comprehension,
) -> str:
    if outer.is_async or middle.is_async or inner.is_async:
        raise unsupported(node, "async list comprehensions are not supported yet")
    if not (
        isinstance(outer.target, ast.Name)
        and isinstance(middle.target, ast.Name)
        and isinstance(inner.target, ast.Name)
    ):
        if outer.ifs or middle.ifs or inner.ifs:
            return (
                f"#listCompTargetForForIfs({emit_exp(outer.iter)}, {emit_target(outer.target)}, "
                f"{emit_maybe_comp_filters(outer.ifs)}, {emit_exp(middle.iter)}, "
                f"{emit_target(middle.target)}, {emit_maybe_comp_filters(middle.ifs)}, "
                f"{emit_exp(inner.iter)}, {emit_target(inner.target)}, "
                f"{emit_maybe_comp_filters(inner.ifs)}, {emit_exp(elt)})"
            )
        return (
            f"#listCompTargetForFor({emit_exp(outer.iter)}, {emit_target(outer.target)}, "
            f"{emit_exp(middle.iter)}, {emit_target(middle.target)}, "
            f"{emit_exp(inner.iter)}, {emit_target(inner.target)}, {emit_exp(elt)})"
        )
    if outer.ifs or middle.ifs or inner.ifs:
        return (
            f"#listCompForForIfs({emit_exp(outer.iter)}, {outer.target.id}, "
            f"{emit_maybe_comp_filters(outer.ifs)}, {emit_exp(middle.iter)}, "
            f"{middle.target.id}, {emit_maybe_comp_filters(middle.ifs)}, "
            f"{emit_exp(inner.iter)}, {inner.target.id}, "
            f"{emit_maybe_comp_filters(inner.ifs)}, {emit_exp(elt)})"
        )
    return (
        f"#listCompForFor({emit_exp(outer.iter)}, {outer.target.id}, "
        f"{emit_exp(middle.iter)}, {middle.target.id}, "
        f"{emit_exp(inner.iter)}, {inner.target.id}, {emit_exp(elt)})"
    )


def emit_dict_comprehension(
    node: ast.AST, key: ast.expr, value: ast.expr, generator: ast.comprehension
) -> str:
    if generator.is_async:
        raise unsupported(node, "async dict comprehensions are not supported yet")
    if not isinstance(generator.target, ast.Name):
        if generator.ifs:
            return (
                f"#dictCompTargetIfs({emit_exp(generator.iter)}, {emit_target(generator.target)}, "
                f"{emit_comp_filters(generator.ifs)}, {emit_exp(key)}, {emit_exp(value)})"
            )
        return (
            f"#dictCompTarget({emit_exp(generator.iter)}, {emit_target(generator.target)}, "
            f"{emit_exp(key)}, {emit_exp(value)})"
        )
    if len(generator.ifs) > 1:
        return (
            f"#dictCompIfs({emit_exp(generator.iter)}, {generator.target.id}, "
            f"{emit_comp_filters(generator.ifs)}, {emit_exp(key)}, {emit_exp(value)})"
        )
    if generator.ifs:
        return (
            f"#dictCompIf({emit_exp(generator.iter)}, {generator.target.id}, "
            f"{emit_exp(generator.ifs[0])}, {emit_exp(key)}, {emit_exp(value)})"
        )
    return (
        f"#dictComp({emit_exp(generator.iter)}, {generator.target.id}, "
        f"{emit_exp(key)}, {emit_exp(value)})"
    )


def emit_dict_comprehension_two_generators(
    node: ast.AST,
    key: ast.expr,
    value: ast.expr,
    outer: ast.comprehension,
    inner: ast.comprehension,
) -> str:
    if outer.is_async or inner.is_async:
        raise unsupported(node, "async dict comprehensions are not supported yet")
    if not isinstance(outer.target, ast.Name) or not isinstance(inner.target, ast.Name):
        if outer.ifs or inner.ifs:
            return (
                f"#dictCompTargetForIfs({emit_exp(outer.iter)}, {emit_target(outer.target)}, "
                f"{emit_maybe_comp_filters(outer.ifs)}, {emit_exp(inner.iter)}, "
                f"{emit_target(inner.target)}, {emit_maybe_comp_filters(inner.ifs)}, "
                f"{emit_exp(key)}, {emit_exp(value)})"
            )
        return (
            f"#dictCompTargetFor({emit_exp(outer.iter)}, {emit_target(outer.target)}, "
            f"{emit_exp(inner.iter)}, {emit_target(inner.target)}, {emit_exp(key)}, {emit_exp(value)})"
        )
    if outer.ifs or inner.ifs:
        return (
            f"#dictCompForIfs({emit_exp(outer.iter)}, {outer.target.id}, "
            f"{emit_maybe_comp_filters(outer.ifs)}, {emit_exp(inner.iter)}, "
            f"{inner.target.id}, {emit_maybe_comp_filters(inner.ifs)}, "
            f"{emit_exp(key)}, {emit_exp(value)})"
        )
    return (
        f"#dictCompFor({emit_exp(outer.iter)}, {outer.target.id}, "
        f"{emit_exp(inner.iter)}, {inner.target.id}, {emit_exp(key)}, {emit_exp(value)})"
    )


def emit_dict_comprehension_three_generators(
    node: ast.AST,
    key: ast.expr,
    value: ast.expr,
    outer: ast.comprehension,
    middle: ast.comprehension,
    inner: ast.comprehension,
) -> str:
    if outer.is_async or middle.is_async or inner.is_async:
        raise unsupported(node, "async dict comprehensions are not supported yet")
    if not (
        isinstance(outer.target, ast.Name)
        and isinstance(middle.target, ast.Name)
        and isinstance(inner.target, ast.Name)
    ):
        if outer.ifs or middle.ifs or inner.ifs:
            return (
                f"#dictCompTargetForForIfs({emit_exp(outer.iter)}, {emit_target(outer.target)}, "
                f"{emit_maybe_comp_filters(outer.ifs)}, {emit_exp(middle.iter)}, "
                f"{emit_target(middle.target)}, {emit_maybe_comp_filters(middle.ifs)}, "
                f"{emit_exp(inner.iter)}, {emit_target(inner.target)}, "
                f"{emit_maybe_comp_filters(inner.ifs)}, {emit_exp(key)}, {emit_exp(value)})"
            )
        return (
            f"#dictCompTargetForFor({emit_exp(outer.iter)}, {emit_target(outer.target)}, "
            f"{emit_exp(middle.iter)}, {emit_target(middle.target)}, "
            f"{emit_exp(inner.iter)}, {emit_target(inner.target)}, {emit_exp(key)}, {emit_exp(value)})"
        )
    if outer.ifs or middle.ifs or inner.ifs:
        return (
            f"#dictCompForForIfs({emit_exp(outer.iter)}, {outer.target.id}, "
            f"{emit_maybe_comp_filters(outer.ifs)}, {emit_exp(middle.iter)}, "
            f"{middle.target.id}, {emit_maybe_comp_filters(middle.ifs)}, "
            f"{emit_exp(inner.iter)}, {inner.target.id}, "
            f"{emit_maybe_comp_filters(inner.ifs)}, {emit_exp(key)}, {emit_exp(value)})"
        )
    return (
        f"#dictCompForFor({emit_exp(outer.iter)}, {outer.target.id}, "
        f"{emit_exp(middle.iter)}, {middle.target.id}, "
        f"{emit_exp(inner.iter)}, {inner.target.id}, {emit_exp(key)}, {emit_exp(value)})"
    )


def emit_dict_comprehension_many(
    node: ast.AST,
    key: ast.expr,
    value: ast.expr,
    generators: list[ast.comprehension],
) -> str:
    if len(generators) < 4:
        raise unsupported(node, "dict comprehension generator shape is not supported")
    ensure_non_async_comprehension(node, "dict", generators)
    outer = generators[0]
    return (
        f"#dictCompMany({emit_exp(outer.iter)}, {emit_target(outer.target)}, "
        f"{emit_maybe_comp_filters(outer.ifs)}, "
        f"{emit_maybe_comp_clauses(generators[1:])}, {emit_exp(key)}, {emit_exp(value)})"
    )


def emit_set_comprehension(
    node: ast.AST, elt: ast.expr, generator: ast.comprehension
) -> str:
    if generator.is_async:
        raise unsupported(node, "async set comprehensions are not supported yet")
    if not isinstance(generator.target, ast.Name):
        if generator.ifs:
            return (
                f"#setCompTargetIfs({emit_exp(generator.iter)}, {emit_target(generator.target)}, "
                f"{emit_comp_filters(generator.ifs)}, {emit_exp(elt)})"
            )
        return (
            f"#setCompTarget({emit_exp(generator.iter)}, {emit_target(generator.target)}, "
            f"{emit_exp(elt)})"
        )
    if len(generator.ifs) > 1:
        return (
            f"#setCompIfs({emit_exp(generator.iter)}, {generator.target.id}, "
            f"{emit_comp_filters(generator.ifs)}, {emit_exp(elt)})"
        )
    if generator.ifs:
        return (
            f"#setCompIf({emit_exp(generator.iter)}, {generator.target.id}, "
            f"{emit_exp(generator.ifs[0])}, {emit_exp(elt)})"
        )
    return f"#setComp({emit_exp(generator.iter)}, {generator.target.id}, {emit_exp(elt)})"


def emit_set_comprehension_two_generators(
    node: ast.AST, elt: ast.expr, outer: ast.comprehension, inner: ast.comprehension
) -> str:
    if outer.is_async or inner.is_async:
        raise unsupported(node, "async set comprehensions are not supported yet")
    if not isinstance(outer.target, ast.Name) or not isinstance(inner.target, ast.Name):
        if outer.ifs or inner.ifs:
            return (
                f"#setCompTargetForIfs({emit_exp(outer.iter)}, {emit_target(outer.target)}, "
                f"{emit_maybe_comp_filters(outer.ifs)}, {emit_exp(inner.iter)}, "
                f"{emit_target(inner.target)}, {emit_maybe_comp_filters(inner.ifs)}, {emit_exp(elt)})"
            )
        return (
            f"#setCompTargetFor({emit_exp(outer.iter)}, {emit_target(outer.target)}, "
            f"{emit_exp(inner.iter)}, {emit_target(inner.target)}, {emit_exp(elt)})"
        )
    if outer.ifs or inner.ifs:
        return (
            f"#setCompForIfs({emit_exp(outer.iter)}, {outer.target.id}, "
            f"{emit_maybe_comp_filters(outer.ifs)}, {emit_exp(inner.iter)}, "
            f"{inner.target.id}, {emit_maybe_comp_filters(inner.ifs)}, {emit_exp(elt)})"
        )
    return (
        f"#setCompFor({emit_exp(outer.iter)}, {outer.target.id}, "
        f"{emit_exp(inner.iter)}, {inner.target.id}, {emit_exp(elt)})"
    )


def emit_set_comprehension_three_generators(
    node: ast.AST,
    elt: ast.expr,
    outer: ast.comprehension,
    middle: ast.comprehension,
    inner: ast.comprehension,
) -> str:
    if outer.is_async or middle.is_async or inner.is_async:
        raise unsupported(node, "async set comprehensions are not supported yet")
    if not (
        isinstance(outer.target, ast.Name)
        and isinstance(middle.target, ast.Name)
        and isinstance(inner.target, ast.Name)
    ):
        if outer.ifs or middle.ifs or inner.ifs:
            return (
                f"#setCompTargetForForIfs({emit_exp(outer.iter)}, {emit_target(outer.target)}, "
                f"{emit_maybe_comp_filters(outer.ifs)}, {emit_exp(middle.iter)}, "
                f"{emit_target(middle.target)}, {emit_maybe_comp_filters(middle.ifs)}, "
                f"{emit_exp(inner.iter)}, {emit_target(inner.target)}, "
                f"{emit_maybe_comp_filters(inner.ifs)}, {emit_exp(elt)})"
            )
        return (
            f"#setCompTargetForFor({emit_exp(outer.iter)}, {emit_target(outer.target)}, "
            f"{emit_exp(middle.iter)}, {emit_target(middle.target)}, "
            f"{emit_exp(inner.iter)}, {emit_target(inner.target)}, {emit_exp(elt)})"
        )
    if outer.ifs or middle.ifs or inner.ifs:
        return (
            f"#setCompForForIfs({emit_exp(outer.iter)}, {outer.target.id}, "
            f"{emit_maybe_comp_filters(outer.ifs)}, {emit_exp(middle.iter)}, "
            f"{middle.target.id}, {emit_maybe_comp_filters(middle.ifs)}, "
            f"{emit_exp(inner.iter)}, {inner.target.id}, "
            f"{emit_maybe_comp_filters(inner.ifs)}, {emit_exp(elt)})"
        )
    return (
        f"#setCompForFor({emit_exp(outer.iter)}, {outer.target.id}, "
        f"{emit_exp(middle.iter)}, {middle.target.id}, "
        f"{emit_exp(inner.iter)}, {inner.target.id}, {emit_exp(elt)})"
    )


def emit_set_comprehension_many(
    node: ast.AST, elt: ast.expr, generators: list[ast.comprehension]
) -> str:
    if len(generators) < 4:
        raise unsupported(node, "set comprehension generator shape is not supported")
    ensure_non_async_comprehension(node, "set", generators)
    outer = generators[0]
    return (
        f"#setCompMany({emit_exp(outer.iter)}, {emit_target(outer.target)}, "
        f"{emit_maybe_comp_filters(outer.ifs)}, "
        f"{emit_maybe_comp_clauses(generators[1:])}, {emit_exp(elt)})"
    )


def emit_slice_bound(bound: ast.expr | None) -> str:
    if bound is None:
        return "None"
    return emit_exp(bound)


def emit_arg_exp_texts(items: list[str]) -> str:
    if not items:
        return "#noArgs"
    head = items[0]
    if len(items) == 1:
        return f"#arg({head})"
    return f"#args({head}, {emit_arg_exp_texts(items[1:])})"


def emit_kw_defaults(defaults: list[ast.expr | None]) -> str | None:
    if all(default is None for default in defaults):
        return None
    return emit_arg_exp_texts([
        "#kwDefaultMissing" if default is None else emit_exp(default)
        for default in defaults
    ])


def emit_lambda(node: ast.AST, args: ast.arguments, body: ast.expr) -> str:
    if args.kwonlyargs:
        kw_names = [arg.arg for arg in args.kwonlyargs]
        kw_defaults = emit_kw_defaults(args.kw_defaults)
        names = [arg.arg for arg in args.args]
        if args.posonlyargs:
            pos_names = [arg.arg for arg in args.posonlyargs]
            if args.vararg is not None:
                if args.kwarg is not None:
                    if args.defaults or kw_defaults is not None:
                        pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                        kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                        return f"#lambdaPosOnlyVarArgsKwDefaultsKwArgs({emit_id_items(pos_names)}, {emit_id_items(names)}, {pos_defaults}, {args.vararg.arg}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {args.kwarg.arg}, {emit_exp(body)})"
                    return f"#lambdaPosOnlyVarArgsKwOnlyKwArgs({emit_id_items(pos_names)}, {emit_id_items(names)}, {args.vararg.arg}, {emit_id_items(kw_names)}, {args.kwarg.arg}, {emit_exp(body)})"
                if args.defaults or kw_defaults is not None:
                    pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                    kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                    return f"#lambdaPosOnlyVarArgsKwDefaults({emit_id_items(pos_names)}, {emit_id_items(names)}, {pos_defaults}, {args.vararg.arg}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {emit_exp(body)})"
                return f"#lambdaPosOnlyVarArgsKwOnly({emit_id_items(pos_names)}, {emit_id_items(names)}, {args.vararg.arg}, {emit_id_items(kw_names)}, {emit_exp(body)})"
            if args.kwarg is not None:
                if args.defaults or kw_defaults is not None:
                    pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                    kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                    return f"#lambdaPosOnlyKwDefaultsKwArgs({emit_id_items(pos_names)}, {emit_id_items(names)}, {pos_defaults}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {args.kwarg.arg}, {emit_exp(body)})"
                return f"#lambdaPosOnlyKwOnlyKwArgs({emit_id_items(pos_names)}, {emit_id_items(names)}, {emit_id_items(kw_names)}, {args.kwarg.arg}, {emit_exp(body)})"
            if args.defaults or kw_defaults is not None:
                pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                return f"#lambdaPosOnlyKwOnlyDefaults({emit_id_items(pos_names)}, {emit_id_items(names)}, {pos_defaults}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {emit_exp(body)})"
            return f"#lambdaPosOnlyKwOnly({emit_id_items(pos_names)}, {emit_id_items(names)}, {emit_id_items(kw_names)}, {emit_exp(body)})"
        if args.kwarg is not None:
            if args.vararg is not None:
                if args.defaults or kw_defaults is not None:
                    pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                    kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                    return f"#lambdaVarArgsKwDefaultsKwArgs({emit_id_items(names)}, {pos_defaults}, {args.vararg.arg}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {args.kwarg.arg}, {emit_exp(body)})"
                return f"#lambdaVarArgsKwOnlyKwArgs({emit_id_items(names)}, {args.vararg.arg}, {emit_id_items(kw_names)}, {args.kwarg.arg}, {emit_exp(body)})"
            if names:
                if args.defaults or kw_defaults is not None:
                    pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                    kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                    return f"#lambdaPosKwDefaultsKwArgs({emit_id_items(names)}, {pos_defaults}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {args.kwarg.arg}, {emit_exp(body)})"
                return f"#lambdaPosKwOnlyKwArgs({emit_id_items(names)}, {emit_id_items(kw_names)}, {args.kwarg.arg}, {emit_exp(body)})"
            if kw_defaults is not None:
                return f"#lambdaKwDefaultsKwArgs({emit_id_items(kw_names)}, {kw_defaults}, {args.kwarg.arg}, {emit_exp(body)})"
            return f"#lambdaKwOnlyKwArgs({emit_id_items(kw_names)}, {args.kwarg.arg}, {emit_exp(body)})"
        if args.vararg is not None:
            if args.defaults or kw_defaults is not None:
                pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                return f"#lambdaVarArgsKwDefaults({emit_id_items(names)}, {pos_defaults}, {args.vararg.arg}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {emit_exp(body)})"
            return f"#lambdaVarArgsKwOnly({emit_id_items(names)}, {args.vararg.arg}, {emit_id_items(kw_names)}, {emit_exp(body)})"
        if names:
            if args.defaults or kw_defaults is not None:
                pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                return f"#lambdaPosKwDefaults({emit_id_items(names)}, {pos_defaults}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {emit_exp(body)})"
            return f"#lambdaPosKwOnly({emit_id_items(names)}, {emit_id_items(kw_names)}, {emit_exp(body)})"
        if kw_defaults is not None:
            return f"#lambdaKwDefaults({emit_id_items(kw_names)}, {kw_defaults}, {emit_exp(body)})"
        return f"#lambdaKwOnly({emit_id_items(kw_names)}, {emit_exp(body)})"
    names = [arg.arg for arg in args.args]
    if args.posonlyargs:
        if args.kwarg is not None or any(default is not None for default in args.kw_defaults):
            if any(default is not None for default in args.kw_defaults):
                raise unsupported(node, "lambda positional-only parameters are supported only without keyword-only parameters")
        pos_names = [arg.arg for arg in args.posonlyargs]
        if args.kwarg is not None:
            if args.vararg is not None:
                if args.defaults:
                    return f"#lambdaPosOnlyVarKwArgsDefaults({emit_id_items(pos_names)}, {emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {args.vararg.arg}, {args.kwarg.arg}, {emit_exp(body)})"
                return f"#lambdaPosOnlyVarKwArgs({emit_id_items(pos_names)}, {emit_id_items(names)}, {args.vararg.arg}, {args.kwarg.arg}, {emit_exp(body)})"
            if args.defaults:
                return f"#lambdaPosOnlyKwArgsDefaults({emit_id_items(pos_names)}, {emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {args.kwarg.arg}, {emit_exp(body)})"
            return f"#lambdaPosOnlyKwArgs({emit_id_items(pos_names)}, {emit_id_items(names)}, {args.kwarg.arg}, {emit_exp(body)})"
        if args.vararg is not None:
            if args.defaults:
                return f"#lambdaPosOnlyVarArgsDefaults({emit_id_items(pos_names)}, {emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {args.vararg.arg}, {emit_exp(body)})"
            return f"#lambdaPosOnlyVarArgs({emit_id_items(pos_names)}, {emit_id_items(names)}, {args.vararg.arg}, {emit_exp(body)})"
        if args.defaults:
            return f"#lambdaPosOnlyDefaults({emit_id_items(pos_names)}, {emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {emit_exp(body)})"
        return f"#lambdaPosOnly({emit_id_items(pos_names)}, {emit_id_items(names)}, {emit_exp(body)})"
    if args.kwarg is not None:
        if args.posonlyargs or any(default is not None for default in args.kw_defaults):
            raise unsupported(node, "lambda kwargs are supported only without positional-only parameters or keyword-only parameters")
        if args.vararg is not None:
            if args.defaults:
                return f"#lambdaVarKwArgsDefaults({emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {args.vararg.arg}, {args.kwarg.arg}, {emit_exp(body)})"
            return f"#lambdaVarKwArgs({emit_id_items(names)}, {args.vararg.arg}, {args.kwarg.arg}, {emit_exp(body)})"
        if args.defaults:
            return f"#lambdaKwArgsDefaults({emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {args.kwarg.arg}, {emit_exp(body)})"
        return f"#lambdaKwArgs({emit_id_items(names)}, {args.kwarg.arg}, {emit_exp(body)})"
    if (
        args.posonlyargs
        or any(default is not None for default in args.kw_defaults)
    ):
        raise unsupported(node, "lambda positional-only, keyword-only, and kwargs are not supported yet")
    if args.vararg is not None:
        if args.defaults:
            return f"#lambdaVarArgsDefaults({emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {args.vararg.arg}, {emit_exp(body)})"
        return f"#lambdaVarArgs({emit_id_items(names)}, {args.vararg.arg}, {emit_exp(body)})"
    if args.defaults:
        return f"#lambdaDefaults({emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {emit_exp(body)})"
    if len(names) == 1:
        return f"(lambda {names[0]}: {emit_exp(body)})"
    return f"#lambdaArgs({emit_id_items(names)}, {emit_exp(body)})"


def emit_function_def(
    node: ast.AST,
    name: str,
    args: ast.arguments,
    body: list[ast.stmt],
    decorators: list[ast.expr],
    returns: ast.expr | None,
    type_comment: str | None,
) -> str:
    # Python 3.14 annotations are lazy metadata. The current function values do
    # not expose metadata/introspection, so annotations are erased in this subset.
    if type_comment is not None:
        raise unsupported(node, "function type comments are not supported yet")
    doc_value, body_items = split_body_docstring(body)
    body = body_items
    global_names = collect_current_block_global_names(body)
    if global_names:
        if not supported_global_function_signature(args, decorators):
            raise unsupported(node, "global declarations are currently supported only for undecorated ordinary positional functions")
        if current_block_contains_yield(body):
            raise unsupported(node, "global declarations in generator functions are not supported yet")

    def finish(stmt: str) -> str:
        if global_names:
            stmt = f"#functionGlobals({emit_id(name)}, {emit_id_items(global_names)}, {stmt})"
        if doc_value == "None":
            return stmt
        return f"#functionDoc({emit_id(name)}, {doc_value}, {stmt})"

    generator_function = emit_simple_generator_function_def(name, args, body, decorators, returns)
    if generator_function is not None:
        return finish(generator_function)
    if decorators:
        return emit_decorated_function_def(node, name, args, body, decorators)
    if args.kwonlyargs:
        kw_names = [arg.arg for arg in args.kwonlyargs]
        kw_defaults = emit_kw_defaults(args.kw_defaults)
        names = [arg.arg for arg in args.args]
        if args.posonlyargs:
            pos_names = [arg.arg for arg in args.posonlyargs]
            if args.vararg is not None:
                if args.kwarg is not None:
                    if args.defaults or kw_defaults is not None:
                        pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                        kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                        return finish(f"#defPosOnlyVarArgsKwDefaultsKwArgs({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {pos_defaults}, {args.vararg.arg}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {args.kwarg.arg}, {emit_block(body)})")
                    return finish(f"#defPosOnlyVarArgsKwOnlyKwArgs({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {args.vararg.arg}, {emit_id_items(kw_names)}, {args.kwarg.arg}, {emit_block(body)})")
                if args.defaults or kw_defaults is not None:
                    pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                    kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                    return finish(f"#defPosOnlyVarArgsKwDefaults({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {pos_defaults}, {args.vararg.arg}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {emit_block(body)})")
                return finish(f"#defPosOnlyVarArgsKwOnly({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {args.vararg.arg}, {emit_id_items(kw_names)}, {emit_block(body)})")
            if args.kwarg is not None:
                if args.defaults or kw_defaults is not None:
                    pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                    kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                    return finish(f"#defPosOnlyKwDefaultsKwArgs({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {pos_defaults}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {args.kwarg.arg}, {emit_block(body)})")
                return finish(f"#defPosOnlyKwOnlyKwArgs({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {emit_id_items(kw_names)}, {args.kwarg.arg}, {emit_block(body)})")
            if args.defaults or kw_defaults is not None:
                pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                return finish(f"#defPosOnlyKwOnlyDefaults({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {pos_defaults}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {emit_block(body)})")
            return finish(f"#defPosOnlyKwOnly({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {emit_id_items(kw_names)}, {emit_block(body)})")
        if args.kwarg is not None:
            if args.vararg is not None:
                if args.defaults or kw_defaults is not None:
                    pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                    kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                    return finish(f"#defVarArgsKwDefaultsKwArgs({name}, {emit_id_items(names)}, {pos_defaults}, {args.vararg.arg}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {args.kwarg.arg}, {emit_block(body)})")
                return finish(f"#defVarArgsKwOnlyKwArgs({name}, {emit_id_items(names)}, {args.vararg.arg}, {emit_id_items(kw_names)}, {args.kwarg.arg}, {emit_block(body)})")
            if names:
                if args.defaults or kw_defaults is not None:
                    pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                    kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                    return finish(f"#defPosKwDefaultsKwArgs({name}, {emit_id_items(names)}, {pos_defaults}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {args.kwarg.arg}, {emit_block(body)})")
                return finish(f"#defPosKwOnlyKwArgs({name}, {emit_id_items(names)}, {emit_id_items(kw_names)}, {args.kwarg.arg}, {emit_block(body)})")
            if kw_defaults is not None:
                return finish(f"#defKwDefaultsKwArgs({name}, {emit_id_items(kw_names)}, {kw_defaults}, {args.kwarg.arg}, {emit_block(body)})")
            return finish(f"#defKwOnlyKwArgs({name}, {emit_id_items(kw_names)}, {args.kwarg.arg}, {emit_block(body)})")
        if args.vararg is not None:
            if args.defaults or kw_defaults is not None:
                pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                return finish(f"#defVarArgsKwDefaults({name}, {emit_id_items(names)}, {pos_defaults}, {args.vararg.arg}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {emit_block(body)})")
            return finish(f"#defVarArgsKwOnly({name}, {emit_id_items(names)}, {args.vararg.arg}, {emit_id_items(kw_names)}, {emit_block(body)})")
        if names:
            if args.defaults or kw_defaults is not None:
                pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                return finish(f"#defPosKwDefaults({name}, {emit_id_items(names)}, {pos_defaults}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {emit_block(body)})")
            return finish(f"#defPosKwOnly({name}, {emit_id_items(names)}, {emit_id_items(kw_names)}, {emit_block(body)})")
        if kw_defaults is not None:
            return finish(f"#defKwDefaults({name}, {emit_id_items(kw_names)}, {kw_defaults}, {emit_block(body)})")
        return finish(f"#defKwOnly({name}, {emit_id_items(kw_names)}, {emit_block(body)})")
    names = [arg.arg for arg in args.args]
    if args.posonlyargs:
        if args.kwarg is not None or any(default is not None for default in args.kw_defaults):
            if any(default is not None for default in args.kw_defaults):
                raise unsupported(node, "positional-only parameters are supported only without keyword-only parameters")
        pos_names = [arg.arg for arg in args.posonlyargs]
        if args.kwarg is not None:
            if args.vararg is not None:
                if args.defaults:
                    return finish(f"#defPosOnlyVarKwArgsDefaults({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {args.vararg.arg}, {args.kwarg.arg}, {emit_block(body)})")
                return finish(f"#defPosOnlyVarKwArgs({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {args.vararg.arg}, {args.kwarg.arg}, {emit_block(body)})")
            if args.defaults:
                return finish(f"#defPosOnlyKwArgsDefaults({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {args.kwarg.arg}, {emit_block(body)})")
            return finish(f"#defPosOnlyKwArgs({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {args.kwarg.arg}, {emit_block(body)})")
        if args.vararg is not None:
            if args.defaults:
                return finish(f"#defPosOnlyVarArgsDefaults({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {args.vararg.arg}, {emit_block(body)})")
            return finish(f"#defPosOnlyVarArgs({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {args.vararg.arg}, {emit_block(body)})")
        if args.defaults:
            return finish(f"#defPosOnlyDefaults({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {emit_block(body)})")
        return finish(f"#defPosOnly({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {emit_block(body)})")
    if args.kwarg is not None:
        if args.posonlyargs or any(default is not None for default in args.kw_defaults):
            raise unsupported(node, "kwargs are supported only without positional-only parameters or keyword-only parameters")
        if args.vararg is not None:
            if args.defaults:
                return finish(f"#defVarKwArgsDefaults({name}, {emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {args.vararg.arg}, {args.kwarg.arg}, {emit_block(body)})")
            return finish(f"#defVarKwArgs({name}, {emit_id_items(names)}, {args.vararg.arg}, {args.kwarg.arg}, {emit_block(body)})")
        if args.defaults:
            return finish(f"#defKwArgsDefaults({name}, {emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {args.kwarg.arg}, {emit_block(body)})")
        return finish(f"#defKwArgs({name}, {emit_id_items(names)}, {args.kwarg.arg}, {emit_block(body)})")
    if (
        args.posonlyargs
        or any(default is not None for default in args.kw_defaults)
    ):
        raise unsupported(node, "positional-only, keyword-only, and kwargs are not supported yet")
    if args.vararg is not None:
        if args.defaults:
            return finish(f"#defVarArgsDefaults({name}, {emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {args.vararg.arg}, {emit_block(body)})")
        return finish(f"#defVarArgs({name}, {emit_id_items(names)}, {args.vararg.arg}, {emit_block(body)})")
    if args.defaults:
        return finish(f"#defDefaults({name}, {emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {emit_block(body)})")
    if len(names) == 1:
        return finish(f"#def({name}, {names[0]}, {emit_block(body)})")
    return finish(f"#defArgs({name}, {emit_id_items(names)}, {emit_block(body)})")


def emit_async_function_def(
    node: ast.AST,
    name: str,
    args: ast.arguments,
    body: list[ast.stmt],
    decorators: list[ast.expr],
    returns: ast.expr | None,
    type_comment: str | None,
) -> str:
    # Python 3.14 async-function annotations are lazy metadata. The current
    # async profile preserves the declaration as a distinct value but does not
    # expose annotation introspection yet.
    _ = returns
    if type_comment is not None:
        raise unsupported(node, "async function type comments are not supported yet")
    if getattr(node, "type_params", []):
        raise unsupported(node, "async function type parameters are not supported yet")
    if decorators:
        raise unsupported(node, "decorated async functions are not supported yet")
    if (
        args.posonlyargs
        or args.defaults
        or args.vararg is not None
        or args.kwonlyargs
        or any(default is not None for default in args.kw_defaults)
        or args.kwarg is not None
    ):
        raise unsupported(node, "only ordinary positional async functions without defaults are supported yet")
    doc_value, body_items = split_body_docstring(body)
    if current_block_contains_yield(body_items):
        raise unsupported(node, "async generator functions are not supported yet")
    names = [arg.arg for arg in args.args]
    stmt = f"#asyncDef({emit_id(name)}, {emit_id_items(names)}, {emit_block(body_items)})"
    if doc_value == "None":
        return stmt
    return f"#functionDoc({emit_id(name)}, {doc_value}, {stmt})"


def emit_decorated_function_def(
    node: ast.AST,
    name: str,
    args: ast.arguments,
    body: list[ast.stmt],
    decorators: list[ast.expr],
) -> str:
    def value_spec(value: str) -> str:
        return value

    def default_spec(defaults: str, builder: str) -> str:
        return f"#functionDefaultSpec({defaults}, {builder})"

    def two_default_spec(defaults: str, kw_defaults: str, builder: str) -> str:
        return f"#functionTwoDefaultSpec({defaults}, {kw_defaults}, {builder})"

    names = [arg.arg for arg in args.args]
    body_text = emit_block(body)
    if args.kwonlyargs:
        kw_names = [arg.arg for arg in args.kwonlyargs]
        kw_defaults = emit_kw_defaults(args.kw_defaults)
        kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
        if args.posonlyargs:
            pos_names = [arg.arg for arg in args.posonlyargs]
            pos_ids = emit_id_items(pos_names)
            rest_ids = emit_id_items(names)
            kw_ids = emit_id_items(kw_names)
            if args.vararg is not None:
                if args.kwarg is not None:
                    if args.defaults or kw_defaults is not None:
                        pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                        function_value = two_default_spec(
                            pos_defaults,
                            kw_defaults_exp,
                            f"#buildFunctionPosOnlyVarArgsKwDefaultsKwArgs({pos_ids}, {rest_ids}, {args.vararg.arg}, {kw_ids}, {args.kwarg.arg}, {body_text})",
                        )
                    else:
                        function_value = value_spec(
                            f"#functionPosOnlyVarArgsKwOnlyKwArgs({pos_ids}, {rest_ids}, {args.vararg.arg}, {kw_ids}, {args.kwarg.arg}, {body_text})"
                        )
                elif args.defaults or kw_defaults is not None:
                    pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                    function_value = two_default_spec(
                        pos_defaults,
                        kw_defaults_exp,
                        f"#buildFunctionPosOnlyVarArgsKwDefaults({pos_ids}, {rest_ids}, {args.vararg.arg}, {kw_ids}, {body_text})",
                    )
                else:
                    function_value = value_spec(
                        f"#functionPosOnlyVarArgsKwOnly({pos_ids}, {rest_ids}, {args.vararg.arg}, {kw_ids}, {body_text})"
                    )
            elif args.kwarg is not None:
                if args.defaults or kw_defaults is not None:
                    pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                    function_value = two_default_spec(
                        pos_defaults,
                        kw_defaults_exp,
                        f"#buildFunctionPosOnlyKwDefaultsKwArgs({pos_ids}, {rest_ids}, {kw_ids}, {args.kwarg.arg}, {body_text})",
                    )
                else:
                    function_value = value_spec(
                        f"#functionPosOnlyKwOnlyKwArgs({pos_ids}, {rest_ids}, {kw_ids}, {args.kwarg.arg}, {body_text})"
                    )
            elif args.defaults or kw_defaults is not None:
                pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                function_value = two_default_spec(
                    pos_defaults,
                    kw_defaults_exp,
                    f"#buildFunctionPosOnlyKwOnlyDefaults({pos_ids}, {rest_ids}, {kw_ids}, {body_text})",
                )
            else:
                function_value = value_spec(
                    f"#functionPosOnlyKwOnly({pos_ids}, {rest_ids}, {kw_ids}, {body_text})"
                )
        else:
            ids = emit_id_items(names)
            kw_ids = emit_id_items(kw_names)
            if args.kwarg is not None:
                if args.vararg is not None:
                    if args.defaults or kw_defaults is not None:
                        pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                        function_value = two_default_spec(
                            pos_defaults,
                            kw_defaults_exp,
                            f"#buildFunctionVarArgsKwDefaultsKwArgs({ids}, {args.vararg.arg}, {kw_ids}, {args.kwarg.arg}, {body_text})",
                        )
                    else:
                        function_value = value_spec(
                            f"#functionVarArgsKwOnlyKwArgs({ids}, {args.vararg.arg}, {kw_ids}, {args.kwarg.arg}, {body_text})"
                        )
                elif names:
                    if args.defaults or kw_defaults is not None:
                        pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                        function_value = two_default_spec(
                            pos_defaults,
                            kw_defaults_exp,
                            f"#buildFunctionPosKwDefaultsKwArgs({ids}, {kw_ids}, {args.kwarg.arg}, {body_text})",
                        )
                    else:
                        function_value = value_spec(
                            f"#functionPosKwOnlyKwArgs({ids}, {kw_ids}, {args.kwarg.arg}, {body_text})"
                        )
                elif kw_defaults is not None:
                    function_value = default_spec(
                        kw_defaults,
                        f"#buildFunctionKwDefaultsKwArgs({kw_ids}, {args.kwarg.arg}, {body_text})",
                    )
                else:
                    function_value = value_spec(
                        f"#functionKwOnlyKwArgs({kw_ids}, {args.kwarg.arg}, {body_text})"
                    )
            elif args.vararg is not None:
                if args.defaults or kw_defaults is not None:
                    pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                    function_value = two_default_spec(
                        pos_defaults,
                        kw_defaults_exp,
                        f"#buildFunctionVarArgsKwDefaults({ids}, {args.vararg.arg}, {kw_ids}, {body_text})",
                    )
                else:
                    function_value = value_spec(
                        f"#functionVarArgsKwOnly({ids}, {args.vararg.arg}, {kw_ids}, {body_text})"
                    )
            elif names:
                if args.defaults or kw_defaults is not None:
                    pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                    function_value = two_default_spec(
                        pos_defaults,
                        kw_defaults_exp,
                        f"#buildFunctionPosKwDefaults({ids}, {kw_ids}, {body_text})",
                    )
                else:
                    function_value = value_spec(
                        f"#functionPosKwOnly({ids}, {kw_ids}, {body_text})"
                    )
            elif kw_defaults is not None:
                function_value = default_spec(
                    kw_defaults,
                    f"#buildFunctionKwDefaults({kw_ids}, {body_text})",
                )
            else:
                function_value = value_spec(f"#functionKwOnly({kw_ids}, {body_text})")
    elif args.posonlyargs:
        pos_names = [arg.arg for arg in args.posonlyargs]
        pos_ids = emit_id_items(pos_names)
        rest_ids = emit_id_items(names)
        if args.kwarg is not None:
            if args.vararg is not None:
                if args.defaults:
                    function_value = default_spec(
                        emit_arg_exps(args.defaults),
                        f"#buildFunctionPosOnlyVarKwArgsDefaults({pos_ids}, {rest_ids}, {args.vararg.arg}, {args.kwarg.arg}, {body_text})",
                    )
                else:
                    function_value = value_spec(
                        f"#functionPosOnlyVarKwArgs({pos_ids}, {rest_ids}, {args.vararg.arg}, {args.kwarg.arg}, {body_text})"
                    )
            elif args.defaults:
                function_value = default_spec(
                    emit_arg_exps(args.defaults),
                    f"#buildFunctionPosOnlyKwArgsDefaults({pos_ids}, {rest_ids}, {args.kwarg.arg}, {body_text})",
                )
            else:
                function_value = value_spec(
                    f"#functionPosOnlyKwArgs({pos_ids}, {rest_ids}, {args.kwarg.arg}, {body_text})"
                )
        elif args.vararg is not None:
            if args.defaults:
                function_value = default_spec(
                    emit_arg_exps(args.defaults),
                    f"#buildFunctionPosOnlyVarArgsDefaults({pos_ids}, {rest_ids}, {args.vararg.arg}, {body_text})",
                )
            else:
                function_value = value_spec(
                    f"#functionPosOnlyVarArgs({pos_ids}, {rest_ids}, {args.vararg.arg}, {body_text})"
                )
        elif args.defaults:
            function_value = default_spec(
                emit_arg_exps(args.defaults),
                f"#buildFunctionPosOnlyDefaults({pos_ids}, {rest_ids}, {body_text})",
            )
        else:
            function_value = value_spec(
                f"#functionPosOnly({pos_ids}, {rest_ids}, {body_text})"
            )
    elif args.kwarg is not None:
        ids = emit_id_items(names)
        if args.vararg is not None:
            if args.defaults:
                function_value = default_spec(
                    emit_arg_exps(args.defaults),
                    f"#buildFunctionVarKwArgsDefaults({ids}, {args.vararg.arg}, {args.kwarg.arg}, {body_text})",
                )
            else:
                function_value = value_spec(
                    f"#functionVarKwArgs({ids}, {args.vararg.arg}, {args.kwarg.arg}, {body_text})"
                )
        elif args.defaults:
            function_value = default_spec(
                emit_arg_exps(args.defaults),
                f"#buildFunctionKwArgsDefaults({ids}, {args.kwarg.arg}, {body_text})",
            )
        else:
            function_value = value_spec(
                f"#functionKwArgs({ids}, {args.kwarg.arg}, {body_text})"
            )
    elif args.vararg is not None:
        ids = emit_id_items(names)
        if args.defaults:
            function_value = default_spec(
                emit_arg_exps(args.defaults),
                f"#buildFunctionVarArgsDefaults({ids}, {args.vararg.arg}, {body_text})",
            )
        else:
            function_value = value_spec(
                f"#functionVarArgs({ids}, {args.vararg.arg}, {body_text})"
            )
    elif args.defaults:
        function_value = f"#functionDefaults({emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {body_text})"
    elif len(names) == 1:
        function_value = f"#function({names[0]}, {body_text})"
    else:
        function_value = f"#functionArgs({emit_id_items(names)}, {body_text})"
    return f"#defDecorated({name}, {emit_arg_exps(decorators)}, {function_value})"


def emit_for_stmt(
    node: ast.AST,
    target: ast.expr,
    iter_: ast.expr,
    body: list[ast.stmt],
    orelse: list[ast.stmt],
) -> str:
    if isinstance(target, ast.Name):
        if not orelse:
            return f"#for({target.id}, {emit_exp(iter_)}, {emit_block(body)})"
        return f"#forElse({target.id}, {emit_exp(iter_)}, {emit_block(body)}, {emit_block(orelse)})"
    if isinstance(target, ast.Tuple | ast.List):
        if target_contains_star(target):
            emitted_target = emit_target(target)
            if not orelse:
                return f"#forTarget({emitted_target}, {emit_exp(iter_)}, {emit_block(body)})"
            return f"#forTargetElse({emitted_target}, {emit_exp(iter_)}, {emit_block(body)}, {emit_block(orelse)})"
        star_parts = emit_starred_target_parts(target, "for")
        if star_parts is not None:
            prefix, star, suffix = star_parts
            if not orelse:
                return (
                    f"#forStarUnpack({emit_id_items(prefix)}, {star}, {emit_id_items(suffix)}, "
                    f"{emit_exp(iter_)}, {emit_block(body)})"
                )
            return (
                f"#forStarUnpackElse({emit_id_items(prefix)}, {star}, {emit_id_items(suffix)}, "
                f"{emit_exp(iter_)}, {emit_block(body)}, {emit_block(orelse)})"
            )
        if target_contains_nested(target):
            targets = emit_targets_from_sequence(target)
            if not orelse:
                return f"#forTargetUnpack({targets}, {emit_exp(iter_)}, {emit_block(body)})"
            return f"#forTargetUnpackElse({targets}, {emit_exp(iter_)}, {emit_block(body)}, {emit_block(orelse)})"
        ids = emit_id_items(emit_flat_target_names(target))
        if not orelse:
            return f"#forUnpack({ids}, {emit_exp(iter_)}, {emit_block(body)})"
        return f"#forUnpackElse({ids}, {emit_exp(iter_)}, {emit_block(body)}, {emit_block(orelse)})"
    raise unsupported(node, "only simple-name and flat/starred sequence for targets are supported")


def emit_with_stmt(node: ast.AST, items: list[ast.withitem], body: list[ast.stmt]) -> str:
    if not items:
        raise unsupported(node, "with statements require at least one context manager")
    if len(items) == 1:
        item = items[0]
        if item.optional_vars is None:
            return f"#with({emit_exp(item.context_expr)}, {emit_block(body)})"
        if isinstance(item.optional_vars, ast.Name):
            return f"#withAs({emit_exp(item.context_expr)}, {emit_id(item.optional_vars.id)}, {emit_block(body)})"
        if isinstance(item.optional_vars, ast.Tuple | ast.List):
            return f"#withAsTarget({emit_exp(item.context_expr)}, {emit_target(item.optional_vars)}, {emit_block(body)})"
        raise unsupported(node, "with-as targets currently support only simple names and sequence targets")
    return f"#withMany({emit_with_items(node, items)}, {emit_block(body)})"


def emit_with_items(node: ast.AST, items: list[ast.withitem]) -> str:
    head = emit_with_item(node, items[0])
    if len(items) == 1:
        return f"#withOne({head})"
    return f"#withItems({head}, {emit_with_items(node, items[1:])})"


def emit_with_item(node: ast.AST, item: ast.withitem) -> str:
    if item.optional_vars is None:
        return f"#withItem({emit_exp(item.context_expr)})"
    if isinstance(item.optional_vars, ast.Name):
        return f"#withItemAs({emit_exp(item.context_expr)}, {emit_id(item.optional_vars.id)})"
    if isinstance(item.optional_vars, ast.Tuple | ast.List):
        return f"#withItemAsTarget({emit_exp(item.context_expr)}, {emit_target(item.optional_vars)})"
    raise unsupported(node, "with-as targets currently support only simple names and sequence targets")


def emit_assign(node: ast.AST, targets: list[ast.expr], value: ast.expr) -> str:
    if len(targets) == 1:
        target = targets[0]
        if isinstance(target, ast.Name):
            if target.id == "Ellipsis":
                return f"#assignName({ELLIPSIS_NAME_ID}, {emit_exp(value)})"
            return f"{emit_id(target.id)} = {emit_exp(value)}"
        if isinstance(target, ast.Attribute) and isinstance(target.ctx, ast.Store):
            return f"#assignAttr({emit_exp(target.value)}, {emit_id(target.attr)}, {emit_exp(value)})"
        if (
            isinstance(target, ast.Subscript)
            and isinstance(target.value, ast.Name)
            and isinstance(target.slice, ast.Slice)
        ):
            if target.slice.step is not None:
                return (
                    f"#sliceStepAssign({emit_id(target.value.id)}, "
                    f"{emit_slice_bound(target.slice.lower)}, "
                    f"{emit_slice_bound(target.slice.upper)}, "
                    f"{emit_exp(target.slice.step)}, {emit_exp(value)})"
                )
            return (
                f"#sliceAssign({emit_id(target.value.id)}, "
                f"{emit_slice_bound(target.slice.lower)}, "
                f"{emit_slice_bound(target.slice.upper)}, {emit_exp(value)})"
            )
        if (
            isinstance(target, ast.Subscript)
            and isinstance(target.value, ast.Name)
            and not isinstance(target.slice, ast.Slice)
        ):
            return (
                f"#subscriptAssign({emit_id(target.value.id)}, "
                f"{emit_exp(target.slice)}, {emit_exp(value)})"
            )
        if (
            isinstance(target, ast.Subscript)
            and isinstance(target.value, ast.Subscript)
            and isinstance(target.value.value, ast.Name)
            and not isinstance(target.value.slice, ast.Slice)
            and not isinstance(target.slice, ast.Slice)
        ):
            return (
                f"#subscriptAssign2({emit_id(target.value.value.id)}, "
                f"{emit_exp(target.value.slice)}, {emit_exp(target.slice)}, {emit_exp(value)})"
            )
        if isinstance(target, ast.Tuple | ast.List):
            return emit_sequence_assign(target, value)
        raise unsupported(target, "only simple-name, simple attribute, simple-name subscript/slice, two-level simple-name subscript, and flat/starred sequence assignment targets are supported")

    names: list[str] = []
    for target in targets:
        if not isinstance(target, ast.Name):
            raise unsupported(target, "only simple-name chained assignment targets are supported")
        names.append(target.id)
    if len(names) < 1:
        raise unsupported(node, "assignment needs at least one target")
    return f"#assignMany({emit_id_items(names)}; {emit_exp(value)})"


def emit_ann_assign(node: ast.AST, target: ast.expr, value: ast.expr | None) -> str:
    if not isinstance(target, ast.Name):
        raise unsupported(target, "only simple-name annotated assignment targets are supported")
    if value is None:
        return f"#annOnly({emit_id(target.id)})"
    return f"#annAssign({emit_id(target.id)}, {emit_exp(value)})"


def emit_type_alias(
    node: ast.AST,
    name: ast.expr,
    type_params: list[ast.type_param],
    value: ast.expr,
) -> str:
    if not isinstance(name, ast.Name):
        raise unsupported(node, "type alias targets currently support only simple names")
    if type_params:
        raise unsupported(node, "generic type aliases are not supported yet")
    return f"#typeAlias({emit_id(name.id)}, {emit_exp(value)})"


def emit_delete(node: ast.AST, targets: list[ast.expr]) -> str:
    if len(targets) == 1:
        target = targets[0]
        if isinstance(target, ast.Attribute) and isinstance(target.ctx, ast.Del):
            return f"#delAttr({emit_exp(target.value)}, {emit_id(target.attr)})"
        if (
            isinstance(target, ast.Subscript)
            and isinstance(target.value, ast.Name)
            and isinstance(target.slice, ast.Slice)
        ):
            if target.slice.step is not None:
                return (
                    f"#delSliceStep({emit_id(target.value.id)}, "
                    f"{emit_slice_bound(target.slice.lower)}, "
                    f"{emit_slice_bound(target.slice.upper)}, {emit_exp(target.slice.step)})"
                )
            return (
                f"#delSlice({emit_id(target.value.id)}, "
                f"{emit_slice_bound(target.slice.lower)}, {emit_slice_bound(target.slice.upper)})"
            )
        if (
            isinstance(target, ast.Subscript)
            and isinstance(target.value, ast.Name)
            and not isinstance(target.slice, ast.Slice)
        ):
            return f"#delSubscript({emit_id(target.value.id)}, {emit_exp(target.slice)})"
        if (
            isinstance(target, ast.Subscript)
            and isinstance(target.value, ast.Subscript)
            and isinstance(target.value.value, ast.Name)
            and not isinstance(target.value.slice, ast.Slice)
            and not isinstance(target.slice, ast.Slice)
        ):
            return (
                f"#delSubscript2({emit_id(target.value.value.id)}, "
                f"{emit_exp(target.value.slice)}, {emit_exp(target.slice)})"
            )

    names: list[str] = []
    for target in targets:
        if not isinstance(target, ast.Name):
            raise unsupported(target, "only simple-name, attribute, single simple-name subscript/slice, and two-level simple-name subscript delete targets are supported")
        names.append(target.id)
    if len(names) < 1:
        raise unsupported(node, "delete statement needs at least one target")
    return f"#delMany({emit_id_items(names)})"


def emit_sequence_assign(target: ast.Tuple | ast.List, value: ast.expr) -> str:
    if target_contains_star(target):
        return f"#targetAssign({emit_target(target)}; {emit_exp(value)})"
    star_parts = emit_starred_target_parts(target, "assignment")
    if star_parts is None:
        if target_contains_nested(target):
            return f"#unpackTargetAssign({emit_targets_from_sequence(target)}; {emit_exp(value)})"
        return f"#unpackAssign({emit_id_items(emit_flat_target_names(target))}; {emit_exp(value)})"
    prefix, star, suffix = star_parts
    return (
        f"#unpackStarAssign({emit_id_items(prefix)}; {star}; "
        f"{emit_id_items(suffix)}; {emit_exp(value)})"
    )


def emit_starred_target_parts(
    target: ast.Tuple | ast.List,
    context: str,
) -> tuple[list[str], str, list[str]] | None:
    star_indexes = [index for index, elt in enumerate(target.elts) if isinstance(elt, ast.Starred)]
    if not star_indexes:
        return None
    if len(star_indexes) > 1:
        raise unsupported(target.elts[star_indexes[1]], f"only one starred {context} target is allowed")

    star_index = star_indexes[0]
    star = target.elts[star_index]
    if not isinstance(star, ast.Starred) or not isinstance(star.value, ast.Name):
        raise unsupported(star, f"only simple-name starred {context} targets are supported")

    prefix = emit_flat_target_names_from_elts(target.elts[:star_index])
    suffix = emit_flat_target_names_from_elts(target.elts[star_index + 1 :])
    return prefix, star.value.id, suffix


def target_contains_nested(target: ast.Tuple | ast.List) -> bool:
    return any(isinstance(elt, ast.Tuple | ast.List) for elt in target.elts)


def target_contains_star(target: ast.expr) -> bool:
    if isinstance(target, ast.Starred):
        return True
    if isinstance(target, ast.Tuple | ast.List):
        return any(target_contains_star(elt) for elt in target.elts)
    return False


def emit_targets_from_sequence(target: ast.Tuple | ast.List) -> str:
    if not target.elts:
        raise unsupported(target, "empty sequence assignment targets are not supported yet")
    return emit_targets(target.elts)


def emit_maybe_targets(elts: list[ast.expr]) -> str:
    if not elts:
        return "#noTargets"
    return f"#targets({emit_targets(elts)})"


def emit_targets(elts: list[ast.expr]) -> str:
    head = emit_target(elts[0])
    if len(elts) == 1:
        return f"#targetLast({head})"
    return f"#targetCons({head}, {emit_targets(elts[1:])})"


def emit_target(target: ast.expr) -> str:
    if isinstance(target, ast.Name):
        return f"#targetName({target.id})"
    if isinstance(target, ast.Starred):
        raise unsupported(target, "starred nested sequence assignment targets are not supported yet")
    if isinstance(target, ast.Tuple | ast.List):
        star_indexes = [index for index, elt in enumerate(target.elts) if isinstance(elt, ast.Starred)]
        if len(star_indexes) > 1:
            raise unsupported(target.elts[star_indexes[1]], "only one starred target is allowed in a target list")
        if star_indexes:
            star_index = star_indexes[0]
            star = target.elts[star_index]
            if not isinstance(star, ast.Starred) or not isinstance(star.value, ast.Name):
                raise unsupported(star, "only simple-name starred targets are supported")
            return (
                f"#targetStarSeq({emit_maybe_targets(target.elts[:star_index])}; "
                f"{star.value.id}; {emit_maybe_targets(target.elts[star_index + 1:])})"
            )
        return f"#targetSeq({emit_targets_from_sequence(target)})"
    raise unsupported(target, "only simple-name and nested sequence assignment targets are supported")


def emit_flat_target_names(target: ast.Tuple | ast.List) -> list[str]:
    names = emit_flat_target_names_from_elts(target.elts)
    if not names:
        raise unsupported(target, "empty sequence assignment targets are not supported yet")
    return names


def emit_flat_target_names_from_elts(elts: list[ast.expr]) -> list[str]:
    names: list[str] = []
    for elt in elts:
        if not isinstance(elt, ast.Name):
            raise unsupported(elt, "only flat name sequence assignment targets are supported")
        names.append(elt.id)
    return names


def emit_id_items(names: list[str]) -> str:
    if not names:
        return "#noIds"
    if len(names) == 1:
        return f"#id({emit_id(names[0])})"
    return f"#ids({emit_id(names[0])}, {emit_id_items(names[1:])})"


def emit_arg_exps(args: list[ast.expr]) -> str:
    if not args:
        return "#noArgs"
    head = args[0]
    if isinstance(head, ast.Starred):
        if len(args) == 1:
            return f"#starArg({emit_exp(head.value)})"
        return f"#starArgs({emit_exp(head.value)}, {emit_arg_exps(args[1:])})"
    if len(args) == 1:
        return f"#arg({emit_exp(head)})"
    return f"#args({emit_exp(head)}, {emit_arg_exps(args[1:])})"


def emit_kw_arg_exps(node: ast.AST, keywords: list[ast.keyword]) -> str:
    if not keywords:
        return "#noKwArgs"
    keyword = keywords[0]
    if keyword.arg is None:
        if len(keywords) == 1:
            return f"#kwStarArg({emit_exp(keyword.value)})"
        return f"#kwStarArgs({emit_exp(keyword.value)}, {emit_kw_arg_exps(node, keywords[1:])})"
    if len(keywords) == 1:
        return f"#kwArg({keyword.arg}, {emit_exp(keyword.value)})"
    return f"#kwArgs({keyword.arg}, {emit_exp(keyword.value)}, {emit_kw_arg_exps(node, keywords[1:])})"


def emit_dict_ctor_keywords(
    node: ast.AST, base: ast.expr | None, keywords: list[ast.keyword]
) -> str:
    kws = emit_kw_arg_exps(node, keywords)
    if base is None:
        return f"#dictCtorKw({kws})"
    return f"#dictCtorMixed({emit_exp(base)}, {kws})"


def emit_complex_ctor_keywords(
    node: ast.AST, base: ast.expr | None, keywords: list[ast.keyword]
) -> str:
    kws = emit_kw_arg_exps(node, keywords)
    if base is None:
        return f"#complexCtorKw({kws})"
    return f"#complexCtorMixed({emit_exp(base)}, {kws})"


def emit_list(elts: list[ast.expr]) -> str:
    return f"#list({emit_arg_exps(elts)})"


def emit_tuple(elts: list[ast.expr]) -> str:
    return f"#tuple({emit_arg_exps(elts)})"


def emit_dict(node: ast.AST, keys: list[ast.expr | None], values: list[ast.expr]) -> str:
    pairs: list[tuple[ast.expr | None, ast.expr]] = []
    for key, value in zip(keys, values, strict=True):
        pairs.append((key, value))
    return f"#dict({emit_dict_exps(pairs)})"


def emit_dict_exps(items: list[tuple[ast.expr | None, ast.expr]]) -> str:
    if not items:
        return "#noDictItems"
    key, value = items[0]
    if key is None:
        if len(items) == 1:
            return f"#dictStarItem({emit_exp(value)})"
        return f"#dictStarItems({emit_exp(value)}, {emit_dict_exps(items[1:])})"
    if len(items) == 1:
        return f"#dictItem({emit_exp(key)}, {emit_exp(value)})"
    return f"#dictItems({emit_exp(key)}, {emit_exp(value)}, {emit_dict_exps(items[1:])})"


def emit_set(elts: list[ast.expr]) -> str:
    if not elts:
        raise UnsupportedPythonSubset("empty set displays are not Python syntax; use set()")
    return f"#set({emit_arg_exps(elts)})"


def emit_aug_op(op: ast.operator) -> str:
    if isinstance(op, ast.Add):
        return "+"
    if isinstance(op, ast.Sub):
        return "-"
    if isinstance(op, ast.Mult):
        return "*"
    if isinstance(op, ast.MatMult):
        return "@"
    if isinstance(op, ast.Div):
        return "/"
    if isinstance(op, ast.Mod):
        return "%"
    if isinstance(op, ast.Pow):
        return "**"
    if isinstance(op, ast.LShift):
        return "<<"
    if isinstance(op, ast.RShift):
        return ">>"
    if isinstance(op, ast.BitAnd):
        return "&"
    if isinstance(op, ast.BitXor):
        return "^"
    if isinstance(op, ast.BitOr):
        return "|"
    raise unsupported(op, "augmented assignment operator is not supported")


def emit_aug_op_tag(op: ast.operator) -> str:
    if isinstance(op, ast.Add):
        return "#augAdd"
    if isinstance(op, ast.Sub):
        return "#augSub"
    if isinstance(op, ast.Mult):
        return "#augMul"
    if isinstance(op, ast.MatMult):
        return "#augMatMul"
    if isinstance(op, ast.Div):
        return "#augTrueDiv"
    if isinstance(op, ast.FloorDiv):
        return "#augFloorDiv"
    if isinstance(op, ast.Mod):
        return "#augMod"
    if isinstance(op, ast.Pow):
        return "#augPow"
    if isinstance(op, ast.LShift):
        return "#augLShift"
    if isinstance(op, ast.RShift):
        return "#augRShift"
    if isinstance(op, ast.BitAnd):
        return "#augBitAnd"
    if isinstance(op, ast.BitXor):
        return "#augBitXor"
    if isinstance(op, ast.BitOr):
        return "#augBitOr"
    raise unsupported(op, "augmented assignment operator is not supported")


def emit_binary_op(op: ast.operator) -> str:
    if isinstance(op, ast.Add):
        return "+"
    if isinstance(op, ast.Sub):
        return "-"
    if isinstance(op, ast.Mult):
        return "*"
    if isinstance(op, ast.MatMult):
        return "@"
    if isinstance(op, ast.Pow):
        return "**"
    if isinstance(op, ast.Mod):
        return "%"
    if isinstance(op, ast.LShift):
        return "<<"
    if isinstance(op, ast.RShift):
        return ">>"
    if isinstance(op, ast.BitAnd):
        return "&"
    if isinstance(op, ast.BitXor):
        return "^"
    if isinstance(op, ast.BitOr):
        return "|"
    raise unsupported(op, "binary operator is not supported")


def emit_cmp_op(op: ast.cmpop) -> str:
    if isinstance(op, ast.Lt):
        return "<"
    if isinstance(op, ast.LtE):
        return "<="
    if isinstance(op, ast.Gt):
        return ">"
    if isinstance(op, ast.GtE):
        return ">="
    if isinstance(op, ast.Eq):
        return "=="
    if isinstance(op, ast.NotEq):
        return "!="
    if isinstance(op, ast.In):
        return "in"
    if isinstance(op, ast.NotIn):
        return "not in"
    if isinstance(op, ast.Is):
        return "is"
    if isinstance(op, ast.IsNot):
        return "is not"
    raise unsupported(op, "comparison operator is not supported")


def emit_cmp_op_tag(op: ast.cmpop) -> str:
    if isinstance(op, ast.Lt):
        return "#lt"
    if isinstance(op, ast.LtE):
        return "#le"
    if isinstance(op, ast.Gt):
        return "#gt"
    if isinstance(op, ast.GtE):
        return "#ge"
    if isinstance(op, ast.Eq):
        return "#eq"
    if isinstance(op, ast.NotEq):
        return "#ne"
    if isinstance(op, ast.Is):
        return "#is"
    if isinstance(op, ast.IsNot):
        return "#isNot"
    if isinstance(op, ast.In):
        return "#in"
    if isinstance(op, ast.NotIn):
        return "#notIn"
    raise unsupported(op, "comparison operator is not supported")


def emit_cmp_chain(ops: list[ast.cmpop], comparators: list[ast.expr]) -> str:
    if len(ops) != len(comparators) or not ops:
        raise UnsupportedPythonSubset("comparison chain must have matching operators and comparators")
    op = emit_cmp_op_tag(ops[0])
    comparator = emit_exp(comparators[0])
    if len(ops) == 1:
        return f"#cmpLast({op}, {comparator})"
    return f"#cmpCons({op}, {comparator}, {emit_cmp_chain(ops[1:], comparators[1:])})"


def emit_eval_input(expression: ast.Expression) -> str:
    return f"{emit_exp(expression.body)};"


def main(argv: list[str]) -> int:
    args = argv[1:]
    mode = "exec"
    if args and args[0] == "--mode":
        if len(args) < 2:
            print(f"usage: {argv[0]} [--mode exec|eval|single|interactive] SOURCE.py", file=sys.stderr)
            return 2
        mode = args[1]
        args = args[2:]
    elif args and args[0].startswith("--mode="):
        mode = args[0].split("=", 1)[1]
        args = args[1:]
    if len(args) != 1 or mode not in {"exec", "eval", "single", "interactive"}:
        print(f"usage: {argv[0]} [--mode exec|eval|single|interactive] SOURCE.py", file=sys.stderr)
        return 2
    path = Path(args[0])
    source = path.read_bytes()
    try:
        parse_mode = "single" if mode == "interactive" else mode
        parsed = ast.parse(source, filename=str(path), mode=parse_mode)
        if mode == "exec":
            assert isinstance(parsed, ast.Module)
            print(emit_module(parsed), end="")
        elif mode == "eval":
            assert isinstance(parsed, ast.Expression)
            print(emit_eval_input(parsed), end="")
        else:
            assert isinstance(parsed, ast.Interactive)
            print(emit_interactive_input(parsed), end="")
    except (SyntaxError, UnsupportedPythonSubset) as err:
        print(f"{path}: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
