total = 0
records = [(1, (2, 3)), [4, [5, 6]]]
for a, (b, c) in records:
    total += a * 100 + b * 10 + c

result = total == 579

for (same,), same in [((7,), 8)]:
    result = result and same == 8

for (sa, sb), in {((9, 10),)}:
    result = result and sa == 9 and sb == 10

for left, (set_a, set_b) in [(0, {11, 12})]:
    result = result and left == 0 and {set_a, set_b} == {11, 12}

assert result
result
