dash = b"-"

byteslike_ok = (
    dash.join([bytearray(b"a"), memoryview(b"b")]) == b"a-b"
    and b"".join((memoryview(b"a"), bytearray(b"b"))) == b"ab"
)

type_error_ok = True
try:
    dash.join([b"a", "b"])
    type_error_ok = False
except TypeError:
    pass

try:
    dash.join([b"a", 98])
    type_error_ok = False
except TypeError:
    pass

try:
    dash.join("ab")
    type_error_ok = False
except TypeError:
    pass

try:
    dash.join(b"ab")
    type_error_ok = False
except TypeError:
    pass

try:
    dash.join(123)
    type_error_ok = False
except TypeError:
    pass

unchanged_ok = dash == b"-"

result = byteslike_ok and type_error_ok and unchanged_ok
assert result
result
