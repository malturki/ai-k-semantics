cr = b"a\rb"

result = cr.splitlines() == [b"a", b"b"] and cr.splitlines(True) == [b"a\r", b"b"]
assert result
result
