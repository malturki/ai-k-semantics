result = True

outer = iter([1, 2])
inner = iter([10, 20])
persistent_inner = [i * 100 + j for i in outer for j in inner]
result = result and persistent_inner == [110, 120]
result = result and next(outer, 99) == 99
result = result and next(inner, 98) == 98

fresh_inner = [i * 100 + j for i in [1, 2] for j in iter([i, i + 10])]
result = result and fresh_inner == [101, 111, 202, 212]

filtered_outer = iter([0, 1, 2, 3])
filtered_values = [i * 10 + j for i in filtered_outer if i > 1 for j in iter([0, 1, 2]) if j != 1]
result = result and filtered_values == [20, 22, 30, 32]
result = result and next(filtered_outer, 97) == 97

rows = iter([[1, [10, 11]], [2, [20]]])
target_values = [name * 100 + value for name, seq in rows for value in iter(seq)]
result = result and target_values == [110, 111, 220]
result = result and next(rows, 96) == 96

set_outer = iter([1, 2])
set_values = {i + j for i in set_outer for j in iter([0, 1, 1])}
result = result and set_values == {1, 2, 3}
result = result and next(set_outer, 95) == 95

set_rows = iter([[1, [1, 2]], [2, [2, 3]]])
set_target_filtered = {a * 10 + b for a, seq in set_rows if a > 1 for b in iter(seq) if b > 2}
result = result and set_target_filtered == {23}
result = result and next(set_rows, 94) == 94

dict_outer = iter([1, 2])
dict_values = {i * 10 + j: i + j for i in dict_outer for j in iter([0, 1])}
result = result and dict_values == {10: 1, 11: 2, 20: 2, 21: 3}
result = result and next(dict_outer, 93) == 93

dict_rows = iter([[1, [0, 1, 2]], [2, [2, 3]]])
dict_filtered = {a: b for a, seq in dict_rows if a > 1 for b in iter(seq) if b > 2}
result = result and dict_filtered == {2: 3}
result = result and next(dict_rows, 92) == 92

assert result
result
