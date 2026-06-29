result = (
    (b"%*.*b|%*.*b" % (5, 1, b"xyz", -5, 1, b"xyz"))
    == b"    x|x    "
)

assert result
result
