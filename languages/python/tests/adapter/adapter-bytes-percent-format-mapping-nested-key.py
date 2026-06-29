out = b"%(f(o)o)b|%((x))b|%()d" % {
    b"f(o)o": b"abc",
    b"(x)": b"xy",
    b"": 7,
}

result = out == b"abc|xy|7"

assert result
result
