result = (
    (b"%*.3d|%*.3lx" % (5, 12, 5, 12))
    == b"  012|  00c"
)

assert result
result
