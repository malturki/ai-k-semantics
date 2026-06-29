fmt = bytearray(b"%(word)b:%(num)04d")
out = fmt % {
    b"word": bytearray(b"ba"),
    b"num": 6,
}

result = (
    isinstance(out, bytearray)
    and not isinstance(out, bytes)
    and out == bytearray(b"ba:0006")
    and fmt == bytearray(b"%(word)b:%(num)04d")
)

assert result
result
