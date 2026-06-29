data = b"banana"

result = (
    data.count(b"an", 1) == 2
    and data.count(b"an", 2, 5) == 1
    and data.count(bytearray(b"na"), 2, 6) == 2
    and data.count(memoryview(b"an"), 0, 3) == 1
    and data.count(97, -4, -1) == 1
    and data.count(b"", 2, 2) == 1
    and data.count(b"", 2, 1) == 0
    and data == b"banana"
)

assert result
result
