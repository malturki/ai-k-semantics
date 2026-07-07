import builtins
from builtins import object as imported_object
from builtins import type as imported_type


def mark_type_error(thunk):
    try:
        thunk()
    except TypeError:
        return True
    return False


type_alias = type
object_alias = object


def type_without_arguments():
    type_alias()


def type_with_two_arguments():
    type_alias(1, 2)


def type_with_keyword():
    type_alias(object=1)


def type_with_mixed_keyword():
    type_alias(1, name=2)


name_exposure = (
    object is builtins.object
    and type is builtins.type
    and imported_object is object
    and imported_type is type
    and object_alias is builtins.object
)

type_alias_calls = (
    type_alias(1) is int
    and type_alias(True) is bool
    and type_alias(object) is type
    and type_alias(type) is type
    and mark_type_error(type_without_arguments)
    and mark_type_error(type_with_two_arguments)
    and mark_type_error(type_with_keyword)
    and mark_type_error(type_with_mixed_keyword)
)

class_attributes = (
    object.__class__ is type
    and type.__class__ is type
    and int.__class__ is type
    and bool.__class__ is type
    and object.__base__ is None
    and type.__base__ is object
    and int.__base__ is object
    and bool.__base__ is int
    and object.__bases__ == ()
    and type.__bases__ == (object,)
    and int.__bases__ == (object,)
    and bool.__bases__ == (int,)
    and object.__mro__ == (object,)
    and type.__mro__ == (type, object)
    and int.__mro__ == (int, object)
    and bool.__mro__ == (bool, int, object)
    and getattr(str, "__base__") is object
    and getattr(str, "__bases__") == (object,)
    and getattr(str, "__mro__") == (str, object)
    and hasattr(bytes, "__base__")
    and hasattr(bytes, "__bases__")
    and hasattr(bytes, "__mro__")
)

classinfo = (
    isinstance(1, object)
    and isinstance(None, object)
    and isinstance(object, object)
    and isinstance(type, object)
    and isinstance(object, type)
    and isinstance(type, type)
    and isinstance(int, type)
    and not isinstance(1, type)
    and issubclass(object, object)
    and not issubclass(object, type)
    and issubclass(type, type)
    and issubclass(type, object)
    and issubclass(int, object)
    and issubclass(bool, int)
    and issubclass(bool, object)
    and not issubclass(bool, type)
)

result = name_exposure and type_alias_calls and class_attributes and classinfo

result
