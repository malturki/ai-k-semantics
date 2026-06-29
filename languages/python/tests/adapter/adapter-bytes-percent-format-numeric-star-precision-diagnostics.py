bad_precision = False
try:
    b"%.*d" % ("3", 12)
except TypeError:
    bad_precision = True

bad_star_precision = False
try:
    b"%*.*d" % (5, "3", 12)
except TypeError:
    bad_star_precision = True

bad_value = False
try:
    b"%*.*d" % (5, 3, "x")
except TypeError:
    bad_value = True

too_few = False
try:
    b"%.*d" % (3,)
except TypeError:
    too_few = True

result = bad_precision and bad_star_precision and bad_value and too_few

assert result
result
