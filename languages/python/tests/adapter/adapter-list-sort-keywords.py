identity = lambda x: x
negate = lambda x: 0 - x
first = lambda item: item[0]
same_key = lambda item: 0

nums = [3, 1, 2]
nums_ret = nums.sort(reverse=True)

falsy_reverse = [2, 1]
falsy_ret = falsy_reverse.sort(reverse=[])

truthy_reverse = [1, 2]
truthy_ret = truthy_reverse.sort(reverse=[0])

keyed = [3, 1, 2]
keyed_ret = keyed.sort(key=negate)

key_none = [3, 1, 2]
key_none_ret = key_none.sort(key=None, reverse=True)

pairs = [(1, 3), (1, 2), (0, 9)]
pairs_ret = pairs.sort(key=first)

pairs_reverse = [(1, 3), (1, 2), (0, 9)]
pairs_reverse_ret = pairs_reverse.sort(key=first, reverse=True)

pairs_reverse_key_order = [(1, 3), (1, 2), (0, 9)]
pairs_reverse_key_order_ret = pairs_reverse_key_order.sort(reverse=True, key=first)

empty_key = []
empty_key_ret = empty_key.sort(key=3)

basic_ok = (
    nums_ret is None
    and nums == [3, 2, 1]
    and falsy_ret is None
    and falsy_reverse == [1, 2]
    and truthy_ret is None
    and truthy_reverse == [2, 1]
    and keyed_ret is None
    and keyed == [3, 2, 1]
    and key_none_ret is None
    and key_none == [3, 2, 1]
    and pairs_ret is None
    and pairs == [(0, 9), (1, 3), (1, 2)]
    and pairs_reverse_ret is None
    and pairs_reverse == [(1, 3), (1, 2), (0, 9)]
    and pairs_reverse_key_order_ret is None
    and pairs_reverse_key_order == [(1, 3), (1, 2), (0, 9)]
    and empty_key_ret is None
    and empty_key == []
)

order = 0
order_items = [(order := order * 10 + 1), 2]
order_ret = order_items.sort(
    key=(order := order * 10 + 2) and identity,
    reverse=(order := order * 10 + 3) and [],
)
order_key_reverse_ok = order_ret is None and order == 123 and order_items == [1, 2]

order = 0
order_items = [(order := order * 10 + 1), 2]
order_ret = order_items.sort(
    reverse=(order := order * 10 + 3) and [],
    key=(order := order * 10 + 2) and identity,
)
order_reverse_key_ok = order_ret is None and order == 132 and order_items == [1, 2]

errors_ok = True

try:
    nums.sort(1)
except TypeError:
    pass
else:
    errors_ok = False

noncallable_key = [1]
try:
    noncallable_key.sort(key=3)
except TypeError:
    pass
else:
    errors_ok = False

key_eval = [1]
try:
    key_eval.sort(key=1 // 0)
except ZeroDivisionError:
    pass
else:
    errors_ok = False

bad_key = [1, "x"]
try:
    bad_key.sort(key=identity)
except TypeError:
    pass
else:
    errors_ok = False

same = [(1, 3), (1, 2), (0, 9)]
same_ret = same.sort(key=same_key, reverse=True)
same_ok = same_ret is None and same == [(1, 3), (1, 2), (0, 9)]

errors_ok = errors_ok and bad_key == [1, "x"]

result = basic_ok and order_key_reverse_ok and order_reverse_key_ok and errors_ok and same_ok
assert result
result
