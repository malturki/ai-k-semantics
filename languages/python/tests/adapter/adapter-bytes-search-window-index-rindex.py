data = b"banana"

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

result = (
    data.index(b"an", 2) == 3
    and data.index(97, 2, 5) == 3
    and data.index(b"", 2, 2) == 2
    and data.rindex(b"an", 0, 5) == 3
    and data.rindex(bytearray(b"an"), 1, 5) == 3
    and data.rindex(97, 1, 5) == 3
    and data.rindex(b"", 1, 5) == 5
    and value_error_ok
    and data == b"banana"
)

assert result
result
