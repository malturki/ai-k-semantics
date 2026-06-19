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
import sys
from pathlib import Path


class UnsupportedPythonSubset(ValueError):
    """Raised when the current K semantics has no faithful target construct."""


def unsupported(node: ast.AST, message: str) -> UnsupportedPythonSubset:
    location = ""
    lineno = getattr(node, "lineno", None)
    col = getattr(node, "col_offset", None)
    if lineno is not None and col is not None:
        location = f" at line {lineno}, column {col}"
    return UnsupportedPythonSubset(f"{message}{location}: {node.__class__.__name__}")


def emit_module(module: ast.Module) -> str:
    return emit_stmt_list(module.body) + "\n"


def emit_stmt_list(stmts: list[ast.stmt]) -> str:
    return "\n".join(f"{emit_stmt(stmt)};" for stmt in stmts)


def emit_block(stmts: list[ast.stmt]) -> str:
    if not stmts:
        return "{}"
    return "{\n" + emit_stmt_list(stmts) + "\n}"


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
        case ast.Assert(msg=msg):
            raise unsupported(msg, "assert messages are not supported yet")
        case ast.Global(names=[name]):
            return f"global {name}"
        case ast.Global():
            raise unsupported(stmt, "only one name per global statement is supported")
        case ast.Delete(targets=[ast.Name(id=name)]):
            return f"del {name}"
        case ast.Delete():
            raise unsupported(stmt, "only simple-name del is supported")
        case ast.Assign(targets=[ast.Name(id=name)], value=value):
            return f"{name} = {emit_exp(value)}"
        case ast.Assign():
            raise unsupported(stmt, "only single-target simple-name assignment is supported")
        case ast.AugAssign(target=ast.Name(id=name), op=op, value=value):
            return f"{name} {emit_aug_op(op)}= {emit_exp(value)}"
        case ast.AugAssign():
            raise unsupported(stmt, "only simple-name +=, -=, and *= are supported")
        case ast.Return(value=None):
            return "return None"
        case ast.Return(value=value):
            return f"return {emit_exp(value)}"
        case ast.FunctionDef(
            name=name,
            args=args,
            body=body,
            decorator_list=decorators,
            returns=returns,
            type_comment=type_comment,
        ):
            return emit_function_def(stmt, name, args, body, decorators, returns, type_comment)
        case ast.If(test=test, body=body, orelse=orelse):
            return f"#if({emit_exp(test)}, {emit_block(body)}, {emit_block(orelse)})"
        case ast.While(test=test, body=body, orelse=[]):
            return f"#while({emit_exp(test)}, {emit_block(body)})"
        case ast.While(orelse=orelse):
            raise unsupported(orelse[0], "while else clauses are not supported yet")
        case ast.For(target=ast.Name(id=name), iter=iter_, body=body, orelse=[]):
            return f"#for({name}, {emit_exp(iter_)}, {emit_block(body)})"
        case ast.For(orelse=[first, *_]):
            raise unsupported(first, "for else clauses are not supported yet")
        case ast.For():
            raise unsupported(stmt, "only simple-name for targets are supported")
        case _:
            raise unsupported(stmt, "statement is not supported by the current K subset")


def emit_exp(exp: ast.expr) -> str:
    match exp:
        case ast.Constant(value=value):
            return emit_constant(exp, value)
        case ast.Name(id=name):
            return name
        case ast.BinOp(left=left, op=op, right=right):
            return emit_bin_op(left, op, right)
        case ast.UnaryOp(op=op, operand=operand):
            return emit_unary_op(op, operand)
        case ast.BoolOp(op=op, values=values):
            return emit_bool_op(exp, op, values)
        case ast.Compare(left=left, ops=[op], comparators=[right]):
            return f"({emit_exp(left)} {emit_cmp_op(op)} {emit_exp(right)})"
        case ast.Compare():
            raise unsupported(exp, "chained comparisons are not supported yet")
        case ast.IfExp(test=test, body=body, orelse=orelse):
            return f"({emit_exp(body)} if {emit_exp(test)} else {emit_exp(orelse)})"
        case ast.Lambda(args=args, body=body):
            return emit_lambda(exp, args, body)
        case ast.Call(func=func, args=[arg], keywords=[]):
            return f"({emit_exp(func)}({emit_exp(arg)}))"
        case ast.Call():
            raise unsupported(exp, "only one positional argument and no keywords are supported")
        case ast.List(elts=elts, ctx=ast.Load()):
            return emit_list(elts)
        case ast.Tuple(elts=elts, ctx=ast.Load()):
            return emit_tuple(elts)
        case ast.Dict(keys=keys, values=values):
            return emit_dict(exp, keys, values)
        case ast.Set(elts=elts):
            return emit_set(elts)
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
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        return json.dumps(value)
    raise unsupported(node, f"constant {value!r} is not supported")


