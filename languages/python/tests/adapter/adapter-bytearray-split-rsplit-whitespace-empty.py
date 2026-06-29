empty = bytearray()
spaces = bytearray(b"   ")

result = empty.split() == [] and spaces.rsplit() == []
assert result
result
