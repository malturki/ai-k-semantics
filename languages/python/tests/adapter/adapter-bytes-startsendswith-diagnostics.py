data = b"abc"

type_error_ok = True

try:
    data.startswith(97)
    type_error_ok = False
except TypeError:
    pass

try:
    data.startswith("a")
    type_error_ok = False
except TypeError:
    pass

try:
    data.startswith((b"z", 1))
    type_error_ok = False
except TypeError:
    pass

try:
    data.endswith(99)
    type_error_ok = False
except TypeError:
    pass

try:
    data.endswith("c")
    type_error_ok = False
except TypeError:
    pass

try:
    data.endswith((b"z", 1))
    type_error_ok = False
except TypeError:
    pass

try:
    data.startswith(b"a", "x")
    type_error_ok = False
except TypeError:
    pass

try:
    data.endswith(b"a", 0, "x")
    type_error_ok = False
except TypeError:
    pass

try:
    data.startswith((b"", "x"), 2, 1)
    type_error_ok = False
except TypeError:
    pass

assert type_error_ok
type_error_ok