def emit_bin_op(left: ast.expr, op: ast.operator, right: ast.expr) -> str:
    left_text = emit_exp(left)
    right_text = emit_exp(right)
    if isinstance(op, ast.FloorDiv):
        return f"#floorDiv({left_text}, {right_text})"
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


def emit_lambda(node: ast.AST, args: ast.arguments, body: ast.expr) -> str:
    if (
        args.posonlyargs
        or args.kwonlyargs
        or args.kw_defaults
        or args.defaults
        or args.vararg is not None
        or args.kwarg is not None
        or len(args.args) != 1
    ):
        raise unsupported(node, "only a single positional lambda parameter is supported")
    return f"(lambda {args.args[0].arg}: {emit_exp(body)})"


def emit_function_def(
    node: ast.AST,
    name: str,
    args: ast.arguments,
    body: list[ast.stmt],
    decorators: list[ast.expr],
    returns: ast.expr | None,
    type_comment: str | None,
) -> str:
    if decorators:
        raise unsupported(decorators[0], "function decorators are not supported yet")
    if returns is not None:
        raise unsupported(returns, "function return annotations are not supported yet")
    if type_comment is not None:
        raise unsupported(node, "function type comments are not supported yet")
    if (
        args.posonlyargs
        or args.kwonlyargs
        or args.kw_defaults
        or args.defaults
        or args.vararg is not None
        or args.kwarg is not None
        or len(args.args) != 1
    ):
        raise unsupported(node, "only one positional function parameter is supported")
    return f"#def({name}, {args.args[0].arg}, {emit_block(body)})"


def emit_list(elts: list[ast.expr]) -> str:
    if not elts:
        return "[]"
    return "[" + ", ".join(emit_val_exp(elt) for elt in elts) + ",]"


def emit_tuple(elts: list[ast.expr]) -> str:
    if not elts:
        return "()"
    return "(" + ", ".join(emit_val_exp(elt) for elt in elts) + ",)"


def emit_val_exp(exp: ast.expr) -> str:
    match exp:
        case ast.Constant(value=value):
            return emit_constant(exp, value)
        case ast.List(elts=elts, ctx=ast.Load()):
            return emit_list(elts)
        case ast.Tuple(elts=elts, ctx=ast.Load()):
            return emit_tuple(elts)
        case ast.Dict(keys=keys, values=values):
            return emit_dict(exp, keys, values)
        case ast.Set(elts=elts):
            return emit_set(elts)
        case _:
            raise unsupported(exp, "container displays currently support only value elements")


def emit_dict(node: ast.AST, keys: list[ast.expr | None], values: list[ast.expr]) -> str:
    if not keys:
        return "{}"
    items: list[str] = []
    for key, value in zip(keys, values, strict=True):
        if key is None:
            raise unsupported(node, "dictionary unpacking is not supported yet")
        items.append(f"{emit_val_exp(key)}: {emit_val_exp(value)}")
    return "{" + ", ".join(items) + ",}"


def emit_set(elts: list[ast.expr]) -> str:
    if not elts:
        raise UnsupportedPythonSubset("empty set displays are not Python syntax; set() is not supported yet")
    return "{" + ", ".join(emit_val_exp(elt) for elt in elts) + ",}"


def emit_aug_op(op: ast.operator) -> str:
    if isinstance(op, ast.Add):
        return "+"
    if isinstance(op, ast.Sub):
        return "-"
    if isinstance(op, ast.Mult):
        return "*"
    raise unsupported(op, "augmented assignment operator is not supported")


def emit_binary_op(op: ast.operator) -> str:
    if isinstance(op, ast.Add):
        return "+"
    if isinstance(op, ast.Sub):
        return "-"
    if isinstance(op, ast.Mult):
        return "*"
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
    raise unsupported(op, "comparison operator is not supported")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"usage: {argv[0]} SOURCE.py", file=sys.stderr)
        return 2
    path = Path(argv[1])
    source = path.read_text(encoding="utf-8")
    try:
        module = ast.parse(source, filename=str(path), mode="exec")
        print(emit_module(module), end="")
    except (SyntaxError, UnsupportedPythonSubset) as err:
        print(f"{path}: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
