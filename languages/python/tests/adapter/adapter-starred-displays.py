items = [2, 3]
result = [1, *items, 4] == [1, 2, 3, 4]
result = result and (*"ab", "c") == ("a", "b", "c")
result = result and {*[1, 2], 2, 3} == {1, 2, 3}
assert result
result
