multi = bytearray(b"1<>2<>3<4")

result = multi.rsplit(b"<>", 1) == [bytearray(b"1<>2"), bytearray(b"3<4")]
assert result
result
