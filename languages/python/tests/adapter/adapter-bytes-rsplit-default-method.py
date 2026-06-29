words = b"  a  b c  "

result = words.rsplit(None) == [b"a", b"b", b"c"]
assert result
result
