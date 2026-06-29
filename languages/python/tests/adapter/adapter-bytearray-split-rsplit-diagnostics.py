csv = bytearray(b"1,2,,3,")

type_error_ok = True
try:
    csv.split(" ")
    type_error_ok = False
except TypeError:
    pass

try:
    csv.split([], 1)
    type_error_ok = False
except TypeError:
    pass

try:
    csv.rsplit(b",", 1.0)
    type_error_ok = False
except TypeError:
    pass

try:
    csv.split(b"", "x")
    type_error_ok = False
except TypeError:
    pass

result = type_error_ok and csv == bytearray(b"1,2,,3,")
assert result
result
