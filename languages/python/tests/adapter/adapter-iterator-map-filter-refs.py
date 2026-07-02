result = True


def inc(x):
    return x + 1


def add(x, y):
    return x + y


def odd(x):
    return x % 2


mapped = iter(map(inc, [1, 2, 3]))
result = result and next(mapped) == 2
result = result and list(mapped) == [3, 4]
result = result and next(mapped, "done") == "done"

mapped_tuple = iter(map(inc, []))
result = result and tuple(mapped_tuple) == ()
result = result and next(mapped_tuple, 99) == 99

mapped_strict = iter(map(add, [1, 2], [10, 20], strict=True))
result = result and next(mapped_strict) == 11
result = result and next(mapped_strict) == 22
result = result and next(mapped_strict, 99) == 99

loop_total = 0
mapped_loop = iter(map(inc, [4, 5]))
for value in mapped_loop:
    loop_total = loop_total + value

result = result and loop_total == 11
result = result and next(mapped_loop, 98) == 98

filtered = iter(filter(None, [0, 1, "", 2, False, 3]))
result = result and next(filtered) == 1
result = result and list(filtered) == [2, 3]
result = result and next(filtered, "done") == "done"

filtered_pred = iter(filter(odd, [1, 2, 3, 4]))
result = result and next(filtered_pred) == 1
result = result and next(filtered_pred) == 3
result = result and next(filtered_pred, 97) == 97

filter_tuple = iter(filter(None, [0, "", False]))
result = result and tuple(filter_tuple) == ()
result = result and next(filter_tuple, 96) == 96

filter_loop_total = 0
filter_loop = iter(filter(odd, [2, 3, 4, 5]))
for value in filter_loop:
    filter_loop_total = filter_loop_total + value

result = result and filter_loop_total == 8
result = result and next(filter_loop, 95) == 95

assert result
result
