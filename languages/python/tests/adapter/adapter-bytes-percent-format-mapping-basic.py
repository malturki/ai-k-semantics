fmt = b"%(foo)b:%(bar)s:%(repr)r:%(char)c:%%:%(foo)b"
out = fmt % {
    b"foo": b"abc",
    b"bar": bytearray(b"def"),
    b"repr": "é",
    b"char": 65,
}

result = out == b"abc:def:'\\xe9':A:%:abc"

assert result
result
