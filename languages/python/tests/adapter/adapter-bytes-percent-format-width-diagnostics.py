bad_b_type = False
try:
    b"%5b" % "x"
except TypeError:
    bad_b_type = True

bad_c_range = False
try:
    b"%5c" % 256
except OverflowError:
    bad_c_range = True

bad_c_length = False
try:
    bytearray(b"%-5c") % b"AB"
except TypeError:
    bad_c_length = True

result = bad_b_type and bad_c_range and bad_c_length

assert result
result
