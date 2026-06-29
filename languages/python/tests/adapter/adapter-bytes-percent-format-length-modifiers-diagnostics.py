bad_decimal_bytes = False
try:
    b"%hd" % b"1"
except TypeError:
    bad_decimal_bytes = True

bad_c_overflow = False
try:
    b"%lc" % 256
except OverflowError:
    bad_c_overflow = True

result = bad_decimal_bytes and bad_c_overflow

assert result
result
