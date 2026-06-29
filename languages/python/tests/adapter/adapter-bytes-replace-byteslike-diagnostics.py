data = b"banana"
abc = b"abc"
abcabc = b"abcabc"

byteslike_ok = (
    data.replace(bytearray(b"an"), memoryview(b"__"), 1) == b"b__ana"
    and data.replace(memoryview(b"na"), bytearray(b"!"), 1) == b"ba!na"
)

delete_ok = (
    abcabc.replace(b"b", b"") == b"acac"
    and abc.replace(b"abc", bytearray(b"Q")) == b"Q"
)

type_error_ok = True
try:
    data.replace("a", b"x")
    type_error_ok = False
except TypeError:
    pass

try:
    data.replace(b"a", "x")
    type_error_ok = False
except TypeError:
    pass

try:
    data.replace(b"a", b"x", "bad")
    type_error_ok = False
except TypeError:
    pass

try:
    data.replace(b"a", [120], "bad")
    type_error_ok = False
except TypeError:
    pass

try:
    data.replace(b"a", b"x", None)
    type_error_ok = False
except TypeError:
    pass

unchanged_ok = data == b"banana" and abc == b"abc" and abcabc == b"abcabc"

result = byteslike_ok and delete_ok and type_error_ok and unchanged_ok
assert result
result
