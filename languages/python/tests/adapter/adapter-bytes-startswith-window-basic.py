data = b"banana"

result = (
    data.startswith(b"ba", 0, 6)
    and not data.startswith(b"ba", 1, 5)
    and data.startswith(b"an", 1, 5)
    and data.startswith(bytearray(b"na"), -4, -1)
    and data.startswith(memoryview(b"an"), 1, 5)
)

assert result
result
