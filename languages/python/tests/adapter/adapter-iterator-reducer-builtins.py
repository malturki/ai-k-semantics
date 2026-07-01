result = True

all_it = iter([1, True, 0, 99])
result = result and all(all_it) == False
result = result and next(all_it) == 99
result = result and next(all_it, "done") == "done"

any_it = iter([0, False, "", 5, 6])
result = result and any(any_it) == True
result = result and next(any_it) == 6
result = result and any(any_it) == False

empty_all = iter([])
result = result and all(empty_all) == True
result = result and next(empty_all, 7) == 7

empty_any = iter([])
result = result and any(empty_any) == False
result = result and next(empty_any, 8) == 8

sum_it = iter([2, 3, 4])
result = result and sum(sum_it) == 9
result = result and next(sum_it, 10) == 10

sum_seed_it = iter([1, 2])
result = result and sum(sum_seed_it, 10) == 13
result = result and next(sum_seed_it, 11) == 11

sum_list_it = iter([[1], [2], [3]])
result = result and sum(sum_list_it, []) == [1, 2, 3]
result = result and next(sum_list_it, 12) == 12

sum_bad_start_it = iter([1])
bad_start = False
try:
    sum(sum_bad_start_it, "")
except TypeError:
    bad_start = True
result = result and bad_start
result = result and next(sum_bad_start_it) == 1

sum_bad_item_it = iter([1, "x", 3])
bad_item = False
try:
    sum(sum_bad_item_it)
except TypeError:
    bad_item = True
result = result and bad_item
result = result and next(sum_bad_item_it) == 3

source_all = iter([1, 0, 2])


def pull_all():
    return next(source_all)


callable_all = iter(pull_all, 99)
result = result and all(callable_all) == False
result = result and next(callable_all) == 2
result = result and next(callable_all, 13) == 13

source_any = iter([0, "", 4, 5])


def pull_any():
    return next(source_any)


callable_any = iter(pull_any, 99)
result = result and any(callable_any) == True
result = result and next(callable_any) == 5
result = result and next(callable_any, 14) == 14

source_sum = iter([3, 4, 99])


def pull_sum():
    return next(source_sum)


callable_sum = iter(pull_sum, 99)
result = result and sum(callable_sum) == 7
result = result and next(callable_sum, 15) == 15

source_stop_sum = iter([1, 2])


def pull_stop_sum():
    return next(source_stop_sum)


stop_sum = iter(pull_stop_sum, 99)
result = result and sum(stop_sum) == 3
result = result and next(stop_sum, 16) == 16

assert result
result
