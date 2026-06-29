bad_precision = False
try:
    b"%.*b" % ("1", b"xyz")
except TypeError:
    bad_precision = True

too_few = False
try:
    b"%.*b" % (1,)
except TypeError:
    too_few = True

result = bad_precision and too_few

assert result
result
