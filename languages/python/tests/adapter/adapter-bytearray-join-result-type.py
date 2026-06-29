dash = bytearray(b"-")
joined = dash.join([b"a"])

result = joined == bytearray(b"a") and isinstance(joined, bytearray)
assert result
result
