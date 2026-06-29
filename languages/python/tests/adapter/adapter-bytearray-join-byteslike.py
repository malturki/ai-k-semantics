dash = bytearray(b"-")
joined = dash.join([bytearray(b"a"), memoryview(b"b")])

result = joined == bytearray(b"a-b") and isinstance(joined, bytearray)
assert result
result
