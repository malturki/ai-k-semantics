total = 0
for a, (b, c) in [(1, (2, 3))]:
    total += a * 100 + b * 10 + c
else:
    total += 1000

result = total == 1123

seen = 0
for a, (b, c) in [(1, (2, 3)), (4, (5, 6))]:
    if a == 4:
        break
    seen += a * 100 + b * 10 + c
else:
    seen += 1000

result = result and seen == 123
assert result
result
