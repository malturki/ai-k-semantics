result = min({2.5: "a", 1.5: "b", 3.0: "c"}) == 1.5
result = result and max({2.5: "a", 1.5: "b", 3.0: "c"}) == 3.0

result = result and min({2.5, 1.5, 3.0}) == 1.5
result = result and max({2.5, 1.5, 3.0}) == 3.0
result = result and min(frozenset([2.5, 1.5, 3.0])) == 1.5
result = result and max(frozenset([1.0, 2, False])) == 2

result = result and min({True, 0.5}) == 0.5
result = result and max({False, -1.25}) == False
result = result and min({2.5, 1.5}, default=99.0) == 1.5
result = result and max(frozenset([1.0, 2.5]), default=-1.0) == 2.5

result = result and min({2.5: "a", 1.5: "b"}, key=None) == 1.5
result = result and max({1.0: "a", 2.5: "b"}, key=None, default=-1.0) == 2.5
result = result and min(frozenset([True, 0.5]), key=None, default=9.0) == 0.5

assert result
result
