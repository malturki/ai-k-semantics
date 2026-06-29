bad_bytes = False
try:
    b"%+b" % "xy"
except TypeError:
    bad_bytes = True

bad_char = False
try:
    b"%#05c" % 256
except OverflowError:
    bad_char = True

result = bad_bytes and bad_char

assert result
result
