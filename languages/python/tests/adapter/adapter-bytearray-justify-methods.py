empty = bytearray()
data = bytearray(b"abc")

default_ok = (
    data.ljust(6) == bytearray(b"abc   ")
    and data.rjust(6) == bytearray(b"   abc")
    and data.center(7) == bytearray(b"  abc  ")
    and data.center(8) == bytearray(b"  abc   ")
    and data.center(2) == bytearray(b"abc")
    and empty.center(3) == bytearray(b"   ")
)

fill_ok = (
    data.ljust(6, b"x") == bytearray(b"abcxxx")
    and data.rjust(6, bytearray(b"y")) == bytearray(b"yyyabc")
    and data.center(8, b"z") == bytearray(b"zzabczzz")
    and data.rjust(5, b"\xff") == bytearray(b"\xff\xffabc")
)

bool_width_ok = (
    data.center(True) == bytearray(b"abc")
    and empty.ljust(True, b"q") == bytearray(b"q")
    and empty.rjust(False, b"q") == bytearray()
)

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

unchanged_ok = data == bytearray(b"abc")

result = default_ok and fill_ok and bool_width_ok and type_error_ok and unchanged_ok
assert result
result
