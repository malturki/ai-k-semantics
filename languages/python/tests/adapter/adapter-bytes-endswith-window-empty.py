data = b"banana"

result = (
    data.endswith(b"", 6, 6)
    and not data.endswith(b"", 7, 7)
    and data.endswith(b"a", None, None)
)

assert result
result
