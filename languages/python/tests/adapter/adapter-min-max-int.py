result = min([3, 1, 2]) == 1
result = result and max([3, 1, 2]) == 3
result = result and min((True, False, 3)) == False
result = result and max((True, False, 3)) == 3
result = result and min({3, 1, 2}) == 1
result = result and max({3, 1, 2}) == 3
result = result and min({1: "a", 4: "b", 2: "c"}) == 1
result = result and max({1: "a", 4: "b", 2: "c"}) == 4
result = result and min(range(2, 7)) == 2
result = result and max(range(2, 7)) == 6
result = result and min(range(5, -1, -2)) == 1
result = result and max(range(5, -1, -2)) == 5
assert result
result
