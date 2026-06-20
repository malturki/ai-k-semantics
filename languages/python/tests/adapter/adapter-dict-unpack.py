base = {"a": 1, "b": 2}
merged = {**base, "b": 3, **{"c": 4}}
numeric = {**{1: 2}, 1: 3}
empty = {**{}, "x": 5}

result = merged == {"a": 1, "b": 3, "c": 4}
result = result and merged["a"] == 1
result = result and merged["b"] == 3
result = result and merged["c"] == 4
result = result and numeric[1] == 3
result = result and empty == {"x": 5}
assert result
result
