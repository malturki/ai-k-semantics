fmt = b"%.3b|%.0b|%.3s|%.5a|%.5r|%.3c|%.3b!"
value = fmt % (b"abcdef", b"abc", bytearray(b"abcdef"), "éé", b"abcdef", 65, b"xyz")

single = b"%.4b" % memoryview(b"abcdef")
tuple_arg = b"%.4b" % (b"tuple",)

result = (
    value == b"abc||abc|'\\xe9|b'abc|A|xyz!"
    and single == b"abcd"
    and tuple_arg == b"tupl"
)

assert result
result
