result = True

set_it = iter([3, 1, 2, 1])
result = result and set(set_it) == {1, 2, 3}
result = result and next(set_it, 9) == 9

empty_set_it = iter([])
result = result and set(empty_set_it) == set()
result = result and next(empty_set_it, 10) == 10

frozen_it = iter([2, 1, 2])
frozen = frozenset(frozen_it)
result = result and frozen == frozenset([1, 2])
result = result and next(frozen_it, 11) == 11

nested_it = iter([frozenset([1]), frozenset([1, 2]), frozenset([1])])
result = result and set(nested_it) == {frozenset([1]), frozenset([1, 2])}
result = result and next(nested_it, 12) == 12

source_set = iter([3, 1, 3, 99])


def pull_set():
    return next(source_set)


callable_set = iter(pull_set, 99)
result = result and set(callable_set) == {1, 3}
result = result and next(callable_set, 13) == 13

source_frozen = iter([4, 2, 4, 99])


def pull_frozen():
    return next(source_frozen)


callable_frozen = iter(pull_frozen, 99)
result = result and frozenset(callable_frozen) == frozenset([2, 4])
result = result and next(callable_frozen, 14) == 14

bad_set_it = iter([[1], 2])
bad_set_seen = False
try:
    set(bad_set_it)
except TypeError:
    bad_set_seen = True

bad_frozen_it = iter([[1], 2])
bad_frozen_seen = False
try:
    frozenset(bad_frozen_it)
except TypeError:
    bad_frozen_seen = True

result = result and bad_set_seen and bad_frozen_seen

assert result
result
