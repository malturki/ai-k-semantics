empty = b""
data = b"\xf0\xf1\xf2"
value = b"UUDDLRLRAB"
mixed = bytes([0, 1, 15, 16, 255])

plain_ok = (
    empty.hex() == ""
    and data.hex() == "f0f1f2"
    and value.hex() == "555544444c524c524142"
    and mixed.hex() == "00010f10ff"
)

separator_ok = (
    data.hex("-") == "f0-f1-f2"
    and data.hex(b"-") == "f0-f1-f2"
    and value.hex("_", 2) == "5555_4444_4c52_4c52_4142"
    and value.hex(" ", -4) == "55554444 4c524c52 4142"
    and mixed.hex("|", 1) == "00|01|0f|10|ff"
    and mixed.hex("|", -1) == "00|01|0f|10|ff"
    and mixed.hex("_", 2) == "00_010f_10ff"
    and mixed.hex("_", -2) == "0001_0f10_ff"
    and mixed.hex("|", 0) == "00010f10ff"
    and mixed.hex("|", False) == "00010f10ff"
    and mixed.hex("|", True) == "00|01|0f|10|ff"
    and mixed.hex("|", 99) == "00010f10ff"
    and mixed.hex("|", -99) == "00010f10ff"
    and empty.hex("-") == ""
    and empty.hex("-", 2) == ""
)

value_error_ok = True
try:
    data.hex("")
    value_error_ok = False
except ValueError:
    pass

try:
    data.hex("--")
    value_error_ok = False
except ValueError:
    pass

try:
    data.hex(b"\xff")
    value_error_ok = False
except ValueError:
    pass

type_error_ok = True
try:
    data.hex(bytearray(b"-"))
    type_error_ok = False
except TypeError:
    pass

try:
    data.hex(memoryview(b"-"))
    type_error_ok = False
except TypeError:
    pass

try:
    data.hex(None)
    type_error_ok = False
except TypeError:
    pass

try:
    data.hex("-", 1.0)
    type_error_ok = False
except TypeError:
    pass

try:
    data.hex("--", "bad")
    type_error_ok = False
except TypeError:
    pass

unchanged_ok = (
    empty == b""
    and data == b"\xf0\xf1\xf2"
    and value == b"UUDDLRLRAB"
    and mixed == bytes([0, 1, 15, 16, 255])
)

result = plain_ok and separator_ok and value_error_ok and type_error_ok and unchanged_ok
assert result
result
