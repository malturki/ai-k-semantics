empty = bytearray()
digits = bytearray(b"42")
negative = bytearray(b"-42")
positive = bytearray(b"+42")
double_sign = bytearray(b"--42")
leading_space = bytearray(b" 42")
non_ascii = bytearray(b"\xff42")

basic_ok = (
    empty.zfill(0) == bytearray()
    and empty.zfill(3) == bytearray(b"000")
    and digits.zfill(1) == bytearray(b"42")
    and digits.zfill(2) == bytearray(b"42")
    and digits.zfill(5) == bytearray(b"00042")
)

sign_ok = (
    negative.zfill(5) == bytearray(b"-0042")
    and positive.zfill(5) == bytearray(b"+0042")
    and double_sign.zfill(5) == bytearray(b"-0-42")
)

other_ok = (
    leading_space.zfill(5) == bytearray(b"00 42")
    and non_ascii.zfill(5) == bytearray(b"00\xff42")
    and digits.zfill(True) == bytearray(b"42")
    and empty.zfill(True) == bytearray(b"0")
    and digits.zfill(False) == bytearray(b"42")
)

type_error_ok = False
try:
    digits.zfill("5")
except TypeError:
    type_error_ok = True

unchanged_ok = (
    digits == bytearray(b"42")
    and negative == bytearray(b"-42")
    and non_ascii == bytearray(b"\xff42")
)

result = basic_ok and sign_ok and other_ok and type_error_ok and unchanged_ok
assert result
result
