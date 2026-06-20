x = 10
ys = [x + 1 for x in [1, 2, 3]]
result = ys == [2, 3, 4] and x == 10
letters = [c for c in "ab"]
result = result and letters == ["a", "b"]
squares = [(n, n * n) for n in range(4)]
result = result and squares == [(0, 0), (1, 1), (2, 4), (3, 9)]
assert result
result
