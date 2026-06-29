empty = b""
digits = b"42"

result = (
    empty.zfill(0) == b""
    and empty.zfill(3) == b"000"
    and digits.zfill(1) == b"42"
    and digits.zfill(2) == b"42"
    and digits.zfill(5) == b"00042"
    and digits == b"42"
)

assert result
result
