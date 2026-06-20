x = 99
evens = [n for n in range(7) if n % 2 == 0]
result = evens == [0, 2, 4, 6] and x == 99
large = [n * 10 for n in [1, 2, 3, 4] if n > 2]
result = result and large == [30, 40]
letters = [c for c in "abc" if c != "b"]
result = result and letters == ["a", "c"]
assert result
result
