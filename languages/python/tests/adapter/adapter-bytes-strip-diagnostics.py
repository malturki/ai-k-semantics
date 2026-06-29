data = b"abc"

type_error_ok = True

try:
    data.strip(97)
    type_error_ok = False
except TypeError:
    pass

try:
    data.lstrip("a")
    type_error_ok = False
except TypeError:
    pass

try:
    data.rstrip([97])
    type_error_ok = False
except TypeError:
    pass

assert type_error_ok
type_error_ok
