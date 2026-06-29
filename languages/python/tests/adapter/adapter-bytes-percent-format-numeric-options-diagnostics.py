bad_decimal_bytes = False
try:
    b"%5d" % b"1"
except TypeError:
    bad_decimal_bytes = True

bad_hex_bytes = False
try:
    b"%#6x" % b"1"
except TypeError:
    bad_hex_bytes = True

bad_bytearray_string = False
try:
    bytearray(b"%+05d") % "1"
except TypeError:
    bad_bytearray_string = True

result = bad_decimal_bytes and bad_hex_bytes and bad_bytearray_string

assert result
result
