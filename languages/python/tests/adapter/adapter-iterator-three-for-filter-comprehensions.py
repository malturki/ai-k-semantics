result = True

list_outer = iter([0, 1, 2])
list_values = [
    i * 100 + j * 10 + k
    for i in list_outer if i > 0
    for j in iter([i, i + 1]) if j != 2
    for k in iter([j, j + 1]) if k % 2 == 0
]
result = result and list_values == [112, 234]
result = result and next(list_outer, 99) == 99

set_outer = iter([0, 1, 2])
set_values = {
    i + j + k
    for i in set_outer if i > 0
    for j in iter([i, i + 1]) if j != 2
    for k in iter([j, j + 1]) if k % 2 == 0
}
result = result and set_values == {4, 9}
result = result and next(set_outer, 98) == 98

dict_outer = iter([0, 1, 2])
dict_values = {
    i * 100 + j * 10 + k: i + j + k
    for i in dict_outer if i > 0
    for j in iter([i, i + 1]) if j != 2
    for k in iter([j, j + 1]) if k % 2 == 0
}
result = result and dict_values == {112: 4, 234: 9}
result = result and next(dict_outer, 97) == 97

assert result
result
