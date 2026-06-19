result = list("ab") == ["a", "b"]
result = result and tuple("ab") == ("a", "b")
result = result and list((1, 2)) == [1, 2]
result = result and tuple([1, 2]) == (1, 2)
result = result and list([]) == []
result = result and tuple(()) == ()
result = result and list({"a": 1, "b": 2}) == ["a", "b"]
result = result and tuple({"a": 1, "b": 2}) == ("a", "b")
result = result and list(range(3)) == [0, 1, 2]
result = result and tuple(range(1, 4)) == (1, 2, 3)
result = result and list(range(5, -1, -2)) == [5, 3, 1]
result = result and tuple(range(0)) == ()
assert result
result
