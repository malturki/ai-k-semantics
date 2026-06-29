double_lf = b"\n\n"

result = double_lf.splitlines() == [b"", b""] and double_lf.splitlines(True) == [b"\n", b"\n"]
assert result
result
