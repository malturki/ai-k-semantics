result = (
    (b"%0*d|%-*d|%+*d|%0*d" % (5, 12, 5, 12, 5, 12, -5, 12))
    == b"00012|12   |  +12|12   "
)

assert result
result
