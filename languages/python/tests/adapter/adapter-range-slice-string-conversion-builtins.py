assert repr(range(5)) == "range(0, 5)"
assert str(range(1, 5)) == "range(1, 5)"
assert repr(range(1, 5, 1)) == "range(1, 5)"
assert ascii(range(8, 1, -2)) == "range(8, 1, -2)"

assert repr(slice(5)) == "slice(None, 5, None)"
assert str(slice(1, 5)) == "slice(1, 5, None)"
assert ascii(slice(1, 8, 2)) == "slice(1, 8, 2)"
assert repr(slice("a", None, (1,))) == "slice('a', None, (1,))"

result = repr([range(2), slice(1, 2)])
assert result == "[range(0, 2), slice(1, 2, None)]"

result == "[range(0, 2), slice(1, 2, None)]"
