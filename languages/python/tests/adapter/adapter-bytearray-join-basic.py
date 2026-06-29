dash = bytearray(b"-")
joined = dash.join([b"a", b"b"])

result = joined == bytearray(b"a-b") and dash == bytearray(b"-")
assert result
result
