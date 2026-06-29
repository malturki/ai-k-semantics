bad_width = False
try:
    b"%*d" % ("5", 12)
except TypeError:
    bad_width = True

bad_value = False
try:
    b"%*d" % (5, "x")
except TypeError:
    bad_value = True

too_few = False
try:
    b"%*d" % (5,)
except TypeError:
    too_few = True

result = bad_width and bad_value and too_few

assert result
result
