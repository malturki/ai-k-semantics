a, (b, *c), d = [1, [2, 3, 4], 5]
result = a == 1 and b == 2 and c == [3, 4] and d == 5

(a, *b), c = [[1, 2, 3], 4]
result = result and a == 1 and b == [2, 3] and c == 4

a, (*b,), c = [1, [], 2]
result = result and a == 1 and b == [] and c == 2

a, *b, (c, d) = [1, 2, 3, [4, 5]]
result = result and a == 1 and b == [2, 3] and c == 4 and d == 5

total = 0
for (a, *b), c in [([1, 2, 3], 4), ([5], 6)]:
    total += a + c + len(b)
result = result and total == 18

total = 0
for a, (b, *c) in [[1, [2, 3, 4]], [5, [6]]]:
    total += a + b + len(c)
result = result and total == 16

total = 0
for a, *b, (c, d) in [[1, 2, [3, 4]], [5, [6, 7]]]:
    total += a + c + d + len(b)
result = result and total == 27

assert result
result
