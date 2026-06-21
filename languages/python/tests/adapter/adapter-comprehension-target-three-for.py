groups = [
    [[1, 2], [[[10, 20], [[100, 1], [200, 2]]], [[30, 40], [[300, 3]]]]],
    [[3, 4], [[[50, 60], [[400, 4]]]]],
]

result = [
    a + b + c + d + e + f
    for (a, b), middles in groups
    for (c, d), inners in middles
    for e, f in inners
] == [134, 235, 376, 521]

result = result and {
    a + b + c + d: e + f
    for (a, b), middles in groups
    for (c, d), inners in middles
    for e, f in inners
} == {33: 202, 73: 303, 117: 404}

result = result and {
    a + c + e
    for (a, b), middles in groups
    for (c, d), inners in middles
    for e, f in inners
} == {111, 211, 331, 453}

result = result and [
    left + len(rest) + c + len(tail) + e
    for (left, *rest), middles in groups
    for (c, *tail), inners in middles
    for e, f in inners
] == [113, 213, 333, 455]

a = 100
e = 200
leak_check = [
    a + e
    for (a, b), middles in groups
    for (c, d), inners in middles
    for e, f in inners
]

result = result and leak_check == [101, 201, 301, 403] and a == 100 and e == 200

assert result
result
