empty = b""
lower = b"abc123!"
spaces = b" \t\n\r\v\f"
non_ascii = b"\x00\x7f\x80\xff"

result = (
    empty.isascii()
    and lower.isascii()
    and spaces.isascii()
    and not non_ascii.isascii()
    and empty == b""
    and lower == b"abc123!"
    and non_ascii == b"\x00\x7f\x80\xff"
)

assert result
result
