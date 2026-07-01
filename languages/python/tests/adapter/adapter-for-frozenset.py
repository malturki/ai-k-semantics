seen = set()
total = 0
for item in frozenset([1, 2, 1]):
    seen.add(item)
    total += item

plain_ok = seen == {1, 2} and total == 3

empty_else = 0
for item in frozenset():
    empty_else = 1
else:
    empty_else = 2

nonempty_else = 0
for item in frozenset([3]):
    nonempty_else += item
else:
    nonempty_else += 10

break_else = 0
for item in frozenset([4]):
    break_else += item
    break
else:
    break_else = 99

else_ok = empty_else == 2 and nonempty_else == 13 and break_else == 4

pair_sum = 0
for left, right in frozenset([(1, 2), (3, 4)]):
    pair_sum += left + right

unpack_else = 0
for left, right in frozenset([(5, 6)]):
    unpack_else += left + right
else:
    unpack_else += 20

unpack_ok = pair_sum == 10 and unpack_else == 31

star_sum = 0
for first, *middle, last in frozenset([(1, 2, 3), (4, 5, 6)]):
    star_sum += first + middle[0] + last

star_ok = star_sum == 21

result = plain_ok and else_ok and unpack_ok and star_ok
assert result
result
