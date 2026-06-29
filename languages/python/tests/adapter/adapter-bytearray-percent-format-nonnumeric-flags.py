fmt = bytearray(b"%#05s")
out = fmt % b"xy"

result = (
    isinstance(out, bytearray)
    and not isinstance(out, bytes)
    and out == bytearray(b"   xy")
    and fmt == bytearray(b"%#05s")
)

assert result
result
