name = "start"
result = getattr(range(2, 7), name) == 2

name = "st" + "op"
result = result and getattr(range(2, 7), name) == 7
result = result and hasattr(slice(1, 5, 2), name)

name = "st" + "ep"
result = result and getattr(slice(1, 5, 2), name) == 2

name = "num" + "erator"
result = result and getattr(3, name) == 3

name = "im" + "ag"
result = result and getattr(1 + 2j, name) == 2.0

missing = "miss" + "ing"
result = result and getattr(range(1), missing, 99) == 99
result = result and not hasattr(range(1), missing)

missing_error = False
try:
    getattr(range(1), missing)
except AttributeError:
    missing_error = True
result = result and missing_error

default_eval_error = False
try:
    getattr(range(1), "st" + "art", 1 // 0)
except ZeroDivisionError:
    default_eval_error = True
result = result and default_eval_error

name_type_error = False
try:
    getattr(range(1), 1)
except TypeError:
    name_type_error = True
result = result and name_type_error

hasattr_type_error = False
try:
    hasattr(range(1), None)
except TypeError:
    hasattr_type_error = True
result = result and hasattr_type_error

assert result
result
