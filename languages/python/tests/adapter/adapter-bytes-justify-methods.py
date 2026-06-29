empty = b""
data = b"abc"

default_ok = (
    data.ljust(6) == b"abc   "
    and data.rjust(6) == b"   abc"
    and data.center(7) == b"  abc  "
    and data.center(8) == b"  abc   "
    and data.center(2) == b"abc"
    and empty.center(3) == b"   "
)

fill_ok = (
    data.ljust(6, b"x") == b"abcxxx"
    and data.rjust(6, bytearray(b"y")) == b"yyyabc"
    and data.center(8, b"z") == b"zzabczzz"
    and data.rjust(5, b"\xff") == b"\xff\xffabc"
)

bool_width_ok = (
    data.center(True) == b"abc"
    and empty.ljust(True, b"q") == b"q"
    and empty.rjust(False, b"q") == b""
)

unchanged_ok = data == b"abc"

result = default_ok and fill_ok and bool_width_ok and unchanged_ok
assert result
result
