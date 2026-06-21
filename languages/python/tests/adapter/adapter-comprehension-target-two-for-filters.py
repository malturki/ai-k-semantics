groups = [
    [[1, 2], [[10, 1], [20, 2], [30, 3]]],
    [[3, 4], [[40, 4], [50, 5]]],
    [[5, 1], [[60, 6]]],
]

result = [
    a + b + c + d
    for (a, b), inner in groups
    if b > 1
    if a < 4
    for c, d in inner
    if d > 1
    if c < 50
] == [25, 36, 51]

result = result and {
    a + b: c + d
    for (a, b), inner in groups
    if b > 1
    for c, d in inner
    if c < 50
} == {3: 33, 7: 44}

result = result and {
    a + c
    for (a, b), inner in groups
    if b > 1
    for c, d in inner
    if d > 2
} == {31, 43, 53}

result = result and [
    x + y + z
    for x in [1, 2, 3]
    if x > 1
    for y, z in [[4, 5], [6, 7]]
    if z < 7
] == [11, 12]

a = 100
c = 200
leak_check = [
    a + c
    for (a, b), inner in groups
    if b > 1
    for c, d in inner
    if d > 2
]
result = result and leak_check == [31, 43, 53] and a == 100 and c == 200

assert result
result
