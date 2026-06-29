value_error_ok = True
try:
    bytes.fromhex("2 E")
    value_error_ok = False
except ValueError:
    pass

try:
    bytearray.fromhex("2x")
    value_error_ok = False
except ValueError:
    pass

type_error_ok = True
try:
    bytes.fromhex(None)
    type_error_ok = False
except TypeError:
    pass

result = value_error_ok and type_error_ok
assert result
result
