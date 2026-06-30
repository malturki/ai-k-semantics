base = {1, 2, 3}

copy_value = base.copy()
copy_value = copy_value.union({4})
copy_ok = base == {1, 2, 3} and copy_value == {1, 2, 3, 4}

zero_arg_ok = (
    base.union() == {1, 2, 3}
    and base.intersection() == {1, 2, 3}
    and base.difference() == {1, 2, 3}
)

union_ok = base.union([3, 4], (4, 5), {5, 6}) == {1, 2, 3, 4, 5, 6}
intersection_ok = {1, 2, 3, 4}.intersection([2, 3, 4], (3, 4, 5)) == {3, 4}
difference_ok = {1, 2, 3, 4}.difference([2], {4}, ()) == {1, 3}
symmetric_difference_ok = {1, 2, 3}.symmetric_difference([2, 4]) == {1, 3, 4}

query_ok = (
    base.isdisjoint([4, 5])
    and not base.isdisjoint([3, 4])
    and base.issubset([1, 2, 3, 4])
    and not {1, 5}.issubset([1, 2, 3, 4])
    and set().issubset([])
    and base.issuperset([1, 2])
    and not {1}.issuperset([1, 2])
)

dict_string_range_ok = (
    {"a", "b"}.union({"b": 1, "c": 2}) == {"a", "b", "c"}
    and {"a", "b"}.intersection("bcd") == {"b"}
    and {1, 2, 3}.difference(range(2, 4)) == {1}
)

errors_ok = True

try:
    base.union(3)
except TypeError:
    pass
else:
    errors_ok = False

try:
    base.isdisjoint(3)
except TypeError:
    pass
else:
    errors_ok = False

try:
    base.symmetric_difference()
except TypeError:
    pass
else:
    errors_ok = False

try:
    base.symmetric_difference([1], [2])
except TypeError:
    pass
else:
    errors_ok = False

try:
    base.issubset()
except TypeError:
    pass
else:
    errors_ok = False

try:
    base.issuperset([1], [2])
except TypeError:
    pass
else:
    errors_ok = False

result = (
    copy_ok
    and zero_arg_ok
    and union_ok
    and intersection_ok
    and difference_ok
    and symmetric_difference_ok
    and query_ok
    and dict_string_range_ok
    and errors_ok
)
assert result
result
