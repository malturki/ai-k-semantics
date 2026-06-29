fmt = bytearray(b"%+05d|%#06X|%-5.3d")
out = fmt % (12, 12, 12)

result = (
    isinstance(out, bytearray)
    and not isinstance(out, bytes)
    and out == bytearray(b"+0012|0X000C|012  ")
    and fmt == bytearray(b"%+05d|%#06X|%-5.3d")
)

assert result
result
