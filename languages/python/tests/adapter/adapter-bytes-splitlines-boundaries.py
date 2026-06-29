crlf = b"a\r\nb"

result = (
    crlf.splitlines() == [b"a", b"b"]
    and crlf.splitlines(True) == [b"a\r\n", b"b"]
)
assert result
result
