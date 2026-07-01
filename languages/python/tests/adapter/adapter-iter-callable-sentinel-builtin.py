result = True

source = iter([0, 1, 2, 3])


def pull():
    return next(source)


it = iter(pull, 3)
result = result and next(it) == 0
result = result and next(it) == 1
result = result and next(it) == 2

sentinel_stop_count = 0
try:
    next(it)
except StopIteration:
    sentinel_stop_count += 1
try:
    next(it)
except StopIteration:
    sentinel_stop_count += 1
result = result and sentinel_stop_count == 2
result = result and next(it, 99) == 99

source_list = iter([0, 1, 2, 3, 4])


def pull_list():
    return next(source_list)


list_it = iter(pull_list, 2)
result = result and list(list_it) == [0, 1]
result = result and list(list_it) == []
result = result and next(source_list) == 3

source_tuple = iter(["a", "b", "stop", "tail"])


def pull_tuple():
    return next(source_tuple)


tuple_it = iter(pull_tuple, "stop")
result = result and tuple(tuple_it) == ("a", "b")
result = result and tuple(tuple_it) == ()
result = result and next(source_tuple) == "tail"

source_natural_stop = iter([4, 5])


def pull_until_stop():
    return next(source_natural_stop)


natural_stop_it = iter(pull_until_stop, 99)
result = result and list(natural_stop_it) == [4, 5]
result = result and list(natural_stop_it) == []
result = result and next(natural_stop_it, 42) == 42

source_loop = iter([10, 20, 30])


def pull_loop():
    return next(source_loop)


loop_total = 0
for value in iter(pull_loop, 30):
    loop_total += value
else:
    loop_total += 100
result = result and loop_total == 130

source_break = iter([1, 2, 3, 4])


def pull_break():
    return next(source_break)


break_it = iter(pull_break, 4)
break_total = 0
for value in break_it:
    break_total += value
    if value == 2:
        break
result = result and break_total == 3
result = result and next(break_it) == 3
result = result and next(break_it, 55) == 55


def boom():
    raise RuntimeError


boom_it = iter(boom, 0)
boom_seen = False
try:
    next(boom_it)
except RuntimeError:
    boom_seen = True

boom_seen_again = False
try:
    next(boom_it)
except RuntimeError:
    boom_seen_again = True
result = result and boom_seen and boom_seen_again


def needs_arg(x):
    return x


arity_it = iter(needs_arg, 0)
arity_error = False
try:
    next(arity_it)
except TypeError:
    arity_error = True
result = result and arity_error

guard = iter([0])


def reentrant():
    if next(guard, 1) == 0:
        list(reentrant_it)
        return 1
    return 2


reentrant_it = iter(reentrant, 2)
reentrant_stopped = False
try:
    next(reentrant_it)
except StopIteration:
    reentrant_stopped = True

result = result and reentrant_stopped
result = result and next(reentrant_it, 77) == 77

assert result
result
