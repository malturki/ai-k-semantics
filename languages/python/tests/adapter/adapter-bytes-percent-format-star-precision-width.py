result = (
    (b"%5.*b|%-5.*b|%+.*r" % (1, b"xyz", 1, b"xyz", 4, "xyz"))
    == b"    x|x    |'xyz"
)

assert result
result
