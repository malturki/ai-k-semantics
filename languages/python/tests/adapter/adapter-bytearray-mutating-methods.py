data = bytearray()

append_ret = data.append(65)
append_bool_ret = data.append(True)
extend_bytes_ret = data.extend(b"BC")
extend_bytearray_ret = data.extend(bytearray(b"D"))
extend_list_ret = data.extend([69, False, 255])
extend_tuple_ret = data.extend((70,))
extend_dict_ret = data.extend({71: "G"})
extend_set_ret = data.extend({72})
extend_range_ret = data.extend(range(73, 75))
extend_memoryview_ret = data.extend(memoryview(b"KL"))

empty_ret_1 = data.extend([])
empty_ret_2 = data.extend(())
empty_ret_3 = data.extend({})
empty_ret_4 = data.extend(set())
empty_ret_5 = data.extend(b"")
empty_ret_6 = data.extend(bytearray())
empty_ret_7 = data.extend(memoryview(b""))
empty_ret_8 = data.extend(range(0))

expected = [65, 1, 66, 67, 68, 69, 0, 255, 70, 71, 72, 73, 74, 75, 76]
returns_ok = (
    append_ret is None
    and append_bool_ret is None
    and extend_bytes_ret is None
    and extend_bytearray_ret is None
    and extend_list_ret is None
    and extend_tuple_ret is None
    and extend_dict_ret is None
    and extend_set_ret is None
    and extend_range_ret is None
    and extend_memoryview_ret is None
    and empty_ret_1 is None
    and empty_ret_2 is None
    and empty_ret_3 is None
    and empty_ret_4 is None
    and empty_ret_5 is None
    and empty_ret_6 is None
    and empty_ret_7 is None
    and empty_ret_8 is None
)
mutation_ok = list(data) == expected and data == bytearray(expected)

before_errors = bytearray(data)
errors_ok = True

try:
    data.append(256)
except ValueError:
    pass
else:
    errors_ok = False

try:
    data.append(-1)
except ValueError:
    pass
else:
    errors_ok = False

try:
    data.append("x")
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.extend([1, "x"])
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.extend([256])
except ValueError:
    pass
else:
    errors_ok = False

try:
    data.extend("ab")
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.extend(3)
except TypeError:
    pass
else:
    errors_ok = False

errors_ok = errors_ok and data == before_errors

result = returns_ok and mutation_ok and errors_ok
assert result
result
