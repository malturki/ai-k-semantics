result = True

outer = iter([0, 1, 2])
list_values = [
    a * 1000 + b * 100 + c * 10 + d
    for a in outer if a > 0
    for b in iter([a, a + 1]) if b != 2
    for c in iter([b, b + 1]) if c == b
    for d in iter([c, c + 1]) if d % 2 == 0
]
result = result and list_values == [1112, 2334]
result = result and next(outer, 99) == 99

rows = iter([
    [[0], [
        [[1], [
            [[1], [[2]]],
        ]],
    ]],
    [[1], [
        [[1], [
            [[1], [[1], [2]]],
        ]],
        [[2], [
            [[2], [[2]]],
        ]],
    ]],
    [[2], [
        [[3], [
            [[3], [[3], [4]]],
        ]],
    ]],
])
target_values = [
    a * 1000 + b * 100 + c * 10 + d
    for [a], mids in rows if a > 0
    for [b], inners in iter(mids) if b != 2
    for [c], leaves in iter(inners) if c == b
    for [d] in iter(leaves) if d % 2 == 0
]
result = result and target_values == [1112, 2334]
result = result and next(rows, 98) == 98

set_outer = iter([0, 1, 2])
set_values = {
    a + b + c + d
    for a in set_outer if a > 0
    for b in iter([a, a + 1]) if b != 2
    for c in iter([b, b + 1]) if c == b
    for d in iter([c, c + 1]) if d % 2 == 0
}
result = result and set_values == {5, 12}
result = result and next(set_outer, 97) == 97

dict_outer = iter([0, 1, 2])
dict_values = {
    a * 1000 + b * 100 + c * 10 + d: a + b + c + d
    for a in dict_outer if a > 0
    for b in iter([a, a + 1]) if b != 2
    for c in iter([b, b + 1]) if c == b
    for d in iter([c, c + 1]) if d % 2 == 0
}
result = result and dict_values == {1112: 5, 2334: 12}
result = result and next(dict_outer, 96) == 96

assert result
result
