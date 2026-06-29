data = b"a\nb"

result = data.splitlines(True) == [b"a\n", b"b"] and data == b"a\nb"
assert result
result
