result = True

rows = iter([
    [[0], [[[1], [[2]]]]],
    [[1], [[[1], [[1], [2]]], [[2], [[2]]]]],
    [[2], [[[3], [[3], [4]]]]],
])
values = [
    i * 100 + j * 10 + k
    for [i], mids in rows if i > 0
    for [j], inners in iter(mids) if j != 2
    for [k] in iter(inners) if k % 2 == 0
]
result = result and values == [112, 234]
result = result and next(rows, 99) == 99

set_rows = iter([
    [[0], [[[1], [[2]]]]],
    [[1], [[[1], [[1], [2]]], [[2], [[2]]]]],
    [[2], [[[3], [[3], [4]]]]],
])
set_values = {
    i + j + k
    for [i], mids in set_rows if i > 0
    for [j], inners in iter(mids) if j != 2
    for [k] in iter(inners) if k % 2 == 0
}
result = result and set_values == {4, 9}
result = result and next(set_rows, 98) == 98

dict_rows = iter([
    [[0], [[[1], [[2]]]]],
    [[1], [[[1], [[1], [2]]], [[2], [[2]]]]],
    [[2], [[[3], [[3], [4]]]]],
])
dict_values = {
    i * 100 + j * 10 + k: i + j + k
    for [i], mids in dict_rows if i > 0
    for [j], inners in iter(mids) if j != 2
    for [k] in iter(inners) if k % 2 == 0
}
result = result and dict_values == {112: 4, 234: 9}
result = result and next(dict_rows, 97) == 97

assert result
result
