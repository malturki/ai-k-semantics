binary_int = False
try:
    1 @ 2
except TypeError:
    binary_int = True

binary_float = False
try:
    1.0 @ 2.0
except TypeError:
    binary_float = True

binary_list = False
try:
    [1] @ [2]
except TypeError:
    binary_list = True

binary_string = False
try:
    "a" @ "b"
except TypeError:
    binary_string = True

name_aug = False
x = 5
try:
    x @= 2
except TypeError:
    name_aug = x == 5

list_aug = False
items = [3]
try:
    items[0] @= 4
except TypeError:
    list_aug = items == [3]

dict_aug = False
mapping = {"x": 3}
try:
    mapping["x"] @= 4
except TypeError:
    dict_aug = mapping == {"x": 3}

result = (
    binary_int
    and binary_float
    and binary_list
    and binary_string
    and name_aug
    and list_aug
    and dict_aug
)
assert result
result
