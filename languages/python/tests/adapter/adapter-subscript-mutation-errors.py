def boom():
    raise AssertionError


assign_target = [1, 2]
assign_oob = False
try:
    assign_target[2] = 9
except IndexError:
    assign_oob = assign_target == [1, 2]

assign_empty = []
assign_empty_oob = False
try:
    assign_empty[0] = 1
except IndexError:
    assign_empty_oob = assign_empty == []

aug_target = [1]
aug_oob = False
try:
    aug_target[1] += boom()
except IndexError:
    aug_oob = aug_target == [1]

del_target = [1, 2]
del_oob = False
try:
    del del_target[-3]
except IndexError:
    del_oob = del_target == [1, 2]

del_empty = []
del_empty_oob = False
try:
    del del_empty[0]
except IndexError:
    del_empty_oob = del_empty == []

del_dict = {"x": 1}
del_missing = False
try:
    del del_dict["y"]
except KeyError:
    del_missing = del_dict == {"x": 1}

aug_dict = {"x": 1}
aug_missing = False
try:
    aug_dict["y"] += boom()
except KeyError:
    aug_missing = aug_dict == {"x": 1}

aug_empty_dict = {}
aug_empty_missing = False
try:
    aug_empty_dict[0] += boom()
except KeyError:
    aug_empty_missing = aug_empty_dict == {}

result = (
    assign_oob
    and assign_empty_oob
    and aug_oob
    and del_oob
    and del_empty_oob
    and del_missing
    and aug_missing
    and aug_empty_missing
)
assert result
result
