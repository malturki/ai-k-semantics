result = list(enumerate(["a", "b"])) == [(0, "a"), (1, "b")]
result = result and tuple(enumerate(("x", "y"), 3)) == ((3, "x"), (4, "y"))
result = result and list(enumerate("ab", start=1)) == [(1, "a"), (2, "b")]
result = result and list(enumerate(b"\x05\x06", -1)) == [(-1, 5), (0, 6)]
result = result and list(enumerate({10: "a", 20: "b"})) == [(0, 10), (1, 20)]
result = result and list(enumerate({7})) == [(0, 7)]
result = result and list(enumerate(frozenset([8]), True)) == [(1, 8)]
result = result and list(enumerate(range(2, 5), 10)) == [(10, 2), (11, 3), (12, 4)]

total = 0
for i, value in enumerate([2, 3], start=4):
    total += i * value
result = result and total == 23

seen = []
for pair in enumerate(("m", "n"), -2):
    seen.append(pair)
result = result and seen == [(-2, "m"), (-1, "n")]

result = result and [i + value for i, value in enumerate([10, 20], 1)] == [11, 22]
result = result and bool(enumerate([])) is True

marker = 0
for i, value in enumerate([]):
    marker = 99
else:
    marker = 7
result = result and marker == 7

bad_iterable = False
try:
    enumerate(1)
except TypeError:
    bad_iterable = True

bad_start = False
try:
    enumerate([1], 1.5)
except TypeError:
    bad_start = True

result = result and bad_iterable and bad_start
assert result
result
