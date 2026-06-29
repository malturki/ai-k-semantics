data = bytearray(b"01\t012\t0123\t01234")
simple = bytearray(b"a\tb")
terminal = bytearray(b"ab\t")
only_tab = bytearray(b"\t")
empty = bytearray()
no_tabs = bytearray(b"abc")
newline_lf = bytearray(b"a\n\tb")
newline_cr = bytearray(b"a\r\tb")
newline_crlf = bytearray(b"a\r\n\tb")

basic_ok = (
    data.expandtabs() == bytearray(b"01      012     0123    01234")
    and data.expandtabs(8) == bytearray(b"01      012     0123    01234")
    and data.expandtabs(4) == bytearray(b"01  012 0123    01234")
    and simple.expandtabs(4) == bytearray(b"a   b")
    and terminal.expandtabs(4) == bytearray(b"ab  ")
    and only_tab.expandtabs(4) == bytearray(b"    ")
    and empty.expandtabs() == bytearray()
    and no_tabs.expandtabs() == bytearray(b"abc")
)

nonpositive_ok = (
    data.expandtabs(0) == bytearray(b"01012012301234")
    and data.expandtabs(-1) == bytearray(b"01012012301234")
    and simple.expandtabs(False) == bytearray(b"ab")
    and simple.expandtabs(True) == bytearray(b"a b")
    and only_tab.expandtabs(0) == bytearray()
)

newline_ok = (
    newline_lf.expandtabs(4) == bytearray(b"a\n    b")
    and newline_cr.expandtabs(4) == bytearray(b"a\r    b")
    and newline_crlf.expandtabs(4) == bytearray(b"a\r\n    b")
    and newline_lf.expandtabs(0) == bytearray(b"a\nb")
    and newline_cr.expandtabs(-1) == bytearray(b"a\rb")
)

type_error_ok = True
try:
    simple.expandtabs(1.0)
    type_error_ok = False
except TypeError:
    pass

try:
    simple.expandtabs("4")
    type_error_ok = False
except TypeError:
    pass

try:
    simple.expandtabs(None)
    type_error_ok = False
except TypeError:
    pass

try:
    simple.expandtabs([])
    type_error_ok = False
except TypeError:
    pass

try:
    simple.expandtabs(b"4")
    type_error_ok = False
except TypeError:
    pass

unchanged_ok = (
    data == bytearray(b"01\t012\t0123\t01234")
    and simple == bytearray(b"a\tb")
    and terminal == bytearray(b"ab\t")
    and only_tab == bytearray(b"\t")
    and empty == bytearray()
    and no_tabs == bytearray(b"abc")
    and newline_lf == bytearray(b"a\n\tb")
    and newline_cr == bytearray(b"a\r\tb")
    and newline_crlf == bytearray(b"a\r\n\tb")
)

result = basic_ok and nonpositive_ok and newline_ok and type_error_ok and unchanged_ok
assert result
result
