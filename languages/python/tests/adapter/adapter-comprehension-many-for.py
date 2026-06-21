a = 100
d = 200

result = [
    a * 1000 + b * 100 + c * 10 + d
    for a in range(2)
    for b in range(a + 1)
    for c in range(b + 1)
    for d in range(c + 1)
] == [0, 1000, 1100, 1110, 1111]

result = result and [
    a * 1000 + b * 100 + c * 10 + d
    for a in range(3)
    if a
    for b in range(a + 1)
    if b != 0
    for c in range(b + 1)
    if c == b
    for d in range(c + 1)
    if d
] == [1111, 2111, 2221, 2222]

data = [
    [[1, 2], [
        [[10, 20], [
            [[100, 1], [
                [[1000, 10], [[10000, 100]]],
            ]],
        ]],
    ]],
]

result = result and [
    a + b + c + d + e + f + g + h + i + j
    for (a, b), middles in data
    for (c, d), inners in middles
    for (e, f), leaves in inners
    for (g, h), finals in leaves
    for i, j in finals
] == [11244]

result = result and {
    a * 100 + b * 10 + c: d
    for a in range(2)
    for b in range(2)
    for c in range(2)
    for d in range(2)
} == {0: 1, 1: 1, 10: 1, 11: 1, 100: 1, 101: 1, 110: 1, 111: 1}

result = result and {
    a * 10 + b: c
    for a in range(3)
    if a
    for b in range(3)
    if b
    for c in range(a + b)
    if c == 1
    for e in range(2)
    if e
} == {11: 1, 12: 1, 21: 1, 22: 1}

result = result and {
    a + b + c + d
    for a in range(2)
    for b in range(2)
    for c in range(2)
    for d in range(2)
} == {0, 1, 2, 3, 4}

result = result and {
    a * 10 + b * 10 + c + d
    for a in range(3)
    if a
    for b in range(a)
    for c in range(2)
    if c
    for d in range(2)
} == {11, 12, 21, 22, 31, 32}

leak_check = [
    a + d
    for a in range(2)
    for b in range(1)
    for c in range(1)
    for d in range(2)
]

result = result and leak_check == [0, 1, 1, 2] and a == 100 and d == 200

assert result
result
