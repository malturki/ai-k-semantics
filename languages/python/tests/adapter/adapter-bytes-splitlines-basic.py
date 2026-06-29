data = b"ab c\n\nde fg\rkl\r\n"

result = data.splitlines() == [b"ab c", b"", b"de fg", b"kl"]
assert result
result
