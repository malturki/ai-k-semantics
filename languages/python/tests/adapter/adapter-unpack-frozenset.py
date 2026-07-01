a, b = frozenset([1, 2])
flat_ok = {a, b} == {1, 2}

first, *rest = frozenset([3, 4, 5])
star_prefix_ok = set(rest + [first]) == {3, 4, 5}
star_prefix_ok = star_prefix_ok and len(rest) == 2

head, *middle, tail = frozenset([6, 7, 8, 9])
star_middle_ok = set(middle + [head, tail]) == {6, 7, 8, 9}
star_middle_ok = star_middle_ok and len(middle) == 2

*items, = frozenset()
empty_star_ok = items == []

(p1a, p1b), (p2a, p2b) = frozenset([(7, 8), (9, 10)])
nested_ok = {p1a + p1b, p2a + p2b} == {15, 19}

(nested_head, *nested_tail), = frozenset([(11, 12, 13)])
nested_star_ok = nested_head == 11 and nested_tail == [12, 13]

try:
    x, y, z = frozenset([1, 2])
    flat_error_ok = False
except ValueError:
    flat_error_ok = True

try:
    low, *between, high = frozenset([1])
    star_error_ok = False
except ValueError:
    star_error_ok = True

result = flat_ok and star_prefix_ok and star_middle_ok and empty_star_ok
result = result and nested_ok and nested_star_ok
result = result and flat_error_ok and star_error_ok

assert result
result
