result = sum([1, 2, 3]) == 6
result = result and sum((True, False, 4)) == 5
result = result and sum([], 7) == 7
result = result and sum([], True) is True
result = result and sum([1, 2], 10) == 13
result = result and sum({1, 2, 3}) == 6
result = result and sum({1: "a", 2: "b"}) == 3
result = result and sum(range(4)) == 6
result = result and sum(range(-3, 0)) == -6
result = result and sum(range(5, -1, -2)) == 9
result = result and sum(range(0), True) is True
result = result and sum(range(1, 4), True) == 7
assert result
result
