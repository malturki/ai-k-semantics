values = [1, "x", True, None, ...]
result = repr(values)
assert result == "[1, 'x', True, None, Ellipsis]"
assert str(values) == result
assert ascii(values) == result

pair = (1, "x")
assert repr(pair) == "(1, 'x')"
assert str((1,)) == "(1,)"
assert ascii(()) == "()"

mapping = {"a": 1, 2: "b"}
assert repr(mapping) == "{'a': 1, 2: 'b'}"
assert str(mapping) == "{'a': 1, 2: 'b'}"

nested = [(), (1,), ["z", False], {"k": None}]
assert repr(nested) == "[(), (1,), ['z', False], {'k': None}]"

assert str(set()) == "set()"

result == "[1, 'x', True, None, Ellipsis]"
