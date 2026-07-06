import types


def mark_attribute_error(thunk):
    try:
        thunk()
    except AttributeError:
        return True
    return False


none_value = None
ellipsis_value = ...
notimplemented_value = NotImplemented


def missing_none():
    none_value.missing


def missing_ellipsis():
    ellipsis_value.missing


def missing_notimplemented():
    notimplemented_value.missing


result = (
    none_value.__class__ is types.NoneType
    and ellipsis_value.__class__ is types.EllipsisType
    and notimplemented_value.__class__ is types.NotImplementedType
    and none_value.__class__ is type(none_value)
    and ellipsis_value.__class__ is type(ellipsis_value)
    and notimplemented_value.__class__ is type(notimplemented_value)
    and getattr(none_value, "__class__") is types.NoneType
    and getattr(ellipsis_value, "__class__") is types.EllipsisType
    and getattr(notimplemented_value, "__class__") is types.NotImplementedType
    and hasattr(none_value, "__class__")
    and hasattr(ellipsis_value, "__class__")
    and hasattr(notimplemented_value, "__class__")
    and not hasattr(none_value, "missing")
    and not hasattr(ellipsis_value, "missing")
    and not hasattr(notimplemented_value, "missing")
    and mark_attribute_error(missing_none)
    and mark_attribute_error(missing_ellipsis)
    and mark_attribute_error(missing_notimplemented)
)

result
