groups = [
    [[1, 2], [[10, 20], [30, 40]]],
    [[3, 4], [[50, 60]]],
]

result = [a + b + c + d for (a, b), inner in groups for c, d in inner] == [33, 73, 117]
result = result and {a + b: c + d for (a, b), inner in groups for c, d in inner} == {3: 70, 7: 110}
result = result and {a + c for (a, b), inner in groups for c, d in inner} == {11, 31, 53}

result = result and [x + y + z for x in [1, 2] for y, z in [[3, 4]]] == [8, 9]

star_groups = [
    [[1, 2, 3], [[4, 5]]],
]
result = result and [a + len(rest) + c + d for (a, *rest), inner in star_groups for c, d in inner] == [12]

a = 100
c = 200
leak_check = [a + c for (a, b), inner in groups for c, d in inner]
result = result and leak_check == [11, 31, 53] and a == 100 and c == 200

assert result
result
