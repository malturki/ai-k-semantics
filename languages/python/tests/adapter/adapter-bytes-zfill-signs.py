negative = b"-42"
positive = b"+42"
double_sign = b"--42"
leading_space = b" 42"
non_ascii = b"\xff42"
empty = b""
digits = b"42"

result = (
    negative.zfill(5) == b"-0042"
    and positive.zfill(5) == b"+0042"
    and double_sign.zfill(5) == b"-0-42"
    and leading_space.zfill(5) == b"00 42"
    and non_ascii.zfill(5) == b"00\xff42"
    and digits.zfill(True) == b"42"
    and empty.zfill(True) == b"0"
    and digits.zfill(False) == b"42"
    and negative == b"-42"
    and non_ascii == b"\xff42"
)

assert result
result
