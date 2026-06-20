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
        case ast.Assert(test=test, msg=msg):
            return f"#assertMsg({emit_exp(test)}, {emit_exp(msg)})"
        case ast.Global(names=[name]):
            return f"global {name}"
        case ast.Global(names=names):
            return f"#globalMany({emit_id_items(names)})"
        case ast.Delete(targets=[ast.Name(id=name)]):
            return f"del {name}"
        case ast.Delete(targets=targets):
            return emit_delete(stmt, targets)
        case ast.Assign(targets=targets, value=value):
            return emit_assign(stmt, targets, value)
        case ast.AugAssign(target=ast.Name(id=name), op=op, value=value):
            if isinstance(op, ast.FloorDiv):
                return f"#floorDivAssign({name}, {emit_exp(value)})"
            return f"{name} {emit_aug_op(op)}= {emit_exp(value)}"
        case ast.AugAssign():
            raise unsupported(stmt, "only simple-name augmented assignment targets are supported")
        case ast.Return(value=None):
            return "return"
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
        case ast.While(test=test, body=body, orelse=orelse):
            return f"#whileElse({emit_exp(test)}, {emit_block(body)}, {emit_block(orelse)})"
        case ast.For(target=target, iter=iter_, body=body, orelse=orelse):
            return emit_for_stmt(stmt, target, iter_, body, orelse)
        case _:
            raise unsupported(stmt, "statement is not supported by the current K subset")


def emit_exp(exp: ast.expr) -> str:
    match exp:
        case ast.Constant(value=value):
            return emit_constant(exp, value)
        case ast.Name(id=name):
            return name
        case ast.NamedExpr(target=ast.Name(id=name), value=value):
            return f"#namedExpr({name}, {emit_exp(value)})"
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
        case ast.Call(func=ast.Name(id="dict"), args=[], keywords=[]):
            return "#dictCtor()"
        case ast.Call(func=ast.Name(id="dict"), args=[arg], keywords=[]):
            return f"#dictCtor({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="set"), args=[], keywords=[]):
            return "#setCtor()"
        case ast.Call(func=ast.Name(id="set"), args=[arg], keywords=[]):
            return f"#setCtor({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="bool"), args=[], keywords=[]):
            return "#boolCtor()"
        case ast.Call(func=ast.Name(id="bool"), args=[arg], keywords=[]):
            return f"#boolCtor({emit_exp(arg)})"
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
        case ast.Call(func=ast.Name(id="min"), args=args, keywords=[]) if len(args) >= 2:
            return f"#minArgs({emit_arg_exps(args)})"
        case ast.Call(func=ast.Name(id="max"), args=[arg], keywords=[]):
            return f"#max({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="max"), args=args, keywords=[]) if len(args) >= 2:
            return f"#maxArgs({emit_arg_exps(args)})"
        case ast.Call(func=ast.Name(id="int"), args=[], keywords=[]):
            return "#intCtor()"
        case ast.Call(func=ast.Name(id="int"), args=[arg], keywords=[]):
            return f"#intCtor({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="float"), args=[], keywords=[]):
            return "#floatCtor()"
        case ast.Call(func=ast.Name(id="float"), args=[arg], keywords=[]):
            return f"#floatCtor({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="abs"), args=[arg], keywords=[]):
            return f"#abs({emit_exp(arg)})"
        case ast.Call(func=ast.Name(id="divmod"), args=[left, right], keywords=[]):
            return f"#divmod({emit_exp(left)}, {emit_exp(right)})"
        case ast.Call(func=ast.Name(id="pow"), args=[base, exponent], keywords=[]):
            return f"#pow({emit_exp(base)}, {emit_exp(exponent)})"
        case ast.Call(func=ast.Name(id="pow"), args=[base, exponent, modulus], keywords=[]):
            return f"#pow({emit_exp(base)}, {emit_exp(exponent)}, {emit_exp(modulus)})"
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
        case ast.ListComp(elt=elt, generators=[generator]):
            return emit_list_comprehension(exp, elt, generator)
        case ast.ListComp():
            raise unsupported(exp, "only one-generator list comprehensions are supported yet")
        case ast.DictComp(key=key, value=value, generators=[generator]):
            return emit_dict_comprehension(exp, key, value, generator)
        case ast.DictComp():
            raise unsupported(exp, "only one-generator dict comprehensions are supported yet")
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
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return repr(value)
    if isinstance(value, str):
        return json.dumps(value)
    raise unsupported(node, f"constant {value!r} is not supported")


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


