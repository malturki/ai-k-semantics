x = 99

outer_only = [i * 10 + j for i in range(4) if i % 2 == 0 for j in range(2)]
result = outer_only == [0, 1, 20, 21] and x == 99

inner_only = [i * 10 + j for i in range(3) for j in range(4) if j > i]
result = result and inner_only == [1, 2, 3, 12, 13, 23]

both = [
    i * 10 + j
    for i in range(5)
    if i > 1
    if i != 4
    for j in range(i)
    if j % 2 == 1
    if i + j < 5
]
result = result and both == [21, 31]

empty_outer = [i for i in range(3) if i > 5 for j in range(i)]
result = result and empty_outer == []

empty_inner = [i for i in range(3) for j in range(0) if i == j]
result = result and empty_inner == []

assert result
result
