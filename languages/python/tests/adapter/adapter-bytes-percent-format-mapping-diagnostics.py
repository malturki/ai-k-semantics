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

missing_nonempty = False
try:
    b"%(x)d" % {b"y": 7}
except KeyError:
    missing_nonempty = True

bytes_key_required = False
try:
    b"%(x)d" % {"x": 7}
except KeyError:
    bytes_key_required = True

prefix_missing = False
try:
    b"prefix:%(x)d" % {b"y": 7}
except KeyError:
    prefix_missing = True

later_missing = False
try:
    b"%(x)d:%(y)d" % {b"x": 1}
except KeyError:
    later_missing = True

incomplete_nonempty = False
try:
    b"%(x" % {b"x": 7}
except ValueError:
    incomplete_nonempty = True

result = (
    nonmapping
    and missing_key
    and missing_nonempty
    and bytes_key_required
    and prefix_missing
    and later_missing
    and incomplete_nonempty
)

assert result
result
