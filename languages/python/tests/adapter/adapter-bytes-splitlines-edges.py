empty = b""

result = empty.splitlines() == [] and empty.splitlines(True) == []
assert result
result
