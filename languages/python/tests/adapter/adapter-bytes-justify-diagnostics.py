data = b"abc"

type_error_ok = True
try:
    data.center("5")
    type_error_ok = False
except TypeError:
    pass

try:
    data.ljust(5.0)
    type_error_ok = False
except TypeError:
    pass

try:
    data.center(5, 120)
    type_error_ok = False
except TypeError:
    pass

try:
    data.ljust(5, b"")
    type_error_ok = False
except TypeError:
    pass

try:
    data.rjust(5, bytearray(b"xy"))
    type_error_ok = False
except TypeError:
    pass

try:
    data.center(5, memoryview(b"z"))
    type_error_ok = False
except TypeError:
    pass

try:
    data.center(1, b"xy")
    type_error_ok = False
except TypeError:
    pass

result = type_error_ok and data == b"abc"
assert result
result
