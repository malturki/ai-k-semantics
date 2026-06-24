values = [1, "x", True, None, ...]
mapping = {"a": 1, 2: "b"}
nested = [(), (1,), ["z", False], {"k": None}]

result = format(0) == "0"
result = result and format(-3) == "-3"
result = result and format(True) == "True"
result = result and format(False) == "False"
result = result and format(None) == "None"
result = result and format(...) == "Ellipsis"
result = result and format("x") == "x"
result = result and format("x", "") == "x"
result = result and format(b"a") == "b'a'"
result = result and format(values) == "[1, 'x', True, None, Ellipsis]"
result = result and format((1,)) == "(1,)"
result = result and format(mapping) == "{'a': 1, 2: 'b'}"
result = result and format(nested) == "[(), (1,), ['z', False], {'k': None}]"
result = result and format(set()) == "set()"
result = result and format(range(1, 5)) == "range(1, 5)"
result = result and format(range(1, 5, 1)) == "range(1, 5)"
result = result and format(range(8, 1, -2)) == "range(8, 1, -2)"
result = result and format(slice(5)) == "slice(None, 5, None)"
result = result and format(slice(1, 5)) == "slice(1, 5, None)"
result = result and format(slice(1, 8, 2)) == "slice(1, 8, 2)"
result = result and format(slice("a", None, (1,))) == "slice('a', None, (1,))"

assert result
result
