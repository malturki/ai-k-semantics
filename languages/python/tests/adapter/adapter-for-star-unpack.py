total = 0

for a, *middle, c in [[1, 2, 3, 4], (5, 6, 7)]:
    total = total + a * 100 + len(middle) * 10 + c

result = total == 641

star_total = 0
empty_seen = False

for *rest, in [(8, 9), ()]:
    star_total = star_total + len(rest)
    empty_seen = empty_seen or rest == []

result = result and star_total == 2
result = result and empty_seen

flag = 0

for head, *tail in [(1, 2, 3)]:
    flag = flag + head + len(tail)
else:
    flag = flag + 10

result = result and flag == 13

count = 0

for first, *rest in [(1, 2), (3, 4)]:
    count = count + first
    continue
    count = 99

result = result and count == 4

breaker = 0

for first, *rest in [(5, 6), (7, 8)]:
    breaker = breaker + first + len(rest)
    break
else:
    breaker = 99

result = result and breaker == 6

def first_value():
    for first, *rest in [(9, 10)]:
        return first + len(rest)
    return 0

result = result and first_value() == 10
assert result
result
