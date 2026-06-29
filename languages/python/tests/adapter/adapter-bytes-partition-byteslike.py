data = b"a:b:c"
double = b"ab<>cd<>ef"

byteslike_ok = (
    data.partition(bytearray(b":")) == (b"a", b":", b"b:c")
    and data.rpartition(memoryview(b":")) == (b"a:b", b":", b"c")
)

multibyte_ok = (
    double.partition(b"<>") == (b"ab", b"<>", b"cd<>ef")
    and double.rpartition(bytearray(b"<>")) == (b"ab<>cd", b"<>", b"ef")
)

result = byteslike_ok and multibyte_ok and data == b"a:b:c" and double == b"ab<>cd<>ef"
assert result
result
