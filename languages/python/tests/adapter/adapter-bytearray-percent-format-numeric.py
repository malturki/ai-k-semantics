fmt = bytearray(b"%d:%o:%X")
out = fmt % (1.9, True, 255)
single = bytearray(b"%x") % 15

result = (
    isinstance(out, bytearray)
    and not isinstance(out, bytes)
    and out == bytearray(b"1:1:FF")
    and single == bytearray(b"f")
    and fmt == bytearray(b"%d:%o:%X")
)

assert result
result
