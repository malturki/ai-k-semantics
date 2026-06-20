unpacked = dict(**{"a": 1, "b": 2})
result = unpacked == {"a": 1, "b": 2}

base = {"a": 0, "z": 9}
mixed = dict(base, **{"a": 1, "b": 2})
result = result and mixed == {"a": 1, "z": 9, "b": 2}

pairs = dict([("x", 0)], y=1, **{"z": 2})
result = result and pairs == {"x": 0, "y": 1, "z": 2}

multi_unpack = dict(**{"left": 1}, **{"right": 2})
result = result and multi_unpack == {"left": 1, "right": 2}

empty = dict(**{})
result = result and empty == {}

assert result
result
