fmt = bytearray(b"%5.*s")
out = fmt % (1, b"xyz")

result = (
    isinstance(out, bytearray)
    and not isinstance(out, bytes)
    and out == bytearray(b"    x")
    and fmt == bytearray(b"%5.*s")
)

assert result
result
