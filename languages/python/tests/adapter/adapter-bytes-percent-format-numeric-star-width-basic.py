result = (
    (b"%*d|%*x|%#*x" % (5, 12, 5, 12, 5, 12))
    == b"   12|    c|  0xc"
)

assert result
result
