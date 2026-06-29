data = b"banana"

result = (
    data.find(b"an", 2) == 3
    and data.find(97, 2, 5) == 3
    and data.find(memoryview(b"an"), 0, 3) == 1
    and data.find(b"", 2, 2) == 2
    and data.find(b"", 100, 200) == -1
    and data.find(b"an", None, None) == 1
    and data.rfind(b"an", 0, 3) == 1
    and data.rfind(b"an", 0, 5) == 3
    and data.rfind(97, 1, 5) == 3
    and data.rfind(b"", 1, 5) == 5
    and data.rfind(b"", 2, 1) == -1
    and data.rfind(b"a", False, True) == -1
    and data == b"banana"
)

assert result
result
