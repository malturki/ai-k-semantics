result = True

gen = (x + 1 for x in [1, 2, 3])
result = result and next(gen) == 2
result = result and list(gen) == [3, 4]
result = result and next(gen, "done") == "done"

empty = (x for x in [])
result = result and list(empty) == []
result = result and next(empty, 99) == 99

filtered = (x * 2 for x in range(6) if x % 2 if x > 2)
result = result and tuple(filtered) == (6, 10)

total = 0
for value in (x for x in [4, 5]):
    total = total + value
result = result and total == 9

pairs = ((a, b) for (a, b) in [(1, 2), (3, 4)])
result = result and next(pairs) == (1, 2)
result = result and list(pairs) == [(3, 4)]

star = (rest for first, *rest in [(1, 2, 3), (4,)])
result = result and next(star) == [2, 3]
result = result and next(star) == []
result = result and next(star, "done") == "done"

two_for = (a * 10 + b for a in [1, 2] if a > 1 for b in [3, 4] if b == 4)
result = result and list(two_for) == [24]

many_for = (a + b + c + d for a in [1] for b in [2] for c in [3] for d in [4])
result = result and list(many_for) == [10]

outer = "kept"
scoped = (outer for outer in [7, 8])
result = result and outer == "kept"
result = result and list(scoped) == [7, 8]
result = result and outer == "kept"

assert result
result
