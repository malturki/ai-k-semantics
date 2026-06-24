empty = bytes()
zero_filled = bytes(3)
false_size = bytes(False)
true_size = bytes(True)
from_bytes = bytes(b"ab")
from_list = bytes([65, 66, 67])
from_bool_items = bytes([True, False, 2])
from_tuple = bytes((0, 1, 255))
from_range = bytes(range(4))
from_step_range = bytes(range(0, 6, 2))
from_desc_range = bytes(range(3, 0, -1))
from_dict_keys = bytes({65: "a", 66: "b"})
from_singleton_set = bytes({67})

result = len(empty) == 0 and empty == b""
result = result and zero_filled == b"\x00\x00\x00"
result = result and false_size == b""
result = result and true_size == b"\x00"
result = result and from_bytes == b"ab"
result = result and from_list == b"ABC"
result = result and from_bool_items == b"\x01\x00\x02"
result = result and list(from_tuple) == [0, 1, 255]
result = result and from_range == b"\x00\x01\x02\x03"
result = result and list(from_step_range) == [0, 2, 4]
result = result and list(from_desc_range) == [3, 2, 1]
result = result and from_dict_keys == b"AB"
result = result and from_singleton_set == b"C"

assert result
result
