fmt = b"%5b|%-5s|%6.3a|%-6.3r|%3c!"
value = fmt % (b"xy", bytearray(b"xy"), "é", b"abcdef", 65)

single = b"%6b" % memoryview(b"xy")
with_precision = b"%6.4b" % b"abcdef"

result = (
    value == b"   xy|xy   |   '\\x|b'a   |  A!"
    and single == b"    xy"
    and with_precision == b"  abcd"
)

assert result
result
