left = {"a": 1, "b": 2}
right = {"b": 9, "c": 3}
merged = left | right
or_ok = (
    merged == {"a": 1, "b": 9, "c": 3}
    and left == {"a": 1, "b": 2}
    and right == {"b": 9, "c": 3}
)

empty_or_ok = ({} | {"x": 1}) == {"x": 1} and ({"x": 1} | {}) == {"x": 1}

inplace_dict_target = {"a": 1, "b": 2}
inplace_dict_target |= {"b": 9, "c": 3}
inplace_dict_ok = inplace_dict_target == {"a": 1, "b": 9, "c": 3}

inplace_pairs_target = {"a": 1}
inplace_pairs_target |= [("b", 2), ["c", 3], "de", range(2)]
inplace_pairs_ok = inplace_pairs_target == {"a": 1, "b": 2, "c": 3, "d": "e", 0: 1}

int_or_target = 5
int_or_target |= 8
int_or_ok = int_or_target == 13

errors_ok = True

try:
    {"a": 1} | [("b", 2)]
except TypeError:
    pass
else:
    errors_ok = False

try:
    [("a", 1)] | {"b": 2}
except TypeError:
    pass
else:
    errors_ok = False

bad_ior_noniterable = {}
try:
    bad_ior_noniterable |= 3
except TypeError:
    pass
else:
    errors_ok = False

bad_ior_pair_type = {}
try:
    bad_ior_pair_type |= [1]
except TypeError:
    pass
else:
    errors_ok = False

bad_ior_pair_short = {}
try:
    bad_ior_pair_short |= [("x",)]
except ValueError:
    pass
else:
    errors_ok = False

bad_ior_pair_long = {}
try:
    bad_ior_pair_long |= [("x", 1, 2)]
except ValueError:
    pass
else:
    errors_ok = False

bad_ior_key = {}
try:
    bad_ior_key |= [([], 1)]
except TypeError:
    pass
else:
    errors_ok = False

result = (
    or_ok
    and empty_or_ok
    and inplace_dict_ok
    and inplace_pairs_ok
    and int_or_ok
    and errors_ok
)
assert result
result
