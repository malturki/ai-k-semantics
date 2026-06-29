words = bytearray(b"  a  b c  ")

maxsplit_ok = (
    words.split(None, 1) == [bytearray(b"a"), bytearray(b"b c  ")]
    and words.rsplit(None, 1) == [bytearray(b"  a  b"), bytearray(b"c")]
)

result = maxsplit_ok and words == bytearray(b"  a  b c  ")
assert result
result
