csv = b"1,2,,3,"

byteslike_ok = (
    csv.split(bytearray(b","), 2) == [b"1", b"2", b",3,"]
    and csv.rsplit(memoryview(bytearray(b",")), 1) == [b"1,2,,3", b""]
)

result = byteslike_ok and csv == b"1,2,,3,"
assert result
result