def emit_list_comprehension(
    node: ast.AST, elt: ast.expr, generator: ast.comprehension
) -> str:
    if generator.is_async:
        raise unsupported(node, "async list comprehensions are not supported yet")
    if len(generator.ifs) > 1:
        raise unsupported(node, "multiple list comprehension if-clauses are not supported yet")
    if not isinstance(generator.target, ast.Name):
        raise unsupported(generator.target, "only simple-name list comprehension targets are supported")
    if generator.ifs:
        return (
            f"#listCompIf({emit_exp(generator.iter)}, {generator.target.id}, "
            f"{emit_exp(generator.ifs[0])}, {emit_exp(elt)})"
        )
    return f"#listComp({emit_exp(generator.iter)}, {generator.target.id}, {emit_exp(elt)})"


def emit_dict_comprehension(
    node: ast.AST, key: ast.expr, value: ast.expr, generator: ast.comprehension
) -> str:
    if generator.is_async:
        raise unsupported(node, "async dict comprehensions are not supported yet")
    if generator.ifs:
        raise unsupported(node, "dict comprehension if-clauses are not supported yet")
    if not isinstance(generator.target, ast.Name):
        raise unsupported(generator.target, "only simple-name dict comprehension targets are supported")
    return (
        f"#dictComp({emit_exp(generator.iter)}, {generator.target.id}, "
        f"{emit_exp(key)}, {emit_exp(value)})"
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
        if args.posonlyargs or args.vararg is not None or args.kwarg is not None:
            raise unsupported(node, "lambda keyword-only parameters are supported only without positional-only parameters, varargs, or kwargs")
        kw_names = [arg.arg for arg in args.kwonlyargs]
        kw_defaults = emit_kw_defaults(args.kw_defaults)
        names = [arg.arg for arg in args.args]
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
        if args.defaults or args.vararg is not None or args.kwarg is not None or any(default is not None for default in args.kw_defaults):
            raise unsupported(node, "lambda positional-only parameters are supported only without defaults, varargs, kwargs, or keyword-only parameters")
        pos_names = [arg.arg for arg in args.posonlyargs]
        return f"#lambdaPosOnly({emit_id_items(pos_names)}, {emit_id_items(names)}, {emit_exp(body)})"
    if args.kwarg is not None:
        if args.posonlyargs or args.vararg is not None or args.defaults or any(default is not None for default in args.kw_defaults):
            raise unsupported(node, "lambda kwargs are supported only without positional-only parameters, defaults, varargs, or keyword-only parameters")
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
    if decorators:
        raise unsupported(decorators[0], "function decorators are not supported yet")
    if returns is not None:
        raise unsupported(returns, "function return annotations are not supported yet")
    if type_comment is not None:
        raise unsupported(node, "function type comments are not supported yet")
    if args.kwonlyargs:
        if args.posonlyargs or args.vararg is not None or args.kwarg is not None:
            raise unsupported(node, "keyword-only parameters are supported only without positional-only parameters, varargs, or kwargs")
        kw_names = [arg.arg for arg in args.kwonlyargs]
        kw_defaults = emit_kw_defaults(args.kw_defaults)
        names = [arg.arg for arg in args.args]
        if names:
            if args.defaults or kw_defaults is not None:
                pos_defaults = emit_arg_exps(args.defaults) if args.defaults else "#noArgs"
                kw_defaults_exp = kw_defaults if kw_defaults is not None else "#noArgs"
                return f"#defPosKwDefaults({name}, {emit_id_items(names)}, {pos_defaults}, {emit_id_items(kw_names)}, {kw_defaults_exp}, {emit_block(body)})"
            return f"#defPosKwOnly({name}, {emit_id_items(names)}, {emit_id_items(kw_names)}, {emit_block(body)})"
        if kw_defaults is not None:
            return f"#defKwDefaults({name}, {emit_id_items(kw_names)}, {kw_defaults}, {emit_block(body)})"
        return f"#defKwOnly({name}, {emit_id_items(kw_names)}, {emit_block(body)})"
    names = [arg.arg for arg in args.args]
    if args.posonlyargs:
        if args.defaults or args.vararg is not None or args.kwarg is not None or any(default is not None for default in args.kw_defaults):
            raise unsupported(node, "positional-only parameters are supported only without defaults, varargs, kwargs, or keyword-only parameters")
        pos_names = [arg.arg for arg in args.posonlyargs]
        return f"#defPosOnly({name}, {emit_id_items(pos_names)}, {emit_id_items(names)}, {emit_block(body)})"
    if args.kwarg is not None:
        if args.posonlyargs or args.vararg is not None or args.defaults or any(default is not None for default in args.kw_defaults):
            raise unsupported(node, "kwargs are supported only without positional-only parameters, defaults, varargs, or keyword-only parameters")
        return f"#defKwArgs({name}, {emit_id_items(names)}, {args.kwarg.arg}, {emit_block(body)})"
    if (
        args.posonlyargs
        or any(default is not None for default in args.kw_defaults)
    ):
        raise unsupported(node, "positional-only, keyword-only, and kwargs are not supported yet")
    if args.vararg is not None:
        if args.defaults:
            return f"#defVarArgsDefaults({name}, {emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {args.vararg.arg}, {emit_block(body)})"
        return f"#defVarArgs({name}, {emit_id_items(names)}, {args.vararg.arg}, {emit_block(body)})"
    if args.defaults:
        return f"#defDefaults({name}, {emit_id_items(names)}, {emit_arg_exps(args.defaults)}, {emit_block(body)})"
    if len(names) == 1:
        return f"#def({name}, {names[0]}, {emit_block(body)})"
    return f"#defArgs({name}, {emit_id_items(names)}, {emit_block(body)})"


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
        ids = emit_id_items(emit_flat_target_names(target))
        if not orelse:
            return f"#forUnpack({ids}, {emit_exp(iter_)}, {emit_block(body)})"
        return f"#forUnpackElse({ids}, {emit_exp(iter_)}, {emit_block(body)}, {emit_block(orelse)})"
    raise unsupported(node, "only simple-name and flat/starred sequence for targets are supported")


def emit_assign(node: ast.AST, targets: list[ast.expr], value: ast.expr) -> str:
    if len(targets) == 1:
        target = targets[0]
        if isinstance(target, ast.Name):
            return f"{target.id} = {emit_exp(value)}"
        if isinstance(target, ast.Tuple | ast.List):
            return emit_sequence_assign(target, value)
        raise unsupported(target, "only simple-name and flat/starred sequence assignment targets are supported")

    names: list[str] = []
    for target in targets:
        if not isinstance(target, ast.Name):
            raise unsupported(target, "only simple-name chained assignment targets are supported")
        names.append(target.id)
    if len(names) < 1:
        raise unsupported(node, "assignment needs at least one target")
    return f"#assignMany({emit_id_items(names)}; {emit_exp(value)})"


def emit_delete(node: ast.AST, targets: list[ast.expr]) -> str:
    names: list[str] = []
    for target in targets:
        if not isinstance(target, ast.Name):
            raise unsupported(target, "only simple-name delete targets are supported")
        names.append(target.id)
    if len(names) < 1:
        raise unsupported(node, "delete statement needs at least one target")
    return f"#delMany({emit_id_items(names)})"


def emit_sequence_assign(target: ast.Tuple | ast.List, value: ast.expr) -> str:
    star_parts = emit_starred_target_parts(target, "assignment")
    if star_parts is None:
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
        return f"#id({names[0]})"
    return f"#ids({names[0]}, {emit_id_items(names[1:])})"


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
