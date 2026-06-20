a, b = {1, 2}
flat_ok = {a, b} == {1, 2}

first, *rest = {3, 4, 5}
star_prefix_ok = set(rest + [first]) == {3, 4, 5}
star_prefix_ok = star_prefix_ok and len(rest) == 2

head, *middle, tail = {6, 7, 8, 9}
star_middle_ok = set(middle + [head, tail]) == {6, 7, 8, 9}
star_middle_ok = star_middle_ok and len(middle) == 2

*items, = set()
empty_star_ok = items == []

result = flat_ok and star_prefix_ok and star_middle_ok and empty_star_ok

assert result
result
