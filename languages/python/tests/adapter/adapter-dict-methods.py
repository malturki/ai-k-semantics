d = {"a": 1, "b": 2}

get_ok = (
    d.get("a") == 1
    and d.get("missing") is None
    and d.get("missing", 99) == 99
)

copy_source = {"a": 1, "b": 2}
copy_value = copy_source.copy()
copy_value["a"] = 9
copy_ok = copy_source == {"a": 1, "b": 2} and copy_value == {"a": 9, "b": 2}

clear_target = {"x": 1, "y": 2}
clear_ret = clear_target.clear()
clear_ok = clear_ret is None and clear_target == {}

pop_target = {"a": 1, "b": 2}
pop_a = pop_target.pop("a")
pop_missing = pop_target.pop("z", 99)
pop_ok = pop_a == 1 and pop_missing == 99 and pop_target == {"b": 2}

popitem_target = {"first": 1, "second": 2}
popitem_target["first"] = 3
popitem_value = popitem_target.popitem()
popitem_ok = popitem_value == ("second", 2) and popitem_target == {"first": 3}

setdefault_target = {"a": 1}
setdefault_existing = setdefault_target.setdefault("a", 7)
setdefault_missing_none = setdefault_target.setdefault("b")
setdefault_missing_value = setdefault_target.setdefault("c", 4)
setdefault_ok = (
    setdefault_existing == 1
    and setdefault_missing_none is None
    and setdefault_missing_value == 4
    and setdefault_target == {"a": 1, "b": None, "c": 4}
)

empty_get = {}
empty_setdefault = {}
empty_ok = (
    empty_get.get("x") is None
    and empty_get.get("x", 5) == 5
    and empty_setdefault.setdefault("x") is None
    and empty_setdefault == {"x": None}
)

errors_ok = True

empty_pop = {}
try:
    empty_pop.pop("missing")
except KeyError:
    pass
else:
    errors_ok = False

empty_popitem = {}
try:
    empty_popitem.popitem()
except KeyError:
    pass
else:
    errors_ok = False

try:
    d.get([])
except TypeError:
    pass
else:
    errors_ok = False

try:
    d.pop([])
except TypeError:
    pass
else:
    errors_ok = False

try:
    d.setdefault([])
except TypeError:
    pass
else:
    errors_ok = False

result = get_ok and copy_ok and clear_ok and pop_ok and popitem_ok and setdefault_ok and empty_ok and errors_ok
assert result
result
