result = True

rows = iter([
    [[1], [[[10], [[100], [101]]], [[20], [[200]]]]],
    [[2], [[[30], [[300]]]]],
])
values = [i + j + k for [i], mids in rows for [j], inners in iter(mids) for [k] in iter(inners)]
result = result and values == [111, 112, 221, 332]
result = result and next(rows, 99) == 99

set_rows = iter([
    [[1], [[[1], [[1], [2]]]]],
    [[2], [[[2], [[2]]]]],
])
set_values = {i + j + k for [i], mids in set_rows for [j], inners in iter(mids) for [k] in iter(inners)}
result = result and set_values == {3, 4, 6}
result = result and next(set_rows, 98) == 98

dict_rows = iter([
    [[1], [[[1], [[1], [2]]]]],
    [[2], [[[2], [[2]]]]],
])
dict_values = {i * 100 + j * 10 + k: i + j + k for [i], mids in dict_rows for [j], inners in iter(mids) for [k] in iter(inners)}
result = result and dict_values == {111: 3, 112: 4, 222: 6}
result = result and next(dict_rows, 97) == 97

assert result
result
