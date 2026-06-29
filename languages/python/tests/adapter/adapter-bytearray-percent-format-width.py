fmt = bytearray(b"%5b|%-5c|%6.2r")
out = fmt % (memoryview(b"xy"), 65, b"abcdef")

result = (
    isinstance(out, bytearray)
    and not isinstance(out, bytes)
    and out == bytearray(b"   xy|A    |    b'")
    and fmt == bytearray(b"%5b|%-5c|%6.2r")
)

assert result
result
