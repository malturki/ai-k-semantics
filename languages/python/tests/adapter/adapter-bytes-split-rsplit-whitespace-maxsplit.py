words = b"  a  b c  "

maxsplit_ok = (
    words.split(None, 1) == [b"a", b"b c  "]
    and words.rsplit(None, 1) == [b"  a  b", b"c"]
)

result = maxsplit_ok and words == b"  a  b c  "
assert result
result
