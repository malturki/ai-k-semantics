data = b"banana"
empty = b""

count_ok = (
    data.count(b"an") == 2
    and data.count(bytearray(b"an")) == 2
    and data.count(memoryview(b"an")) == 2
    and data.count(b"") == 7
    and empty.count(b"") == 1
    and empty.count(b"a") == 0
)

index_ok = (
    data.index(b"an") == 1
    and data.index(bytearray(b"an")) == 1
    and data.index(memoryview(b"an")) == 1
    and data.index(b"") == 0
    and empty.index(b"") == 0
)

rindex_ok = (
    data.rindex(97) == 5
    and data.rindex(b"an") == 3
    and data.rindex(bytearray(b"an")) == 3
    and data.rindex(memoryview(b"an")) == 3
    and data.rindex(b"") == 6
    and empty.rindex(b"") == 0
)

value_error_ok = True
try:
    data.index(b"z")
    value_error_ok = False
except ValueError:
    pass

try:
    data.rindex(b"z")
    value_error_ok = False
except ValueError:
    pass

try:
    data.rindex(300)
    value_error_ok = False
except ValueError:
    pass

try:
    empty.rindex(97)
    value_error_ok = False
except ValueError:
    pass

type_error_ok = True
try:
    data.count("a")
    type_error_ok = False
except TypeError:
    pass

try:
    data.rindex("a")
    type_error_ok = False
except TypeError:
    pass

unchanged_ok = data == b"banana" and empty == b""

result = count_ok and index_ok and rindex_ok and value_error_ok and type_error_ok and unchanged_ok
assert result
result
