csv = bytearray(b"1,2,,3,")

byteslike_ok = (
    csv.split(bytearray(b","), 2) == [bytearray(b"1"), bytearray(b"2"), bytearray(b",3,")]
    and csv.rsplit(memoryview(bytearray(b",")), 1) == [bytearray(b"1,2,,3"), bytearray()]
)

result = byteslike_ok and csv == bytearray(b"1,2,,3,")
assert result
result
