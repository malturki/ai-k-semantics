data = bytearray(b"banana")
triple = bytearray(b"aaa")
abc = bytearray(b"abc")
abcabc = bytearray(b"abcabc")
empty = bytearray()

basic_ok = (
    data.replace(b"na", b"XY") == bytearray(b"baXYXY")
    and data.replace(b"z", b"Q") == bytearray(b"banana")
    and triple.replace(b"aa", b"X") == bytearray(b"Xa")
)

count_ok = (
    data.replace(b"a", b"A", 0) == bytearray(b"banana")
    and data.replace(b"a", b"A", 1) == bytearray(b"bAnana")
    and data.replace(b"a", b"A", 2) == bytearray(b"bAnAna")
    and data.replace(b"a", b"A", -1) == bytearray(b"bAnAnA")
    and data.replace(b"a", b"A", True) == bytearray(b"bAnana")
    and data.replace(b"a", b"A", False) == bytearray(b"banana")
)

empty_old_ok = (
    abc.replace(b"", b"-") == bytearray(b"-a-b-c-")
    and abc.replace(b"", b"-", 1) == bytearray(b"-abc")
    and abc.replace(b"", b"-", 2) == bytearray(b"-a-bc")
    and abc.replace(b"", b"-", 3) == bytearray(b"-a-b-c")
    and abc.replace(b"", b"-", 4) == bytearray(b"-a-b-c-")
    and abc.replace(b"", b"-", 0) == bytearray(b"abc")
    and empty.replace(b"", b"-") == bytearray(b"-")
    and empty.replace(b"", b"-", 0) == bytearray()
)

byteslike_ok = (
    data.replace(bytearray(b"an"), memoryview(b"__"), 1) == bytearray(b"b__ana")
    and data.replace(memoryview(b"na"), bytearray(b"!"), 1) == bytearray(b"ba!na")
)

delete_ok = (
    abcabc.replace(b"b", b"") == bytearray(b"acac")
    and abc.replace(b"", b"") == bytearray(b"abc")
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

unchanged_ok = (
    data == bytearray(b"banana")
    and triple == bytearray(b"aaa")
    and abc == bytearray(b"abc")
    and abcabc == bytearray(b"abcabc")
    and empty == bytearray()
)

result = basic_ok and count_ok and empty_old_ok and byteslike_ok and delete_ok and type_error_ok and unchanged_ok
assert result
result
