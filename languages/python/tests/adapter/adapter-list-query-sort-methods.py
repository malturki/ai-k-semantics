values = [1, True, 2, 1, "1", 1.0, False, 0]
empty_values = []

count_ok = (
    values.count(1) == 4
    and values.count(False) == 2
    and values.count("1") == 1
    and values.count(99) == 0
    and empty_values.count(1) == 0
)

query = ["a", "b", "a", "c", "a"]

index_ok = (
    query.index("a") == 0
    and query.index("a", 1) == 2
    and query.index("a", -2) == 4
    and query.index("a", 0, 3) == 0
    and query.index("a", 1, 3) == 2
    and query.index("a", -10, -1) == 0
)

sort_nums = [3, 1, 2]
sort_nums_ret = sort_nums.sort()
sort_empty = []
sort_empty_ret = sort_empty.sort()
sort_strings = ["b", "a", "c"]
sort_strings_ret = sort_strings.sort()
sort_bools = [True, 0, False, 1]
sort_bools_ret = sort_bools.sort()

sort_ok = (
    sort_nums_ret is None
    and sort_nums == [1, 2, 3]
    and sort_empty_ret is None
    and sort_empty == []
    and sort_strings_ret is None
    and sort_strings == ["a", "b", "c"]
    and sort_bools_ret is None
    and sort_bools == [0, False, True, 1]
)

errors_ok = True

try:
    query.index("a", 3, 4)
except ValueError:
    pass
else:
    errors_ok = False

try:
    empty_values.index(1)
except ValueError:
    pass
else:
    errors_ok = False

try:
    query.index("a", "bad")
except TypeError:
    pass
else:
    errors_ok = False

try:
    query.index("a", 0, None)
except TypeError:
    pass
else:
    errors_ok = False

try:
    query.count("a", 0)
except TypeError:
    pass
else:
    errors_ok = False

bad_sort = [1, "x"]
try:
    bad_sort.sort()
except TypeError:
    pass
else:
    errors_ok = False

errors_ok = errors_ok and query == ["a", "b", "a", "c", "a"] and bad_sort == [1, "x"]

result = count_ok and index_ok and sort_ok and errors_ok
assert result
result
