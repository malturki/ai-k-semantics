groups = [
    [[1, 2], [[[10, 20], [[100, 1], [200, 2]]], [[30, 40], [[300, 3]]]]],
    [[3, 4], [[[50, 60], [[400, 4]]]]],
    [[5, 6], [[[70, 80], [[500, 5]]]]],
]

result = [
    a + b + c + d + e + f
    for (a, b), middles in groups
    if a < 5
    for (c, d), inners in middles
    if c != 30
    for e, f in inners
    if f != 2
] == [134, 521]

result = result and {
    a + b + c + d: e + f
    for (a, b), middles in groups
    if a < 5
    for (c, d), inners in middles
    if c != 30
    for e, f in inners
    if f != 2
} == {33: 101, 117: 404}

result = result and {
    a + c + e
    for (a, b), middles in groups
    if a < 5
    for (c, d), inners in middles
    if c != 30
    for e, f in inners
    if f != 2
} == {111, 453}

result = result and [
    left + len(rest) + c + len(tail) + e + len(suffix)
    for (left, *rest), middles in groups
    if left < 5
    for (c, *tail), inners in middles
    if c != 30
    for e, *suffix in inners
    if len(suffix) == 1
] == [114, 214, 456]

a = 100
e = 200
leak_check = [
    a + e
    for (a, b), middles in groups
    if a < 5
    for (c, d), inners in middles
    if c != 30
    for e, f in inners
    if f != 2
]

result = result and leak_check == [101, 403] and a == 100 and e == 200

assert result
result
