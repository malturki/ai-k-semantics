bad_width = False
try:
    b"%*b" % ("5", b"xy")
except TypeError:
    bad_width = True

too_few = False
try:
    b"%*b" % (5,)
except TypeError:
    too_few = True

result = bad_width and too_few

assert result
result
