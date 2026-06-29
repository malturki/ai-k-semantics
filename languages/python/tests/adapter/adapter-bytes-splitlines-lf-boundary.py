lf = b"a\nb"

result = lf.splitlines() == [b"a", b"b"] and lf.splitlines(True) == [b"a\n", b"b"]
assert result
result
