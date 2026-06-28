spacey = bytearray(b" \t\nabc\r ")
vertical = bytearray(b"\v\fabc\v")
data = bytearray(b"abc")
www = bytearray(b"www.example.com")
arthur = bytearray(b"Arthur: three!")
mississippi = bytearray(b"mississippi")
ababa = bytearray(b"ababa")
abca = bytearray(b"abca")
aabc = bytearray(b"aabc")

default_ok = (
    spacey.strip() == bytearray(b"abc")
    and spacey.lstrip() == bytearray(b"abc\r ")
    and spacey.rstrip() == bytearray(b" \t\nabc")
    and spacey.strip(None) == bytearray(b"abc")
    and vertical.strip() == bytearray(b"abc")
)

explicit_ok = (
    www.lstrip(b"cmowz.") == bytearray(b"example.com")
    and arthur.lstrip(b"Arthur: ") == bytearray(b"ee!")
    and mississippi.rstrip(bytearray(b"ipz")) == bytearray(b"mississ")
    and mississippi.strip(b"im") == bytearray(b"ssissipp")
    and ababa.strip(b"ab") == bytearray()
)

bytes_like_ok = (
    abca.strip(memoryview(b"a")) == bytearray(b"bc")
    and aabc.lstrip(memoryview(bytearray(b"a"))) == bytearray(b"bc")
)

empty_set_ok = (
    data.strip(b"") == bytearray(b"abc")
    and data.lstrip(bytearray()) == bytearray(b"abc")
    and data.rstrip(memoryview(b"")) == bytearray(b"abc")
)

type_error_ok = True
try:
    data.strip(97)
    type_error_ok = False
except TypeError:
    pass

try:
    data.lstrip("a")
    type_error_ok = False
except TypeError:
    pass

try:
    data.rstrip([97])
    type_error_ok = False
except TypeError:
    pass

unchanged_ok = spacey == bytearray(b" \t\nabc\r ") and data == bytearray(b"abc")

result = default_ok and explicit_ok and bytes_like_ok and empty_set_ok and type_error_ok and unchanged_ok
assert result
result
