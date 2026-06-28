data = bytearray(b"ab c\n\nde fg\rkl\r\n")
empty = bytearray()
terminal = bytearray(b"One line\n")
crlf = bytearray(b"a\r\nb")
cr = bytearray(b"a\rb")
lf = bytearray(b"a\nb")
double_lf = bytearray(b"\n\n")
not_boundaries = bytearray(b"a\x0b b\x0c c")

basic_ok = data.splitlines() == [
    bytearray(b"ab c"),
    bytearray(b""),
    bytearray(b"de fg"),
    bytearray(b"kl"),
]

keep_ok = data.splitlines(True) == [
    bytearray(b"ab c\n"),
    bytearray(b"\n"),
    bytearray(b"de fg\r"),
    bytearray(b"kl\r\n"),
]

truthy_ok = (
    data.splitlines(1) == data.splitlines(True)
    and data.splitlines(2) == data.splitlines(True)
    and data.splitlines([1]) == data.splitlines(True)
    and data.splitlines(b"x") == data.splitlines(True)
    and data.splitlines(0) == data.splitlines()
    and data.splitlines(False) == data.splitlines()
    and data.splitlines("") == data.splitlines()
    and data.splitlines([]) == data.splitlines()
    and data.splitlines(b"") == data.splitlines()
)

edge_ok = (
    empty.splitlines() == []
    and empty.splitlines(True) == []
    and terminal.splitlines() == [bytearray(b"One line")]
    and terminal.splitlines(True) == [bytearray(b"One line\n")]
    and crlf.splitlines() == [bytearray(b"a"), bytearray(b"b")]
    and crlf.splitlines(True) == [bytearray(b"a\r\n"), bytearray(b"b")]
    and cr.splitlines() == [bytearray(b"a"), bytearray(b"b")]
    and cr.splitlines(True) == [bytearray(b"a\r"), bytearray(b"b")]
    and lf.splitlines() == [bytearray(b"a"), bytearray(b"b")]
    and lf.splitlines(True) == [bytearray(b"a\n"), bytearray(b"b")]
    and double_lf.splitlines() == [bytearray(b""), bytearray(b"")]
    and double_lf.splitlines(True) == [bytearray(b"\n"), bytearray(b"\n")]
    and not_boundaries.splitlines() == [bytearray(b"a\x0b b\x0c c")]
)

unchanged_ok = (
    data == bytearray(b"ab c\n\nde fg\rkl\r\n")
    and empty == bytearray()
    and terminal == bytearray(b"One line\n")
    and crlf == bytearray(b"a\r\nb")
    and cr == bytearray(b"a\rb")
    and lf == bytearray(b"a\nb")
    and double_lf == bytearray(b"\n\n")
    and not_boundaries == bytearray(b"a\x0b b\x0c c")
)

result = basic_ok and keep_ok and truthy_ok and edge_ok and unchanged_ok
assert result
result
