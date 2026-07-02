seed = 10
result = True


class WithAttrs:
    x = 1
    y = seed + 2
    x = 3
    z = x + y
    pass


class Shadow:
    result = False


obj = WithAttrs()

result = result and WithAttrs.x == 3
result = result and WithAttrs.y == 12
result = result and WithAttrs.z == 15
result = result and obj.x == 3
result = result and obj.z == 15
result = result and getattr(WithAttrs, "x") == 3
result = result and getattr(obj, "z") == 15
result = result and getattr(WithAttrs, "missing", 99) == 99
result = result and getattr(obj, "missing", 88) == 88
result = result and getattr(WithAttrs, "absent_class_attr", 77) == 77
result = result and hasattr(WithAttrs, "x")
result = result and hasattr(obj, "z")
result = result and not hasattr(WithAttrs, "missing")
result = result and not hasattr(obj, "missing")
result = result and not hasattr(obj, "absent_class_attr")
result = result and Shadow.result is False

missing_error = False
try:
    getattr(WithAttrs, "missing")
except AttributeError:
    missing_error = True
result = result and missing_error

dynamic_missing_error = False
try:
    getattr(obj, "absent_class_attr")
except AttributeError:
    dynamic_missing_error = True
result = result and dynamic_missing_error

assert result
result
