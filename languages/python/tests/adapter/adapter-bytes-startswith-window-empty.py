data = b"banana"

result = (
    data.startswith(b"", 2, 2)
    and not data.startswith(b"", 2, 1)
    and not data.startswith(b"", 100, 200)
    and not data.startswith(b"a", False, True)
)

assert result
result
