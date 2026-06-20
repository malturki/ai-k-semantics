base = {"a": 1, "b": 2}
copy = dict(base)
pairs = dict([("x", 3), ["y", 4], ("x", 5)])
empty_list = dict([])
empty_tuple = dict(())

result = copy == base and copy["a"] == 1 and list(copy) == ["a", "b"]
result = result and pairs == {"x": 5, "y": 4}
result = result and pairs["x"] == 5 and pairs["y"] == 4 and list(pairs) == ["x", "y"]
result = result and empty_list == {} and empty_tuple == {}
assert result
result
