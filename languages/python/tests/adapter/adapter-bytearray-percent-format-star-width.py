fmt = bytearray(b"%*c")
out = fmt % (5, 65)

result = (
    isinstance(out, bytearray)
    and not isinstance(out, bytes)
    and out == bytearray(b"    A")
    and fmt == bytearray(b"%*c")
)

assert result
result
