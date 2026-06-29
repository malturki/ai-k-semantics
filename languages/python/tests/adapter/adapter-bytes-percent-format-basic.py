fmt = b"%b:%s:%a:%r:%c:%%"
value = fmt % (b"hi", bytearray(b"there"), "é", b"x", 65)

single_ok = (
    b"%b" % memoryview(b"mv") == b"mv"
    and b"%b" % (b"tuple",) == b"tuple"
)

literal_ok = (
    b"plain %% ok" % () == b"plain % ok"
    and b"plain" % dict() == b"plain"
)

result = (
    value == b"hi:there:'\\xe9':b'x':A:%"
    and single_ok
    and literal_ok
)

assert result
result
