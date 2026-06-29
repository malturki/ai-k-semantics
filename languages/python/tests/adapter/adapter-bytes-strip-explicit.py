www = b"www.example.com"
arthur = b"Arthur: three!"
mississippi = b"mississippi"
ababa = b"ababa"

result = (
    www.lstrip(b"cmowz.") == b"example.com"
    and arthur.lstrip(b"Arthur: ") == b"ee!"
    and mississippi.rstrip(bytearray(b"ipz")) == b"mississ"
    and mississippi.strip(b"im") == b"ssissipp"
    and ababa.strip(b"ab") == b""
    and www == b"www.example.com"
)

assert result
result
