fromkeys_default = dict.fromkeys(["a", "b", "a"]) == {"a": None, "b": None}
fromkeys_value = dict.fromkeys(("x", "y"), 7) == {"x": 7, "y": 7}
fromkeys_iterables = (
    dict.fromkeys("ab", 1) == {"a": 1, "b": 1}
    and dict.fromkeys(range(2), "r") == {0: "r", 1: "r"}
)

update_noarg_target = {"a": 1}
update_noarg_ret = update_noarg_target.update()
update_noarg_ok = update_noarg_ret is None and update_noarg_target == {"a": 1}

update_dict_target = {"a": 1, "b": 2}
update_dict_ret = update_dict_target.update({"b": 9, "c": 3})
update_dict_ok = (
    update_dict_ret is None
    and update_dict_target == {"a": 1, "b": 9, "c": 3}
)

update_pairs_target = {"a": 1}
update_pairs_ret = update_pairs_target.update([("b", 2), ["c", 3], "de", range(2)])
update_pairs_ok = (
    update_pairs_ret is None
    and update_pairs_target == {"a": 1, "b": 2, "c": 3, "d": "e", 0: 1}
)

errors_ok = True

try:
    dict.fromkeys(3)
except TypeError:
    pass
else:
    errors_ok = False

try:
    dict.fromkeys([[]])
except TypeError:
    pass
else:
    errors_ok = False

bad_update_noniterable = {}
try:
    bad_update_noniterable.update(3)
except TypeError:
    pass
else:
    errors_ok = False

bad_update_pair_type = {}
try:
    bad_update_pair_type.update([1])
except TypeError:
    pass
else:
    errors_ok = False

bad_update_pair_short = {}
try:
    bad_update_pair_short.update([("x",)])
except ValueError:
    pass
else:
    errors_ok = False

bad_update_pair_long = {}
try:
    bad_update_pair_long.update([("x", 1, 2)])
except ValueError:
    pass
else:
    errors_ok = False

bad_update_key = {}
try:
    bad_update_key.update([([], 1)])
except TypeError:
    pass
else:
    errors_ok = False

result = (
    fromkeys_default
    and fromkeys_value
    and fromkeys_iterables
    and update_noarg_ok
    and update_dict_ok
    and update_pairs_ok
    and errors_ok
)
assert result
result
