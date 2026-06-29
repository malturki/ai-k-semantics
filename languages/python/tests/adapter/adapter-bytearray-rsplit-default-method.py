words = bytearray(b"  a  b c  ")

result = words.rsplit(None) == [bytearray(b"a"), bytearray(b"b"), bytearray(b"c")]
assert result
result
