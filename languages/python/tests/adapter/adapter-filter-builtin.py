def positive(x):
    return x > 0


def odd(x):
    return x % 2


def keep_pair(pair):
    return pair[0]


def boom(x):
    raise ValueError


result = list(filter(None, [0, 1, "", "x", [], [2], False, True, None])) == [1, "x", [2], True]
result = result and tuple(filter(odd, (0, 1, 2, 3))) == (1, 3)
result = result and list(filter(positive, [-1, 0, 2, 3])) == [2, 3]
result = result and list(filter(lambda b: b, b"\x00\x02")) == [2]
result = result and list(filter(lambda x: x > 2, range(0, 5))) == [3, 4]
result = result and list(filter(None, {0: "zero", 2: "two"})) == [2]
result = result and bool(filter(None, [])) == True

total = 0
for value in filter(lambda x: x > 1, [1, 2, 3]):
    total += value
result = result and total == 5

pairs_total = 0
for a, b in filter(keep_pair, [(0, 9), (2, 3)]):
    pairs_total += a * b
result = result and pairs_total == 6

marker = 0
for value in filter(None, [0, "", None]):
    marker = 99
else:
    marker = 7
result = result and marker == 7

constructed = False
try:
    candidate = filter(1, [2])
    constructed = bool(candidate)
except TypeError:
    constructed = False

bad_callable = False
try:
    list(filter(1, [2]))
except TypeError:
    bad_callable = True

bad_iterable = False
try:
    filter(None, 1)
except TypeError:
    bad_iterable = True

bad_arity_zero = False
try:
    filter()
except TypeError:
    bad_arity_zero = True

bad_arity_one = False
try:
    filter(None)
except TypeError:
    bad_arity_one = True

bad_arity_three = False
try:
    filter(None, [1], [2])
except TypeError:
    bad_arity_three = True

predicate_error = False
try:
    list(filter(boom, [1]))
except ValueError:
    predicate_error = True

result = (
    result
    and constructed
    and bad_callable
    and bad_iterable
    and bad_arity_zero
    and bad_arity_one
    and bad_arity_three
    and predicate_error
)
assert result
result
