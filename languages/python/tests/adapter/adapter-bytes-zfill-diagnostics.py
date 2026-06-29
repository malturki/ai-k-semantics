digits = b"42"

type_error_ok = False
try:
    digits.zfill("5")
except TypeError:
    type_error_ok = True

assert type_error_ok
type_error_ok
