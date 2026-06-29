nonmapping = False
try:
    b"%(x)d" % (1,)
except TypeError:
    nonmapping = True

missing_key = False
try:
    b"%(x)d" % {}
except KeyError:
    missing_key = True

result = nonmapping and missing_key

assert result
result
