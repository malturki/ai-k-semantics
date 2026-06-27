total = 0
for byte in memoryview(b"abc"):
    total += byte

bytearray_total = 0
for byte in memoryview(bytearray(b"\x01\x02")):
    bytearray_total += byte

else_total = 0
for byte in memoryview(b"\x02"):
    else_total += byte
else:
    else_total += 40

list_ok = list(memoryview(b"abc")) == [97, 98, 99]
tuple_ok = tuple(memoryview(b"xy")) == (120, 121)
set_ok = set(memoryview(b"aba")) == {97, 98}
sorted_ok = sorted(memoryview(b"cab")) == [97, 98, 99]

all_any_ok = (
    all(memoryview(b"\x01\x02"))
    and not all(memoryview(b"\x00\x01"))
    and any(memoryview(b"\x00\x01"))
    and not any(memoryview(b""))
)

sum_ok = sum(memoryview(b"\x01\x02\x03")) == 6
sum_start_ok = sum(memoryview(b"\x01\x02"), 10) == 13
min_max_ok = min(memoryview(b"cab")) == 97 and max(memoryview(b"cab")) == 99

comp_ok = [byte + 1 for byte in memoryview(b"ab")] == [98, 99]
target_comp_ok = [left + right for (left, right) in [memoryview(b"ab")]] == [195]

result = (
    total == 294
    and bytearray_total == 3
    and else_total == 42
    and list_ok
    and tuple_ok
    and set_ok
    and sorted_ok
    and all_any_ok
    and sum_ok
    and sum_start_ok
    and min_max_ok
    and comp_ok
    and target_comp_ok
)
assert result
result
