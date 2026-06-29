fmt = bytearray(b"%0*d")
out = fmt % (5, 12)

result = (
    isinstance(out, bytearray)
    and not isinstance(out, bytes)
    and out == bytearray(b"00012")
    and fmt == bytearray(b"%0*d")
)

assert result
result
