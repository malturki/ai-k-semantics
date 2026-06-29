data = b"banana"

result = (
    data.startswith((b"x", b""), 2, 2)
    and not data.startswith((b"x", b""), 2, 1)
    and data.startswith((b"z", b"ba"), 0, 2)
    and data.endswith((b"zz", b"na"), 0, 6)
    and not data.endswith((b"x", b""), 100, 200)
)

assert result
result
