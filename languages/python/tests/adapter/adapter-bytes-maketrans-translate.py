table = bytes.maketrans(b"ab", b"AB")
data = b"abracadabra"
one = b"a"
map_a_to_b = bytes.maketrans(b"a", b"b")

table_ok = (
    isinstance(table, bytes)
    and len(table) == 256
    and table[97] == 65
    and table[98] == 66
    and table[99] == 99
    and table[255] == 255
)

translate_ok = (
    data.translate(table) == b"ABrAcAdABrA"
    and data.translate(None) == b"abracadabra"
    and data.translate(table, b"r") == b"ABAcAdABA"
    and data.translate(None, b"aeiou") == b"brcdbr"
    and data.translate(None, delete=b"aeiou") == b"brcdbr"
)

byteslike_table_ok = (
    data.translate(bytearray(table)) == b"ABrAcAdABrA"
    and data.translate(memoryview(table), b"r") == b"ABAcAdABA"
)

delete_before_translate_ok = (
    one.translate(map_a_to_b, b"b") == b"b"
    and one.translate(map_a_to_b, b"a") == b""
)

duplicate_from_ok = bytes.maketrans(b"aa", b"xy")[97] == 121

result = table_ok and translate_ok and byteslike_table_ok
result = result and delete_before_translate_ok and duplicate_from_ok

assert result
result
