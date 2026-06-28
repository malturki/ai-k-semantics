data = bytearray(b"abc")
copied = data.copy()

reverse_ret = data.reverse()
reverse_ok = reverse_ret is None and data == bytearray(b"cba")
copy_initial_ok = copied == bytearray(b"abc")

copied_append_ret = copied.append(120)
copy_independent_ok = (
    copied_append_ret is None
    and copied == bytearray(b"abcx")
    and data == bytearray(b"cba")
)

clear_ret = data.clear()
clear_ok = clear_ret is None and data == bytearray() and list(data) == []
copy_after_clear_ok = copied == bytearray(b"abcx")

empty = bytearray()
empty_copy = empty.copy()
empty_reverse_ret = empty.reverse()
empty_clear_ret = empty.clear()
empty_ok = (
    empty_copy == bytearray()
    and empty_reverse_ret is None
    and empty_clear_ret is None
    and empty == bytearray()
)

data.extend([1, 2, 3])
post_clear_extend_ok = data == bytearray([1, 2, 3])

result = (
    reverse_ok
    and copy_initial_ok
    and copy_independent_ok
    and clear_ok
    and copy_after_clear_ok
    and empty_ok
    and post_clear_extend_ok
)
assert result
result
