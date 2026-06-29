result = (
    (b"%.*b|%.*s|%.*c" % (1, b"xyz", 2, b"xyz", -1, 65))
    == b"x|xy|A"
)

assert result
result
