data = b"01\t012\t0123\t01234"
simple = b"a\tb"
terminal = b"ab\t"
only_tab = b"\t"
empty = b""
no_tabs = b"abc"
newline_lf = b"a\n\tb"
newline_cr = b"a\r\tb"
newline_crlf = b"a\r\n\tb"

basic_ok = (
    data.expandtabs() == b"01      012     0123    01234"
    and data.expandtabs(8) == b"01      012     0123    01234"
    and data.expandtabs(4) == b"01  012 0123    01234"
    and simple.expandtabs(4) == b"a   b"
    and terminal.expandtabs(4) == b"ab  "
    and only_tab.expandtabs(4) == b"    "
    and empty.expandtabs() == b""
    and no_tabs.expandtabs() == b"abc"
)

nonpositive_ok = (
    data.expandtabs(0) == b"01012012301234"
    and data.expandtabs(-1) == b"01012012301234"
    and simple.expandtabs(False) == b"ab"
    and simple.expandtabs(True) == b"a b"
    and only_tab.expandtabs(0) == b""
)

newline_ok = (
    newline_lf.expandtabs(4) == b"a\n    b"
    and newline_cr.expandtabs(4) == b"a\r    b"
    and newline_crlf.expandtabs(4) == b"a\r\n    b"
    and newline_lf.expandtabs(0) == b"a\nb"
    and newline_cr.expandtabs(-1) == b"a\rb"
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
    data == b"01\t012\t0123\t01234"
    and simple == b"a\tb"
    and terminal == b"ab\t"
    and only_tab == b"\t"
    and empty == b""
    and no_tabs == b"abc"
    and newline_lf == b"a\n\tb"
    and newline_cr == b"a\r\tb"
    and newline_crlf == b"a\r\n\tb"
)

result = basic_ok and nonpositive_ok and newline_ok and type_error_ok and unchanged_ok
assert result
result
