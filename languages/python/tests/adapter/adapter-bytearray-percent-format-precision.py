fmt = bytearray(b"%.2b:%.4r:%.2c")
out = fmt % (memoryview(b"abcdef"), b"abcdef", bytearray(b"Z"))

result = (
    isinstance(out, bytearray)
    and not isinstance(out, bytes)
    and out == bytearray(b"ab:b'ab:Z")
    and fmt == bytearray(b"%.2b:%.4r:%.2c")
)

assert result
result
