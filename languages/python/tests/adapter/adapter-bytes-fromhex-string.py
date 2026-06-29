value = bytes.fromhex("2Ef0 F1f2  ")
empty = bytes.fromhex(" \t\n\r\f\v")

result = value == b".\xf0\xf1\xf2" and empty == b"" and isinstance(value, bytes)
assert result
result
