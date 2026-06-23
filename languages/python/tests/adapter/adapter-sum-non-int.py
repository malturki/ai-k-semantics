result = sum([1.5, True]) == 2.5
result = result and sum([1, 2.5, 3j]) == 3.5 + 3j
result = result and sum([1], 0.5) == 1.5
result = result and sum([1, 2], 3j) == 3 + 3j
result = result and sum(range(2), 0.5) == 1.5
result = result and sum([], 1.5) == 1.5
result = result and sum([], 1j) == 1j
result = result and sum([], None) is None

result = result and sum([[1], [2]], []) == [1, 2]
result = result and sum([(1,), (2,)], ()) == (1, 2)
result = result and sum([], []) == []
result = result and sum([], ()) == ()
result = result and sum(range(0), []) == []

string_item = False
try:
    sum(["a"])
except TypeError:
    string_item = True

mixed_item = False
try:
    sum([1, "a"])
except TypeError:
    mixed_item = True

string_start = False
try:
    sum([], "")
except TypeError:
    string_start = True

bytes_start = False
try:
    sum([], b"")
except TypeError:
    bytes_start = True

bytes_item_and_start = False
try:
    sum([b"a"], b"")
except TypeError:
    bytes_item_and_start = True

none_item = False
try:
    sum([None])
except TypeError:
    none_item = True

list_without_start = False
try:
    sum([[1]])
except TypeError:
    list_without_start = True

result = (
    result
    and string_item
    and mixed_item
    and string_start
    and bytes_start
    and bytes_item_and_start
    and none_item
    and list_without_start
)
assert result
result
