import importlib
import types
from types import EllipsisType as ET
from types import NoneType as NT
from types import NotImplementedType as NIT


def mark_type_error(thunk):
    try:
        thunk()
    except TypeError:
        return True
    return False


none_type = types.NoneType
ellipsis_type = types.EllipsisType
notimplemented_type = types.NotImplementedType
module = importlib.import_module("types")
none_class = type(None)
ellipsis_class = type(...)
notimplemented_class = type(NotImplemented)


def none_with_argument():
    none_type(1)


def ellipsis_with_argument():
    ellipsis_type(1)


def notimplemented_with_argument():
    notimplemented_type(1)


result = (
    none_class is none_type
    and ellipsis_class is ellipsis_type
    and notimplemented_class is notimplemented_type
    and none_type is NT
    and ellipsis_type is ET
    and notimplemented_type is NIT
    and module.NoneType is none_type
    and module.EllipsisType is ellipsis_type
    and module.NotImplementedType is notimplemented_type
    and none_type() is None
    and ellipsis_type() is Ellipsis
    and notimplemented_type() is NotImplemented
    and isinstance(None, none_type)
    and isinstance(..., ellipsis_type)
    and isinstance(NotImplemented, notimplemented_type)
    and issubclass(none_class, none_type)
    and issubclass(ellipsis_class, ellipsis_type)
    and issubclass(notimplemented_class, notimplemented_type)
    and str(none_type) == "<class 'NoneType'>"
    and repr(ellipsis_type) == "<class 'ellipsis'>"
    and ascii(notimplemented_type) == "<class 'NotImplementedType'>"
    and none_type.__name__ == "NoneType"
    and ellipsis_type.__name__ == "ellipsis"
    and notimplemented_type.__name__ == "NotImplementedType"
    and none_type.__qualname__ == "NoneType"
    and ellipsis_type.__qualname__ == "ellipsis"
    and notimplemented_type.__qualname__ == "NotImplementedType"
    and getattr(none_type, "__module__") == "builtins"
    and getattr(ellipsis_type, "__module__") == "builtins"
    and getattr(notimplemented_type, "__module__") == "builtins"
    and hasattr(none_type, "__qualname__")
    and hasattr(ellipsis_type, "__module__")
    and not hasattr(notimplemented_type, "missing")
    and {none_type: 1, ellipsis_type: 2, notimplemented_type: 3}[ellipsis_type] == 2
    and mark_type_error(none_with_argument)
    and mark_type_error(ellipsis_with_argument)
    and mark_type_error(notimplemented_with_argument)
)

result
