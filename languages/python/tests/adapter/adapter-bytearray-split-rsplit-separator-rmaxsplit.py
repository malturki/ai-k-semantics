csv = bytearray(b"1,2,,3,")

result = csv.rsplit(b",", 1) == [bytearray(b"1,2,,3"), bytearray()]
assert result
result
