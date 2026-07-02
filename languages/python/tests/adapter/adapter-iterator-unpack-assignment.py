result = True

pair_it = iter([1, 2])
a, b = pair_it
result = result and a == 1 and b == 2
result = result and next(pair_it, 9) == 9

nested_it = iter([(3, 4), [5, 6]])
(c, d), [e, f] = nested_it
result = result and c == 3 and d == 4 and e == 5 and f == 6
result = result and next(nested_it, 10) == 10

star_it = iter([7, 8, 9, 10])
head, *middle, tail = star_it
result = result and head == 7 and middle == [8, 9] and tail == 10
result = result and next(star_it, 11) == 11

all_star_it = iter([12, 13])
*all_items, = all_star_it
result = result and all_items == [12, 13]
result = result and next(all_star_it, 14) == 14

empty_star_it = iter([])
*empty_items, = empty_star_it
result = result and empty_items == []
result = result and next(empty_star_it, 15) == 15

source_pair = iter([16, 17, 99])


def pull_pair():
    return next(source_pair)


callable_pair = iter(pull_pair, 99)
g, h = callable_pair
result = result and g == 16 and h == 17
result = result and next(callable_pair, 18) == 18

source_star = iter([19, 20, 21, 99])


def pull_star():
    return next(source_star)


callable_star = iter(pull_star, 99)
i, *j, k = callable_star
result = result and i == 19 and j == [20] and k == 21
result = result and next(callable_star, 22) == 22

too_few = iter([1])
too_few_seen = False
try:
    x, y = too_few
except ValueError:
    too_few_seen = True

too_many = iter([1, 2, 3])
too_many_seen = False
try:
    x, y = too_many
except ValueError:
    too_many_seen = True

star_too_few = iter([1])
star_too_few_seen = False
try:
    x, *y, z, w = star_too_few
except ValueError:
    star_too_few_seen = True

result = result and too_few_seen and too_many_seen and star_too_few_seen

assert result
result
