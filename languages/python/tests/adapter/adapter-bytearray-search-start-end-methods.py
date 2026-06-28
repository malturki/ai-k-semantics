data = bytearray(b"banana")

count_ok = (
    data.count(b"an", 1) == 2
    and data.count(b"an", 2, 5) == 1
    and data.count(bytearray(b"na"), 2, 6) == 2
    and data.count(memoryview(b"an"), 0, 3) == 1
    and data.count(97, -4, -1) == 1
    and data.count(b"", 2, 2) == 1
    and data.count(b"", 2, 1) == 0
)

find_ok = (
    data.find(b"an", 2) == 3
    and data.find(97, 2, 5) == 3
    and data.find(memoryview(b"an"), 0, 3) == 1
    and data.find(b"", 2, 2) == 2
    and data.find(b"", 100, 200) == -1
    and data.find(b"an", None, None) == 1
)

rfind_ok = (
    data.rfind(b"an", 0, 3) == 1
    and data.rfind(b"an", 0, 5) == 3
    and data.rfind(97, 1, 5) == 3
    and data.rfind(b"", 1, 5) == 5
    and data.rfind(b"", 2, 1) == -1
    and data.rfind(b"a", False, True) == -1
)

index_ok = (
    data.index(b"an", 2) == 3
    and data.index(97, 2, 5) == 3
    and data.index(b"", 2, 2) == 2
)

rindex_ok = (
    data.rindex(b"an", 0, 5) == 3
    and data.rindex(bytearray(b"an"), 1, 5) == 3
    and data.rindex(97, 1, 5) == 3
    and data.rindex(b"", 1, 5) == 5
)

value_error_ok = True
try:
    data.index(b"an", 2, 3)
    value_error_ok = False
except ValueError:
    pass

try:
    data.rindex(b"an", 2, 3)
    value_error_ok = False
except ValueError:
    pass

try:
    data.index(b"", 2, 1)
    value_error_ok = False
except ValueError:
    pass

try:
    data.rindex(b"", 2, 1)
    value_error_ok = False
except ValueError:
    pass

try:
    data.find(300, 0, 1)
    value_error_ok = False
except ValueError:
    pass

type_error_ok = True
try:
    data.count("a", 0, 1)
    type_error_ok = False
except TypeError:
    pass

try:
    data.find(b"a", "x")
    type_error_ok = False
except TypeError:
    pass

try:
    data.rfind(b"a", 0, "x")
    type_error_ok = False
except TypeError:
    pass

try:
    data.index(300, "x")
    type_error_ok = False
except TypeError:
    pass

unchanged_ok = data == bytearray(b"banana")

result = (
    count_ok
    and find_ok
    and rfind_ok
    and index_ok
    and rindex_ok
    and value_error_ok
    and type_error_ok
    and unchanged_ok
)
assert result
result
