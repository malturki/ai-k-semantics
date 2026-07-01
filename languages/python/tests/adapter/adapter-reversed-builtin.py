result = list(reversed([1, 2, 3])) == [3, 2, 1]
result = result and tuple(reversed((1, 2, 3))) == (3, 2, 1)
result = result and list(reversed("ab")) == ["b", "a"]
result = result and list(reversed(b"\x01\x02")) == [2, 1]
result = result and list(reversed(bytearray(b"\x03\x04"))) == [4, 3]
result = result and list(reversed(memoryview(b"\x05\x06"))) == [6, 5]
result = result and list(reversed(range(1, 5))) == [4, 3, 2, 1]
result = result and list(reversed(range(5, 1, -1))) == [2, 3, 4, 5]
result = result and list(reversed({1: "a", 2: "b"})) == [2, 1]

total = 0
for value in reversed([1, 2, 3]):
    total += value
result = result and total == 6

pairs_total = 0
for a, b in reversed([(1, 2), (3, 4)]):
    pairs_total += a * b
result = result and pairs_total == 14

result = result and [x * 2 for x in reversed([1, 2, 3])] == [6, 4, 2]
result = result and bool(reversed([])) == True

marker = 0
for value in reversed([]):
    marker = 99
else:
    marker = 7
result = result and marker == 7

bad_set = False
try:
    reversed({1})
except TypeError:
    bad_set = True

bad_frozenset = False
try:
    reversed(frozenset([1]))
except TypeError:
    bad_frozenset = True

bad_iterator = False
try:
    reversed(enumerate([1]))
except TypeError:
    bad_iterator = True

result = result and bad_set and bad_frozenset and bad_iterator
assert result
result
