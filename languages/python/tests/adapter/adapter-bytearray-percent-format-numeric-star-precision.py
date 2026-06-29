fmt = bytearray(b"%5.*d")
out = fmt % (3, 12)

result = (
    isinstance(out, bytearray)
    and not isinstance(out, bytes)
    and out == bytearray(b"  012")
    and fmt == bytearray(b"%5.*d")
)

assert result
result
