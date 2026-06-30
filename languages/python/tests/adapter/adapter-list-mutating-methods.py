data = []

append_ret = data.append(1)
append_str_ret = data.append("x")
extend_empty_ret = data.extend([])
extend_tuple_ret = data.extend((2,))
extend_string_ret = data.extend("ab")
extend_bytes_ret = data.extend(b"CD")
extend_bytearray_ret = data.extend(bytearray(b"E"))
extend_memoryview_ret = data.extend(memoryview(b"F"))
extend_dict_ret = data.extend({70: "g"})
extend_set_ret = data.extend({71})
extend_range_ret = data.extend(range(72, 74))

expected = [1, "x", 2, "a", "b", 67, 68, 69, 70, 70, 71, 72, 73]
append_extend_ok = (
    append_ret is None
    and append_str_ret is None
    and extend_empty_ret is None
    and extend_tuple_ret is None
    and extend_string_ret is None
    and extend_bytes_ret is None
    and extend_bytearray_ret is None
    and extend_memoryview_ret is None
    and extend_dict_ret is None
    and extend_set_ret is None
    and extend_range_ret is None
    and data == expected
)

copy_value = data.copy()
copy_append_ret = copy_value.append("copy")
clear_target = [9]
clear_ret = clear_target.clear()
reverse_target = [1, 2, 3]
reverse_ret = reverse_target.reverse()

zero_arg_ok = (
    copy_append_ret is None
    and copy_value == expected + ["copy"]
    and data == expected
    and clear_ret is None
    and clear_target == []
    and reverse_ret is None
    and reverse_target == [3, 2, 1]
)

pop_data = [10, 20, 30, 40]
pop_last = pop_data.pop()
pop_first = pop_data.pop(0)
pop_neg = pop_data.pop(-1)
pop_bool = pop_data.pop(False)

pop_ok = (
    pop_last == 40
    and pop_first == 10
    and pop_neg == 30
    and pop_bool == 20
    and pop_data == []
)

remove_data = ["x", "y", "x"]
remove_ret = remove_data.remove("x")

remove_ok = remove_ret is None and remove_data == ["y", "x"]

insert_data = [2, 4]
insert_ret_0 = insert_data.insert(0, 1)
insert_ret_1 = insert_data.insert(2, 3)
insert_ret_2 = insert_data.insert(99, 5)
insert_ret_3 = insert_data.insert(-99, 0)
insert_ret_4 = insert_data.insert(-1, 99)
insert_empty = []
insert_ret_5 = insert_empty.insert(True, "t")

insert_ok = (
    insert_ret_0 is None
    and insert_ret_1 is None
    and insert_ret_2 is None
    and insert_ret_3 is None
    and insert_ret_4 is None
    and insert_ret_5 is None
    and insert_data == [0, 1, 2, 3, 4, 99, 5]
    and insert_empty == ["t"]
)

errors_ok = True
empty = []
mut = [1, 2]

try:
    empty.pop()
except IndexError:
    pass
else:
    errors_ok = False

try:
    mut.pop("0")
except TypeError:
    pass
else:
    errors_ok = False

try:
    mut.pop(9)
except IndexError:
    pass
else:
    errors_ok = False

try:
    mut.remove(3)
except ValueError:
    pass
else:
    errors_ok = False

try:
    mut.insert("bad", 0)
except TypeError:
    pass
else:
    errors_ok = False

try:
    mut.extend(3)
except TypeError:
    pass
else:
    errors_ok = False

errors_ok = errors_ok and empty == [] and mut == [1, 2]

result = append_extend_ok and zero_arg_ok and pop_ok and remove_ok and insert_ok and errors_ok
assert result
result
