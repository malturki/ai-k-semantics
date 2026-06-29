data = b"a:b:c"

value_error_ok = True
try:
    data.partition(b"")
    value_error_ok = False
except ValueError:
    pass

try:
    data.rpartition(bytearray())
    value_error_ok = False
except ValueError:
    pass

type_error_ok = True
try:
    data.partition(97)
    type_error_ok = False
except TypeError:
    pass

try:
    data.rpartition("a")
    type_error_ok = False
except TypeError:
    pass

try:
    data.partition([97])
    type_error_ok = False
except TypeError:
    pass

result = value_error_ok and type_error_ok and data == b"a:b:c"
assert result
result
