value = bytearray.fromhex("2Ef0 F1f2  ")
empty = bytearray.fromhex(" \t\n\r\f\v")

result = value == bytearray(b".\xf0\xf1\xf2") and empty == bytearray() and isinstance(value, bytearray)
assert result
result
