x = 13

all_filters = {
    i * 100 + j * 10 + k: i + j + k
    for i in range(4) if i > 0 if i < 3
    for j in range(i + 2) if j != 1 if j < 3
    for k in range(j + 1) if k != 0 if k <= 1
}
result = all_filters == {121: 4, 221: 5} and x == 13

outer_only = {
    i * 100 + j * 10 + k: i
    for i in range(4) if i % 2 == 1
    for j in range(2)
    for k in range(j + 1)
}
result = result and outer_only == {100: 1, 110: 1, 111: 1, 300: 3, 310: 3, 311: 3}

middle_only = {
    i * 100 + j * 10 + k: j
    for i in range(2)
    for j in range(3) if j != 1
    for k in range(j + 1)
}
result = result and middle_only == {0: 0, 20: 2, 21: 2, 22: 2, 100: 0, 120: 2, 121: 2, 122: 2}

inner_only = {
    i * 100 + j * 10 + k: k
    for i in range(2)
    for j in range(2)
    for k in range(3) if k == j
}
result = result and inner_only == {0: 0, 11: 1, 100: 0, 111: 1}

duplicates = {
    j: i * 10 + j
    for i in range(3)
    for j in range(2) if j >= 0
    for k in range(1)
}
result = result and duplicates == {0: 20, 1: 21}

assert result
result
