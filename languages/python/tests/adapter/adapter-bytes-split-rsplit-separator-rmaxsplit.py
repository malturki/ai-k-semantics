csv = b"1,2,,3,"

result = csv.rsplit(b",", 1) == [b"1,2,,3", b""]
assert result
result
