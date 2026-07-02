result = True

pairs = iter([(1, 2), (3, 4), (5, 6)])
seen = []

for a, b in pairs:
    seen = seen + [a * 10 + b]
    if a == 3:
        break

result = result and seen == [12, 34]
result = result and next(pairs) == (5, 6)
result = result and next(pairs, "done") == "done"

nested = iter([([1, 2], 3), ([4, 5], 6)])
total = 0

for [a, b], c in nested:
    total = total + a * 100 + b * 10 + c
else:
    total = total + 1000

result = result and total == 1579
result = result and next(nested, 99) == 99

starred = iter([(1, 2, 3), (4, 5), (6, 7, 8, 9)])
pieces = []

for first, *middle, last in starred:
    pieces = pieces + [first * 100 + len(middle) * 10 + last]
    if first == 4:
        continue

result = result and pieces == [113, 405, 629]
result = result and next(starred, 98) == 98

star_else = iter([(10, 11)])
star_total = 0

for x, *ys in star_else:
    star_total = star_total + x + len(ys)
else:
    star_total = star_total + 100

result = result and star_total == 111
result = result and next(star_else, 97) == 97

star_break = iter([(1, 2, 3), (4, 5, 6)])

for x, *ys in star_break:
    if x == 1:
        break

result = result and next(star_break) == (4, 5, 6)

empty = iter([])
marker = 0

for a, b in empty:
    marker = 1
else:
    marker = 2

result = result and marker == 2

assert result
result
