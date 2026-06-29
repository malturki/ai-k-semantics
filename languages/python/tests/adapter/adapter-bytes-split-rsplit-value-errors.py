csv = b"1,2,,3,"

value_error_ok = True
try:
    csv.split(b"")
    value_error_ok = False
except ValueError:
    pass

try:
    csv.rsplit(bytearray())
    value_error_ok = False
except ValueError:
    pass

result = value_error_ok and csv == b"1,2,,3,"
assert result
result
