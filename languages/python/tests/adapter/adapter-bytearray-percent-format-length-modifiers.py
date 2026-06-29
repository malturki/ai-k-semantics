fmt = bytearray(b"%#06LX")
out = fmt % 12

result = (
    isinstance(out, bytearray)
    and not isinstance(out, bytes)
    and out == bytearray(b"0X000C")
    and fmt == bytearray(b"%#06LX")
)

assert result
result
