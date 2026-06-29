not_enough = False
try:
    b"%b %b" % b"x"
except TypeError:
    not_enough = True

too_many = False
try:
    b"%b" % (b"x", b"y")
except TypeError:
    too_many = True

plain_extra = False
try:
    b"plain" % b"x"
except TypeError:
    plain_extra = True

bad_b_type = False
try:
    b"%b" % "x"
except TypeError:
    bad_b_type = True

bad_c_range = False
try:
    b"%c" % 256
except OverflowError:
    bad_c_range = True

bad_c_length = False
try:
    b"%c" % b"AB"
except TypeError:
    bad_c_length = True

bad_c_memoryview = False
try:
    b"%c" % memoryview(b"A")
except TypeError:
    bad_c_memoryview = True

result = not_enough and too_many and plain_extra and bad_b_type
result = result and bad_c_range and bad_c_length and bad_c_memoryview

assert result
result
