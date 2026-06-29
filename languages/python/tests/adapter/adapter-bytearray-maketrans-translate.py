table = bytearray.maketrans(bytearray(b"ab"), memoryview(b"xy"))
data = bytearray(b"abracadabra")
out = data.translate(table)

table_ok = isinstance(table, bytes) and len(table) == 256 and table[97] == 120 and table[98] == 121

translate_ok = (
    isinstance(out, bytearray)
    and not isinstance(out, bytes)
    and out == bytearray(b"xyrxcxdxyrx")
    and data.translate(None) == bytearray(b"abracadabra")
    and data.translate(table, memoryview(b"r")) == bytearray(b"xyxcxdxyx")
    and data.translate(None, b"r") == bytearray(b"abacadaba")
    and data.translate(None, delete=bytearray(b"a")) == bytearray(b"brcdbr")
)

byteslike_table_ok = data.translate(memoryview(table), b"b") == bytearray(b"xrxcxdxrx")

unchanged_ok = data == bytearray(b"abracadabra")

result = table_ok and translate_ok and byteslike_table_ok and unchanged_ok

assert result
result
