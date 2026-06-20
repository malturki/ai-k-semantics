x = 81

all_filters = {
    i * 100 + j * 10 + k
    for i in range(4) if i > 0 if i < 3
    for j in range(i + 2) if j != 1 if j < 3
    for k in range(j + 1) if k != 0 if k <= 1
}
result = all_filters == {121, 221} and x == 81

outer_only = {
    i * 100 + j * 10 + k
    for i in range(4) if i % 2 == 1
    for j in range(2)
    for k in range(j + 1)
}
result = result and outer_only == {100, 110, 111, 300, 310, 311}

middle_only = {
    i * 100 + j * 10 + k
    for i in range(2)
    for j in range(3) if j != 1
    for k in range(j + 1)
}
result = result and middle_only == {0, 20, 21, 22, 100, 120, 121, 122}

inner_only = {
    i * 100 + j * 10 + k
    for i in range(2)
    for j in range(2)
    for k in range(3) if k == j
}
result = result and inner_only == {0, 11, 100, 111}

duplicates = {j for i in range(3) for j in range(2) if j >= 0 for k in range(2)}
result = result and duplicates == {0, 1}

empty = {i for i in range(3) if i > 5 for j in range(i) for k in range(j)}
result = result and empty == set()

assert result
result
