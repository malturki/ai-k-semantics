remove_data = bytearray(b"banana")
remove_first = remove_data.remove(97)
remove_second = remove_data.remove(110)

remove_bool_data = bytearray([0, 1, 1])
remove_bool = remove_bool_data.remove(True)

remove_ok = (
    remove_first is None
    and remove_second is None
    and remove_data == bytearray(b"bana")
    and remove_bool is None
    and remove_bool_data == bytearray([0, 1])
)

insert_data = bytearray(b"bd")
insert_front = insert_data.insert(0, 97)
insert_middle = insert_data.insert(2, 99)
insert_end = insert_data.insert(99, 101)
insert_low = insert_data.insert(-99, 120)
insert_negative = insert_data.insert(-1, 121)

insert_bool_data = bytearray([2])
insert_bool = insert_bool_data.insert(False, True)

insert_ok = (
    insert_front is None
    and insert_middle is None
    and insert_end is None
    and insert_low is None
    and insert_negative is None
    and insert_data == bytearray(b"xabcdye")
    and insert_bool is None
    and insert_bool_data == bytearray([1, 2])
)

errors_ok = True

remove_errors_data = bytearray(b"ab")

try:
    remove_errors_data.remove(120)
except ValueError:
    pass
else:
    errors_ok = False

try:
    remove_errors_data.remove(300)
except ValueError:
    pass
else:
    errors_ok = False

try:
    remove_errors_data.remove(-1)
except ValueError:
    pass
else:
    errors_ok = False

try:
    remove_errors_data.remove(1.0)
except TypeError:
    pass
else:
    errors_ok = False

try:
    remove_errors_data.remove("a")
except TypeError:
    pass
else:
    errors_ok = False

insert_errors_data = bytearray(b"ab")

try:
    insert_errors_data.insert(1.0, 120)
except TypeError:
    pass
else:
    errors_ok = False

try:
    insert_errors_data.insert(1, 1.0)
except TypeError:
    pass
else:
    errors_ok = False

try:
    insert_errors_data.insert(1, 300)
except ValueError:
    pass
else:
    errors_ok = False

try:
    insert_errors_data.insert(1, -1)
except ValueError:
    pass
else:
    errors_ok = False

errors_ok = (
    errors_ok
    and remove_errors_data == bytearray(b"ab")
    and insert_errors_data == bytearray(b"ab")
)

result = remove_ok and insert_ok and errors_ok
assert result
result
