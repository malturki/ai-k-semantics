import importlib
import types
from types import NotImplementedType as NIT


def mark_type_error(thunk):
    try:
        thunk()
    except TypeError:
        return True
    return False


T = types.NotImplementedType
C = type(NotImplemented)
M = importlib.import_module("types")


def call_with_argument():
    T(1)


result = (
    C is T
    and C == T
    and T is NIT
    and M.NotImplementedType is T
    and isinstance(NotImplemented, T)
    and issubclass(C, T)
    and T() is NotImplemented
    and bool(T)
    and str(T) == "<class 'NotImplementedType'>"
    and repr(T) == "<class 'NotImplementedType'>"
    and ascii(T) == "<class 'NotImplementedType'>"
    and hash(NotImplemented) == hash(NotImplemented)
    and {NotImplemented: 1}[NotImplemented] == 1
    and {T: 2}[T] == 2
    and mark_type_error(call_with_argument)
)

result
