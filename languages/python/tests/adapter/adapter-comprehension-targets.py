pairs = [[1, 2], [3, 4]]
result = [a + b for a, b in pairs] == [3, 7]

result = result and {a: b for a, b in pairs} == {1: 2, 3: 4}
result = result and {a + b for a, b in pairs} == {3, 7}

nested = [[1, [2, 3, 4]], [5, [6]]]
result = result and [a + b + len(c) for a, (b, *c) in nested] == [5, 11]

starred = [[1, 2, 3, 4], [5, 6]]
result = result and [a + len(b) + c for a, *b, c in starred] == [7, 11]

a = 100
leak_check = [a + b for a, b in pairs]
result = result and leak_check == [3, 7] and a == 100

assert result
result
