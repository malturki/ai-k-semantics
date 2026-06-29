data = b"banana"
triple = b"aaa"

basic_ok = (
    data.replace(b"na", b"XY") == b"baXYXY"
    and data.replace(b"z", b"Q") == b"banana"
    and triple.replace(b"aa", b"X") == b"Xa"
)

count_ok = (
    data.replace(b"a", b"A", 0) == b"banana"
    and data.replace(b"a", b"A", 1) == b"bAnana"
    and data.replace(b"a", b"A", 2) == b"bAnAna"
    and data.replace(b"a", b"A", -1) == b"bAnAnA"
    and data.replace(b"a", b"A", True) == b"bAnana"
    and data.replace(b"a", b"A", False) == b"banana"
)

unchanged_ok = data == b"banana" and triple == b"aaa"

result = basic_ok and count_ok and unchanged_ok
assert result
result
