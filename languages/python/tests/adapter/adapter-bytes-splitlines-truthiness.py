data = b"a\nb"

truthy_ok = data.splitlines(b"x") == [b"a\n", b"b"]
falsey_ok = data.splitlines(b"") == [b"a", b"b"]

result = truthy_ok and falsey_ok and data == b"a\nb"
assert result
result
