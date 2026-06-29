data = b"abc"
abca = b"abca"
aabc = b"aabc"

result = (
    abca.strip(memoryview(b"a")) == b"bc"
    and aabc.lstrip(memoryview(bytearray(b"a"))) == b"bc"
    and data.strip(b"") == b"abc"
    and data.lstrip(bytearray()) == b"abc"
    and data.rstrip(memoryview(b"")) == b"abc"
)

assert result
result
