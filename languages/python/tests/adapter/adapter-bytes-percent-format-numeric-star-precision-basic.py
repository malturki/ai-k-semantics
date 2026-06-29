result = (
    (b"%.*d|%.*x|%.*u" % (3, 12, 3, 12, -1, 12))
    == b"012|00c|12"
)

assert result
result
