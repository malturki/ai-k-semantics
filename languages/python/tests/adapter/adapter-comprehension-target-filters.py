pairs = [[1, 2], [3, 4], [5, 6], [7, 1]]
threshold = 3

result = [a + b for a, b in pairs if b > threshold] == [7, 11]
result = result and [a + b for a, b in pairs if a > 1 if b < 6] == [7, 8]

result = result and {a: b for a, b in pairs if b > threshold} == {3: 4, 5: 6}
result = result and {a + b for a, b in pairs if a > 1 if b < 6} == {7, 8}

nested = [[1, [2, 3, 4]], [5, [6, 7]], [8, [9, 10, 11]]]
result = result and [a + b + len(c) for a, (b, *c) in nested if b > 2 if len(c) == 2] == [19]

a = 100
leak_check = [a + b for a, b in pairs if b > threshold]
result = result and leak_check == [7, 11] and a == 100

assert result
result
