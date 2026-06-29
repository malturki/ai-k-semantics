fmt = bytearray(b"%b-%c-%%")
out = fmt % (memoryview(b"xy"), bytearray(b"Z"))

result = (
    isinstance(out, bytearray)
    and not isinstance(out, bytes)
    and out == bytearray(b"xy-Z-%")
    and fmt == bytearray(b"%b-%c-%%")
)

assert result
result
