def boom():
    raise AssertionError


string_index = False
try:
    "abc"[1.0]
except TypeError:
    string_index = True

bytes_index = False
try:
    b"a"["x"]
except TypeError:
    bytes_index = True

list_index = False
try:
    [1]["x"]
except TypeError:
    list_index = True

tuple_index = False
try:
    (1,)[None]
except TypeError:
    tuple_index = True

range_index = False
try:
    range(3)["x"]
except TypeError:
    range_index = True

dict_unhashable_lookup = False
try:
    {1: 2}[[]]
except TypeError:
    dict_unhashable_lookup = True

dict_tuple_missing = False
try:
    {1: 2}[(1, 2)]
except KeyError:
    dict_tuple_missing = True

dict_range_missing = False
try:
    {1: 2}[range(1)]
except KeyError:
    dict_range_missing = True

dict_slice_missing = False
try:
    {1: 2}[slice(0, 1)]
except KeyError:
    dict_slice_missing = True

assign_target = [1]
assign_bad_index = False
try:
    assign_target["x"] = 2
except TypeError:
    assign_bad_index = assign_target == [1]

dict_assign_target = {"x": 1}
dict_assign_bad_key = False
try:
    dict_assign_target[[]] = 2
except TypeError:
    dict_assign_bad_key = dict_assign_target == {"x": 1}

aug_target = [1]
aug_bad_index = False
try:
    aug_target["x"] += boom()
except TypeError:
    aug_bad_index = aug_target == [1]

dict_aug_target = {"x": 1}
dict_aug_bad_key = False
try:
    dict_aug_target[[]] += boom()
except TypeError:
    dict_aug_bad_key = dict_aug_target == {"x": 1}

del_target = [1]
del_bad_index = False
try:
    del del_target["x"]
except TypeError:
    del_bad_index = del_target == [1]

dict_del_target = {"x": 1}
dict_del_bad_key = False
try:
    del dict_del_target[[]]
except TypeError:
    dict_del_bad_key = dict_del_target == {"x": 1}

result = (
    string_index
    and bytes_index
    and list_index
    and tuple_index
    and range_index
    and dict_unhashable_lookup
    and dict_tuple_missing
    and dict_range_missing
    and dict_slice_missing
    and assign_bad_index
    and dict_assign_bad_key
    and aug_bad_index
    and dict_aug_bad_key
    and del_bad_index
    and dict_del_bad_key
)
assert result
result
