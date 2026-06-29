multi = b"1<>2<>3<4"

result = multi.rsplit(b"<>", 1) == [b"1<>2", b"3<4"]
assert result
result
