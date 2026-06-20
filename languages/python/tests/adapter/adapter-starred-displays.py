items = [2, 3]
result = [1, *items, 4] == [1, 2, 3, 4]
result = result and (*"ab", "c") == ("a", "b", "c")
result = result and {*[1, 2], 2, 3} == {1, 2, 3}
source = {2, 3}
listed = [1, *source, 4]
tupled = (*source, 4)
result = result and len(listed) == 4 and set(listed) == {1, 2, 3, 4}
result = result and len(tupled) == 3 and set(tupled) == {2, 3, 4}
result = result and {*source, 4} == {2, 3, 4}
assert result
result
