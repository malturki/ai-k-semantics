data = {1, 2}
add_ret = data.add(3)
add_dup_ret = data.add(3)
discard_ret = data.discard(2)
discard_missing_ret = data.discard(99)
remove_ret = data.remove(1)
element_methods_ok = (
    add_ret is None
    and add_dup_ret is None
    and discard_ret is None
    and discard_missing_ret is None
    and remove_ret is None
    and data == {3}
)

clear_target = {1, 2}
clear_ret = clear_target.clear()
clear_ok = clear_ret is None and clear_target == set()

pop_data = {10, 20}
before_pop = pop_data.copy()
pop_first = pop_data.pop()
after_first = pop_data.copy()
pop_second = pop_data.pop()
pop_ok = (
    pop_first in before_pop
    and pop_first not in after_first
    and pop_second in before_pop
    and pop_second != pop_first
    and pop_data == set()
)

update_target = {1, 2}
update_empty_ret = update_target.update()
update_ret = update_target.update([2, 3], (4,), {5})
update_ok = (
    update_empty_ret is None
    and update_ret is None
    and update_target == {1, 2, 3, 4, 5}
)

intersection_empty = {1, 2}
intersection_empty_ret = intersection_empty.intersection_update()
intersection_target = {1, 2, 3, 4}
intersection_ret = intersection_target.intersection_update([2, 3, 4], (3, 4, 5))
intersection_ok = (
    intersection_empty_ret is None
    and intersection_empty == {1, 2}
    and intersection_ret is None
    and intersection_target == {3, 4}
)

difference_target = {1, 2, 3, 4}
difference_empty_ret = difference_target.difference_update()
difference_ret = difference_target.difference_update([2], {4}, ())
difference_ok = (
    difference_empty_ret is None
    and difference_ret is None
    and difference_target == {1, 3}
)

symmetric_target = {1, 2, 3}
symmetric_ret = symmetric_target.symmetric_difference_update([2, 4])
symmetric_ok = symmetric_ret is None and symmetric_target == {1, 3, 4}

mixed = {"a"}
mixed_update_ret = mixed.update({"b": 1}, "cd", range(1, 3))
filter_target = {"a", "b", "c"}
filter_ret = filter_target.intersection_update({"b": 1, "c": 2}, "bcde")
mixed_iterables_ok = (
    mixed_update_ret is None
    and mixed == {"a", "b", "c", "d", 1, 2}
    and filter_ret is None
    and filter_target == {"b", "c"}
)

temporary_ok = (
    ({1}).add(2) is None
    and ({1}).clear() is None
    and ({1, 2}).pop() in {1, 2}
)

errors_ok = True

try:
    set().pop()
except KeyError:
    pass
else:
    errors_ok = False

try:
    data.add([])
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.remove([])
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.discard([])
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.remove(404)
except KeyError:
    pass
else:
    errors_ok = False

try:
    data.update([[]])
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.update(3)
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.intersection_update(3)
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.symmetric_difference_update()
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.symmetric_difference_update([1], [2])
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.clear(1)
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.pop(1)
except TypeError:
    pass
else:
    errors_ok = False

try:
    set().difference_update(123)
except TypeError:
    pass
else:
    errors_ok = False

errors_ok = errors_ok and data == {3}

result = (
    element_methods_ok
    and clear_ok
    and pop_ok
    and update_ok
    and intersection_ok
    and difference_ok
    and symmetric_ok
    and mixed_iterables_ok
    and temporary_ok
    and errors_ok
)
assert result
result
