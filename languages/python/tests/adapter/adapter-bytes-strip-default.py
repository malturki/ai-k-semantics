spacey = b" \t\nabc\r "
vertical = b"\v\fabc\v"
plain = b"abc"

result = (
    spacey.strip() == b"abc"
    and spacey.lstrip() == b"abc\r "
    and spacey.rstrip() == b" \t\nabc"
    and spacey.strip(None) == b"abc"
    and plain.strip(None) == b"abc"
    and vertical.strip() == b"abc"
    and spacey == b" \t\nabc\r "
)

assert result
result
