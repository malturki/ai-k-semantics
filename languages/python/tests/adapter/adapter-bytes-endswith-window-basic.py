data = b"banana"

result = (
    data.endswith(b"na", 0, 6)
    and not data.endswith(b"na", 1, 5)
    and data.endswith(b"an", 1, 5)
    and data.endswith(bytearray(b"an"), -4, -1)
    and data.endswith(memoryview(b"na"), 0, 6)
)

assert result
result
