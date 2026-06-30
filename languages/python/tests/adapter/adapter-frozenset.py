empty = frozenset()
letters = frozenset("abca")
from_list = frozenset([1, 2, 1])
from_tuple = frozenset((2, 3, 2))
from_dict = frozenset({"x": 1, "y": 2})
from_range = frozenset(range(3))
from_set = frozenset({1, 1, 2})

constructors_ok = (
    not empty
    and len(empty) == 0
    and letters == {"a", "b", "c"}
    and from_list == {1, 2}
    and from_tuple == {2, 3}
    and from_dict == {"x", "y"}
    and from_range == {0, 1, 2}
    and from_set == frozenset([1, 2])
)

equality_order_ok = (
    frozenset("abc") == set("cba")
    and frozenset("ab") < set("abc")
    and frozenset("ab") <= frozenset("abc")
    and set("abc") > frozenset("ab")
    and frozenset("abc") >= set("abc")
    and not (frozenset("ab") < set("ab"))
    and frozenset("ab") != "ab"
)

operator_ok = (
    (frozenset("ab") | set("bc")) == frozenset("abc")
    and isinstance(frozenset("ab") | set("bc"), frozenset)
    and ({1, 2} | frozenset([2, 3])) == {1, 2, 3}
    and isinstance({1, 2} | frozenset([2, 3]), set)
    and (frozenset([1, 2, 3]) & {2, 3, 4}) == frozenset([2, 3])
    and (frozenset([1, 2, 3]) - {2}) == frozenset([1, 3])
    and (frozenset([1, 2]) ^ {2, 3}) == frozenset([1, 3])
)

method_ok = (
    frozenset("ab").copy() == frozenset("ab")
    and isinstance(frozenset("ab").copy(), frozenset)
    and frozenset("ab").union("bc", frozenset("de")) == frozenset("abcde")
    and frozenset("abc").intersection("bcd", {"b", "c", "e"}) == frozenset("bc")
    and frozenset("abc").difference("b", {"c"}) == frozenset("a")
    and frozenset("ab").symmetric_difference("bc") == frozenset("ac")
    and frozenset("ab").isdisjoint("cd")
    and not frozenset("ab").isdisjoint("bc")
    and frozenset("ab").issubset("abc")
    and frozenset("abc").issuperset("ab")
)

key = frozenset([1, 2])
same_key = frozenset([2, 1])
mapping = {key: 42}
outer = {key, "x"}
hashable_ok = mapping[same_key] == 42 and same_key in outer and {1, 2} in outer

iterable_ok = (
    set(frozenset([1, 2, 1])) == {1, 2}
    and list(frozenset()) == []
    and tuple(frozenset()) == ()
    and len(list(frozenset([3, 4]))) == 2
    and set(list(frozenset([3, 4]))) == {3, 4}
)

errors_ok = True
try:
    frozenset([[]])
except TypeError:
    pass
else:
    errors_ok = False

try:
    frozenset(3)
except TypeError:
    pass
else:
    errors_ok = False

try:
    frozenset("ab") | "bc"
except TypeError:
    pass
else:
    errors_ok = False

try:
    "bc" | frozenset("ab")
except TypeError:
    pass
else:
    errors_ok = False

result = constructors_ok and equality_order_ok and operator_ok and method_ok and hashable_ok and iterable_ok and errors_ok
assert result
result
