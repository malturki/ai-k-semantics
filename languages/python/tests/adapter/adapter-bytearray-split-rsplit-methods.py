words = bytearray(b"  a  b c  ")

result = words.split() == [bytearray(b"a"), bytearray(b"b"), bytearray(b"c")]
assert result
result
