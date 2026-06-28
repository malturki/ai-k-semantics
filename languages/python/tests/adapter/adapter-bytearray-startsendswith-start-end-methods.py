data = bytearray(b"banana")

startswith_ok = (
    data.startswith(b"ba", 0, 6)
    and not data.startswith(b"ba", 1, 5)
    and data.startswith(b"an", 1, 5)
    and data.startswith(bytearray(b"na"), -4, -1)
    and data.startswith(memoryview(b"an"), 1, 5)
    and data.startswith(b"", 2, 2)
    and not data.startswith(b"", 2, 1)
    and not data.startswith(b"", 100, 200)
    and not data.startswith(b"a", False, True)
)

endswith_ok = (
    data.endswith(b"na", 0, 6)
    and not data.endswith(b"na", 1, 5)
    and data.endswith(b"an", 1, 5)
    and data.endswith(bytearray(b"an"), -4, -1)
    and data.endswith(memoryview(b"na"), 0, 6)
    and data.endswith(b"", 6, 6)
    and not data.endswith(b"", 7, 7)
    and data.endswith(b"a", None, None)
)

tuple_ok = (
    data.startswith((b"x", b""), 2, 2)
    and not data.startswith((b"x", b""), 2, 1)
    and data.startswith((b"z", b"ba"), 0, 2)
    and data.endswith((b"zz", b"na"), 0, 6)
    and not data.endswith((b"x", b""), 100, 200)
)

type_error_ok = True
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
    data.startswith("a", 0, 1)
    type_error_ok = False
except TypeError:
    pass

try:
    data.endswith("a", 0, 1)
    type_error_ok = False
except TypeError:
    pass

try:
    data.startswith((b"z", "x"), 0, 1)
    type_error_ok = False
except TypeError:
    pass

try:
    data.endswith((b"z", "x"), 0, 6)
    type_error_ok = False
except TypeError:
    pass

try:
    data.startswith((b"", "x"), 2, 1)
    type_error_ok = False
except TypeError:
    pass

unchanged_ok = data == bytearray(b"banana")

result = startswith_ok and endswith_ok and tuple_ok and type_error_ok and unchanged_ok
assert result
result
