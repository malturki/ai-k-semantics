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

star_missing = False
try:
    b"%(x)*d" % {b"y": 7}
except KeyError:
    star_missing = True

star_width_int = False
try:
    b"%(x)*d" % {b"x": 7}
except TypeError:
    star_width_int = True

star_width_bytes = False
try:
    b"%(x)*b" % {b"x": b"abc"}
except TypeError:
    star_width_bytes = True

star_precision_bytes = False
try:
    b"%(x).*b" % {b"x": b"abc"}
except TypeError:
    star_precision_bytes = True

later_star = False
try:
    b"%(x)d:%(y)*d" % {b"x": 1, b"y": 7}
except TypeError:
    later_star = True

later_star_missing = False
try:
    b"%(x)d:%(y)*d" % {b"x": 1}
except KeyError:
    later_star_missing = True

bytearray_star = False
try:
    bytearray(b"%(x)*d") % {b"x": 7}
except TypeError:
    bytearray_star = True

result = (
    nonmapping
    and missing_key
    and missing_nonempty
    and bytes_key_required
    and prefix_missing
    and later_missing
    and incomplete_nonempty
    and star_missing
    and star_width_int
    and star_width_bytes
    and star_precision_bytes
    and later_star
    and later_star_missing
    and bytearray_star
)

assert result
result
