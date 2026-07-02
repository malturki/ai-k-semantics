result = True

outer = iter([1, 2])
middle = iter([10, 20])
inner = iter([100, 200])
persistent = [i + j + k for i in outer for j in middle for k in inner]
result = result and persistent == [111, 211]
result = result and next(outer, 99) == 99
result = result and next(middle, 98) == 98
result = result and next(inner, 97) == 97

fresh = [i * 100 + j * 10 + k for i in [1, 2] for j in iter([i, i + 1]) for k in iter([j, j + 1])]
result = result and fresh == [111, 112, 122, 123, 222, 223, 233, 234]

set_outer = iter([1, 2])
set_values = {i + j + k for i in set_outer for j in iter([0, 1]) for k in iter([0, 1])}
result = result and set_values == {1, 2, 3, 4}
result = result and next(set_outer, 96) == 96

dict_outer = iter([1, 2])
dict_values = {i * 100 + j * 10 + k: i + j + k for i in dict_outer for j in iter([0, 1]) for k in iter([0, 1])}
result = result and dict_values == {100: 1, 101: 2, 110: 2, 111: 3, 200: 2, 201: 3, 210: 3, 211: 4}
result = result and next(dict_outer, 95) == 95

assert result
result
