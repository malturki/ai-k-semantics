bad_decimal_bytes = False
try:
    b"%d" % b"1"
except TypeError:
    bad_decimal_bytes = True

bad_hex_float = False
try:
    b"%x" % 1.0
except TypeError:
    bad_hex_float = True

bad_octal_string = False
try:
    bytearray(b"%o") % "1"
except TypeError:
    bad_octal_string = True

decimal_inf = False
try:
    b"%d" % float("inf")
except OverflowError:
    decimal_inf = True

decimal_nan = False
try:
    b"%u" % float("nan")
except ValueError:
    decimal_nan = True

result = bad_decimal_bytes and bad_hex_float and bad_octal_string
result = result and decimal_inf and decimal_nan

assert result
result
