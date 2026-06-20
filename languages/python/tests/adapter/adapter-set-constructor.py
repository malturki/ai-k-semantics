result = set([1, 2, 1]) == {1, 2} and len(set([1, 2, 1])) == 2
result = result and set((1, 2, 1)) == {1, 2}
result = result and set("aba") == {"a", "b"} and len(set("aba")) == 2
result = result and set({"x": 1, "y": 2}) == {"x", "y"}
result = result and set(range(4)) == {0, 1, 2, 3}
result = result and set(set([1, 1, 2])) == {1, 2}
result = result and set([]) == set() and not set(())
assert result
result
