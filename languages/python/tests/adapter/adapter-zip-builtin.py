result = list(zip()) == []
result = result and list(zip([1, 2])) == [(1,), (2,)]
result = result and list(zip([1, 2], ["a", "b"])) == [(1, "a"), (2, "b")]
result = result and tuple(zip((1, 2, 3), "ab")) == ((1, "a"), (2, "b"))
result = result and list(zip([1, 2], [3, 4], [5, 6])) == [(1, 3, 5), (2, 4, 6)]
result = result and list(zip(b"\x01\x02", range(5, 7))) == [(1, 5), (2, 6)]
result = result and list(zip({10: "a", 20: "b"}, ["x", "y"])) == [(10, "x"), (20, "y")]
result = result and list(zip({7}, [8])) == [(7, 8)]
result = result and list(zip(frozenset([9]), [10])) == [(9, 10)]
result = result and list(zip(enumerate(["q"]), [99])) == [((0, "q"), 99)]

total = 0
for a, b in zip([2, 3], [4, 5]):
    total += a * b
result = result and total == 23

seen = []
for pair in zip("ab", [1, 2]):
    seen.append(pair)
result = result and seen == [("a", 1), ("b", 2)]

result = result and [a + b for a, b in zip([10, 20], [1, 2])] == [11, 22]
result = result and bool(zip()) == True

marker = 0
for a, b in zip([], []):
    marker = 99
else:
    marker = 7
result = result and marker == 7

result = result and list(zip([1, 2], [3, 4], strict=True)) == [(1, 3), (2, 4)]
result = result and list(zip([1, 2], [3], strict=False)) == [(1, 3)]

strict_error = False
try:
    for a, b in zip([1, 2], [3], strict=True):
        marker = a + b
except ValueError:
    strict_error = True

bad_iterable = False
try:
    zip([1], 2)
except TypeError:
    bad_iterable = True

result = result and strict_error and bad_iterable
assert result
result
