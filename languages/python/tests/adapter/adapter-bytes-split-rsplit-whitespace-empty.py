empty = b""
spaces = b"   "

result = empty.split() == [] and spaces.rsplit() == []
assert result
result
