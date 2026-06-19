total = 0
pairs = [(1, 1), (2, 2), (3, 3)]
for a, b in pairs:
    if a == 1:
        continue
    if a == 3:
        break
    total += a + b

total == 4
