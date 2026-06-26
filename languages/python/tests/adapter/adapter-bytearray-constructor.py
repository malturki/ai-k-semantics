empty = bytearray()
zero_filled = bytearray(3)
false_size = bytearray(False)
true_size = bytearray(True)
from_bytes = bytearray(b"Az\xff")
from_bytearray = bytearray(bytearray(b"ab"))
from_list = bytearray([65, 66, 67])
from_bool_items = bytearray([True, False, 2])
from_tuple = bytearray((0, 1, 255))
from_range = bytearray(range(4))
from_step_range = bytearray(range(0, 6, 2))
from_desc_range = bytearray(range(3, 0, -1))
from_dict_keys = bytearray({65: "a", 66: "b"})
from_singleton_set = bytearray({67})
from_utf8 = bytearray("A\xe9", "utf-8")
from_ascii_ignore = bytearray("A\xe9", "ascii", "ignore")
from_latin_replace = bytearray("A\u0100", "latin-1", "replace")

result = len(empty) == 0 and empty == bytearray(b"")
result = result and repr(empty) == "bytearray(b'')"
result = result and str(from_bytes) == "bytearray(b'Az\\xff')"
result = result and bool(empty) is False and bool(zero_filled) is True
result = result and zero_filled == bytearray(b"\x00\x00\x00")
result = result and false_size == bytearray(b"")
result = result and true_size == bytearray(b"\x00")
result = result and from_bytes == bytearray(b"Az\xff")
result = result and from_bytes == b"Az\xff" and b"Az\xff" == from_bytes
result = result and from_bytearray == bytearray(b"ab")
result = result and bytes(from_bytes) == b"Az\xff"
result = result and from_list == bytearray(b"ABC")
result = result and from_bool_items == bytearray(b"\x01\x00\x02")
result = result and list(from_tuple) == [0, 1, 255]
result = result and tuple(from_tuple) == (0, 1, 255)
result = result and set(bytearray([0, 0, 1])) == {0, 1}
result = result and from_range == bytearray(b"\x00\x01\x02\x03")
result = result and list(from_step_range) == [0, 2, 4]
result = result and list(from_desc_range) == [3, 2, 1]
result = result and from_dict_keys == bytearray(b"AB")
result = result and from_singleton_set == bytearray(b"C")
result = result and from_utf8 == bytearray(b"A\xc3\xa9")
result = result and from_ascii_ignore == bytearray(b"A")
result = result and from_latin_replace == bytearray(b"A?")
result = result and isinstance(from_bytes, bytearray)
result = result and not isinstance(from_bytes, bytes)
result = result and bytearray(b"a") < bytearray(b"b")
result = result and bytearray(b"a") < b"b"
result = result and b"a" < bytearray(b"b")
result = result and bytearray(b"a") + b"b" == bytearray(b"ab")
result = result and b"a" + bytearray(b"b") == b"ab"
result = result and bytearray(b"a") * 2 == bytearray(b"aa")
result = result and 2 * bytearray(b"a") == bytearray(b"aa")
result = result and bytearray(b"abc")[0] == 97
result = result and bytearray(b"abc")[-1] == 99
result = result and bytearray(b"abc")[1:] == bytearray(b"bc")
result = result and bytearray(b"abc")[::-1] == bytearray(b"cba")

total = 0
for item in bytearray(b"\x01\x02\x03"):
    total += item
result = result and total == 6

first, second = bytearray(b"AZ")
result = result and first == 65 and second == 90

head, *tail = bytearray(b"abc")
result = result and head == 97 and tail == [98, 99]

match from_bytes:
    case bytearray():
        matched_zero = True
    case _:
        matched_zero = False

match from_bytes:
    case bytearray(captured):
        matched_one = captured == from_bytes
    case _:
        matched_one = False

result = result and matched_zero and matched_one

assert result
result
