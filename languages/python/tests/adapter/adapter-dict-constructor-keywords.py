kw_only = dict(a=1, b=2)
result = kw_only == {"a": 1, "b": 2}

base = {"a": 1, "z": 0}
mixed = dict(base, a=3, c=4)
result = result and mixed == {"a": 3, "z": 0, "c": 4}

pairs = dict([("a", 1), ["b", 2]], b=5, c=6)
result = result and pairs == {"a": 1, "b": 5, "c": 6}

empty_list = dict([], a=1)
empty_tuple = dict((), b=2)
result = result and empty_list == {"a": 1} and empty_tuple == {"b": 2}

assert result
result
